# VoxCore Dormant Systems Register

**Date:** 2026-05-26
**Source reports:** `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md`,
`AI_Studio/Reports/system_inventory_2026-05-26/cat_D_agents_rules.md`,
`AI_Studio/Reports/pictures1_ingest/HOOKS_PROMOTION_REPORT.md`
**Scope:** All systems committed or partially committed to VoxCore but not active in production as of this date.
**Rule:** Do NOT activate anything in this register without an explicit Adam GO. No code edits this document.

---

## Summary table

| ID | System | Path | Dormancy type |
|----|--------|------|---------------|
| D-01 | Model router | `tools/model_router.py` | Committed, 0 importers |
| D-02 | Anthropic cost helpers | `tools/anthropic_helpers.py` | Committed, 0 importers |
| D-03 | Backend decision matrix | `config/backend_selection.yaml` | Untracked, unread by prod |
| D-04 | Memory Control Plane v0.1 | `tools/memory_schema.py`, `memory_context.py`, `memory_fix_proposals.py`, `agent_task_ledger.py` | Committed on unmerged branch, unwired |
| D-05 | CC-05 SubagentStop breadcrumb | `hook_daemon.py:_subagent_complete_work` | Code present, activates on next daemon reload |
| D-06 | sql-write-monitor hook route | `hook_daemon.py` route + `ROUTE_TABLE` entry | Route present, NOT wired in `settings.json` |
| D-07 | GraphRAG scaffold | `graphrag/PLAN.md` | Plan only, zero production code |
| D-08 | Contradiction scaffold | `contradiction/PLAN.md` | Plan only, blocked on typed KG edges |
| D-09 | Three untracked rule files | `.claude/rules/documentation-discipline.md`, `measurement-discipline.md`, `session-handoff.md` | Loaded into CLAUDE.md context, not version-controlled |
| D-10 | dormant-project-watchdog agent | `.claude/agents/dormant-project-watchdog/CLAUDE.md` | No skill or hook references it |
| D-11 | HyDE retrieval | `retrieval/hyde.py` | Killed by design (−10 pp measured regression) |

---

## D-01 — Model router (`tools/model_router.py`)

**Why dormant:** Committed at `0018077959`. `select_backend()` works and `--print` resolves all 16 operations from `backend_selection.yaml`. Zero production importers — no tool in `tools/`, `tools-dev/`, or any skill calls it. Routing defaults it would enforce already match current hardcoded values, so adoption is centralization/control, not a cost delta today.

**What activates it:** Any call site that replaces a hardcoded model string with `from tools.model_router import select_backend; be = select_backend("operation")`. The lowest-risk first site is a new `tools/batch_eval.py` (see `docs/VOXCORE_COST_OPTIMIZATION_STATUS.md`).

**Risk of activation:** LOW. Additive only. `--print` dry-run previews all routing decisions before any live call. `--assume-local-down` previews cloud-fallback behavior.

**Minimum safe activation test:**
1. `python tools/model_router.py --print` — confirm all 16 operations resolve without error.
2. `python tools/model_router.py --assume-local-down --print` — confirm cloud fallbacks are sane.
3. In a new, non-entangled file: `from tools.model_router import select_backend; print(select_backend("judge_citation"))` — verify dict returned with `model` key.
4. Do NOT wire into `citation_scorer.py` or `quality_probe.py` until entanglement is resolved (see D-02 note and `VOXCORE_COST_OPTIMIZATION_STATUS.md`).

**Rollback path:** Remove the import. Router is opt-in; removing it reverts the call site to its prior hardcoded model string. No daemon restart, no DB change.

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/COST_BANKING_READINESS.md` §1, `AI_Studio/Reports/pictures1_ingest/COST_NOTES.md` Lever 3.

---

## D-02 — Anthropic cost helpers (`tools/anthropic_helpers.py`)

**Why dormant:** Committed. Self-test passes: `cached_system()` (prompt-cache block builder), `estimate_cache_savings()` (cost math), `build_batch()` / `submit_batch(dry_run=True)` (Batch API, dry-run by default). Zero importers. The marquee use case (caching the judge prompt) was verified as $0-fit: `JUDGE_PROMPT` is 169 tokens, below the ~1024-token prompt-cache minimum. No current VoxCore call site has a system prefix that meets the cache floor.

**What activates it:** A future call site whose stable system prefix exceeds ~1024 tokens, OR wiring `submit_batch()` into a new `tools/batch_eval.py` for the Batch API lever (~50% cost reduction on eval sweeps). The `submit_batch(dry_run=True)` default saves a JSON plan without spending — safe to invoke.

**Risk of activation:** LOW for `submit_batch(dry_run=True)`. MEDIUM for `cached_system()` — only useful when the target call site truly has a ≥1024-token stable prefix; applying it blindly to smaller prompts is a no-op that adds latency from unnecessary cache header overhead.

**Minimum safe activation test:**
1. `python tools/anthropic_helpers.py` — confirm self-test PASS output.
2. In a new non-entangled file: `from tools.anthropic_helpers import submit_batch; submit_batch([{"custom_id": "test", "params": {}}], dry_run=True)` — confirm JSON written, no API call made.
3. Before enabling caching anywhere: verify the target system prompt token count is ≥1024 (use `estimate_cache_savings()` with real token count as input).

**Rollback path:** Remove the import. `submit_batch(dry_run=True)` writes a local JSON file — delete it. No daemon restart, no DB change.

**Related report:** `AI_Studio/Reports/pictures1_ingest/COST_BANKED.md`, `AI_Studio/Reports/pictures1_ingest/COST_NOTES.md` Lever 1 (withdrawn) + Lever 2.

---

## D-03 — Backend decision matrix (`config/backend_selection.yaml`)

**Why dormant:** 390-line routing decision matrix. UNTRACKED (not committed to git). The committed `tools/model_router.py` depends on it via `select_backend()`, meaning model_router is broken on a fresh checkout without this file. Unread by any production code (model_router itself has zero importers).

**What activates it:** Committing the file (`git add config/backend_selection.yaml && git commit`) repairs the fresh-checkout break. Full activation follows D-01's adoption path.

**Risk of activation:** LOW for committing only. The file contains routing policy (model names, local-required flags) but no credentials or personal paths — safe to version-control per operational-discipline repo-exclusion criteria (verify with a grep for `Excluded/` paths before committing).

**Minimum safe activation test:**
1. `git add config/backend_selection.yaml` — then `git diff --cached config/backend_selection.yaml | grep -i excluded` — confirm no personal paths surface.
2. After commit: `python tools/model_router.py --print` — confirm no KeyError or missing-file error.

**Rollback path:** `git revert` the commit. model_router falls back to its prior broken-on-fresh-checkout state (no production impact since model_router has zero importers).

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` E3.

---

## D-04 — Memory Control Plane v0.1

**Files:** `tools/memory_schema.py` (132 lines), `tools/memory_context.py` (125 lines), `tools/agent_task_ledger.py` (127 lines), `tools/memory_fix_proposals.py` (110 lines).

**Why dormant:** Committed at `73c6d4c771` on branch `feature/ai-harvest-quick-wins` — NOT merged to master. No references in `.claude/commands/`, `.claude/hooks/`, `.claude/rules/`, or any skill file. No hook_daemon route calls any of the four tools. The design document (`AI_Studio/Reports/MEMORY_CONTROL_PLANE_V0_1.md`) is gitignored. Tools are runnable (`--help` confirmed) but nothing invokes them automatically.

**What activates it:**
1. Merge `feature/ai-harvest-quick-wins` to master (after smoke test).
2. Optional wiring paths (all additive, propose-only):
   - Add `memory-context` lookup to session-start (dynamic memory routing instead of the static table).
   - Add `memory_fix_proposals.py --dry-run` as a second pass in `/memory-audit` skill.

**Risk of activation:** LOW. All four tools are read-only proposers. `memory_fix_proposals.py` explicitly never auto-applies changes. Worst case: `--help` works but nothing is wired = current state.

**Minimum safe activation test:**
1. `python tools/memory_schema.py --dry-run` on any memory file — confirm no writes occur.
2. `python tools/memory_fix_proposals.py --dry-run` — confirm proposals-only output, no file mutations.
3. `python tools/memory_context.py "case filing"` — confirm ranked memory list returned.
4. `python tools/agent_task_ledger.py list` — confirm no crash.

**Rollback path:** Remove any added wiring from session-start.md or skill files. The tools themselves are inert without callers; deleting them removes the capability entirely.

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/cat_D_agents_rules.md` §6.

---

## D-05 — CC-05 SubagentStop breadcrumb (`hook_daemon.py:_subagent_complete_work`)

**Why dormant:** Code added in commit `5e93222f62`, added to `_subagent_complete_work` inside `hook_daemon.py`. The running daemon (pid 34224, ~21h uptime as of 2026-05-25) predates the commit — it does not have the new code loaded. The route `/hook/subagent-complete` is already wired in `settings.json` (SubagentStop event), so NO settings change is required. The breadcrumb activates on the next natural daemon reload.

**What activates it:** Natural daemon reload on the next `SessionStart` (via `daemon_shim.py`) or deliberate restart when no tab has in-flight hooks. No code edit, no settings change needed.

**Risk of activation:** LOW. The breadcrumb is additive and exception-wrapped. Worst case: `data.result` field is absent from the SubagentStop payload (payload schema UNKNOWN — could not be confirmed from session data); the handler has defensive `.get()` fallbacks and a `try/except` that logs the exception rather than raising — it cannot break tool calls.

**UNKNOWN:** Exact SubagentStop payload schema. After first real fire (non-isotest), verify that a non-`isotest` SubagentStop line appears in `session_state_live.md` and that `data.result` is populated (vs the `(no result field in payload)` fallback).

**Minimum safe activation test (isolation, already completed 2026-05-25):**
1. Import `hook_daemon` module (safe — server bind is under `__name__` guard).
2. Call `_subagent_complete_work` with simulated payload.
3. Confirm append to `session_state_live.md`.
4. After first real reload: `grep SubagentStop AI_Studio/Reports/session_state_live.md` — confirm non-isotest entry.

**Rollback path:** Delete the `# CC-05:` try/except block in `_subagent_complete_work`. Additive-only removal, no state corrupted. Daemon reload required to take effect.

**Related report:** `AI_Studio/Reports/pictures1_ingest/HOOKS_PROMOTION_REPORT.md` §CC-05.

---

## D-06 — sql-write-monitor hook route

**Why dormant:** Route `/hook/sql-write-monitor` present in `hook_daemon.py` ROUTE_TABLE (verified). Handler `handle_sql_write_monitor` isolation-tested (writes reminder to `session_state_live.md`, returns `{}`). NOT wired in `.claude/settings.json` — `grep "sql-write-monitor" .claude/settings.json` count = 0. Log-only when promoted (PostToolUse cannot block writes; it runs after).

**What activates it:** Three-step promotion after observing a clean daemon reload:
1. Confirm route answers: `curl -s -X POST http://127.0.0.1:19484/hook/sql-write-monitor -d "{}"` returns `{}` (not 404).
2. Add matcher block to `.claude/settings.json` → `hooks.PostToolUse`:
   ```json
   { "matcher": "Write|Edit",
     "hooks": [{ "type": "http", "url": "http://127.0.0.1:19484/hook/sql-write-monitor", "timeout": 2 }] }
   ```
3. Write a `.sql` file; confirm reminder lands in `AI_Studio/Reports/session_state_live.md`.
4. Run `/sync-infra` — CalmCore must stay in parity (4 symlinks point CalmCore hooks at VoxCore daemon code).

**Risk of activation:** LOW-MEDIUM. The route itself is log-only (cannot block). Risk is the daemon restart required to load the route — the daemon serves all tabs + CalmCore (4 symlinks). Restart mid-session with in-flight hooks drops those hooks. Safest window: when no other tab is active and `in_flight=0` (check via `curl http://127.0.0.1:19484/health`).

**Minimum safe activation test:** Steps 1–3 above, in order.

**Rollback path:** Remove the settings.json matcher block (instant deactivate — no daemon restart needed). Optionally remove handler + route entry from `hook_daemon.py` and reload daemon.

**Related report:** `AI_Studio/Reports/pictures1_ingest/HOOKS_PROMOTION_REPORT.md` §.sql-write-monitor.

---

## D-07 — GraphRAG scaffold (`graphrag/PLAN.md`)

**Why dormant:** `graphrag/PLAN.md` is a planning document only. Zero production code exists in `graphrag/`. Verified: agent search found no `.py` files under `graphrag/`. The upstream prerequisite — typed KG edges — does not exist: all 743,207 relations in `.cache/excluded_kg.db` are `predicate='mentioned_with'` (co-mention only). GraphRAG requires typed directed edges (e.g., `employed_by`, `filed_against`) to provide value above the existing hybrid RRF pipeline.

**What activates it:** First implement typed edges in `tools/excluded_daemon/kg/build.py` (currently at line 411: single-predicate co-mention logic). GraphRAG design work follows. This is a multi-session research arc, not a quick wire.

**Risk of activation:** N/A — no code to activate. Risk is in the prerequisite typed-edge work: modifying `kg/build.py` changes the KG ingestion pipeline; requires a full re-index of the corpus (~272 MB DB). The existing 92.0% hybrid baseline (`run_id 43b4e9ba4752_20260504`) must be re-measured post-index rebuild to confirm no regression.

**Minimum safe activation test:** N/A until code exists.

**Rollback path:** N/A. `graphrag/PLAN.md` can be deleted or left as-is with no production effect.

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` A6, A7.

---

## D-08 — Contradiction scaffold (`contradiction/PLAN.md`)

**Why dormant:** `contradiction/PLAN.md` is a planning document only. Zero production code exists. Blocked on the same prerequisite as GraphRAG (D-07): typed KG edges. Without typed edges, contradiction detection cannot distinguish "X filed against Y" from "X mentioned near Y." The `contradiction-finder` agent (`.claude/agents/contradiction-finder/CLAUDE.md`) provides partial coverage today via document-level pattern matching, independent of this scaffold.

**What activates it:** Same prerequisite as D-07 (typed KG edges). Contradiction detection code implementation follows.

**Risk of activation:** N/A — no code to activate.

**Minimum safe activation test:** N/A until code exists.

**Rollback path:** N/A. `contradiction/PLAN.md` can be left as-is.

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` A7.

---

## D-09 — Three untracked rule files

**Files:**
- `.claude/rules/documentation-discipline.md`
- `.claude/rules/measurement-discipline.md`
- `.claude/rules/session-handoff.md`

**Why dormant (as version-controlled artifacts):** All three are loaded into the CLAUDE.md system context on every session — they are LIVE in terms of behavioral effect. However, `git status` shows all three as `??` (untracked). A fresh checkout or `git clean -f .claude/rules/` would silently delete them, breaking session behavior without any warning in git history.

**What activates it (version control):** `git add .claude/rules/documentation-discipline.md .claude/rules/measurement-discipline.md .claude/rules/session-handoff.md && git commit -m "track three live rule files"`. Low-risk, no behavioral change — files already in effect.

**Risk of activation:** LOW. No code or config changes. The commit makes existing behavior version-controlled. After committing, `git status` will no longer show them as `??`.

**Minimum safe activation test:**
1. `git add` the three files.
2. `git diff --cached` — confirm only these three files, no surprise inclusions.
3. `git commit`.
4. `git log --oneline -1` — confirm commit landed.

**Rollback path:** `git revert` the commit or `git rm --cached` the three files. Behavioral effect of the rules is unchanged (CLAUDE.md still loads them from disk).

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/cat_D_agents_rules.md` §3.

---

## D-10 — dormant-project-watchdog agent

**Path:** `.claude/agents/dormant-project-watchdog/CLAUDE.md`

**Why dormant:** The agent is committed and runnable, but no skill file in `.claude/commands/` references or spawns it. No hook_daemon route calls it. No session-start rule mentions it. It was designed to scan `memory/` for stalled/idle projects and surface them, but was never wired into the daily workflow.

**What activates it:** Add a reference in `/memory-audit` skill or in the session-start rule to spawn `dormant-project-watchdog` during the memory staleness pass. Alternatively, wire it as an optional step in `/wrap-up`.

**Risk of activation:** LOW. Agent is Haiku-class, read-only by design (scans memory files, does not write). Activating it adds one agent call to memory-audit or wrap-up flows.

**Minimum safe activation test:**
1. Manually invoke: `Agent: run dormant-project-watchdog` with the memory/ path as context.
2. Confirm output lists stalled projects without modifying any file.

**Rollback path:** Remove the reference from whatever skill or rule was updated. Agent file itself can remain.

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/cat_D_agents_rules.md` §1.

---

## D-11 — HyDE retrieval (`retrieval/hyde.py`)

**Why dormant:** DORMANT BY DESIGN. HyDE (Hypothetical Document Embeddings) was measured at −10 percentage points regression against the 92.0% hybrid baseline in Phase 4 (A/B: Run A HyDE-off vs Run B HyDE-on, identical gold set + snapshot). Decision recorded at `retrieval/HYDE_DECISION.md`. Implementation kept in tree for reference; production retrieval path does not use it. The Phase 4 HyDE refactor that added `hybrid_hyde_query()` to `tools/quality_probe.py` (+23 uncommitted lines) is the entangled prior-session work blocking clean cost-tool adoption.

**What activates it:** NOTHING — do not activate. Decision is final unless a new measurement on the same gold set shows a reversal (requires identical test conditions per measurement-discipline).

**Risk of activation:** HIGH (retrieval regression). Re-enabling HyDE degrades the eval baseline by 10 pp.

**Minimum safe activation test:** N/A — not a candidate for re-activation.

**Rollback path:** N/A — already dormant.

**Related report:** `AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` A8, `COST_BANKING_READINESS.md` §3 (entanglement note).

---

## Activation priority order (suggested)

| Priority | ID | System | Effort | Risk | Gate |
|----------|----|--------|--------|------|------|
| 1 | D-09 | Commit 3 untracked rules | 2 min | LOW | None — just commit |
| 2 | D-05 | CC-05 breadcrumb | 0 min active | LOW | Activates on next natural reload |
| 3 | D-03 | Commit backend_selection.yaml | 5 min | LOW | Grep for personal paths first |
| 4 | D-06 | sql-write-monitor wiring | 15 min | LOW-MED | Quiet daemon window + `/sync-infra` |
| 5 | D-04 | Memory Control Plane v0.1 | 30 min | LOW | Merge branch + smoke test |
| 6 | D-01/D-02 | Model router + helpers adoption | 1 session | LOW | Entanglement resolved first (D-03 + reconcile E4/E5) |
| — | D-07/D-08 | GraphRAG + Contradiction | Multi-session | MED | Typed KG edges prerequisite |
| — | D-10 | dormant-project-watchdog | 10 min | LOW | Optional quality-of-life |
| — | D-11 | HyDE | DO NOT | HIGH | Decision final |
