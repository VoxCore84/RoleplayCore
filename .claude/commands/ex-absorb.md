---
allowed-tools: Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(python:*), Bash(ls:*), Bash(find:*), Bash(cp:*), Bash(mkdir:*), Agent, TaskCreate, TaskUpdate, mcp__docs-rag__*, mcp__arcanum__*, mcp__local-llm__*
description: Use when a new file, folder, email, recording, or attachment arrives that needs to land in the Excluded/ knowledge base. Extracts, OCRs, transcribes, indexes, and proposes memory updates in one pass.
---

# /ex-absorb — One-Shot Ingestion

Take a newly-arrived file or folder and fully absorb it into the knowledge stack: text extraction → OCR → transcription → docs-rag indexing → memory update proposal. One command, one paste, and the corpus knows about it.

## Invocation

`/ex-absorb <path>` — path can be:
- A single file (PDF/DOCX/EML/MSG/PNG/JPG/M4A/MP3/MBOX)
- A folder (ingests every supported file recursively)
- A URL (downloads first, then absorbs) — only if user explicitly says "url"

If no path given, ask the user. Do not guess.

## Workflow

### Phase 0 — Classify

Determine:
1. Is `<path>` a file or folder?
2. What extensions are present? (count per type)
3. Is it already in `Excluded/`? If not, propose a destination folder under `Excluded/_Needs Sorted/` or ask user. Do NOT auto-move into `Case_Reference/` (chain of custody).
4. Estimate work: tiny (<10 extractable) / small (10-100) / medium (100-1000) / large (>1000)

### Phase 1 — Stage (if external)

If the path is outside `Excluded/`, propose copying it into a staging folder. Ask confirmation before copying.

### Phase 2 — Extraction

```bash
python tools/extract_cache.py "<resolved-path>"
```

Report new/changed/cached/failed counts.

### Phase 3 — OCR (if images present)

```bash
python tools/ocr_images.py "<resolved-path>" --workers 8
```

### Phase 4 — Audio transcription (if audio present)

- **If ≤2 audio files, total <10 minutes**: run foreground.
- **If more**: prompt user — "N audio files (~M minutes total). Run in background overnight? [y/N]" — if yes, launch via `run_in_background=true`. Do not block the session.

```bash
python tools/audio_transcribe.py "<resolved-path>" --model base --language en
```

### Phase 5 — Mbox ingest (if .mbox present)

```bash
python tools/mbox/index.py "<resolved-path>"
```

This is incremental — `ingest_progress` table handles resumability.

### Phase 6 — docs-rag indexing

Trigger background re-index via MCP:

```
mcp__docs-rag__docs_rag_rebuild(folder="<folder-name>", extract_only=False)
```

For a single file, run `tools/rag_build.py --single-file <path>` if the flag is available; otherwise rely on the incremental rebuild.

### Phase 7 — SME extraction (the value add)

Read the extracted text of the ingested content. Then:

1. **Summarize** what was absorbed (3-5 sentences): what kind of doc/email/recording, key entities mentioned, date, significance.
2. **Classify** against memory topic map (`~/.claude/projects/C--Users-atayl-VoxCore/memory/MEMORY.md` routing table):
   - Case/legal → case-*.md memory files
   - Angel VA → angel-va.md
   - Finance → finances-overview.md
   - Career → career-package.md, resume-package.md
   - Brand → brand-and-business.md
   - etc.
3. **Propose memory edits** — for each affected memory file, show exact before/after diff. Do NOT apply without user confirmation.
4. **Flag contradictions** — if new content conflicts with existing memory, call it out explicitly.

Use `mcp__local-llm__local_extract` or `local_summarize` for the summary step if the content is long (>2K tokens) — saves context.

### Phase 8 — Action item detection

Scan the ingested content for:
- Dates and deadlines → propose additions to `.claude/deadlines.json` or memory/case-status.md
- Names and contacts → propose additions to memory/case-contacts.md
- Evidence → flag for inclusion in filings (memory/case-filings-tracker.md)
- New legal channels / agencies → memory/case-filings-tracker.md

### Phase 9 — Report

Output:

```
## /ex-absorb — [filename or folder]

### Absorbed
- Path: [resolved path]
- Classification: [type]
- Sizes: X files, Y MB, Z extractable, N images, M audio

### Extraction
- New: N | Changed: N | Cached: N | Failed: N

### Index
- Extracted cache: [bucket name]
- OCR cache: [bucket name] (if applicable)
- Audio cache: [bucket or DEFERRED overnight] (if applicable)
- docs-rag: +N chunks (rebuild running in background, ETA ~Xm)
- mbox_index.db: +N messages (if applicable)

### Summary
[3-5 sentence human summary]

### Classification
[which memory topic(s) this affects]

### Proposed memory edits
1. File: [path]
   Before: [quote]
   After: [proposed]
   Reason: [why]
2. ...

### Action items detected
- [ ] [deadline/contact/evidence/channel] — [detail]

### Contradictions (if any)
[explicit list]

### Confirm?
Reply "apply" to execute memory edits and action-item additions.
```

## Constraints

- **Never modify `Case_Reference/` contents.** Read-only.
- **Never auto-apply memory edits.** Always require user confirmation.
- **Background long jobs** (transcription, RAG rebuild). The session should not block on them.
- **Write incrementally** — if the ingestion takes >30s, emit progress updates rather than silently waiting.
- If the source is an email with attachments, absorb the attachments too (CAS dedup handles duplicates).
- If content is sensitive (SSN, DOB, MRN), flag for `redaction-scanner` agent before propagating to any filing draft.
- **Delegate heavy synthesis to local-llm** (`mcp__local-llm__local_extract`, `local_summarize`) when possible — keeps Claude's context clean.
