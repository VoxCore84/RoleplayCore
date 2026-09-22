# rules-reference — long form + history for `.claude/rules/*.md`

Created 2026-09-22 (optimization sweep, session e523922e). Each file here holds the narrative rationale, worked examples, verified-facts tables, and strikethrough history that were moved out of the matching always-loaded rule in `.claude/rules/` to cut per-turn context cost. The operative rules (MUST / NEVER / gates / checklists / trigger rows) stayed in `.claude/rules/`; nothing was deleted, only relocated verbatim.

Why here and not `.claude/rules/reference/`: Claude Code discovers `.claude/rules/**` recursively, so a subfolder there would still be loaded every turn. `docs/` is read only when a session opens it.

Files: fan-out-scaling, skill-reminders, operational-discipline, measurement-discipline, session-handoff, documentation-discipline. Pre-move originals: `AI_Studio/Reports/sweep_2026-09-22/rules_backup_*/` and git history.
