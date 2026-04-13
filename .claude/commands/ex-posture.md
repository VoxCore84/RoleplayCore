---
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(python:*), Bash(ls:*), Bash(find:*), mcp__docs-rag__*, mcp__arcanum__*
description: Use at session start or when asking "what should I be working on today?" Surfaces deadline pressure, urgent items, new evidence absorbed since last session, stale corpus items, and pending actions across legal/career/finance lanes.
---

# /ex-posture — Morning Posture Brief

A single snapshot of where things stand across the Excluded/ corpus and the active legal/career/finance lanes. Designed to be run at session start or first thing in the morning.

## Invocation

`/ex-posture` — full brief
`/ex-posture brief` — abbreviated (top 5 items only)

## Data Sources

1. **Deadlines** — `.claude/deadlines.json` via `.claude/hooks/deadline-alert.py`
2. **Memory** — `~/.claude/projects/C--Users-atayl-VoxCore/memory/case-status.md`, `case-filings-tracker.md`, `case-contacts.md`, `finances-overview.md`, `angel-va.md`
3. **Recent filesystem activity** — files in `Excluded/` modified in last 24h, 7d
4. **Recent ingestion** — newest folders in `.cache/extracted/` and `.cache/ocr/`
5. **Pending synthesis** — `AI_Studio/Reports/sme_*/` folders where README.md is older than underlying pass reports
6. **docs-rag status** — collection size and any rebuild-in-progress flag

## Execution

### Step 1 — Deadline countdown

```bash
python .claude/hooks/deadline-alert.py --all
```

Captures HARD deadlines (<30d), critical (<14d), past-due.

### Step 2 — Memory state

Read these in parallel and extract:
- `memory/case-status.md` — current posture summary, red flags
- `memory/case-filings-tracker.md` — filings with "NEXT ACTION" annotations
- `memory/recent-work.md` — what happened in the last 3 sessions

### Step 3 — Recent filesystem activity

```bash
python3 -c "
import datetime
from pathlib import Path

ROOT = Path('C:/Users/atayl/Desktop/Excluded')
now = datetime.datetime.now().timestamp()

buckets = {'24h':[],'7d':[],'30d':[]}
for p in ROOT.rglob('*'):
    if not p.is_file(): continue
    try:
        age = (now - p.stat().st_mtime) / 86400
    except: continue
    if age < 1: buckets['24h'].append((age, p))
    elif age < 7: buckets['7d'].append((age, p))
    elif age < 30: buckets['30d'].append((age, p))

for label, items in buckets.items():
    print(f'\\n=== Modified in last {label} ({len(items)}) ===')
    for age, p in sorted(items)[:20]:
        rel = p.relative_to(ROOT)
        print(f'  {age*24:.1f}h  {rel}')
"
```

### Step 4 — Ingestion/synthesis lag

```bash
python3 -c "
from pathlib import Path
import datetime

now = datetime.datetime.now().timestamp()
sme = Path('C:/Users/atayl/Desktop').parent / 'atayl/VoxCore/AI_Studio/Reports'
if not sme.exists(): exit()
for d in sme.iterdir():
    if not d.is_dir() or not d.name.startswith('sme_'): continue
    readme = d / 'README.md'
    if not readme.exists(): 
        print(f'{d.name}: README MISSING')
        continue
    readme_age = (now - readme.stat().st_mtime) / 86400
    newest = max((f.stat().st_mtime for f in d.rglob('*.md') if f.is_file()), default=0)
    newest_age = (now - newest) / 86400 if newest else 999
    if readme_age - newest_age > 1:
        print(f'{d.name}: README is {readme_age - newest_age:.1f}d older than newest pass report — resync needed')
"
```

### Step 5 — Urgent flag synthesis

From case-status.md, extract lines containing: DEADLINE, HARD, URGENT, RED FLAG, 5-alarm, five-alarm, critical, blocker.

## Output Format

```
## /ex-posture — [today's date, day of week]

### ⏰ Deadline pressure
| Deadline | Date | Days | Alert |
|----------|------|------|-------|
| ... | | | 🔴/🟡/🟢 |

(🔴 = <14d or past due, 🟡 = <30d, 🟢 = ≥30d)

### 🔥 Top urgency (next 72h)
1. [specific action] — [blocker] — [owner]
2. ...
(Max 5 items. Pull from case-status.md + deadlines + active filings.)

### 📩 Recent activity (last 24h)
- N files modified in Excluded/
- [list top 5 most interesting — case files, emails with attachments]

### 🆕 Ingested since last session
- [folders that appeared in .cache/extracted or .cache/ocr in last 7d]

### ⚠️ Stale / attention needed
- Memory files older than 7d
- Synthesis reports where README is older than pass reports
- Filings with "NEXT ACTION" but no recent activity

### 📋 Legal lane status
| Lane | Owner | Status | Last contact |
|------|-------|--------|-------------|
| ... | | | |

### 💰 Finance state (one line)
[from finances-overview.md — deficit, critical bills this week]

### 🎯 Suggested session focus
Based on the above, here's what today should look like:
1. [specific action]
2. [specific action]
3. [specific action]

### Questions to ask today
- [if any data gaps would resolve a decision, list them]
```

## Constraints

- **Run this fast.** Total execution <30s. If memory files are slow to read, parallelize.
- **No hedging.** If there's urgency, state it. If nothing's urgent, say so.
- **Specific, not generic.** "File DCSA response by Apr 15" beats "follow up on security clearance."
- **Max 100 lines output.** Dashboard, not essay.
- **Safe to run repeatedly.** Read-only.
