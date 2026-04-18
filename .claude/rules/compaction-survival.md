# Compaction Survival — Automatic State Persistence

Context compresses. Disk doesn't. Write state to disk proactively so compaction never causes drift.

## Auto-Write Triggers

Write to `AI_Studio/Reports/session_state_live.md` (overwrite, not accumulate) when ANY of these occur:

1. **Completed a significant subtask** — applied SQL, finished a code change, completed a multi-file search
2. **Switching work type** — SQL to C++, research to implementation, one subsystem to another
3. **20+ tool calls since last write** — context is getting heavy
4. **Background agent returned results** — capture findings immediately
5. **Discovered expensive data** — schema details, file paths, person info, regulatory citations, query results
6. **User gave a new major directive** — session goal shifted

## What to Write (< 50 lines)

```markdown
# Live State — [date] [time]
## Goal: [current objective]
## Done: [numbered list of completed items with output file paths]
## Modified: [files changed this session]
## Key Facts: [expensive-to-rediscover data — schemas, paths, names, amounts]
## Pending: [what's left]
## Agents: [any running/completed agents and their findings]
```

## Write-Through Rules

- **Architecture decisions**: When the user approves a design choice, write it to the relevant memory file or doc THAT SAME TURN. Don't hold decisions in context.
- **Query results**: If a DB query or search took multiple steps to produce, write the result to a file. Don't rely on context to preserve it.
- **Agent findings**: When a background agent completes, persist key results to a file BEFORE continuing other work.

## What NOT to Do

- Don't use CronCreate (BANNED — see no-recurring-cron.md)
- Don't announce checkpoints to the user (silent unless asked)
- Don't write multi-page reports — this is a survival scratchpad
- Don't checkpoint trivial ops (file reads, git status, single grep)
- Don't accumulate checkpoint files — one file, overwritten each time
