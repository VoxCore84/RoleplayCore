# VoxCore Cost Optimization Status

**Date:** 2026-05-26
**Source reports:** `AI_Studio/Reports/system_inventory_2026-05-26/COST_BANKING_READINESS.md`,
`AI_Studio/Reports/pictures1_ingest/COST_BANKED.md`,
`AI_Studio/Reports/pictures1_ingest/COST_NOTES.md`,
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` §E
**Verdict:** $0 cleanly banked as of 2026-05-26. The only real cost lever (Batch API, ~50%) is blocked on entanglement reconciliation. Caching does not apply to current call patterns.

**Rule:** Do NOT edit production call sites this session. Do NOT enable Batch API without an explicit Adam GO and the entanglement gate cleared.

---

## 1. Current state of the cost tools

### `tools/model_router.py`
- **Status:** Committed (`0018077959`), importable, functional.
- `python tools/model_router.py --print` resolves all 16 operations from `config/backend_selection.yaml`.
- `--assume-local-down` previews cloud-fallback behavior.
- **Zero production importers.** No tool in `tools/`, `tools-dev/`, or any skill calls it.
- Self-test: `local_up=True, cloud_up=True` detected (as of 2026-05-25 verification).

### `tools/anthropic_helpers.py`
- **Status:** Committed, importable, self-test PASS.
- Provides: `cached_system()` (prompt-cache block builder), `estimate_cache_savings()` (cost math), `build_batch()` / `submit_batch(dry_run=True)` (Batch API, dry-run by default — saves JSON, no spend).
- **Zero production importers.** No tool calls it.
- `submit_batch(dry_run=True)` is safe to call at any time — it writes a local JSON file and makes no API request.

### `config/backend_selection.yaml`
- **Status:** 390-line routing decision matrix. UNTRACKED (not committed to git).
- The committed `model_router.py` depends on it. On a fresh checkout, model_router fails without this file.
- Not read by any production code (model_router has zero importers).
- **Action required:** Commit this file to repair the fresh-checkout break. Grep for personal paths before committing (per `operational-discipline.md` repo-exclusion criteria).

---

## 2. Why these tools aren't saving money yet

### Reason 1: Zero importers — tools are unconnected
`model_router` and `anthropic_helpers` are infrastructure modules with no callers. Until a call site adopts them, they have no effect on costs.

### Reason 2: Caching is $0-fit for current call patterns — verified, not assumed

The original analysis projected ~$21/run savings from caching the judge prompt. **This claim was withdrawn after reading the actual code** (per measurement-discipline withdrawn-claim discipline):

- `judge_span_claude` in `tools/citation_scorer.py` (~L305) uses raw `urllib` with a **single user message and no system block**.
- `JUDGE_PROMPT` is **169 tokens** — below the **~1024-token prompt-cache minimum**.
- `cache_control` headers on a 169-token prompt trigger nothing and save $0.
- VoxCore has **no current call site with a ≥1024-token repeated system prompt** — caching, while a generically-correct best practice, does not apply here today.
- The global `ENABLE_PROMPT_CACHING_1H=1` in `~/.claude/settings.json` already caches the Claude Code session itself; this is separate from these tools' own API clients.

### Reason 3: Routing defaults already match the YAML
`select_backend("judge_citation")` resolves to `ollama/gemma`; `select_backend("legal_pdf")` resolves to `opus`. The existing code already does this by default via hardcoded model strings. Adopting the router centralizes control but produces **$0 delta today**.

---

## 3. Exact adoption blockers

### Blocker A: Entangled files — reconcile first

Two files carry uncommitted work from prior sessions that must be committed or staged before any cost-tool edits touch the same files:

| File | Uncommitted lines | Prior-session work | Risk if overwritten |
|------|------------------|--------------------|---------------------|
| `tools/citation_scorer.py` | +93 / −2 | Phase 3.9 `judge`-package hook (`use_judge_package`, `judge_pkg_backend`, `judge_verdicts_v2`) | Loss of additive judge-package feature |
| `tools/quality_probe.py` | +23 | Phase 4 `hybrid_hyde_query()` HyDE fusion channel | Loss of HyDE channel code |

Adjacent entangled file (not a cost-tool target, but context):
- `tools/excluded_hybrid_search.py` +105 (Phase 4 HyDE refactor) — not a cost-tool adoption site, but part of the same unreconciled work block.

**Gate:** Reconcile (commit or discard) all three files before touching them for cost-tool adoption. Interactive staging (`git add -p`) is the recommended approach. This is an owner decision — do not overwrite prior-session work.

### Blocker B: urllib judge → Batch API is a refactor, not a flag

The citation judge (`judge_span_claude`) calls the Anthropic API via raw `urllib`, one call per claim-citation pair. Batch API requires:
1. Collect all judge requests as `[{"custom_id": id, "params": {model, max_tokens, system, messages}}, ...]`.
2. Submit via `anthropic_helpers.submit_batch(requests, dry_run=True)` — inspect JSON output.
3. Submit live: `submit_batch(requests, dry_run=False)`.
4. Poll for results (async; up to 24h turnaround).

This is a real refactor, not a one-line flag addition. The urllib call must be replaced with a batch collector. The synchronous path must remain as default for interactive use.

### Blocker C: Async eval workflow decision

Batch API is asynchronous (up to 24h turnaround). This is correct for offline gold-set sweeps but wrong for interactive `/ex ask` or real-time judging. A deliberate decision is required: Batch is an `--batch` mode for offline sweeps only; the synchronous path remains the default. This choice must be made explicitly before any batch wiring, not under pressure.

---

## 4. The entangled files and why reconcile-first

The cost-optimization target files (`citation_scorer.py`, `quality_probe.py`) are the same files that carry prior-session uncommitted work. Stacking a batch-API refactor on top of uncommitted changes would:
- Entangle two unrelated feature additions in one commit (bad history hygiene).
- Risk silently discarding or mismerging the Phase 3.9 judge-package hook or Phase 4 HyDE channel.
- Make rollback of either change impossible without untangling the merge.

The correct sequence is: (1) reconcile prior work into its own commit(s), then (2) build the batch tooling in a new file, then (3) wire the new file to the now-clean entangled files if needed.

---

## 5. Low-risk call sites

The following call sites are clean (no entanglement) and could adopt `model_router` or `anthropic_helpers` today without risk:

| Call site | What to adopt | Benefit |
|-----------|---------------|---------|
| A new `tools/batch_eval.py` (does not yet exist) | `anthropic_helpers.submit_batch(dry_run=True)` | Proves batch pipeline end-to-end; no spend until `dry_run=False` |
| `tools/ai_studio/review_cycle.py` | `model_router.select_backend("reviewer")` | Centralizes model selection for Triad reviewers; ~15 calls/session (low volume, low $ impact) |

Neither of the above touches the entangled files. `review_cycle.py` calls Claude via a `call_claude` bridge module, not direct `urllib`; no urllib refactor needed.

---

## 6. Required flags before any production adoption

These flags/guards must be present before enabling any cost-optimization feature in a production call site:

| Feature | Required guard |
|---------|---------------|
| Batch API | `--batch` flag (or config key); synchronous path remains default |
| Batch API live submit | `--submit` flag required; `dry_run=True` is default in `submit_batch()` |
| Prompt caching | `--cache` flag (or `ENABLE_PROMPT_CACHING` env var); default OFF until a call site is verified to have ≥1024-token system prefix |
| Model router | `from tools.model_router import select_backend` — opt-in per call site; no global monkey-patch |

---

## 7. Test checklist (for the future batch-adoption session)

Before declaring batch adoption complete, all of the following must produce evidence (per completion-integrity rules):

- [ ] Entanglement reconciled: `git status tools/citation_scorer.py tools/quality_probe.py` → clean (no `M` markers).
- [ ] `tools/batch_eval.py` created (new file, not the entangled files).
- [ ] Dry-run pass: `python tools/batch_eval.py --dry-run` → JSON batch plan written, no API call made.
- [ ] Batch plan inspected: review the JSON for correct `custom_id`, `model`, `messages` structure before submitting.
- [ ] Live submit (with GO): `python tools/batch_eval.py --submit` → batch job ID returned.
- [ ] Batch results polled: results file written with one row per `custom_id`.
- [ ] Before/after comparison: same gold set, same snapshot, synchronous baseline vs batch results — confirm identical pass rate (batch is async delivery, not a different judge).
- [ ] Cost comparison: synchronous API spend vs batch API spend — confirm ~50% reduction.
- [ ] Regression check: `python tools/quality_probe.py` baseline still 92.0% (no retrieval regression from the refactor).

---

## 8. FUTURE — paste-ready cost-banking prompt

> **NOT FOR THIS SESSION.** Use this prompt to open the batch-adoption session after entanglement is resolved and Adam GO is given.

---

```
VoxCore batch-eval session. Prerequisites confirmed:
- tools/citation_scorer.py and tools/quality_probe.py are clean (no uncommitted changes).
- tools/anthropic_helpers.py self-test PASS (submit_batch dry_run confirmed).
- Adam GO given for Batch API adoption.

Task: Build tools/batch_eval.py — a NEW file (do not edit the entangled files).

Requirements:
1. Collect judge requests from quality_probe's 50-query gold-set sweep as a list of
   {"custom_id": <query_id>, "params": {model, max_tokens, system, messages}} dicts.
2. Call `from tools.anthropic_helpers import submit_batch`.
3. Default: dry_run=True — write JSON plan to AI_Studio/Reports/batch_eval_dryrun.json, no spend.
4. --submit flag: dry_run=False — submit live batch, write job ID to the same JSON.
5. Keep synchronous path (existing quality_probe behavior) as the default for interactive use.
6. After live submit: poll for results; write results to AI_Studio/Reports/batch_eval_results.json.
7. Compare results to the 92.0% baseline (run_id 43b4e9ba4752_20260504) — must not regress.
8. Report before/after cost: synchronous spend vs batch spend on the same gold set.

Constraints:
- Do NOT edit citation_scorer.py or quality_probe.py directly.
- Do NOT enable caching (JUDGE_PROMPT = 169 tok < 1024 floor = $0).
- do NOT change the synchronous default path.
- Measurement-discipline: same gold set, same snapshot, report both regressions and lifts.
```

---

## 9. Status summary

| Lever | Status | Verified saving | Blocker |
|-------|--------|----------------|---------|
| Prompt caching | NOT APPLICABLE | $0 (JUDGE_PROMPT 169 tok < floor) | No call site qualifies today |
| Model router | BUILT, NOT WIRED | $0 delta (defaults already match) | Zero importers; entanglement gate |
| Batch API on eval sweep | BLOCKED | ~50% on eval sweeps (unverified end-to-end) | Entanglement (citation_scorer +93, quality_probe +23) + urllib refactor + async workflow decision |

**Verified real cost banked to date: $0.**
**Verified real lever available: Batch API (~50% on eval sweeps), blocked on reconciliation.**
