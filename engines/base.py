#!/usr/bin/env python3
"""
Base engine interface and shared utilities for research automation.

All engines (Parallel AI, Gemini, Perplexity) implement BaseEngine
to ensure consistent interface, logging, and metrics tracking.
"""

import logging
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ── Shared logging setup ────────────────────────────────────

LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
LOG_DATE_FORMAT = "%H:%M:%S"


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Create a named logger with consistent formatting."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT))
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


# ── Metrics tracking ────────────────────────────────────────

@dataclass
class ResearchMetrics:
    """Tracks cost, timing, and success rates for research runs."""
    queries_total: int = 0
    queries_success: int = 0
    queries_failed: int = 0
    total_chars_produced: int = 0
    total_cost_usd: float = 0.0
    total_time_seconds: float = 0.0
    per_query: list = field(default_factory=list)

    @property
    def success_rate(self) -> float:
        return self.queries_success / self.queries_total if self.queries_total > 0 else 0.0

    @property
    def avg_cost(self) -> float:
        return self.total_cost_usd / self.queries_total if self.queries_total > 0 else 0.0

    @property
    def avg_time(self) -> float:
        return self.total_time_seconds / self.queries_total if self.queries_total > 0 else 0.0

    def record_query(self, success: bool, chars: int = 0,
                     cost_usd: float = 0.0, time_seconds: float = 0.0,
                     topic: str = "") -> None:
        """Record a completed query."""
        self.queries_total += 1
        if success:
            self.queries_success += 1
            self.total_chars_produced += chars
        else:
            self.queries_failed += 1
        self.total_cost_usd += cost_usd
        self.total_time_seconds += time_seconds
        self.per_query.append({
            "topic": topic,
            "success": success,
            "chars": chars,
            "cost_usd": cost_usd,
            "time_s": round(time_seconds, 1),
        })

    def summary(self) -> str:
        """Human-readable metrics summary."""
        lines = [
            f"{'═' * 50}",
            f"📊 Research Metrics Summary",
            f"{'═' * 50}",
            f"  Total queries:    {self.queries_total}",
            f"  Successful:       {self.queries_success}",
            f"  Failed:           {self.queries_failed}",
            f"  Success rate:     {self.success_rate:.0%}",
            f"  Total output:     {self.total_chars_produced:,} chars",
            f"  Total cost:       ${self.total_cost_usd:.2f}",
            f"  Total time:       {self.total_time_seconds / 60:.1f} min",
            f"  Avg cost/query:   ${self.avg_cost:.2f}",
            f"  Avg time/query:   {self.avg_time / 60:.1f} min",
            f"{'═' * 50}",
        ]
        return "\n".join(lines)


# ── Base Engine ABC ─────────────────────────────────────────

class BaseEngine(ABC):
    """Abstract base class for all research engines.

    Subclasses must implement:
        - run_research(prompt, output_file) -> str | None
        - engine_name (property)

    Provides:
        - Consistent logging via self.log
        - Metrics tracking via self.metrics
        - Timing wrapper
    """

    def __init__(self) -> None:
        self.metrics = ResearchMetrics()
        self.log = setup_logger(self.engine_name)

    @property
    @abstractmethod
    def engine_name(self) -> str:
        """Short identifier for this engine (e.g., 'parallel', 'gemini')."""
        ...

    @abstractmethod
    def run_research(self, prompt: str, output_file: Optional[str] = None) -> Optional[str]:
        """Execute a research query. Returns markdown content or None on failure."""
        ...

    def run_tracked(self, prompt: str, output_file: Optional[str] = None,
                    topic: str = "", cost_usd: float = 0.0) -> Optional[str]:
        """Run research with automatic metrics tracking."""
        start = time.time()
        try:
            result = self.run_research(prompt, output_file)
            elapsed = time.time() - start
            self.metrics.record_query(
                success=result is not None,
                chars=len(result) if result else 0,
                cost_usd=cost_usd,
                time_seconds=elapsed,
                topic=topic,
            )
            return result
        except Exception as e:
            elapsed = time.time() - start
            self.log.error(f"Research failed: {e}")
            self.metrics.record_query(
                success=False, cost_usd=cost_usd,
                time_seconds=elapsed, topic=topic,
            )
            return None
