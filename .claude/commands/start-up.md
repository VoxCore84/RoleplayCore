# /start-up — Session orientation (pair with /wrap-up)

Read-only orientation ritual. Before any project work: establish canonical state, reconcile across tabs/branches, surface blockers, and pick ≤3 next actions. **Do not rediscover the system from scratch, and do not start work until the report is done.**

This is the deep, on-demand companion to the auto-run `.claude/rules/session-start.md`. Run it when picking up a fragmented multi-tab/multi-branch state, or any time you're unsure where things stand.

## Hard rules
- **Read-only by default.** No edits, no `git push`, no branch switch, no feature work until the report is complete AND the user picks an action.
- **Never push the local-only memory repo.** If it has a remote → STOP and flag CRITICAL (it holds HIPAA/legal/financial content).
- If a handoff says **another tab owns the current branch/files**, STOP and report — do not edit.
- If handoffs **disagree**, report the conflict; never silently choose.
- **Discover** blockers from current state — do NOT hardcode a fixed blocker list (it rots).
- Maximum **3** recommended next actions. No BUILD recommendation unless blockers are clean.
- Never print sensitive memory contents or leak sensitive filenames into tracked docs.

## Step 1 — Canonical state (read, in order)
1. `docs/VOXCORE_HANDOFF_INDEX.md` — **canonical entry point.** Its "Latest session" line + the `CURRENT_STATE.md` / `NEXT_SESSION.md` it points to are the spine.
2. `AI_Studio/Handoffs/voxcore/CURRENT_STATE.md` and `NEXT_SESSION.md`.
3. `~/.claude/projects/C--Users-atayl-VoxCore/memory/todo.md` → `## Next Session`.

If `docs/VOXCORE_HANDOFF_INDEX.md` is missing, fall back to the newest `AI_Studio/Handoffs/voxcore/*.md` + `doc/session_state.md`, and say in the report that you used the fallback. Treat `0_Central_Brain.md` and `doc/session_state.md` as possibly stale — HANDOFF_INDEX supersedes them on conflict.

## Step 2 — Review the last 3–5 handoffs
Start with the per-session handoff HANDOFF_INDEX points at, then up to 4 more newest-first in `AI_Studio/Handoffs/voxcore/` (and any temp `AI_Studio/Reports/*HANDOFF*/*INTEGRATION*/*STATUS*` referenced by the canonical docs). For each, extract: date/session · branch+commit · stated next action · blockers · "do not" constraints · files owned by other tabs · canonical-vs-temp-vs-stale. List any strong extras under "Not reviewed (cap)."

## Step 3 — Live repo state (read-only)
```
git status -sb
git branch --show-current
git log --oneline -8
git rev-list --left-right --count origin/master...HEAD   # behind / ahead
```
Report: branch · ahead/behind origin · dirty files · unpushed commits · and whether any dirty file is claimed by another tab in the handoffs (entanglement risk). Do NOT edit.

## Step 4 — Memory repo safety (read-only)
```
git -C "$USERPROFILE/.claude/projects/C--Users-atayl-VoxCore/memory" status -sb
git -C "$USERPROFILE/.claude/projects/C--Users-atayl-VoxCore/memory" log --oneline -3
git -C "$USERPROFILE/.claude/projects/C--Users-atayl-VoxCore/memory" remote -v
```
**If any remote exists → STOP, flag CRITICAL, never push.** Run `python tools/memory_staleness.py` if present (read-only; do not auto-fix). Do not mutate memory files.

## Step 5 — Slipped-through-cracks (discover from Steps 1–4 + NEXT_SESSION)
Scan for, and LABEL each finding:
- temp Reports handoffs that should be promoted to canonical `docs/VOXCORE_*` → **DOCS**
- canonical docs that exist only on an unmerged branch → **COORDINATION**
- unpushed commits / dirty files owned by another tab → **COORDINATION**
- handoffs disagreeing on next work → **COORDINATION**
- acknowledged-but-unresolved blockers, entangled uncommitted files → **BLOCKER**
- pre-push leak risk, memory-repo remote, sensitive content near a commit → **SAFETY**
- known deferrals (e.g., things gated on a prerequisite) → **BACKLOG**

Pull the actual items from the current handoffs/NEXT_SESSION/git — do not assume last week's list.

## Step 6 — Report (exact shape)
```
# /start-up report
## Canonical entry point — found / used / fallback
## Last handoffs reviewed (3–5) — path · canonical/temp/stale · one-line purpose
## Repo state — branch · ahead/behind origin · dirty · unpushed · ownership risk
## Memory repo — status · latest commit · remote (must be none) · staleness
## Handoffs agree on — ≤7 bullets
## Conflicts / uncertainty — ≤7 bullets (or "none found")
## Slipped-through-cracks — ≤10 bullets, each labeled BLOCKER/COORDINATION/DOCS/SAFETY/BACKLOG
## Recommended next actions — MAX 3, each one of CONSOLIDATE/UNBLOCK/PUSH/DOCUMENT/BUILD/DEFER
## Do not do yet — explicit no-go list from the handoffs
```

## Step 7 — Stop
Stop after the report. Do not begin the recommended work until the user explicitly says to proceed.
