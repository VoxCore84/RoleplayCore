---
allowed-tools: Bash(claude:*), WebFetch, WebSearch, Read
description: Check Claude Code changelog for updates relevant to this setup
---

# Claude Code Updates Check

Check the Claude Code changelog for new features, fixes, and changes relevant to this specific environment.

## Instructions

### Step 1: Get current version

Run `claude --version` to get the installed version number (e.g., "2.1.111").

### Step 2: Fetch the changelog

Use WebFetch to read the official changelog:
- URL: `https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md`
- Prompt: "Extract ALL changelog entries. For each version, list every feature, fix, and improvement. Include version numbers."

If WebFetch fails or is truncated, fall back to WebSearch:
- Query: `"Claude Code changelog" site:github.com anthropics/claude-code CHANGELOG`

### Step 3: Identify new entries

Filter the changelog to only show entries with version numbers NEWER than the currently installed version. If the changelog doesn't show version numbers clearly, use date-based filtering (entries from the last 2 weeks).

### Step 4: Cross-reference against this setup

Read `~/.claude/projects/C--Users-atayl-VoxCore/memory/MEMORY.md` to load the setup profile. Key setup characteristics to match against:

| Setup Aspect | What to Match |
|---|---|
| **Windows 11** | Any Windows-specific fixes, PowerShell tool changes, path handling |
| **6+ MCP servers** (arcanum, codeintel, docs-rag, voxcore-db, voxcore-server, local-llm) | MCP transport fixes, timeout changes, connection handling, large output |
| **60+ custom skills** | Skill loading, frontmatter parsing, token budgets |
| **23+ hooks via daemon** (PreToolUse, PostToolUse, PreCompact, SessionStart, etc.) | Hook event changes, new hook events, hook output handling |
| **Multi-tab workflow** | Session resume, worktrees, session_state coordination |
| **Long sessions** (1M context, Opus 4.6) | Context compaction, memory management, prompt caching |
| **Heavy agent usage** | Agent spawning, subagent fixes, permission inheritance |
| **Legal case work** | Large file handling, document reading, search tools |
| **Git operations** | Git command changes, push/commit behavior |
| **Windows Terminal** | Rendering fixes, keyboard shortcuts, NO_FLICKER |

### Step 5: Output

Format as a ranked list, most impactful first:

```
## Claude Code Updates: v[current] → v[latest]

### High Impact (affects your daily workflow)
1. **[Feature/Fix name]** (v[version]) — [1-line description]
   Why it matters: [how it affects this specific setup]

### Medium Impact (nice to have)
2. ...

### Low Impact (awareness only)
3. ...

### Already Up to Date
[If current version IS the latest, say so and list the last 3 notable changes you already have]
```

### Step 6: Suggest actions

If any new entries suggest configuration changes (new env vars, new settings, deprecated features), list them as actionable items:

```
### Suggested Actions
- [ ] Add `ENV_VAR=value` to settings.json — [reason]
- [ ] Run `/doctor` — [new diagnostic available]
- [ ] Test `/new-command` — [relevant to your workflow because...]
```
