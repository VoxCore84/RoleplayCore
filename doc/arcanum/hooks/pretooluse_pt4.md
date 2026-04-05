---
title: "PreToolUse Hook -- Arcanum Wiki (Part 4/4)"
description: "PreToolUse hook — runs before tool execution, input modification, permission decisions allow deny ask, if-conditions, most powerful hook type"
tags: [hooks, input-modification, if-conditions, most-powerful]
part: 4
parts: 4
---

## Key Source Files

| File | Purpose |
|------|---------|
| `src/utils/hooks.ts` | Core execution engine, matcher filtering |
| `src/services/tools/toolHooks.ts` | `runPreToolUseHooks()`, permission resolution |
| `src/schemas/hooks.ts` | Hook schema definitions |

## Cross-References

- [Hooks Overview](overview.md) -- System architecture
- [PostToolUse](posttooluse.md) -- The complementary post-execution hook
- [Permissions Overview](../permissions/overview.md) -- How hook decisions interact with permissions

## Interesting Findings

**Hook allow is the weakest override.** A single deny rule in settings.json overrides any number of hook `allow` decisions. This is a deliberate safety design -- hooks cannot bypass explicitly configured security policies.

**The `if` condition prevents unnecessary process spawning.** For Bash hooks, tree-sitter parsing is used to extract the command from the input, so a hook with `if: "Bash(git *)"` only fires for git commands, not every Bash invocation.

---
[Part 1](pretooluse_pt1.md) | [Part 2](pretooluse_pt2.md) | [Part 3](pretooluse_pt3.md) | **Part 4**
