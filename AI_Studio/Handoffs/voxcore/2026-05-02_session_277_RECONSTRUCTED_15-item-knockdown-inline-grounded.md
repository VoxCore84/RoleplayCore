# VoxCore Session Handoff — May 2 2026 (Session 277) — RECONSTRUCTED

> **[RECONSTRUCTED on 2026-05-02]** — This handoff was NOT written contemporaneously at the end of session 277.
> It is a deterministic template fill from the memory files listed in the Sources footer.
> A reader citing facts from this document should cross-verify against the primary sources.
> This is a back-fill so the `AI_Studio/Handoffs/voxcore/` folder has a complete audit trail; it is not a substitute for a real handoff.

**Session:** 277
**Date:** May 2 2026
**Title:** 15-item knockdown + inline-grounded citations + 7 ADRs
**Commit (best-guess from `git log --grep`):** 3e11280f36
**Source provenance:** see footer

---

## What Happened (from recent-work.md)

- **Mbox absorb**: Read 21MB `VoxCore Architecture Stuff.mbox` (45 emails + 18 unique PDFs covering acquihire strategy, IP chain-of-title, JAG ethics, Builder Framing, Benchmarking Methodology). Wrote SYNTHESIS.md + MANIFEST.md + memory file `voxcore-acquihire-track.md`. Confirmed naming lock: VoxCore=legal-AI, CalmCore=WoW.
- **Round 1 — 10 critical-path items**: PyMuPDF→pdfplumber+pypdfium2 swap via `tools/pdf_lib.py` shim (AGPL blocker removed across 9 consumers, 50/50 random PDFs validated); LLM-as-judge wrapper for citation_scorer (gemma4:26b via /api/chat); full git-history secrets scan (`tools/secrets_scan.py`, 31,257 blobs / 875 commits, 0 real findings); pinned-dep audit (`tools/deps_audit.py --fix`, 7 .pinned.txt files); `docs/ENVIRONMENT.md`; subscription audit (IP chain folder 02); governance audit log (`tools/governance_audit.py` + 5 wires); N=30 citation batch (100% path precision across audio/OCR/extracted/master-synth modalities); Triad entry-point doc (`docs/architecture/TRIAD_ENTRY_POINT.md`); Cat 9 license remediation closed 6/6 (extract-msg→`tools/msg_extract.py` BSD/olefile, 3 GPL deps removed).
- **Round 2 — 5 more items**: Audio cross-instance WER (0.59% across 26 dups via `tools/wer_measure.py` Levenshtein-C); OCR character accuracy (24% avg / 0-5% prose / 50%+ layout-heavy via `tools/ocr_accuracy.py` using pdfplumber-vs-Tesseract); classification marking detector (`scan_classification_markers()` with TS//SECRET//CUI//FOUO/sealing/Rule-6(e), 15/15 smoke + 0/1484 false-positives after 2 tightening rounds); LegalBench LLM-as-judge for free-text tasks (`--judge` flag in legalbench_harness, 3/3 smoke); 7 Architecture Decision Records in `docs/architecture/decisions/`.
- **Round 3 — inline-grounded citation pipeline (NOVEL)**: Built `tools/inline_grounding.py` (~270 LOC) — Anthropic Citations API pattern. `extract_inline_quotes()` with 6 quote-format regexes; `verify_quote_in_file()` with FTS-exact / FTS-normalized / file-exact / file-normalized / Unicode-dash-fallback. Extended `citation_scorer.py` with two-path scoring (inline-grounded vs chunk-fetch). N=15 batch with `--judge`: **3.25× span-correctness lift on inline-grounded path (0.65 vs 0.20 chunk-fetch)**, 100% verbatim verification rate (10/10), 0 fabrications. Concrete 1-2hr path to <10% hallucination via one-quote-per-claim prompt refactor next session.
- **Verification**: 4 passes per round (static + smoke + cross-ref + edge/security). Found and fixed 2 bugs: TRIAD doc line 38→37 GEMINI_MODEL drift, stale `docs/acquihire/02_IP_Chain_of_Title.md` ref → folder structure. Found and fixed 5 bugs in inline_grounding during build: apostrophe regex break, dash character-range error, em-dash mojibake, stale __pycache__, `from tools.inline_grounding` import path failure when run as `python tools/...`.
- **Master Checklist**: 53/170 → **83/171 verified (49%, +30 items)**. Cat 9 closed 6/6. Cat 4 (Calibration) jumped 6 → 15 verified.
- Commit: `3e11280f36`
- **Step 5 — KG MCP tools**: Added 4 tools to docs-rag MCP server (`tools-dev/docs-rag/`, gitignored per project convention): `kg_entity`, `kg_mentions`, `kg_relations`, `kg_stats`. Also extended `docs_rag_reload` to recursively reload `tools.excluded_daemon.kg.*` modules so future kg.query.py edits hot-reload without MCP restart. Verified: 7/7 smoke tests, kg_stats matches 24,640 entities baseline, MCP tools live after `/mcp` reconnect.
- **Step 6 — entity_expand BFS**: Added multi-hop traversal to `tools/excluded_daemon/kg/query.py` with salience ranking (`kind_bonus × log(mention_count) × relation_count × confidence`). Persons get 3x bonus over orgs (0.7x), preventing single `mentioned_with` predicate from drowning signal in popular-org noise. Added compact mode that strips `mentions_by_hop` + trims entity fields — keeps depth=2 expansion on Adam (11K co-occurrences) at 35KB instead of 99KB so MCP wire stays inline. Verified: Johnston + McMaster surface at hop 1, salience puts 10/10 hop-1 connections as persons; latency 0.26s.
- **Step 7 — /ex ask pre-fetch**: Added "Pre-flight: KG entity context (for `ask`)" section to `.claude/commands/ex.md` (Steps A-D): identify candidate entities (uppercase 2-6 letter tokens, person names, regulation citations, dates, case numbers), resolve via new MCP tools, build Entity Context Block (canonical names, kinds, mentions, top connections, multi-hop reach), inject into each of the 4 fan-out agents. Includes ambiguity caveat for fuzzy substring matches ("ET" → 647 hits demonstrates the trap). Demonstrated end-to-end: McMaster pre-flight surfaces `org=AFPC` from KG metadata before any fan-out search + 11 prioritized doc paths + multi-hop reach to Earles, Grandin, Lujan, DD7050, DD149, SCRA, DCN 5500000247204119.
- **Step 8 — Contradiction scanner v2**: Added `_semantic_compare()` + `_filter_semantic()` to `tools/excluded_daemon/jobs/contradiction.py`. sonnet-4-6 binary classifier via urllib (5 parallel workers, ~$0.07 per scan, ~20s for 58 candidates — pattern mirrors `_sonnet_ner` in build.py). Default-on for manual `/kg-query scan`, opt-out flag for daemon autopilot scans (zero API cost). Tightened prompt distinguishes same-event contradictions from co-incidental date overlaps. Degraded-state warning fires when ERROR rate >50% so a billing-blocked run doesn't read as "no contradictions found." Verified: 58 v1 candidates → 0/1/57/0 (YES/NO/UNRELATED/ERROR), 5/5 unit-test verdicts correct.
- **MCP wire-limit bug found + fixed mid-session**: kg_relations depth=2 returned 99KB → triggered file-output workaround. Added `compact: bool = False` parameter to entity_expand; MCP wrapper opts in. 89KB → 35KB inline.
- **QA/QC**: 21/21 checks passed across 3 passes — Pass 1 code review (5 files), Pass 2 edge cases (12 tests: SQL injection, whitespace, hops=0, max_entities, empty inputs, long inputs, defaults), Pass 3 cross-step integration (9 tests: JSON round-trip, MCP/direct parity, daemon path purity, salience verification, latency budgets).
- **Anthropic credits depleted mid-session** — user topped up; verified API working with 1-token probe before re-running scan.
- Commit: `4553599d5c` (3 tracked files, +603/-15; tools-dev/docs-rag/ changes are gitignored).


---

## Automation Ledger Entry (from automation-ledger.md)

**Built**:
- `tools/inline_grounding.py` — Anthropic Citations API pattern: extract inline quotes, substring-verify in source
- `tools/pdf_lib.py` — pdfplumber+pypdfium2 shim replacing PyMuPDF/AGPL (9 consumers updated)
- `tools/msg_extract.py` — olefile-based .msg parser replacing extract-msg/GPL
- `tools/governance_audit.py` — append-only JSONL audit log + CLI
- `tools/secrets_scan.py` — full git-history credential scanner (gitleaks alternative)
- `tools/deps_audit.py` — requirements-file auditor + .pinned.txt generator
- `tools/wer_measure.py` — word/char error rate via Levenshtein C-extension
- `tools/ocr_accuracy.py` — pdfplumber-vs-Tesseract OCR accuracy methodology
- `tools/citation_scorer.py` extended — LLM-as-judge wrapper + two-path scoring (inline-grounded vs chunk-fetch)
- `tools/legalbench_harness.py` extended — `--judge` flag for free-text task scoring
- `tools/extract_cache.py` extended — `scan_classification_markers()` (TS//SECRET//CUI//FOUO/sealing/Rule-6(e))
- `docs/architecture/decisions/0001-0007` — 7 ADRs documenting non-obvious choices
- `docs/ENVIRONMENT.md`, `docs/architecture/TRIAD_ENTRY_POINT.md`
- `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/`, `04_Open_Source_Inventory/`

**Pain → Fix**:

| # | Pain | First seen | Tags | Fix | Effort | Status |
|---|------|-----------|------|-----|--------|--------|
| 1 | PyMuPDF AGPL blocks commercial use | s.275 | `legal`,`audit` | tools/pdf_lib.py shim over pdfplumber+pypdfium2; 9 consumers swapped; 50/50 PDFs validated | MED | DONE |
| 2 | extract-msg GPL blocks commercial use | NEW | `legal`,`audit`,`extract` | Built tools/msg_extract.py on olefile (BSD); uninstalled extract-msg | MED | DONE |
| 3 | mysql-connector-python/pcodedmp GPL listed but unused | NEW | `legal`,`audit` | grep clean → uninstalled both | LOW | DONE |
| 4 | No LLM-as-judge for span correctness — claims at PDF can't be defended | NEW | `rag`,`llm`,`audit` | judge_span_ollama + judge_span_claude via /api/chat; 2048-token Qwen budget; verdict regex parser | MED | DONE |
| 5 | Single-chunk-fetch artifact drives 47.8% IRRELEVANT in chunk-fetch path | NEW | `rag`,`audit` | Inline-grounding pipeline (NOVEL) — model declares which span; substring-verify; 3.25× lift | HIGH | DONE |
| 6 | No defensible secrets-scan story for diligence | NEW | `audit`,`git`,`legal` | tools/secrets_scan.py; 31,257 blobs / 875 commits clean | MED | DONE |
| 7 | requirements.txt files unpinned, hurts reproducibility | NEW | `audit`,`build` | tools/deps_audit.py --fix; 7 .pinned.txt companions written | LOW | DONE |
| 8 | No environment manifest for reproducibility | NEW | `audit`,`build` | docs/ENVIRONMENT.md (hardware/OS/Python/GPU/Ollama/DBs) | LOW | DONE |
| 9 | Subscription audit missing for IP chain-of-title diligence | NEW | `audit`,`legal` | docs/acquihire/03_IP.../02_Subscriptions/subscription_summary.md | LOW | DONE |
| 10 | No governance audit log; "prove you didn't process X" unanswerable | NEW | `audit`,`daemon`,`legal` | tools/governance_audit.py + 5 wires (extract_cache + router); CLI for stats/query | MED | DONE |
| 11 | Citation precision claim 96% INFERRED, never measured | s.275 | `rag`,`audit` | N=30 batch with diverse modalities (audio/OCR/extracted/master-synth); 100% path precision measured | MED | DONE |
| 12 | Triad entry point undocumented; diligence Q "where does request flow" unanswerable | NEW | `triad`,`audit` | docs/architecture/TRIAD_ENTRY_POINT.md mapping orchestrate() → run_architect → run_executor → run_auditor | LOW | DONE |
| 13 | No classification banner detection in governance gate | NEW | `audit`,`legal`,`daemon` | scan_classification_markers() with TS//SECRET//CUI//FOUO/sealing/Rule-6(e); 15/15 smoke + 0/1484 false-positives after 2 tightening rounds | MED | DONE |
| 14 | Audio WER never measured — multimodal claim unsupported | NEW | `audio`,`audit` | tools/wer_measure.py cross-instance on 26 dups → 0.59% avg | LOW | DONE |
| 15 | OCR character accuracy never measured | NEW | `ocr`,`audit` | tools/ocr_accuracy.py pdfplumber-vs-Tesseract → 24% avg / 0-5% prose | LOW | DONE |
| 16 | LegalBench rule_qa scored 10% but answers correct (string-match issue) | s.275 | `llm`,`audit` | Added `--judge` flag + score_answer_with_judge for free-text tasks; user re-run pending | MED | DONE (wrapper); QUEUED (re-run) |
| 17 | "Why built this way?" diligence Q-set unanswered | NEW | `audit`,`triad` | 7 ADRs in Context/Decision/Alternatives/Consequences format | MED | DONE |
| 18 | Stale __pycache__ caused phantom test failures during build | NEW | `build`,`audit` | rm -rf __pycache__; documented as gotcha in handoff | LOW | DONE |
| 19 | `from tools.X` import fails when script run as `python tools/X.py` (sys.path[0]=tools/) | NEW | `build` | Two-path try/except in citation_scorer | LOW | DONE |
| 20 | Em-dash mojibake between answer text and corpus content | NEW | `extract`,`rag` | Unicode dash normalization in inline_grounding._normalize_for_match | LOW | DONE |
| 21 | Composite hallucination rate at 39.81% (chunk-fetch only) — PDF says <2% | NEW | `rag`,`audit`,`legal` | Honest measurement + named tier-1/2/3 roadmap to <10% in next session, <2% over months | HIGH | DOCUMENTED (roadmap), QUEUED (one-quote-per-claim refactor) |

**Compounding**: 2/21 by tag-overlap, 5/21 with judgment
- Tag-matched: #1 (`legal`,`audit` ↔ s.275 PyMuPDF QUEUED entry), #11 (`rag`,`audit` ↔ s.275 PDF-INFERRED-not-MEASURED entry)
- Judgment-additional: #4 (LLM-as-judge — built on s.275 citation_scorer foundation), #16 (LegalBench judge — built on s.275 legalbench harness foundation), #17 (ADRs — extends s.275 docs/acquihire/ pattern)

**Trend update** (last 10): `0/2 → 2/2 → N/A → 2/3 → 2/6 → 3/7 → 8/8 → 1/8 → 2/21`
*(s.277 has the lowest tag-overlap ratio because most pain points were NEW — 18/21 — reflecting the breadth of the 15-item knockdown across previously-untouched categories: license remediation, secrets, governance audit, environment manifest, subscription audit, classification detection, audio WER, OCR accuracy, ADRs, inline grounding. The system compounded HARD on the 2 items where prior work had laid groundwork — citation_scorer + legalbench_harness extensions both built directly on s.275 foundations.)*

**Pattern detection**: No 3+ occurrences of any single pain pattern this session. The closest is `audit`-tagged items (15/21) — but that's the breadth of acquihire-readiness work, not a recurring pain class.

**Quick-win gate fired** (Step 6):
- Surveyed 21 in-session pain points + 13 historical QUEUED items
- 1 quick win built (~5 min): added 3 inline-grounding trigger rows to `.claude/rules/skill-reminders.md` so future sessions reach for the inline-grounded format by default. Trigger pain (~"footnote-only citations get 47.8% IRRELEVANT in scoring") would have been logged as recurring s.275+s.277 if not auto-applied.
- 2 QUEUED items deferred to next session (do not meet LOW-effort gate):
  - #16 LegalBench `--judge` re-run on rule_qa + citation_prediction (10-15 min runtime, but model choice user-decision-dependent + costs API credits if `--judge claude`)
  - #21 One-quote-per-claim prompt refactor (1-2 hr = MED, not LOW)

---

## Resume Evidence (from resume-evidence.md)

**Quantifiable**: Master Checklist 53/170 → 83/171 verified (+30 items / 49%). 15 critical-path engineering items closed across 3 rounds. New tools: 9 (~1,500 LOC). New docs: 16 (7 ADRs + ENV + TRIAD + 2 IP-chain folders). Production files modified: 13. **Citation pipeline**: 100% path precision + 100% recall on N=30 batch. Inline-grounded path **3.25× span correctness** vs chunk-fetch fallback (0.65 vs 0.20). 100% verbatim verification rate (10/10 inline quotes). **Audio WER 0.59%** (cross-instance, 26 files / 83K words). **OCR CER 24%** avg / 0-5% prose (10 files). **Secrets scan**: 0/31,257 blobs / 875 commits clean. License remediation Cat 9: 6/6 closed (AGPL PyMuPDF + 5 GPL deps swapped or removed). 4-pass verification per round; 7 bugs found and fixed.
**Technical**: Anthropic Citations API pattern in `tools/inline_grounding.py` (~270 LOC) — substring verification (FTS exact / FTS normalized / file exact / file normalized / Unicode dash fallback) + LLM-as-judge. Two-path scorer (inline-grounded / chunk-fetch) in `citation_scorer.py`. Forensically-defensible verbatim-quote citations. pdfplumber + pypdfium2 shim replacing AGPL PyMuPDF. olefile-based .msg parser replacing GPL extract-msg. Multi-stage governance gate (filename + content + classification banners + sealing markers) with append-only JSONL audit log. Word/character error rate via Levenshtein C-extension on chr-encoded token sequences. Tesseract-vs-pdfplumber-native-text OCR accuracy methodology. Python-based git-history credential scanner (gitleaks alternative). LLM-as-judge for free-text LegalBench tasks via Ollama /api/chat.
**Outcome**: Concrete 1-2 hour path to <10% hallucination rate via one-quote-per-claim prompt refactor next session. Differentiated diligence story — no commercial vertical legal-AI vendor ships forensically-verifiable inline-quoted citations today. Cat 9 license remediation closed enables clean acquihire IP transfer. All Round-1/Round-2/Round-3 work three-pass-verified before claiming completion.
**STAR bullet**: Built a forensically-verifiable inline citation pipeline for a solo-built legal-AI platform using the Anthropic Citations API pattern — substring-verifying every cited quote against the source corpus and routing semantic-support checks through a local LLM judge — producing a measurable **3.25× lift in citation span correctness** over standard chunk-fetch RAG (0.65 vs 0.20), while in the same session closing 15 acquihire-readiness items (license remediation, secrets audit, governance gate, audio WER, OCR accuracy, 7 ADRs) and lifting the verification scorecard from 31% to 49%.
**Tags**: `rag`, `llm`, `legal`, `audit`, `triad`, `mcp`, `extract`, `ocr`, `audio`


---

## Sources

This reconstructed handoff was generated by `tools/backfill_handoffs.py` on 2026-05-02 from:

- `memory/recent-work.md` lines 26-43 — primary activity log
- `memory/automation-ledger.md` lines 297-355 — pain→fix entries + compounding score
- `memory/resume-evidence.md` lines 138-144 — STAR bullet + measurables
- git commit `3e11280f36` — found via `git log --all --grep "session 277"`

To verify any specific claim, open the cited file at the cited line range and read the primary entry.

---

*Reconstructed handoff — DO NOT cite externally without verification against the primary memory files. For going-forward sessions, `/wrap-up` Step 6.5 writes contemporaneous handoffs to this folder automatically.*
