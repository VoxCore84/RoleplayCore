---
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(python:*), Bash(ls:*), Bash(find:*), TaskCreate, TaskUpdate, mcp__docs-rag__*
description: Use when the Excluded/ corpus needs maintenance — re-extract/OCR/transcribe/reindex after bulk file changes, or when /ex-status shows staleness. NEVER auto-invoke from another command; only run when the user explicitly asks for refresh.
---

# /ex-refresh — Incremental Maintenance Cycle

Bring the indexes up to date with the current state of `Excluded/`. Designed to be runnable manually and scriptable for Windows Task Scheduler (nightly).

## Invocation

`/ex-refresh` — full refresh across all of `Excluded/`
`/ex-refresh <folder>` — scoped refresh
`/ex-refresh --audio` — target only audio (for overnight Whisper run)
`/ex-refresh --scheduled` — non-interactive mode, no audio prompts, writes report to `AI_Studio/Reports/scheduled/ex_refresh_<timestamp>.md`

## Workflow

### Phase 1 — Pre-flight (report what will run)

```bash
python3 -c "
from pathlib import Path
ROOT = Path('C:/Users/atayl/Desktop/Excluded')
target = ROOT  # or scoped folder
EXTRACTABLE = {'.pdf','.docx','.doc','.eml','.msg'}
OCR = {'.png','.jpg','.jpeg'}
AUDIO = {'.m4a','.mp3','.wav'}
MBOX = {'.mbox'}

counts = {'extractable':0, 'images':0, 'audio':0, 'mbox':0, 'audio_minutes_est':0}
for p in target.rglob('*'):
    if not p.is_file(): continue
    ext = p.suffix.lower()
    if ext in EXTRACTABLE: counts['extractable'] += 1
    elif ext in OCR: counts['images'] += 1
    elif ext in AUDIO: 
        counts['audio'] += 1
        # Rough estimate: 1MB of m4a ≈ 1 minute
        try: counts['audio_minutes_est'] += p.stat().st_size / 1_000_000
        except: pass
    elif ext in MBOX: counts['mbox'] += 1
for k,v in counts.items(): print(f'  {k}: {v}')
"
```

If `--scheduled` not set, pause and show plan to user before running.

### Phase 2 — Extraction

```bash
python tools/extract_cache.py "<target>"
```

Incremental; skips unchanged files. Report new/changed/cached/deleted.

### Phase 3 — OCR

```bash
python tools/ocr_images.py "<target>" --workers 8
```

Incremental; skips cached images.

### Phase 4 — Audio transcription (conditional)

Audio is the most expensive step (CPU-bound Whisper). Behavior:

- **Default**: Skip if >5 files or >30 minutes total estimated. Print a note: "N audio files, ~M minutes — skipped. Run `/ex-refresh --audio` to transcribe overnight."
- **`--audio` flag**: Run foreground. Acceptable to block a long time.
- **`--scheduled` + small queue**: Run if ≤5 files AND ≤30 minutes. Skip otherwise.

```bash
python tools/audio_transcribe.py "<target>" --model base --language en
```

### Phase 5 — Mbox

```bash
# Only if .mbox present under target
python tools/mbox/index.py "<target>"
```

Resumable via `ingest_progress` table.

### Phase 6 — docs-rag reindex

```
mcp__docs-rag__docs_rag_rebuild(folder="<folder-name-if-scoped>", extract_only=False)
```

Runs in background. Report job path. Do not block on it.

### Phase 7 — Verification

```
mcp__docs-rag__docs_rag_status()
```

Compare chunk count before/after. If shrinking unexpectedly, flag.

### Phase 8 — Report

Write report to either stdout (interactive) or `AI_Studio/Reports/scheduled/ex_refresh_<timestamp>.md` (scheduled).

```
## /ex-refresh — [target] — [timestamp]

### Pre-flight
- Extractable: N
- Images: N
- Audio: N (~M min est)
- Mbox: N

### Extraction
- new: N | changed: N | cached: N | failed: N | deleted: N
- Duration: Xs

### OCR
- new: N | cached: N | failed: N
- Duration: Xs

### Audio
- [Run: new/cached/failed counts]
- OR [Skipped: N files, ~M min, reason]

### Mbox
- [counts from ingest_progress]
- OR [skipped — none present]

### docs-rag
- Chunks before: N
- Chunks after (estimate): N
- Rebuild job: [path or "background, ETA ~Xm"]

### Warnings
- [any stale-flag from Phase 7]

### Next suggested action
- [e.g. "Run /ex-refresh --audio overnight" or "Run /ex-absorb on _Needs Sorted"]
```

## Task Scheduler Integration (NEVER CronCreate)

For nightly runs, use **Windows Task Scheduler**, not Claude Code's `CronCreate`. CronCreate with `recurring=true` has historically fired prompts into idle Claude tabs and frozen sessions.

```powershell
# schedule-task-excluded-refresh.ps1
$action = New-ScheduledTaskAction -Execute "python" -Argument "C:\Users\atayl\VoxCore\tools\rag_build.py --no-legacy" -WorkingDirectory "C:\Users\atayl\VoxCore"
$trigger = New-ScheduledTaskTrigger -Daily -At 3am
Register-ScheduledTask -TaskName "Excluded Refresh Nightly" -Action $action -Trigger $trigger
```

Output lands at `AI_Studio/Reports/scheduled/ex_refresh_<timestamp>.md`, read at session-start via the existing hooks.

Prefer putting the scheduled logic into the **ExcludedDaemon** (always-on process with its own asyncio scheduler) so there's no second scheduling system to maintain.

## Constraints

- **Incremental.** Never full-reindexes; always uses sha256-based skipping.
- **Never modifies source files.**
- **Audio is explicit opt-in** for scheduled runs unless queue is tiny.
- **Safe to run concurrently** with interactive session — `.cache/` writes are isolated per folder-slug.
- **If a step fails, continue** with remaining steps and report failures in the final report. One bad PDF shouldn't block OCR on 100 images.
- **Idempotent.** Running `/ex-refresh` twice in a row on the same state should produce identical output (except for timestamps).
