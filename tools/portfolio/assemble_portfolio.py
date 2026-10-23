#!/usr/bin/env python3
"""Builds resources/js/data/portfolio.json from the edited copy (copy JSON) and the media list below.

Text comes from the copy file (one object per case study, without images). Images are declared here, next to the
alt text and captions, and their width/height are read from the exported WebP files so they can never drift.
Unpublished case studies go to tools/portfolio/drafts.json instead, so nothing that is not cleared reaches the JS
bundle; their images wait in tools/portfolio/raw/staged/<slug>/ (git-ignored) rather than in public/.

    python tools/portfolio/assemble_portfolio.py [copy.json]

Without an argument the text is taken from the current portfolio.json and drafts.json, so after editing the copy
there (or a caption here) a plain run rebuilds both files.
"""
import json
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PUBLIC = os.path.join(ROOT, "public")
OUT = os.path.join(ROOT, "resources", "js", "data", "portfolio.json")
DRAFTS = os.path.join(ROOT, "tools", "portfolio", "drafts.json")
STAGED = os.path.join(ROOT, "tools", "portfolio", "raw", "staged")
KEY_ORDER = ["slug", "name", "tagline", "summary", "engagement", "status", "categories", "timeline", "role",
             "platforms", "stack", "challenge", "built", "results", "nextSteps", "diagram", "cover", "gallery",
             "videos", "links", "featured", "published", "order"]

# slug -> cover (name, alt), diagram (alt, caption) or None, gallery [(name, alt, caption)],
# videos [(file name without .mp4, title, caption)] with a <name>-poster.webp next to each video.
MEDIA = {
    "selenix": {
        "cover": ("cover", "The Selenix IDE after a scraping test run, with the books.toscrape.com catalogue page it visited"),
        "diagram": ("Selenix architecture: the desktop IDE with its AI assistant, automation engine and MCP bridge, "
                    "connected to the AI proxy, selenix.io and two browser backends",
                    "The AI assistant drives the same engine you use by hand; the cloud side handles accounts, plans and AI access."),
        "gallery": [
            ("ide-run", "Selenix test editor with every step of a scraping test marked as passed and the run log below",
             "A finished run: each step passes and the log shows what the scraper found."),
            ("playback", "The books.toscrape.com catalogue page opened by a Selenix test during playback",
             "Playback drives a real browser page, here the practice catalogue the demo scrapes."),
            ("scheduler", "Selenix scheduling dialog for running a test once or on a recurring schedule",
             "Tests can run once or on an hourly, daily, weekly or monthly schedule."),
            ("ai-assistant", "The Selenix AI assistant panel next to a test, ready for a plain-English request",
             "The AI assistant lives next to the test it is editing."),
            ("selenix-io", "The selenix.io home page: AI-powered browser automation, zero code required",
             "selenix.io sells and licenses the app: accounts, plans and downloads."),
        ],
    },
    "selenix-mcp-server": {
        "cover": ("cover", "A Claude Code session calling Selenix MCP tools to list tests, run one and read its results"),
        "diagram": ("How an MCP client reaches Selenix: stdio to the MCP server, HTTP with a token to the app's local "
                    "bridge, then the session controllers and the browser",
                    "Every tool call is a local HTTP request to the running Selenix app."),
        "gallery": [
            ("ide-after-run", "Selenix showing the test Claude started over MCP, with every step passed",
             "The same run, seen in Selenix: Claude started it through the MCP server."),
            ("npm-package", "The @selenix/mcp-server page on npm: version 1.0.7, public, with the install command",
             "Published on npm, so any MCP client can install it with one command."),
        ],
    },
    "element-140": {
        "cover": ("cover", "A garden atrium inside the underground colony, with trees in round planters under a hexagonal skylight"),
        "diagram": None,
        "gallery": [
            ("atrium-spiral", "The spiral staircase winding around its central column through several decks of the colony "
                              "shaft, past lit walkways, fan housings and a garden deck",
             "The spiral stair from the side: one continuous staircase climbs the 103-meter shaft."),
            ("shaft-from-above", "Looking down the colony shaft: the spiral stair winding down past several decks and walkways",
             "The spiral stair from the top of the shaft, turning down through the decks."),
            ("spiral-stair", "First-person view straight down the spiral stair's well, with lamps on the landings",
             "Straight down the stair: one continuous spiral links all ten decks."),
            ("canteen", "A canteen hall with rows of tables under a hexagonal skylight and wide misty windows",
             "Lived-in spaces make the colony feel inhabited before the fighting starts."),
            ("arena", "An indoor football pitch built into the colony under a skylight",
             "A sports hall carved into the rock, two decks tall."),
            ("colonnade", "A curved colonnade walkway with round windows, lamps and planters along the shaft",
             "The ring walkways that circle the shaft on every deck."),
            ("control-room", "A control room with rows of consoles under a large glowing world map",
             "Set dressing that carries the story without a single line of dialog."),
            ("sky-lounge", "A lounge with neon wall lights facing a large window showing a cloudy sky",
             "A lounge with a screen of open sky, deep underground."),
            ("garden-deck", "A garden deck at night with a lit red-leaf tree behind red scaffolding",
             "Lighting does most of the storytelling on the garden decks."),
            ("dome", "Looking up at a blue glass dome with concrete ribs and ceiling lights",
             "The dome at the top of the shaft."),
            ("mech-dog", "The Mech Dog enemy, a four-legged robot with a mounted gun, in a studio render",
             "The Mech Dog enemy: 48 rigid parts on 38 bones, built for part-by-part damage."),
            ("mech-dog-exploded", "Exploded view of the Mech Dog showing its separate armor, gun and leg parts",
             "Every part can break off as physics debris when it is shot."),
            ("mech-trooper", "The Mech Trooper, a humanoid robot soldier with a red visor, aiming its rifle",
             "The Mech Trooper, the second machine enemy, with armor generated part by part."),
        ],
    },
    "ai-game-pipeline": {
        "cover": ("cover", "Side by side: the concept image of the robot dog and the finished 3D model rendered in Blender"),
        "diagram": ("The asset pipeline from concept art through 3D mesh, textures and headless Blender to the Unreal Editor and automated tests",
                    "Each stage hands a file to the next; nothing reaches a playtest without passing the self-tests."),
        "gallery": [
            ("texturing-bake-off", "Three renders of the robot dog: the concept, a procedural PBR texture and an AI-painted texture",
             "A bake-off between two texturing routes before committing to one."),
            ("review-sheet", "A grid of review renders of the robot dog from many angles, intact and damaged",
             "The review sheet a person signs off before the model goes into the engine."),
            ("damage-states", "The robot dog rendered with damaged parts",
             "Damage states are part of the model contract, not an afterthought."),
            ("trooper-concepts", "Four AI-generated concept images of a humanoid robot soldier with a red visor and a rifle",
             "Mech Trooper concepts: four directions explored with FLUX.2 before one was picked."),
            ("trooper-concept-vs-final", "Side by side: the picked Mech Trooper concept and the finished 3D model",
             "From the picked concept to the finished model."),
            ("trooper-parts", "Three views of the Mech Trooper's helmet, a generated armor part with a red visor slit",
             "The armor is generated part by part: one image per part, then a textured mesh fitted to the skeleton."),
            ("trooper-final", "Three renders of the finished Mech Trooper: the inner frame, the armored body and an aiming pose",
             "The finished Mech Trooper: inner frame, armor and an aiming pose."),
            ("trooper-animation", "Four frames of the Mech Trooper walking forward with its rifle raised",
             "A retargeted walk, checked frame by frame before it goes into the engine."),
            ("prop-reference-to-mesh", "A stone portal: the AI reference image next to four views of the generated, textured 3D mesh",
             "A prop from one command: reference image in, textured and engine-ready mesh out."),
        ],
    },
    "zombie-stick-kill": {
        "cover": ("cover", "Top-down Zombie Stick Kill gameplay: the player fighting a wave of zombies among barrels and fences"),
        "diagram": ("How the game runs on Reddit: the post opens the Phaser client, which talks to an Express server "
                    "with Redis on Reddit's serverless runtime",
                    "Scores are checked on the server before they reach the leaderboard."),
        "gallery": [
            ("gameplay", "Top-down gameplay with zombies, blood splatter, barrels and the score panel",
             "Waves get faster and denser every level."),
            ("title-screen", "Zombie Stick Kill title screen with a zombie horde silhouette, how-to-play and leaderboard panels",
             "Title screen from a local test build, so the leaderboard panel is empty; live scores are stored on Reddit."),
            ("wave-start", "A wave-start banner reading Wave 1, Fight",
             "Short, punchy wave banners keep the pace up."),
            ("reddit-app-page", "Zombie Stick Kill's page on Reddit's developer platform, with the game's description and readme",
             "The game's page on Reddit's developer platform."),
        ],
    },
    "frenamies": {
        "cover": ("cover", "Three phone screens from the game: an action card with a timer, the Wheel of Fate mini-game and a question card"),
        "diagram": ("Frenamies architecture: a content pipeline feeds bundled decks to the draw engine, mini-games and "
                    "stores, with optional subscription, analytics and crash-reporting services",
                    "Every service is optional: the game runs offline even with none of them configured."),
        "gallery": [
            ("mini-games-and-dares", "A two-player reaction-duel mini-game and two light dare cards with the players' names filled in",
             "Mini-games play inside the card, and players' names are filled into every prompt."),
        ],
    },
    "babysleep": {
        "cover": ("cover", "Three phone screens from BabySleep: creating a family, the SweetSpot prediction on the home screen and the weekly sleep report"),
        "diagram": ("BabySleep architecture: an installable web app and its Android package sync with an Express API, "
                    "which runs the SweetSpot engine and reminders over MySQL",
                    "The prediction runs on the server, so every caregiver's phone shows the same answer."),
        "gallery": [
            ("home-and-invite", "The home screen with today's sleep totals, and the family code screen for inviting a caregiver",
             "Totals for today, and a short code to invite a second caregiver. Shown with demo data."),
            ("settings", "BabySleep settings on a phone: this device's caregiver name, SweetSpot notifications, and the baby's name and date of birth",
             "Each phone names its caregiver and opts in to reminders. Demo data."),
        ],
    },
    "easyace": {
        "cover": ("cover", "The easyace.ai landing page with model prices and calls to try the studio or read the API docs"),
        "diagram": ("easyace.ai architecture: studio and API clients call a FastAPI app with PostgreSQL, whose GPU queue "
                    "drives ComfyUI and a local LLM",
                    "One queue in front of one GPU, grouped by model so jobs rarely wait for a reload."),
        "gallery": [
            ("api-docs", "The easyace.ai API documentation page with quick start, authentication and generation sections",
             "An OpenAI-style API with its own documentation."),
        ],
    },
    "local-ai-inference": {
        "cover": ("cover", "Benchmark chart comparing generation speed and prompt-reading time of four model configurations on one RTX 5090"),
        "diagram": ("Inside Strata: always-used layers and an adaptive expert cache on the GPU, all 24,576 experts pinned in "
                    "RAM, an n-gram table on the SSD, and guess-then-check decoding",
                    "How Strata fits a 125B model on one card, from its documentation; the speeds on this page are our own measurements."),
        "gallery": [
            ("monitor", "Strata's monitor on our RTX 5090: decode and prefill speed, 30.7 of 32 GB VRAM with 5,523 experts cached, "
                        "PCIe Gen5, and recent requests with 80 to 86 percent VRAM hit rates",
                        "Live telemetry during a coding-agent session: 32K-token prompts, most expert reads served from VRAM."),
            ("gpu-gate", "A GPU gate in front of two local model engines on one RTX 5090, handing the GPU to the image "
                         "service when a customer job arrives",
                         "The gate we wrote: customer jobs on our generation service always come first."),
        ],
    },
    "match-recap-videos": {
        "cover": ("cover", "Three phone screens showing frames of a generated match-recap video, with demo fixtures: the score and a match-minute ring"),
        "diagram": ("The recap pipeline: video plates generated once per template, then each match composited from "
                    "match data and a player photo",
                    "The expensive diffusion work happens once; each match is composited."),
        "gallery": [
            ("diffusion-background", "An AI-generated stadium at night with floodlights and a crowd, used as a video plate",
             "One of the cached diffusion plates every recap is built on."),
            ("more-matches", "Three phone screens from recaps of other demo matches, each with its score and match-minute ring over a stadium plate",
             "The same template across different matches and team colors. Demo fixtures and scores."),
        ],
        "videos": [
            ("recap", "Two-player match recap, Romania against Italy, 10 seconds",
             "A complete recap from the two-player template: the score counts up goal by goal over AI-generated stadium "
             "plates. Demo fixture and score."),
            ("recap-ai-closing", "One-player match recap, Spain against Greece, with an AI-animated closing shot",
             "The one-player variant: the closing seconds animate the player photo with Wan2.1 image-to-video. "
             "Demo fixture and score."),
        ],
    },
    "translation-api-platform": {
        "cover": ("cover", "The platform's authoring screen: a content-generation prompt above a source and translation editor"),
        "diagram": ("The platform: a web client and API customers call the translation API and the file workflow API, "
                    "backed by GPU machine-translation engines, an LLM and storage",
                    "Two FastAPI services share the work: instant text and generation, and file jobs."),
        "gallery": [
            ("sign-in", "The Xtensos platform sign-in screen with single sign-on",
             "Sign-in with Microsoft Entra ID single sign-on, or a password and a one-time code."),
            ("quick-translate", "Quick-translate screen with language pickers, machine-translation options and an AI enhance control",
             "Quick translation with optional AI post-editing."),
            ("translation-jobs", "Translation jobs list with status, source and target languages",
             "File jobs are split per file and target language and tracked to completion."),
            ("translation-memories", "Translation memory settings with a TMX upload form and memories grouped by tag",
             "Translation memories and terminology are managed per customer."),
        ],
    },
    "project-adam": {
        "cover": ("cover", "The Project ADAM website home page"),
        "diagram": ("How Project ADAM answers: an agent searches reviewed knowledge in Qdrant and MySQL; contributions "
                    "are voted on and approved by a moderator before analysis",
                    "Only knowledge a moderator approved is searchable."),
        "gallery": [
            ("roadmap", "Project ADAM roadmap page showing the current phase, the community knowledge pipeline",
             "The current phase is the knowledge pipeline described here."),
            ("contribute", "Project ADAM contribute page with volunteer roles for compute and storage",
             "The website explains the project and collects volunteer sign-ups."),
        ],
    },
}


def image(slug, name, alt, caption=None):
    rel = f"/img/portfolio/{slug}/{name}"
    path = os.path.join(PUBLIC, "img", "portfolio", slug, name + ".webp")
    if not os.path.isfile(path):
        path = os.path.join(STAGED, slug, name + ".webp")
    with Image.open(path) as im:
        w, h = im.size
    out = {"src": rel, "alt": alt}
    if caption is not None:
        out["caption"] = caption
    out.update({"width": w, "height": h})
    return out


def video(slug, name, title, caption):
    """A published MP4 and its poster; the size comes from the poster, which is a full-size frame."""
    base = f"/img/portfolio/{slug}/{name}"
    with Image.open(os.path.join(PUBLIC, "img", "portfolio", slug, name + "-poster.webp")) as im:
        w, h = im.size
    if not os.path.isfile(os.path.join(PUBLIC, "img", "portfolio", slug, name + ".mp4")):
        raise FileNotFoundError(base + ".mp4")
    return {"src": base + ".mp4", "poster": base + "-poster.webp", "title": title, "caption": caption,
            "width": w, "height": h}


def main(copy_path=None):
    if copy_path:
        projects = json.load(open(copy_path, encoding="utf-8"))
    else:
        projects = json.load(open(OUT, encoding="utf-8"))
        if os.path.isfile(DRAFTS):
            projects += json.load(open(DRAFTS, encoding="utf-8"))
        projects.sort(key=lambda p: p.get("order", 99))
    built = []
    for p in projects:
        m = MEDIA.get(p["slug"], {})
        if m.get("cover"):
            p["cover"] = image(p["slug"], *m["cover"])
        else:
            p.setdefault("cover", None)
        if m.get("diagram"):
            alt, caption = m["diagram"]
            p["diagram"] = image(p["slug"], "diagram", alt, caption)
        else:
            p.setdefault("diagram", None)
        p["gallery"] = [image(p["slug"], *g) for g in m.get("gallery", [])] if m else p.get("gallery", [])
        p["videos"] = [video(p["slug"], *v) for v in m.get("videos", [])]
        built.append({k: p[k] for k in KEY_ORDER if k in p})
    for path, items in ((OUT, [p for p in built if p.get("published")]),
                        (DRAFTS, [p for p in built if not p.get("published")])):
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"wrote {os.path.relpath(path, ROOT)}: {len(items)} case studies")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
