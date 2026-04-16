---
allowed-tools: Bash(ls:*), Bash(date:*), Bash(mysql:*), Bash(cat:*), Bash(echo:*), Bash(python3:*), Read, Write, Grep, Glob
description: Full SQL lifecycle — create file, validate SmartAI, apply to DB, check for errors
paths: sql/**/*.sql
---

# SQL Pipeline

End-to-end SQL workflow: create the update file, optionally validate SmartAI, apply it, and verify no DB errors.

## Arguments

`$ARGUMENTS` — `<database> [description]`
- Database: `world`, `auth`, `characters`, or `hotfixes`
- Description (optional): brief note for the file header comment

Example: `/sql-pipeline world fix missing creature spawns`

## Pipeline

### Phase 1: Create the SQL file

Follow the instructions from `/new-sql-update`:
1. Parse the database name from $ARGUMENTS (first word)
2. Get today's date in `YYYY_MM_DD` format
3. Find the next sequence number in `sql/updates/<db>/master/`
4. Create the file with a header comment using the description if provided
5. **Report the file path** and tell the user: "Edit the SQL file now. Tell me when ready, or paste the SQL content."

### Phase 2: Wait for user content

**STOP HERE and wait for the user.** They need to either:
- Edit the file externally and say "ready" or "go"
- Paste SQL content for you to write into the file

Do NOT proceed until the user confirms the SQL content is in the file.

### Phase 3: Validate (if SmartAI)

Read the first 50 lines of the SQL file. If it contains `smart_scripts`, `smartai`, `creature_ai_scripts`, `SAI`, or `INSERT INTO.*smart`:
1. Run `/smartai-check` validation against the file
2. If errors found, report them and ask user to fix before continuing
3. If clean, proceed

If the SQL doesn't contain SmartAI content, skip this phase.

### Phase 4: Apply

Follow the instructions from `/apply-sql`:
1. Verify the SQL file exists and has content
2. Apply using: `echo "SET innodb_lock_wait_timeout=120;" | cat - <file> | "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe" -u root -padmin <database>`
3. Report success or failure

### Phase 5: Verify

Check for DB errors after application:
1. Read the last 20 lines of the DBErrors log (use the voxcore-server MCP `tail_log` tool with log="dberrors" and lines=20)
2. If new errors appear that reference tables/columns from the applied SQL, report them
3. If clean, report "Applied and verified — no new DB errors"

### Output

```
## SQL Pipeline Complete

| Phase | Status |
|-------|--------|
| Create | `sql/updates/<db>/master/YYYY_MM_DD_NN_<db>.sql` |
| Validate | [skipped / N issues / clean] |
| Apply | [success / failed: reason] |
| Verify | [clean / N new errors] |
```
