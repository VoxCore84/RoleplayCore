# VoxCore — Current State

**Updated:** 2026-09-22 evening (cc audit v3, session 288b) · earlier the same day (config sweep, 288) · prior snapshot 2026-05-26 · **Branch:** `feature/ai-harvest-quick-wins` · **HEAD (pre-this-commit):** `5addae2ae1`

Navigational snapshot. Authoritative detail: `docs/VOXCORE_SYSTEM_REGISTRY.md`.

## 2026-09-23 — superpowers plugin fork ACTIVE (sessions 289 → 289b)
- **Superpowers 6.4.1-adam.2 is live** as `superpowers@skills-dir` from `~/.claude/skills/superpowers/` (277 files, byte-identical to `~/superpowers-work/fork/`), in every session under `C:\Users\atayl`. Nine precedence lines sit at the end of `C:\Users\atayl\CLAUDE.md`; line 9 was amended in 289b's fix loop (backups `CLAUDE.md.bak_20260923_163824_superpowers`, `_170627_line9`; canonical text `AI_Studio/Reports/superpowers_supercharge/CLAUDE_MD_OVERRIDES.md`).
- **Verified (289b):** 12-row triple-check, 12 checks + 12 skeptics, all tested-pass/upheld; evals 7/7 Windows-runnable cases at 3/3 with the plugin after the line-9 fix (before: 5/7; the one real failure traced to a gate-skip in a kept trace); per-turn context **58.0k → 60.5k (+2.5k)**; rollback proven both directions — **deactivate by moving the folder out of `~/.claude/skills` (renaming does not unload it)**. Report `~/superpowers-work/REPORT.md`; evidence `AI_Studio/Reports/superpowers_activation/`.
- **Windows harness limits:** `claude plugin eval --scaffold` and `context.add_dirs` fail on native 2.1.281; `--keep-temp` dirs cannot be sealed; eval arms do NOT load the global CLAUDE.md or user-scope plugins (runner-verified 2026-09-24, `evals/adam3-inherit-check` + `adam3-isolation-check`; the 09-23 claim is withdrawn in `tasks/lessons.md`) — evals measure plugin prose, headless probes measure override lines.
- **Queued:** Adam's 7-item interactive checklist (REPORT §7); two override edits (VoxCore-primary); adam.3 eval-gated trims via `superpowers-work/tools/activation/eval_run.ps1`; with/without comparison on real tasks. Handoffs: `2026-09-23_session_289_superpowers-fork.md`, `2026-09-23_session_289b_superpowers-activation.md`.

## 2026-09-22 evening — after cc audit v3 (session 288b; commits `acd8ed1f06`, `047fad20cc`)
- **Live per-turn context:** 61.1k → **57.8k** (three headless captures); deferring the last three `.mcp.json` servers would give 52.0k (measured, unshipped, Adam's call).
- **Safety:** daemon v1.3.1 `git-destructive-guard` (force-push, hard reset, `git clean`, whole-tree checkout, recursive delete outside scratch, game-DB import without snapshot; heredoc-aware). Hook suite 2/22/13 passing (was 0 of 17 scenarios). Release-gate archive-verb case bug fixed.
- **Settings:** inert `effortLevel`/`alwaysThinkingEnabled` removed; `modelSettings` fable xhigh + opus-5-5 high; `fastModePerSessionOptIn`; `enableAllProjectMcpServers=false` with allowlists (VoxCore 5, CalmCore 8); `PYTHONUTF8=1`; code-review plugin disabled; `status` → `sys-status`.
- **Standing priority:** power first, efficiency second (`memory/feedback_power_over_efficiency.md`). Built-in Explore stays on inherited Opus 5.5.
- **Handoff:** `AI_Studio/Handoffs/voxcore/2026-09-22_session_288b_cc-audit-v3.md`; report `AI_Studio/Reports/cc_audit_v3_20260922-1804/REPORT.md`; CalmCore half `AI_Studio/Handoffs/calmcore/2026-09-22_cc_audit_v3_calmcore.md` + follow-up prompt.

## 2026-09-22 — Claude Code config state after the optimization sweep (session 288)
- **Live per-turn context:** 75.2k → **60.8k** (headless `/context`, same method both sides). Rules 33.4k → 21.9k (six condensed, long form in `docs/rules-reference/`; protocol-gate path-scoped); MEMORY.md 6.6k → 4.3k.
- **Pins:** Fable 5.1 primary, Sonnet 5 subagents (canary-verified, no credit gate), `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=95` (the `_CODE_` spelling was never read — renamed).
- **Removed from VoxCore:** MCP `mysql` + `wago-db2` (broken), 5 WoW agents (identical in CalmCore), 6 dead `Write()` permission rules, `cpp-build-reminder` hook, `MAX_THINKING_TOKENS`.
- **Agents/skills/rules now:** 23 agents (all with `effort:`) / 59 listed skills + 24 off / 17 rules files (3 path-scoped + protocol-gate). Hook daemon 38 handlers, breadcrumbs → `AI_Studio/Reports/subagent_activity.log`.
- **Measured negative:** `skillOverrides` visibility states save 0 tokens (4 captures). Use them for behaviour only.
- **Kept by decision:** `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` (gates /skill-doctor, Remote Control, auto-updates → `claude update` is manual).
- Evidence: `AI_Studio/Reports/OPTIMIZATION_SWEEP_2026-09-22.md`, `AI_Studio/Reports/sweep_2026-09-22/APPLIED_LEDGER.md`; durable memory `memory/claude-code-config-state.md`.

## Live (production)
- **Retrieval:** hybrid FTS5 + ChromaDB (477 MB) + KG-entity RRF (`tools/excluded_hybrid_search.py`); **92.0% baseline** (run_id `43b4e9ba4752a6fc`).
- **KG:** `.cache/excluded_kg.db` (272 MB, 24,640 entities / 743K relations) — but **co-mention only, no typed edges**.
- **MCP:** 5 servers / 33 tools (voxcore-db, voxcore-server, arcanum, docs-rag, local-llm).
- **Daemons:** hook_daemon v1.3.0 (25 routes; 38 handlers wired as of 2026-09-22); excluded-corpus daemon (PARTIAL, 6 known issues).
- **Agents/skills/rules:** ~~28 / 79 / 16~~ → 23 / 59 listed (+24 off) / 17 files (as of 2026-09-22).

## Dormant (committed/built, not active)
- Cost tools: `tools/model_router.py`, `tools/anthropic_helpers.py` (0 importers); `config/backend_selection.yaml` (inert, untracked).
- Memory Control Plane v0.1 (`tools/memory_*.py`, commit `73c6d4c771`, unwired).
- hook_daemon CC-05 breadcrumb (live on next reload); sql-write-monitor route (unwired).

## Scaffold-only (do NOT build this session)
- `graphrag/PLAN.md`, `contradiction/PLAN.md` — both gated on **typed KG edges** (absent).

## Blocked / entangled (do NOT touch)
- `citation_scorer.py` (+93), `quality_probe.py` (+23), `excluded_hybrid_search.py` (+105) — prior-session uncommitted work; reconcile before any cost/eval edit.

## Privacy
- Image digest (PII) quarantined + gitignored (`_PRIVATE_quarantine/`). No exposure.

→ **Next action:** `NEXT_SESSION.md` and `memory/todo.md`.
