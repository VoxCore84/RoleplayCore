# Fan-Out Scaling — Confident 100-Agent Dispatch (P0 Reliability)

> Long form + history: docs/rules-reference/fan-out-scaling.md

Single source of truth for HOW to dispatch parallel agents at scale. `/swarm`, `/deep-investigate`, `/ex-ask` reference this file.

## The three execution modes — pick by N

| N | Mode | Mechanism |
|---|---|---|
| **1 – 16** | **A — Wave** | single message, parallel `Agent` calls |
| **17 – ~1000** | **B — Workflow-queued** | a `Workflow` script (`pipeline()`/`parallel()`); ≤16 concurrent, queues the rest, retries, null-on-failure, resumable |
| **N ≳ 200, mechanical, non-urgent** | **C — Batches** | Python → Message Batches API (separate pool, 50% cost, <1hr) |

Default: **N ≤ 16 → A. N > 16 → B.** Choose **C** only when N ≈200+, work is **fully mechanical**, AND results in <30 min are acceptable. If latency matters at any N, prefer **B**.

**Mode A:**
- All agents in ONE message (parallel, not sequential).
- **Canary first** if the prompt shape is novel: launch 2–3, confirm they don't insta-fail (auth/credit/empty), then launch the rest.
- Each agent gets a **deterministic, unique output path** (`.../wave_N/agent_K.md`) — never a shared file (clobber risk).
- `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` caps concurrent subagents per message (default 20).

**Mode B:**
- Requires the Workflow tool's opt-in (`ultracode`, or the user asking for a workflow). **No opt-in → Mode A in sequential waves** (≤16 per wave, finish a wave before the next).
- Put common context/instructions/file-paths in ONE shared cached prefix.
- **`pipeline()` by default**; `parallel()` only for true barriers (dedup/merge across all results).
- **`schema:`** on mechanical agents → forced StructuredOutput.
- **`effort: 'low'`** on mechanical stages (extraction/triage); reserve `high`/`max` for synthesis/verify.
- **Adversarial verify stage** for findings that will be acted on (legal/filing-grade): `find → verify` pipeline.
- `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256) is a per-run override only — do NOT set it globally in settings.json; 16 is the ITPM-safe default.

## The seven reliability primitives

Mode B gives you 1, 2, 3, 5, 7 by construction and 4 partially. It does **NOT** give you **6** — a systemic non-retryable error (401/402/403) makes Mode B return `null` for *every* unit rather than aborting. **Always run a 1-agent canary before the full N**, even in Mode B. In Mode A you own all seven.

1. **Bounded concurrency.** Never fan out all N at once. Size against the ITPM ceiling (`ITPM / avg_input_tokens_per_agent`).
2. **Exponential backoff with full jitter.** `sleep = random.uniform(0, min(CAP, BASE * 2**attempt))`, then `sleep = max(sleep, retry_after_header)`. `BASE=1s, CAP=60s, max_attempts=6`. Wrap **each call**, not the batch.
3. **Failure isolation (bulkhead).** Per-worker `try/except` → `{id, status, result, error}`. Collect via `gather(return_exceptions=True)` (NOT `TaskGroup` — it cancels siblings on first error). Report "X/N succeeded, Y failed". Never abort the batch on one failure.
4. **Per-result durability.** Each worker writes to a **unique deterministic path** the instant it finishes, **atomically** (`tmp` then `os.replace()` — NOT `os.rename()`, which raises on Windows if the target exists). Assemble by globbing the results dir, not by holding return values in memory.
5. **Idempotency / resume.** Skip-key = `sha256(canonical_serialization(input))` with `sort_keys=True` (raw `sha256(input)` is unstable across dict insertion order). If `results/{key}.json` exists and is valid, skip. (Mode B: `resumeFromRunId`.)
6. **Staggered ramp + canary.** Don't start all workers in the same millisecond. Launch a 3-worker canary sequentially; **abort the whole batch** on 401/402/403; then admit the rest.
7. **Live observability.** Track `(done, failed, in_flight, queued, total)` + ETA. Mode A: overwrite a `STATUS.txt`. Mode B: `/workflows` + `log()`.

### Error-class routing (Anthropic API)
- **Stop the batch (systemic, non-retryable):** 401 authentication, 402 billing, 403 permission.
- **Retry with backoff:** 429 rate_limit (honor `retry-after`), 500, 503, 504, **529 overloaded** (back ALL workers off together — global overload — and jitter hard). **Only 429 carries a documented `retry-after`**; for 529 use your own jittered backoff.
- Acceleration-limit 429s can carry `x-should-retry: false` — respect it.

## Preflight gates (before a large dispatch)

- **[1m] extra-usage gate — RESOLVED 2026-09-22.** `CLAUDE_CODE_SUBAGENT_MODEL` is `claude-sonnet-5` (natively 1M, no credit requirement on any plan). The gate returns only if a `[1m]`-suffixed pin does — then confirm extra-usage is enabled before a big swarm, or the whole fleet fails at once.
- **ITPM headroom.** Estimate `concurrent_agents × avg_input_tokens` against your tier ceiling. If cache-cold and over budget, lower concurrency or warm the shared cache first.
- **Opt-in for Mode B.** No `ultracode`/explicit ask → sequential Mode-A waves.
- **Model routing.** Sonnet for structured/mechanical; Opus only for narrative synthesis / legal-accuracy / contradiction-with-stakes.

## Myths — do NOT repeat (gate-refuted)
- ❌ "100 agents is architecturally impossible" — waves + Workflow-queuing make it routine.
- ❌ "There's a 5–7 simultaneous-session ceiling" — that's 5–7 **RPM** for small teams, not sessions.
- ❌ "`xhigh` multiplies Sonnet 4.6 token cost" — Sonnet 4.6 has no `xhigh`; it runs `high`.
- ❌ "Both 429 and 529 return `retry-after`" — only 429 does.
- ❌ "A mid-wave crash loses ALL agent work" — incrementally-written outputs survive; only in-flight units are lost.

UNVERIFIED / community-sourced items must NOT be promoted into "do this" guidance without re-sourcing (`completion-integrity.md` verify-before-recommend). Verified-facts tables, changelog addenda, machine config, throughput-lever detail, and all strikethrough history → reference file.
