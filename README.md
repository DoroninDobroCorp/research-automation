# Research Automation Module

Автоматизация tri-source deep research для AI Adult Platform.

> **Status:** v1.0 — Production-ready for C2C Creator Copilot research
> **Date:** July 2025
> **Author:** Vladimir (PM)
> **BMAD Story:** RESEARCH-001-S2 (see `_bmad-output/implementation-artifacts/stories/research-001-epic.md`)

## Scope & Purpose

Automates the tri-source research methodology:
1. **Parallel AI** (API) — ultra8x deep research with key rotation
2. **Gemini Deep Research** (browser automation) — Chrome + Playwright + CDP
3. **Perplexity Deep Research** (browser automation) — Chrome + Playwright

**Input:** Research prompts (`docs/research-prompts.md`)
**Output:** Raw markdown research files → consolidated analyses → decision packets

### Acceptance Criteria
- ✅ Each engine produces markdown research file per prompt
- ✅ Key rotation handles API rate limits / expired keys automatically
- ✅ Orchestrator tracks completed vs pending research across all engines
- ✅ Consolidation script merges 3 sources into single analysis via Claude Opus
- ✅ All secrets (.env, Chrome profiles) excluded from git

## Prerequisites

```bash
# Python 3.10+
python3 --version

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers (for Gemini/Perplexity runners)
python -m playwright install chromium

# Configure API keys
cp config/keys.env.example config/keys.env
# Edit config/keys.env with your Parallel AI keys
```

## Quick Start

### 1. Parallel AI (API — полностью автоматически)

```bash
# Тест на одном промпте
python3 engines/parallel_client.py --test

# Свой промпт
python3 engines/parallel_client.py \
  --prompt "Research Section 230 application to AI adult content platforms" \
  --output output/section-230_aiparallel.md
```

### 2. Gemini Deep Research (браузерная автоматизация)

```bash
# Первоначальная настройка — залогиниться в Google
python3 engines/gemini_autoclicker.py --setup

# Тест на одном промпте
python3 engines/gemini_autoclicker.py --test

# Свой промпт
python3 engines/gemini_autoclicker.py \
  --prompt "Research CSAM laws and AI generation 2024-2026" \
  --output output/csam-protect-act_gemini.md
```

### 3. Orchestrator (все движки)

```bash
# Один топик через Parallel AI
python3 scripts/run_research.py \
  --topic section-230 \
  --prompt "Research Section 230..." \
  --engine parallel

# Один топик через Gemini
python3 scripts/run_research.py \
  --topic section-230 \
  --prompt "Research Section 230..." \
  --engine gemini
```

## Структура

```
research-automation/
├── README.md               ← Этот файл
├── requirements.txt        ← Python dependencies
├── config/
│   └── keys.env            ← API ключи (НЕ в git)
├── engines/
│   ├── __init__.py         ← Package exports (BaseEngine, ResearchMetrics)
│   ├── base.py             ← BaseEngine ABC + ResearchMetrics + logging setup
│   ├── parallel_client.py  ← Parallel AI Task API (ultra8x)
│   ├── gemini_runner.py    ← Gemini Deep Research (Playwright + CDP)
│   └── perplexity_runner.py ← Perplexity Deep Research (Playwright + CDP)
├── scripts/
│   ├── run_research.py     ← Orchestrator
│   └── consolidate.py      ← Tri-source → opus_common merge
├── tests/
│   └── test_automation.py  ← Unit tests (33 tests, pytest)
├── output/                 ← Результаты (НЕ в git)
└── .gitignore
```

## Architecture

All engines implement `BaseEngine` ABC from `engines/base.py`:

```python
from engines.base import BaseEngine

class MyEngine(BaseEngine):
    @property
    def engine_name(self) -> str:
        return "my-engine"

    def run_research(self, prompt, output_file=None):
        # ... implementation
```

**Built-in features:**
- `self.log` — named logger (replaces print statements)
- `self.metrics` — `ResearchMetrics` tracking cost, timing, success rates
- `run_tracked()` — wrapper that automatically records metrics per query
- Metrics summary printed at end of each run (total cost, success rate, avg time)

## Parallel AI

- **API**: Task API с Deep Research
- **Процессор**: `ultra8x` — самый глубокий ($2.40/запрос, 5мин-2ч)
- **Ключи**: 3 ключа с автоматической ротацией
- **Формат**: Markdown report с inline citations
- **Если ключ кончился**: Скрипт автоматически переключится на следующий.
  Если все 3 кончились — покажет ссылку на https://platform.parallel.ai

## Gemini Deep Research

- **Метод**: Playwright browser automation (Chrome)
- **Режим**: Deep Research + Pro model
- **Экспорт**: Share → Export to Google Docs → copy content
- **Первый запуск**: `--setup` для сохранения cookies
- **⚠️ Known limitation**: Requires one-time manual Google login via `--setup`. This is inherent to browser automation — Google blocks automated login to protect accounts. After initial setup, cookies are saved and subsequent runs are automatic.

## Правила

1. **Не запускать пачкой** — по одному, проверяем результат
2. **ultra8x, НЕ fast** — fast удорожает процесс
3. **Perplexity** — будет добавлен позже

## Testing

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run with coverage
python3 -m pytest tests/ --cov=engines --cov=scripts
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| `No API keys found` | Add keys to `config/keys.env` (format: `PARALLEL_KEY_1=xxx`) |
| `playwright not found` | Run `pip install playwright && python -m playwright install chromium` |
| Gemini login fails | Run `python3 engines/gemini_runner.py --setup` to save cookies |
| All keys exhausted | Get new keys at https://platform.parallel.ai |
| `research-prompts.md not found` | Ensure `docs/research-prompts.md` exists in project root |
| Chrome not found | Install Chrome or set custom path in engine config |
