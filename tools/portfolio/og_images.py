"""Link-preview images (Open Graph / Twitter): 1200x630 JPEGs, kept small because WhatsApp drops previews over ~300 KB
and several apps show no preview for WebP.

- public/img/portfolio/<slug>/og.jpg for every published case study, centre-cropped from its 1600x900 cover;
- public/img/og/{default,portfolio,digital-marketing}.jpg, rendered from og/card.html with the text of each page's hero.

resources/js/data/seo.json and the /portfolio/{slug} route point at these files. Run after assemble_portfolio.py:
    python tools/portfolio/og_images.py
"""
import json
import subprocess
import urllib.parse
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "public"
RAW = ROOT / "tools" / "portfolio" / "raw" / "og"
CARD = (ROOT / "tools" / "portfolio" / "og" / "card.html").as_uri()
SIZE = (1200, 630)


def cover(slug):
    return (PUBLIC / "img" / "portfolio" / slug / "cover.webp").as_uri()


def mockup(brand, view):
    return (PUBLIC / "img" / "digital-marketing" / brand / f"{view}.webp").as_uri()


# Text and pills come from each page's hero (HeroSection.vue, Portfolio.vue + portfolioMeta.js categories,
# webDevelopmentServices.js), shortened to fit. The portfolio label gets its count in main().
CARDS = {
    "default": {
        "title": "A software development agency",
        "highlight": "that ships",
        "sub": "Web, mobile, desktop, APIs and agentic AI, built end to end.",
        "pills": ["E-commerce & Web Apps", "Mobile & Desktop Apps", "APIs & Backends", "Automation Pipelines",
                  "Agentic AI Systems"],
        "label": "Selected work",
        "images": [cover("selenix"), cover("element-140"), cover("babysleep")],
    },
    "portfolio": {
        "title": "Case studies",
        "highlight": "from the team that will build yours",
        "sub": "Products we have shipped and systems we have built. Every screenshot is real.",
        "pills": ["Web & SaaS", "Mobile", "Desktop", "AI & Automation", "Games", "APIs & Infrastructure"],
        "images": [cover(s) for s in ("selenix", "element-140", "ai-game-pipeline", "frenamies")],
    },
    "digital-marketing": {
        "title": "Digital Marketing & Growth",
        "sub": "Search, paid media, email and analytics, run by the same team that builds your site.",
        "pills": ["SEO", "Google Ads", "Meta Ads", "Email automation", "GA4 & CRO"],
        # The brands are fictional; the page labels them as examples, and so does the card.
        "label": "Example campaigns",
        "images": [mockup("kettlebird", "landing"), mockup("fernridge", "dashboard"), mockup("harborline", "ads")],
    },
}


def fit(im):
    """Centre-crop to 1200:630 (1.905:1), then resize to 1200x630."""
    w, h = im.size
    ratio = SIZE[0] / SIZE[1]
    if w / h > ratio:
        nw = round(h * ratio)
        im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = round(w / ratio)
        im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im.resize(SIZE, Image.LANCZOS)


def save_jpeg(im, path, limit_kb=200):
    """4:4:4 chroma keeps the small UI text in screenshots sharp; photo-like images that come out over the limit
    are saved again with 4:2:0, which they don't suffer from. Returns the size in KB."""
    path.parent.mkdir(parents=True, exist_ok=True)
    for subsampling in (0, 2):
        im.convert("RGB").save(path, "JPEG", quality=85, optimize=True, progressive=True, subsampling=subsampling)
        if path.stat().st_size <= limit_kb * 1024:
            break
    return path.stat().st_size // 1024


def main():
    projects = json.loads((ROOT / "resources" / "js" / "data" / "portfolio.json").read_text(encoding="utf-8"))
    for p in projects:
        src = PUBLIC / (p["cover"]["src"].lstrip("/") + ".webp")
        out = src.parent / "og.jpg"
        print(f"{out.relative_to(ROOT).as_posix()}: {save_jpeg(fit(Image.open(src)), out)} KB")

    CARDS["portfolio"]["label"] = f"{len(projects)} case studies"
    RAW.mkdir(parents=True, exist_ok=True)
    jobs = []
    for name, card in CARDS.items():
        params = {k: v for k, v in card.items() if k not in ("images", "pills")}
        params |= {"pills": "|".join(card.get("pills", [])), "images": ",".join(card["images"])}
        jobs.append({
            "url": CARD + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote),
            "out": str(RAW / f"{name}.png"),
            "selector": "#card",
            "waitFor": "body[data-ready='1']",
            "viewport": {"width": SIZE[0], "height": SIZE[1]},
            "scale": 2,
        })
    (RAW / "jobs.json").write_text(json.dumps(jobs, indent=1), encoding="utf-8")
    subprocess.run(["node", str(ROOT / "tools" / "portfolio" / "capture.mjs"), "jobs", str(RAW / "jobs.json")],
                   cwd=ROOT, check=True)
    for name in CARDS:
        out = PUBLIC / "img" / "og" / f"{name}.jpg"
        rendered = Image.open(RAW / f"{name}.png").resize(SIZE, Image.LANCZOS)  # captured at 2x for crisp text
        print(f"{out.relative_to(ROOT).as_posix()}: {save_jpeg(rendered, out)} KB")


if __name__ == "__main__":
    main()
