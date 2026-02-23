#!/usr/bin/env python3
"""
Perplexity Deep Research Runner — persistent Chrome via subprocess + CDP.

Browser starts ONCE and stays open between tasks.

Usage:
    python3 perplexity_runner.py --dump-ui
    python3 perplexity_runner.py -p "prompt" -o out.md
    python3 perplexity_runner.py --prompt-file prompt.txt -o out.md --no-wait
    python3 perplexity_runner.py --tasks-dir tasks/ --output-dir output/
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
STATE_FILE = Path(__file__).parent.parent / "config" / ".chrome_perplexity_state.json"
PERPLEXITY_URL = "https://www.perplexity.ai"
RESEARCH_TIMEOUT = 45 * 60  # 45 min max

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
            email or creds.get("PERPLEXITY_EMAIL", ""),
            password or creds.get("PERPLEXITY_PASSWORD", ""),
        )
    return email or "", password or ""


def _profile_dir(email):
    slug = email.split("@")[0].replace(".", "_")
    d = PROFILES_DIR / f"perplexity_{slug}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _screenshot(page, name):
    out = OUTPUT_DIR / f"perplexity_{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        page.screenshot(path=str(out))
        print(f"   📸 {out}")
    except:
        pass


def _human_type(page, text):
    for ch in text:
        page.keyboard.type(ch, delay=random.randint(45, 110))
        time.sleep(random.uniform(0.02, 0.07))


def _mouse_click(page, locator):
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
        "--window-size=1440,900",
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

    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({
        "pid": proc.pid, "port": port, "profile": str(profile_dir)
    }))

    return proc, port


def _chrome_alive(pid):
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def _cdp_alive(port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect(("127.0.0.1", port))
        s.close()
        return True
    except:
        return False


def get_or_launch_chrome(profile_dir):
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
            pid, port = state["pid"], state["port"]
            if _chrome_alive(pid) and _cdp_alive(port):
                print(f"   ♻️  Reconnecting to Chrome (PID: {pid}, CDP: {port})")
                return None, port
        except:
            pass
    return launch_chrome(profile_dir)


def connect_cdp(pw, port):
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
    try:
        client = context.new_cdp_session(page)
        client.send("Page.addScriptToEvaluateOnNewDocument", {"source": STEALTH_SCRIPT})
        client.send("Page.setBypassCSP", {"enabled": True})
    except:
        pass


# ── Login ──────────────────────────────────────────────────

def login(page, email, password):
    """Login to Perplexity. Check if already logged in first."""
    print("   Checking login...")

    page.goto(f"{PERPLEXITY_URL}", timeout=60000)
    time.sleep(5)

    # Check if already logged in — look for the ask-input or user menu
    ask_input = page.locator('#ask-input')
    if ask_input.count() > 0:
        # Verify it's a logged-in state (check for model chooser — Pro feature)
        model_btn = page.locator('button[aria-label="Choose a model"]')
        if model_btn.count() > 0:
            print("   ✅ Already logged in (Pro)")
            return True
        # Still might be logged in
        print("   ✅ Already logged in")
        return True

    signin_btn = page.locator('button:has-text("Sign In"), button:has-text("Log In"), a:has-text("Sign In"), a:has-text("Log In")')
    if signin_btn.count() == 0:
        if page.locator('[data-testid="user-menu"], button:has-text("Library"), a[href="/library"]').count() > 0:
            print("   ✅ Already logged in")
            return True
        if page.locator('textarea, input[placeholder]').count() > 0:
            print("   ✅ Appears logged in (search box present)")
            return True

    # Need to log in
    print("   → Logging in...")
    _screenshot(page, "before_login")

    # Click Sign In
    try:
        signin_btn.first.click()
        time.sleep(3)
    except:
        # Try navigating directly to login
        page.goto(f"{PERPLEXITY_URL}/login", timeout=30000)
        time.sleep(3)

    _screenshot(page, "login_page")

    # Look for email input or "Continue with email" option
    email_option = page.locator('button:has-text("email"), button:has-text("Email"), a:has-text("email")')
    if email_option.count() > 0:
        email_option.first.click()
        time.sleep(2)

    # Enter email
    email_input = page.locator('input[type="email"], input[name="email"], input[placeholder*="email" i]')
    if email_input.count() > 0:
        email_input.first.click()
        time.sleep(0.5)
        _human_type(page, email)
        time.sleep(1)

        # Submit email
        submit_btn = page.locator('button[type="submit"], button:has-text("Continue"), button:has-text("Next"), button:has-text("Продолжить")')
        if submit_btn.count() > 0:
            submit_btn.first.click()
            time.sleep(3)

    _screenshot(page, "after_email")

    # Enter password
    pw_input = page.locator('input[type="password"]')
    if pw_input.count() > 0:
        pw_input.first.click()
        time.sleep(0.5)
        _human_type(page, password)
        time.sleep(1)

        submit_btn = page.locator('button[type="submit"], button:has-text("Log In"), button:has-text("Sign In"), button:has-text("Continue")')
        if submit_btn.count() > 0:
            submit_btn.first.click()
            time.sleep(5)

    _screenshot(page, "after_password")

    # Verify login
    page.wait_for_load_state("networkidle", timeout=15000)
    time.sleep(3)

    if page.locator('[data-testid="user-menu"], button:has-text("Library"), textarea').count() > 0:
        print("   ✅ Logged in!")
        return True

    print("   ❌ Login may have failed")
    _screenshot(page, "login_result")
    return False


# ── Deep Research UI flow ─────────────────────────────────

def dump_ui(page):
    """Dump all visible interactive elements for debugging."""
    elements = page.evaluate("""() => {
        const els = document.querySelectorAll('button, a, input, textarea, [role="button"], [role="tab"], [role="option"]');
        return Array.from(els).slice(0, 100).map(el => ({
            tag: el.tagName,
            text: (el.textContent || '').trim().slice(0, 80),
            ariaLabel: el.getAttribute('aria-label') || '',
            placeholder: el.getAttribute('placeholder') || '',
            role: el.getAttribute('role') || '',
            type: el.getAttribute('type') || '',
            href: el.getAttribute('href') || '',
            visible: el.offsetParent !== null,
        }));
    }""")
    return elements


def enter_prompt(page, prompt):
    """Enter research prompt into Perplexity contenteditable div."""
    ask = page.locator('#ask-input')
    if ask.count() == 0:
        # Fallback to textarea
        textarea = page.locator('textarea')
        if textarea.count() == 0:
            print("   ❌ No input found")
            _screenshot(page, "no_input")
            return False
        textarea.last.click()
        time.sleep(0.5)
        textarea.last.fill(prompt)
        time.sleep(1)
        print(f"   ✅ Prompt entered via textarea ({len(prompt)} chars)")
        return True

    ask.click()
    time.sleep(0.5)
    # Clear existing text
    ask.evaluate('el => el.innerText = ""')
    time.sleep(0.3)
    # Type prompt (keyboard for natural input)
    page.keyboard.type(prompt, delay=15)
    time.sleep(1)
    print(f"   ✅ Prompt entered ({len(prompt)} chars)")
    return True


def select_deep_research(page):
    """Select Deep Research mode via 'Add files or tools' menu."""
    # Check if Deep Research badge is already shown near input
    dr_badge = page.locator('button:has-text("Deep research"), span:has-text("Deep research")')
    # Filter to ones near the input area (not in answer)
    for i in range(dr_badge.count()):
        try:
            box = dr_badge.nth(i).bounding_box()
            if box and box['y'] > 300:  # Near bottom where input is
                print("   ✅ Deep Research already active")
                return True
        except:
            pass

    # Click "Add files or tools" button
    tools_btn = page.locator('button[aria-label="Add files or tools"]')
    if tools_btn.count() > 0 and tools_btn.first.is_visible():
        tools_btn.first.click()
        time.sleep(2)

        # Click "Deep research" from popup menu
        dr_option = page.locator('text=Deep research')
        if dr_option.count() > 0:
            dr_option.first.click()
            time.sleep(1)
            print("   ✅ Deep Research selected")
            return True

    # Fallback: try direct button click
    dr_btn = page.locator('button:has-text("Deep Research"), button:has-text("Research")')
    if dr_btn.count() > 0:
        dr_btn.first.click()
        time.sleep(2)
        print("   ✅ Deep Research selected (direct)")
        return True

    print("   ⚠️  Deep Research selector not found")
    _screenshot(page, "no_deep_research")
    return False


def submit_prompt(page):
    """Submit the prompt (press Enter or click submit)."""
    submit = page.locator('button[aria-label="Submit"], button[aria-label="Отправить"], button[type="submit"]')
    if submit.count() > 0 and submit.last.is_visible():
        submit.last.click()
        print("   ✅ Submitted")
        return True

    # Try Enter key
    page.keyboard.press("Enter")
    print("   ✅ Submitted (Enter)")
    return True


def wait_research(page):
    """Wait for Perplexity Deep Research to complete."""
    start = time.time()
    last_len = 0
    stable_count = 0

    # First quick checks (Deep Research may be fast for simple queries)
    for _ in range(6):
        time.sleep(10)
        text = page.locator('body').inner_text()
        # "Prepared by Deep Research" = done
        if 'Prepared by Deep Research' in text:
            elapsed = int(time.time() - start)
            print(f"   ✅ Research complete! ({elapsed}s, {len(text):,} chars)")
            return True

    while time.time() - start < RESEARCH_TIMEOUT:
        time.sleep(30)
        elapsed = int((time.time() - start) / 60)

        text = page.locator('body').inner_text()
        text_len = len(text)

        # Check for completion marker
        if 'Prepared by Deep Research' in text:
            print(f"   ✅ Research complete! ({elapsed}m, {text_len:,} chars)")
            return True

        # Check for "Ask a follow-up" prompt (another completion signal)
        if 'Ask a follow-up' in text and text_len > 3000:
            print(f"   ✅ Research complete (follow-up prompt visible, {elapsed}m, {text_len:,} chars)")
            return True

        # Stability check: if text stopped growing for 3 checks (90s) and is substantial
        if text_len > 5000 and text_len == last_len:
            stable_count += 1
            if stable_count >= 3:
                print(f"   ✅ Research appears complete (stable, {elapsed}m, {text_len:,} chars)")
                return True
        else:
            stable_count = 0

        print(f"   ⏳ {elapsed}min... ({text_len:,} chars)")
        last_len = text_len

    print(f"   ❌ Timeout after {RESEARCH_TIMEOUT // 60}min")
    return False


def extract_content(page):
    """Extract the research result text from Perplexity page."""
    # Try prose/markdown containers first
    content = page.evaluate("""() => {
        // Perplexity renders answer in .prose or similar containers
        const selectors = [
            '.prose', '.markdown-content', '[class*="answer"]',
            '[class*="response"]', 'article', '.post-text'
        ];
        for (const sel of selectors) {
            const els = document.querySelectorAll(sel);
            if (els.length) {
                const texts = Array.from(els).map(e => e.innerText).filter(t => t.length > 200);
                if (texts.length) return texts.join('\\n\\n');
            }
        }
        return null;
    }""")

    if content and len(content) > 500:
        print(f"   📄 Extracted via prose selector ({len(content):,} chars)")
        return content

    # Fallback: get body text and strip UI chrome
    text = page.locator('body').inner_text()
    if text:
        # Remove common UI elements from text
        lines = text.split('\n')
        # Skip navigation (first lines) and footer
        # Find the actual content start (after the query)
        content_lines = []
        in_content = False
        for line in lines:
            stripped = line.strip()
            if 'Reviewed' in stripped and 'source' in stripped:
                in_content = True
                continue
            if in_content:
                if stripped in ('Ask a follow-up', 'Deep research', 'Share'):
                    continue
                if stripped.startswith('History') or stripped.startswith('Discover'):
                    continue
                content_lines.append(line)

        if content_lines:
            result = '\n'.join(content_lines).strip()
            if len(result) > 200:
                print(f"   📄 Extracted via body text cleanup ({len(result):,} chars)")
                return result

    # Last resort: full body text
    if text and len(text) > 500:
        print(f"   📄 Extracted raw body text ({len(text):,} chars)")
        return text

    return None


# ── Full research cycle ────────────────────────────────────

def do_research(page, prompt, output_file=None):
    """One Deep Research task."""
    print(f"\n{'─' * 60}")
    print(f"🔬 {prompt[:100]}...")
    print(f"{'─' * 60}")

    # Navigate to home for fresh search
    page.goto(f"{PERPLEXITY_URL}", timeout=60000)
    time.sleep(5)

    # Select Deep Research mode FIRST (before entering prompt)
    select_deep_research(page)

    if not enter_prompt(page, prompt):
        return None

    submit_prompt(page)
    time.sleep(5)

    # Check if URL changed (research started)
    if '/search/' not in page.url:
        print("   ⚠️  URL didn't change, waiting...")
        time.sleep(10)

    print(f"   ⏳ Waiting (up to {RESEARCH_TIMEOUT // 60}min)...")
    if not wait_research(page):
        _screenshot(page, "timeout")
        # Still try to extract whatever we got
        content = extract_content(page)
        if content and len(content) > 1000:
            print(f"   ⚠️  Timeout but got {len(content):,} chars — saving partial")
        else:
            return None
    else:
        content = extract_content(page)

    if content and output_file:
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        Path(output_file).write_text(content)
        print(f"   💾 {output_file} ({len(content):,} chars)")

    return content


def _keep_alive():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


def _close_chrome(chrome_proc):
    """Terminate Chrome and clean up state file."""
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
            pid = state.get("pid")
            if pid and _chrome_alive(pid):
                os.kill(pid, 15)  # SIGTERM
                print(f"   🧹 Chrome closed (PID: {pid})")
            STATE_FILE.unlink()
        except Exception as e:
            print(f"   ⚠️  Chrome cleanup error: {e}")
    elif chrome_proc:
        try:
            chrome_proc.terminate()
            chrome_proc.wait(timeout=5)
            print(f"   🧹 Chrome closed (PID: {chrome_proc.pid})")
        except Exception:
            pass


# ── Main ───────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Perplexity Deep Research (Chrome + CDP)")
    parser.add_argument("--prompt", "-p")
    parser.add_argument("--prompt-file", "-f")
    parser.add_argument("--output", "-o")
    parser.add_argument("--tasks-dir")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR))
    parser.add_argument("--email")
    parser.add_argument("--password")
    parser.add_argument("--dump-ui", action="store_true")
    parser.add_argument("--no-wait", action="store_true")
    parser.add_argument("--close-browser", action="store_true",
                        help="Close Chrome after completion (used by pipeline)")
    args = parser.parse_args()

    email, password = _load_creds(args.email, args.password)
    if not email or not password:
        print("❌ Set PERPLEXITY_EMAIL / PERPLEXITY_PASSWORD in config/keys.env")
        return

    profile = _profile_dir(email)
    print(f"🌐 Launching Chrome for Perplexity...")
    print(f"   Account: {email}")
    print(f"   Profile: {profile}\n")

    chrome_proc, cdp_port = get_or_launch_chrome(profile)

    try:
        with sync_playwright() as pw:
            browser = connect_cdp(pw, cdp_port)
            if not browser:
                print("❌ CDP connection failed")
                return

            ctx = browser.contexts[0]
            page = ctx.pages[0] if ctx.pages else ctx.new_page()
            setup_stealth(ctx, page)

            if not login(page, email, password):
                print("❌ Login failed")
                _screenshot(page, "login_failed")
                if not args.no_wait:
                    print("\n⏸️  Ctrl+C to close. Browser stays open for debugging.")
                    _keep_alive()
                return

            # ── dump-ui ──
            if args.dump_ui:
                for el in dump_ui(page):
                    if el.get("visible") and (el.get("text") or el.get("ariaLabel")):
                        print(f"  {el['tag']:10} '{el['text'][:50]}' "
                              f"aria='{el['ariaLabel'][:30]}' {el.get('role','')}")
                _screenshot(page, "dump_ui")
                if not args.no_wait:
                    print("\n⏸️  Ctrl+C to close.")
                    _keep_alive()
                return

            # ── single prompt ──
            if args.prompt or args.prompt_file:
                prompt = args.prompt or Path(args.prompt_file).read_text().strip()
                out = args.output or str(OUTPUT_DIR / "result_perplexity.md")
                do_research(page, prompt, out)
                if not args.no_wait:
                    print("\n⏸️  Ctrl+C to close.")
                    _keep_alive()
                return

            # ── interactive ──
            print("🎮 Interactive. Ctrl+C to exit.\n")
            try:
                while True:
                    p = input("📝 Prompt: ").strip()
                    if not p or p.lower() in ("quit", "exit", "q"):
                        break
                    do_research(page, p, str(OUTPUT_DIR / f"perplexity_interactive.md"))
            except (KeyboardInterrupt, EOFError):
                pass

        print(f"\n✅ Script done. Chrome stays open (PID: {'reconnected' if not chrome_proc else chrome_proc.pid}).")

    except KeyboardInterrupt:
        print("\n⏹️  Interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if args.close_browser:
            _close_chrome(chrome_proc)


if __name__ == "__main__":
    main()
