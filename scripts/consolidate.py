#!/usr/bin/env python3
"""
Consolidation script: merge 3 raw research files into opus_common using Copilot CLI.
Usage:
    python3 consolidate.py --topic section-230 --category legal
    python3 consolidate.py --all
    python3 consolidate.py --all --dry-run
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))
from engines.base import setup_logger

log = setup_logger("consolidate")

MODULE_ROOT = Path(__file__).parent.parent
RAW_DIR = MODULE_ROOT / "output" / "raw"
OUTPUT_DIR = MODULE_ROOT / "output" / "consolidated"

# Mapping: prompt_id → (topic_slug, category, output_name)
TOPICS: dict[str, tuple[str, str, str]] = {
    "1-1": ("section-230", "legal", "section-230"),
    "1-2": ("csam-laws", "legal", "csam-protect-act"),
    "1-3": ("take-it-down-act", "legal", "take-it-down-act"),
    "2-1": ("california-laws", "legal", "california-laws"),
    "2-2": ("texas-laws", "legal", "texas-laws"),
    "2-3": ("state-by-state", "legal", "state-by-state"),
    "3-1": ("eu-ai-act", "legal", "eu-ai-act"),
    "3-2": ("gdpr-biometric", "legal", "gdpr-biometric"),
    "4-1": ("gpu-pricing", "financial", "gpu-pricing"),
    "4-2": ("cac-benchmarks", "financial", "cac-benchmarks"),
    "4-3": ("payment-processors", "financial", "payment-processors"),
    "5-1": ("image-models", "tech", "image-models"),
    "5-2": ("video-models", "tech", "video-models"),
    "5-3": ("voice-models", "tech", "voice-models"),
    "6-1": ("companion-risks", "ethics", "companion-risks"),
    "6-2": ("competitors", "market", "competitors"),
}

VALID_CATEGORIES = {"legal", "financial", "tech", "ethics", "market"}
MAX_SOURCE_CHARS = 40000

def find_raw_files(prefix: str) -> dict[str, Path]:
    """Find gemini, perplexity, parallel files for a prompt prefix."""
    files: dict[str, Path] = {}
    if not RAW_DIR.exists():
        return files
    for f in RAW_DIR.glob(f"{prefix}_*"):
        name = f.name
        if "_gemini.md" in name:
            files["gemini"] = f
        elif "_perplexity.md" in name:
            files["perplexity"] = f
        elif "_parallel.md" in name:
            files["parallel"] = f
    return files


def consolidate_topic(prefix: str, topic: str, category: str,
                      output_name: str) -> bool:
    """Consolidate 3 sources into one opus_common file."""
    files = find_raw_files(prefix)

    if len(files) < 2:
        log.warning("Only %d sources for %s, skipping", len(files), prefix)
        return False

    out_dir = OUTPUT_DIR / category
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{output_name}_opus_common.md"

    if out_file.exists() and out_file.stat().st_size > 1000:
        log.info("Already exists: %s (%s chars)", out_file.name, f"{out_file.stat().st_size:,}")
        return True

    # Read sources (truncate very large files to fit context)
    sources: dict[str, str] = {}
    for engine, path in files.items():
        try:
            content = path.read_text()
        except OSError as e:
            log.error("Failed to read %s: %s", path, e)
            continue
        if len(content) > MAX_SOURCE_CHARS:
            content = content[:MAX_SOURCE_CHARS] + f"\n\n[TRUNCATED from {len(content):,} chars]"
        sources[engine] = content
    
    prompt = f"""You are a research analyst consolidating tri-source deep research for a C2C Creator Copilot AI Adult Platform.

TOPIC: {topic}
CATEGORY: {category}

C2C MODEL CONTEXT: Platform provides AI tools to adult content creators. Creators upload their own photos (18+, with consent) for LoRA training. Platform generates NSFW content variations. Creators sell to subscribers (watermark preview → paid clean download). Additional: 18+ AI companion chatbot.

SOURCE 1 — Gemini Deep Research:
{sources.get('gemini', 'NOT AVAILABLE')}

SOURCE 2 — Perplexity Deep Research:
{sources.get('perplexity', 'NOT AVAILABLE')}

SOURCE 3 — Parallel AI:
{sources.get('parallel', 'NOT AVAILABLE')}

Create a consolidated analysis following this structure:

# {topic.replace('-', ' ').title()} — Consolidated Analysis

## Executive Summary
(2-3 paragraphs, key findings)

## Detailed Findings
(Compare all sources, note agreements/contradictions)

## Implications for C2C Creator Copilot Model
(Specific to our platform)

## Confidence Assessment
- High Confidence (3/3 agree): ...
- Medium Confidence (2/3 agree): ...
- Low Confidence / Conflicting: ...
- REQUIRES VERIFICATION: ...

## Risk Assessment for C2C Model
- Key risks
- Mitigation strategies

## Sources
(All cited sources from all 3 engines)

Requirements:
1. Compare ALL 3 sources, identify where they agree and contradict
2. Flag REQUIRES VERIFICATION for claims where sources disagree on facts
3. Do NOT invent data. If all 3 lack info, write REQUIRES RESEARCH
4. Be specific about implications for the C2C adult AI platform model
5. Include confidence levels for each major finding"""

    # Write prompt to temp file
    prompt_file = Path(f"/tmp/consolidate_{prefix}.txt")
    prompt_file.write_text(prompt)
    
    log.info("Consolidating with Copilot Opus 4.6...")

    # Call copilot CLI
    try:
        result = subprocess.run(
            ["copilot", "--allow-all", "--model", "claude-opus-4.6",
             "-p", f"@{prompt_file}"],
            capture_output=True, text=True, timeout=600,
            cwd=str(MODULE_ROOT)
        )
        if result.returncode == 0 and len(result.stdout) > 500:
            out_file.write_text(result.stdout)
            log.info("Saved: %s (%s chars)", out_file, f"{len(result.stdout):,}")
            return True
        else:
            log.error("Copilot failed (rc=%d): %s", result.returncode, result.stderr[:200])
            return False
    except subprocess.TimeoutExpired:
        log.error("Copilot timeout (600s) for topic: %s", topic)
        return False
    except FileNotFoundError:
        log.error("Copilot CLI not found — save prompt for manual consolidation")
        out_file.write_text(f"# {topic} — CONSOLIDATION PENDING\n\nPrompt saved at: {prompt_file}\n")
        return False
    except OSError as e:
        log.error("OS error running copilot: %s", e)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Consolidate tri-source research")
    parser.add_argument("--topic", help="Topic prefix (e.g., 1-1)")
    parser.add_argument("--all", action="store_true", help="Consolidate all topics")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    args = parser.parse_args()

    if args.topic:
        if args.topic not in TOPICS:
            log.error("Unknown topic: %s", args.topic)
            log.info("Available: %s", ", ".join(TOPICS.keys()))
            return
        topic, category, output_name = TOPICS[args.topic]
        consolidate_topic(args.topic, topic, category, output_name)
    elif args.all:
        success = 0
        fail = 0
        for prefix, (topic, category, output_name) in sorted(TOPICS.items()):
            log.info("═" * 50)
            log.info("[%s] %s → %s/%s_opus_common.md", prefix, topic, category, output_name)

            if args.dry_run:
                files = find_raw_files(prefix)
                log.info("  Sources: %s (%d/3)", ", ".join(files.keys()), len(files))
                continue

            if consolidate_topic(prefix, topic, category, output_name):
                success += 1
            else:
                fail += 1

        log.info("═" * 50)
        log.info("DONE: %d success, %d failed", success, fail)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
