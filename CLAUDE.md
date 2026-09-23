# RoleplayCore — Project Guide

## P0 — USE THE TRIAD (do not brute-force)
**You have live API access to ChatGPT (gpt-5.4) and Gemini (gemini-3.1-pro). USE THEM.**

### The Pipeline
```
1. DESIGN  → ChatGPT generates spec    → lands in AI_Studio/1_Inbox/
2. REVIEW  → ChatGPT reviews spec      → approved specs move to AI_Studio/2_Active_Specs/
3. BUILD   → Claude Code implements     → code/SQL/config written
4. REVIEW CYCLE (5-round, 3 reviewers):
   4a. ChatGPT reviews   → architecture/design      → fix issues
   4b. Gemini reviews    → correctness/edge cases   → fix issues
   4c. Claude API reviews → cold-read, impl bias    → fix issues
   4d. ChatGPT reviews   → verify fixes, coherence  → fix issues
   4e. Gemini reviews    → final seal (strictest)
5. USER    → human review of final artifact
```

### When to Call Each
| Trigger | Who | Command |
|---------|-----|---------|
| New feature / subsystem / architecture | ChatGPT | `python tools/api_architect/run_architect.py --prompt "..."` |
| Spec in inbox needs review before implementing | ChatGPT | `python tools/ai_studio/chatgpt_bridge.py --file SPEC.md` |
| Implementation done, non-trivial changes | Gemini | `python tools/ai_studio/orchestrator.py` |
| Unsure about an architecture decision | ChatGPT | Same as row 1 — ask before deciding |

### How Handoffs Work
- **ChatGPT → Claude Code**: Spec `.md` file lands in `AI_Studio/1_Inbox/`. Read it, claim it in Central Brain, implement it
- **Claude Code → Gemini**: After implementation, run orchestrator. It sends your diff + context to Gemini, gets back approval or rejection with specific issues
- **Gemini → Claude Code**: If rejected, fix the cited issues and re-run the audit. If approved, write handoff to `AI_Studio/Reports/Audits/`
- **Coordination**: Update `AI_Studio/0_Central_Brain.md` when starting/finishing work. Update `doc/session_state.md` for multi-tab coordination

### Exceptions (no API call needed)
Localized bug fixes, log parsing, build-loop, file cleanup, simple CLI ops, git operations.

### Self-Check
Before completing any session with non-trivial work, ask: *"Did I use the Triad, or did I brute-force this?"*

## THE TRIAD EVOLUTION DIRECTIVE (Core Philosophy)
At every step, ask: *"What would I do differently if I knew I had nearly unlimited potential to run AIs?"* You have agent swarms, subagents, custom skills, ChatGPT API, Gemini API, Cowork scheduled tasks, and massive parallel compute. Claude Code is the primary terminal — all other AIs are API endpoints. Never accept a standard approach if you can think of a smarter, faster, cheaper, or better way to leverage the swarm.

## What This Is
TrinityCore-based WoW private server targeting **12.x / Midnight** client, specialized for **roleplay**. Custom systems, 5 databases (auth, characters, world, hotfixes, roleplay).

## WoW DB rules
Live in `CalmCore/CLAUDE.md` § CRITICAL RULES (item_template, broadcast_text, creature_template columns) and `.claude/rules/project-reference.md` (path-scoped); VoxCore has been the non-WoW workspace since 2026-04-09.

## Session Start — MANDATORY
See `.claude/rules/session-start.md`. In brief: Read `AI_Studio/0_Central_Brain.md` + `doc/session_state.md` + `todo.md` BEFORE responding. EXTRACT actionable items and show to user. Never silently drop items.

## Proactive Skill Reminders — MANDATORY
See `.claude/rules/skill-reminders.md`. The user should NEVER have to remember a slash command. Key: `/wrap-up` at end of session, `/check-logs` on crash/restart, `/lookup-*` for names without IDs.

## Debugging — MANDATORY PIPELINE
See `.claude/rules/debugging.md`. 4-gate pipeline. No hypothesis without data. Never combine fixes.

## Completion Integrity — MANDATORY
See `.claude/rules/completion-integrity.md`. Never claim completion without tool output proving it.

## Documentation Discipline — MANDATORY (per-checkpoint cadence)
See `.claude/rules/documentation-discipline.md`. Per-checkpoint cadence (achievement record + closeout + update log per phase, before moving on); supersession discipline (Theranos pattern — never retroactively edit audit trail); anti-fabrication verify-before-summarize (call the function that produced the numbers, do not free-recall).

## Operational Discipline — MANDATORY (pre-action gates)
See `.claude/rules/operational-discipline.md`. Pre-mortem checklist before every destructive batch; named filesystem traps (stat on symlinks, truncate, ln -s on Windows); act-vs-pause-vs-ask escalation; budget-tension protocol; no production code changes without Adam GO.

## Session Handoff — MANDATORY (cross-session continuity)
See `.claude/rules/session-handoff.md`. Every multi-phase session arc closes with `SESSION_<date>_FINAL.md`; document state line + update log per phase; next-session priority order with cost + wall-time estimates; architectural debt enqueueing; handoff payload definition.

## Measurement Discipline — MANDATORY (diligence-grade reporting)
See `.claude/rules/measurement-discipline.md`. Calibration choice IS policy (do not soften post-hoc); cost dimension explicit and consistent across Pareto comparisons; tie-break rules declared in advance; A/B reports both regressions and lifts; no-cherry-pick discipline (Phase 5 MRR-vs-pass-rate is the canonical example); withdrawn-claim discipline (Phase 3.75-A 82% → 92.0% formal retirement); conservative-vs-permissive labeling on every calibrated number; sample-size disclosure in the same sentence as the headline.

## Multi-Tab Delegation — BLOCKING OBLIGATION
See `.claude/rules/multi-tab.md`. If task touches 2+ independent subsystems, MUST suggest tab split.

## Compaction Instructions
When compacting, ALWAYS preserve: (1) files modified this session, (2) current task/goal, (3) pending SQL or build actions, (4) spawned agents and findings. Drop: exploration results, failed approaches, verbose tool output.

## Release Gate — MANDATORY for Shipping
Before shipping any addon, tool, or app: run `/pre-ship <path>`. It runs automated checks (naming, non-ASCII, TOC, versions, docs, secrets) then spawns 3 adversarial review agents (noob, bully, security) in parallel. Writes `.claude/release-gate-status.json` which enforcement hooks read — `git push --tags` and `gh release create` are BLOCKED when gate != PASS. Full checklist: `memory/addon-building-checklist.md` (16 phases, ~130 items).

## Reference (loaded on-demand from `.claude/rules/`)
- **Project structure, build, DBs, systems, key files, tools** → `project-reference.md`
- **C++ coding conventions** → `coding-conventions.md`
- **Protocol/binary work gate (dump before implement)** → `protocol-gate.md`
- **Compaction survival (auto-write state to disk)** → `compaction-survival.md`
- **Documentation discipline (per-checkpoint cadence + supersession)** → `documentation-discipline.md`
- **Operational discipline (pre-action gates + filesystem traps)** → `operational-discipline.md`
- **Session handoff (cross-session continuity)** → `session-handoff.md`
- **Measurement discipline (diligence-grade reporting)** → `measurement-discipline.md`
