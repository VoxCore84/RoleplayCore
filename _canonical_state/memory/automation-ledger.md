---
name: automation-ledger
description: "Per-session structured log of what was automated/built + pain→fix mapping with effort/status + compounding score (tag-overlap + judgment) tracking whether the system is converging."
type: project
originSessionId: 641e8d44-aaaa-4c7b-a5ff-b67650f03c9a
---
# Automation Ledger

> Append-only structured log replacing the narrative `improvements.md`. Written by `/wrap-up` Step 5.
>
> **Compounding score** = how many of THIS session's pain points were already addressed by prior session automation. Rising score across sessions = system is getting better at preventing its own pain.

## Compounding trend (last 10 sessions, by tag-overlap)

```
2/2 → N/A → 2/3 → 2/6 → 3/7 → 8/8 → 1/8 → 2/21 → 7/9
```
*(s.270 → s.271 → s.272 → s.273 → s.274 → s.274b → s.275 → s.277 → s.277b. **s.277b compounded HARD on s.277 work** because the 5-round Tier 1+2 knockdown built directly on s.277 foundations: citation_scorer.py extended (claim_kind helper, [synthesis] tag), inline_grounding.py extended (escape unescape), legalbench_harness.py extended (Claude judge backend), Triad orchestration pattern reused for ChatGPT-as-Architect spec generation, ADR 0005 updated, methodology rule durably encoded in feedback_calibration_overfit.md. The 2/9 NEW pain points were specific to the v4/v5 trade-offs not yet seen — Sonnet auditor calibration drift between rewrite-and-retry passes, top-k bump-doesn't-help finding.)*

## Tag vocabulary

Controlled vocab. Add new tags only when an existing one doesn't fit. Current set:
`kg`, `rag`, `ner`, `extract`, `ocr`, `audio`, `mcp`, `skill`, `hook`, `daemon`, `legal`, `db`, `build`, `audit`, `ui`, `llm`, `git`, `triad`, `wrap-up`, `case`, `mil`.

## Effort scale

- **LOW**: < 15 min, single file or trivial script
- **MED**: 15 min – 3 hr, new tool or non-trivial change
- **HIGH**: half-day+, pipeline or system-level

## Status values

- **DONE**: built and verified this session
- **QUEUED**: scoped for next session, in `todo.md`
- **DEFERRED**: acknowledged but not scheduled (workaround acceptable, or higher-priority blocks it)
- **ESCALATED**: hit 3+ occurrences, moved to `todo.md` HIGH

## Compounding score format

Two numbers, both visible:
- **By tag-overlap** (reproducible): count of THIS session's pain points whose tag set intersects any DONE entry from the prior 5–10 sessions.
- **With judgment** (subjective): claude reads prior entries and decides whether a prior fix actually addresses this pain (regardless of exact tag match).

Format: `Compounding: 3/7 by tag-overlap, 5/7 with judgment` followed by 2–4 lines of which prior session(s) match which current pain points.

---

## Entries

### Session 277b — 2026-05-02 — CONTRADICTS Auditor MVP + Economic Impact v3.1 + 5-round Tier 1+2 knockdown
**Built**:
- `tools/citation_holdout_synthesizer.py` v1 — initial held-out synthesizer (round 1)
- `tools/citation_holdout_synthesizer_v2.py` — one-quote-per-claim + FABRICATED verify-retry (round 2)
- `tools/citation_holdout_synthesizer_v3.py` — per-claim re-retrieval architecture (round 3+5; regex fixed)
- `tools/citation_holdout_synthesizer_v4.py` — adds CONTRADICTS Auditor MVP integration (round 4) — **production-recommended**
- `tools/citation_holdout_synthesizer_v5.py` — adds FABRICATED verify-retry on rewrite path (round 5; high-coverage alternative)
- `tools/inline_auditor.py` — Sonnet 4.6 in-pipeline CONTRADICTS judge with 0.70 confidence threshold (round 4)
- `tools/citation_rewriter_step1.py` — calibration-batch rewriter (round 1)
- `tools/citation_holdout_generator.py` — Claude Opus generates held-out queries with calibration exclusions (round 1)
- `tools/multihop_generator.py` — Claude Opus generates multi-hop queries with hop-type tags (round 4)
- `tools/spec_via_chatgpt.py` — wrapper for ChatGPT-as-Architect spec generation (round 3)
- `tools/throughput_measure.py` — per-modality cold-cache extraction throughput benchmark (round 3)
- `tools/legalbench_harness.py` extended with `_judge_via_claude` + `--judge-backend claude` flag (round 4)
- `tools/citation_scorer.py` extended with `claim_kind()` helper for `[synthesis]` tag honoring (round 1)
- `tools/inline_grounding.py` extended with `_unescape_inner()` for escaped-quote handling (round 1)
- 13 new docs: `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`, `docs/INGEST_LIFECYCLE.md`, `docs/LEGALBENCH_HARNESS_GUIDE.md`, `docs/COST_AND_LATENCY_BENCHMARKS.md`, `docs/DEPLOYMENT_MODEL.md`, `docs/architecture/MCP_TRANSPORT.md` (extended), `docs/architecture/CHUNKING_STRATEGY.md`, `Desktop/Do NOT Delete These/VoxCore_Economic_Impact_Analysis_v3.1.md`, `Desktop/Do NOT Delete These/VoxCore_Verification_Summary_3page.md`, `Desktop/Do NOT Delete These/VoxCore_JAG_Meeting_Agenda_and_Questions.md`, `Desktop/Do NOT Delete These/VoxCore_Adam_HumanActions_PrepPack.md`, `AI_Studio/2_Active_Specs/contradicts_auditor_v1_20260502_115918.md` (ChatGPT-generated), `~/.claude/projects/.../memory/feedback_calibration_overfit.md` (durable methodology rule)
- README full replacement (was WoW server description; now AI/citation product) + walkthrough audit (43/45 paths resolve; 1 real bug fixed)
- Desktop reorganization: 4 docs → `Do NOT Delete These/`, 4 → `Safe To Delete/`; canonical trackers stayed at root

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | Published "<2% hallucination" was inferred-not-measured; would not survive 5-min diligence Q&A | s.275 (PDF v2) | `audit`,`legal`,`llm` | v2 verify-retry shipped (held-out 30%→24.7%) + v4 auditor (24.7%→16.7% on shipped) + Economic Impact v3.1 with measured numbers + Verification Summary 3-page | HIGH | DONE |
| 2 | Calibration n=15 hit 0% but held-out n=35 was 30% — calibration overfit risk | NEW (s.277b) | `audit`,`llm` | Methodology rule durably encoded in `feedback_calibration_overfit.md`; operationalized 7-step gate in `docs/PUBLISHABLE_CLAIM_WORKFLOW.md`; confidence-tier rubric (PROVEN/WELL-SUPPORTED/etc.) | LOW | DONE |
| 3 | Same answers scored 45.5% (Gemma) vs 30.3% (Claude) — judge calibration was 15pp of "improvement" | NEW (s.277b) | `audit`,`llm` | All published numbers now specify the judge model; Claude judge added to legalbench_harness via `--judge-backend claude` flag for apples-to-apples | LOW | DONE |
| 4 | Model would invent plausible-sounding "verbatim" quotes when source didn't have them (24 FABRICATED on n=35 held-out) | s.277 (inline_grounding scoring catches) | `llm`,`legal`,`audit` | v2 verify-retry loop rewrites or [synthesis]-tags fabricated quotes BEFORE shipping (0/0 fabricated shipped on n=35 v2) | MED | DONE |
| 5 | Model would pair claims with quotes that DIRECTLY CONTRADICTED the claim (14 CONTRADICTS on n=35 v2; legal-malpractice grade) | NEW (s.277b) | `llm`,`legal`,`audit` | v4 CONTRADICTS Auditor MVP — Sonnet 4.6 inline judge + 0.70 confidence threshold + targeted rewrite + `[AUDITOR_FAILED]` hold tag (0 silent CONTRADICTS shipped) | HIGH | DONE |
| 6 | v4 rewrite path bypassed FABRICATED verify-retry → 5 new fabricated quotes appeared on rewrites | NEW (s.277b) | `llm`,`audit` | v5 adds `call_with_fabricated_retry` wrapping rewrite calls (0 fabricated on rewrites in v5) | MED | DONE |
| 7 | v3 [grounded]-tag regex was brittle — matched 0/35 real answers because model put tag AFTER claim sentence | NEW (s.277b) | `llm` | Replaced regex with `inline_grounding.extract_inline_quotes` + sentence-boundary walk-back (offline-validated 20/35 with 72 deduped claims) | LOW | DONE |
| 8 | Per-claim re-retrieval architecture executes correctly (16/35 refined) but doesn't beat v2 — IRRELEVANT is synthesis problem, not retrieval | NEW (s.277b) | `rag`,`llm` | Negative finding documented — v6 should extend auditor to PARTIAL/IRRELEVANT verdicts (queued for next session) | MED | QUEUED |
| 9 | Two parallel Opus jobs hit API rate-limit contention; v3b ran 45+ min silent then was killed | s.277 (parallel API spawn issues) | `llm` | Sequential execution policy adopted for next session; PYTHONUNBUFFERED=1 standardized for Python background scripts | LOW | DEFERRED |

**Compounding**: 7/9 by tag-overlap, 8/9 with judgment
- Tag-matched: #1 (`legal`,`llm` ↔ s.275 + s.277), #2-#3 (`audit`,`llm` ↔ s.277), #4 (`llm`,`legal` ↔ s.277), #5 (`llm`,`legal`,`audit` ↔ s.277), #6-#7 (`llm`,`audit` ↔ s.277), #9 (`llm` ↔ s.277)
- Judgment-additional: #8 — per-claim re-retrieval is a sibling of the chunk-fetch refinement work in s.277 even though the negative finding is new. The architecture is one s.277 ADR away from being a planned next step.
- New (no prior session): #2 calibration-overfit (a methodology lesson, not addressable by prior tooling)

**Pattern detection / escalation**:
- Pain #2 (calibration overfit) — first occurrence, but it's CLASS-OF-FAILURE serious (would have killed the diligence call). Encoded as durable memory rule rather than one-session fix. Watch for recurrence: any future "X% on calibration" claim without a held-out re-run is the alarm trigger.
- Pain #9 (parallel Opus API contention) — second occurrence in 2 sessions. **Escalation candidate** if hit again next session: build a `python tools/api_serializer.py` script-runner that queues Opus jobs and prevents concurrent submission. LOW effort.
- All other pain points are addressed by the v4 + queued-v6 architecture and don't compound across sessions in a recurring way.

### Session 274b — 2026-04-28 — GraphRAG Steps 5-8 (KG MCP Tools + Multi-Hop BFS + Pre-Fetch + Semantic Contradiction Filter)
**Built**:
- `tools-dev/docs-rag/docs_rag_logic.py` — 4 KG wrapper functions + recursive hot-reload (gitignored, local-only)
- `tools-dev/docs-rag/docs_rag_server.py` — 4 MCP tool registrations + improved `docs_rag_reload` (gitignored)
- `tools/excluded_daemon/kg/query.py` — `entity_expand(entity_id, hops, max_entities, per_hop_cap, compact)` with salience ranking
- `.claude/commands/ex.md` — "Pre-flight: KG entity context" section (Steps A-D) with ambiguity caveat
- `tools/excluded_daemon/jobs/contradiction.py` — `_semantic_compare`, `_filter_semantic`, semantic_filter param threading, degraded-state warning, CLI flags

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | MCP output token limit (~25k tokens) blocks rich tool responses; forces file-output workaround that disrupts caller flow | NEW | `mcp` | Added `compact: bool = False` to entity_expand; MCP wrapper opts in (89KB→35KB, 60% reduction). Pattern reusable for any large MCP response. | LOW | DONE |
| 2 | Hot-reload of MCP logic doesn't propagate to lazily-imported submodules (cached in sys.modules); chicken-and-egg when fixing a downstream module | NEW | `mcp`, `daemon` | Extended `docs_rag_reload` to recursively reload `tools.excluded_daemon.kg.*` modules. Future kg.* edits no longer need MCP restart. | LOW | DONE |
| 3 | KG only has one predicate (`mentioned_with`) at uniform 0.7 confidence — ties drown signal in popular-org noise (Adam → USAF/DoD before Johnston/McMaster) | s.273 | `kg`, `ner` | Salience ranking `kind_bonus × log(mentions) × relation_count × confidence`; persons 3x over orgs 0.7x. Future v2: enrich predicates from semantic NER pass. | MED | DONE (mitigation); predicate enrichment DEFERRED |
| 4 | KG fuzzy LIKE matching produces substring noise on short tokens ("ET" → 647 hits including "DHA Market/Intermediate Headquarters") | NEW | `kg` | Documented ambiguity caveat in /ex ask pre-flight; agents fall back to corpus search when ambiguous. Future: confidence threshold OR canonical-only matching for ≤3-char queries | LOW | DONE (caveat); MED (proper fix) DEFERRED |
| 5 | Contradiction scanner v1 produces 58 false positives on date co-occurrence | s.273 | `kg`, `audit`, `legal` | sonnet-4-6 binary classifier via urllib + ThreadPoolExecutor (5 workers, ~$0.07/scan); default-on for manual `/kg-query scan`, opt-out for daemon | LOW | DONE |
| 6 | Anthropic API credit balance depleted mid-session (HTTP 400 mid-task, surfaces as silent zero results without warning) | NEW | `llm` | Added degraded-state warning in scanner (>50% ERROR rate triggers banner in log + JSON output + report header) so a billing-blocked run never reads as "no contradictions." | LOW | DONE |
| 7 | MCP server restart pain (had to reconnect 2x this session for new tools / fixed signature) | s.265 | `mcp`, `wrap-up` | Recursive reload helper covers module-edit case (no future restart for kg.* edits). Server-file edits still need restart — that's a CC harness limitation, not addressable here. | LOW | DONE (partial) |
| 8 | PEP-8 nit: `import math` inside `entity_expand` instead of module top | NEW | `audit` | Trivial cleanup, deferred — purely cosmetic, doesn't recur, doesn't block anything | LOW | DEFERRED |

**Compounding**: 8/8 by tag-overlap, 8/8 with judgment
- Tag-matched: #1 ↔ s.270 (`mcp` voxcore-db ToolError), #2 ↔ s.269/272 (`mcp,daemon` hook overhaul + sync), #3 ↔ s.273 (`kg,ner` KG build), #4 ↔ s.273 (`kg`), #5 ↔ s.273 (`kg,audit` v1 scanner — direct successor), #6 ↔ s.273 (`llm` backend), #7 ↔ s.265 (`mcp`) + s.274 (`wrap-up`), #8 ↔ s.272 (`audit` test harness, s.270 hook verification)
- Judgment-additional: same as tag-matched. This is the first session with full overlap because it built directly on the foundations of s.265-273.
- Special note: pain #5 is the cleanest compound — it was the QUEUED followup from s.273 retro #4 ("contradiction scanner v1 produces false positives — needs semantic comparison"). Built and shipped one session later. The wrap-up s.273 → s.274b cycle is the first to demonstrate the queue-and-build pattern working end-to-end.

**First-encountered tracking**:
- Pain #3 (uniform predicate confidence) was implicit in s.273 KG build but didn't surface as a problem until BFS traversal exposed it. 1 session lag.
- Pain #5 surfaced s.273 (acknowledged in retro #4); fixed s.274b. 1 session lag — fastest queue-to-fix cycle so far.
- Pain #7 (MCP restart) goes back to s.265+ MCP server adoption. The fix this session is partial (kg.* edits covered, server.py edits still need full restart).

**Note**: This is the highest compounding score yet (8/8). Every pain point had prior-session tag overlap because the work built directly on the established `mcp`/`kg`/`ner`/`daemon`/`wrap-up` infrastructure. The system has reached the regime where new work mostly extends existing patterns — predicted by the s.274 retro thesis ("future sessions should now show tighter overlap").

### Session 274 — 2026-04-28 — Wrap-Up Refactor (Resume Evidence + Automation Ledger + Quick-Win Gate)
**Built**:
- `.claude/commands/wrap-up.md` — 7-step rewrite (218 lines), 30-min soft cap on quick-win build time, hard-stop on failure
- `memory/resume-evidence.md` — STAR-format per-session log (108 lines, 9 backfilled)
- `memory/automation-ledger.md` — structured pain→fix + compounding score (157 lines, 5 backfilled, this is the file)
- (deleted) `.claude/commands/retro.md` — absorbed into wrap-up Step 5

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | Wrap-up ceremony 5–7 min — gets skipped or rushed | NEW | `wrap-up` | Cut 8 → 7 steps; drop redundant Cowork-already-covers parts (gist check, Central Brain, session_state.md) | LOW | DONE |
| 2 | Resume-worthy accomplishments lost in narrative `recent-work.md` (no one reads it for resumes) | NEW | `wrap-up`, `skill` | `memory/resume-evidence.md` per-session STAR log + tag vocabulary | LOW | DONE |
| 3 | Retro auto-build rule existed since s.262 but rarely fired (last step of session, format didn't expose effort/impact) | s.262 | `wrap-up`, `audit` | Quick-win gate moved BEFORE session-complete; tightened LOW-effort rule to require 2+ in-session occurrences (was hypothetical) | LOW | DONE |
| 4 | `improvements.md` is narrative — no compounding visibility, no trend, no tag analytics | NEW | `wrap-up`, `audit` | `automation-ledger.md` with controlled-vocab tags + dual compounding score (tag-overlap + judgment) + trend line | LOW | DONE |
| 5 | `/retro` skill exists but user said "never use it" — dead code | NEW | `skill`, `wrap-up` | Absorb into wrap-up Step 5; `git rm` the skill | LOW | DONE |
| 6 | Central Brain auto-update at every wrap-up was redundant with Cowork bridge | NEW | `wrap-up` | Drop from wrap-up; document "manual when major Triad context shifts" | LOW | DONE |
| 7 | Periodic Resume Updates folder snapshots (role-framed) are manual today | NEW | `skill`, `wrap-up` | `/resume-snapshot` skill aggregating resume-evidence.md → role-framed file in `Resume Stuff/Resume Updates/` | LOW | QUEUED |

**Compounding**: 3/7 by tag-overlap, 6/7 with judgment
- Tag-matched: #2, #5, #7 (`skill` ↔ s.273 `/kg-query`, s.272 sync checker, s.267 `/triad`, s.263 combo skills — `skill` is well-established).
- Judgment-additional:
  - #3 ↔ s.262 (retro pattern detection rule was the prior attempt at this — same problem, looser mechanism). Same class as today's fix.
  - #4 ↔ s.211 quick-wins batch + s.262 pattern detection (both prior attempts at structured improvement tracking; this session formalizes them).
  - #6 ↔ s.258 Excluded KB stack made memory-files-via-bridge possible — Central Brain became redundant retroactively.
- Judgment dissent on #1: this is a genuinely-new diagnostic ("wrap-up itself is the bottleneck") — no prior session had cut wrap-up time as a goal. Counted only by tag-overlap if at all.

**First-encountered tracking**:
- Pain #3 first surfaced session 262 (retro auto-build rule) — 12 sessions to actually re-engineer the trigger so it fires. Worth flagging: the rule existed but the FORMAT and POSITION of the rule in the workflow were wrong. Fix took 12 sessions because the symptom was "didn't fire" rather than "didn't exist," which is a much harder diagnosis.

**Note**: This session was the meta-session — it built the system that captures session work. The compounding score is moderate (3/7) because `wrap-up` itself is a sparsely-tagged dimension in prior entries. Future sessions should now show tighter overlap because the framework exists to capture and tag improvement work consistently.

---

### Session 273 — 2026-04-27 — Knowledge Graph Build
**Built**:
- `/kg-query` — slash command exposing KG entity API
- `tools/excluded_daemon/kg/` — entity/mention/relation SQLite database, NER worker, dedup utility, query layer
- `tools/excluded_daemon/workers/llm_worker.py` — daemon LLM dispatch with dual-backend round-robin
- `tools/excluded_daemon/jobs/contradiction.py` — synthesis-vs-source contradiction scanner v1

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | Ollama qwen3.5 stashes JSON in `thinking` field instead of `response` | NEW | `llm`, `kg` | Read from `thinking` field + type guards | LOW | DONE |
| 2 | LLM type variability (string vs dict, None vs "") crashed build twice | NEW | `llm`, `kg` | Defensive type-guard pattern library | LOW | DONE |
| 3 | KG build crashes lose work | NEW | `kg`, `daemon` | Crash-resume via `already_seen` content-addressed set | LOW | DONE |
| 4 | Cautious worker ramp-up wasted ~30 min | NEW | `daemon`, `kg` | Start parallel-heavy from session 1 | LOW | DEFERRED (mindset, not code) |
| 5 | Contradiction scanner v1 false positives (date co-occurrence ≠ contradiction) | NEW | `audit`, `kg` | Semantic comparison instead of date overlap | MED | QUEUED |
| 6 | No `/kg-query` skill — KG only reachable via Python CLI | NEW | `kg`, `skill` | Build slash command | LOW | DONE |
| 7 | UKB `06_Case_Intelligence/` not updated with KG pipeline doc | NEW | `legal`, `kg` | Write pipeline doc | LOW | QUEUED |

**Compounding**: 2/7 by tag-overlap, 3/7 with judgment
- Tag-matched: #3 (`daemon` ↔ s.269/272), #6 (`skill` ↔ s.263 combo skills, s.267 `/triad`)
- Judgment-additional: #1,#2 (`llm` defensive coding) ↔ session 244 config-API verification mismatch (same "verify before assuming" class)
- Note: KG/NER is a new domain in s.273, so most pains are NEW. Future KG-adjacent sessions should show much higher overlap.

---

### Session 272 — 2026-04-27 — Hook Unification
**Built**:
- `~/.claude/hooks/check_hook_sync.py` — VoxCore↔CalmCore parity checker
- 4 Windows symlinks: `hook_daemon.py`, `daemon_shim.py`, `compact-reinject.py`, `deadline-alert.py` (CalmCore → VoxCore source-of-truth)
- Tribal knowledge regex extraction in `handle_db_failure_chain` daemon route (7 SQL keywords + MySQL error patterns)

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | Git Bash `ln -s` silently creates copies instead of symlinks on Windows | NEW | `build`, `git` | Use Python `os.symlink()` (caught after one round-trip) | LOW | DONE |
| 2 | Hook drift between VoxCore and CalmCore (2+ weeks unnoticed) | NEW | `hook`, `daemon` | Symlinks + parity checker | LOW | DONE |
| 3 | Word-boundary mismatch in tribal_knowledge `wrong` field substring match | NEW | `audit`, `db` | Tighten with word boundaries | LOW | DEFERRED (low priority) |

**Compounding**: 2/3 by tag-overlap, 2/3 with judgment
- Tag-matched: #2 (`hook`,`daemon` ↔ s.269 hook overhaul), #3 (`db` ↔ s.250 DB lint patterns)
- Note: This session was a direct extension of s.269 — the high overlap is expected and welcome. The system caught its own drift.

---

### Session 271 — 2026-04-27 — Env Config (PowerShell tool)
**Built**: nothing (one-line settings change).
**Pain → Fix**: N/A (trivial single-config session).
**Compounding**: N/A — excluded from trend.

---

### Session 270 — 2026-04-27 — MCP ToolError Routing
**Built**:
- `_return_or_raise()` helper in `tools/mcp-voxcore-db/src/voxcore_db/server.py`
- 6 voxcore-db tool wrappers updated to raise on runtime errors

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | MCP server changes can't be tested in same session (server is process-managed) | NEW | `mcp` | Test prompt for next session (workaround) | HIGH | DEFERRED (would need MCP-test framework) |
| 2 | Built s.269 chain handlers against an event that never fired (FastMCP returned errors as success) | NEW | `hook`, `mcp` | `/hooks-test` skill that mocks MCP calls and verifies which event fires | MED | QUEUED |

**Compounding**: 2/2 by tag-overlap, 2/2 with judgment
- Tag-matched: both pains (`mcp`, `hook`) overlap with s.269 hook overhaul.
- Note: This session was the AUDIT pass on s.269's work — high overlap is the system catching its own gap. Pain #2 is a meta-pain ("built infrastructure against unverified trigger path") that should be a checklist item before any future hook work.

---

### Session 269 — 2026-04-27 — Hook Infra Overhaul (genesis)
**Built**:
- `.claude/hooks/hook_daemon.py` v1.3.0 (24 routes, 4 hook types in use)
- 38 hooks across 13 events (was 22 across 2 events)
- 5 MCP tool hooks (auto-tail server.log, auto-tail DBErrors, tribal knowledge on DB failure, diagnose startup failure)
- 3 chain handlers (build-failure-chain, db-failure-chain, server-failure-chain)
- 1 prompt hook (Haiku quality gate on `tools/publishable/`)
- duration_ms pipeline (capture → JSONL → slow-tool alerter → statusline → analytics → calibration)
- Tab ownership conflict detection on Edit/Write to shared files
- JSONL rotation on startup (14MB → 3.4MB)
- 17 dead standalone hook scripts deleted
- `.claude/hooks/AGENT_HOOK_EXAMPLES.md` documented

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | 1M context extra-usage gate blocks agent spawns (recurring s.263–268) | s.263 | `wrap-up` | WebSearch/WebFetch fallback (workaround) | HIGH | DEFERRED (Anthropic-side) |
| 2 | settings.local.json duplicate hooks silently double every HTTP call | NEW | `hook` | `/hooks-audit` skill diffing settings files | LOW | QUEUED (~20 min) |

**Compounding**: 0/2 by tag-overlap, 0/2 with judgment — **GENESIS session for `hook`/`daemon` tags**.
- No prior automation in this domain; this session created the surface that subsequent sessions extend.

---

## How to use this file

- **At session end**: `/wrap-up` appends a new entry. Update the trend line at the top.
- **At session start**: optionally read the last 3 entries to see what pain has been addressed and what's queued.
- **For analysis**: scan the QUEUED column to see backlog. Scan DEFERRED for items that may have been wrong to defer.
- **For automation discovery**: when planning a new tool, search the ledger by tag to see what already exists.

## Migration notes

- `improvements.md` is superseded by this file as of session 273. New retros go HERE.
- Historical 5-bullet retros remain in `improvements.md` as read-only history.
- The pattern-detection rule (3+ occurrences → escalate) still applies, but it now reads from this file's QUEUED/DEFERRED columns instead of free-text bullets.

### Session 275 — 2026-05-01 — Measurement Infrastructure + Acquihire Prep
**Built**:
- `tools/citation_scorer.py` — citation precision/recall/hallucination composite scorer
- `tools/legalbench_harness.py` — Stanford LegalBench with Claude API + Ollama multi-model
- `voxcore-portfolio/` — Next.js portfolio website (FROZEN)
- `docs/acquihire/01-03` — JAG questions, IP chain of title, diligence checklist
- Desktop document system — 4 canonical tracking files
- `grep-case-enricher` hook — PostToolUse updatedToolOutput for case searches

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | No measured citation precision number | NEW | `rag`,`audit`,`legal` | Built citation_scorer.py | MED | DONE |
| 2 | No external benchmark scores | NEW | `llm`,`audit`,`legal` | Built legalbench_harness.py | MED | DONE |
| 3 | PDF claims are INFERRED not MEASURED | NEW | `audit`,`legal` | Verification pass + measurement pipelines | HIGH | DONE (infra), numbers pending |
| 4 | Agent spawns fail on 1M context | s.263 | `llm`,`mcp` | Platform limitation — accepted | — | DEFERRED |
| 5 | MCP tool-search deferral adds latency | NEW | `mcp` | alwaysLoad: true on all 17 servers | LOW | DONE |
| 6 | Desktop file sprawl | NEW | `audit` | Triage + sort 28 files to proper locations | LOW | DONE |
| 7 | No acquihire document suite | NEW | `legal` | Built 3 docs + 4 tracking files | MED | DONE |
| 8 | PyMuPDF AGPL blocks commercial use | NEW | `legal`,`audit` | Swap to pdfplumber recommended | LOW | QUEUED |

**Compounding**: 1/8 by tag-overlap, 2/8 with judgment
- Tag-matched: #4 (`llm`,`mcp` ↔ s.263-269 agent-gate work)
- Judgment-additional: #5 (`mcp` latency addressed by s.270 MCP server hardening pattern)


### Session 277 — 2026-05-02 — 15-Item Knockdown + Inline-Grounded Citations + 7 ADRs
**Built**:
- `tools/inline_grounding.py` — Anthropic Citations API pattern: extract inline quotes, substring-verify in source
- `tools/pdf_lib.py` — pdfplumber+pypdfium2 shim replacing PyMuPDF/AGPL (9 consumers updated)
- `tools/msg_extract.py` — olefile-based .msg parser replacing extract-msg/GPL
- `tools/governance_audit.py` — append-only JSONL audit log + CLI
- `tools/secrets_scan.py` — full git-history credential scanner (gitleaks alternative)
- `tools/deps_audit.py` — requirements-file auditor + .pinned.txt generator
- `tools/wer_measure.py` — word/char error rate via Levenshtein C-extension
- `tools/ocr_accuracy.py` — pdfplumber-vs-Tesseract OCR accuracy methodology
- `tools/citation_scorer.py` extended — LLM-as-judge wrapper + two-path scoring (inline-grounded vs chunk-fetch)
- `tools/legalbench_harness.py` extended — `--judge` flag for free-text task scoring
- `tools/extract_cache.py` extended — `scan_classification_markers()` (TS//SECRET//CUI//FOUO/sealing/Rule-6(e))
- `docs/architecture/decisions/0001-0007` — 7 ADRs documenting non-obvious choices
- `docs/ENVIRONMENT.md`, `docs/architecture/TRIAD_ENTRY_POINT.md`
- `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/`, `04_Open_Source_Inventory/`

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | PyMuPDF AGPL blocks commercial use | s.275 | `legal`,`audit` | tools/pdf_lib.py shim over pdfplumber+pypdfium2; 9 consumers swapped; 50/50 PDFs validated | MED | DONE |
| 2 | extract-msg GPL blocks commercial use | NEW | `legal`,`audit`,`extract` | Built tools/msg_extract.py on olefile (BSD); uninstalled extract-msg | MED | DONE |
| 3 | mysql-connector-python/pcodedmp GPL listed but unused | NEW | `legal`,`audit` | grep clean → uninstalled both | LOW | DONE |
| 4 | No LLM-as-judge for span correctness — claims at PDF can't be defended | NEW | `rag`,`llm`,`audit` | judge_span_ollama + judge_span_claude via /api/chat; 2048-token Qwen budget; verdict regex parser | MED | DONE |
| 5 | Single-chunk-fetch artifact drives 47.8% IRRELEVANT in chunk-fetch path | NEW | `rag`,`audit` | Inline-grounding pipeline (NOVEL) — model declares which span; substring-verify; 3.25× lift | HIGH | DONE |
| 6 | No defensible secrets-scan story for diligence | NEW | `audit`,`git`,`legal` | tools/secrets_scan.py; 31,257 blobs / 875 commits clean | MED | DONE |
| 7 | requirements.txt files unpinned, hurts reproducibility | NEW | `audit`,`build` | tools/deps_audit.py --fix; 7 .pinned.txt companions written | LOW | DONE |
| 8 | No environment manifest for reproducibility | NEW | `audit`,`build` | docs/ENVIRONMENT.md (hardware/OS/Python/GPU/Ollama/DBs) | LOW | DONE |
| 9 | Subscription audit missing for IP chain-of-title diligence | NEW | `audit`,`legal` | docs/acquihire/03_IP.../02_Subscriptions/subscription_summary.md | LOW | DONE |
| 10 | No governance audit log; "prove you didn't process X" unanswerable | NEW | `audit`,`daemon`,`legal` | tools/governance_audit.py + 5 wires (extract_cache + router); CLI for stats/query | MED | DONE |
| 11 | Citation precision claim 96% INFERRED, never measured | s.275 | `rag`,`audit` | N=30 batch with diverse modalities (audio/OCR/extracted/master-synth); 100% path precision measured | MED | DONE |
| 12 | Triad entry point undocumented; diligence Q "where does request flow" unanswerable | NEW | `triad`,`audit` | docs/architecture/TRIAD_ENTRY_POINT.md mapping orchestrate() → run_architect → run_executor → run_auditor | LOW | DONE |
| 13 | No classification banner detection in governance gate | NEW | `audit`,`legal`,`daemon` | scan_classification_markers() with TS//SECRET//CUI//FOUO/sealing/Rule-6(e); 15/15 smoke + 0/1484 false-positives after 2 tightening rounds | MED | DONE |
| 14 | Audio WER never measured — multimodal claim unsupported | NEW | `audio`,`audit` | tools/wer_measure.py cross-instance on 26 dups → 0.59% avg | LOW | DONE |
| 15 | OCR character accuracy never measured | NEW | `ocr`,`audit` | tools/ocr_accuracy.py pdfplumber-vs-Tesseract → 24% avg / 0-5% prose | LOW | DONE |
| 16 | LegalBench rule_qa scored 10% but answers correct (string-match issue) | s.275 | `llm`,`audit` | Added `--judge` flag + score_answer_with_judge for free-text tasks; user re-run pending | MED | DONE (wrapper); QUEUED (re-run) |
| 17 | "Why built this way?" diligence Q-set unanswered | NEW | `audit`,`triad` | 7 ADRs in Context/Decision/Alternatives/Consequences format | MED | DONE |
| 18 | Stale __pycache__ caused phantom test failures during build | NEW | `build`,`audit` | rm -rf __pycache__; documented as gotcha in handoff | LOW | DONE |
| 19 | `from tools.X` import fails when script run as `python tools/X.py` (sys.path[0]=tools/) | NEW | `build` | Two-path try/except in citation_scorer | LOW | DONE |
| 20 | Em-dash mojibake between answer text and corpus content | NEW | `extract`,`rag` | Unicode dash normalization in inline_grounding._normalize_for_match | LOW | DONE |
| 21 | Composite hallucination rate at 39.81% (chunk-fetch only) — PDF says <2% | NEW | `rag`,`audit`,`legal` | Honest measurement + named tier-1/2/3 roadmap to <10% in next session, <2% over months | HIGH | DOCUMENTED (roadmap), QUEUED (one-quote-per-claim refactor) |

**Compounding**: 2/21 by tag-overlap, 5/21 with judgment
- Tag-matched: #1 (`legal`,`audit` ↔ s.275 PyMuPDF QUEUED entry), #11 (`rag`,`audit` ↔ s.275 PDF-INFERRED-not-MEASURED entry)
- Judgment-additional: #4 (LLM-as-judge — built on s.275 citation_scorer foundation), #16 (LegalBench judge — built on s.275 legalbench harness foundation), #17 (ADRs — extends s.275 docs/acquihire/ pattern)

**Trend update** (last 10): `0/2 → 2/2 → N/A → 2/3 → 2/6 → 3/7 → 8/8 → 1/8 → 2/21`
*(s.277 has the lowest tag-overlap ratio because most pain points were NEW — 18/21 — reflecting the breadth of the 15-item knockdown across previously-untouched categories: license remediation, secrets, governance audit, environment manifest, subscription audit, classification detection, audio WER, OCR accuracy, ADRs, inline grounding. The system compounded HARD on the 2 items where prior work had laid groundwork — citation_scorer + legalbench_harness extensions both built directly on s.275 foundations.)*

**Pattern detection**: No 3+ occurrences of any single pain pattern this session. The closest is `audit`-tagged items (15/21) — but that's the breadth of acquihire-readiness work, not a recurring pain class.

**Quick-win gate fired** (Step 6):
- Surveyed 21 in-session pain points + 13 historical QUEUED items
- 1 quick win built (~5 min): added 3 inline-grounding trigger rows to `.claude/rules/skill-reminders.md` so future sessions reach for the inline-grounded format by default. Trigger pain (~"footnote-only citations get 47.8% IRRELEVANT in scoring") would have been logged as recurring s.275+s.277 if not auto-applied.
- 2 QUEUED items deferred to next session (do not meet LOW-effort gate):
  - #16 LegalBench `--judge` re-run on rule_qa + citation_prediction (10-15 min runtime, but model choice user-decision-dependent + costs API credits if `--judge claude`)
  - #21 One-quote-per-claim prompt refactor (1-2 hr = MED, not LOW)
