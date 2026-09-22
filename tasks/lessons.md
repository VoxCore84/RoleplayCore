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

## 2026-05-25 — 7-Zip CLI `-p` (space-separated, interactive) backup failed verification

**Context:** Memory Persistence v1 encrypted backup. A manual 7-Zip CLI run using the space-separated interactive form (`7z a -mhe=on -p <archive> <dir>`) failed verification and left no usable archive (`D:\MemoryBackups` ended up empty). User pivoted to the 7-Zip GUI (AES-256 + encrypt-filenames). `memory_backup.py --backup` uses the *same* space-separated `-p` form and is NOT verified end-to-end in a real TTY. `--self-test` passes only because it uses the attached form `-p{pw}`, not the interactive one.
**Lesson:** 7-Zip CLI `-p` with no attached value is an unreliable way to create a verified encrypted archive; the GUI (or attached `-p"pass"`) is dependable. A passing self-test using a different code path does NOT validate the `--backup` path.
**Rule:** Don't claim `--backup` works for real archives (unverified + suspect form). For real backups use the 7-Zip GUI now; pursue a public-key (age/gpg) flow for v2. Never record an unverified/failed archive as a good backup.

## 2026-05-25 — Placeholder filenames in copy-paste commands get run literally

**Context:** I handed the user `Get-FileHash "D:\MemoryBackups\memory_YYYYMMDD_HHMMSS.7z"` with a literal placeholder; it was run verbatim and failed (no such file).
**Lesson:** Any placeholder token in a copy-paste command will be executed as-is by the user.
**Rule:** In runbook commands, auto-detect the real target (`Get-ChildItem D:\MemoryBackups\memory_*.7z | Sort LastWriteTime | Select -Last 1`) or compute the value. If a placeholder is unavoidable, mark it `<REPLACE_ME>` and say "substitute before running."

## 2026-05-25 — Caching savings claimed without checking prompt size or call shape

**Context:** Recommended prompt-caching `citation_scorer.py`'s judge for "~$21/run." PHASE-2 code-read showed `judge_span_claude` uses raw `urllib` with a single user message (no `system=` block), and `JUDGE_PROMPT` is 169 tokens — below the ~1024-token cache floor. Caching there saves $0. The estimate had been fed a fictional 2000-token rubric.
**Lesson:** Prompt caching only pays when a LARGE (≥~1024 tok Sonnet/Opus, ≥2048 Haiku), STABLE system prefix repeats across many calls. A cost claim is worthless without (a) the real prompt token count and (b) the actual call shape (SDK `system=` vs single user message vs raw HTTP body).
**Rule:** Before claiming any caching saving: read the actual call site, confirm a separable stable system block exists, and measure its tokens against the cache floor. Never feed assumed token counts into a cost estimator.

## 2026-05-25 — Measured: bulk image-triage transcription is unreliable on dense screenshots

**Context:** Validated the Pictures/1 harvest with a 20-image Sonnet-vision fidelity check (`tools/ocr_fidelity_check.py`). Relevance classification was 100% accurate (0/20 misclassified), but verbatim transcription had **6/20 MAJOR errors** on dense technical screenshots — garbled numbers (700W→700μ, INT4→INT9), wrong stat (85 vs 95%), wrong filenames (refactorer.md, reranker.py), dropped sections.
**Lesson:** Cheap vision triage (Haiku) is reliable for *is-this-relevant* classification but NOT for exact values/filenames/configs/stats on dense screenshots. Two-layer trust: structure/relevance = trust; verbatim specifics = verify.
**Rule:** Treat bulk image-OCR output as leads, not facts. Any exact command/config/number/filename from a screenshot digest must be verified against the source image or authoritative docs before it lands in code or a recommendation. Re-extract high-stakes specifics with a stronger vision model.

## 2026-09-22 — Recommended a built-in slash command that this machine's config disables

**Context:** The 2.1.278 update-sweep session told the user "after restart: run /skill-doctor". User ran it and got `Unknown command: /skill-doctor` (session e523922e transcript). The command is real (docs: skills page § "Find unused skills", v2.1.252+) but the binary's embedded note says it is unavailable when the client "does not receive feature settings (Bedrock/Vertex/Foundry, telemetry or non-essential traffic disabled, or a first launch that has not fetched them yet)". `~/.claude/settings.json` line 34 sets `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, which turns off feature-flag fetching on every launch.
**Lesson:** "Exists in the changelog/docs" is not the same as "available in this session." Feature-flag-gated commands (`/skill-doctor` and anything else the docs mark as needing feature-flag fetching) are silently absent under `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`, Bedrock/Vertex/Foundry, or `DISABLE_TELEMETRY`.
**Rule:** Before recommending a Claude Code feature, grep `~/.claude/settings.json` env for `DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_TELEMETRY` / provider vars and check the docs for a "feature-flag fetching" caveat. If gated, say so and give the one-session workaround (temporarily unset the var, restart, run, restore) instead of a bare "run X".

## 2026-09-22 — Docs fetches truncate; the binary is the authority for env-var names

**Context:** A May catch recorded `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` as "misnamed (missing `_CODE_`)". The env-vars docs page truncates on every fetch, so nobody re-read the row. A docs agent claimed the opposite today. `grep -a -o NAME claude.exe | wc -l` settled it in one call: 0 hits for the `_CODE_` spelling, 6 for the plain one. The setting had been a silent no-op for four months.
**Lesson:** For "is this key real / what is it called", a truncated docs fetch is weaker evidence than the installed binary. Zero string hits = the code cannot read it. Positive hits = real, even if undocumented (five "NOT-IN-DOCS → remove" recommendations today were wrong for that reason).
**Rule:** Before removing or renaming any Claude Code env var or settings key, grep the installed `claude.exe` for the exact string and record the count in the ledger. Treat "undocumented" as "unverified", not "dead".

## 2026-09-22 — `json.dump` round-trips wreck git-tracked settings diffs; Python text mode flips line endings

**Context:** Removing two dead permission rules via `json.load`/`json.dump` produced a 21-line diff (inline hook objects expanded). A later `write_text` turned every LF into CRLF (99-line diff for a 7-line insert). Both were reverted from backup and redone as byte-level line edits.
**Lesson:** Formatting churn hides the real change and makes review impossible; Windows Python text mode rewrites newlines unless `newline=""` or bytes are used.
**Rule:** For git-tracked JSON/MD: back up, edit as bytes or exact lines, re-parse to validate, then `diff` against the backup and require the diff to be exactly the intended lines before moving on.

## 2026-09-22 — Git Bash rewrites slash-prefixed args to `claude -p`

**Context:** `claude -p "/context"` from the Bash tool became `C:/Users/atayl/AppData/Local/Programs/Git/context` (MSYS path conversion) and burned a full headless session-start answering a nonsense path.
**Lesson:** Any argument beginning with `/` is a path candidate to MSYS.
**Rule:** Run headless slash commands from the PowerShell tool, or set `MSYS_NO_PATHCONV=1`. The working recipe for a per-turn context baseline is in `claude-code-config-state.md`.

## 2026-09-22 — `skillOverrides` visibility states do not cut context; measure the TOTAL, not a category

**Context:** A triage agent estimated −1.7k tokens/turn from moving 53 skills to `name-only` / `user-invocable-only`. Four headless `/context` captures (26 name-only, 26 on, 53 on, every override on including the 24 `off`) all totalled exactly 60.8k. The "Skills" bucket fell and "System tools" rose by the same amount each time; even the 24 `off` skills changed nothing in the total. The estimate was wrong in kind, not degree.
**Lesson:** The harness still carries hidden skills somewhere in the tool definitions in 2.1.278, and `/context` re-buckets rather than removes them. Category deltas can be pure accounting. The only thing that removed tokens this session was content that stopped being loaded at all (rules files condensed or path-scoped, MEMORY.md shortened, agent files deleted).
**Rule:** Any "saves N tokens" claim must be backed by the `/context` **total** from two captures of the shipped state, not a category line or a chars/4 estimate. Report negative results with the same prominence as wins (measurement-discipline no-cherry-pick).

<!-- Append new entries above this line is NOT required; append chronologically below the last entry. -->
