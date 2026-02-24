🇬🇧 [English](#-english) | 🇷🇺 [Русский](#-русский)

---

# 🇬🇧 English

# 🔬 Research Automation

Automated deep research from three sources with consolidation via Claude Opus.

```
Prompt → [Parallel AI + Gemini + Perplexity] → 3 raw files → Claude Opus → final report
```

## Engines

| Engine | Method | Time | Cost |
|:-------|:-------|:-----|:-----|
| **Parallel AI** | REST API (ultra8x) | 5–30 min | ~$2.40/request |
| **Gemini Deep Research** | Chrome + Playwright | 3–10 min | free (rate-limited) |
| **Perplexity Deep Research** | Chrome + Playwright | 3–10 min | free (Pro) |

Consolidation: **Copilot CLI** (Claude Opus 4.6) — merges all sources into a single report.

## Quick Start

```bash
# 1. Dependencies
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium

# 2. API keys
cp config/keys.env.example config/keys.env
# Fill in config/keys.env — API keys and credentials

# 3. Run (all three sources + consolidation)
python3 scripts/run_custom.py \
  -f output/prompts/my-topic.txt \
  -s my-topic
```

## Usage

### Full Pipeline (recommended)

```bash
# All 3 engines in parallel → consolidation
python3 scripts/run_custom.py -f prompt.txt -s my-topic

# Specific engines only
python3 scripts/run_custom.py -f prompt.txt -s my-topic --engines parallel,gemini

# Skip engines that already have results
python3 scripts/run_custom.py -f prompt.txt -s my-topic --reuse-existing

# Consolidate even if some sources failed
python3 scripts/run_custom.py -f prompt.txt -s my-topic --allow-partial
```

### Individual Engines

```bash
# Parallel AI
python3 engines/parallel_client.py -p "Your query" -o output/result.md

# Gemini Deep Research
python3 engines/gemini_runner.py -p "Your query" -o output/result.md

# Perplexity Deep Research
python3 engines/perplexity_runner.py -p "Your query" -o output/result.md
```

### Standalone Consolidation

```bash
python3 scripts/consolidate_custom.py --slug my-topic
```

## Project Structure

```
research-automation/
├── engines/
│   ├── base.py               # BaseEngine ABC, metrics, logging
│   ├── parallel_client.py    # Parallel AI Task API (ultra8x)
│   ├── gemini_runner.py      # Gemini Deep Research (Playwright + CDP)
│   └── perplexity_runner.py  # Perplexity Deep Research (Playwright + CDP)
├── scripts/
│   ├── run_custom.py         # Full pipeline: engines → consolidation
│   ├── run_research.py       # Orchestrator for batch prompts
│   ├── consolidate.py        # Consolidation for batch prompts
│   └── consolidate_custom.py # Consolidation for custom queries
├── config/
│   ├── keys.env.example      # Template for keys
│   └── keys.env              # API keys and credentials (not in git)
├── output/
│   ├── prompts/              # Prompt files
│   ├── raw/                  # Raw results from each engine
│   └── consolidated/         # Final consolidated reports
├── tests/
│   └── test_automation.py    # Unit tests (pytest)
├── requirements.txt
└── README.md
```

## Configuration (`config/keys.env`)

```env
# Parallel AI (https://platform.parallel.ai)
PARALLEL_KEY_1=your-key-here
PARALLEL_KEY_2=
PARALLEL_KEY_3=

# Google account for Gemini
GEMINI_EMAIL=your@gmail.com
GEMINI_PASSWORD=your-password

# Perplexity account
PERPLEXITY_EMAIL=your@email.com
PERPLEXITY_PASSWORD=your-password
```

## How Browser-Based Engines Work

Gemini and Perplexity use a **real Chrome** instance via CDP (Chrome DevTools Protocol):

1. Chrome launches with a persistent profile → cookies are preserved between runs
2. Playwright connects via CDP → controls the page
3. Stealth scripts hide automation from bot detection
4. After completion, Chrome is closed (in pipeline mode) or left open (in manual mode)

**First run** — you may need to log in manually (2FA, CAPTCHA). Cookies will be saved for subsequent runs.

## Browser Engine Flags

| Flag | Description |
|:-----|:------------|
| `--no-wait` | Exit immediately after completion (no Ctrl+C needed) |
| `--close-browser` | Close Chrome after finishing |
| `--dump-ui` | Show all interactive elements (for debugging) |

## Tests

```bash
python3 -m pytest tests/ -v
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| `No API keys found` | Fill in `config/keys.env` |
| Gemini login fails | Run `python3 engines/gemini_runner.py --dump-ui` to diagnose |
| All keys exhausted | Get new keys at https://platform.parallel.ai |
| Chrome not found | Install Google Chrome |
| Rate limit | Wait and restart with `--reuse-existing` |

---

# 🇷🇺 Русский

# 🔬 Research Automation

Автоматический deep research из трёх источников с консолидацией через Claude Opus.

```
Промпт → [Parallel AI + Gemini + Perplexity] → 3 raw-файла → Claude Opus → итоговый отчёт
```

## Движки

| Движок | Метод | Время | Стоимость |
|:-------|:------|:------|:----------|
| **Parallel AI** | REST API (ultra8x) | 5–30 мин | ~$2.40/запрос |
| **Gemini Deep Research** | Chrome + Playwright | 3–10 мин | бесплатно (лимиты) |
| **Perplexity Deep Research** | Chrome + Playwright | 3–10 мин | бесплатно (Pro) |

Консолидация: **Copilot CLI** (Claude Opus 4.6) — объединяет все источники в один отчёт.

## Быстрый старт

```bash
# 1. Зависимости
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium

# 2. Ключи
cp config/keys.env.example config/keys.env
# Заполни config/keys.env — API ключи и креды

# 3. Запуск (все три источника + консолидация)
python3 scripts/run_custom.py \
  -f output/prompts/my-topic.txt \
  -s my-topic
```

## Использование

### Полный пайплайн (рекомендуемый способ)

```bash
# Все 3 движка параллельно → консолидация
python3 scripts/run_custom.py -f prompt.txt -s my-topic

# Только конкретные движки
python3 scripts/run_custom.py -f prompt.txt -s my-topic --engines parallel,gemini

# Не перезапускать уже готовые
python3 scripts/run_custom.py -f prompt.txt -s my-topic --reuse-existing

# Консолидировать даже если не все источники отработали
python3 scripts/run_custom.py -f prompt.txt -s my-topic --allow-partial
```

### Движки по отдельности

```bash
# Parallel AI
python3 engines/parallel_client.py -p "Ваш запрос" -o output/result.md

# Gemini Deep Research
python3 engines/gemini_runner.py -p "Ваш запрос" -o output/result.md

# Perplexity Deep Research
python3 engines/perplexity_runner.py -p "Ваш запрос" -o output/result.md
```

### Консолидация отдельно

```bash
python3 scripts/consolidate_custom.py --slug my-topic
```

## Структура проекта

```
research-automation/
├── engines/
│   ├── base.py               # BaseEngine ABC, метрики, логгирование
│   ├── parallel_client.py    # Parallel AI Task API (ultra8x)
│   ├── gemini_runner.py      # Gemini Deep Research (Playwright + CDP)
│   └── perplexity_runner.py  # Perplexity Deep Research (Playwright + CDP)
├── scripts/
│   ├── run_custom.py         # Полный пайплайн: движки → консолидация
│   ├── run_research.py       # Оркестратор для batch-промптов
│   ├── consolidate.py        # Консолидация для batch-промптов
│   └── consolidate_custom.py # Консолидация для кастомных запросов
├── config/
│   ├── keys.env.example      # Шаблон для ключей
│   └── keys.env              # API ключи и креды (не в git)
├── output/
│   ├── prompts/              # Файлы с промптами
│   ├── raw/                  # Сырые результаты от каждого движка
│   └── consolidated/         # Итоговые консолидированные отчёты
├── tests/
│   └── test_automation.py    # Unit-тесты (pytest)
├── requirements.txt
└── README.md
```

## Конфигурация (`config/keys.env`)

```env
# Parallel AI (https://platform.parallel.ai)
PARALLEL_KEY_1=your-key-here
PARALLEL_KEY_2=
PARALLEL_KEY_3=

# Google аккаунт для Gemini
GEMINI_EMAIL=your@gmail.com
GEMINI_PASSWORD=your-password

# Perplexity аккаунт
PERPLEXITY_EMAIL=your@email.com
PERPLEXITY_PASSWORD=your-password
```

## Как работают браузерные движки

Gemini и Perplexity используют **реальный Chrome** через CDP (Chrome DevTools Protocol):

1. Запускается Chrome с профилем → сохраняются куки между запусками
2. Playwright подключается через CDP → управляет страницей
3. Стелс-скрипты скрывают автоматизацию от ботодетекта
4. После завершения Chrome закрывается (в пайплайне) или остаётся открытым (при ручном запуске)

**Первый запуск** — может потребоваться ручной логин (2FA, капча). После этого куки сохранятся.

## Флаги браузерных движков

| Флаг | Описание |
|:-----|:---------|
| `--no-wait` | Выйти сразу после завершения (без Ctrl+C) |
| `--close-browser` | Закрыть Chrome после работы |
| `--dump-ui` | Показать все интерактивные элементы (для дебага) |

## Тесты

```bash
python3 -m pytest tests/ -v
```

## Troubleshooting

| Проблема | Решение |
|:---------|:--------|
| `No API keys found` | Заполни `config/keys.env` |
| Gemini login fails | Запусти `python3 engines/gemini_runner.py --dump-ui` для диагностики |
| All keys exhausted | Новые ключи на https://platform.parallel.ai |
| Chrome not found | Установи Google Chrome |
| Rate limit | Подожди и перезапусти с `--reuse-existing` |
