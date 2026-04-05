---
title: "Tool Pipeline Overview -- Arcanum Wiki (Part 4/4)"
description: "tool pipeline overview — buildTool factory, Tool.ts, ToolDef interface, tool registration, assembleToolPool, concurrent batching, ToolSearch deferred loading, tool result persistence"
tags: [tools, buildtool-factory, toolts, tooldef-interface, tool-registration, assembletoolpool, concurrent-batching, tool-result]
part: 4
parts: 4
---

## Permission Modes

The `ToolPermissionContext` (src/Tool.ts:123-138) supports these modes:

- `default` -- standard interactive approval
- `bypassPermissions` -- skip all permission checks (`--dangerously-skip-permissions`)
- `acceptEdits` -- auto-approve file edits
- `auto` -- AI classifier auto-approves based on transcript analysis
- `plan` -- read-only exploration mode (blocks writes, allows reads)

Each mode affects which tools require user confirmation and which auto-approve.

---
[Part 1](pipeline_overview_pt1.md) | [Part 2](pipeline_overview_pt2.md) | [Part 3](pipeline_overview_pt3.md) | **Part 4**
