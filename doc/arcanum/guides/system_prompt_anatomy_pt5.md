---
title: "Guide: Anatomy of the System Prompt — Arcanum Wiki (Part 5/5)"
description: "system prompt anatomy — assembly pipeline, dynamic boundary, CLAUDE.md as user message not system, cacheable sections, token costs, what you can control"
tags: [guides, assembly-pipeline, dynamic-boundary, cacheable-sections, token-costs, what-you]
part: 5
parts: 5
---

## Token Costs

Approximate token costs for each section:

| Section | ~Tokens | Cacheable |
|---------|---------|-----------|
| Static prefix + instructions | 8,000-12,000 | Yes (global) |
| Tool descriptions (40+ tools) | 3,000-5,000 | Yes (global) |
| Git instructions | ~2,000 | Yes (global) |
| Environment | ~500 | No (per-session) |
| Memory instructions | ~800 | No (per-session) |
| MCP instructions | Variable | No (per-session) |
| Skill descriptions | Variable | No (per-session) |
| CLAUDE.md (user message) | YOUR content | No |
| Rules files | YOUR content | No |
| Memory files | YOUR content | No |
| Git status | Up to 2K chars | No |

**Total baseline**: ~15-20K tokens before your content. This is the "tax" every turn.

## Cross-References

- [Architecture Overview](../core/architecture.md) — full system architecture
- [CLAUDE.md Injection](../core/claude_md_injection.md) — how CLAUDE.md is found and merged
- [Context Window](optimizing_context.md) — optimizing your context budget
- [Rules System](../core/rules_system.md) — conditional rules deep dive

---
[Part 1](system_prompt_anatomy_pt1.md) | [Part 2](system_prompt_anatomy_pt2.md) | [Part 3](system_prompt_anatomy_pt3.md) | [Part 4](system_prompt_anatomy_pt4.md) | **Part 5**
