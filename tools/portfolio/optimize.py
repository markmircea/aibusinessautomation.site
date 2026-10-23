#!/usr/bin/env python3
"""Redact, crop and resize case-study screenshots to WebP (full + 800px variants)."""

import argparse
import json
import os
import sys

from PIL import Image, ImageFilter

DEFAULT_MAX_WIDTH = 1600
SMALL_WIDTH = 800


def pixelate(img, rect):
    """Blocky + blurred cover for sensitive regions (source pixel coordinates)."""
    x, y, w, h = rect
    w = min(w, img.width - x)
    h = min(h, img.height - y)
    if w <= 0 or h <= 0:
        return
    region = img.crop((x, y, x + w, y + h))
    block = region.resize((max(1, w // 24), max(1, h // 24)), Image.BILINEAR)
    block = block.resize((w, h), Image.NEAREST)
    block = block.filter(ImageFilter.GaussianBlur(6))
    img.paste(block, (x, y))


def centre_crop(img, ratio):
    try:
        cw, ch = (float(p) for p in ratio.split(":"))
        if cw <= 0 or ch <= 0:
            raise ValueError(ratio)
    except ValueError:
        raise ValueError("bad crop ratio: %s" % ratio)
    target = cw / ch
    if img.width / img.height > target:
        w = int(round(img.height * target))
        x = (img.width - w) // 2
        img = img.crop((x, 0, x + w, img.height))
    else:
        h = int(round(img.width / target))
        y = (img.height - h) // 2
        img = img.crop((0, y, img.width, y + h))
    return img


def shrink(img, width):
    if img.width <= width:
        return img  # never upscale
    h = int(round(img.height * width / img.width))
    return img.resize((width, h), Image.LANCZOS)


def process(job):
    src = job["src"]
    name = job["name"]
    out_dir = job["out_dir"]
    os.makedirs(out_dir, exist_ok=True)

    img = Image.open(src)
    has_alpha = img.mode in ("RGBA", "LA") or "transparency" in img.info
    img = img.convert("RGBA" if has_alpha else "RGB")
    img.info = {}  # keep EXIF/metadata out of the output
    img.load()

    for rect in job.get("blur", []):
        pixelate(img, rect)
    for x, y, w, h, color in job.get("fill", []):
        # Paint a region out entirely (logos, names). "auto" samples the pixel just above-left of the region.
        if color == "auto":
            color = img.getpixel((max(0, x - 2), max(0, y - 2)))
        img.paste(color, (x, y, x + w, y + h))
    if job.get("crop"):
        img = centre_crop(img, job["crop"])

    big = shrink(img, int(job.get("max_width", DEFAULT_MAX_WIDTH)))
    small = shrink(img, SMALL_WIDTH)

    big_path = os.path.join(out_dir, "%s.webp" % name)
    small_path = os.path.join(out_dir, "%s-800.webp" % name)
    for path, im in ((big_path, big), (small_path, small)):
        im.save(path, "WEBP", quality=82, method=6)
        print("%s  %dx%d  %d KB" % (path, im.width, im.height, os.path.getsize(path) // 1024))

    return {"name": name, "src": src, "file": big_path, "file_800": small_path,
            "width": big.width, "height": big.height}


def main():
    ap = argparse.ArgumentParser(description="Screenshots -> WebP (with redaction/crop)")
    ap.add_argument("--jobs", required=True, help="jobs json file")
    ap.add_argument("--manifest", help="optional manifest json to write")
    args = ap.parse_args()

    with open(args.jobs, "r", encoding="utf-8") as fh:
        jobs = json.load(fh)

    entries, errors, files, total = [], [], 0, 0
    for job in jobs:
        if not os.path.exists(job["src"]):
            errors.append("missing src: %s" % job["src"])
            continue
        try:  # one bad job must not lose the rest of the batch
            entries.append(process(job))
        except Exception as exc:  # noqa: BLE001 - report and carry on
            errors.append("%s: %s" % (job["src"], exc))

    for entry in entries:
        for key in ("file", "file_800"):
            files += 1
            total += os.path.getsize(entry[key])
    print("TOTAL %d files %d KB" % (files, total // 1024))

    if args.manifest:
        out_dir = os.path.dirname(os.path.abspath(args.manifest))
        os.makedirs(out_dir, exist_ok=True)
        with open(args.manifest, "w", encoding="utf-8") as fh:
            json.dump(entries, fh, indent=2)

    for err in errors:
        print(err, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
