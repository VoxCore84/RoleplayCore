---
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(python:*), Bash(ls:*), Bash(find:*), Bash(wc:*), Bash(du:*), mcp__docs-rag__*, mcp__arcanum__*
description: Use when you want to know what's stale, what's missing, or what needs re-indexing in the Excluded/ corpus before running a query, absorb, or filing draft. Shows per-folder freshness, extraction gaps, OCR/audio/RAG coverage.
---

# /ex-status — Excluded Corpus Health Dashboard

Display the operational health of `C:\Users\atayl\Desktop\Excluded\` — what's extracted, what's indexed, what's stale, what's missing. This is the "situation report" for the most important corpus in the workspace.

## Invocation

`/ex-status` — full dashboard
`/ex-status <folder>` — focused on a specific subfolder (e.g. `Monday_HAF_Call_13Apr2026`)

## Data Sources

1. **Filesystem inventory** of `C:/Users/atayl/Desktop/Excluded/` — count files per subfolder by extension class (pdf/docx/eml/msg/txt/md/png/jpg/m4a/mp3/mbox)
2. **Extraction cache** at `C:/Users/atayl/VoxCore/.cache/extracted/` — bucket names embed the folder slug + root hash
3. **OCR cache** at `C:/Users/atayl/VoxCore/.cache/ocr/`
4. **Audio cache** at `C:/Users/atayl/VoxCore/.cache/audio/` (may not exist)
5. **docs-rag ChromaDB** via `mcp__docs-rag__docs_rag_status()` — collection size, per-folder stats
6. **mbox index** at `C:/Users/atayl/Desktop/Excluded/mbox/mbox_index.db` — size, last-modified, message count via `mcp__arcanum__arcanum_mbox_search(query="", max_results=1)` to confirm liveness
7. **Memory sync** — mtime of `~/.claude/projects/C--Users-atayl-VoxCore/memory/case-status.md` vs mtime of newest file in `Excluded/IMPORTANT DOCS/Case_Reference/`

## Execution

### Step 1 — Inventory script

```bash
python3 -c "
import os, json, datetime
from pathlib import Path

ROOT = Path('C:/Users/atayl/Desktop/Excluded')
CACHE_EXTRACT = Path('C:/Users/atayl/VoxCore/.cache/extracted')
CACHE_OCR = Path('C:/Users/atayl/VoxCore/.cache/ocr')

EXTRACTABLE = {'.pdf','.docx','.doc','.eml','.msg','.txt','.md'}
OCR_EXTS = {'.png','.jpg','.jpeg'}
AUDIO_EXTS = {'.m4a','.mp3','.wav'}

def scan(folder):
    stats = {'files':0,'size':0,'extractable':0,'ocr':0,'audio':0,'mbox':0,'newest':None}
    if not folder.exists(): return stats
    for p in folder.rglob('*'):
        if not p.is_file(): continue
        stats['files'] += 1
        try: stats['size'] += p.stat().st_size
        except: pass
        ext = p.suffix.lower()
        if ext in EXTRACTABLE: stats['extractable'] += 1
        elif ext in OCR_EXTS: stats['ocr'] += 1
        elif ext in AUDIO_EXTS: stats['audio'] += 1
        elif ext == '.mbox': stats['mbox'] += 1
        try:
            mt = p.stat().st_mtime
            if stats['newest'] is None or mt > stats['newest']: stats['newest'] = mt
        except: pass
    return stats

def human(n):
    for u in ['B','KB','MB','GB']:
        if n < 1024: return f'{n:.1f}{u}'
        n /= 1024
    return f'{n:.1f}TB'

now = datetime.datetime.now().timestamp()
print('Folder | Files | Size | Extractable | Images | Audio | Mbox | Newest | Age')
print('---|---|---|---|---|---|---|---|---')
for sub in sorted(ROOT.iterdir()):
    if not sub.is_dir(): continue
    s = scan(sub)
    if s['files'] == 0: continue
    newest = datetime.datetime.fromtimestamp(s['newest']).strftime('%Y-%m-%d') if s['newest'] else '-'
    age = f'{int((now - s[\"newest\"])/86400)}d' if s['newest'] else '-'
    print(f'{sub.name} | {s[\"files\"]} | {human(s[\"size\"])} | {s[\"extractable\"]} | {s[\"ocr\"]} | {s[\"audio\"]} | {s[\"mbox\"]} | {newest} | {age}')
print()
print('Extraction cache buckets:')
if CACHE_EXTRACT.exists():
    for b in sorted(CACHE_EXTRACT.iterdir()):
        if b.is_dir():
            c = sum(1 for _ in b.rglob('*.txt'))
            print(f'  {b.name}: {c} extracted files')
print()
print('OCR cache buckets:')
if CACHE_OCR.exists():
    for b in sorted(CACHE_OCR.iterdir()):
        if b.is_dir():
            c = sum(1 for _ in b.rglob('*.txt'))
            print(f'  {b.name}: {c} OCR files')
"
```

### Step 2 — Query docs-rag and mbox MCPs

```
mcp__docs-rag__docs_rag_status()
mcp__arcanum__arcanum_mbox_search(query="", max_results=1)
```

The mbox call just confirms the index is live and returns a message count hint.

### Step 3 — Memory sync check

```bash
python3 -c "
import os, datetime
from pathlib import Path

MEMORY = Path.home() / '.claude/projects/C--Users-atayl-VoxCore/memory'
CASE_REF = Path('C:/Users/atayl/Desktop/Excluded/IMPORTANT DOCS/Case_Reference')

mem_mtime = max((f.stat().st_mtime for f in MEMORY.rglob('*.md') if f.is_file()), default=0)
case_mtime = max((f.stat().st_mtime for f in CASE_REF.rglob('*') if f.is_file()), default=0)
if mem_mtime and case_mtime:
    lag = (case_mtime - mem_mtime) / 86400
    mem_age = (datetime.datetime.now().timestamp() - mem_mtime) / 86400
    print(f'Memory newest: {datetime.datetime.fromtimestamp(mem_mtime).strftime(\"%Y-%m-%d %H:%M\")} ({mem_age:.1f}d ago)')
    print(f'Case_Reference newest: {datetime.datetime.fromtimestamp(case_mtime).strftime(\"%Y-%m-%d %H:%M\")}')
    print(f'Drift: memory is {lag:.1f} days behind the archive' if lag > 0 else f'Memory leads archive by {-lag:.1f} days')
"
```

## Output Format

```
## /ex-status — Excluded Corpus Health — [today]

### Top-level inventory
| Folder | Files | Size | Extractable | Images | Audio | Mbox | Newest | Age |
|--------|-------|------|-------------|--------|-------|------|--------|-----|
| ... | | | | | | | | |

### Index coverage
- **docs-rag ChromaDB**: N chunks (vs. 25,820 at session-256 baseline) — growing/stable/shrinking
- **mbox_index.db**: M messages indexed, L live (last returned in test query: [ID/subject preview])
- **Extraction cache**: K buckets, total P MB
- **OCR cache**: K buckets, total Q MB
- **Audio cache**: present/absent; N transcripts

### Staleness flags
- [RED/YELLOW/GREEN] Folders whose newest file is newer than their last extraction bucket
- [flag] Folders with extractable files but no extraction bucket
- [flag] Folders with images but no OCR output
- [flag] Folders with audio but no transcripts
- [flag] Memory files lagging Case_Reference by >7 days

### Recommended actions
- Rank the top 3-5 gaps by leverage (e.g. "Recordings has 38 files, 0 transcripts — run /ex-refresh Recordings overnight")

### Quick wins
- Which single command call would close the most coverage gap (usually /ex-refresh over a specific folder)
```

## Constraints

- **Do not modify anything.** This is read-only.
- If docs-rag MCP returns empty or errors, report and suggest `python tools/rag_build.py` to rebuild.
- If mbox index is missing, suggest `python tools/mbox/index.py "C:/Users/atayl/Desktop/Excluded/mbox/*.mbox"`.
- Focus output on gaps, not on what's working. The user sees this to decide what to fix next.
- **Keep the dashboard under 80 lines.** If the data is bigger, summarize and save detail to `AI_Studio/Reports/ex_status_<timestamp>.md`.
