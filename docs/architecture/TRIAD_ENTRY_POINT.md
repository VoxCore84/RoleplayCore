# Triad Orchestration — Entry Point and Routing

**Verified:** 2026-05-02
**Resolves:** Checklist Cat 1 — "Triad entry point identified — what file, what function routes Architect → Executor → Auditor?"

---

## Entry point

| Layer | File | Symbol |
|-------|------|--------|
| **Routing function** | `tools/ai_studio/orchestrator.py:168` | `TriadOrchestrator.orchestrate(user_prompt)` |
| **CLI** | `tools/ai_studio/orchestrator.py:202-209` | `__main__` — `python tools/ai_studio/orchestrator.py "<request>"` |
| **Class** | `tools/ai_studio/orchestrator.py:40` | `class TriadOrchestrator` |

A user request enters at `orchestrate()`, which calls `run_architect` → `run_executor` → `run_auditor` in sequence with up to 3 retry iterations on auditor reject.

---

## Role assignments

| Role | File | Function | Provider | Model |
|------|------|----------|----------|-------|
| **Architect** | `orchestrator.py:55-90` | `run_architect(user_prompt) -> str` | Google | `gemini-3.1-pro` (env: `ORCHESTRATOR_GEMINI_MODEL`) |
| **Executor** | `orchestrator.py:92-122` | `run_executor(spec) -> list[str]` | Anthropic | `claude-opus-4-7` |
| **Auditor** | `orchestrator.py:124-166` | `run_auditor(spec, modified_files) -> tuple[bool, str]` | Google | `gemini-3.1-pro` (same as Architect, but separate invocation with different system prompt — see "Auditor independence" below) |

The Architect and Auditor share the same provider in this minimal orchestrator. The full **5-Round Review Cycle** (`tools/ai_studio/review_cycle.py`) uses true cross-provider independence — Codex (OpenAI), Gemini (Google), Claude (Anthropic) — and is the version invoked for non-trivial reviews.

---

## Routing logic — orchestrate()

`orchestrate()` (lines 168-200) is the canonical Architect → Executor → Auditor pipeline:

```
1. spec = run_architect(user_prompt)                    # Gemini designs spec
2. for attempt in 1..3:
3.     executor_prompt = spec [+ prior_feedback]
4.     modified_files = run_executor(executor_prompt)   # Claude proposes file list
5.     success, reason = run_auditor(spec, modified_files)  # Gemini verifies
6.     if success: break
7.     prior_feedback = reason                          # auditor reject → executor retry
8. if not success: pipeline aborts
```

Up to 3 iterations of executor-then-auditor before giving up.

---

## Auditor verdict enforcement

`run_auditor` returns `(bool, str)`. The orchestrate loop branches on the bool:

- **PASS** (line 191-192): pipeline marks SUCCESS and exits the retry loop. The Executor's draft is the final output.
- **FAIL** (line 193-197): the Auditor's `reason` becomes `prior_feedback`, fed into the next Executor call. The Executor's flagged output never gets shipped because the loop only emits a final result when the Auditor passes. After 3 failed attempts, the pipeline aborts with no output.

The Auditor returns FAIL by default if Gemini emits anything other than "PASS" / "FAIL" (line 164-166: "Defaulting to FAIL"). This is **fail-closed** — ambiguous Auditor output blocks ship, never the other way.

---

## Auditor independence

The Auditor sees:
- The original spec (`spec_content`)
- The list of files the Executor proposed (`modified_files`)

The Auditor does NOT see:
- The Executor's reasoning chain
- Any intermediate state from the Executor's call

This isolation is what prevents the "self-confirmation" failure mode of single-model RAG: the role that drafts is not the role that verifies.

In the minimal `orchestrator.py`, the Architect and Auditor share a model (`gemini-3.1-pro`) but execute in separate API calls with different system prompts. The 5-round `review_cycle.py` swaps in cross-provider independence (Codex/Gemini/Claude all participate as peer reviewers + Codex returns to verify, Gemini final-seals).

---

## Model identifier selection

| Role | How model is resolved | Override |
|------|-----------------------|----------|
| Architect | `GEMINI_MODEL = os.environ.get("ORCHESTRATOR_GEMINI_MODEL", "gemini-3.1-pro")` (line 37) | `ORCHESTRATOR_GEMINI_MODEL=<id>` env |
| Executor | Hardcoded `"claude-opus-4-7"` (line 100) | requires code edit |
| Auditor | Same `GEMINI_MODEL` constant as Architect (line 141) | same env |

For the 5-round `review_cycle.py`, model IDs are arguments passed to `call_claude.py`, `call_gemini.py`, `call_chatgpt_review.py`, `call_codex_review.py`.

**Future hardening (Cat 1 follow-on):** lift Executor model from hardcoded constant to env var (e.g., `ORCHESTRATOR_EXECUTOR_MODEL`) for parity with Architect / Auditor. Trivial edit; not currently a blocker.

---

## Failure modes

| Case | Behavior |
|------|----------|
| Architect API error | `spec_content = f"**ERROR**: Architect call failed: {e}"` (line 86-87). Pipeline continues with the error string as the spec — Executor will produce a meaningless file list, Auditor will FAIL, retry loop ends after 3. **Hardening candidate:** abort early if Architect fails. |
| Executor JSON parse failure | `modified_files = []` (line 117-119). Auditor gets empty list, FAILs, executor retries. |
| Auditor API error | Returns `(False, "Gemini API error: ...")`. Pipeline retries up to 3x then aborts. **Fail-closed.** |
| Auditor returns non-PASS/FAIL | Defaults to FAIL (line 164-166). **Fail-closed.** |
| 3 consecutive fails | "Pipeline aborted after 3 failed attempts." — no output shipped. |

---

## Observability

The orchestrator prints colored role banners (`[Architect]`, `[Executor]`, `[Auditor]`) to stdout. There's no structured trace logging in `orchestrator.py` itself. The 5-round `review_cycle.py` writes feedback files to `AI_Studio/Reports/Audits/` and timestamped JSON traces; for `orchestrator.py` runs, the only persistent record is the pipeline's stdout capture.

**Hardening candidate (Cat 1):** add JSON trace logging to a new file `AI_Studio/Reports/scheduled/orchestrator_trace_<ts>.json` containing `{user_prompt, spec, attempts: [{executor_files, auditor_verdict, auditor_reason}], outcome}`. Mirrors the citation_scorer telemetry pattern.

---

## Cost & latency

Not yet instrumented. **Cat 1 follow-on items:**
- Cost per query, broken down by role
- Latency p50/p95/p99 across runs
- Model swap test (e.g., swap Executor to Sonnet 4.6 — does anything break?)

---

## Companion: 5-Round Review Cycle

`tools/ai_studio/review_cycle.py` is the larger sibling for non-trivial reviews:

- Phase 1 (parallel): Codex + Gemini + Claude review same artifact simultaneously
- Phase 2 (sequential): Codex verifies fixes against all Phase 1 feedback
- Phase 3 (sequential): Gemini final-seal with all prior feedback

Roughly 15 min per cycle (vs ~45 min sequential). Used by `/triad` skill and Triad pipeline outside the minimal orchestrator.
