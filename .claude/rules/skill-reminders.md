# Proactive Skill Reminders — MANDATORY

**The user should NEVER have to remember to run a slash command.** Remind at the right moment or just run it if unambiguous.

| Trigger | Action |
|---|---|
| "I'm done", wrapping up, conversation winding down | `/wrap-up` — ask or run |
| Server restart, crash, debugging begins | `/check-logs` — just run it |
| Build error pasted | `/parse-errors` — just run it |
| C++ file edited, work complete | Remind: "Ready to build" — use `_build_ps.ps1` or VS |
| Claiming completion on any deliverable | Run `python tools/validate_deliverable.py <path>` — catch hallucination + structure issues |
| Producing case answers / filing prose / briefings with citations | **Use inline-grounded citation format** — every cited path paired with verbatim quoted span: `` `path.md`: "the actual text from the file" ``. Verifies in 1ms via `tools/inline_grounding.py`. 3.25× span-correctness lift over footnote-style citation. Forensically-defensible for legal use (Anthropic Citations API pattern). |
| Scoring citation quality on any output | Run `python tools/citation_scorer.py --batch <input.jsonl> --output <out.json> --judge ollama` — full path-precision + recall + LLM-as-judge span correctness in one shot |
| Verifying inline quotes exist verbatim in source | `python tools/inline_grounding.py verify --quote "..." --path "path/to/file.md"` — fast substring + Unicode-normalized fallback |
| User asks to audit code quality, find bugs, review custom systems | `/code-audit [dir]` — fan out parallel agents |
| About to spawn 2+ parallel sub-agents (Agent tool) for a non-trivial task | **Run `/extra-usage` FIRST** — sub-agents inherit 1M context from parent. Without /extra-usage enabled, ALL parallel sub-agents fail with "Extra usage is required for 1M context" before consuming any tokens. Pain logged 7+ times across sessions 263–278h. |
| Choosing model for sub-agent tasks | **Heuristic**: structured catalog/extraction/classification → Sonnet 4.6 is sufficient and ~5× cheaper. Narrative synthesis / cross-document reasoning / legal-accuracy verification → Opus 4.7. Don't default-spawn Opus when Sonnet suffices — caught session 278h ($150-300 → $25-50 actual when corrected mid-task). |
| SQL file created/edited | `/smartai-check` (if SmartAI) or `/apply-sql` |
| Writing new SQL update | `/new-sql-update` — run for filename |
| Multiple tasks / scope expanding | Suggest tab split (see multi-tab rules) |
| Session start | Auto-read `doc/session_state.md` + `todo.md` |
| Name without ID (spell/item/creature/area) | Run `/lookup-*` to resolve |
| Addon/tool/app approaching "done" state | `/pre-ship` — remind before commit |
| Writing to `tools/publishable/` directory | `/pre-ship` — ask if ready for audit |
| User says "ship it", "release", "v1.0", "zip it up" | `/pre-ship` — run before packaging |
| Working on Case_Reference or legal case files | `/case-status` — run at session start for case work |
| Starting a focused work session on the case/career/finance corpus | `/ex-sme` — primes Claude as SME across the Excluded/ tree |
| Specific question about the case that requires evidence + citations | `/ex-ask "question"` — swarm answer with confidence rating |
| "What should I work on today?" / morning brief | `/ex-posture` — deadlines, urgency, new evidence |
| New file/folder/recording/email arrived | `/ex-absorb <path>` — one-shot ingestion + memory update proposals |
| User asks "is the corpus up to date?" / "what's stale?" | `/ex-status` — health dashboard |
| User explicitly requests corpus refresh (never auto-invoke) | `/ex-refresh [folder]` |
| User asks about a specific person (role/org/all mentions) | `python tools/persons_resolve.py "<name>"` — entity resolve + hits |
| User pastes keyword/phrase to find | Try `python tools/excluded_hybrid_search.py "query"` first — FTS5+vector RRF fusion |
| User asks about an email thread / conversation | `python tools/mbox_thread.py --subject "<term>"` — reply-chain expansion |
| User asks "how good is retrieval" / "regression" | `python tools/quality_probe.py --engine all` — 50-query scoreboard |
| User asks to build/update persons list from data | `python tools/persons_ner_seed.py` — NER sweep, ~50 min |
| User says "ship retrieval improvement" / "compare models" | Run `/ex probe` BEFORE the change, make change, run AGAIN, compare |
| User pastes output from ChatGPT/Gemini/Grok for case | Spawn `case-intake` agent to parse and plan edits |
| User asks "who handles X" or "which lawyer" | `/lane-map` — show legal lane ownership |
| User asks for a summary, brief, or one-pager | `/one-pager [audience]` — generate executive summary |
| User mentions .mbox, Gmail export, email archive | `/mbox-parse` — index and search |
| User mentions deadline, "how many days", ADSCD | `/deadlines` — show countdown |
| User asks to find evidence or verify a claim | `/evidence-xref "claim"` — trace to source |
| User asks to search case files for a name/topic | `/case-search [term]` — search archive |
| User asks to sort/triage/organize files | `/file-sort [dir]` — plan + execute with confirmation |
| User asks to read/ingest/analyze a folder of images | `python tools/ingest_images.py <dir>` — NEVER read images into conversation context |
| User needs to read a .docx file | `/read-doc [path]` — extract text |
| User asks about a specific person in the case | `/person-dossier [name]` — full mention search |
| User asks "who is X", "everything about X", entity lookup | `/kg-query [name]` — instant KG entity resolution (25K entities, 178K mentions) |
| User asks about entity relationships, co-mentions | `/kg-query relations [id]` — graph traversal |
| User asks "what regulations apply" or regulation lookup | `/kg-query --kind regulation` — 3,377 regulations indexed |
| User asks for contradiction check, memory drift, accuracy | `/kg-query scan` — run contradiction scanner |
| User asks about KG status, entity counts | `/kg-query stats` or `/kg-query build` |
| User preparing a filing (DD7050, AFBCMR, NPDB, etc.) | `/filing-prep [type]` — draft with evidence citations |
| User asks "do we have evidence for X" before filing | `/evidence-gap [filing]` — requirements vs archive |
| User asks to update or regenerate the timeline | `/case-timeline [update]` — rebuild from all sources |
| Need to draft/send an email | `/draft-email [recipient + topic]` — plain text, no markdown disasters |
| Session running 30+ min, major topic shift, or heavy context | `/checkpoint [label]` — snapshot state to survive compaction |
| User needs to read ANY document (PDF, DOCX, EML, MSG) | `/read-any [path]` — unified extractor with fallbacks |
| End of wrap-up or user says "what could be better" | `/wrap-up` Step 5 runs the automation retro automatically (writes to `automation-ledger.md` with compounding score + tags); Step 6 builds qualifying quick wins. No separate `/retro` skill — absorbed into wrap-up as of session 273. |
| Same pain point logged 3+ times in `memory/improvements.md` | Auto-escalate to `todo.md` HIGH and build if low-effort |
| Financial planning, income/expense scenarios | `python tools/scenario_calc.py` — scenario comparison tables |
| About to search a large directory for agents | `/index-folder` first, then pass manifest to agents |
| Launching agents that need case/file context | Pre-read `memory/` topic files and pass relevant context in prompt |
| Fresh TDB import or migration completed | `mysql -u root -padmin < sql/RoleplayCore/custom_tables.sql` — recreate custom tables |
| Memory files seem stale, MEMORY.md over 200 lines | `/memory-audit` — check health, find orphans, flag issues |
| Edited settings.json hooks, added/changed hooks or daemon code | `/sync-infra` — check CalmCore parity. Also: `python ~/.claude/hooks/check_hook_sync.py` for quick count |
| Session touches .claude/ infra in either project | `/sync-infra` — drift audit |
| End of session, gists may be stale | `/publish-gists` — check and update changed gists |
| Handing off to another tab or ending complex session | `/handoff [label]` — auto-generate context for next tab |
| DB errors, orphan references, data quality concerns | `/db-lint [db]` — scan for common issues, generate fix SQL |
| Comparing local DB against upstream TrinityCore | `/tdb-diff <table>` — download TDB, diff, generate update SQL |

## Workflow Chains — Suggest Combos When Steps Are Manual

When the user is doing steps from a chain manually, suggest the combo skill instead.

| Pattern Detected | Suggest |
|---|---|
| User creates SQL file, then validates, then applies | `/sql-pipeline <db>` — full lifecycle in one command |
| User runs `/case-status` then `/deadlines` then `/lane-map` | `/case-brief` — all three in one view |
| User runs `/pre-ship` then `/release-gate-fix` then re-audits | `/ship <path>` — audit-fix-reaudit loop |
| User fetches a USAJobs posting then tailors resume | `/apply-job <url>` — fetch + tailor in one command |
| User runs `/desktop-triage` then `/file-sort` | `/triage [dir]` — combined triage + sort with approval gates |
| User runs `/one-pager` then `/draft-email` | Suggest: "Want me to draft the email to send this?" |
| User runs `/filing-prep` then `/evidence-gap` | Suggest: "Want me to check evidence gaps for this filing?" |
| User runs `/tdb-diff` then manually applies the SQL | Suggest: "Want me to apply the generated SQL with `/apply-sql`?" |
| User runs `/build-loop` and server restarts | Auto-run `/check-logs` — always safe, read-only |
| User runs `/ex-status` and stale items appear | Suggest: "Stale items found — run `/ex-refresh` when ready?" (never auto-invoke) |

**Rules:**
- If in doubt, ask. A one-line reminder is cheap; forgetting `/wrap-up` loses work.
- Never skip `/wrap-up` at end of session.
- `/check-logs` is always safe to run proactively — read-only.
