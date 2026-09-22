# Fan-Out Scaling — Confident 100-Agent Dispatch (P0 Reliability)

Single source of truth for HOW to dispatch parallel agents at scale. `/swarm`, `/deep-investigate`,
and `/ex-ask` all reference this file. Every numeric claim below was verified against live docs on
2026-06-22 (see § Verified-facts reference); addenda marked (v2.1.NNN) were verified against the official
changelog on 2026-09-22 during the 2.1.215 → 2.1.278 update sweep. UNVERIFIED / community-sourced items
are fenced as such — do not promote them into "do this" guidance without re-sourcing
(`completion-integrity.md` verify-before-recommend).

---

## Why 40+ agents in one message melts down (the root-cause model)

Dispatching N agents as N parallel `Agent` tool calls **in a single assistant message** has **zero
backpressure** — the harness tries to open all N full Claude conversations at once. At ~40 they collide on:

1. **The 1M-context credit gate.** ~~This machine's `~/.claude/settings.json` sets
   `CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-4-6[1m]`, so **every sub-agent runs at 1M context**.~~
   Sonnet 4.6 1M **requires extra-usage credits on every subscription plan** (model-config.md). With
   extra-usage off, *all* spawned sub-agents fail with "Extra usage is required for 1M context"
   **before consuming a token** — 1 failure or 100, same instant. (Logged 7+ times, sessions 263–278h.)
   **[Resolved 2026-09-22]:** subagent pin migrated to `claude-sonnet-5` — natively 1M, **no `[1m]` suffix
   exists for it, no usage credits required on any plan** (live model-config docs). The gate no longer
   applies on this machine; mechanism kept as history because any future `[1m]`-suffixed pin reintroduces it.
2. **ITPM, not RPM, is the binding limit.** Long-context agents are input-token-heavy. 40 cache-cold
   agents at ~50K input each = 2,000,000 input tokens/min = the *entire* Tier-4 Sonnet ITPM ceiling
   in one burst (api/rate-limits). RPM (4,000 at Tier 4) is nowhere near the bottleneck.
3. **Acceleration-limit 429s.** A sharp usage spike triggers 429 *independent of* your per-minute
   ceiling. The docs' fix is explicit: "ramp up your traffic gradually." Firehosing is the anti-pattern.

The fix is not "fewer agents" — it is **bounded concurrency + queuing + caching + graceful retry**.
The harness already ships a primitive that does all of this: the **Workflow tool**.

---

## The three execution modes — pick by N

| N (logical agents) | Mode | Mechanism | Why |
|---|---|---|---|
| **1 – 16** | **A — Wave** | single message, parallel `Agent` calls | Under the harness's own concurrency line; simplest; today's behavior |
| **17 – ~1000** | **B — Workflow-queued** | author a `Workflow` script (`pipeline()`/`parallel()`) | **The 100+-unit answer** (NOT 100 simultaneous). Bounded to ≤16 concurrent, queues the rest, retries terminal errors, null-on-failure, resumable |
| **huge, mechanical, non-urgent** (N ≳ 200) | **C — Batches** | Python script → Message Batches API | Separate rate-limit pool, 50% cost, results <1hr; sidesteps real-time ITPM entirely |

Default decision: **N ≤ 16 → Mode A. N > 16 → Mode B.** **B and C overlap at large N** — choose **C** only when
N is large (≈200+), the work is **fully mechanical**, AND results in <30 min are acceptable. If latency matters
at any N, prefer **B**.

### Mode A — Wave (N ≤ 16)
- All agents in ONE message (parallel, not sequential).
- Harness backstop: `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` caps concurrently-running subagents per message
  (default 20, v2.1.217) — one message can no longer fan out unbounded background agents.
- **Canary first** if the prompt shape is novel: launch 2–3, confirm they don't insta-fail (auth/credit/empty),
  then launch the rest. Surfaces a systemic failure on 3 agents, not 16.
- Each agent gets a **deterministic, unique output path** (`.../wave_N/agent_K.md`) — never a shared file (clobber risk).
- Aggregation spot-checks 2–3 real output files (not all N — that's not the bottleneck).

### Mode B — Workflow-queued (17 → ~1000) — the confident-100 path
The `Workflow` tool **is** the production fan-out harness. It enforces, by construction, most of the
reliability primitives below:

- **Bounded concurrency:** up to **16 concurrent agents** (fewer on CPU-limited machines), excess **queues**.
  Pass 100 items to `parallel()`/`pipeline()`; only ~16 run at once, 84 wait. (workflows.md)
  **Override:** `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256, v2.1.269) raises the per-run cap for
  inference-bound fan-outs. Set per-run with ITPM headroom in mind — do NOT set globally in settings.json;
  the 16 default is the ITPM-safe posture.
- **Usage-limit resilience:** dynamic workflows pause when the usage limit is hit and continue automatically
  when it resets, instead of dropping the affected agents (v2.1.271).
- **Cheap to invoke:** the Workflow tool's prompt footprint is ~1k tokens (was 5.7k; script-writing reference
  moved to the bundled `workflow-authoring` skill, v2.1.248).
- **Failure isolation:** an agent that dies on a terminal API error after retries returns **null** — the
  batch never aborts. `.filter(Boolean)` the results.
- **Retry built in:** terminal API errors are retried before the null fallback.
- **Idempotency / resume:** `resumeFromRunId` returns cached results for unchanged `(prompt, opts)` calls —
  content-keyed, exactly the idempotency primitive below, for free.
- **Observability:** `/workflows` shows live per-agent progress; `log()` emits narrator lines.
- **Backstop:** 1,000 agents total per run.

Author the script to also exploit the levers (§ Throughput levers):
- **Shared cached preamble** — put common context/instructions/file-paths in ONE prefix the agents share;
  cache reads don't count toward ITPM, so 100 agents read it at ~0 ITPM each.
- **`pipeline()` by default**, `parallel()` only for true barriers (dedup/merge across all results).
- **`schema:`** on mechanical agents → forced StructuredOutput, no parse errors, model retries on mismatch.
- **`effort: 'low'`** on mechanical stages (extraction/triage) → cuts thinking-token (OTPM) pressure;
  reserve `high`/`max` for synthesis/verify stages.
- **Adversarial verify stage** for findings that will be acted on (legal/filing-grade): `find → verify` pipeline.

Mode B requires the Workflow tool's opt-in (the `ultracode` keyword, or the user asking for a workflow).
If not opted in, fall back to **Mode A in sequential waves** (≤16 per wave, finish a wave before the next).

### Mode C — Message Batches (huge mechanical, non-latency-sensitive)
For cataloging / classification / extraction over hundreds–thousands of units where you don't need answers
now: a Python script against the **Message Batches API** has its own rate-limit pool (shared across models),
costs **50% less**, and most batches finish **<1 hr** (Tier 4 allows 500K queued). Route here instead of
burning real-time ITPM on mechanical work.

---

## The seven reliability primitives (verified; Anthropic-specific corrections applied)

Mode B gives you **1, 2, 3, 5, and 7** by construction (bounded concurrency, backoff/retry, failure-isolation,
resume/idempotency via `resumeFromRunId`, observability via `/workflows`+`log()`) and **4 partially** (results are
journaled for resume — also write to disk if you want files). It does **NOT** give you **6**: a systemic
non-retryable error (401/402/403) makes Mode B return `null` for *every* unit rather than aborting, so it can
burn the whole queue against a 402-blocked account. **Always run a 1-agent canary before the full N**, even in
Mode B. In Mode A you own all seven.

1. **Bounded concurrency.** A semaphore/worker-pool caps concurrency but does **not by itself** cap the
   token *rate* — pair it with awareness of the ITPM ceiling (sized roughly by `ITPM / avg_input_tokens_per_agent`).
   Never "fan out all N at once." (Mode B's ≤16 cap is this primitive.)
2. **Exponential backoff with full jitter.** `sleep = random.uniform(0, min(CAP, BASE * 2**attempt))`,
   then `sleep = max(sleep, retry_after_header)`. Suggested `BASE=1s, CAP=60s, max_attempts=6`. Full jitter
   **substantially reduces** (does not *eliminate*) synchronized-retry thundering herds. Wrap **each call**, not the batch.
3. **Failure isolation (bulkhead).** Each worker `try/except` → `{id, status:'ok'|'failed', result, error}`.
   Collect via `gather(return_exceptions=True)` (NOT `TaskGroup` — it cancels siblings on first error).
   Report "X/N succeeded, Y failed", write the failure list for triage. Never abort the batch on one failure.
4. **Per-result durability.** Each worker writes its result to a **unique deterministic path** the instant it
   finishes, **atomically** (`tmp` file then `os.replace()` — NOT `os.rename()`, which raises on Windows if the
   target exists). Crash loss is bounded by *in-flight* count (≈pool size), not 1, and not the whole batch.
   Orchestrator assembles by globbing the results dir, not by holding return values in memory.
5. **Idempotency / resume.** Skip-key = `sha256(canonical_serialization(input))` with `sort_keys=True`
   (raw `sha256(input)` is unstable across dict insertion order). If `results/{key}.json` exists and is valid, skip.
   (Mode B: `resumeFromRunId` does this for you.)
6. **Staggered ramp + canary.** Don't start all workers in the same millisecond (acceleration-limit trap).
   Launch a 3-worker canary sequentially; **abort the whole batch** on a non-retryable error
   (401 auth / 402 billing / 403); then admit the rest. (Mode B queues ≤16 at a time = inherent ramp.)
7. **Live observability.** Maintain `(done, failed, in_flight, queued, total)` + ETA (`elapsed/done * remaining`).
   In Mode A, overwrite a `STATUS.txt` the operator can `tail` from another terminal. (Mode B: `/workflows` + `log()`.)

### Error-class routing (Anthropic API)
- **Stop the batch (systemic, non-retryable):** 401 authentication, 402 billing, 403 permission.
- **Retry with backoff:** 429 rate_limit (honor `retry-after`), 500, 503, 504, **529 overloaded** (Anthropic-side;
  back ALL workers off together — global overload — and jitter hard). **Only 429 carries a documented `retry-after`**;
  for 529 use your own jittered backoff.
- Acceleration-limit 429s can carry `x-should-retry: false` — respect it.

---

## Throughput levers (how to push the safe agent count UP)

1. **Prompt caching — the #1 lever.** `cache_read_input_tokens` do **NOT** count toward ITPM (except Haiku 3.5).
   `ENABLE_PROMPT_CACHING_1H=1` is already set here. A 100K shared preamble cached at 80% hit rate across 20
   Sonnet agents multiplies effective ITPM throughput ~5×. Put the common context in ONE cached prefix.
   Since v2.1.229 workflow fan-outs **stagger same-prefix sibling agents automatically** so later siblings read
   the cached prefix instead of re-paying it (`CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0` disables).
2. **Effort routing.** Mechanical extraction/triage → `effort: 'low'` (Sonnet is sufficient and far cheaper).
   Reserve `high`/`max` for synthesis, cross-document reasoning, filing-grade verification.
   Note: `xhigh` is **not** a real level on Sonnet 4.6 — it silently runs at `high`. **Sonnet 5 DOES support
   `xhigh`** (live effort table, 2026-09-22) — with subagents on Sonnet 5, the full low→xhigh range is real.
3. **Model routing.** Sonnet for structured/mechanical; Opus only for narrative synthesis / legal-accuracy /
   contradiction-with-stakes (per `feedback_swarm_authorization.md`).
4. **Batches API** for non-urgent mechanical work (separate pool, 50% cost) — § Mode C.
5. **Tier advancement** raises every ceiling (Tier 1 → 4 lifts Sonnet ITPM 30K → 2M).

---

## Preflight gates (check before a large dispatch)

- **[1m] extra-usage gate — RESOLVED 2026-09-22.** `CLAUDE_CODE_SUBAGENT_MODEL` is now `claude-sonnet-5`
  (natively 1M, no credit requirement on any plan). This gate only returns if a `[1m]`-suffixed pin does —
  in that case confirm extra-usage is enabled before a big swarm, or the whole fleet fails at once.
  `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` (v2.1.257) forces one model onto **every** subagent, ignoring per-spawn
  and agent-definition overrides — the clean one-var switch for temporary model reroutes.
- **ITPM headroom.** Estimate `concurrent_agents × avg_input_tokens` against your tier ceiling. If cache-cold
  and over budget, lower concurrency or warm the shared cache first.
- **Opt-in for Mode B.** Workflow tool needs `ultracode`/explicit ask. No opt-in → sequential Mode-A waves.

---

## Verified-facts reference (sources fetched 2026-06-22)

| Fact | Tag | Source |
|---|---|---|
| Workflow: up to **16 concurrent**, **1,000 total/run**; documented path for "dozens to hundreds" | ✅ VERIFIED | code.claude.com/docs/en/workflows.md |
| Subagents = "a few delegated tasks per turn"; workflows for larger | ✅ VERIFIED | workflows.md, agents.md |
| Sub-agents get fresh context, don't inherit parent conversation (fork is the exception) | ✅ VERIFIED | sub-agents.md, prompt-caching.md, agent-teams.md |
| Sonnet **[1m] requires extra-usage credits on ALL subscription plans**; off → fails before tokens | ✅ VERIFIED | model-config.md |
| Rate limits = **RPM + ITPM + OTPM**, token-bucket (continuous replenish; 60 RPM ≈ 1/sec) | ✅ VERIFIED | platform.claude.com/docs/en/api/rate-limits |
| Sonnet 4.x ITPM: **Tier 1 = 30K, Tier 4 = 2M**; RPM Tier 4 = 4,000 | ✅ VERIFIED | api/rate-limits |
| **cache_read excluded from ITPM** (except Haiku 3.5) | ✅ VERIFIED | api/rate-limits |
| **Acceleration limits**: spikes → 429 independent of ceiling; ramp gradually | ✅ VERIFIED | api/rate-limits, api/errors |
| Message Batches: separate pool, **50% cost**, <1hr, Tier 4 = 500K queued | ✅ VERIFIED | api/rate-limits, batch-processing |
| **Only 429** documented to return `retry-after`; 429 also fires on acceleration limits; SDK 2 retries default | ✅ VERIFIED | api/errors, SDK docs |
| **`xhigh` unsupported on Sonnet 4.6** → runs as `high` | ✅ VERIFIED | model-config.md |
| Concurrency formula `min(16, cpu_cores−2)` | ⚠️ UNVERIFIED (community) | GitHub #63938 (not official); empirically consistent with "up to 16" on this 32-core box — EXPERIMENTAL, not Tier-1 guidance. Moot in practice since v2.1.269: the official override below controls the cap |

**Changelog-verified addenda (official changelog, fetched 2026-09-22, update sweep 2.1.215 → 2.1.278):**

| Fact | Tag | Source |
|---|---|---|
| `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256) raises Workflow per-run concurrency for inference-bound fan-outs | ✅ VERIFIED | changelog v2.1.269 |
| `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` caps Mode-A concurrent subagents (default 20) | ✅ VERIFIED | changelog v2.1.217 |
| `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` applies one model to every subagent, ignoring per-spawn overrides | ✅ VERIFIED | changelog v2.1.257 |
| Workflow fan-outs auto-stagger same-prefix siblings for cache reads (`CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0` disables) | ✅ VERIFIED | changelog v2.1.229 |
| Dynamic workflows pause at usage limit, auto-continue at reset (agents not dropped) | ✅ VERIFIED | changelog v2.1.271 |
| Workflow tool prompt footprint ~1k tokens (was 5.7k) | ✅ VERIFIED | changelog v2.1.248 |
| Task tools (TaskCreate etc.) offered only on Claude 3.x/4.x models; `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` restores elsewhere (set here 2026-09-22) | ✅ VERIFIED | changelog v2.1.268 |
| TaskOutput tool removed; `TASK_MAX_OUTPUT_LENGTH`/`taskOutputMaxChars` have no effect (removed from settings here 2026-09-22) | ✅ VERIFIED | changelog v2.1.277 |

**Live-docs model verdicts (claude-code-guide agent, fetched 2026-09-22 — model-config.md + models table):**

| Fact | Tag | Source |
|---|---|---|
| Sonnet 5 is always 1M on the Anthropic API — "no 200K variant, no [1m] suffix to select, and no usage credits required on any plan" | ✅ VERIFIED | model-config.md, 2026-09-22 |
| Sonnet 5 supports `low/medium/high/xhigh/max`; Sonnet 4.6 has no `xhigh` | ✅ VERIFIED | model-config effort table, 2026-09-22 |
| Sonnet 5 list price $2 in / $10 out per MTok | ✅ VERIFIED | models table, 2026-09-22 |
| Fable 5.1 (`claude-fable-5-1`) is the default Fable; $10/$50; **2.5% cache-read rate ($0.25/MTok) vs standard 10% ($1.00/MTok)** | ✅ VERIFIED | model-config.md, 2026-09-22 |
| `ANTHROPIC_SMALL_FAST_MODEL` deprecated in favor of `ANTHROPIC_DEFAULT_HAIKU_MODEL` | ✅ VERIFIED | model-config.md, 2026-09-22 |
| Sonnet 4.6 per-MTok price | ⚠️ UNVERIFIED this sweep | legacy model absent from current comparison table; fetch its overview page before quoting a 4.6 price or delta |

This machine's config (verified against `~/.claude/settings.json`, 2026-06-22; re-verified and migrated
2026-09-22 after the 2.1.215 → 2.1.278 update):
`ANTHROPIC_MODEL=claude-fable-5-1` · `CLAUDE_CODE_SUBAGENT_MODEL=claude-sonnet-5` (native 1M, no credit gate,
xhigh-capable) · `ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-sonnet-5` (replaces deprecated
`ANTHROPIC_SMALL_FAST_MODEL`) · `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY=15` · `ENABLE_PROMPT_CACHING_1H=1` ·
`effortLevel=xhigh`.
2026-09-22 changes: model pins migrated (Fable 5 → 5.1 for 2.5% cache-read rate; Sonnet 4.6[1m] → Sonnet 5
killing the extra-usage gate) · `TASK_MAX_OUTPUT_LENGTH` removed (dead since v2.1.277) ·
`CLAUDE_CODE_ENABLE_TODO_TOOLS=1` added (task tools gated off Fable 5 since v2.1.268) ·
`syncClaudeAiSkills=false` / `syncClaudeAiPlugins=false` added (claude.ai account-skill sync opt-out, v2.1.275).

## Myths — do NOT repeat (gate-refuted)
- ❌ "100 agents is architecturally impossible" — waves + Workflow-queuing make it routine.
- ❌ "There's a 5–7 simultaneous-session ceiling" — that's 5–7 **RPM** for small teams, not sessions.
- ❌ "`xhigh` multiplies Sonnet 4.6 token cost" — Sonnet 4.6 has no `xhigh`; it runs `high`.
- ❌ "Both 429 and 529 return `retry-after`" — only 429 does.
- ❌ "A mid-wave crash loses ALL agent work" — incrementally-written outputs survive; only in-flight units are lost.

## Cross-references
- Operational engine: `~/.claude/commands/swarm.md` (Mode A/B/C decision + dispatch)
- Investigation fan-out: `VoxCore/.claude/commands/deep-investigate.md`
- Cited evidence fan-out: `VoxCore/.claude/commands/ex-ask.md`
- Standing authorization: `~/.claude/projects/C--Users-atayl-VoxCore/memory/feedback_swarm_authorization.md` (this rule **supersedes** its "20 concurrent" figure — Mode A ceiling is 16; N > 16 → Mode B)
- Agent hygiene (paths, incremental writes, verify-content): `<project>/.claude/rules/agent-practices.md`
- Verify-before-recommend gate (why the UNVERIFIED fences exist): `<project>/.claude/rules/completion-integrity.md`
