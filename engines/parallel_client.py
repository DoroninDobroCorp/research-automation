#!/usr/bin/env python3
"""
Parallel AI Deep Research Client
Universal module for running deep research via Parallel AI Task API.

Usage:
    python3 parallel_client.py --prompt "Your research question" --output output/test.md
    python3 parallel_client.py --prompt-file prompts/section-230.txt --output output/section-230_aiparallel.md
    python3 parallel_client.py --test  # Quick test with a simple query

Processor: ultra8x (deepest research, 5min-2hr per query, ~$2.40/query)
Key rotation: cycles through keys when one returns 401/402/429
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Optional

import urllib.request
import urllib.error

from engines.base import BaseEngine, setup_logger

# ── Config ──────────────────────────────────────────────────────────

API_BASE = "https://api.parallel.ai/v1"
PROCESSOR = "ultra8x"  # Deepest research. NOT fast — user explicitly said no fast.
POLL_INTERVAL = 15     # seconds between status checks
MAX_WAIT = 7200        # 2 hours max wait (ultra8x can take up to 2h)
COST_PER_QUERY = 2.40  # USD estimate for ultra8x


def load_keys(env_file: Optional[str] = None) -> list[str]:
    """Load API keys from env file or environment."""
    keys: list[str] = []

    # Try env file first
    if env_file is None:
        env_file = str(Path(__file__).parent.parent / "config" / "keys.env")

    if Path(env_file).exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line.startswith("PARALLEL_KEY_") and "=" in line:
                    key = line.split("=", 1)[1].strip()
                    if key:
                        keys.append(key)

    # Also check environment variable
    env_key = os.environ.get("PARALLEL_API_KEY")
    if env_key and env_key not in keys:
        keys.insert(0, env_key)

    if not keys:
        print("❌ No API keys found. Set PARALLEL_API_KEY or add to config/keys.env")
        sys.exit(1)

    return keys


class ParallelClient(BaseEngine):
    """Parallel AI Task API client with key rotation and metrics tracking."""

    def __init__(self, keys: list[str], processor: str = PROCESSOR) -> None:
        super().__init__()
        self.keys = keys
        self.current_key_idx: int = 0
        self.processor = processor
        self.exhausted_keys: set[int] = set()

    @property
    def engine_name(self) -> str:
        return "parallel"

    @property
    def current_key(self) -> str:
        return self.keys[self.current_key_idx]

    def _rotate_key(self, reason: str) -> bool:
        """Try next key. Returns False if all keys exhausted."""
        self.exhausted_keys.add(self.current_key_idx)
        self.log.warning("Key #%d issue: %s", self.current_key_idx + 1, reason)

        for i in range(len(self.keys)):
            if i not in self.exhausted_keys:
                self.current_key_idx = i
                self.log.info("Switching to key #%d", i + 1)
                return True

        self.log.error("All API keys exhausted! Get a new key at https://platform.parallel.ai")
        return False

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> tuple[int, dict]:
        """Make API request with current key. Handles network errors gracefully."""
        url = f"{API_BASE}{path}"
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.current_key,
        }

        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body_text = e.read().decode() if e.fp else ""
            try:
                err_json = json.loads(body_text)
            except (json.JSONDecodeError, ValueError):
                err_json = {"error": body_text}
            return e.code, err_json
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            self.log.warning("Network error on %s %s: %s", method, path, e)
            return 0, {"error": f"Network error: {e}"}

    def create_task(self, prompt: str, output_mode: str = "text") -> Optional[str]:
        """Create a deep research task. Returns run_id or None."""
        body = {
            "input": prompt,
            "processor": self.processor,
            "task_spec": {
                "output_schema": {
                    "type": output_mode,
                    "description": (
                        "Comprehensive research report in markdown format. "
                        "Include all relevant data, statistics, legal precedents, "
                        "expert opinions. Cite every source with URL and date. "
                        "Be thorough — this is deep research for a knowledge base."
                    )
                }
            }
        }

        status, data = self._request("POST", "/tasks/runs", body)

        if status in (200, 201, 202):
            run_id = data.get("run_id")
            self.log.info("Task created: %s (processor: %s)", run_id, self.processor)
            return run_id

        # Network error — retry once
        if status == 0:
            self.log.warning("Network error, retrying in 5s...")
            time.sleep(5)
            status, data = self._request("POST", "/tasks/runs", body)
            if status in (200, 201, 202):
                return data.get("run_id")

        # Key issues — try rotation
        if status in (401, 402, 403, 429):
            reason = f"HTTP {status}: {data.get('error', data.get('message', 'unknown'))}"
            if self._rotate_key(reason):
                return self.create_task(prompt, output_mode)
            return None

        self.log.error("API error %d: %s", status, json.dumps(data, indent=2))
        return None

    def poll_result(self, run_id: str) -> Optional[dict]:
        """Poll until task completes. Returns result or None."""
        start = time.time()
        last_status: Optional[str] = None
        network_errors = 0

        while time.time() - start < MAX_WAIT:
            status, data = self._request("GET", f"/tasks/runs/{run_id}")

            # Handle transient network errors with backoff
            if status == 0:
                network_errors += 1
                if network_errors > 5:
                    self.log.error("Too many network errors (%d), giving up", network_errors)
                    return None
                backoff = min(30, POLL_INTERVAL * network_errors)
                self.log.warning("Network error #%d, retry in %ds", network_errors, backoff)
                time.sleep(backoff)
                continue
            network_errors = 0  # reset on success

            if status in (401, 402, 403, 429):
                reason = f"HTTP {status} on poll"
                if self._rotate_key(reason):
                    continue
                return None

            if status != 200:
                self.log.error("Poll error %d: %s", status, data)
                return None

            task_status = data.get("status", "unknown")
            elapsed = int(time.time() - start)

            if task_status != last_status:
                self.log.info("[%ds] Status: %s", elapsed, task_status)
                last_status = task_status

            if task_status == "completed":
                r_status, r_data = self._request("GET", f"/tasks/runs/{run_id}/result")
                if r_status == 200:
                    return r_data
                self.log.error("Result fetch error %d: %s", r_status, r_data)
                return None

            if task_status == "failed":
                errors = data.get("errors", [])
                self.log.error("Task failed: %s", errors)
                return None

            time.sleep(POLL_INTERVAL)

        self.log.error("Timeout after %ds", MAX_WAIT)
        return None

    def run_research(self, prompt: str, output_file: Optional[str] = None) -> Optional[str]:
        """Full pipeline: create task → poll → save result. Returns markdown or None."""
        self.log.info("=" * 60)
        self.log.info("Starting Parallel AI Deep Research")
        self.log.info("  Processor: %s | Key: #%d (***%s)",
                      self.processor, self.current_key_idx + 1, self.current_key[-6:])
        self.log.info("  Prompt: %s...", prompt[:100])

        run_id = self.create_task(prompt)
        if not run_id:
            return None

        self.log.info("Polling for result (ultra8x can take 5min-2hr)...")
        result = self.poll_result(run_id)
        if not result:
            return None

        # Extract markdown content
        output = result.get("output", {})
        content = output.get("content", "")
        basis = output.get("basis", [])

        if isinstance(content, dict):
            markdown = f"# Deep Research Result\n\n```json\n{json.dumps(content, indent=2, ensure_ascii=False)}\n```\n"
        elif isinstance(content, str):
            markdown = content
        else:
            markdown = str(content)

        # Append citations if present
        if basis:
            markdown += "\n\n---\n## Sources & Citations\n\n"
            for b in basis[:50]:
                citations = b.get("citations", [])
                for c in citations:
                    url = c.get("url", "")
                    title = c.get("title", "")
                    markdown += f"- [{title}]({url})\n"

        # Save if output file specified
        if output_file:
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, "w") as f:
                f.write(markdown)
            self.log.info("Saved to: %s (%s chars)", output_file, f"{len(markdown):,}")

        self.log.info("Research complete!")
        return markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Parallel AI Deep Research Client")
    parser.add_argument("--prompt", "-p", help="Research prompt text")
    parser.add_argument("--prompt-file", "-f", help="File containing prompt")
    parser.add_argument("--output", "-o", help="Output markdown file path")
    parser.add_argument("--processor", default=PROCESSOR, help=f"Processor (default: {PROCESSOR})")
    parser.add_argument("--test", action="store_true", help="Run a quick test query")
    parser.add_argument("--keys", help="Path to keys.env file")
    args = parser.parse_args()

    keys = load_keys(args.keys)
    print(f"🔑 Loaded {len(keys)} API key(s)")

    client = ParallelClient(keys, processor=args.processor)

    if args.test:
        prompt = (
            "Research Section 230 of the Communications Decency Act application to "
            "AI-generated adult content platforms in 2024-2026. "
            "Focus on: Does Section 230 protect platforms hosting AI-generated content? "
            "Recent court cases involving AI content and Section 230. "
            "Provide specific court cases, legal analyses, and expert opinions. "
            "Include dates and sources for all information."
        )
        output = Path(__file__).parent / "output" / "test_section230_aiparallel.md"
        result = client.run_tracked(prompt, str(output), topic="section-230-test",
                                    cost_usd=COST_PER_QUERY)
        print(client.metrics.summary())
        return

    if args.prompt_file:
        with open(args.prompt_file) as f:
            prompt = f.read().strip()
    elif args.prompt:
        prompt = args.prompt
    else:
        parser.error("Need --prompt, --prompt-file, or --test")

    output_file = args.output or str(Path(__file__).parent / "output" / "result.md")
    client.run_tracked(prompt, output_file, cost_usd=COST_PER_QUERY)
    print(client.metrics.summary())


if __name__ == "__main__":
    main()
