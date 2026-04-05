---
title: "Rules System -- Arcanum Wiki (Part 3/4)"
description: "rules system — .claude/rules/ files, conditional vs unconditional, paths frontmatter activation, recursive walk-up, priority order, token savings"
tags: [core, clauderules-files, recursive-walk-up, priority-order, token-savings]
part: 3
parts: 4
---

### File Processing Pipeline

Each rules file goes through this pipeline:

```
File on disk
  -> readFileSync()
  -> parseYAMLFrontmatter()  (extract paths:, name:, description:, etc.)
  -> stripHtmlComments()     (remove <!-- ... --> blocks)
  -> resolveIncludes()       (process @path directives, max depth 5)
  -> MemoryFileInfo object   (path, content, type, frontmatter)
```

---
[Part 1](rules_system_pt1.md) | [Part 2](rules_system_pt2.md) | **Part 3** | [Part 4](rules_system_pt4.md)
