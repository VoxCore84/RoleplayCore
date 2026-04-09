# VoxCore Session State — Multi-Tab Coordination

**Read this FIRST in any new Claude Code tab.**
This is the single source of truth for what all tabs are doing, what's done, what's blocked, and what to pick up next. Updated by whichever tab finishes work.

**Last updated**: April 8, 2026 -- Main tab dispatched CC 2.1.97 source refresh to a new tab. Handoff: `doc/handoff_cc_297_source_refresh.md`. New tab OWNS all of `AI_Studio/Reports/ClaudeCodeInternals/` + `memory/claude-code-internals.md`.

---

## Active Tabs & Assignments

| Tab | Assignment | Status | Notes |
|-----|-----------|--------|-------|
| Main (229) | Warlock Phase 4 modernization + Tier B triage | COMPLETE | 15 old-style handlers → RegisterSpellScript. Triage: 147 TC-native / 22 real TODO. Handoffs below. |
| **Warlock-A1** | Tier A: Summon Demonic Tyrant (265187) | COMPLETE | `spell_warl_summon_demonic_tyrant`: demon duration +15s, Reign of Tyranny buff. SQL: `_06_world.sql`. Commit: `0d4717c013` |
| **Warlock-A2** | Tier A: Mayhem (387506) | READY | Destruction. Spell duplication to secondary target. See handoff below. |
| **Warlock-A3** | Tier A: Demonic Soul (449614) | COMPLETE | Aura 396 = native TRIGGER_SPELL_ON_POWER_AMOUNT (not PROC_TRIGGER_SPELL_COPY). Handler on 450510 chains to AoE damage burst 449801 (3.53 SP coeff). SQL: `_07_world.sql`. Commit: `0d4717c013` |
| **Warlock-B** | Tier B: 6 Summon spells | COMPLETE | 5 handlers + 1 TC_NATIVE. C++ compiles clean (LNK1104 = server running). SQL: `2026_04_04_08_world.sql`. |
| **Warlock-C** | Tier C: 5 Class utilities | COMPLETE | Demon Skin + Soul Link handlers. Mortal Coil/Soulburn/Ichor TC_NATIVE. Deep audit: GetPet() fix. SQL: `_09_world.sql`. Commits: `0d4717c013`, `51d8381bd1`. |
| **Warlock-D** | Tier D: 8 MAYBE spells + deep audit | COMPLETE | All 8 resolved. Deep audit: fixed 5 orphan DB entries (2 name mismatches + 3 stale), Soul Link pet check. SQL: `_11`. Commits: `0d4717c013`, `51d8381bd1`. |
| **CC-297-Refresh** | Re-extract claude-code 2.1.97 sources, diff vs 2.1.88, patch all 22 internals reports + memory file | IN PROGRESS (2026-04-08) | Handoff: `doc/handoff_cc_297_source_refresh.md`. OWNS: `AI_Studio/Reports/ClaudeCodeInternals/**`, `memory/claude-code-internals.md`. Do NOT touch from other tabs. |
| -- | -- | -- | Add rows as tabs are opened |

**Rule**: Before starting work, check this file. If another tab owns a file or task, don't touch it. Update your row when you start and when you finish.

---


> Historical tab rows (sessions 107-228) and Warlock session 229 handoff prompts archived to [session_state_archive.md](session_state_archive.md).

## Release Gate System (NEW — Session 165)

A pre-ship audit system is now available for all addon/tool work. Use it before shipping anything.

### Available Tools

| Tool | What | When |
|------|------|------|
| `/pre-ship <path>` | Full 5-phase audit: mechanical checks + 3 parallel adversarial agents (noob, bully, security) | Before any release, zip, or GitHub publish |
| `/release-gate-fix` | Focus only on open BLOCKING items from last audit | After running `/pre-ship`, to fix what it found |
| Enforcement hooks | `PreToolUse` blocks `git push --tags`, `gh release`, zip when gate != PASS. `PostToolUse` invalidates gate when publishable/ files are edited | Automatic — no action needed |

### Validator Agents (`.claude/agents/`)

| Agent | Role | Mode |
|-------|------|------|
| `grep-auditor` | Naming remnants, non-ASCII, secrets, dead refs | Read-only |
| `doc-auditor` | Path verification, version consistency, feature claims vs reality | Read-only |
| `app-reviewer` | Adversarial personas (noob, bully, security) | Read-only |

### Gate State File

`.claude/release-gate-status.json` — written by `/pre-ship`, read by hooks. Values: `PASS`, `FAIL`, `STALE`, `UNKNOWN`.

### Checklist Reference

Full 16-phase, ~130 item checklist: `memory/addon-building-checklist.md`. Covers Lua, C++, Python, naming, docs, packaging, security, distribution.

### Known Issue

Custom agent types (`app-reviewer`, `grep-auditor`, `doc-auditor`) require Claude Code restart to register. Until then, `/pre-ship` uses `general-purpose` agents with detailed prompts — same results, just no type restriction.

### Pre-Ship Audit Findings (Session 165)

62 findings across CreatureCodex + VoxGM. Full report was delivered in session chat. Key blockers for each project:

**CreatureCodex blockers**: Rename not finished (live source still says Bestiary), dev artifacts in distribution (CHATGPT_AUDIT_REQUEST*.md, reference/ dir), em dashes in Python/C++, RBAC SQL inconsistency between README and sql file, Linux shell scripts call Windows-only APIs

**VoxGM blockers**: ~300-400 lines dead code, Favorites/History claimed as features with zero UI, em dashes in 4 Lua files, "Max Gold (999g)" label wrong (gives ~9999g), README claims "any TrinityCore server" but ~15 commands are VoxCore-specific

---

## Current Server State

- **Build**: Current (VS build done). Includes transmog fail-open + bridge grace + BestiaryForge hooks
- **Server**: RUNNING (PID 33360, 22GB RAM)
- **Client**: 12.0.1.66709
- **DB**: world ~1,400 MB (TC TDB + LoreWalker merged) | hotfixes ~900 MB (TC + LW) | characters 4 MB
- **Logs**: 6.8M DBErrors from LAST boot (pre-cleanup). After Phase 1-2a (886K rows) + Phase 4 (32K world + 20K hotfix), expect ~2-3M remaining (loot items, flags, serverside spells — not fixable with SQL). Zero crashes.
- **LoreWalker TDB**: APPLIED. **TC TDB 1200.26021**: BACKFILLED via INSERT IGNORE (session 227). Both data sets coexist. **RoleplayCore SQL**: Re-applied (session 228 Tab A).

---

## What Needs Doing — Priority Order

### Tier 1: Server Restart & Test (requires human)

Build is done. These need a server restart and in-game testing.

- [ ] **Restart worldserver** and test:
  - Arcane Waygate (`.cast 1900028`, gossip, teleports)
  - Stormwind phase fixes (7 phase_area, Genn/Velen/Anduin visibility)
  - Valdrakken portal, embassy NPCs, Hero's Call Boards
  - Apply `_08_00` SQL before restarting
- [ ] **CreatureCodex in-game test** — C++ build clean (866/866), `.codex` command, addon deployed. GitHub v1.0.0 released
- [ ] **Enable crash dumps** — Windows crash dump generation for worldserver

> **Note**: Transmog Outfits UI work is ARCHIVED — reimplemented externally. All transmog bugs, slash commands, and agents have been removed. Historical docs preserved in `doc/archive/transmog.md` and `doc/transmog_*`.

### Tier 2: World DB Cleanup (Claude Code tab can do independently)

**Assign to**: Any available tab
**How**: Run `python tools/diff_draconic.py --zone <id> --map <map>`
**Plan**: `doc/world_db_cleanup_plan.md`

Priority order:
1. Orgrimmar (zone 1637, map 1)
2. Ironforge (zone 1537, map 0)
3. Thunder Bluff (zone 1638, map 1)
4. Darnassus (zone 1657, map 1)
5. Undercity (zone 1497, map 0)
6. Exodar (zone 3557, map 530)
7. Silvermoon (zone 3487, map 530 → newly map 0 for Midnight)
8. Dalaran (zone 4395, map 571)
9. Global phase_area audit (after all zones done)

Each zone produces a SQL file in `sql/exports/` and findings for review.

### Tier 3: Spell Implementation (Claude Code tab can do independently)

**Assign to**: Any available tab
**Context**: `memory/spell-audit.md`
- 13 RED spells need real C++ implementations (SimC-guided)
- 84 YELLOW passive DUMMY auras (low priority)
- Key spells: Avenging Wrath, Pillar of Frost, Blood Plague, Divine Hymn

### Tier 4: Data Quality (Claude Code tab can do independently)

- **66 crash-risk creature displayIDs** — query world DB, fix or remove
- **3 MySQL deadlocks** — investigate transaction contention patterns
- **Companion Squad SQL** — apply `sql/RoleplayCore/5.1 companion characters.sql`
- **Equipment gaps** — 13K NPCs missing `creature_equip_template`

### Tier 5: Website & Polish

- Arcane Codex website asset pipeline (Phase 0 ready)
- Skyriding/dragonriding outside Dragon Isles
- Orgrimmar portal room → Silvermoon (BC-era → Midnight)

---

## Key Files Quick Reference

| What | Where |
|------|-------|
| **This file** (coordination) | `doc/session_state.md` |
| Transmog bug tracker | `memory/transmog-bugtracker.md` |
| Transmog full report | `doc/transmog_implementation_report.md` |
| Transmog behavioral rules | CLAUDE.md → "Transmog UI / Midnight 12.x" section |
| World cleanup plan | `doc/world_db_cleanup_plan.md` |
| Spell audit status | `memory/spell-audit.md` |
| To-do list | `memory/todo.md` |
| Open issues (GitHub gist) | `doc/gist_open_issues.md` |
| Changelog (GitHub gist) | `doc/gist_changelog.md` |
| DB report (GitHub gist) | `doc/gist_db_report.md` |

## Skills Available

| Skill | What It Does |
|-------|-------------|
| `/build-loop` | Iterative build + fix compilation errors |
| `/check-logs` | Read server logs for errors |
| `/apply-sql` | Apply SQL file to a database |
| `/new-sql-update` | Create correctly-named SQL update file |
| `/lookup-spell` / `/lookup-item` / etc. | DB2 lookups |
| `/wrap-up` | End-of-session checklist |

---

## Rules for Multi-Tab Work

1. **Read this file first** in every new tab
2. **Claim your assignment** — update the Active Tabs table before starting
3. **One bug per commit** — don't combine fixes across domains
4. **Don't touch files another tab owns** — check the table
5. **Update this file when done** — move your task to completed, note what changed
6. **Building from Claude Code is allowed** — use `ninja -j32` via Bash (VS IDE also works)
7. **Don't duplicate research** — if a memory file or report covers it, read that instead of re-analyzing source code
8. **Update bug trackers** — after fixing a bug, change its status in the tracker

---

## Recently Completed (for context)

| Session | What | Key Output |
|---------|------|-----------|
| 227 (main) | VoxSniffer Combat Audit v1 | CombatAudit.lua + ProcExpectations.lua + audit_report.py. Gemini audit PASS after 4 HIGH fixes. `5cd63fdd3f` |
| 227 (tab 2) | DB error cleanup + TC TDB backfill | Phase 1-2a cleanup (886K rows), TC TDB INSERT IGNORE (771+433 tables), 5 mismatch fixes, 329 removed items purged, plan doc. `eef19fe221` |
| 224 | Session 222/223 wrap-up + optimization application | 13 skills conditional, FileChanged hook, SubagentStart/ConfigChange hooks, SME handoff prompt. `8f01aa113c` |
| 223 | Claude Code Tier 2 reports (1M tab) | 7 reports (5,550 lines): tool pipeline, swarm, coordinator, hooks, permissions, skills, MCP. 4 audit agents: concurrency, hooks, skills paths, fork mode. 13 skills made conditional |
| 222 | Claude Code internals research + config optimizations | 11 reports (266KB), 1M context enabled, 3 conditional rules, .gitignore optimized (205→15 untracked), 54 memory frontmatter files. Source: `C:/Users/atayl/Desktop/claude-code-source/`. `0916b667c9` |
| 221 | Swift Crusade spell + timestamp hook fix | Custom spell 1900031 (+100% move speed, +200% mounted ground+flight). Timestamp hook statusMessage added for terminal visibility. `0916b667c9` |
| 220 | Bnetserver fix + Chrono Surge spell + DB schema repair | Port 1119 fix, custom spell 1900030 (+250% haste/-75% CD), 3 DB schema fixes (crafting columns/tables for TC sync), duplicate process cleanup. `54d9ef6621` |
| 215 | Angel VA TDIU (21-8940) filing support | Filled PDF (103 XFA fields), draft answers doc, migraine legal analysis (3 decisions), 4 buddy statements (Adam v2 + 3 templates), neurologist letter template, complete action plan, print-ready Item 26 continuation sheet. All in Desktop/Excluded/Angel_VA/. No VoxCore commit |
| 214 | Gemini Pro VoxCore business briefing | 15-doc package (1,440 lines combined). 10 memory + 11 desktop files synthesized. Identity correction for wrong VoxCore. Google ecosystem + Triad-to-Vertex migration mapped. `c690e31568` |
| 185 | Legal filing review + submission package build | 5 FINAL filing packages, 47 evidence subfolders, master checklist, 12 unknown unknowns, 24-claim fact-check. No VoxCore commit (Desktop files) |
| 184 | Case file organization + folder indexing | 40 documents filed, 7 __Master_Index.md files created. `f6796a89a3` |
| 183 | Legal audit + cross-tab integration + MASTER_00 | 14 BLOCKING + 20 WARNING fixes across 6 MASTER docs. Exec summary created. Contact numbers verified. No VoxCore commit (Desktop files) |
| 173 | VoxGM v2.0 spec autonomous review loop | 6 iterations x 5 rounds (30 total). R1-R6. ~50 findings fixed. Packaged to Desktop. `e1e3ad393e` |
| 172 | Community engagement + Reddit outreach | GitHub: responded to 6 commenters, contested #33465, PR contribution for mvanhorn #32755. awesome-claude-code fork submitted. Reddit: 26 threads, 14 comment drafts, 5-day posting plan |
| 171c | 8 claude-code-* repos v1.0.0 | Full audit + fix cycle: em dashes, .gitignore, VoxCore refs, config naming, __pycache__. All 8 repos released on GitHub. enforce.py overbroad match bug fixed |
| 168 | VoxSniffer v1.0.0 | 14-module server data sniffer (62 files, 8,881 lines). 7-round dual ChatGPT review. Source-bound callbacks, nameplate reseeding, dedup-after-envelope. GitHub + AddOns + publishable/ |
| 167 | VoxGM v1.0.0 | 26-file GM control panel (2,700 lines). 9-round review. 6 tabs, minimap button, event parsers. GitHub + AddOns + publishable/ |
| 166 | CreatureCodex v1.0.0 | Creature spell/aura sniffer. 7-round review. C++ hooks + addon + Eluna. install_hooks.py fix, session.py WoW root detection. GitHub + AddOns |
| 123 | auto_parse v3 | 19-module package (2,498 lines). Plugin parser arch, session-aware watcher, alert dedup, HTML dashboard, TOML config, tray icon, crash scanner, packet pipeline. 3 QA + Antigravity audit |
| 121 | VoxPlacer Polish | 4 features (undo 10-deep stack, face-toward, favorites list, minimap button), ghost preview aura (spell 37800), 6 QA fixes. ~1140 lines C++, ~930 lines Lua |
| 120 | NotebookLM Knowledge Base | 97 files in `doc/notebooklm/` (docs, source as .txt, SQL, Lua addons). Evaluated Antigravity IDE, reviewed 12 claude-code issues |
| 119 | Anti-Theater Protocol | Completion Integrity rules in CLAUDE.md. 6 prohibitions, mandatory checklist, 5 memory files updated |
| 118 | LoreWalker TDB Import | 7 SQL files applied, 502K inserts + 7.7K updates, _00_ column bug fixed, QA clean |
| 115b | Transmog Tooling Phase 1 | Created `transmog_common_maps.py`, fixed DT maps in 3 tools (DT 12/14 added, lookup.py wrong numbering fixed), regenerated enriched CSVs for 66263, annotated bridge v3 spec |
| 113 | Transmog Resource Audit | 3-pass QA of all transmog tools/CSVs/bridge. Key: bridge v3 implemented, lookup.py wrong DT numbering, enriched CSVs stale. `doc/transmog_resource_audit.md` |
| 112 | Sniffing Guide Polish | Hub gist cleanup, generic branding, Heads Up section |
| 111 | LoreWalker TDB Analysis | 6-agent sweep, import pipeline ready in `doc/lorewalker_import_prompt.md` |
| 110 | Transmog Master Tab | 8 bugs fixed, 3 QA passes, DT/validator clean, resource audit. `doc/transmog_next_steps.md` |
| 109 | ImageMagick + sniffing docs | Installed IM, updated Midnight priorities + WPP sanitize |
| 108 | Transmog consolidation | Slot ordering fix, sniffing docs tracked |
| 107 | Meta infrastructure | This file, bug tracker, skills, gist updates |
| 106 | Wrap-up | Committed sessions 104-105b work |
| 105b | Transmog DeepDive | `doc/transmog_deepdive_wiki.md`, 4 memory files |
| 104 | Draconic diff + SW | `tools/diff_draconic.py`, 7 phase_area fixes |
| 103 | NPC tooling | `.npc copy` command |
| 102 | Collection unlocks | `.maxrep`/`.maxachieve`/`.maxtitles` |
| 101 | SpellAudit cleanup | Removed 1,842 broken stubs |

---

## GitHub Gists (synced April 4 — session 228)

- DB Report: https://gist.github.com/528e801b53f6c62ce2e5c2ffe7e63e29
- Changelog: https://gist.github.com/4c63baf8154753d2a89475d9a4f5b2cc
- Open Issues: https://gist.github.com/2b69757faa2a53172c7acb5bfa3ad3c4
