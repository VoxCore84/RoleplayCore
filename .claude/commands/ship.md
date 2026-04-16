---
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(grep:*), Bash(find:*), Bash(python3:*), Bash(git:*), Bash(sed:*), Agent, mcp__mysql__*
description: Ship loop — run pre-ship audit, fix blockers, re-audit until gate passes
paths: tools/publishable/**
---

# Ship

Iterative ship loop: audit, fix, re-audit until the release gate passes. Wraps `/pre-ship` and `/release-gate-fix`.

## Arguments

`$ARGUMENTS` — path to the project directory (e.g., `tools/publishable/VoxGM`)

## Pipeline

### Phase 1: Initial Audit

Run the full `/pre-ship` audit on the project path:
1. Follow all instructions in `.claude/commands/pre-ship.md`
2. This runs automated checks + spawns 3 adversarial review agents (noob, bully, security)
3. Results written to `.claude/release-gate-status.json`

### Phase 2: Check Gate Status

Read `.claude/release-gate-status.json`. If gate status is `PASS`:
- Report "Release gate PASS — ready to ship" and stop
- Suggest: `git tag v<version>` and `gh release create`

If gate status is `FAIL`:
- Count blocking items
- Proceed to Phase 3

### Phase 3: Fix Blockers

Run `/release-gate-fix` on the same project path:
1. Follow all instructions in `.claude/commands/release-gate-fix.md`
2. This surgically fixes only BLOCKING items, not warnings
3. Report what was fixed

### Phase 4: Re-Audit

Run `/pre-ship` again on the same path. This is a full re-audit, not a partial check.
- If PASS → report success, suggest tag + release
- If FAIL → report remaining blockers. Ask user: "N blockers remain after fix attempt. Want me to try another round, or review manually?"

### Rules

- **Maximum 3 audit-fix cycles.** If still failing after 3 rounds, stop and present the remaining issues for manual review. Infinite loops are worse than manual fixes.
- **Never skip the re-audit.** A fix might introduce new issues.
- **Never auto-tag or auto-release.** Always stop and let the user decide.
