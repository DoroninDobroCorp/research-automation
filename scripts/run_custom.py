#!/usr/bin/env python3
"""
Full-auto research pipeline: launch all engines in parallel, wait for all,
consolidate via Claude Opus, notify user.

Usage:
    python3 scripts/run_custom.py -f output/prompts/proxy-research.txt -s proxy-research
    python3 scripts/run_custom.py -f prompt.txt -s my-topic --engines parallel,gemini
    python3 scripts/run_custom.py -f prompt.txt -s my-topic --no-consolidate
"""
import argparse
import os
import platform
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

MODULE_ROOT = Path(__file__).parent.parent
ENGINES_DIR = MODULE_ROOT / "engines"
RAW_DIR = MODULE_ROOT / "output" / "raw"
CONSOLIDATED_DIR = MODULE_ROOT / "output" / "consolidated"

ALL_ENGINES = ["parallel", "gemini", "perplexity"]
ENGINE_SCRIPTS = {
    "parallel": "parallel_client.py",
    "gemini": "gemini_runner.py",
    "perplexity": "perplexity_runner.py",
}


# ── Notification ───────────────────────────────────────────

def notify_user(title: str, message: str):
    """Send desktop notification (macOS/Linux)."""
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}" sound name "Glass"'
            ], timeout=5)
        elif system == "Linux":
            subprocess.run(["notify-send", title, message], timeout=5)
    except Exception:
        pass
    # Also print with bell character
    print(f"\a\n{'🔔' * 10}")
    print(f"🔔  {title}")
    print(f"🔔  {message}")
    print(f"{'🔔' * 10}\n")


# ── Engine runner (thread-safe) ────────────────────────────

def run_engine_thread(engine: str, prompt_file: Path, output_file: Path,
                      results: dict, lock: threading.Lock):
    """Run one engine in a thread. Stores result in results dict."""
    script = ENGINE_SCRIPTS[engine]
    cmd = [
        sys.executable,
        str(ENGINES_DIR / script),
        "--prompt-file", str(prompt_file),
        "--output", str(output_file),
    ]
    # --no-wait only for browser engines (gemini, perplexity)
    if engine in ("gemini", "perplexity"):
        cmd.append("--no-wait")
        cmd.append("--close-browser")

    env = dict(os.environ, PYTHONPATH=str(MODULE_ROOT))
    start = time.time()

    with lock:
        print(f"🚀 [{engine}] Starting {script}...")

    try:
        proc = subprocess.run(
            cmd, cwd=str(MODULE_ROOT), env=env,
            capture_output=True, text=True,
            timeout=7200,  # 2 hour max per engine
        )
        elapsed = int(time.time() - start)
        success = (
            proc.returncode == 0
            and output_file.exists()
            and output_file.stat().st_size > 100
        )

        # Detect specific failure reasons from stderr/stdout
        output_text = (proc.stdout or "") + (proc.stderr or "")
        failure_reason = None
        if not success:
            if "402" in output_text or "Insufficient credit" in output_text:
                failure_reason = "NO_BALANCE"
            elif "401" in output_text or "Unauthorized" in output_text:
                failure_reason = "BAD_KEY"
            elif "429" in output_text or "rate limit" in output_text.lower():
                failure_reason = "RATE_LIMIT"
            elif "All API keys exhausted" in output_text:
                failure_reason = "ALL_KEYS_EXHAUSTED"
            elif "Login" in output_text and "failed" in output_text.lower():
                failure_reason = "LOGIN_FAILED"
            elif "Chrome not found" in output_text:
                failure_reason = "NO_CHROME"
            else:
                failure_reason = "UNKNOWN"

        with lock:
            if success:
                size = output_file.stat().st_size
                print(f"✅ [{engine}] Done in {_fmt_time(elapsed)} — {size:,} chars")
                results[engine] = {"success": True, "chars": size, "time": elapsed}
            else:
                print(f"❌ [{engine}] Failed (rc={proc.returncode}, {_fmt_time(elapsed)})")
                results[engine] = {
                    "success": False, "time": elapsed,
                    "reason": failure_reason, "output": output_text[-500:],
                }

    except subprocess.TimeoutExpired:
        elapsed = int(time.time() - start)
        with lock:
            print(f"⏰ [{engine}] Timeout after {_fmt_time(elapsed)}")
            results[engine] = {"success": False, "time": elapsed, "reason": "TIMEOUT"}
    except Exception as e:
        elapsed = int(time.time() - start)
        with lock:
            print(f"💥 [{engine}] Error: {e}")
            results[engine] = {"success": False, "time": elapsed, "reason": "EXCEPTION", "error": str(e)}


def _fmt_time(seconds: int) -> str:
    if seconds < 60:
        return f"{seconds}s"
    return f"{seconds // 60}m{seconds % 60:02d}s"


FAILURE_HINTS = {
    "NO_BALANCE": "💳 API ключ без баланса. Пополни на https://platform.parallel.ai/settings?tab=billing",
    "BAD_KEY": "🔑 API ключ невалидный. Проверь config/keys.env",
    "RATE_LIMIT": "⏱️  Rate limit. Подожди и попробуй снова",
    "ALL_KEYS_EXHAUSTED": "🔑 Все API ключи исчерпаны. Нужен новый ключ в config/keys.env",
    "LOGIN_FAILED": "🔐 Не удалось залогиниться. Проверь email/password в config/keys.env",
    "NO_CHROME": "🌐 Chrome не найден. Установи Google Chrome",
    "TIMEOUT": "⏰ Таймаут (>2ч). Попробуй снова — возможно сервис был перегружен",
}


def _ask_retry(engine: str, reason: str, output_snippet: str) -> str:
    """Ask user what to do with a failed engine. Returns: retry/skip/abort."""
    hint = FAILURE_HINTS.get(reason, f"Неизвестная ошибка: {reason}")

    print(f"\n{'⚠️' * 20}")
    print(f"⚠️  [{engine.upper()}] FAILED — {hint}")
    if reason in ("NO_BALANCE", "BAD_KEY", "ALL_KEYS_EXHAUSTED"):
        print(f"    Файл ключей: {MODULE_ROOT / 'config' / 'keys.env'}")
    if output_snippet:
        # Show last few meaningful lines
        lines = [l for l in output_snippet.strip().splitlines() if l.strip()][-5:]
        print(f"    Последний вывод:")
        for l in lines:
            print(f"      {l}")
    print(f"{'⚠️' * 20}")

    while True:
        print(f"\n  [R] Retry — исправь проблему и нажми R")
        print(f"  [S] Skip  — пропустить этот источник")
        print(f"  [A] Abort — прервать весь пайплайн")
        try:
            choice = input(f"\n  [{engine}] Что делаем? (R/S/A): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            return "abort"
        if choice in ("R", "RETRY", ""):
            return "retry"
        elif choice in ("S", "SKIP"):
            return "skip"
        elif choice in ("A", "ABORT"):
            return "abort"
        print("  → Введи R, S или A")


# ── Consolidation ─────────────────────────────────────────

def consolidate(slug: str) -> bool:
    """Run consolidate_custom.py and return success."""
    print(f"\n{'━' * 60}")
    print("▶ Consolidating all sources via Claude Opus...")
    print(f"{'━' * 60}")

    # Remove old consolidated file if exists
    for f in CONSOLIDATED_DIR.glob(f"{slug}*"):
        f.unlink()

    cmd = [
        sys.executable,
        str(MODULE_ROOT / "scripts" / "consolidate_custom.py"),
        "--slug", slug,
    ]
    env = dict(os.environ, PYTHONPATH=str(MODULE_ROOT))

    proc = subprocess.run(cmd, cwd=str(MODULE_ROOT), env=env, timeout=900)

    # Check for output (copilot may create file with different name)
    consolidated_files = list(CONSOLIDATED_DIR.glob(f"{slug}*"))
    if consolidated_files:
        total = sum(f.stat().st_size for f in consolidated_files)
        if total > 500:
            print(f"✅ Consolidated: {', '.join(f.name for f in consolidated_files)} ({total:,} chars)")
            return True

    print("❌ Consolidation failed or produced empty output")
    return False


# ── Main ───────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Full-auto research: all engines → consolidate → notify",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s -f prompts/proxy.txt -s proxy-research
  %(prog)s -f prompts/proxy.txt -s proxy-research --engines parallel,gemini
  %(prog)s -f prompts/proxy.txt -s proxy-research --no-consolidate
  %(prog)s -f prompts/proxy.txt -s proxy-research --reuse-existing""",
    )
    parser.add_argument("--prompt-file", "-f", required=True, help="Prompt text file")
    parser.add_argument("--slug", "-s", required=True, help="Output filename slug")
    parser.add_argument("--engines", "-e", default="all",
                        help="Engines: 'all' or comma-separated (parallel,gemini,perplexity)")
    parser.add_argument("--no-consolidate", action="store_true",
                        help="Skip consolidation step")
    parser.add_argument("--reuse-existing", action="store_true",
                        help="Don't re-run engines that already have output")
    parser.add_argument("--allow-partial", action="store_true",
                        help="Allow consolidation with fewer sources (default: require ALL)")
    parser.add_argument("--non-interactive", action="store_true",
                        help="Don't ask for retry — fail immediately on errors")
    args = parser.parse_args()

    prompt_file = Path(args.prompt_file)
    if not prompt_file.is_absolute():
        prompt_file = MODULE_ROOT / prompt_file
    if not prompt_file.exists():
        print(f"❌ Prompt file not found: {prompt_file}")
        sys.exit(1)

    # Parse engine list
    if args.engines == "all":
        engines = list(ALL_ENGINES)
    else:
        engines = [e.strip() for e in args.engines.split(",")]
        for e in engines:
            if e not in ALL_ENGINES:
                print(f"❌ Unknown engine: {e}. Available: {', '.join(ALL_ENGINES)}")
                sys.exit(1)

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    CONSOLIDATED_DIR.mkdir(parents=True, exist_ok=True)
    slug = args.slug

    # ── Header ──
    start_time = time.time()
    print(f"\n{'═' * 60}")
    print(f"🔬 RESEARCH PIPELINE — {slug}")
    print(f"   Prompt: {prompt_file.name}")
    print(f"   Engines: {', '.join(engines)}")
    print(f"   Started: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'═' * 60}")

    # ── Skip already-done engines ──
    engines_to_run = []
    for engine in engines:
        out = RAW_DIR / f"{slug}_{engine}.md"
        if args.reuse_existing and out.exists() and out.stat().st_size > 100:
            print(f"⏭️  [{engine}] Already done ({out.stat().st_size:,} chars)")
        else:
            engines_to_run.append(engine)

    # ── Launch engines with retry loop ──
    results = {}
    lock = threading.Lock()
    skipped_engines = []

    while engines_to_run:
        # Launch all pending engines in parallel
        print(f"\n🚀 Launching {len(engines_to_run)} engine(s) in parallel...")
        threads = []
        batch_results = {}
        for engine in engines_to_run:
            out = RAW_DIR / f"{slug}_{engine}.md"
            t = threading.Thread(
                target=run_engine_thread,
                args=(engine, prompt_file, out, batch_results, lock),
                name=f"engine-{engine}",
                daemon=True,
            )
            threads.append(t)
            t.start()

        # Wait for all threads
        print(f"⏳ Waiting for all engines (up to 2h)...\n")
        while not all(not t.is_alive() for t in threads):
            alive = [t.name.replace("engine-", "") for t in threads if t.is_alive()]
            elapsed = int(time.time() - start_time)
            with lock:
                print(f"   ⏳ [{_fmt_time(elapsed)}] Still running: {', '.join(alive)}")
            time.sleep(30)

        for t in threads:
            t.join(timeout=5)

        results.update(batch_results)

        # Check which engines failed
        failed_engines = []
        for engine in engines_to_run:
            r = batch_results.get(engine, {})
            out = RAW_DIR / f"{slug}_{engine}.md"
            if out.exists() and out.stat().st_size > 100:
                continue  # success
            failed_engines.append(engine)

        if not failed_engines:
            break  # all good!

        # Handle failures — ask user for each
        engines_to_run = []  # will be repopulated with retries
        for engine in failed_engines:
            r = batch_results.get(engine, {})
            reason = r.get("reason", "UNKNOWN")
            output_snippet = r.get("output", "")

            if args.non_interactive:
                print(f"\n❌ [{engine}] Failed: {FAILURE_HINTS.get(reason, reason)}")
                skipped_engines.append(engine)
                continue

            # Notify user with sound so they come back
            notify_user(
                f"⚠️ {engine.upper()} failed!",
                FAILURE_HINTS.get(reason, f"Error: {reason}")
            )

            action = _ask_retry(engine, reason, output_snippet)
            if action == "retry":
                engines_to_run.append(engine)
                print(f"   🔄 [{engine}] Will retry...")
            elif action == "skip":
                skipped_engines.append(engine)
                print(f"   ⏭️  [{engine}] Skipped by user")
            elif action == "abort":
                print(f"\n🛑 Aborted by user")
                sys.exit(1)

        if engines_to_run:
            print(f"\n🔄 Retrying {len(engines_to_run)} engine(s): {', '.join(engines_to_run)}")

    # ── Summary ──
    total_elapsed = int(time.time() - start_time)
    print(f"\n{'═' * 60}")
    print(f"📊 ENGINE RESULTS ({_fmt_time(total_elapsed)} total)")
    print(f"{'═' * 60}")

    done_count = 0
    for engine in engines:
        out = RAW_DIR / f"{slug}_{engine}.md"
        if out.exists() and out.stat().st_size > 100:
            print(f"  ✅ {engine}: {out.stat().st_size:,} chars")
            done_count += 1
        elif engine in skipped_engines:
            r = results.get(engine, {})
            reason = r.get("reason", "skipped")
            print(f"  ⏭️  {engine}: SKIPPED ({reason})")
        elif engine in results:
            r = results[engine]
            reason = r.get("reason", "unknown")
            print(f"  ❌ {engine}: FAILED ({reason})")
        else:
            print(f"  ⬜ {engine}: not run")

    # ── Consolidation ──
    min_sources = 2 if args.allow_partial else len(engines)

    if args.no_consolidate:
        print(f"\n⏭️  Consolidation skipped (--no-consolidate)")
    elif done_count >= min_sources:
        ok = consolidate(slug)
        if ok:
            notify_user(
                "✅ Research Complete!",
                f"{slug}: {done_count}/{len(engines)} sources → consolidated"
            )
        else:
            notify_user(
                "⚠️ Research Partial",
                f"{slug}: {done_count} sources done, consolidation failed"
            )
    elif done_count > 0:
        print(f"\n❌ Only {done_count}/{len(engines)} sources — ALL required for consolidation")
        print(f"   Use --allow-partial to consolidate with fewer sources")
        notify_user(
            "❌ Research Incomplete",
            f"{slug}: only {done_count}/{len(engines)} sources (all required)"
        )
    else:
        print(f"\n❌ All engines failed!")
        notify_user("❌ Research Failed", f"{slug}: all engines failed")

    # ── Final paths ──
    print(f"\n{'═' * 60}")
    print("📁 Output files:")
    for f in sorted(RAW_DIR.glob(f"{slug}_*")):
        print(f"   {f}")
    for f in sorted(CONSOLIDATED_DIR.glob(f"{slug}*")):
        print(f"   🏆 {f}")
    print(f"{'═' * 60}")

    total_elapsed = int(time.time() - start_time)
    print(f"\n⏱️  Total time: {_fmt_time(total_elapsed)}")


if __name__ == "__main__":
    main()
