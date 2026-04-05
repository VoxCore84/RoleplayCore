---
title: "PostToolUse Hook -- Arcanum Wiki (Part 3/4)"
description: "PostToolUse hook — runs after tool execution, context injection, MCP output replacement, observe-only no blocking, logging audit trail"
tags: [hooks, context-injection, mcp-output, observe-only-no, logging-audit]
part: 3
parts: 4
---

### Exit Code Semantics

| Exit Code | PostToolUse Behavior |
|-----------|---------------------|
| 0 | Stdout shown in transcript mode |
| 2 | Stderr shown to model as blocking error |
| Other | Stderr shown to user only |

---
[Part 1](posttooluse_pt1.md) | [Part 2](posttooluse_pt2.md) | **Part 3** | [Part 4](posttooluse_pt4.md)
