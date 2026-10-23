# Portfolio image tooling

Pick screenshots, capture them, frame them, ship WebP.

**contact_sheet.py** — numbered tiles so screenshots can be requested by `#NNN`:

    python tools/portfolio/contact_sheet.py --glob "shots/**/*.png" --out shots/sheets --cols 4 --rows 3 --thumb 480

Writes `sheet_01.png`, ... and `index.txt` (`#NNN<TAB>path<TAB>WxH`).

**capture.mjs** — Playwright captures (uses the repo's playwright install). Web page or local frame, one browser per jobs file
(`url`, `out`, `viewport`, `scale`, `waitFor`, `fullPage`, `selector`, `hide`):

    node tools/portfolio/capture.mjs jobs shots/jobs.json

Electron app: prints `READY`, then every file dropped in `<out-dir>/.requests/` becomes `<name>.png`; a file named `quit` closes it:

    node tools/portfolio/capture.mjs electron --exe "C:/path/app.exe" --out-dir shots --width 1600 --height 1000 -- --flag

**frames/*.html** — 1600x900 device frames driven by the query string; capture jobs wait for `body[data-ready='1']`:

    node tools/portfolio/capture.mjs jobs frames/jobs.json   # url: file:///.../frames/browser.html?src=file:///shots/app.png&url=example.com

`browser.html` (`src`, `url`), `window.html` (`src`, `title`), `phone.html` (`src`: up to 3 comma-separated; `ratio=9:16` for 9:16 sources),
`terminal.html` (`src`: URL of a UTF-8 text log, `title`).

**optimize.py** — redact, centre-crop, write `<name>.webp` + `<name>-800.webp`
(job keys: `src`, `out_dir`, `name`, `crop` `"16:9"`, `blur` `[[x,y,w,h],...]` in source pixels, `fill` `[[x,y,w,h,"#hex"|"auto"],...]` to paint a region out, `max_width`):

    python tools/portfolio/optimize.py --jobs optimize/jobs.json --manifest optimize/manifest.json
