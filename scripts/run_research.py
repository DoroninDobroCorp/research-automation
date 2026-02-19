#!/usr/bin/env python3
"""
Research Orchestrator — runs all 16 prompts through Parallel AI + Gemini.

Usage:
    python3 scripts/run_research.py --all                   # All prompts, both engines
    python3 scripts/run_research.py --engine parallel       # All prompts, Parallel AI only
    python3 scripts/run_research.py --engine gemini         # All prompts, Gemini only
    python3 scripts/run_research.py --topic section-230     # Single topic, both engines
    python3 scripts/run_research.py --list                  # List all prompts

Parallel AI runs fire-and-forget (API tasks run in cloud, we poll later).
Gemini runs sequentially (one browser, one at a time).
"""

import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from engines.parallel_client import ParallelClient, load_keys, COST_PER_QUERY
from engines.base import setup_logger, ResearchMetrics

log = setup_logger("orchestrator")

PROMPTS_FILE = Path(__file__).parent.parent.parent / "docs" / "research-prompts.md"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
TASKS_DIR = OUTPUT_DIR / "tasks"    # prompt files for Gemini batch mode
RAW_DIR = OUTPUT_DIR / "raw"


def parse_prompts(prompts_file: Path = PROMPTS_FILE) -> list[dict]:
    """Parse research-prompts.md → list of {slug, title, prompt}."""
    text = prompts_file.read_text()
    prompts: list[dict] = []

    # Split by ### Prompt X.Y: Title
    parts = re.split(r'### Prompt (\d+\.\d+): (.+)', text)
    # parts: [preamble, id1, title1, body1, id2, title2, body2, ...]

    for i in range(1, len(parts) - 2, 3):
        prompt_id = parts[i].strip()
        title = parts[i + 1].strip()
        body = parts[i + 2].strip()

        # Extract content between ``` markers
        m = re.search(r'```\n(.+?)\n```', body, re.DOTALL)
        if not m:
            continue

        prompt_text = m.group(1).strip()
        # Generate slug from id + title
        slug = f"{prompt_id.replace('.', '-')}_{title.lower()}"
        slug = re.sub(r'[^a-z0-9_-]', '-', slug)
        slug = re.sub(r'-+', '-', slug).strip('-')

        prompts.append({
            'id': prompt_id,
            'slug': slug,
            'title': title,
            'prompt': prompt_text,
        })

    return prompts


def run_parallel_all(prompts: list[dict], max_retries: int = 2) -> dict[str, str]:
    """Fire all prompts to Parallel AI, return {slug: run_id}."""
    keys = load_keys()
    client = ParallelClient(keys, processor="ultra8x")
    tasks: dict[str, str] = {}
    failed: list[dict] = []

    for p in prompts:
        out_file = RAW_DIR / f"{p['slug']}_parallel.md"
        if out_file.exists():
            log.info("⏭️  %s %s — already done", p['id'], p['title'][:40])
            continue

        run_id = client.create_task(p['prompt'])
        if run_id:
            tasks[p['slug']] = run_id
            log.info("🚀 %s %s → %s", p['id'], p['title'][:40], run_id)
        else:
            failed.append(p)
            log.warning("❌ %s %s — failed to create", p['id'], p['title'][:40])
        time.sleep(1)  # small delay between API calls

    # Retry failed tasks with exponential backoff
    for attempt in range(1, max_retries + 1):
        if not failed:
            break
        log.info("🔄 Retry attempt %d/%d for %d failed tasks...", attempt, max_retries, len(failed))
        time.sleep(5 * attempt)
        still_failed: list[dict] = []
        for p in failed:
            run_id = client.create_task(p['prompt'])
            if run_id:
                tasks[p['slug']] = run_id
                log.info("🚀 Retry OK: %s %s → %s", p['id'], p['title'][:40], run_id)
            else:
                still_failed.append(p)
        failed = still_failed

    if failed:
        log.warning("⚠️  %d tasks failed after %d retries", len(failed), max_retries)

    return tasks


def poll_parallel(tasks: dict[str, str], prompts: list[dict]) -> None:
    """Poll all running Parallel AI tasks until complete."""
    keys = load_keys()
    client = ParallelClient(keys)
    pending = dict(tasks)
    start = time.time()
    metrics = ResearchMetrics()

    while pending and time.time() - start < 7200:
        time.sleep(30)
        elapsed = int(time.time() - start)

        for slug, run_id in list(pending.items()):
            status_code, data = client._request("GET", f"/tasks/runs/{run_id}")

            # Handle network errors gracefully
            if status_code == 0:
                log.warning("Network error polling %s, will retry", slug)
                continue

            if status_code != 200:
                continue

            status = data.get("status", "unknown")
            if status == "completed":
                r_code, r_data = client._request("GET", f"/tasks/runs/{run_id}/result")
                if r_code == 200:
                    content = r_data.get("output", {}).get("content", "")
                    out_file = RAW_DIR / f"{slug}_parallel.md"
                    out_file.write_text(content)
                    metrics.record_query(True, len(content), COST_PER_QUERY, elapsed, slug)
                    log.info("✅ [%dm] %s: %s chars", elapsed // 60, slug, f"{len(content):,}")
                del pending[slug]
            elif status == "failed":
                metrics.record_query(False, topic=slug)
                log.error("❌ [%dm] %s: FAILED", elapsed // 60, slug)
                del pending[slug]

        if pending:
            log.info("⏳ [%dm] %d still running...", elapsed // 60, len(pending))

    if pending:
        log.warning("⚠️ %d tasks timed out: %s", len(pending), list(pending.keys()))

    print(metrics.summary())


def prepare_gemini_tasks(prompts: list[dict]) -> int:
    """Write prompt files for Gemini batch mode."""
    TASKS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for p in prompts:
        out_file = RAW_DIR / f"{p['slug']}_gemini.md"
        if out_file.exists():
            log.info("⏭️  %s %s — already done", p['id'], p['title'][:40])
            continue
        task_file = TASKS_DIR / f"{p['slug']}.txt"
        task_file.write_text(p['prompt'])
        count += 1
    log.info("📝 %d task files written to %s", count, TASKS_DIR)
    return count


def run_gemini_batch() -> bool:
    """Run Gemini batch using gemini_runner.py --tasks-dir."""
    import subprocess
    cmd = [
        sys.executable,
        str(Path(__file__).parent.parent / "engines" / "gemini_runner.py"),
        "--tasks-dir", str(TASKS_DIR),
        "--output-dir", str(RAW_DIR),
    ]
    log.info("🌐 Running: %s", " ".join(cmd[-4:]))
    proc = subprocess.run(cmd, cwd=str(Path(__file__).parent.parent))
    return proc.returncode == 0


def show_status(prompts: list[dict]) -> None:
    """Show current status of all prompts with colored indicators."""
    # Table header
    header = f"{'ID':<6} {'Topic':<45} {'PAI':>5} {'GEM':>5} {'PPX':>5}"
    sep = "═" * len(header)
    print(f"\n{sep}")
    print(header)
    print(sep)

    done_count = 0
    total_possible = len(prompts) * 3  # 3 engines per prompt

    for p in prompts:
        pai = "✅" if (RAW_DIR / f"{p['slug']}_parallel.md").exists() else "⬜"
        gem = "✅" if (RAW_DIR / f"{p['slug']}_gemini.md").exists() else "⬜"
        ppx = "✅" if (RAW_DIR / f"{p['slug']}_perplexity.md").exists() else "⬜"

        done_count += sum(1 for x in [pai, gem, ppx] if x == "✅")
        print(f"{p['id']:<6} {p['title'][:44]:<45} {pai:>5} {gem:>5} {ppx:>5}")

    print(sep)
    pct = (done_count / total_possible * 100) if total_possible > 0 else 0
    print(f"Progress: {done_count}/{total_possible} ({pct:.0f}%)")
    print(sep)


def main() -> None:
    parser = argparse.ArgumentParser(description="Research Orchestrator")
    parser.add_argument("--all", action="store_true", help="Run all prompts")
    parser.add_argument("--topic", "-t", help="Run single topic by slug or prompt ID")
    parser.add_argument("--engine", "-e", choices=["parallel", "gemini", "both"],
                        default="both", help="Which engine(s)")
    parser.add_argument("--list", action="store_true", help="List prompts and status")
    parser.add_argument("--poll", help="Poll Parallel AI tasks from saved state")
    args = parser.parse_args()

    prompts = parse_prompts()
    log.info("📋 Loaded %d prompts from %s", len(prompts), PROMPTS_FILE.name)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if args.list:
        show_status(prompts)
        return

    if args.topic:
        prompts = [p for p in prompts if args.topic in p['slug'] or args.topic == p['id']]
        if not prompts:
            log.error("Topic '%s' not found", args.topic)
            return

    if not args.all and not args.topic:
        show_status(prompts)
        print("\nUse --all to run, or --topic ID to run one.")
        return

    # === Parallel AI ===
    if args.engine in ("parallel", "both"):
        print(f"\n{'━'*50}")
        print("▶ Parallel AI (ultra8x) — firing all tasks")
        print(f"{'━'*50}")
        tasks = run_parallel_all(prompts)

        if tasks:
            # Save task IDs for recovery
            state_file = OUTPUT_DIR / ".parallel_tasks.json"
            existing: dict = {}
            if state_file.exists():
                existing = json.loads(state_file.read_text())
            existing.update(tasks)
            state_file.write_text(json.dumps(existing, indent=2))
            log.info("📊 %d tasks launched, polling...", len(tasks))
            poll_parallel(tasks, prompts)

    # === Gemini ===
    if args.engine in ("gemini", "both"):
        print(f"\n{'━'*50}")
        print("▶ Gemini Deep Research (Chrome + CDP)")
        print(f"{'━'*50}")
        n = prepare_gemini_tasks(prompts)
        if n > 0:
            run_gemini_batch()
        else:
            log.info("All Gemini tasks already completed!")

    # === Status ===
    show_status(prompts)
    log.info("✅ Orchestration complete!")


if __name__ == "__main__":
    main()
