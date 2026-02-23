#!/usr/bin/env python3
"""
Gemini Deep Research Runner — persistent Chrome via subprocess + CDP.

Chrome launches as a normal subprocess (invisible to Google's bot detection),
Playwright connects via Chrome DevTools Protocol to control it.

Browser starts ONCE and stays open between tasks.

Login flow: warmup → Gemini Sign in → email → mouse-click Next → password → done.

Usage:
    python3 gemini_runner.py --dump-ui
    python3 gemini_runner.py --test
    python3 gemini_runner.py -p "prompt" -o out.md
    python3 gemini_runner.py --tasks-dir tasks/ --output-dir output/
    python3 gemini_runner.py --email other@gmail.com --password Pass123
"""

import argparse
import json
import os
import random
import socket
import subprocess
import sys
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("❌ pip install playwright && python -m playwright install chromium")
    sys.exit(1)

# ── Config ─────────────────────────────────────────────────

PROFILES_DIR = Path(__file__).parent.parent / "config" / "chrome_profiles"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
STATE_FILE = Path(__file__).parent.parent / "config" / ".chrome_state.json"
GEMINI_URL = "https://gemini.google.com"
RESEARCH_TIMEOUT = 45 * 60

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
]

STEALTH_SCRIPT = """
(function() {
    const proto = Object.getPrototypeOf(navigator);
    try { delete proto.webdriver; } catch(e) {}
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined, configurable: true
    });
    const origDP = Object.defineProperty;
    Object.defineProperty = function(obj, prop, desc) {
        if (obj === navigator && prop === 'webdriver') return obj;
        return origDP.apply(this, arguments);
    };
    window.chrome = {runtime: {}};
})();
"""


# ── Helpers ────────────────────────────────────────────────

def _find_chrome():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    return None


def _free_port():
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _load_creds(email=None, password=None):
    if email and password:
        return email, password
    env_file = Path(__file__).parent.parent / "config" / "keys.env"
    if env_file.exists():
        creds = {}
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                creds[k.strip()] = v.strip()
        return (
            email or creds.get("GEMINI_EMAIL", ""),
            password or creds.get("GEMINI_PASSWORD", ""),
        )
    return email or "", password or ""


def _profile_dir(email):
    slug = email.split("@")[0].replace(".", "_")
    d = PROFILES_DIR / f"gemini_{slug}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _screenshot(page, name):
    out = OUTPUT_DIR / f"gemini_{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        page.screenshot(path=str(out))
    except:
        pass


def _human_type(page, text):
    """Type with human-like variable delays."""
    for ch in text:
        page.keyboard.type(ch, delay=random.randint(45, 110))
        time.sleep(random.uniform(0.02, 0.07))


def _mouse_click(page, locator):
    """Click element with mouse at random offset (like human)."""
    box = locator.bounding_box()
    if box:
        page.mouse.click(
            box["x"] + box["width"] / 2 + random.randint(-3, 3),
            box["y"] + box["height"] / 2 + random.randint(-2, 2),
            delay=random.randint(80, 180),
        )
        return True
    locator.click()
    return True


# ── Chrome subprocess ──────────────────────────────────────

def launch_chrome(profile_dir):
    """Launch Chrome as a normal process with CDP port."""
    chrome = _find_chrome()
    if not chrome:
        print("❌ Chrome not found!")
        sys.exit(1)

    port = _free_port()
    args = [
        chrome,
        f"--remote-debugging-port={port}",
        f"--user-data-dir={profile_dir}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-blink-features=AutomationControlled",
        "--disable-automation",
        "--disable-infobars",
        "--disable-component-update",
        "--password-store=basic",
        "--use-mock-keychain",
        "--enable-features=NetworkService,NetworkServiceInProcess",
        "about:blank",
    ]

    proc = subprocess.Popen(
        args, start_new_session=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    time.sleep(3)

    if proc.poll() is not None:
        print("❌ Chrome exited immediately")
        sys.exit(1)

    print(f"   PID: {proc.pid}, CDP: {port}")

    # Save state for reconnection
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"pid": proc.pid, "port": port, "profile": str(profile_dir)}))

    return proc, port


def _chrome_alive(pid):
    """Check if Chrome process is still running."""
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def _cdp_alive(port):
    """Check if CDP port is responsive."""
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect(("127.0.0.1", port))
        s.close()
        return True
    except:
        return False


def get_or_launch_chrome(profile_dir):
    """Reconnect to existing Chrome if alive, otherwise launch new."""
    # Try reconnect
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
            pid, port = state["pid"], state["port"]
            if _chrome_alive(pid) and _cdp_alive(port):
                print(f"   ♻️  Reconnecting to Chrome (PID: {pid}, CDP: {port})")
                return None, port  # proc=None means we didn't launch it
        except:
            pass

    # Launch new
    return launch_chrome(profile_dir)


def connect_cdp(pw, port):
    """Connect Playwright to Chrome via CDP."""
    for attempt in range(10):
        try:
            browser = pw.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
            print("   ✅ CDP connected")
            return browser
        except:
            if attempt == 9:
                return None
            time.sleep(1)


def setup_stealth(context, page):
    """Inject stealth before any navigation."""
    try:
        client = context.new_cdp_session(page)
        client.send("Page.addScriptToEvaluateOnNewDocument", {"source": STEALTH_SCRIPT})
        client.send("Page.setBypassCSP", {"enabled": True})
    except:
        pass


# ── Cookie warmup ──────────────────────────────────────────

def warmup(page):
    """Visit popular sites to build cookie history (like droidec)."""
    print("   Cookie warmup...")
    for site in ["https://www.google.com", "https://www.youtube.com", "https://github.com"]:
        try:
            page.goto(site, timeout=15000)
            time.sleep(random.uniform(2, 4))
            page.evaluate("window.scrollTo(0, Math.random() * 300)")
            time.sleep(random.uniform(1, 2))
        except:
            pass


# ── Login ──────────────────────────────────────────────────

def login(page, email, password):
    """
    Full auto-login to Google for Gemini.
    Flow: warmup → Gemini → Sign in → email → Next → password → done.
    """
    # Check if already logged in
    print("   Checking login...")
    page.goto(f"{GEMINI_URL}/app", timeout=60000)
    time.sleep(8)

    try:
        # Gemini now uses contenteditable div, not textarea
        editor = page.locator('.ql-editor[role="textbox"], textarea')
        if editor.first.is_visible(timeout=8000):
            print("   ✅ Already logged in")
            return True
    except:
        pass

    # Warmup
    warmup(page)

    # Go to Gemini
    print("   Going to Gemini...")
    page.goto(f"{GEMINI_URL}/app", timeout=60000)
    time.sleep(5)

    # Click "Sign in"
    for sel in ['a:has-text("Sign in")', 'button:has-text("Sign in")',
                'a:has-text("Войти")', 'button:has-text("Войти")']:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=3000):
                _mouse_click(page, el)
                print("   Clicked Sign in")
                break
        except:
            pass

    time.sleep(8)

    # === Email ===
    # Could be account picker or fresh login
    # Try account picker first
    for sel_tpl in [
        '[data-email="{}"]', '[data-identifier="{}"]',
    ]:
        try:
            el = page.locator(sel_tpl.format(email)).first
            if el.is_visible(timeout=2000):
                _mouse_click(page, el)
                print(f"   ✅ Picked account: {email}")
                time.sleep(5)
                break
        except:
            pass
    else:
        # Try JS click on email text
        found = page.evaluate("""(email) => {
            const els = document.querySelectorAll('*');
            for (const el of els) {
                if (el.children.length === 0 && el.innerText &&
                    el.innerText.trim() === email) {
                    let t = el;
                    for (let i = 0; i < 5; i++) {
                        if (t.parentElement) t = t.parentElement;
                        if (t.tagName === 'LI' || t.getAttribute('data-identifier')) break;
                    }
                    t.click();
                    return true;
                }
            }
            return false;
        }""", email)

        if found:
            print(f"   ✅ Picked account (JS)")
            time.sleep(5)
        else:
            # Fresh login — type email
            email_input = page.locator('input[type="email"]')
            try:
                email_input.wait_for(state="visible", timeout=5000)
                email_input.first.click()
                time.sleep(0.5)
                _human_type(page, email)
                time.sleep(random.uniform(0.5, 1.5))

                # Mouse-click Next (critical: NOT keyboard Enter!)
                next_btn = page.locator("#identifierNext button, button:has-text('Next'), button:has-text('Далее')")
                if next_btn.count() > 0:
                    _mouse_click(page, next_btn.first)
                    print("   ✅ Email → Next clicked")
                else:
                    page.keyboard.press("Enter")
                    print("   Email → Enter")

                time.sleep(8)
            except:
                print("   ❌ No email input found")
                _screenshot(page, "login_fail")
                return False

    # === Password ===
    pw_input = page.locator('input[type="password"]')
    visible_pw = None
    for i in range(pw_input.count()):
        if pw_input.nth(i).is_visible():
            visible_pw = pw_input.nth(i)
            break

    if visible_pw:
        visible_pw.click()
        time.sleep(0.5)
        _human_type(page, password)
        time.sleep(random.uniform(0.5, 1.5))

        # Mouse-click Next
        pw_next = page.locator("#passwordNext button, button:has-text('Next'), button:has-text('Далее')")
        if pw_next.count() > 0:
            _mouse_click(page, pw_next.first)
            print("   ✅ Password → Next clicked")
        else:
            page.keyboard.press("Enter")

        time.sleep(10)
    elif "gemini.google.com" in page.url:
        # Already redirected — no password needed
        pass
    else:
        print("   ❌ No password field")
        _screenshot(page, "no_password")
        return False

    # === Post-password: wait for redirect ===
    # URL may briefly contain "challenge/pwd" — that's NORMAL (password step).
    # Real 2FA would keep us on challenge/ page for a long time.
    time.sleep(10)

    if "gemini.google.com" in page.url:
        print("   ✅ Logged in!")
        return True

    # Still on Google — might be real 2FA or other challenge
    if "challenge" in page.url and "challenge/pwd" not in page.url:
        print("   ⚠️  Security challenge — check browser window")
        for _ in range(24):
            time.sleep(5)
            if "gemini.google.com" in page.url or "myaccount" in page.url:
                break
        else:
            print("   ❌ Challenge timeout")
            _screenshot(page, "challenge")
            return False

    # Try navigating to Gemini
    if "gemini.google.com" not in page.url:
        page.goto(f"{GEMINI_URL}/app", timeout=60000)
        time.sleep(5)

    print("   ✅ Logged in!")
    return True


# ── Deep Research ──────────────────────────────────────────

def _dump_ui(page):
    """Dump all visible interactive elements."""
    return page.evaluate("""() => {
        const r = [];
        const sels = 'button,[role="button"],[role="tab"],[role="option"],[role="listbox"],' +
                      '[role="combobox"],[aria-haspopup],select,textarea,input,[role="menuitem"],' +
                      '[role="radio"],[role="switch"]';
        document.querySelectorAll(sels).forEach(el => {
            if (el.offsetParent !== null || el.tagName === 'TEXTAREA') {
                r.push({
                    tag: el.tagName, text: (el.innerText||'').substring(0,80).trim(),
                    ariaLabel: el.getAttribute('aria-label') || '',
                    role: el.getAttribute('role') || '',
                    cls: (el.className||'').substring(0,60),
                    ariaHaspopup: el.getAttribute('aria-haspopup') || '',
                });
            }
        });
        return r;
    }""")


def select_thinking_mode(page):
    """Select Думающая (Thinking) mode via the mode picker button.

    Google moved Deep Research from Pro → Thinking mode (Feb 2026).
    The mode picker shows current mode (Быстрая/Fast/Pro/Думающая/Thinking).
    """
    print("   → Selecting Thinking mode...")

    mode_btn = page.locator(
        'button.input-area-switch, [aria-label="Open mode picker"], '
        'button:has-text("Быстрая"), button:has-text("Fast"), '
        'button:has-text("Pro"), button:has-text("Думающая"), '
        'button:has-text("Thinking")'
    )
    try:
        if mode_btn.first.is_visible(timeout=5000):
            current = mode_btn.first.inner_text().strip()
            if "Думающая" in current or "Thinking" in current:
                print(f"   ✅ Already on Thinking mode")
                return True
            _mouse_click(page, mode_btn.first)
            time.sleep(2)

            # Look for Думающая/Thinking in dropdown
            for sel in [
                'text="Думающая"', 'text="Thinking"',
                '[role="option"]:has-text("Думающая")', '[role="option"]:has-text("Thinking")',
                '[role="menuitem"]:has-text("Думающая")', '[role="menuitem"]:has-text("Thinking")',
                'li:has-text("Думающая")', 'li:has-text("Thinking")',
                'button:has-text("Думающая")', 'button:has-text("Thinking")',
                'mat-option:has-text("Думающая")', 'mat-option:has-text("Thinking")',
            ]:
                try:
                    opt = page.locator(sel).first
                    if opt.is_visible(timeout=2000):
                        _mouse_click(page, opt)
                        time.sleep(2)
                        print("   ✅ Thinking mode selected!")
                        return True
                except:
                    pass

            # Dump what's in the dropdown for debugging
            items = page.evaluate('''() => {
                const r = [];
                document.querySelectorAll('[role="option"],[role="menuitem"],mat-option,.mat-mdc-menu-item').forEach(el => {
                    if (el.offsetParent !== null) r.push(el.innerText.trim().substring(0, 50));
                });
                return r;
            }''')
            print(f"   Dropdown items: {items}")

            page.keyboard.press("Escape")
            time.sleep(0.5)
    except:
        pass

    print("   ⚠️  Thinking mode not found in mode picker")
    _screenshot(page, "thinking_select")
    return False


def navigate_deep_research(page):
    """Activate Deep Research: fresh chat → Thinking mode → Tools → Deep Research.

    Google moved Deep Research to Thinking mode (Feb 2026).
    Flow: navigate to /app → select Думающая → Tools → Deep Research.
    """
    print("   → Deep Research...")

    # Always navigate to fresh /app page (new chat)
    page.goto(f"{GEMINI_URL}/app", timeout=60000)
    time.sleep(5)

    # Step 1: Select "Думающая" (Thinking) mode
    select_thinking_mode(page)
    time.sleep(2)

    # Step 2: Click "Инструменты" (Tools) button
    tools_btn = page.locator('button:has-text("Инструменты"), button:has-text("Tools")')
    try:
        tools_btn.first.wait_for(state="visible", timeout=10000)
        tools_btn.first.click()
        time.sleep(2)
    except:
        _screenshot(page, "no_tools")
        # Deep Research might be auto-active in Thinking mode
        print("   ℹ️  Tools button not found — Deep Research may be auto-active in Thinking mode")
        return True

    # Step 3: Click "Deep Research" in the menu
    dr_item = page.locator('text="Deep Research"')
    try:
        dr_item.first.wait_for(state="visible", timeout=5000)
        dr_item.first.click()
        time.sleep(3)
        print("   ✅ Deep Research activated")
        return True
    except:
        _screenshot(page, "no_deep_research")
        print("   ℹ️  Deep Research not in Tools menu — may be auto-active in Thinking mode")
        return True


def enter_prompt(page, prompt):
    """Type and submit prompt (Gemini uses Quill rich-text editor, not textarea)."""
    # Gemini input: contenteditable div with class ql-editor
    editor = page.locator('.ql-editor[role="textbox"], [role="textbox"][contenteditable="true"]')
    try:
        editor.wait_for(state="visible", timeout=10000)
    except:
        # Fallback: try textarea (older Gemini)
        ta = page.locator("textarea")
        try:
            ta.wait_for(state="visible", timeout=5000)
            ta.click()
            ta.fill(prompt)
            time.sleep(1)
            page.keyboard.press("Enter")
            print("   ✅ Sent (textarea fallback)")
            return True
        except:
            _screenshot(page, "no_input")
            print("   ❌ No input found")
            return False

    editor.click()
    time.sleep(0.5)
    # For contenteditable, use keyboard.type or insertText
    page.keyboard.insert_text(prompt)
    time.sleep(1)

    # Send button
    for sel in ['button[aria-label*="Send"]', 'button[aria-label*="Отправить"]',
                'button[aria-label*="send"]', 'button[aria-label*="Submit"]']:
        try:
            btn = page.locator(sel).first
            if btn.is_visible(timeout=2000) and btn.is_enabled(timeout=1000):
                _mouse_click(page, btn)
                print("   ✅ Sent")
                return True
        except:
            pass

    page.keyboard.press("Enter")
    print("   ✅ Sent (Enter)")
    return True


def confirm_plan(page):
    """Click 'Start research' / 'Начать исследование' when plan confirmation appears.

    The button may be below the viewport — aggressively scroll before checking.
    """
    print("   Waiting for research plan...")

    # Selectors for the start button (EN + RU + aria-label variants)
    BTN_SELECTORS = [
        'button[aria-label="Start research"]',
        'button[aria-label="Начать исследование"]',
        'button:has-text("Start research")',
        'button:has-text("Начать исследование")',
    ]

    for attempt in range(36):  # up to 3 min
        time.sleep(5)

        # Aggressively scroll down to reveal the button
        page.evaluate('() => window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(0.5)
        # Also scroll any overflow containers that Gemini uses
        page.evaluate('''() => {
            document.querySelectorAll('[class*="scroll"], [class*="container"], main, [role="main"]').forEach(el => {
                if (el.scrollHeight > el.clientHeight + 100) {
                    el.scrollTop = el.scrollHeight;
                }
            });
        }''')
        time.sleep(1)

        for sel in BTN_SELECTORS:
            btn = page.locator(sel)
            try:
                if btn.last.is_visible(timeout=2000):
                    btn.last.scroll_into_view_if_needed()
                    time.sleep(0.5)
                    # Playwright .click() silently fails on this button — use JS click
                    btn.last.evaluate('el => el.click()')
                    print(f"   → Clicked: {sel}")
                    time.sleep(5)
                    # Verify research started (stop button appears)
                    stop = page.locator('button[aria-label*="Остановить"], button[aria-label*="Stop"]')
                    try:
                        if stop.count() > 0 and stop.first.is_visible(timeout=3000):
                            print("   ✅ Research started!")
                            return True
                    except:
                        pass
                    print("   ⚠️  Click may have missed, retrying...")
                    break  # retry outer loop
            except:
                pass

        if attempt % 6 == 5:
            print(f"   ⏳ Still waiting for plan... ({(attempt+1)*5}s)")

    # Maybe it started automatically
    print("   ℹ️  No plan confirmation found, continuing")
    return True


def wait_research(page):
    """Wait for Deep Research to complete.

    Reliable signal: the side panel button "Поделиться и экспортировать"
    only appears after the full report is generated (not during plan phase).
    We also check that the stop button is gone and enough time has passed.
    """
    start = time.time()
    last_log = 0

    while time.time() - start < RESEARCH_TIMEOUT:
        elapsed = int(time.time() - start)

        # Primary completion signal: "Поделиться и экспортировать" panel button
        share_panel = page.locator('button:has-text("Поделиться и экспортировать")')
        try:
            if share_panel.first.is_visible(timeout=2000) and elapsed > 60:
                print(f"   ✅ Research complete! ({elapsed // 60}m{elapsed % 60}s)")
                return True
        except:
            pass

        if elapsed - last_log >= 60:
            last_log = elapsed
            # Check stop button for status
            stop_btn = page.locator('button[aria-label*="Остановить"], button[aria-label*="Stop"]')
            try:
                generating = stop_btn.count() > 0 and stop_btn.first.is_visible(timeout=1000)
            except:
                generating = False
            txt_len = len(page.evaluate('() => document.body.innerText') or '')
            status = "generating" if generating else "waiting"
            print(f"   ⏳ {elapsed // 60}min... ({txt_len:,} chars, {status})")

        time.sleep(15)

    _screenshot(page, "timeout")
    print("   ❌ Timeout waiting for research")
    return False


def export_to_docs(page, context):
    """Export Deep Research result via Google Docs download.

    Flow: open side panel → click Export → wait for Docs tab →
          download as .txt via export URL → cleanup tabs.
    """
    time.sleep(2)

    # Step 1: Open "Поделиться и экспортировать" side panel
    panel_btn = page.locator('button:has-text("Поделиться и экспортировать")')
    try:
        panel_btn.last.scroll_into_view_if_needed()
        time.sleep(1)
        panel_btn.last.click()
        time.sleep(3)
        print("   → Opened share panel")
    except Exception as e:
        print(f"   ⚠️  Share panel click issue: {e}")

    # Step 2: Click "Экспортировать в Документы" — wait for new tab
    pages_before = set(id(p) for p in context.pages)

    export_clicked = False
    for sel in ['button:has-text("Экспортировать в Документы")',
                'button:has-text("Export to Docs")']:
        try:
            btn = page.locator(sel)
            if btn.count() > 0 and btn.last.is_visible(timeout=5000):
                btn.last.scroll_into_view_if_needed()
                time.sleep(0.5)
                btn.last.click()
                print("   ✅ Clicked Export to Docs")
                export_clicked = True
                break
        except:
            pass

    if not export_clicked:
        print("   ❌ Export button not found")
        _screenshot(page, "no_export")
        return _fallback(page)

    # Step 3: Wait for Google Docs tab to appear and load
    # Tab may open as about:blank first, then redirect to docs.google.com
    docs_page = None
    for attempt in range(30):  # 60 seconds max
        time.sleep(2)
        for pg in context.pages:
            try:
                url = pg.url
                if "docs.google.com/document" in url:
                    docs_page = pg
                    break
                # Also check about:blank pages that might redirect
                if url == "about:blank" and pg != page:
                    try:
                        pg.wait_for_url("**/docs.google.com/**", timeout=5000)
                        if "docs.google.com/document" in pg.url:
                            docs_page = pg
                            break
                    except:
                        pass
            except:
                pass
        if docs_page:
            break

    if not docs_page:
        print("   ❌ Google Docs tab didn't open")
        _screenshot(page, "no_docs_tab")
        return _fallback(page)

    # Step 4: Wait for Docs to fully load
    try:
        docs_page.wait_for_load_state("domcontentloaded", timeout=30000)
    except:
        pass
    time.sleep(5)

    # Extract doc ID
    try:
        doc_id = docs_page.url.split("/d/")[1].split("/")[0]
        print(f"   📄 Doc ID: {doc_id}")
    except Exception as e:
        print(f"   ❌ Failed to parse doc ID from {docs_page.url}: {e}")
        return _fallback(page)

    # Step 5: Download as plain text via export URL
    export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=txt"
    content = None
    try:
        with docs_page.expect_download(timeout=30000) as download_info:
            docs_page.evaluate(f'() => window.open("{export_url}")')
        download = download_info.value
        tmp_path = str(OUTPUT_DIR / "_tmp_export.txt")
        download.save_as(tmp_path)
        with open(tmp_path) as f:
            content = f.read()
        os.remove(tmp_path)
        print(f"   ✅ Exported {len(content):,} chars from Docs")
    except Exception as e:
        print(f"   ⚠️  Download failed ({e}), trying fallback")

    # Step 6: Close all non-Gemini tabs
    for pg in list(context.pages):
        if pg != page and "gemini.google.com" not in pg.url:
            try:
                pg.close()
            except:
                pass

    if content and len(content) > 100:
        return content
    return _fallback(page)


def _fallback(page):
    """Extract from Gemini page directly."""
    try:
        content = page.evaluate("""() => {
            const sels = ['.response-container','.model-response','.markdown-content'];
            for (const s of sels) {
                const els = document.querySelectorAll(s);
                if (els.length) return Array.from(els).map(e=>e.innerText).join('\\n\\n');
            }
            return document.body.innerText;
        }""")
        if content and len(content) > 200:
            print(f"   ✅ {len(content):,} chars (fallback)")
            return content
    except:
        pass
    return None


def _check_rate_limit(page):
    """Check if Deep Research rate limit hit. Returns minutes to wait, or 0."""
    try:
        text = page.locator('body').inner_text()
        # Only match exact Russian rate limit message (avoid false positives)
        if 'исчерпали лимит' in text or 'exhausted your limit' in text.lower():
            import re
            m = re.search(r'в (\d{1,2}):(\d{2})', text)
            if m:
                from datetime import datetime
                now = datetime.now()
                target_h, target_m = int(m.group(1)), int(m.group(2))
                target = now.replace(hour=target_h, minute=target_m, second=0)
                if target < now:
                    target = target.replace(day=target.day + 1)
                wait_mins = max(1, int((target - now).total_seconds() / 60) + 2)
                return wait_mins
            return 60
    except:
        pass
    return 0


# ── Full research cycle ────────────────────────────────────

def do_research(page, context, prompt, output_file=None):
    """One Deep Research task. Browser stays open."""
    print(f"\n{'─' * 60}")
    print(f"🔬 {prompt[:100]}...")
    print(f"{'─' * 60}")

    navigate_deep_research(page)

    if not enter_prompt(page, prompt):
        return None

    confirm_plan(page)

    # Check for rate limit after prompt/plan
    wait_mins = _check_rate_limit(page)
    if wait_mins > 0:
        print(f"   ⏳ Rate limit hit! Waiting {wait_mins} min...")
        time.sleep(wait_mins * 60)
        # Retry from scratch
        return do_research(page, context, prompt, output_file)

    print(f"   ⏳ Waiting (up to {RESEARCH_TIMEOUT // 60}min)...")
    if not wait_research(page):
        return None

    content = export_to_docs(page, context)

    if content and output_file:
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        Path(output_file).write_text(content)
        print(f"   💾 {output_file} ({len(content):,} chars)")

    return content


# ── Main ───────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gemini Deep Research (Chrome + CDP)")
    parser.add_argument("--prompt", "-p")
    parser.add_argument("--prompt-file", "-f")
    parser.add_argument("--output", "-o")
    parser.add_argument("--tasks-dir")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    parser.add_argument("--email")
    parser.add_argument("--password")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--dump-ui", action="store_true")
    parser.add_argument("--no-wait", action="store_true",
                        help="Exit after research instead of waiting for Ctrl+C")
    args = parser.parse_args()

    email, password = _load_creds(args.email, args.password)
    if not email or not password:
        print("❌ Set GEMINI_EMAIL / GEMINI_PASSWORD in config/keys.env")
        return

    profile = _profile_dir(email)
    print(f"🌐 Launching Chrome...")
    print(f"   Account: {email}")
    print(f"   Profile: {profile}\n")

    chrome_proc, cdp_port = get_or_launch_chrome(profile)

    try:
        with sync_playwright() as pw:
            browser = connect_cdp(pw, cdp_port)
            if not browser:
                return

            ctx = browser.contexts[0] if browser.contexts else browser.new_context()
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            setup_stealth(ctx, page)

            if not login(page, email, password):
                print("❌ Login failed")
                return

            # ── dump-ui ──
            if args.dump_ui:
                navigate_deep_research(page)
                for el in _dump_ui(page):
                    if el.get("text") or el.get("ariaLabel"):
                        print(f"  {el['tag']:10} '{el['text'][:50]}' "
                              f"aria='{el['ariaLabel'][:30]}' {el.get('role','')}")
                _screenshot(page, "dump_ui")
                print("\n⏸️  Ctrl+C to close.")
                _keep_alive()
                return

            # ── test ──
            if args.test:
                prompt = (
                    "Research Section 230 of the Communications Decency Act application to "
                    "AI-generated adult content platforms in 2024-2026. "
                    "Focus on: Does Section 230 protect platforms hosting AI-generated content? "
                    "Recent court cases involving AI content and Section 230."
                )
                do_research(page, ctx, prompt, str(OUTPUT_DIR / "test_section230_gemini.md"))
                print("\n⏸️  Ctrl+C to close.")
                _keep_alive()
                return

            # ── single ──
            if args.prompt or args.prompt_file:
                prompt = args.prompt or Path(args.prompt_file).read_text().strip()
                out = args.output or str(OUTPUT_DIR / "result_gemini.md")
                do_research(page, ctx, prompt, out)
                if not args.no_wait:
                    print("\n⏸️  Ctrl+C to close.")
                    _keep_alive()
                return

            # ── batch ──
            if args.tasks_dir:
                out_dir = Path(args.output_dir)
                out_dir.mkdir(parents=True, exist_ok=True)
                tasks = sorted(Path(args.tasks_dir).glob("*.txt"))
                print(f"📋 {len(tasks)} tasks\n")
                for i, tf in enumerate(tasks):
                    topic = tf.stem
                    out_file = out_dir / f"{topic}_gemini.md"
                    if out_file.exists():
                        print(f"⏭️  [{i + 1}/{len(tasks)}] {topic} — done")
                        continue
                    print(f"\n📌 [{i + 1}/{len(tasks)}] {topic}")
                    result = do_research(page, ctx, tf.read_text().strip(), str(out_file))
                    if not result:
                        page.goto(f"{GEMINI_URL}/app", timeout=60000)
                        time.sleep(5)
                print("\n✅ All done!")
                _keep_alive()
                return

            # ── interactive ──
            print("🎮 Interactive. Ctrl+C to exit.\n")
            n = 0
            try:
                while True:
                    p = input("📝 Prompt: ").strip()
                    if not p or p.lower() in ("quit", "exit", "q"):
                        break
                    n += 1
                    do_research(page, ctx, p, str(OUTPUT_DIR / f"i_{n}_gemini.md"))
            except (KeyboardInterrupt, EOFError):
                pass

    finally:
        # NEVER close Chrome — it stays open for next run
        pid = chrome_proc.pid if chrome_proc else "reconnected"
        print(f"\n✅ Script done. Chrome stays open (PID: {pid}).")
        print("   Reconnect with: python3 gemini_runner.py ...")


def _keep_alive():
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
