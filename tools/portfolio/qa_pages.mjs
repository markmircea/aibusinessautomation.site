// Browser QA for the portfolio and digital-marketing pages at desktop and phone widths.
// Checks per page: console errors, exactly one <h1>, no horizontal scroll, every image loaded with an alt attribute,
// one each of <title> and the og: tags after hydration. Then link previews (the server HTML, which scrapers read
// without running JavaScript, carries the tags and a loadable share image), the portfolio filter (?c=) and the
// case-study lightbox keyboard flow.
// Usage: node tools/portfolio/qa_pages.mjs [base-url]   (default http://aibusinessautomation.site.test)
import { chromium } from 'playwright';
import fs from 'node:fs';

const base = process.argv[2] || 'http://aibusinessautomation.site.test';
const projects = JSON.parse(fs.readFileSync('resources/js/data/portfolio.json', 'utf8')).filter((p) => p.published);
const paths = ['/', '/portfolio', ...projects.map((p) => `/portfolio/${p.slug}`), '/web-development', '/web-development/digital-marketing'];
const failures = [];
const fail = (msg) => { failures.push(msg); console.log('FAIL', msg); };

const browser = await chromium.launch();
for (const width of [1440, 375]) {
    const page = await browser.newPage({ viewport: { width, height: width === 375 ? 812 : 900 } });
    const errors = [];
    page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
    page.on('pageerror', (e) => errors.push(e.message));
    for (const path of paths) {
        errors.length = 0;
        const res = await page.goto(base + path, { waitUntil: 'networkidle' });
        if (!res || res.status() !== 200) fail(`${width} ${path}: HTTP ${res && res.status()}`);
        // Scroll to the bottom in steps so lazy images load, then back up.
        await page.evaluate(async () => {
            for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
            window.scrollTo(0, 0);
        });
        await page.waitForTimeout(600);
        // Lazy images that have not loaded yet: bring each into view and give it up to 4 s before calling it broken.
        await page.evaluate(async () => {
            const pending = [...document.images].filter((i) => !i.complete || i.naturalWidth === 0);
            for (const img of pending) {
                img.loading = 'eager';
                img.scrollIntoView({ block: 'center', inline: 'center' });
                await Promise.race([img.decode().catch(() => {}), new Promise((r) => setTimeout(r, 4000))]);
            }
            window.scrollTo(0, 0);
        });
        const r = await page.evaluate(() => ({
            h1: document.querySelectorAll('h1').length,
            overflow: document.documentElement.scrollWidth - window.innerWidth,
            broken: [...document.images].filter((i) => !i.complete || i.naturalWidth === 0).map((i) => i.getAttribute('src')),
            noAlt: [...document.images].filter((i) => !i.hasAttribute('alt')).map((i) => i.getAttribute('src')),
            // DynamicSEO.vue must take over the server-rendered tags, not add a second set.
            headTags: ['title', 'meta[property="og:title"]', 'meta[property="og:image"]', 'meta[name="description"]']
                .map((sel) => `${sel}=${document.head.querySelectorAll(sel).length}`).filter((s) => !s.endsWith('=1')),
        }));
        if (r.headTags.length) fail(`${width} ${path}: head tags not exactly once: ${r.headTags.join(', ')}`);
        if (r.h1 !== 1) fail(`${width} ${path}: ${r.h1} h1 elements`);
        if (r.overflow > 1) fail(`${width} ${path}: horizontal overflow ${r.overflow}px`);
        if (r.broken.length) fail(`${width} ${path}: images not loaded ${r.broken.join(', ')}`);
        if (r.noAlt.length) fail(`${width} ${path}: images without alt ${r.noAlt.join(', ')}`);
        if (errors.length) fail(`${width} ${path}: console errors ${errors.slice(0, 3).join(' | ')}`);
        console.log(`ok-ish ${width} ${path}`);
    }
    await page.close();
}

// Link previews: WhatsApp, Slack, LinkedIn, Facebook and X read the HTML the server sends and run no JavaScript.
const shareImages = new Map();
for (const path of paths) {
    const html = await (await fetch(base + path)).text();
    const head = html.slice(0, html.indexOf('</head>'));
    const meta = (attr, key) => [...head.matchAll(new RegExp(`<meta[^>]*${attr}="${key}"[^>]*content="([^"]*)"`, 'g'))].map((m) => m[1]);
    for (const [attr, key] of [['name', 'description'], ['property', 'og:title'], ['property', 'og:description'], ['property', 'og:image'], ['name', 'twitter:card']]) {
        const found = meta(attr, key);
        if (found.length !== 1 || !found[0].trim()) fail(`${path}: server HTML has ${found.length} ${key} tag(s)${found.length === 1 ? ', empty' : ''}`);
    }
    const image = meta('property', 'og:image')[0];
    if (image && !shareImages.has(image)) {
        const res = await fetch(image);
        const type = res.headers.get('content-type') || '';
        shareImages.set(image, res.status);
        if (res.status !== 200 || !/^image\/(jpeg|png)/.test(type)) fail(`${path}: og:image ${image} -> HTTP ${res.status} ${type}`);
    }
}
console.log(`link previews: ${paths.length} pages, ${shareImages.size} distinct share images`);

// Unknown and unpublished slugs must 404.
const p404 = await browser.newPage();
const drafts = fs.existsSync('tools/portfolio/drafts.json') ? JSON.parse(fs.readFileSync('tools/portfolio/drafts.json', 'utf8')) : [];
for (const slug of ['nope', ...drafts.map((p) => p.slug)]) {
    const res = await p404.goto(`${base}/portfolio/${slug}`);
    if (res.status() !== 404) fail(`/portfolio/${slug}: expected 404, got ${res.status()}`);
}
await p404.close();

// Filter: the Games chip shows only games and writes ?c=games.
const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
await page.goto(`${base}/portfolio`, { waitUntil: 'networkidle' });
await page.getByRole('button', { name: /^Games/ }).click();
await page.waitForTimeout(400);
const games = projects.filter((p) => p.categories.includes('games')).length;
const cards = await page.locator('a[href*="/portfolio/"]').filter({ hasText: 'Read case study' }).count();
if (cards !== games) fail(`filter Games: ${cards} cards, expected ${games}`);
if (!page.url().includes('c=games')) fail(`filter Games: URL ${page.url()} has no ?c=games`);
const pressed = await page.getByRole('button', { name: /^Games/ }).getAttribute('aria-pressed');
if (pressed !== 'true') fail(`filter Games: aria-pressed=${pressed}`);

// Lightbox: open from the gallery, arrow to the next image, Escape closes and focus returns to the opener.
const withGallery = projects.find((p) => p.gallery.length > 1);
await page.goto(`${base}/portfolio/${withGallery.slug}`, { waitUntil: 'networkidle' });
const opener = page.locator('figure button').first();
await opener.scrollIntoViewIfNeeded();
await opener.click();
const dialog = page.getByRole('dialog');
await dialog.waitFor({ timeout: 3000 }).catch(() => fail('lightbox: no role=dialog after click'));
const firstSrc = await dialog.locator('img').first().getAttribute('src');
await page.keyboard.press('ArrowRight');
await page.waitForTimeout(300);
const secondSrc = await dialog.locator('img').first().getAttribute('src');
if (firstSrc === secondSrc) fail('lightbox: ArrowRight did not change the image');
const focusInside = await page.evaluate(() => !!document.activeElement?.closest('[role="dialog"]'));
if (!focusInside) fail('lightbox: focus is not inside the dialog');
await page.keyboard.press('Escape');
await page.waitForTimeout(300);
if (await dialog.count() && await dialog.isVisible()) fail('lightbox: Escape did not close it');
const focusBack = await opener.evaluate((el) => el === document.activeElement);
if (!focusBack) fail('lightbox: focus did not return to the opener');

await browser.close();
console.log(failures.length ? `${failures.length} failure(s)` : 'ALL CHECKS PASSED');
process.exit(failures.length ? 1 : 0);
