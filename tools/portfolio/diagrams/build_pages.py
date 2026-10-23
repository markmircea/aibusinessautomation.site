"""Writes one HTML page per case-study diagram from the data below (renderer: diagram.js / diagram.css)."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

DIAGRAMS = {
    "selenix": {
        "eyebrow": "How it works",
        "title": "Selenix: an AI assistant on top of a browser-automation engine",
        "columns": [
            {"nodes": [
                {"id": "user", "icon": "user", "title": "You", "text": "Describe the job in plain English"},
                {"id": "mcpc", "icon": "plug", "title": "MCP clients", "text": "Claude Desktop, Claude Code or any MCP client"},
            ]},
            {"label": "Desktop IDE (Electron)", "width": 1.35, "nodes": [
                {"id": "ai", "icon": "bot", "accent": True, "title": "AI assistant",
                 "text": "Writes the steps, runs them, reads the results and fixes what failed",
                 "chips": ["Tool-calling loop", "Auto-run"]},
                {"id": "engine", "icon": "workflow", "title": "Automation engine",
                 "text": "114 commands for browsing, scraping, files, HTTP and email",
                 "chips": ["Scheduler", "Code export"]},
                {"id": "bridge", "icon": "lock", "title": "MCP bridge", "text": "Localhost only, new token on every launch"},
            ]},
            {"nodes": [
                {"id": "proxy", "icon": "cpu", "title": "AI proxy", "text": "OpenAI-compatible endpoint, keys issued per user"},
                {"id": "site", "icon": "server", "title": "selenix.io",
                 "text": "Accounts, PayPal plans, licence keys, daily AI quotas, templates",
                 "chips": ["Laravel", "Filament"]},
                {"id": "electron", "icon": "monitor", "title": "Built-in browser", "text": "Playback over WebDriver"},
                {"id": "chrome", "icon": "globe", "title": "Your own Chrome", "text": "Runs through an MV3 extension, no debug port"},
            ]},
        ],
        "edges": [
            {"from": "user", "to": "ai", "label": "request"},
            {"from": "mcpc", "to": "bridge", "label": "18 MCP tools"},
            {"from": "ai", "to": "engine", "label": "test steps"},
            {"from": "bridge", "to": "engine", "label": "run & inspect"},
            {"from": "ai", "to": "proxy", "label": "LLM calls"},
            {"from": "ai", "to": "site", "label": "quota", "dashed": True},
            {"from": "engine", "to": "electron", "label": "WebDriver"},
            {"from": "engine", "to": "chrome", "label": "WebSocket"},
        ],
        "note": "The IDE is our fork of the open-source Selenium IDE, extended with the AI assistant, new commands, "
                "the scheduler, the MCP bridge and the real-Chrome backend.",
    },
    "selenix-mcp-server": {
        "eyebrow": "How it works",
        "title": "From a chat message to a real browser run",
        "columns": [
            {"nodes": [{"id": "client", "icon": "bot", "title": "MCP client",
                        "text": "Claude Desktop, Claude Code or any client that speaks MCP"}]},
            {"nodes": [{"id": "server", "icon": "plug", "accent": True, "title": "@selenix/mcp-server",
                        "text": "18 tools: 14 to inspect, 4 to change and run tests",
                        "chips": ["TypeScript", "stdio", "npm"]}]},
            {"label": "Selenix desktop app", "width": 1.1, "nodes": [
                {"id": "bridge", "icon": "lock", "title": "Local bridge", "text": "HTTP on localhost, bearer token re-read on every call"},
                {"id": "session", "icon": "workflow", "title": "Session controllers", "text": "Tests, playback, logs, page HTML and screenshots"},
            ]},
            {"nodes": [{"id": "browser", "icon": "globe", "title": "Browser", "text": "Built-in browser or your own Chrome"}]},
        ],
        "edges": [
            {"from": "client", "to": "server", "label": "stdio", "both": True},
            {"from": "server", "to": "bridge", "label": "HTTP + token"},
            {"from": "bridge", "to": "session"},
            {"from": "session", "to": "browser", "label": "WebDriver"},
        ],
        "note": "Read tools inspect the project, the open page and the last run. Write tools add or replace commands "
                "and start a run that returns step-by-step results, so the model can fix a failing step and try again.",
    },
    "local-ai-inference": {
        "eyebrow": "How it works",
        "title": "One GPU, shared between a coding agent and a paid service",
        "columns": [
            {"nodes": [
                {"id": "pi", "icon": "bot", "title": "Coding agent", "text": "Implements specs, reads large files, reviews diffs"},
                {"id": "easyace", "icon": "image", "title": "easyace.ai", "text": "Our image and video service: customer jobs come first"},
            ]},
            {"nodes": [{"id": "gate", "icon": "zap", "accent": True, "title": "GPU gate",
                        "text": "Starts the right model on the first request and yields the GPU when a customer job arrives",
                        "chips": ["Python", "hand-off protocol"]}]},
            {"label": "One RTX 5090 (32 GB)", "width": 1.15, "nodes": [
                {"id": "strata", "icon": "cpu", "title": "125B MoE model, 3-bit",
                 "text": "Experts split across VRAM, pinned RAM and SSD; 256K context", "chips": ["Strata engine"]},
                {"id": "router", "icon": "server", "title": "27B dense model", "text": "Fallback with a 128K context",
                 "chips": ["llama.cpp"]},
            ]},
        ],
        "edges": [
            {"from": "pi", "to": "gate", "label": "OpenAI-compatible API"},
            {"from": "easyace", "to": "gate", "label": "claim / release", "both": True, "dashed": True},
            {"from": "gate", "to": "strata", "label": "start & forward"},
            {"from": "gate", "to": "router", "label": "or", "dashed": True},
        ],
        "note": "Strata and llama.cpp are open-source engines. We built the gate, the hand-off with easyace.ai, "
                "the benchmark harness and the agent tooling around them.",
    },
    "easyace": {
        "eyebrow": "How it works",
        "title": "easyace.ai: a self-hosted generation service",
        "columns": [
            {"nodes": [
                {"id": "web", "icon": "monitor", "title": "Studio & gallery", "text": "Generate, browse and share in the browser"},
                {"id": "api", "icon": "plug", "title": "REST API", "text": "Image, video and chat endpoints with API keys"},
            ]},
            {"label": "Application (Docker)", "width": 1.1, "nodes": [
                {"id": "app", "icon": "server", "accent": True, "title": "FastAPI app",
                 "text": "Accounts, credits, jobs and live progress over server-sent events", "chips": ["HTMX", "Stripe"]},
                {"id": "db", "icon": "database", "title": "PostgreSQL", "text": "Users, credits, jobs and the LoRA library"},
            ]},
            {"nodes": [{"id": "queue", "icon": "workflow", "title": "GPU queue",
                        "text": "Groups jobs by model to avoid reloads; retries and a circuit breaker"}]},
            {"label": "GPU workers", "nodes": [
                {"id": "comfy", "icon": "image", "title": "ComfyUI", "text": "FLUX.2, FLUX.1 and SDXL images; LTX-2.3 video"},
                {"id": "llm", "icon": "bot", "title": "LM Studio", "text": "Local LLM for chat completions"},
            ]},
        ],
        "edges": [
            {"from": "web", "to": "app", "label": "HTTPS"},
            {"from": "api", "to": "app", "label": "API key"},
            {"from": "app", "to": "db"},
            {"from": "app", "to": "queue", "label": "jobs"},
            {"from": "queue", "to": "comfy", "label": "workflows"},
            {"from": "queue", "to": "llm", "label": "prompts"},
        ],
        "note": "A watchdog restarts ComfyUI after a CUDA crash, failed jobs are refunded automatically, "
                "and the GPU is shared with our coding models through a hand-off protocol.",
    },
    "translation-api-platform": {
        "eyebrow": "How it works",
        "title": "A multi-tenant translation platform",
        "columns": [
            {"nodes": [
                {"id": "web", "icon": "monitor", "title": "Web client", "text": "React app with single sign-on and two-factor login",
                 "chips": ["React 19", "Express"]},
                {"id": "cust", "icon": "plug", "title": "API customers", "text": "Per-tenant API keys and usage metering"},
            ]},
            {"label": "Platform APIs (FastAPI)", "width": 1.3, "nodes": [
                {"id": "tapi", "icon": "languages", "accent": True, "title": "Translation API",
                 "text": "Machine and LLM translation, structured generation, quality scoring, LLM post-editing"},
                {"id": "flow", "icon": "workflow", "title": "File workflow API",
                 "text": "Jobs split per file and language, translation memory, terminology, human or AI post-edit"},
            ]},
            {"label": "Infrastructure", "nodes": [
                {"id": "mt", "icon": "cpu", "title": "MT engines", "text": "WebSocket engines on a GPU node pool"},
                {"id": "llm", "icon": "bot", "title": "LLM", "text": "Translation, generation and post-editing"},
                {"id": "store", "icon": "database", "title": "Storage", "text": "PostgreSQL, blob storage and queues"},
            ]},
        ],
        "edges": [
            {"from": "web", "to": "tapi", "label": "text"},
            {"from": "web", "to": "flow", "label": "files"},
            {"from": "cust", "to": "tapi", "label": "API key"},
            {"from": "flow", "to": "tapi", "label": "per segment"},
            {"from": "tapi", "to": "mt", "label": "WebSocket"},
            {"from": "tapi", "to": "llm"},
            {"from": "flow", "to": "store", "label": "jobs & files"},
        ],
        "note": "Shipped as Docker images to Kubernetes, with production and sandbox environments and CI building every release.",
    },
    "ai-game-pipeline": {
        "eyebrow": "How it works",
        "title": "From a prompt to a playable asset in Unreal Engine 5.7",
        "columns": [
            {"nodes": [{"id": "concept", "icon": "image", "title": "Concept art", "text": "FLUX.2 explores directions; a person picks one"}]},
            {"nodes": [{"id": "mesh", "icon": "box", "title": "3D mesh", "text": "Hunyuan3D turns the image into a mesh"}]},
            {"nodes": [{"id": "paint", "icon": "image", "title": "Textures", "text": "Hunyuan Paint bakes PBR materials"}]},
            {"label": "Blender, headless", "width": 1.15, "nodes": [
                {"id": "export", "icon": "workflow", "title": "UE5 export", "text": "Centimetre scale, collision, named texture maps"},
                {"id": "fracture", "icon": "zap", "title": "Cell fracture", "text": "Chunks that reassemble within 3 cm"},
                {"id": "mixamo", "icon": "user", "title": "Animations", "text": "Mixamo clips fetched by script and checked"},
            ]},
            {"label": "Unreal Engine 5.7", "width": 1.15, "nodes": [
                {"id": "editor", "icon": "gamepad", "accent": True, "title": "Editor over MCP",
                 "text": "VibeUE and UnrealClaude import assets, wire Blueprints and place actors"},
                {"id": "tests", "icon": "shield", "title": "Headless self-tests",
                 "text": "A game process fires real projectiles before anyone plays"},
            ]},
        ],
        "edges": [
            {"from": "concept", "to": "mesh"},
            {"from": "mesh", "to": "paint"},
            {"from": "paint", "to": "export"},
            {"from": "export", "to": "fracture"},
            {"from": "export", "to": "editor", "label": "FBX"},
            {"from": "fracture", "to": "editor", "label": "chunks"},
            {"from": "mixamo", "to": "editor", "label": "retarget"},
            {"from": "editor", "to": "tests"},
        ],
        "note": "The generators are third-party models running on our own GPU; the orchestration, export rules, "
                "fracture tooling and editor automation are ours.",
    },
}

DIAGRAMS.update({
    "match-recap-videos": {
        "eyebrow": "How it works",
        "title": "Generate the expensive part once, composite every match",
        "columns": [
            {"label": "Once per template", "nodes": [
                {"id": "ltx", "icon": "film", "title": "Video diffusion", "text": "LTX-2.3 renders stadium and fireworks plates"},
                {"id": "cache", "icon": "database", "title": "Asset library", "text": "Cached plates, fonts, logo and audio"},
            ]},
            {"nodes": [
                {"id": "api", "icon": "plug", "title": "Job API", "text": "Match data and one player photo in, a job ID out",
                 "chips": ["FastAPI", "SQLite"]},
                {"id": "cut", "icon": "user", "title": "Background removal", "text": "Player cutout on every request"},
            ]},
            {"nodes": [{"id": "comp", "icon": "workflow", "accent": True, "title": "Compositor",
                        "text": "Flags, cutout, headline, a score that counts up per goal, the match-minute ring",
                        "chips": ["Pillow", "MoviePy"]}]},
            {"nodes": [
                {"id": "mp4", "icon": "smartphone", "title": "10-second vertical video", "text": "720 × 1280, 24 fps, with audio"},
                {"id": "wan", "icon": "zap", "title": "Optional AI closing shot", "text": "Wan2.1 animates the player for the last seconds"},
            ]},
        ],
        "edges": [
            {"from": "ltx", "to": "cache"},
            {"from": "api", "to": "cut"},
            {"from": "cache", "to": "comp", "label": "plates"},
            {"from": "cut", "to": "comp", "label": "cutout"},
            {"from": "comp", "to": "mp4", "label": "render"},
            {"from": "wan", "to": "mp4", "dashed": True},
        ],
        "note": "The standard variants need no GPU at request time: the diffusion work happens once, when a template is made.",
    },
    "project-adam": {
        "eyebrow": "How it works",
        "title": "Answers grounded in knowledge the community has reviewed",
        "columns": [
            {"nodes": [
                {"id": "ask", "icon": "user", "title": "Question", "text": "Asked in a chat session"},
                {"id": "give", "icon": "workflow", "title": "Contribution", "text": "Addition, correction, clarification or source"},
            ]},
            {"nodes": [
                {"id": "agent", "icon": "bot", "accent": True, "title": "Answering agent",
                 "text": "Calls four retrieval tools, then cites what it used", "chips": ["OpenRouter or LM Studio"]},
                {"id": "mod", "icon": "shield", "title": "Votes, then a moderator", "text": "Nothing is published by votes alone"},
            ]},
            {"label": "Knowledge store", "width": 1.1, "nodes": [
                {"id": "qdrant", "icon": "database", "title": "Qdrant", "text": "Summary and section vectors, embedded locally"},
                {"id": "mysql", "icon": "server", "title": "MySQL", "text": "Knowledge, entities and relationships (13 tables)"},
                {"id": "learn", "icon": "zap", "title": "Analysis",
                 "text": "One AI call turns approved text into a summary, sections and entities"},
            ]},
        ],
        "edges": [
            {"from": "ask", "to": "agent"},
            {"from": "agent", "to": "qdrant", "label": "search"},
            {"from": "agent", "to": "mysql", "label": "entities", "dashed": True},
            {"from": "give", "to": "mod"},
            {"from": "mod", "to": "learn", "label": "approved"},
            {"from": "learn", "to": "mysql"},
        ],
        "note": "An hourly job also reviews finished chats for new facts and queues them for a moderator.",
    },
    "zombie-stick-kill": {
        "eyebrow": "How it works",
        "title": "A game that lives inside a Reddit post",
        "columns": [
            {"nodes": [{"id": "post", "icon": "globe", "title": "Reddit post", "text": "The game opens in the post's webview"}]},
            {"nodes": [{"id": "client", "icon": "gamepad", "accent": True, "title": "Phaser 3 client",
                        "text": "Waves, bosses, perks, mutators and two biomes", "chips": ["TypeScript", "Vite"]}]},
            {"label": "Reddit's serverless runtime", "width": 1.2, "nodes": [
                {"id": "server", "icon": "server", "title": "Express server",
                 "text": "Run tokens and plausibility checks on every score"},
                {"id": "redis", "icon": "database", "title": "Redis", "text": "Global and weekly leaderboards, streaks"},
                {"id": "autopost", "icon": "zap", "title": "Record posts", "text": "New records are posted to the subreddit"},
            ]},
        ],
        "edges": [
            {"from": "post", "to": "client"},
            {"from": "client", "to": "server", "label": "fetch"},
            {"from": "server", "to": "redis"},
            {"from": "redis", "to": "autopost"},
        ],
        "note": "Score submissions are checked against single-use run tokens, a plausible run time and ceilings "
                "derived from the wave math.",
    },
    "babysleep": {
        "eyebrow": "How it works",
        "title": "One tap to log, a prediction for the next sleep",
        "columns": [
            {"nodes": [
                {"id": "pwa", "icon": "smartphone", "title": "Installable web app", "text": "Works offline and replays queued changes",
                 "chips": ["React", "TanStack Query"]},
                {"id": "twa", "icon": "box", "title": "Android package", "text": "Trusted Web Activity for Google Play"},
            ]},
            {"label": "API server", "width": 1.2, "nodes": [
                {"id": "api", "icon": "server", "title": "Express API", "text": "Family code, device tokens, sessions, reports"},
                {"id": "sweet", "icon": "zap", "accent": True, "title": "SweetSpot engine",
                 "text": "Age-based wake windows blended with the baby's own history"},
                {"id": "push", "icon": "zap", "title": "Reminders", "text": "Web Push before naps and bedtime, with quiet hours"},
            ]},
            {"nodes": [{"id": "db", "icon": "database", "title": "MySQL", "text": "Families, babies, sessions, devices, subscriptions"}]},
        ],
        "edges": [
            {"from": "pwa", "to": "api", "label": "sync"},
            {"from": "twa", "to": "pwa", "dashed": True, "label": "wraps"},
            {"from": "api", "to": "sweet"},
            {"from": "sweet", "to": "push"},
            {"from": "api", "to": "db"},
        ],
        "note": "Every prediction comes with plain-language reasons, so parents can see why the app suggests a time.",
    },
    "frenamies": {
        "eyebrow": "How it works",
        "title": "Offline-first, and every service is optional",
        "columns": [
            {"label": "Content pipeline", "nodes": [
                {"id": "author", "icon": "workflow", "title": "Author and curate", "text": "Batches deduplicated, reviewed and merged"},
                {"id": "bundle", "icon": "box", "title": "Bundle and lint", "text": "Decks shipped inside the app"},
            ]},
            {"label": "App (Expo, React Native)", "width": 1.3, "nodes": [
                {"id": "engine", "icon": "cpu", "accent": True, "title": "Draw engine",
                 "text": "Filters, weighted intensity and anti-clumping; unit-tested, no UI code"},
                {"id": "games", "icon": "gamepad", "title": "11 mini-games", "text": "Played inside the card"},
                {"id": "store", "icon": "database", "title": "Stores and storage", "text": "Zustand state, MMKV with schema migrations"},
            ]},
            {"label": "Optional services", "nodes": [
                {"id": "rc", "icon": "lock", "title": "RevenueCat", "text": "Subscriptions and trial"},
                {"id": "ph", "icon": "chart", "title": "PostHog", "text": "17 events, anonymous IDs"},
                {"id": "sentry", "icon": "shield", "title": "Sentry", "text": "Crash reporting"},
            ]},
        ],
        "edges": [
            {"from": "author", "to": "bundle"},
            {"from": "bundle", "to": "engine", "label": "decks"},
            {"from": "engine", "to": "games"},
            {"from": "games", "to": "store"},
            {"from": "store", "to": "rc", "dashed": True},
            {"from": "store", "to": "ph", "dashed": True},
            {"from": "store", "to": "sentry", "dashed": True},
        ],
        "note": "Each service adapter switches itself off when its key is missing, so the game always runs.",
    },
})

DIAGRAMS["local-ai-strata"] = {
    "eyebrow": "Inside Strata",
    "title": "How a 125B model fits on one graphics card",
    "columns": [
        {"label": "Graphics card (VRAM)", "width": 1.15, "nodes": [
            {"id": "core", "icon": "cpu", "title": "Always on the GPU",
             "text": "Attention and DeltaNet layers, routers, shared experts, output head and the MTP draft layer"},
            {"id": "cache", "icon": "zap", "accent": True, "title": "Adaptive expert cache",
             "text": "The rest of VRAM holds the most-used experts, about 700 per GB, and adapts while you chat"},
            {"id": "kv", "icon": "database", "title": "KV cache", "text": "The most-read part stays on the GPU; from 64K the rest streams from RAM"},
        ]},
        {"label": "System RAM", "nodes": [
            {"id": "ram", "icon": "server", "title": "All 24,576 experts, pinned",
             "text": "Each token needs 10. The CPU computes the ones the GPU does not hold, at the same time as the GPU"},
        ]},
        {"label": "Decoding", "width": 1.05, "nodes": [
            {"id": "mtp", "icon": "workflow", "title": "Guess, then check",
             "text": "The MTP layer drafts up to 3 tokens and one pass checks them: 2.4 to 3.2 tokens per pass, identical output"},
            {"id": "prefill", "icon": "film", "title": "Long prompts in big pieces",
             "text": "Read 8,192 tokens at a time while the next layer's experts stream over PCIe"},
        ]},
        {"label": "SSD", "width": 0.8, "nodes": [
            {"id": "ssd", "icon": "database", "title": "28.8 GB n-gram table", "text": "A few rows read per token"},
        ]},
    ],
    "edges": [
        {"from": "ram", "to": "cache", "label": "experts stream in"},
        {"from": "ram", "to": "kv", "label": "KV beyond 64K", "dashed": True},
        {"from": "ssd", "to": "mtp", "label": "lookup rows", "dashed": True},
    ],
    "note": "Strata is an open-source (MIT) engine by Niko1221 and contributors; figures from its documentation. "
            "It serves OpenAI, Anthropic Messages and Responses APIs, so Claude Code and Codex CLI can use it directly.",
}

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{slug} diagram</title>
<!-- Generated by build_pages.py; edit the data there. -->
<link rel="stylesheet" href="https://fonts.bunny.net/css?family=figtree:400,500,600,700">
<link rel="stylesheet" href="diagram.css">
</head><body>
<div id="frame"></div>
<script src="diagram.js"></script>
<script>
renderDiagram(document.getElementById('frame'), {data});
</script>
</body></html>
"""

if __name__ == "__main__":
    for slug, data in DIAGRAMS.items():
        out = HERE / f"{slug}.html"
        out.write_text(TEMPLATE.format(slug=slug, data=json.dumps(data, indent=1, ensure_ascii=False)), encoding="utf-8")
        print("wrote", out.name)
