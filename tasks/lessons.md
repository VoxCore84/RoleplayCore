# Lessons — Self-Improvement Loop

Append-only log of corrections and hard-won lessons. **Read at session start** (per `.claude/rules/session-start.md`). **Append after ANY user correction or surprising failure** (per `.claude/rules/completion-integrity.md`).

Format per entry: a dated heading, then **Context** (what happened), **Lesson** (the generalizable takeaway), **Rule** (the concrete behavior change to prevent recurrence). Keep entries tight — this file is read every session, so it must stay scannable. Promote a recurring lesson (3+ hits) into a `.claude/rules/*.md` file and leave a pointer here.

This complements the read-only `memory/improvements.md` history and the `memory/automation-ledger.md` compounding score. Those are retrospective; this is the fast in-the-moment correction loop.

---

## 2026-05-25 — Phone-library ingestion: HEIC silently skipped

**Context:** Asked to parse `Pictures/1` (1,090 images). `tools/ingest_images.py` only listed `.jpg/.png/...` in `EXTENSIONS`; 69 iPhone `.HEIC` files would have been silently dropped, and the Claude API rejects HEIC media type anyway.
**Lesson:** iPhone camera output is HEIC; screenshots are PNG; saved/edited images are JPG. A library tool that doesn't transcode HEIC silently loses a chunk of the corpus, and "0 errors" hides it.
**Rule:** Before bulk-ingesting any phone library, confirm the tool's `EXTENSIONS` covers HEIC/HEIF and transcodes to a web-safe format. Report skipped/unsupported counts explicitly — a clean run with N<total processed is a partial run.

## 2026-05-25 — Influencer Claude Code screenshots are frequently wrong

**Context:** Harvested CC "settings" tips from screenshots. `autoUpdaterStatus: "disabled"` is NOT a real key (correct: `DISABLE_AUTOUPDATER=1`); `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` was missing the `_CODE_` infix; `CLAUDE_CODE_MAX_TURNS` could not be confirmed.
**Lesson:** Social-media CC tips mix real, misnamed, outdated, and invented settings. Acting on them blind wastes time or breaks config.
**Rule:** Verify every Claude-Code native-feature claim (settings keys, env vars, frontmatter, commands) against live docs (spawn a `claude-code-guide` agent or check context7) AND against the user's actual settings.json before implementing. Tag each claim REAL / NOT-REAL / UNCERTAIN.

## 2026-05-25 — `deny` overrides `allow`: a naive deny-list breaks workflows

**Context:** Considered adding screenshot-suggested `permissions.deny` of `Bash(rm -rf *)` and `Bash(curl *)`. But `settings.local.json` explicitly *allows* `Bash(curl -s http://127.0.0.1:19484/health)` and `Bash(rm -rf _scratch/...)`. Since deny > ask > allow, those blanket denies would silently break the daemon health-check and scratch-cleanup.
**Lesson:** Permission deny-lists are not free safety; they override existing allows and can break established workflows.
**Rule:** Before adding any `deny` pattern, grep the project + local + global `permissions.allow` for commands the pattern would shadow. Keep denies surgical (e.g., secret-file reads), not blanket.

## 2026-05-25 — Naive section-splitting on `## ` breaks on transcribed content

**Context:** The digest splitter split on any `^## ` line, but transcribed screenshot text contained its own markdown headers → 1,156 phantom sections from 1,090 images.
**Lesson:** When content embeds the same delimiter you split on, naive splitting over-segments.
**Rule:** Split on the most specific boundary available (here `^## (?=IMG_)`, the filename pattern), not a generic markdown header.

## 2026-05-25 — Piped stdout is buffered: background progress is invisible

**Context:** A background `python` run's `[N/1090]` progress never appeared in the output file because Python block-buffers stdout when it's a pipe, and the tool wrote its digest only at the end.
**Lesson:** Tailing a backgrounded process's redirected stdout is an unreliable progress signal.
**Rule:** Judge background-job liveness by process state (PID, elapsed, CPU via `Get-CimInstance`/`Get-Process`), not by tailing a buffered output file. For real-time progress, the tool must flush per-item or write a progress file.

<!-- Append new entries above this line is NOT required; append chronologically below the last entry. -->
