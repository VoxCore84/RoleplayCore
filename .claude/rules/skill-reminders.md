# Proactive Skill Reminders — MANDATORY

> Long form + history: docs/rules-reference/skill-reminders.md

**The user should NEVER have to remember to run a slash command.** Remind at the right moment or just run it if unambiguous.

| Trigger | Action |
|---|---|
| "I'm done", wrapping up, winding down | `/wrap-up` |
| C++ file edited, work complete | Remind "Ready to build" — `_build_ps.ps1` or VS |
| Claiming completion on any deliverable | `python tools/validate_deliverable.py <path>` |
| Case answers / filing prose / briefings with citations | **Inline-grounded citation format** — every cited path paired with a verbatim quoted span: `` `path.md`: "the actual text" ``. Verify via `tools/inline_grounding.py`. |
| Scoring citation quality | `python tools/citation_scorer.py --batch <in.jsonl> --output <out.json> --judge ollama` |
| Verifying a quote is verbatim in source | `python tools/inline_grounding.py verify --quote "..." --path "<file>"` |
| Read-only review or audit agents (Workflow `agentType`, Agent `subagent_type`) | `readonly-reviewer` (tools Read/Grep/Glob by definition). A prose "use only Read/Grep/Glob" ban is advisory: 11 of 95 agents ignored it in s.290. Hash the reviewed tree before and after. |
| Choosing model for sub-agent tasks | Structured catalog/extraction/classification → Sonnet 5. Narrative synthesis / cross-document reasoning / legal-accuracy verification → Opus 5 or Fable 5.1. Don't default-spawn the big model when Sonnet suffices. |
| Multiple tasks / scope expanding | Suggest tab split (see multi-tab) |
| Session start | Auto-read `doc/session_state.md` + `todo.md` |
| Addon/tool/app near "done"; writing to `tools/publishable/`; "ship it"/"release"/"v1.0" | `/pre-ship` before commit or packaging |
| Working on Case_Reference or legal case files | `/case-status` at session start |
| Focused session on case/career/finance corpus | `/ex sme [scope]` (the six `ex-*` wrappers are user-typable only since 2026-09-22; `/ex` is the survivor) |
| Case question needing evidence + citations | `/ex ask "question"` |
| "What should I work on today?" / morning brief | `/ex posture` |
| New file/folder/recording/email arrived | `/ex absorb <path>` |
| "Is the corpus up to date?" / "what's stale?" | `/ex status` |
| User explicitly requests corpus refresh (never auto-invoke) | `/ex refresh [folder]` |
| Keyword search / semantic search / KG / batch extract with no other trigger | `/ex search "query"` (hybrid FTS5+vector); `/rag-search`, `/search-docs`, `/case-search`, `/kg-query`, `/bulk-extract`, `/sme-sweep` are user-typable on demand |
| Question about a specific person (role/org/all mentions) | `python tools/persons_resolve.py "<name>"` |
| User pastes a keyword/phrase to find | `python tools/excluded_hybrid_search.py "query"` first |
| Question about an email thread | `python tools/mbox_thread.py --subject "<term>"` |
| "How good is retrieval" / "regression" | `python tools/quality_probe.py --engine all` |
| Build/update persons list from data | `python tools/persons_ner_seed.py` (~50 min) |
| "Ship retrieval improvement" / "compare models" | `/ex probe` BEFORE the change, make change, run AGAIN, compare |
| User pastes ChatGPT/Gemini/Grok output for case | Spawn `case-intake` agent |
| "Who handles X" / "which lawyer" | `/lane-map` |
| Asks for a summary, brief, or one-pager | `/one-pager [audience]` |
| Mentions .mbox, Gmail export, email archive | `/mbox-parse` |
| Mentions deadline, "how many days", ADSCD | `/deadlines` |
| Find evidence or verify a claim | `/evidence-xref "claim"` |
| Search case files for a name/topic | `/case-search [term]` |
| Sort/triage/organize files | `/file-sort [dir]` — plan + execute with confirmation |
| Read/ingest/analyze a folder of images | `python tools/ingest_images.py <dir>` — NEVER read images into conversation context |
| Read any doc type (PDF, DOCX, EML, MSG, TXT) | `/read-any [path]` (`/read-doc` retired 2026-09-22 — strict subset) |
| Asks about a specific person in the case | `/person-dossier [name]` |
| "Who is X" / entity lookup / relations / regulations / KG stats | `/kg-query [name]`, `relations [id]`, `--kind regulation`, `stats`, `build` |
| Contradiction check, memory drift, accuracy | `/kg-query scan` |
| Preparing a filing (DD7050, AFBCMR, NPDB) | `/filing-prep [type]` |
| "Do we have evidence for X" before filing | `/evidence-gap [filing]` |
| Update or regenerate the timeline | `/case-timeline [update]` |
| Draft/send an email | `/draft-email` — plain text, no markdown disasters |
| Session 30+ min, major topic shift, heavy context | `/checkpoint [label]` |
| End of wrap-up / "what could be better" | `/wrap-up` Step 5 runs the automation retro (writes `automation-ledger.md` with compounding score + tags); Step 6 builds qualifying quick wins. No separate `/retro`. |
| Same pain point logged 3+ times in `memory/improvements.md` | Auto-escalate to `todo.md` HIGH; build if low-effort |
| Financial planning, income/expense scenarios | `python tools/scenario_calc.py` |
| About to search a large directory for agents | `/index-folder` first, pass manifest to agents |
| Launching agents needing case/file context | Pre-read `memory/` topic files, pass in prompt |
| Fresh TDB import or migration completed | `mysql -u root -padmin < sql/RoleplayCore/custom_tables.sql` |
| Memory files stale, MEMORY.md over 200 lines | `/memory-audit` |
| Hook daemon needs a restart (after editing `hook_daemon.py`) | `pwsh -File tools/daemon_restart.ps1` — never `pythonw` from Bash or `Start-Process -Wait` (both hang the tool) |
| Edited settings.json hooks, added/changed hooks or daemon code, or any `.claude/` infra | `/sync-infra` drift audit + CalmCore parity. Quick count: `python ~/.claude/hooks/check_hook_sync.py` |
| End of session, gists may be stale | `/publish-gists` |
| Handing off to another tab, ending complex session | `/handoff [label]` |
| Claiming a token/context saving, or before/after any `.claude/` config change | `python tools/cc_context_capture.py --label <x> [--diff <prev>]` — headless /context TOTAL is the only valid evidence |
| Removing/renaming any env var or settings key | `python tools/cc_env_check.py [--also NAME]` — 0 hits in claude.exe = dead/misnamed; undocumented ≠ dead |
| Skills listing cost/usage (`/skill-doctor` is flag-gated here) | `python tools/skill_audit.py --out <report.md>` |

## Workflow Chains — Suggest Combos When Steps Are Manual

| Pattern Detected | Suggest |
|---|---|
| `/case-status` then `/deadlines` then `/lane-map` | `/case-brief` |
| `/pre-ship` then `/release-gate-fix` then re-audit | `/ship <path>` |
| Fetches a USAJobs posting then tailors resume | `/apply-job <url>` |
| `/desktop-triage` then `/file-sort` | `/triage [dir]` |
| `/one-pager` then `/draft-email` | "Want me to draft the email to send this?" |
| `/filing-prep` then `/evidence-gap` | "Want me to check evidence gaps for this filing?" |
| `/ex status` and stale items appear | "Stale items found — run `/ex refresh` when ready?" (never auto-invoke) |

**Visibility note (2026-09-22):** measured on 2.1.278, `skillOverrides` visibility states (`name-only`, `user-invocable-only`, even `off`) do not reduce total per-turn context — `/context` only re-buckets the tokens — so every non-WoW command stays fully listed. Turned-off WoW-era commands (lookup-*, apply-sql, check-logs, build-loop, …) plus `read-doc` and `session-start` return a skillOverrides error in VoxCore; their rows are in the reference file.

**Rules:** If in doubt, ask — a one-line reminder is cheap. Never skip `/wrap-up` at end of session.
