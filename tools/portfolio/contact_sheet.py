#!/usr/bin/env python3
"""Build numbered contact sheets so screenshots can be picked by number."""

import argparse
import glob
import os
import sys

from PIL import Image, ImageDraw, ImageFont

INK = "#0B1020"
SURFACE = "#141A2E"
EXTS = (".png", ".jpg", ".jpeg", ".webp")
GAP = 12
MARGIN = 12
LABEL_H = 34
MAX_NAME = 44


def load_font():
    try:
        return ImageFont.truetype("arial.ttf", 16)
    except OSError:
        return ImageFont.load_default()


def fit(img, box_w, box_h):
    """Letterbox img into a box_w x box_h tile on the surface colour."""
    img.thumbnail((box_w, box_h), Image.LANCZOS)
    tile = Image.new("RGB", (box_w, box_h), SURFACE)
    tile.paste(img, ((box_w - img.width) // 2, (box_h - img.height) // 2))
    return tile


def main():
    ap = argparse.ArgumentParser(description="Contact sheets for screenshot picking")
    ap.add_argument("--glob", required=True, help='image glob, e.g. "shots/**/*.png"')
    ap.add_argument("--out", required=True, help="output folder for the sheets")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--rows", type=int, default=3)
    ap.add_argument("--thumb", type=int, default=480, help="tile width in px")
    args = ap.parse_args()
    if min(args.cols, args.rows, args.thumb) < 1:
        ap.error("--cols, --rows and --thumb must be positive")

    paths = sorted(
        p for p in glob.glob(args.glob, recursive=True) if p.lower().endswith(EXTS)
    )
    if not paths:
        print("no images matched: %s" % args.glob, file=sys.stderr)
        return 1

    font = load_font()
    box_h = args.thumb * 9 // 16
    tile_w = args.thumb
    tile_h = box_h + LABEL_H
    per_sheet = max(1, args.cols * args.rows)
    os.makedirs(args.out, exist_ok=True)

    index_lines = []
    sheet_no = 0
    for start in range(0, len(paths), per_sheet):
        chunk = paths[start:start + per_sheet]
        rows = (len(chunk) + args.cols - 1) // args.cols
        w = MARGIN * 2 + args.cols * tile_w + (args.cols - 1) * GAP
        h = MARGIN * 2 + rows * tile_h + (rows - 1) * GAP
        sheet = Image.new("RGB", (w, h), INK)  # the label strip is the page background
        draw = ImageDraw.Draw(sheet)

        for i, path in enumerate(chunk):
            n = start + i + 1
            with Image.open(path) as im:
                src_w, src_h = im.size
                tile = fit(im.convert("RGB"), tile_w, box_h)
            sheet.paste(tile, (MARGIN + (i % args.cols) * (tile_w + GAP),
                               MARGIN + (i // args.cols) * (tile_h + GAP)))

            name = os.path.basename(path)
            if len(name) > MAX_NAME:
                name = name[:MAX_NAME - 1] + "…"
            draw.text((MARGIN + (i % args.cols) * (tile_w + GAP) + 6,
                       MARGIN + (i // args.cols) * (tile_h + GAP) + box_h + (LABEL_H - 16) // 2),
                      "#%03d  %s" % (n, name), fill="white", font=font)
            index_lines.append("#%03d\t%s\t%dx%d" % (n, os.path.abspath(path), src_w, src_h))

        sheet_no += 1
        sheet.save(os.path.join(args.out, "sheet_%02d.png" % sheet_no))

    with open(os.path.join(args.out, "index.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(index_lines) + "\n")

    print("%d images -> %d sheets in %s" % (len(paths), sheet_no, args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
