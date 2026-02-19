#!/usr/bin/env python3
"""Tests for research automation module."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))


class TestBaseEngine(unittest.TestCase):
    """Tests for base engine ABC and metrics."""

    def test_metrics_record_success(self):
        from engines.base import ResearchMetrics
        m = ResearchMetrics()
        m.record_query(True, chars=5000, cost_usd=2.40, time_seconds=120, topic="test")
        self.assertEqual(m.queries_total, 1)
        self.assertEqual(m.queries_success, 1)
        self.assertEqual(m.success_rate, 1.0)
        self.assertEqual(m.total_cost_usd, 2.40)
        self.assertEqual(m.total_chars_produced, 5000)

    def test_metrics_record_failure(self):
        from engines.base import ResearchMetrics
        m = ResearchMetrics()
        m.record_query(False, topic="fail-test")
        self.assertEqual(m.queries_failed, 1)
        self.assertEqual(m.success_rate, 0.0)

    def test_metrics_mixed(self):
        from engines.base import ResearchMetrics
        m = ResearchMetrics()
        m.record_query(True, chars=1000, cost_usd=2.40, time_seconds=60)
        m.record_query(True, chars=2000, cost_usd=2.40, time_seconds=90)
        m.record_query(False, cost_usd=2.40, time_seconds=10)
        self.assertEqual(m.queries_total, 3)
        self.assertAlmostEqual(m.success_rate, 2 / 3)
        self.assertAlmostEqual(m.avg_cost, 2.40)
        self.assertEqual(m.total_chars_produced, 3000)

    def test_metrics_summary_output(self):
        from engines.base import ResearchMetrics
        m = ResearchMetrics()
        m.record_query(True, chars=5000, cost_usd=2.40, time_seconds=120)
        summary = m.summary()
        self.assertIn("Total queries", summary)
        self.assertIn("$2.40", summary)
        self.assertIn("100%", summary)

    def test_metrics_empty(self):
        from engines.base import ResearchMetrics
        m = ResearchMetrics()
        self.assertEqual(m.success_rate, 0.0)
        self.assertEqual(m.avg_cost, 0.0)

    def test_base_engine_cannot_instantiate(self):
        from engines.base import BaseEngine
        with self.assertRaises(TypeError):
            BaseEngine()

    def test_setup_logger(self):
        from engines.base import setup_logger
        log = setup_logger("test-engine")
        self.assertEqual(log.name, "test-engine")
        self.assertTrue(len(log.handlers) > 0)


class TestParallelClient(unittest.TestCase):
    """Tests for parallel_client.py."""

    def test_load_keys_from_env_var(self):
        """Keys loaded from environment variable."""
        from engines.parallel_client import load_keys
        with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
            f.write("PARALLEL_KEY_1=test-key-abc123\n")
            f.write("PARALLEL_KEY_2=test-key-def456\n")
            f.flush()
            keys = load_keys(f.name)
        os.unlink(f.name)
        self.assertEqual(len(keys), 2)
        self.assertEqual(keys[0], "test-key-abc123")
        self.assertEqual(keys[1], "test-key-def456")

    def test_load_keys_empty_file(self):
        """Empty env file should exit."""
        from engines.parallel_client import load_keys
        with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
            f.write("# no keys here\n")
            f.flush()
            # Remove env var if set
            env_key = os.environ.pop("PARALLEL_API_KEY", None)
            try:
                with self.assertRaises(SystemExit):
                    load_keys(f.name)
            finally:
                if env_key:
                    os.environ["PARALLEL_API_KEY"] = env_key
        os.unlink(f.name)

    def test_client_key_rotation(self):
        """Client rotates to next key on failure."""
        from engines.parallel_client import ParallelClient
        client = ParallelClient(["key1", "key2", "key3"])
        self.assertEqual(client.current_key, "key1")
        result = client._rotate_key("test failure")
        self.assertTrue(result)
        self.assertEqual(client.current_key, "key2")

    def test_client_all_keys_exhausted(self):
        """Returns False when all keys exhausted."""
        from engines.parallel_client import ParallelClient
        client = ParallelClient(["key1"])
        result = client._rotate_key("test failure")
        self.assertFalse(result)

    def test_client_is_base_engine(self):
        """ParallelClient implements BaseEngine."""
        from engines.parallel_client import ParallelClient
        from engines.base import BaseEngine
        client = ParallelClient(["key1"])
        self.assertIsInstance(client, BaseEngine)
        self.assertEqual(client.engine_name, "parallel")

    def test_client_network_error_returns_zero(self):
        """Network errors return status 0."""
        from engines.parallel_client import ParallelClient
        client = ParallelClient(["key1"])
        # Mock _request to simulate network error
        original = client._request
        client._request = lambda m, p, b=None: (0, {"error": "Network error"})
        run_id = client.create_task("test prompt")
        # Should retry once then fail (since both return 0)
        self.assertIsNone(run_id)

    def test_client_metrics_tracking(self):
        """Metrics are tracked via run_tracked."""
        from engines.parallel_client import ParallelClient
        client = ParallelClient(["key1"])
        # Mock the research to return quickly
        client.run_research = lambda p, o=None: "# Test Result"
        result = client.run_tracked("test", topic="test-topic", cost_usd=2.40)
        self.assertEqual(result, "# Test Result")
        self.assertEqual(client.metrics.queries_success, 1)
        self.assertAlmostEqual(client.metrics.total_cost_usd, 2.40)


class TestRunResearch(unittest.TestCase):
    """Tests for run_research.py prompt parsing."""

    def test_parse_prompts_file(self):
        """Prompts parsed correctly from markdown file."""
        from scripts.run_research import parse_prompts
        prompts_file = Path(__file__).parent.parent.parent / "docs" / "research-prompts.md"
        if not prompts_file.exists():
            self.skipTest("research-prompts.md not found")
        prompts = parse_prompts(prompts_file)
        self.assertGreater(len(prompts), 0)
        for p in prompts:
            self.assertIn('id', p)
            self.assertIn('slug', p)
            self.assertIn('title', p)
            self.assertIn('prompt', p)
            self.assertGreater(len(p['prompt']), 50)

    def test_parse_prompts_nonexistent_file(self):
        """Nonexistent prompts file raises error."""
        from scripts.run_research import parse_prompts
        with self.assertRaises((FileNotFoundError, OSError)):
            parse_prompts(Path("/nonexistent/file.md"))


class TestConsolidate(unittest.TestCase):
    """Tests for consolidate.py topic mapping."""

    def test_topics_mapping_completeness(self):
        """All 16 topics are mapped."""
        from scripts.consolidate import TOPICS
        self.assertEqual(len(TOPICS), 16)

    def test_topics_categories(self):
        """Categories cover all expected domains."""
        from scripts.consolidate import TOPICS, VALID_CATEGORIES
        categories = set(cat for _, cat, _ in TOPICS.values())
        self.assertEqual(categories, VALID_CATEGORIES)

    def test_topics_output_names_unique(self):
        """All output names are unique."""
        from scripts.consolidate import TOPICS
        names = [name for _, _, name in TOPICS.values()]
        self.assertEqual(len(names), len(set(names)))

    def test_find_raw_files_empty_dir(self):
        """Returns empty dict for nonexistent prefix."""
        from scripts.consolidate import find_raw_files
        files = find_raw_files("nonexistent-prefix-xyz")
        self.assertEqual(len(files), 0)

    def test_find_raw_files_nonexistent_dir(self):
        """Returns empty dict when RAW_DIR doesn't exist."""
        from scripts.consolidate import find_raw_files
        import scripts.consolidate as mod
        original = mod.RAW_DIR
        mod.RAW_DIR = Path("/nonexistent/dir")
        try:
            files = find_raw_files("anything")
            self.assertEqual(len(files), 0)
        finally:
            mod.RAW_DIR = original


class TestGeminiRunner(unittest.TestCase):
    """Tests for gemini_runner.py helpers (no browser required)."""

    def test_find_chrome_returns_path_or_none(self):
        """Chrome finder returns valid path or None."""
        sys.path.insert(0, str(Path(__file__).parent.parent / "engines"))
        from gemini_runner import _find_chrome
        result = _find_chrome()
        if result is not None:
            self.assertTrue(os.path.exists(result))

    def test_free_port_returns_int(self):
        """Free port helper returns a valid port number."""
        from gemini_runner import _free_port
        port = _free_port()
        self.assertIsInstance(port, int)
        self.assertGreater(port, 0)
        self.assertLess(port, 65536)


class TestPerplexityRunner(unittest.TestCase):
    """Tests for perplexity_runner.py helpers (no browser required)."""

    def test_find_chrome_returns_path_or_none(self):
        """Chrome finder returns valid path or None."""
        sys.path.insert(0, str(Path(__file__).parent.parent / "engines"))
        from perplexity_runner import _find_chrome
        result = _find_chrome()
        if result is not None:
            self.assertTrue(os.path.exists(result))

    def test_free_port_returns_int(self):
        from perplexity_runner import _free_port
        port = _free_port()
        self.assertIsInstance(port, int)
        self.assertGreater(port, 0)

    def test_load_creds_explicit(self):
        """Explicit creds override env file."""
        from perplexity_runner import _load_creds
        email, pw = _load_creds("test@example.com", "pass123")
        self.assertEqual(email, "test@example.com")
        self.assertEqual(pw, "pass123")

    def test_profile_dir_creates_directory(self):
        """Profile dir is created for email."""
        from perplexity_runner import _profile_dir
        with tempfile.TemporaryDirectory() as tmp:
            import perplexity_runner as mod
            original = mod.PROFILES_DIR
            mod.PROFILES_DIR = Path(tmp)
            try:
                d = _profile_dir("user@example.com")
                self.assertTrue(d.exists())
                self.assertIn("user", str(d))
            finally:
                mod.PROFILES_DIR = original


class TestIntegration(unittest.TestCase):
    """Integration tests for end-to-end pipeline."""

    def test_parallel_client_create_task_mock(self):
        """Full pipeline with mocked API calls."""
        from engines.parallel_client import ParallelClient

        client = ParallelClient(["test-key-123"])

        # Mock _request to simulate API behavior
        call_count = [0]

        def mock_request(method, path, body=None):
            call_count[0] += 1
            if method == "POST" and "/tasks/runs" in path:
                return 201, {"run_id": "mock-run-123", "status": "processing"}
            if method == "GET" and "/tasks/runs/mock-run-123/result" in path:
                return 200, {
                    "output": {
                        "content": "# Mock Research\n\nTest content.",
                        "basis": [{"citations": [{"url": "https://example.com", "title": "Test"}]}]
                    }
                }
            if method == "GET" and "/tasks/runs/mock-run-123" in path:
                return 200, {"status": "completed"}
            return 404, {}

        client._request = mock_request
        result = client.run_research("Test prompt")
        self.assertIsNotNone(result)
        self.assertIn("Mock Research", result)
        self.assertIn("example.com", result)
        self.assertGreater(call_count[0], 0)

    def test_parallel_client_task_failure_mock(self):
        """Pipeline handles task failure gracefully."""
        from engines.parallel_client import ParallelClient
        client = ParallelClient(["test-key-123"])

        def mock_request(method, path, body=None):
            if method == "POST":
                return 201, {"run_id": "mock-fail-123", "status": "processing"}
            if method == "GET" and "mock-fail-123" in path:
                return 200, {"status": "failed", "errors": ["Test failure"]}
            return 404, {}

        client._request = mock_request
        result = client.run_research("Test prompt")
        self.assertIsNone(result)

    def test_orchestrator_show_status(self):
        """Orchestrator status display runs without error."""
        from scripts.run_research import parse_prompts
        prompts_file = Path(__file__).parent.parent.parent / "docs" / "research-prompts.md"
        if not prompts_file.exists():
            self.skipTest("research-prompts.md not found")
        prompts = parse_prompts(prompts_file)
        from scripts.run_research import show_status
        from io import StringIO
        import contextlib
        buf = StringIO()
        with contextlib.redirect_stdout(buf):
            show_status(prompts)
        output = buf.getvalue()
        self.assertIn("ID", output)
        self.assertIn("Progress:", output)

    def test_consolidation_prompt_generation(self):
        """Consolidation builds valid prompt from sources."""
        from scripts.consolidate import TOPICS, VALID_CATEGORIES

        for prefix, (topic, category, output_name) in TOPICS.items():
            self.assertIn(category, VALID_CATEGORIES, f"Invalid category for {prefix}")
            self.assertTrue(len(topic) > 0, f"Empty topic for {prefix}")
            self.assertTrue(len(output_name) > 0, f"Empty output_name for {prefix}")

    def test_research_deliverables_consistency(self):
        """Cross-check research deliverables for date/number consistency."""
        project_root = Path(__file__).parent.parent.parent
        research_dir = project_root / "research-c2c-copilot"

        if not research_dir.exists():
            self.skipTest("research-c2c-copilot not found")

        # Check TECHNICAL-PACKET has correct date
        tech_packet = (research_dir / "TECHNICAL-PACKET.md").read_text()
        self.assertNotIn("January 2026", tech_packet, "Date inconsistency in TECHNICAL-PACKET")
        self.assertNotIn("July 2026", tech_packet, "Date inconsistency in TECHNICAL-PACKET")

        # Check RISK-PACKET has correct stream count
        risk_packet = (research_dir / "RISK-PACKET.md").read_text()
        self.assertIn("48 independent research streams", risk_packet)
        self.assertNotIn("24 independent research streams", risk_packet)

        # Check all 4 packets exist
        for packet in ["LEGAL-PACKET.md", "FINANCIAL-PACKET.md", "TECHNICAL-PACKET.md", "RISK-PACKET.md"]:
            self.assertTrue((research_dir / packet).exists(), f"Missing {packet}")

        # Check DECISION-SUMMARY exists and has GO recommendation
        summary = (research_dir / "DECISION-SUMMARY.md").read_text()
        self.assertIn("CONDITIONAL GO", summary)

    def test_research_consolidated_files_exist(self):
        """All 16 consolidated files exist."""
        from scripts.consolidate import TOPICS, OUTPUT_DIR
        if not OUTPUT_DIR.exists():
            self.skipTest("research-c2c-copilot not found")
        for prefix, (topic, category, output_name) in TOPICS.items():
            path = OUTPUT_DIR / category / f"{output_name}_opus_common.md"
            self.assertTrue(path.exists(), f"Missing consolidated: {path}")


if __name__ == "__main__":
    unittest.main()
