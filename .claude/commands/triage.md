---
allowed-tools: Read, Write, Bash(python:*), Bash(python3:*), Bash(ls:*), Glob, Grep, Agent
description: Full desktop/folder cleanup — triage files then execute sort plan with confirmation
---

# Triage

Two-phase folder cleanup: first classify and recommend actions for every file, then execute the sort plan with user approval. Chains `/desktop-triage` and `/file-sort`.

## Arguments

`$ARGUMENTS` — path to the directory to triage (default: `C:/Users/atayl/Desktop` if omitted)

## Pipeline

### Phase 1: Triage

Follow the instructions in `.claude/commands/desktop-triage.md`:
1. List all files in the target directory
2. Read content to classify each by type
3. Recommend action for each: **keep** (in place), **move** (to specific destination), **archive** (to `_Archive/`), or **delete**
4. Present the triage plan as a table

**STOP and wait for user approval.** The user may:
- Approve the entire plan: "go" / "do it" / "approved"
- Modify specific items: "keep file X instead of archiving"
- Cancel: "stop" / "nevermind"

Do NOT proceed to Phase 2 without explicit approval.

### Phase 2: Sort

After user approves (with any modifications), follow the instructions in `.claude/commands/file-sort.md`:
1. Generate the move plan from the approved triage results
2. Run a **dry-run first** — show what would happen without moving anything
3. Wait for user confirmation of the dry-run output
4. Execute the moves
5. Verify each move completed (source gone, dest exists, size matches)
6. Report results

### Output

```
## Triage Complete

### Summary
- **Scanned**: N files
- **Kept**: N files (in place)
- **Moved**: N files (to organized locations)
- **Archived**: N files (to _Archive/)
- **Deleted**: N files
- **Failed**: N files (with reasons)

### Moved Files
| File | From | To |
|------|------|----|
| ... | ... | ... |
```

### Rules

- **Never delete without explicit user confirmation per file**
- **Never move files containing credentials, keys, or PII** without flagging them first
- **Dry-run is mandatory** before any actual file operations
- **Size verification** after each move — catches silent no-clobber (known gotcha from session 235)
