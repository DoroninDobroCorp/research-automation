#!/usr/bin/env python3
"""
Consolidate custom research: merge raw files into one via Copilot CLI (Claude Opus).
Usage:
    python3 scripts/consolidate_custom.py --slug proxy-research
    python3 scripts/consolidate_custom.py --slug proxy-research --dry-run
"""
import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from engines.base import setup_logger

log = setup_logger("consolidate-custom")

MODULE_ROOT = Path(__file__).parent.parent
RAW_DIR = MODULE_ROOT / "output" / "raw"
OUTPUT_DIR = MODULE_ROOT / "output" / "consolidated"
MAX_SOURCE_CHARS = 40000


def find_sources(slug: str) -> dict[str, Path]:
    """Find all raw files for a given slug."""
    files = {}
    for engine in ["parallel", "gemini", "perplexity"]:
        f = RAW_DIR / f"{slug}_{engine}.md"
        if f.exists() and f.stat().st_size > 100:
            files[engine] = f
    return files


def consolidate(slug: str, dry_run: bool = False) -> bool:
    sources = find_sources(slug)
    if len(sources) < 1:
        log.error("No sources found for '%s'", slug)
        return False

    log.info("Found %d sources: %s", len(sources), ", ".join(sources.keys()))
    for engine, path in sources.items():
        log.info("  %s: %s (%s chars)", engine, path.name, f"{path.stat().st_size:,}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUTPUT_DIR / f"{slug}_consolidated.md"

    if out_file.exists() and out_file.stat().st_size > 1000:
        log.info("Already consolidated: %s (%s chars)", out_file, f"{out_file.stat().st_size:,}")
        return True

    # Read sources
    source_texts = {}
    for engine, path in sources.items():
        content = path.read_text()
        if len(content) > MAX_SOURCE_CHARS:
            content = content[:MAX_SOURCE_CHARS] + f"\n\n[TRUNCATED from {len(content):,} chars]"
        source_texts[engine] = content

    # Build consolidation prompt
    sources_block = ""
    for i, (engine, text) in enumerate(source_texts.items(), 1):
        sources_block += f"\n\nSOURCE {i} — {engine.upper()} Deep Research:\n{text}\n"

    prompt = f"""You are a research analyst consolidating multi-source deep research.

TOPIC: {slug.replace('-', ' ').replace('_', ' ').title()}

{sources_block}

Create a consolidated analysis following this structure:

# {slug.replace('-', ' ').replace('_', ' ').title()} — Consolidated Analysis

## Executive Summary
(2-3 paragraphs with key findings across all sources)

## Detailed Findings
(Compare all sources, note agreements and contradictions, organize by sub-topic)

## Confidence Assessment
- High Confidence (all sources agree): ...
- Medium Confidence (most agree): ...
- Low/Conflicting: ...
- REQUIRES VERIFICATION: ...

## Practical Recommendations
(Actionable takeaways, ranked by priority)

## Sources & References
(All cited sources from all engines)

Requirements:
1. Compare ALL sources, identify where they agree and contradict
2. Flag REQUIRES VERIFICATION for claims where sources disagree on facts
3. Do NOT invent data — if all sources lack info, write REQUIRES RESEARCH
4. Be specific with provider names, prices, URLs
5. Include confidence levels for each major finding
6. Prioritize actionable information

IMPORTANT: Save the consolidated analysis to the file: {out_file}
Use the create tool to write the full analysis to that exact path."""

    if dry_run:
        log.info("DRY RUN — prompt length: %d chars", len(prompt))
        log.info("Would save to: %s", out_file)
        return True

    # Write prompt to temp file
    prompt_file = Path(f"/tmp/consolidate_{slug}.txt")
    prompt_file.write_text(prompt)
    log.info("Prompt saved: %s (%s chars)", prompt_file, f"{len(prompt):,}")

    # Try copilot CLI — it creates files via its own tools, not stdout
    log.info("Running consolidation via Copilot CLI (Claude Opus 4.6)...")
    try:
        result = subprocess.run(
            ["copilot", "--allow-all", "--model", "claude-opus-4.6",
             "-p", f"@{prompt_file}"],
            capture_output=True, text=True, timeout=600,
            cwd=str(MODULE_ROOT)
        )
        # Copilot creates the file itself via tools — check output dir
        if out_file.exists() and out_file.stat().st_size > 500:
            log.info("✅ Saved: %s (%s chars)", out_file, f"{out_file.stat().st_size:,}")
            return True
        # Also check if it created with a slightly different name
        for f in OUTPUT_DIR.glob(f"{slug}*"):
            if f.stat().st_size > 500 and f != out_file:
                f.rename(out_file)
                log.info("✅ Saved (renamed): %s (%s chars)", out_file, f"{out_file.stat().st_size:,}")
                return True
        # Last resort: if copilot wrote to stdout instead
        if result.returncode == 0 and len(result.stdout) > 1000:
            # Filter out copilot tool-call logs (lines starting with ●)
            lines = [l for l in result.stdout.splitlines()
                     if not l.strip().startswith("●") and not l.strip().startswith("└")]
            content = "\n".join(lines).strip()
            if len(content) > 500:
                out_file.write_text(content)
                log.info("✅ Saved from stdout: %s (%s chars)", out_file, f"{len(content):,}")
                return True
        log.warning("Copilot returned rc=%d but no output found", result.returncode)
        if result.stderr:
            log.warning("stderr: %s", result.stderr[:300])
    except FileNotFoundError:
        log.warning("Copilot CLI not found")
    except subprocess.TimeoutExpired:
        log.warning("Copilot timeout (600s)")

    # Fallback: save prompt for manual use
    log.info("Saving prompt for manual consolidation...")
    out_file.write_text(
        f"# {slug} — CONSOLIDATION PENDING\n\n"
        f"Prompt saved at: {prompt_file}\n\n"
        f"Run manually:\n"
        f"  copilot --allow-all --model claude-opus-4.6 -p @{prompt_file}\n"
    )
    return False


def main():
    parser = argparse.ArgumentParser(description="Consolidate custom research")
    parser.add_argument("--slug", "-s", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    consolidate(args.slug, args.dry_run)


if __name__ == "__main__":
    main()
