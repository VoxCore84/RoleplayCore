# skill-reminders — reference (moved from .claude/rules/skill-reminders.md on 2026-09-22; operative rules remain in the rules file)

## Rows DELETED on 2026-09-22 (commands turned off that day) — preserved verbatim

These 9 trigger-table rows referenced one or more of the 22 slash commands disabled on 2026-09-22
(apply-sql, build-loop, check-logs, code-audit, compress-video, db-lint, decode-pkt, lookup-area,
lookup-creature, lookup-emote, lookup-faction, lookup-item, lookup-sound, lookup-spell, new-script,
new-sql-update, parse-errors, parse-packet, smartai-check, soap, sql-pipeline, tdb-diff), or were
marked OBSOLETE in the file itself. If any command is re-enabled, restore its row.

| Trigger | Action |
|---|---|
| Server restart, crash, debugging begins | `/check-logs` — just run it |
| Build error pasted | `/parse-errors` — just run it |
| User asks to audit code quality, find bugs, review custom systems | `/code-audit [dir]` — fan out parallel agents |
| About to spawn 2+ parallel sub-agents (Agent tool) for a non-trivial task | **OBSOLETE as of 2026-09-22** — subagent model migrated to `claude-sonnet-5` (natively 1M, no extra-usage credits on any plan, per live model-config docs). The `/extra-usage` pre-check is only needed again if a `[1m]`-suffixed subagent pin ever returns. Historical pain: 7+ failures, sessions 263–278h. |
| SQL file created/edited | `/smartai-check` (if SmartAI) or `/apply-sql` |
| Writing new SQL update | `/new-sql-update` — run for filename |
| Name without ID (spell/item/creature/area) | Run `/lookup-*` to resolve |
| DB errors, orphan references, data quality concerns | `/db-lint [db]` — scan for common issues, generate fix SQL |
| Comparing local DB against upstream TrinityCore | `/tdb-diff <table>` — download TDB, diff, generate update SQL |

## Workflow-chain rows DELETED on 2026-09-22 — preserved verbatim

| Pattern Detected | Suggest |
|---|---|
| User creates SQL file, then validates, then applies | `/sql-pipeline <db>` — full lifecycle in one command |
| User runs `/tdb-diff` then manually applies the SQL | Suggest: "Want me to apply the generated SQL with `/apply-sql`?" |
| User runs `/build-loop` and server restarts | Auto-run `/check-logs` — always safe, read-only |

## Bottom-rule bullet DELETED on 2026-09-22 — preserved verbatim

- `/check-logs` is always safe to run proactively — read-only.

## Section preamble moved from the rules file (verbatim)

### Workflow Chains — Suggest Combos When Steps Are Manual

When the user is doing steps from a chain manually, suggest the combo skill instead.
