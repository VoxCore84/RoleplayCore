# Agent Hook Examples (type: "agent")

Swap these into `.claude/settings.json` to use LLM-powered verification hooks.
These are slower (~3-5s with haiku) but can handle complex logic that daemon
handlers can't express in pure Python.

## Tab Ownership Check (agent version)

Replace the daemon-based `http` hook with this to use an LLM agent instead.
The daemon version is <10ms; this is ~3-5s but can handle fuzzy matching.

```json
{
  "matcher": "Edit|Write",
  "hooks": [
    {
      "type": "agent",
      "if": "Edit(*session_state*)|Edit(*Central_Brain*)|Write(*session_state*)|Write(*Central_Brain*)",
      "model": "haiku",
      "timeout": 10,
      "prompt": "Tab ownership check. Hook input: $ARGUMENTS\n\nRead doc/session_state.md. Find '## Active Tabs & Assignments'. If 2+ ACTIVE tabs exist and the file_path from tool_input appears in another tab's Owns column, respond: {\"decision\": \"block\", \"reason\": \"File owned by another active tab — use patch-file handoff\"}. Otherwise: {\"decision\": \"allow\"}. One file read, one decision. Be fast."
    }
  ]
}
```

## SQL Column Verification (agent)

Before applying SQL, verify column names against the schema.
Reads the SQL file and checks for common mistakes.

```json
{
  "matcher": "mcp__voxcore-db__safe_apply",
  "hooks": [
    {
      "type": "agent",
      "model": "haiku",
      "timeout": 15,
      "prompt": "SQL pre-apply verification. Hook input: $ARGUMENTS\n\nRead the SQL file at sql_file_path from tool_input. Check for: (1) INSERT/UPDATE referencing tables without matching column counts, (2) common VoxCore mistakes: 'FactionID' instead of 'faction', 'npcflag' is bigint, 'item_template' doesn't exist (use hotfixes.item_sparse). If suspicious: {\"decision\": \"block\", \"reason\": \"[specific issue]\"}. If OK: {\"decision\": \"allow\"}."
    }
  ]
}
```

## Memory Citation Check (agent)

Verify memory files include source citations per Excluded corpus Rule 5.

```json
{
  "matcher": "Write",
  "hooks": [
    {
      "type": "agent",
      "if": "Write(*memory*)",
      "model": "haiku",
      "timeout": 10,
      "prompt": "Memory citation check. Hook input: $ARGUMENTS\n\nCheck if the content being written (new_string or content from tool_input) contains at least one source citation (patterns like 'file_path:line', 'Source:', or markdown links to source files). Structural files (MEMORY.md indexes, topic-index.md) are exempt. If factual claims exist without any citations: {\"decision\": \"block\", \"reason\": \"Memory file has factual claims without source citations (Rule 5)\"}. If OK: {\"decision\": \"allow\"}."
    }
  ]
}
```

## Speed Tips

- Always set `model: "haiku"` — it's 10-20x faster than opus for yes/no decisions
- Set `timeout: 10` — default 60s is way too conservative for single-file checks
- Use `if` to filter by file path — prevents the hook from firing on irrelevant tool calls
- Keep prompts short and prescriptive — "read X, check Y, decide Z"
- Agent hooks can use Read, Grep, Glob — NOT Bash, NOT MCP tools
- For anything that can be expressed as regex/parse logic, the daemon is always faster
