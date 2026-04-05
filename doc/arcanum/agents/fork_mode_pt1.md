---
title: "Fork Mode -- Arcanum Wiki (Part 1/4)"
description: "fork mode — prompt cache sharing, byte-identical API prefix, subagent spawning optimization, parent context inheritance, cache hit maximization"
tags: [agents, prompt-cache, cache-hit]
part: 1
parts: 4
---

# Fork Mode -- Arcanum Wiki

## Overview

Fork mode creates child agents that share the parent's full conversation context and prompt cache prefix. Unlike typed subagents that start with fresh context, fork children inherit everything -- system prompt bytes, tool definitions, conversation history, and thinking configuration. This enables significant cost savings through prompt cache reuse while allowing parallel work delegation.

Fork mode is the primary mechanism when the model decides "more of me, not a different specialist." All fork spawns are forced async.

---
**Part 1** | [Part 2](fork_mode_pt2.md) | [Part 3](fork_mode_pt3.md) | [Part 4](fork_mode_pt4.md)
