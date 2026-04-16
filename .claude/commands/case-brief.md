---
allowed-tools: Read, Grep, Glob, Bash(python3:*), Bash(python:*)
description: Combined case dashboard — status + deadlines + lane map in one view
---

# Case Brief

Single-command case situational awareness. Combines `/case-status`, `/deadlines`, and `/lane-map` into one output.

## Instructions

Run all three components IN PARALLEL, then format as a unified brief.

### Component 1: Case Status

Read `~/.claude/projects/C--Users-atayl-VoxCore/memory/case-status.md` and extract:
- ADSCD countdown (days from today to 2026-08-10)
- Current status summary (first 2-3 key bullet points)
- Red flags / action items
- Key contacts with roles

### Component 2: Deadlines

Calculate countdown days for all active case deadlines (same logic as `/deadlines`):

```python
python3 -c "
from datetime import date
today = date.today()
deadlines = [
    ('AFBCMR DD-149 filing', date(2026, 5, 15), 'TARGET'),
    ('Retention request past ADSCD', date(2026, 5, 15), 'TARGET'),
    ('ADSCD (separation)', date(2026, 8, 10), 'HARD'),
    ('Section 1983 SOL (Rio Vista)', date(2026, 9, 23), 'HARD'),
    ('SEAD 9 trigger (1yr clearance susp)', date(2026, 11, 26), 'SOFT'),
]
for name, d, cat in deadlines:
    delta = (d - today).days
    flag = 'CRITICAL' if delta < 14 else 'URGENT' if delta < 30 else 'SOON' if delta < 60 else 'OK'
    if delta >= 0:
        print(f'{delta:>4}d | {flag:<8} | {cat:<7} | {name}')
    else:
        print(f'{abs(delta):>4}d ago | PAST DUE | {cat:<7} | {name}')
"
```

### Component 3: Lane Map

Read `~/.claude/projects/C--Users-atayl-VoxCore/memory/case-contacts.md` and extract the attorney/advocate lane ownership table — who handles what filing type.

### Output Format

```
## Case Brief — [today's date]

### ADSCD: [N] days remaining (Aug 10, 2026)

### Status
[2-3 bullet points from case-status.md]

### Deadlines
[table from Component 2]

### Lane Map
| Lane | Owner | Status |
|------|-------|--------|
| [filing type] | [attorney/advocate] | [active/pending/filed] |

### Action Items
[top 3-5 most urgent items from case-status.md]
```

## After This

- For specific questions about the case: `/ex ask "<question>"`
- To prepare a filing: `/filing-prep <type>`
- For a deep evidence check: `/evidence-gap <filing-type>`
