#!/usr/bin/env node
// Screenshot capture for portfolio shots: web pages, local HTML frames, Electron apps.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { chromium, _electron } from 'playwright';

const USAGE = [
    'usage:',
    '  node tools/portfolio/capture.mjs jobs <jobs.json>',
    '  node tools/portfolio/capture.mjs electron --exe <path> --out-dir <dir> [--width 1600] [--height 1000] [-- <app args...>]',
].join('\n');

async function runJobs(jobsFile) {
    const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
    // file:// frame templates read local logs/screenshots, which Chromium blocks without this flag
    const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
    let failed = 0;

    for (const job of jobs) {
        let context;
        try {
            context = await browser.newContext({
                viewport: job.viewport ?? { width: 1600, height: 900 },
                deviceScaleFactor: job.scale ?? 1,
            });
            const page = await context.newPage();
            await page.goto(job.url, { waitUntil: 'networkidle', timeout: 45000 });

            const waitFor = job.waitFor ?? 1000;
            if (typeof waitFor === 'number') await page.waitForTimeout(waitFor);
            else await page.waitForSelector(waitFor);

            for (const sel of job.hide ?? []) {
                await page.addStyleTag({ content: `${sel} { display: none !important }` });
            }
            await page.evaluate(() => document.fonts.ready);

            const out = path.resolve(job.out);
            fs.mkdirSync(path.dirname(out), { recursive: true });
            if (job.selector) {
                await page.locator(job.selector).screenshot({ path: out });
            } else {
                await page.screenshot({ path: out, fullPage: !!job.fullPage });
            }
            console.log(`OK ${out}`);
        } catch (err) {
            failed += 1;
            console.log(`FAIL ${job.url}: ${err.message}`);
        } finally {
            if (context) await context.close();
        }
    }

    await browser.close();
    if (failed) process.exit(1);
}

function parseElectronArgs(argv) {
    const opts = { width: 1600, height: 1000, appArgs: [] };
    for (let i = 0; i < argv.length; i++) {
        const arg = argv[i];
        if (arg === '--') {
            opts.appArgs = argv.slice(i + 1);
            break;
        } else if (arg === '--exe') opts.exe = argv[++i];
        else if (arg === '--out-dir') opts.outDir = argv[++i];
        else if (arg === '--width') opts.width = Number(argv[++i]);
        else if (arg === '--height') opts.height = Number(argv[++i]);
        else throw new Error(`unknown option: ${arg}`);
    }
    if (!opts.exe || !opts.outDir) throw new Error('--exe and --out-dir are required');
    return opts;
}

async function runElectron(argv) {
    let opts;
    try {
        opts = parseElectronArgs(argv);
    } catch (err) {
        console.log(`FAIL ${err.message}`);
        process.exit(1);
    }

    const env = { ...process.env };
    delete env.ELECTRON_RUN_AS_NODE; // makes Electron run as plain Node
    const requestsDir = path.join(opts.outDir, '.requests');
    fs.mkdirSync(requestsDir, { recursive: true });

    let app;
    try {
        app = await _electron.launch({
            executablePath: opts.exe,
            args: opts.appArgs,
            env,
            timeout: 120000,
        });
        await app.firstWindow();
        await app.evaluate(({ BrowserWindow }, [w, h]) => {
            const b = BrowserWindow.getAllWindows()[0];
            b.setSize(w, h);
            b.center();
        }, [opts.width, opts.height]);
    } catch (err) {
        console.log(`FAIL ${err.message}`);
        process.exit(1);
    }

    // If the app quits on its own, stop polling instead of waiting forever on firstWindow().
    app.on('close', () => {
        console.log('FAIL the app closed');
        process.exit(1);
    });

    console.log('READY');
    for (;;) {
        let names = [];
        try {
            fs.mkdirSync(requestsDir, { recursive: true });
            names = fs.readdirSync(requestsDir);
        } catch (err) {
            console.log(`FAIL reading ${requestsDir}: ${err.message}`);
        }
        for (const name of names) {
            const request = path.join(requestsDir, name);
            try {
                if (name === 'quit') {
                    fs.rmSync(request);
                    // Some apps intercept close (unsaved-project prompts, tray); give them 5 s, then kill.
                    const pid = app.process().pid;
                    await Promise.race([app.close(), new Promise((r) => setTimeout(r, 5000))]);
                    // Kill the whole tree: killing only the main process orphans renderers and chromedriver.
                    try {
                        if (process.platform === 'win32') execFileSync('taskkill', ['/PID', String(pid), '/T', '/F'], { stdio: 'ignore' });
                        else process.kill(-pid);
                    } catch { /* already gone */ }
                    process.exit(0);
                }
                // the page can be replaced, so re-acquire the window each time
                const win = app.windows()[0] ?? (await app.firstWindow());
                if (name.endsWith('.json')) {
                    // Step request: [{ "click": "Visible text" } | { "clickSel": "css" } | { "press": "Enter" } |
                    // { "wait": 1500 } | { "dump": true } | { "shot": "name" }], run in order.
                    const steps = JSON.parse(fs.readFileSync(request, 'utf8'));
                    fs.rmSync(request);
                    for (const s of steps) {
                        if (s.click) await win.getByText(s.click, { exact: true }).first().click();
                        else if (s.clickSel) await win.locator(s.clickSel).first().click();
                        else if (s.press) await win.keyboard.press(s.press);
                        else if (s.wait) await win.waitForTimeout(s.wait);
                        else if (s.shot) {
                            const shotPath = path.join(opts.outDir, `${s.shot}.png`);
                            await win.screenshot({ path: shotPath });
                            console.log(`SHOT ${shotPath}`);
                        } else if (s.osshot) {
                            // OS-level capture of the main window: includes BrowserView/WebContentsView overlays.
                            const hwnd = await app.evaluate(({ BrowserWindow }) => {
                                const b = BrowserWindow.getAllWindows()[0];
                                b.focus();
                                const buf = b.getNativeWindowHandle();
                                return buf.length >= 8 ? buf.readBigUInt64LE(0).toString() : String(buf.readUInt32LE(0));
                            });
                            await win.waitForTimeout(400);
                            const shotPath = path.resolve(opts.outDir, `${s.osshot}.png`);
                            const helper = path.join(path.dirname(fileURLToPath(import.meta.url)), 'printwindow.ps1');
                            execFileSync('powershell', ['-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', helper,
                                '-Hwnd', hwnd, '-Out', shotPath], { stdio: 'pipe' });
                            console.log(`SHOT ${shotPath}`);
                        } else if (s.dump) {
                            // Visible buttons, tabs and inputs, to find what to click next.
                            const items = await win.evaluate(() => [...document.querySelectorAll(
                                'button, [role=tab], [role=button], a, input, [aria-label], [title]')]
                                .filter((e) => e.offsetParent !== null)
                                .map((e) => ({ tag: e.tagName, text: (e.innerText || '').trim().slice(0, 40),
                                    aria: e.getAttribute('aria-label'), title: e.getAttribute('title'),
                                    id: e.id || null, cls: String(e.className || '').slice(0, 60) })));
                            fs.writeFileSync(path.join(opts.outDir, 'dom.json'), JSON.stringify(items, null, 1));
                            console.log(`DUMP ${items.length} elements`);
                        }
                    }
                    console.log(`DONE ${name}`);
                    continue;
                }
                const out = path.join(opts.outDir, `${name}.png`);
                await win.screenshot({ path: out });
                fs.rmSync(request);
                console.log(`SHOT ${out}`);
            } catch (err) {
                console.log(`FAIL ${name}: ${err.message}`);
            }
        }
        await new Promise((resolve) => setTimeout(resolve, 500));
    }
}

const mode = process.argv[2];
if (mode === 'jobs' && process.argv[3]) {
    runJobs(process.argv[3]).catch((err) => {
        console.log(`FAIL ${err.message}`);
        process.exit(1);
    });
} else if (mode === 'electron') {
    runElectron(process.argv.slice(3)).catch((err) => {
        console.log(`FAIL ${err.message}`);
        process.exit(1);
    });
} else {
    console.log(USAGE);
    process.exit(1);
}
