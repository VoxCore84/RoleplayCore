---
allowed-tools: Bash(git:*), Bash(gh:*), Bash(python3:*), Read, Edit, Write, Grep, Glob, Agent
description: End-of-session routine — commit, push, sync bridge, update memory, capture resume evidence, automation retro with compounding score, build quick wins, write session handoff.
---

# Wrap Up Session

## Arguments

- `$ARGUMENTS` — optional override:
  - `quick` → only Steps 1–3 (commit/push/bridge), skip the rest
  - `no push` / `skip push` → no `git push`
  - `no build` → skip Step 6 quick-win build (still log them as QUEUED)
  - free text → used as commit message

## Philosophy

Every session leaves behind two things: (1) the work product, (2) a small automation improvement that makes the NEXT session faster. Wrap-up is where #2 gets captured AND executed. **Build, don't just log.**

Target: ~3 minutes excluding quick-win builds. Soft cap on quick-win build time: 30 minutes total.

---

## Step 1 — Commit and push (~30s)

Run in parallel:
- `git status --porcelain`
- `git log --oneline -5`
- `git diff --stat`
- `git diff --cached --stat`

If no uncommitted changes (no M/A/D in porcelain), skip to Step 2.

Otherwise:
1. **Stage** only modified (M), added (A), and deleted (D) files. Do NOT stage untracked (`??`) unless clearly part of this session's work. Never stage build artifacts, `.env`, credentials, or `* - Copy*` files.
2. **Commit** with message from `$ARGUMENTS` if provided, else write one summarizing the diff. Always include co-author trailer.
3. **Push** `git push origin HEAD` unless user said no push.

## Step 2 — Bridge sync (~3s)

```bash
python /c/Users/atayl/cowork/sync_bridge.py --full 2>&1
```
Fallback: `python /c/Users/atayl/VoxCore/cowork/sync_bridge.py --full 2>&1`. If both fail, note and continue.

## Step 3 — Memory updates (~60s)

Determine session number:
1. Read last entry in `~/.claude/projects/C--Users-atayl-VoxCore/memory/recent-work.md`.
2. If last entry's date == today AND last number was N (or N+letter), this is N+next-letter (a→b→c…). Convention: `270b` = wrapped 270, then kept going.
3. Else this is N+1.
4. Show chosen number to user before writing — easy to override.

Update three files:

**`recent-work.md`** — prepend a new session entry (most recent at top). Format:
```markdown
## [Date] [Year] (session N — [title])
- **[Category]**: [what was done, key outputs, metrics]
- **[Category]**: [what was done, key outputs, metrics]
- Commit: `[hash]`
```

**`todo.md`** —
- Mark completed items: `~~strikethrough~~ DONE (session N)`
- Add new items to HIGH/MEDIUM/LOW
- Replace the entire `## Next Session` section with fresh top-3-to-10 actionable items (never append, always replace — stale next-session items are worse than none)

**Skip** these unless something structural changed: `MEMORY.md`, `session_state.md`, Central Brain. Cowork reads memory files via the bridge (Step 2), so Central Brain is no longer required at every wrap-up. If the user explicitly asks, update Central Brain manually.

## Step 4 — Resume evidence capture (~30s)

**Skip if** session produced no measurable output. Capture only if AT LEAST ONE of:
- A numeric metric (entities/files/% improvement/bugs/lines/latency)
- A new system shipped (skill, tool, hook, script, MCP server, rule file)
- An external artifact produced (filing, gist, release, briefing)

Pure research/discussion/status sessions get no entry. Skip without apology.

Append to `~/.claude/projects/C--Users-atayl-VoxCore/memory/resume-evidence.md`:

```markdown
### Session N — YYYY-MM-DD — [Title]
**Quantifiable**: [numbers]
**Technical**: [stack + named architecture pattern — e.g. "Modular RAG", "GraphRAG", "Reciprocal Rank Fusion", not "search thing"]
**Outcome**: [what it enables]
**STAR bullet**: [Situation/Task → Action → Result, one sentence, civilian-readable, no jargon without context]
**Tags**: `tag1`, `tag2`
```

Numbers matter: "25,000 entities" not "built a knowledge graph". Name the pattern: "Modular RAG" not "search thing". The STAR bullet must be paste-ready into a resume.

## Step 5 — Automation retro (~60s)

Append to `~/.claude/projects/C--Users-atayl-VoxCore/memory/automation-ledger.md`. This replaces the old narrative retro in `improvements.md`.

For each pain point this session, fill the table:

```markdown
### Session N — YYYY-MM-DD — [Title]
**Built**:
- `/skill-name` — what it does
- `tools/script.py` — what it does

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | [description] | NEW or s.N | `tag1`,`tag2` | [what was/should be built] | LOW/MED/HIGH | DONE/QUEUED/DEFERRED |
```

**First seen**: scan `automation-ledger.md` and `improvements.md` (for historical) for the same/similar pain. If found, write `s.N` (the earliest occurrence). If not found, write `NEW`.

**Tags**: pull 1–3 from the controlled vocab. Add new tags ONLY when no existing one fits, and add the new tag to the vocab list at the top of `automation-ledger.md`.

**Compounding score** — compute and write below the table:

```markdown
**Compounding**: X/N by tag-overlap, Y/N with judgment
- Tag-matched: #K (`tag` ↔ s.M)
- Judgment-additional: #L addressed by s.M [explain why]
```

Method:
- **Tag-overlap (X/N, reproducible)**: count pain points whose tag set intersects any DONE entry from prior 5–10 sessions in `automation-ledger.md`.
- **With judgment (Y/N, subjective)**: read the prior 5–10 entries. For pain points NOT counted by tag-overlap, decide if a prior fix actually addresses this pain by class even if tags differ slightly. Add to numerator.

Show both. They diverge informatively.

**Update the trend line** at the top of `automation-ledger.md` — append this session's `X/N` to the "Last 10 sessions" line, drop the oldest if >10.

**Pattern detection / escalation**:
- After writing the entry, scan `automation-ledger.md` + `improvements.md` for any pain whose tags or text recur 3+ times.
- If yes: add to `todo.md` HIGH priority with `[ESCALATED — N occurrences]` tag. Update Status column in current entry to ESCALATED.

## Step 6 — Quick-win gate (0–30 min)

**This step fires BEFORE the session-complete summary.** It's the compounding engine.

For each pain point with Status=QUEUED in this session's automation-ledger entry, check:
1. **Effort = LOW** (< 15 min)
2. **Removes a step that happened 2+ times THIS session** OR **is logged in `improvements.md`/`automation-ledger.md` as recurring** (not hypothetical)
3. **Not already DONE** elsewhere in `automation-ledger.md`

If any pain point meets all three → **build it now**, in priority order (highest impact first).

**Cap**: 30 minutes total quick-win build time per wrap-up. If the cap is hit mid-build:
- Finish the in-flight win
- Move remaining wins to `todo.md` Next Session with `[from quick-win queue]` tag
- Surface the queue to the user

**On failure**: hard-stop, surface the error, do NOT roll back. Tell the user what failed and where so we can debug. The partial work may still be useful.

Skip Step 6 if user passed `no build` in `$ARGUMENTS`.

After building each quick win:
- Update Status in the automation-ledger entry from QUEUED → DONE
- Add a one-line entry to `recent-work.md` under this session
- If a new skill was built, add a trigger row to `~/VoxCore/.claude/rules/skill-reminders.md`

## Step 6.5 — Session handoff doc (~60s)

**Required.** Write a session-end handoff to `AI_Studio/Handoffs/voxcore/<YYYY-MM-DD>_session_<N>_<brief-tag>.md` so the next Claude Code tab can pick up without re-analysis. The Desktop has a `VoxCore Handoffs.lnk` shortcut to this folder — do NOT write the handoff to Desktop root.

Filename format: `2026-05-02_session_277b_evening.md` (date + session number from Step 3 + 1-3-word tag from session focus).

Required sections:

1. **Frontmatter line** — session number, duration, commit hash from Step 1, total API spend.
2. **What happened this session** — brief round-by-round narrative (3-8 sentences per round if multi-round; one paragraph if single-focus).
3. **Headline numbers** — the diligence-grade pitch claim of the session, with confidence tier and evidence file paths. If no measurements were taken, say so explicitly.
4. **State-of-the-world warnings** — anything the next tab needs to know that isn't obvious from `git status` or `recent-work.md`. Examples: uncommitted dirty state with rationale, withdrawn external claims, production-vs-alternative config decisions, recurring API contention, gating actions like "JAG meeting blocks outreach."
5. **What's real (measured numbers)** — current state table for the session's domain. Cross-reference `Desktop/VoxCore_Benchmark_Results.md` if applicable.
6. **Files to read at session start** — exact `Read <path>` commands for the next tab. Include canonical Desktop trackers + active prep files in `Do NOT Delete These/` + this handoff itself + any source files the next priority touches + methodology rule files.
7. **Top 5-10 priorities for next session** — pulled from `todo.md` Next Session block (which was rewritten in Step 3).
8. **Standing directives (unchanged)** — copy the standing-directive block from the prior handoff if one exists, or restate from CLAUDE.md and project rules. Add any new directives this session set.
9. **Workflow reminders for the next tab** — Triad rule reminders, methodology rule reminders, cost discipline notes, recurring-pain prevention pointers.
10. **Provenance footer** — generation timestamp, session totals (items checked, tools shipped, docs written).

Skip Step 6.5 only if:
- The session was a pure documentation read with no measurable output (rare)
- User explicitly passed `quick` in `$ARGUMENTS` (already skipping Steps 4-7)

If skipped: still write a 1-2-line marker entry in `AI_Studio/Handoffs/voxcore/_session_index.md` (create if doesn't exist) noting the session number + skip reason, so the next tab knows nothing is missing.

After writing the handoff, mention its path in the Step 7 summary.

## Step 7 — Session-complete summary (~10s)

Output to user:

```
## Session N Wrap-Up

### Committed
- [hash] message (or "nothing to commit")

### Pushed
- master → origin (or "skipped")

### Bridge
- Synced (or "failed: reason")

### Resume Evidence
[copy the entry just written, or "skipped — no measurable output"]

### Automation Ledger
- Built: [list]
- Pain → Fix: N entries (M DONE / K QUEUED / L DEFERRED)
- Compounding: X/N tag-overlap, Y/N with judgment
- Trend: [last-5 trend line]

### Quick Wins Built
- [skill/tool] — [what it does] (~T min)
[or "none — all pain points already addressed this session"]
[or "queue overflowed cap; deferred N items to todo.md"]

### Handoff
- AI_Studio/Handoffs/voxcore/<filename>.md (or "skipped — quick mode" / "skipped — pure read session")

### Next Session (written to todo.md)
- [ ] item 1
- [ ] item 2
- [ ] item 3
```

If `quick` was passed, output only Committed/Pushed/Bridge.

---

## Rules

- Never force-push
- Never commit `.env`, credentials, or binary files
- Never skip hooks (`--no-verify`)
- If any step fails (other than Step 6 hard-stop), continue with remaining steps and report the failure
- Keep commit messages concise (1–2 lines)
- The `## Next Session` block in `todo.md` must always be fresh — replace it every wrap-up, never append
- Never skip Step 5 (automation retro) — it's the compounding engine. Step 4 (resume evidence) is conditional; Step 5 is not.
- If quick-win gate has nothing to build, say so explicitly (don't silently skip — the user wants to see the gate fired)
- Never skip Step 6.5 (session handoff) unless `quick` was passed or the session was a pure read — the next tab depends on it. Write to `AI_Studio/Handoffs/voxcore/<date>_session_<N>_<tag>.md` (NOT Desktop root — Desktop has the `VoxCore Handoffs.lnk` shortcut to that folder).

## Migration notes (for future Claude reading this skill)

- This skill replaced an 8-step version on 2026-04-28. Old version: gist check, session_state, Central Brain. New version: resume-evidence, automation-ledger, quick-win gate.
- `/retro` was absorbed into Step 5. Do not re-create it.
- `improvements.md` is now read-only history. Append retros to `automation-ledger.md`.
- `/sync-brain` was deliberately not built — Cowork reads memory files via the bridge.
- `/publish-gists` is a separate skill. The user runs it explicitly when they want to update gists.
