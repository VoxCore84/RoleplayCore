---
title: "Guide: Hooks for Power Users — Arcanum Wiki (Part 2/5)"
description: "hooks power user guide — PreToolUse PostToolUse UserPromptSubmit, shell command hooks, JSON protocol, decision allow deny ask, timestamp injector example"
tags: [guides, shell-command, json-protocol, decision-allow]
part: 2
parts: 5
---

## Setting Up Hooks

Hooks are configured in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/verify_edit.py",
            "statusMessage": "Verifying edit..."
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/timestamp_injector.py"
          }
        ]
      }
    ]
  }
}
```

### Matcher Patterns

| Pattern | Matches |
|---------|---------|
| `""` (empty) | ALL events of that type |
| `"Edit"` | Only Edit tool calls |
| `"Bash"` | Only Bash tool calls |
| `"Write"` | Only Write tool calls |

---
[Part 1](hooks_power_user_pt1.md) | **Part 2** | [Part 3](hooks_power_user_pt3.md) | [Part 4](hooks_power_user_pt4.md) | [Part 5](hooks_power_user_pt5.md)
