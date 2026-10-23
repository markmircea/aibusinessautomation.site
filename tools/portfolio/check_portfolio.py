#!/usr/bin/env python3
"""Integrity check for resources/js/data/portfolio.json before publishing.

Checks every case study's required fields and text limits, that each image (cover, diagram, gallery) exists as
<src>.webp and <src>-800.webp with the declared size and alt text, the image weight budget, the link-preview images
(each case study's og.jpg and those in seo.json), and that no confidential string appears in the JSON.
Exits 1 on any error.

    python tools/portfolio/check_portfolio.py
"""
import json
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, "resources", "js", "data", "portfolio.json")
SEO = os.path.join(ROOT, "resources", "js", "data", "seo.json")
PUBLIC = os.path.join(ROOT, "public")
OG_SIZE = (1200, 630)
OG_MAX_KB = 300  # WhatsApp drops link previews whose image is bigger

REQUIRED = ["slug", "name", "tagline", "summary", "engagement", "status", "categories", "timeline", "role",
            "platforms", "stack", "challenge", "built", "results", "nextSteps", "diagram", "cover", "gallery",
            "links", "featured", "published", "order"]
ENGAGEMENTS = {"In-house product", "Client engagement"}
STATUSES = {"Live", "Shipped", "In development"}
CATEGORIES = {"web", "mobile", "desktop", "ai", "games", "apis"}
# Never publish: hosts, local paths, retired claims, filler (case-insensitive). Names of clients, tenants and
# people are kept out of the repo: one per line in tools/portfolio/raw/forbidden.txt (git-ignored), read if present.
FORBIDDEN = ["go.ro", "192.168.", "0.0.0.0", "localhost:", "127.0.0.1", "c:\\", "c:/", "135+", "2,500+", "lorem", "todo"]
_PRIVATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw", "forbidden.txt")
if os.path.isfile(_PRIVATE):
    FORBIDDEN += [w.strip().lower() for w in open(_PRIVATE, encoding="utf-8") if w.strip()]
HYPE = ["revolutionary", "cutting-edge", "state-of-the-art", "seamless", "robust", "leverage", "unlock", "empower",
        "game-changer", "best-in-class", "world-class", "synergy", "innovative", "effortless", "supercharge", "harness"]


def check_image(slug, what, img, errors, sizes):
    if not img.get("alt", "").strip():
        errors.append(f"{slug}: {what} has no alt text")
    for suffix in ("", "-800"):
        path = os.path.join(PUBLIC, img["src"].lstrip("/").replace("/", os.sep) + suffix + ".webp")
        if not os.path.isfile(path):
            errors.append(f"{slug}: missing {os.path.relpath(path, ROOT)}")
            continue
        if suffix == "":
            sizes.append(os.path.getsize(path))
            with Image.open(path) as im:
                if (im.width, im.height) != (img.get("width"), img.get("height")):
                    errors.append(f"{slug}: {what} declares {img.get('width')}x{img.get('height')}, file is {im.width}x{im.height}")


def check_og(src, what, errors):
    """A link-preview image made by og_images.py: a 1200x630 JPEG small enough for WhatsApp."""
    path = os.path.join(PUBLIC, src.lstrip("/").replace("/", os.sep))
    if not os.path.isfile(path):
        errors.append(f"{what}: missing share image {os.path.relpath(path, ROOT)} (run og_images.py)")
        return
    with Image.open(path) as im:
        if im.format != "JPEG" or im.size != OG_SIZE:
            errors.append(f"{what}: share image {src} is {im.format} {im.width}x{im.height}, expected JPEG 1200x630")
    if os.path.getsize(path) > OG_MAX_KB * 1024:
        errors.append(f"{what}: share image {src} is {os.path.getsize(path) // 1024} KB (max {OG_MAX_KB})")


def main():
    projects = json.load(open(DATA, encoding="utf-8"))
    errors, warnings, sizes = [], [], []
    seen = set()
    for p in projects:
        slug = p.get("slug", "?")
        for key in REQUIRED:
            if key not in p:
                errors.append(f"{slug}: missing key {key}")
        if slug in seen:
            errors.append(f"duplicate slug {slug}")
        seen.add(slug)
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            errors.append(f"{slug}: slug must be lowercase letters, digits and dashes")
        if len(p.get("summary", "")) > 160:
            errors.append(f"{slug}: summary is {len(p['summary'])} characters (max 160)")
        if len(p.get("tagline", "")) > 90:
            errors.append(f"{slug}: tagline is {len(p['tagline'])} characters (max 90)")
        if p.get("engagement") not in ENGAGEMENTS:
            errors.append(f"{slug}: engagement {p.get('engagement')!r}")
        if p.get("status") not in STATUSES:
            errors.append(f"{slug}: status {p.get('status')!r}")
        if set(p.get("categories", [])) - CATEGORIES:
            errors.append(f"{slug}: unknown categories {set(p['categories']) - CATEGORIES}")
        if not p.get("results") and not p.get("nextSteps"):
            warnings.append(f"{slug}: neither results nor next steps")
        if p.get("published") and not p.get("cover"):
            warnings.append(f"{slug}: published without a cover image")
        for what in ("cover", "diagram"):
            if p.get(what):
                check_image(slug, what, p[what], errors, sizes)
        if p.get("cover"):
            check_og(p["cover"]["src"].rsplit("/", 1)[0] + "/og.jpg", slug, errors)
        for i, img in enumerate(p.get("gallery", [])):
            check_image(slug, f"gallery[{i}]", img, errors, sizes)
            if not img.get("caption", "").strip():
                warnings.append(f"{slug}: gallery[{i}] has no caption")
        for link in p.get("links", []):
            if not link.get("href", "").startswith("https://"):
                errors.append(f"{slug}: link {link.get('href')!r} is not https")

    seo = json.load(open(SEO, encoding="utf-8"))
    for key, page in [("default", seo)] + list(seo["pages"].items()):
        if page.get("image"):
            check_og(page["image"]["src"], f"seo.json {key}", errors)

    text = open(DATA, encoding="utf-8").read().lower()
    for word in FORBIDDEN:
        # whole words for names (a name must not match inside a longer word), plain substrings for hosts and paths
        hit = re.search(r"\b" + re.escape(word) + r"\b", text) if word.isalpha() else word in text
        if hit:
            errors.append(f"forbidden string in portfolio.json: {word!r}")
    for word in HYPE:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            warnings.append(f"hype word in portfolio.json: {word!r}")

    if sizes:
        avg = sum(sizes) / len(sizes) / 1024
        total = sum(sizes) / 1024 / 1024
        print(f"{len(projects)} case studies, {len(sizes)} full-size images, average {avg:.0f} KB, total {total:.1f} MB")
        if avg > 250:
            errors.append(f"average full-size image is {avg:.0f} KB (budget 250 KB)")
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
