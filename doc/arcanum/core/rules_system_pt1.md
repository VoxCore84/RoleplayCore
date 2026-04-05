---
title: "Rules System -- Arcanum Wiki (Part 1/4)"
description: "rules system — .claude/rules/ files, conditional vs unconditional, paths frontmatter activation, recursive walk-up, priority order, token savings"
tags: [core, clauderules-files, recursive-walk-up, priority-order, token-savings]
part: 1
parts: 4
---

# Rules System -- Arcanum Wiki

## Overview

The `.claude/rules/` directory system provides a structured way to organize Claude Code instructions by topic. Rules files are markdown documents that are loaded alongside CLAUDE.md content and injected into the model's context. The system supports two modes: unconditional rules that are always loaded, and conditional rules that activate only when the model interacts with files matching specified glob patterns.

---
**Part 1** | [Part 2](rules_system_pt2.md) | [Part 3](rules_system_pt3.md) | [Part 4](rules_system_pt4.md)
