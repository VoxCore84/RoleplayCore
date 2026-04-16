---
allowed-tools: Read, Bash(ls:*), Glob, Grep, Write
description: Triage Desktop files — read content, classify by type, recommend keep/move/archive/delete
---

# Desktop Triage

## Next Step

After triage, execute the sort plan with `/file-sort <dir>`, or use `/triage` for the combined workflow.

## Arguments

`$ARGUMENTS` — one of:
- Empty: scan `C:\Users\atayl\Desktop\` (default)
- A directory path to scan instead
- `execute`: execute the last triage plan (moves + deletes with confirmation)

## Instructions

### Phase 1: Scan

1. List all files (not directories) on the Desktop matching: `*.md`, `*.txt`, `*.pdf`, `*.docx`, `*.json`, `*.html`, `*.csv`, `*.eml`, `*.msg`
2. Skip: `*.lnk` (shortcuts), `*.exe`, `*.msi`, `*.zip`, `*.mp4`, `*.png`, `*.jpg`, directories, and the `VocabRef_Parts/` folder (active work)
3. For each file, get: filename, size in KB, modification date

### Phase 2: Read & Classify

For each file, read the first 30-50 lines. Classify into ONE of these categories:

| Class | Meaning | Heuristics |
|-------|---------|------------|
| `CONSUMED_PROMPT` | Session prompt or handoff whose work is fully done | Contains "Paste this into a new Claude Code tab" + work is committed. Contains "HANDOFF" and all items completed. Contains session-specific instructions for past sessions. |
| `LIVE_REFERENCE` | Canonical document still being actively updated | Large (>200 lines), has update timestamps, referenced by other docs or memory files. Architecture docs, playbooks, vocabulary refs. |
| `REUSABLE_PROMPT` | Prompt template useful for future work | ChatGPT/Gemini spec request prompts, test plan templates. Not tied to a completed session. |
| `AI_OUTPUT` | Raw AI response pasted from another model | Contains "Thought for Nm Ns", "Synthesized from social media research", ChatGPT/Gemini analysis output. Should be renamed and moved to `AI_Studio/Reports/`. |
| `CASE_FILE` | Legal case related document | Contains DCSA, HAF, SAPR, AFBCMR, filing, complaint, attorney names, case deadlines. Move to `IMPORTANT DOCS/Case_Reference/`. |
| `TIME_BOUND` | Valid only until a specific date | Call prep, meeting notes, deadline-specific docs. Check if date has passed. |
| `DUPLICATE` | Content exists elsewhere in repo or memory | Cross-check against `AI_Studio/`, `memory/`, `doc/` for matching content. |
| `SCRATCH` | Temp notes with no lasting value | Filename is "new N.txt", file is empty or <5 lines of rough notes, raw transcript paste whose lessons are captured elsewhere. |
| `UNKNOWN` | Can't classify from content | Flag for human review. |

### Phase 3: Recommend

For each file, assign an action:

| Action | When |
|--------|------|
| `KEEP` | LIVE_REFERENCE files actively in use |
| `MOVE` | AI_OUTPUT → `AI_Studio/Reports/` (rename descriptively). CASE_FILE → `IMPORTANT DOCS/Case_Reference/`. REUSABLE_PROMPT → `AI_Studio/1_Inbox/`. |
| `ARCHIVE` | TIME_BOUND past its date, CONSUMED_PROMPT with historical value (e.g., retrospectives) → `AI_Studio/Reports/Archive/` |
| `DELETE` | SCRATCH, CONSUMED_PROMPT with no residual value, DUPLICATE |
| `REVIEW` | UNKNOWN or ambiguous — needs human decision |

### Phase 4: Report

Output a table:

```
## Desktop Triage Report — [date]
Scanned: [N] files in [path]

| # | File | Size | Modified | Class | Action | Destination | Reason |
|---|------|------|----------|-------|--------|-------------|--------|
```

Then a summary:
```
### Summary
- KEEP: N files
- MOVE: N files
- ARCHIVE: N files
- DELETE: N files
- REVIEW: N files
```

Save the report to `AI_Studio/Reports/desktop_triage_[date].md` for the execute phase.

### Phase 5: Execute (only if `$ARGUMENTS` is "execute")

1. Read the most recent `AI_Studio/Reports/desktop_triage_*.md`
2. Show the plan one more time
3. Ask user to confirm: "Proceed with N moves, N archives, N deletes?"
4. Execute MOVES first (safest)
5. Execute ARCHIVES second
6. Execute DELETES last — show each filename before deleting, skip if user says no
7. Report results: N moved, N archived, N deleted, N skipped

### Safety Rules

1. **Never auto-execute** — Phase 4 always stops for review
2. **Never delete without showing the filename** and getting confirmation
3. **Never move CASE_FILE documents without explicit confirmation** — chain of custody matters
4. **If a file is >1MB**, warn before any action (might be a data file, not a document)
5. **If unsure, classify as REVIEW** — false negatives are better than false deletions
6. **Cross-check before calling DUPLICATE** — read both files to confirm, not just filename similarity
