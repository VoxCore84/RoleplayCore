# LegalBench Harness — Setup and Usage Guide

**Closes Verification Master Checklist Cat 10 item:** "LegalBench harness setup guide."

**Source:** `tools/legalbench_harness.py` — full implementation. This guide is the user-facing how-to.

LegalBench is a 162-task benchmark for legal reasoning capability of LLMs (Stanford CodeX project, https://hazyresearch.stanford.edu/legalbench/). VoxCore's harness wraps the HuggingFace dataset loader and runs the chosen task subset against a chosen model (local Ollama or Claude API), with optional LLM-as-judge for free-text task scoring.

---

## Prerequisites

- Python 3.14+ with the project's pinned deps (`pip install -r tools/requirements.pinned.txt`)
- One of:
  - Local Ollama with at least one of `qwen3.5:27b-q4_K_M`, `gemma4:26b`, or `llama4:70b` pulled, OR
  - `ANTHROPIC_API_KEY` in `tools/ai_studio/.env` (for Claude test taker / judge)
- Internet access for HuggingFace dataset download (cached after first run)

---

## Common invocations

### List the 63 available LegalBench tasks
```
python tools/legalbench_harness.py --list-tasks
```

### Run the 5-task production benchmark with Claude Opus (the published-results setup)
```
python tools/legalbench_harness.py \
  --tasks contract_qa diversity_1 hearsay rule_qa citation_prediction_classification \
  --model opus \
  --max-examples 20 \
  --output AI_Studio/Reports/scheduled/legalbench_$(date +%Y%m%d_%H%M%S).json
```

This was the 2026-05-01 production run. Result: 80% / 90% / 70% / 10% / 5% per task, **51% overall**. The 10% on rule_qa was a string-match-scoring artifact (Opus answers were substantively correct but didn't match gold strings exactly).

### Re-run with `--judge` for free-text rescoring (the 2026-05-02 fix)
```
python tools/legalbench_harness.py \
  --tasks rule_qa citation_prediction_classification \
  --model opus \
  --max-examples 20 \
  --judge \
  --judge-model gemma4:26b \
  --output AI_Studio/Reports/scheduled/legalbench_judge_$(date +%Y%m%d_%H%M%S).json
```

This unmasks the string-match-suppressed scores. Result: rule_qa **10% → 100%**, citation_prediction_classification 5% → 10%, **overall 51% → 70%** across the 5-task suite.

**Caveat per the methodology rule (`docs/PUBLISHABLE_CLAIM_WORKFLOW.md`):** the Gemma judge is more lenient than Claude for free-text grading. For an externally-publishable number, re-run the same setup with a Claude judge added to the harness (currently a TODO — judge backend is Ollama-only).

### Run a single task quickly for smoke testing
```
python tools/legalbench_harness.py --tasks contract_qa --model opus --max-examples 5
```

### Run against local Ollama (free, slower, lower scores)
```
python tools/legalbench_harness.py --tasks contract_qa --model qwen3.5:27b-q4_K_M --max-examples 20
```

---

## Flag reference

| Flag | Default | Notes |
|---|---|---|
| `--tasks T1 T2 ...` | (required) | Space-separated task names from `--list-tasks` |
| `--list-tasks` | — | Print the 63 known tasks and exit |
| `--model NAME` | (required) | One of `opus` / `sonnet` / `haiku` (claude alias) OR a literal Ollama model id like `qwen3.5:27b-q4_K_M` |
| `--max-examples N` | 20 | Max examples per task. n=20 is the production default; n≥100 needed for externally-defensible per-task scores |
| `--output PATH` | stdout-only | JSON results file. Recommended: write to `AI_Studio/Reports/scheduled/` with timestamp |
| `--judge` | off | Enable LLM-as-judge for free-text tasks (`rule_qa`, `citation_prediction_*`). Binary tasks are unaffected — string-match still scores them correctly |
| `--judge-model NAME` | `gemma4:26b` | Ollama model id for the judge. Only Ollama supported as judge backend currently |

---

## What the output JSON contains

```jsonc
{
  "model": "opus",                      // resolved test-taker model id
  "judge_model": "gemma4:26b",          // null if --judge not set
  "elapsed_total_s": 587.2,
  "tasks": [
    {
      "name": "rule_qa",
      "examples_run": 20,
      "correct": 20,
      "score": 1.0,
      "scoring": "judge",               // or "string-match" for binary tasks
      "elapsed_s": 312.4,
      "examples": [
        {
          "predicted": "Diversity jurisdiction is codified in 28 U.S.C. § 1332...",
          "gold":      "28 USC § 1332",
          "correct":   true,
          "judge_reason": "Predicted answer cites the same statute as gold."
        }
        // ...
      ]
    }
    // ...
  ],
  "summary": {
    "overall_score": 0.70,
    "per_task": { "rule_qa": 1.0, "citation_prediction_classification": 0.10 },
    "binary_avg": 0.80,
    "free_text_avg": 0.55
  }
}
```

The `examples` array preserves every (predicted, gold, correct, judge_reason) tuple — useful for spot-checking judge calibration and surfacing scoring-artifact patterns.

---

## Methodology gates before publishing a LegalBench number externally

Per `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`, every LegalBench number quoted in an external document must satisfy:

1. **Sample size ≥100 per task.** n=20 is enough for in-house tracking, NOT external publication.
2. **Judge model named.** If `--judge` was used, the judge model id appears in the citation. Currently always Gemma — when Claude judge is added, that becomes the better claim.
3. **Score JSON path cited.** A reviewer can pull up the per-example detail.
4. **Apples-to-apples vs comparison numbers.** If quoting "VoxCore beats Stanford CodeX baseline by N points," the test-taker model and judge must match the baseline's setup.
5. **Confidence tier per `PUBLISHABLE_CLAIM_WORKFLOW.md`.** Today: PARTIALLY-SUPPORTED for the n=20 + Gemma-judge result. WELL-SUPPORTED requires the n≥100 + Claude judge expansion.

---

## Cost notes

Per the 2026-05-02 production run (n=20 per task, 5 tasks, Claude Opus 4.5 test-taker, Gemma 4 26B judge for 2 free-text tasks):

| Component | Cost | Notes |
|---|---|---|
| Claude Opus test-taking (100 examples × ~300 tokens out) | ~$1.50 | API only |
| Gemma judging (40 free-text examples × ~50 tokens) | $0 | Local Ollama |
| Total | **~$1.50** | for the full 5-task n=20 run |

Scaling to n=100/task: ~$7.50. Adding Claude judge for free-text: another ~$1. Total for an externally-publishable run: **~$10**.

---

## Known issues

1. **Judge backend is Ollama-only.** Adding a Claude judge requires extending `_judge_via_ollama` with a `_judge_via_claude` sibling and a `--judge-backend` flag. ~30 min of work.
2. **`--model opus` resolves to claude-opus-4-20250514 (Opus 4.5)**, not 4.7. Update `MODEL_ALIASES` at `legalbench_harness.py:42-44` when 4.7 becomes the production default.
3. **First run downloads the HuggingFace dataset (~200MB)** — slow on first invocation, fast on subsequent.
4. **Some task names have changed upstream.** If `--list-tasks` doesn't include a task you expect, check the upstream `nguha/legalbench` HF dataset for current task IDs.

---

## How this harness was used in the 2026-05-02 measurement work

| Date | Run | Notes |
|---|---|---|
| 2026-05-01 | 5 tasks × Opus (no judge) — published 51% | First production run; rule_qa string-match scoring suppressed the score |
| 2026-05-01 | Same suite × Sonnet (no judge) — 49% | Comparison run; Opus and Sonnet near-identical on binary tasks |
| 2026-05-01 | Same suite × Qwen 27B local — 6% | Floor measurement; local quantized model is not competitive on LegalBench |
| 2026-05-02 | rule_qa + citation_prediction × Opus 4.5 + `--judge gemma4:26b` — 100% / 10% | Re-run that lifted overall to 70%; the Gemma 100% needs validation |

Latest score JSON: `AI_Studio/Reports/scheduled/legalbench_judge_20260502_112127.json`.
