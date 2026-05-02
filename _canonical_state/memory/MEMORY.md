# VoxCore Project Memory

> **Non-WoW workspace** as of 2026-04-09. Houses legal case work, career/finances/brand/Ethical AI, and case-processing tooling (mbox, OCR, RAG, SME sweep, JD migration). Source: `C:\Users\atayl\VoxCore\`, repo: `VoxCore84/VoxCore-legacy`. **WoW server work lives in CalmCore** (`C:\Users\atayl\CalmCore\`) — see split plan at `AI_Studio/Reports/voxcore_calmcore_split.md`. Shared infrastructure (MySQL runtime, wago/, ExtTools/, MCP servers) still physically lives in this tree but is functionally CalmCore's — do not treat as VoxCore work.

## Session Routing — Read the Right Files First

| If working on... | Read these first |
|------------------|------------------|
| Legal/case work | [case-status](case-status.md), [filings](case-filings-tracker.md), [contacts](case-contacts.md), [IDES](ides-process.md) |
| Case evidence | [part1](case-evidence-index-part1.md), [part2](case-evidence-index-part2.md), [part3](case-evidence-index-part3.md), [emails](case-emails-index.md) |
| MH records (extracted) | [mh-records](mh-records-extracted.md) — 64 MHS Genesis notes, PTSD consistent, PCL-5 57-72, NARSUM pending FL4 |
| Angel VA benefits | [angel-va](angel-va.md) |
| Career / job search | [user-profile](user-profile.md), [career-package](career-package.md), [resume-package](resume-package.md) |
| Acquihire track (post-Aug 2026) | [voxcore-acquihire-track](voxcore-acquihire-track.md) — Path 6 plan, Tier 1 targets, builder framing, JAG sequencing. Source: `AI_Studio/Reports/mbox_voxcore_arch/SYNTHESIS.md` |
| Resume evidence (auto-built per session) | [resume-evidence](resume-evidence.md) — STAR-format bullets ready to paste, written by `/wrap-up` Step 4 |
| Finances | [finances](finances-overview.md) |
| Desktop unsorted | [needs-sorted](needs-sorted-inventory.md) |
| C++ / spells / DB | [db-schema](db-schema-notes.md), [server-config](server-config.md), [build-env](build-environment.md) |
| Addons / shipping | [addon-checklist](addon-building-checklist.md), [completed](completed-projects.md) |
| Business / brand | [brand](brand-and-business.md), [revenue](brand-expansion-revenue.md) |
| Ethical AI research | [ethical-ai-research](ethical-ai-research.md) |
| Triad / AI systems | [architecture](system-architecture-snapshot.md), [skills](skills-and-automation.md), [cowork](cowork-setup.md) |
| Local AI / Ollama / RAG | [local-ai-stack](local-ai-stack.md) |
| Excluded/ KB stack (retrieval, /ex-*) | [excluded-kb-stack](excluded-kb-stack.md), [open-items](excluded-kb-open-items.md) — `/ex status`, `/ex ask` |
| Document SME sweeps (any folder) | [sme-sweep-infrastructure](sme-sweep-infrastructure.md) — `/sme-sweep <folder>` |
| Audio evidence (45+ files, transcribed) | [case-audio-recordings](case-audio-recordings.md) — `/rag-search` with `--doc-type transcribed` |
| Claude Code internals | [cc-internals](claude-code-internals.md), [optimization](claude-code-optimization.md) |
| Common errors/pitfalls | [common-errors](common-errors.md) |
| Automation tracking + compounding score | [automation-ledger](automation-ledger.md) — what we built per session, pain→fix mapping, tag-based compounding score. Supersedes [improvements](improvements.md) (read-only history) as of session 273 |
| Feedback: MCP restart pain | [feedback](feedback_mcp_restart_pain.md) — cache expensive init, batch fixes into one restart |
| Feedback: SME/master file quality | [feedback](feedback_sme_master_files.md) — ask for standard first, verify agents, bake paths into prompts |
| Feedback: Calibration overfit + judge calibration | [feedback](feedback_calibration_overfit.md) — held-out test sets only; always state judge model. Source: 2026-05-02 (0% calib → 30% held-out) |
| Monday HAF call (13 Apr 2026) | [haf-call](project_haf_call_13apr2026.md) — time-bounded, delete after follow-ups |
| Migration (TC upstream) | [migration](migration-project.md) |
| Sniffers + OpenClaw backlog | [backlog](project_sniffer_openclaw_backlog.md) — cross-pollinate VoxSniffer/CalmSniffer, find OpenClaw use case or kill |
| All topic files | [topic-index](topic-index.md) |

## P0 — USE THE TRIAD

**You have API access to ChatGPT and Gemini. USE THEM.**

| Trigger | Action | Script |
|---------|--------|--------|
| New feature / architecture | ChatGPT generates spec | `python tools/api_architect/run_architect.py --prompt "..."` |
| Spec needs review | ChatGPT reviews | `python tools/ai_studio/chatgpt_bridge.py --file SPEC.md` |
| Implementation done | Gemini audits | `python tools/ai_studio/orchestrator.py` |

Exceptions: bug fixes, log parsing, build-loop, cleanup, simple CLI ops.
Review cycle: `review_cycle.py` — parallel Phase 1 (3 reviewers) then verify then seal. Details: [architecture](system-architecture-snapshot.md)

## Legal Case — Capt Adam J. Taylor

ADSCD: **10 Aug 2026**. Case files: `C:/Users/atayl/Desktop/IMPORTANT DOCS/Case_Reference/` (26 folders, 1,760 files as of 2026-04-08).
Directive: "No more analysis. FILINGS that create statutory clocks."
Status: **HAF/A1ZA ENGAGED — GO ASSIGNED, SECRETARIAT BRIEFED (Apr 13).** 2hr call with Amy Little. Thursday follow-up. DCSA SIR due ~Apr 15 (Tolin handling, confirmation requested). DHA appeal ACTIVE (Apr 2026 panel). NARSUM PTSD DOWNGRADED (five-alarm fire). Angel TDIU FILED ~Apr 1.
Full details: [case-status](case-status.md) | [filings](case-filings-tracker.md) | [contacts](case-contacts.md) | [evidence](case-evidence-index-part1.md)

## Behavioral Directives (always apply)

**Legal Accuracy**: All case output 100% accurate. Cite exact statutes. Distinguish known/told/documented. Never fabricate.
**Anti-Theater**: Never claim completion without tool output. QA must be falsifiable. Partial = say partial. Full rules: CLAUDE.md.
**Research Persistence**: All findings to persistent files before moving on. Reports to `AI_Studio/Reports/`, state to `memory/`.
**Brutal Honesty**: No hype on money/business/career. Proven vs speculative. "I don't know" beats unsupported confidence.

## User Preferences

- **Claude Code for everything** — engineering, business, real-life, legal. No disclaimers
- **Auto-accept**: `git` and `gh` commands
- **End-of-session**: (1) commit/push? (2) memory update?
- **Always propose parallelism** — agents, subagents, worktrees
- **Multi-tab mandatory** — CLAUDE.md triggers for 2+ subsystems
- **Discord**: Discord markdown, minimal blank lines, no tables, no triple-backtick
- **Proactive skill reminders** — user should NEVER have to remember a slash command
- Comfortable with direct SQL, cmake, elevated terminals
- wow.tools.local: `http://localhost:5000` (build 66263). Wago CSVs at **66709**
- WoW client: `C:\WoW\_retail_\` (retail 12.0.1.66709). DBC extracted via directory junctions to both build dirs.
- AI budget: ~$680-800/mo — [ai-subscription-audit](ai-subscription-audit.md)

## Build

`ninja -j32` from Bash (allowed). VS 2026, OpenSSL 3.6.1 (`lib/VC/x64/MD/`). CMake presets. Details: [build-env](build-environment.md)

## DB Schema Quick-Ref

- `hotfixes.spell_name` (composite PK) + `world.serverside_spell` (col `Id` lowercase d)
- `creature_template_spell`: cols `CreatureID`, `Index`, `Spell`
- MCP MySQL can't parse `schema.table` — use `voxcore-db` MCP instead (explicit `database` param)
- **MySQL**: UniServerZ 8.2.0 at `C:\Users\atayl\VoxCore\runtime\UniServerZ\core\mysql\` (port 3306, root/admin). MySQL80 service DISABLED. Tuned for NVMe (4GB InnoDB pool)
- **DB Base**: LoreWalkerTDB (CaptainCore Apr 3 2026 dump) — 690K spawns, 296K SmartAI, 48K quests + VoxCore patches on top
- Full schema: [db-schema](db-schema-notes.md)

## Key Procedures

- **Bulk images**: `python tools/ingest_images.py <dir>` — NEVER read images into context
- **Custom spells**: hotfix tables (`spell_name`, `spell_misc`, `spell_effect` + `hotfix_data`). NOT `serverside_spell` if in `sSpellNameStore`. Range: 1900003+
- **Gossip menus**: `GossipOptionNpc::None` for scripted. `Taxinode` opens taxi map
- **SQL naming**: `sql/updates/<db>/master/YYYY_MM_DD_NN_<db>.sql`
- **Build bump**: (1) auth SQL (build_info + auth_keys + realmlist), (2) `wago_common.py` CURRENT_BUILD, (3) re-download Wago CSVs (`--build` explicit!), (4) mapextractor.exe → copy dbc/cameras/gt to both build dirs, (5) hotfix repair, (6) update Python refs. See [common-errors](common-errors.md) for pitfalls.

## Hardware

Ryzen 9 9950X3D 16C/32T, 128GB DDR5, RTX 5090 32GB, Samsung 9100 PRO 4TB (boot, PCIe 5.0 — 14.6/12.8 GB/s seq R/W) + 980 PRO 2TB (secondary). BIOS 2103. Full specs: [infrastructure](infrastructure-layout.md)

## Active Systems

| System | Status | Link |
|--------|--------|------|
| Arcanum Wiki | 537 files, Johnny Decimal XXX.YYY, ALL 22 REPORTS | `doc/arcanum/`, [claude-code-internals](claude-code-internals.md) |
| Warlock Pipeline | Phase 5 DONE, 38/199 handled + 156 TC-native (97%) | `tools/warlock/`, `doc/classes/warlock/` |
| Spell Audit | 13 RED / 84 YELLOW | [spell-audit](spell-audit.md) |
| Companion Squad | IN PROGRESS | [companion](companion-system.md) |
| Migration | BUILD 66709 COMPLETE | [migration](migration-project.md) |
| Hook Daemon | v1.3.0, 24 routes, 38 hooks (4 types), chain handlers | `.claude/hooks/hook_daemon.py` |
| Auto-Parse | DEPLOYED v3+ | [completed](completed-projects.md) |
| Release Gate | DEPLOYED | [addon-checklist](addon-building-checklist.md) |
| CreatureCodex | v3.0, needs test | [completed](completed-projects.md) |
| VoxSniffer | v1.0, needs test | [completed](completed-projects.md) |
| VoxGM | v1.0.0 RELEASED | [completed](completed-projects.md) |
| DraconicBot | v3.1, needs deploy | [completed](completed-projects.md) |
| Tor Army | v3.2, 230K/hr | [completed](completed-projects.md) |
| MCP Servers | DEPLOYED (db+server+arcanum+docs-rag) | [completed](completed-projects.md) |
| docs-rag MCP | DEPLOYED — 6 tools, ChromaDB+Ollama semantic search | `tools-dev/docs-rag/` |
| Timestamp Hook | Daemon handler (was standalone) | `.claude/hooks/hook_daemon.py` |
| Transmog | ARCHIVED | `doc/archive/transmog.md` |
| Local AI Stack | 6 LAYERS LIVE (Ollama+WebUI+RAG+MCP), OpenClaw shut down | [local-ai-stack](local-ai-stack.md) |
| Excluded KB Stack | DEPLOYED — 6-layer doc intelligence, 7 /ex-* commands, 64% hybrid baseline | [excluded-kb-stack](excluded-kb-stack.md) |
| ExcludedDaemon | Phase A+B done, tray UI deferred | [excluded-kb-stack](excluded-kb-stack.md) |

## DevOps Pipeline

- **Start**: `tools/shortcuts/start_all.bat` (MySQL, pending SQL, bnet, world, Arctium, auto_parse)
- **Stop**: `tools/shortcuts/stop_all.bat` (kill, sweep, PacketLog, Claude handover)
- **SQL drop zone**: `sql/updates/pending/*.sql` — auto-applied at boot
- **Session Brief**: `PacketLog/_Session_Brief.md` — read FIRST after play session

## Coordination

- **Central Brain**: `AI_Studio/0_Central_Brain.md` — read at start. No longer auto-updated by `/wrap-up` (cut as of session 273 — Cowork reads memory files via the bridge). Update manually when major Triad context shifts.
- **Tab sync**: `doc/session_state.md`
- **Cowork**: Claude Desktop VM, 5 tasks — [cowork](cowork-setup.md)
- **AI Studio**: `AI_Studio/` — Inbox, Active_Specs, Reports/Audits, Archive
- **Gists**: DB Report `528e801b`, Changelog `4c63baf8`, Issues `2b69757f`

## Finances & Business

Combined ~$8,732/mo in, ~$10,100/mo out (**$1,370/mo deficit**). Separation Aug 10.
Off-duty employment form needed. Market unproven. Details: [brand](brand-and-business.md), [finances](finances-overview.md)
User profile: [user-profile](user-profile.md) — LCSW, 11yr military, ADSCD Aug 2026

## Recent Work

See [recent-work.md](recent-work.md) for session log (auto-updated via /wrap-up).
