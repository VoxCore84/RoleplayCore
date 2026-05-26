# VoxCore Decision Log — Engineering & Strategy

**Scope:** Engineering/strategy decisions for the VoxCore system.
**Granular architecture choices** → `docs/architecture/decisions/` (ADR 0001–0007; use ADR format for choices
with code-level consequences — the ADR README describes the template).
**Commercial decisions** → `_canonical_state/desktop/VoxCore_Decisions_Log.md`.
**This log** records operational, sequencing, and policy decisions that span subsystems or set
constraints for future work but do not rise to the level of a full ADR.

Format: Decision record with Date · Decision · Rationale · Evidence · Consequences · Revisit trigger.
Append-only. Supersession discipline: strikethrough old text, add a dated correction note.

---

## DEC-2026-05-26-001: Improve existing systems before building new ones

**Date:** 2026-05-26

**Decision:**
Every recommendation from the 2026-05-26 system inventory is evaluated against the existing
system map first. If an equivalent system exists (live, dormant, or scaffold), the path is
improve/wire/reconcile — not rebuild from scratch. Greenfield builds are permitted only for
capabilities confirmed absent from the inventory.

**Rationale:**
The 2026-05-26 inventory found that VoxCore already has: hybrid FTS5+vector+KG retrieval
at 92.0% baseline, 5 MCP servers (33 tools), 2 daemons, 28 agents, 79 skills, 3 live
indexes (272 MB KG + 173 MB FTS5 + 477 MB ChromaDB), a 50-query eval harness, a cost
router (dormant), a memory control plane (dormant), and an anthropic helpers library
(dormant). Duplication wastes cost and creates maintenance debt. The pattern of
"recommendations proposing new systems that already exist" was observed repeatedly in
the image-harvest finding review.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` (master status table)
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q5, Q6, Q7)

**Consequences:**
- Before starting any build, run the EXISTING_SYSTEMS_MAP question: "Does this already exist?"
- Dormant systems (model_router.py, anthropic_helpers.py, Memory Control Plane v0.1,
  backend_selection.yaml) are candidates for wiring, not rebuilding
- GraphRAG and contradiction scaffolds are improve-existing paths once their upstream
  blocker (typed edges) is resolved
- New items added to the roadmap must pass a "not already built" check

**Revisit trigger:**
If a genuine gap is discovered that the inventory missed, document it in
EXISTING_SYSTEMS_MAP.md and assess whether it meets the bar for a new build.

---

## DEC-2026-05-26-002: GraphRAG deferred until typed KG edges exist

**Date:** 2026-05-26

**Decision:**
GraphRAG (multi-hop graph traversal) is deferred until typed KG edges replace the current
universal `predicate='mentioned_with'` co-mention relations. The `graphrag/PLAN.md` scaffold
is left untouched until that upstream work is done and A/B'd against the 92.0% baseline.

**Rationale:**
All 743,207 relations in the current KG (`tools/excluded_daemon/kg/build.py:411`) are
`predicate='mentioned_with'`. A GraphRAG traversal on an untyped graph cannot distinguish
"was a party to" from "is the author of" from "contradicts" — the traversal produces
entity neighborhoods, not semantic paths. Typed edges are the prerequisite, not a nice-to-have.
This is confirmed at `BUILD_VS_IMPROVE_DECISION.md` Q1: "GraphRAG does NOT exist —
`graphrag/PLAN.md` is a scaffold, zero production code (verified)."

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` (A6, A7 rows)
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q1, Q10)
`tools/excluded_daemon/kg/build.py:411` — predicate assignment (co-mention only)

**Consequences:**
- GraphRAG is Item 4 in the roadmap; Typed KG Edges is Item 3 and is the explicit gate
- `graphrag/PLAN.md` and `contradiction/PLAN.md` are scaffolds, not tickets; neither is
  executed without Adam GO after typed edges are proven
- The existing 3-channel hybrid (FTS5+vector+KG-entity RRF at 92.0%) is the production
  retrieval path until GraphRAG adds measurable net lift in an A/B

**Revisit trigger:**
When typed KG edges are built, A/B'd, and confirmed at 92.0% or better, revisit this
decision and convert `graphrag/PLAN.md` from scaffold to ticket.

---

## DEC-2026-05-26-003: Cost banking before large retrieval refactors

**Date:** 2026-05-26

**Decision:**
Cost controls (specifically Batch API adoption in `tools/batch_eval.py`) are implemented
BEFORE any paid-API retrieval improvement such as typed KG edge extraction. Caching is
explicitly excluded — it is a verified $0 no-op at VoxCore's call sizes.

**Rationale:**
The only real cost lever for VoxCore's eval sweep is the Batch API (~50% reduction on
50-query runs). Prompt caching does not apply: the judge prompt is 169 tokens, below the
~1024-token cache floor for any Anthropic model. The typed-edge extraction (Item 3) is
the highest-cost upcoming operation (per-chunk LLM calls across the full corpus). Running
it without Batch API wired is unnecessarily expensive. The gate is not cost controls
generally — it is specifically reconciling the 3 entangled files that block safely
editing citation_scorer.py and quality_probe.py.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/COST_BANKING_READINESS.md` (§2 call sites,
§3 entanglement, §4 safe patch plan, §5 verdict)
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q8, Q10)

**Consequences:**
- Item 0 (entanglement resolution) gates Item 1 (cost banking), which gates Item 3
  (typed KG edges) for cost reasons
- Do NOT add caching to any tool — verified no-op; document this explicitly to prevent
  future sessions from re-litigating it
- Batch API is opt-in (`--batch` flag), not the default; synchronous path remains default
- The eval sweep cost delta is measured before and after with provenance (run_id, etc.)

**Revisit trigger:**
If VoxCore's call patterns change to include a ≥1024-token repeated system prompt, caching
should be re-evaluated. If the Anthropic Batch API SLA changes materially, revisit the
async-turnaround tradeoff.

ADR candidate: the caching-is-a-no-op finding could be documented as ADR 0008 if this
decision needs a more formal home.

---

## DEC-2026-05-26-004: MCP servers consolidated and wrapped, not duplicated

**Date:** 2026-05-26

**Decision:**
New MCP capabilities are added as tools to existing MCP servers, not as new standalone
servers. The one confirmed gap (hybrid-stack MCP wrapper) is added to the docs-rag server
as a new tool, not as a sixth server. No MCP server is rebuilt from scratch if an existing
server already covers the domain.

**Rationale:**
5 MCP servers with 33 tools are already live and skill-referenced (arcanum 9 tools,
docs-rag 10 tools, voxcore-db 6 tools, voxcore-server 8 tools, local-llm 6 tools). The
inventory found that a prior "zero MCP" claim in `VoxCore_Stack_Reference.md` was stale.
Adding a new server for the hybrid-stack wrapper would create a sixth surface to configure,
maintain, and skill-wire, while the docs-rag server is the natural home (it already
exposes vector + KG tools from the same pipeline). The gap-not-gap distinction matters:
arcanum (keyword) and docs-rag (vector+KG) are complementary, not duplicate.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` (B1–B6 rows)
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q3)

**Consequences:**
- Item 6 (MCP hybrid wrapper) targets `tools-dev/docs-rag/docs_rag_server.py` for the new
  tool definition, not a new server directory
- Future MCP work follows the same pattern: extend existing servers unless a genuinely new
  domain (with no existing server) is being exposed
- Server count is a metric to watch: if a single server exceeds ~15 tools, consider a
  domain split — but currently all servers are well under that limit

**Revisit trigger:**
If a new domain (e.g., live-web-search, audio analysis) requires a first server in that
space, this decision does not block it. The "consolidated/wrapped not duplicated" principle
applies only to capabilities that overlap an existing server's domain.

---

## DEC-2026-05-26-005: Hook promotion requires dry-run/monitor-first pass

**Date:** 2026-05-26

**Decision:**
No hook in `hook_daemon.py` or `.claude/settings.json` is promoted from dormant to active
enforcement mode without first running in log-only (monitor) mode and verifying the log
output. Forced daemon restarts are prohibited for hook promotion; natural reload events are
the only safe activation path.

**Rationale:**
The hook daemon (C1) is live with pid 34224, ~21h uptime, and serves ALL open tabs plus
CalmCore via 4 symlinks. A bad reload or settings.json change disrupts both projects
simultaneously. The sql-write-monitor route (C4) is already implemented; it requires one
settings.json entry to activate. The CC-05 SubagentStop breadcrumb (C3) activates on the
next natural daemon reload — no settings change needed. Forced restarts for non-urgent
hook promotion are never worth the blast radius.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` (C1–C4 rows)
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q9)

**Consequences:**
- sql-write-monitor is added to settings.json with log-only behavior; auto-reject mode
  requires a separate Adam GO and a separate settings.json change
- CC-05 SubagentStop breadcrumb activates naturally; no action required this session
- Any new hook route added to hook_daemon.py follows the same pattern: implement the route
  first (log-only), then promote to enforcement only after log review confirms correct behavior
- Rollback: removing the settings.json entry disables the hook; no code change needed

**Revisit trigger:**
After sql-write-monitor has been in log-only mode for at least 5 sessions with no
false-positive events, consider promoting to soft-enforcement (warn but don't block).

---

## DEC-2026-05-26-006: Screenshot/image-harvest claims require verification before implementation

**Date:** 2026-05-26

**Decision:**
Any recommendation derived from screenshot analysis or image-harvest pipelines is treated
as a draft finding, not a verified fact. Before implementing, the claim must be verified
against source documents (code, config files, live system) by a code-path or query that
can return a failure result. "Verify-before-recommend" is now a rule gate in
`completion-integrity.md` and `operational-discipline.md`.

**Rationale:**
The 2026-05-26 inventory found multiple cases where image-harvest "findings" described
systems as absent that were in fact live (e.g., "zero MCP servers" — actually 5 servers
live). Visual/OCR parsing of screenshots is lossy and context-dependent. A finding that
leads to building a system that already exists wastes cost and creates duplication. The
governance gate (ADR 0004) already handles sensitive-content verification; this decision
extends the same verify-first principle to all image-derived recommendations.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q5, Q6)
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` (B3, stale Stack
Reference note)
`.claude/rules/completion-integrity.md` — verify-before-recommend gate (added session 285)
`.claude/rules/operational-discipline.md` — same gate

**Consequences:**
- Any session that receives image-harvest findings must cross-check them against the live
  system (grep, describe, query) before acting
- "System X does not exist" from image analysis is a hypothesis, not a fact; verify by
  reading the relevant source path
- The verify gate applies to all image-sourced claims, including claims about what code
  does, what config is set, and what systems are deployed

**Revisit trigger:**
If a higher-fidelity image analysis pipeline (one that reads source files directly rather
than screenshots) is adopted, the verify-first step may become less critical for that
specific pipeline. The principle remains.

---

## DEC-2026-05-26-007: Privacy artifacts stay quarantined and gitignored

**Date:** 2026-05-26

**Decision:**
Files in `_PRIVATE_quarantine/` and any file matching the security-sensitive patterns in
`tools/extract_cache.py:_is_security_sensitive()` and `tools/excluded_daemon/router.py`
are permanently gitignored and never promoted to the committed tree. This applies even
when the repository is local-only.

**Rationale:**
ADR 0004 establishes the multi-layer pre-ingest filter (Governance Gate by Construction).
The decision here extends that to git: local repos can be pushed, backed up, or imaged
unintentionally; git history retains content permanently. Personal-corpus paths, SSN-bearing
documents, attorney-client material, and credentials must never enter a tracked file,
regardless of the repo's current remote status. The `_PRIVATE_quarantine/` directory was
created and populated during privacy remediation (2026-05-26 session); its `.gitignore`
entry must never be removed.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/NEXT_IMPLEMENTATION_PROMPT.md` (HARD CONSTRAINTS)
ADR 0004 (`docs/architecture/decisions/0004-governance-gate.md`)
`.claude/rules/operational-discipline.md` — Repository exclusion criteria

**Consequences:**
- `git add` of any file matching Excluded/IMPORTANT DOCS/Case_Reference/Desktop/SSN/
  credentials is blocked by the operational-discipline pre-mortem check
- The `.gitignore` entry for `_PRIVATE_quarantine/` must not be removed or modified
- This decision applies to any future personal-path inventory, system map, or file-system
  map that contains Excluded/ path strings: default is "kept out unless explicitly approved"

**Revisit trigger:**
Not revisitable without a full security review and explicit Adam GO.

---

## DEC-2026-05-26-008: Untrusted content must be delimited in prompts

**Date:** 2026-05-26

**Decision:**
Any user-supplied or corpus-derived content that is embedded in an LLM prompt must be
wrapped in explicit XML or markdown delimiters that separate it from instruction text.
This applies to all prompts in `tools/citation_scorer.py`, `tools/quality_probe.py`,
`tools/ai_studio/review_cycle.py`, and any future tool that sends corpus content to an
LLM API.

**Rationale:**
Prompt injection is a structural risk when retrieval results, OCR output, or user queries
are concatenated directly into system or user messages without delimitation. Corpus content
may contain adversarial instruction text, especially in OCR'd legal correspondence or
email mbox content. The Excluded/ corpus contains 1,760+ files including emails, which
are a known vector for injection payloads. Delimiters (e.g., `<document>...</document>`,
`<retrieved_content>...</retrieved_content>`) are a lightweight mitigation that does not
require model changes.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q5, verify-
before-recommend and injection-defense cluster)
`.claude/rules/operational-discipline.md` — untrusted content delimiting (added session 285)
ADR 0004 — governance gate applies to ingest; this decision applies to prompting

**Consequences:**
- All new LLM prompt construction wraps corpus content in explicit delimiters
- Existing prompts in citation_scorer.py and review_cycle.py are audited for missing
  delimiters when those files are next touched (Item 0 or Item 1)
- The delimiter pattern is documented in a comment adjacent to any `JUDGE_PROMPT` or
  equivalent constant so reviewers can verify at a glance

**Revisit trigger:**
If an LLM provider releases native prompt-injection mitigation (e.g., a structured message
format that isolates instructions from data), evaluate whether explicit delimiters can be
replaced by that mechanism.

---

## DEC-2026-05-26-009: Entangled files must be reconciled before modifying behavior

**Date:** 2026-05-26

**Decision:**
`tools/citation_scorer.py` (+93 uncommitted, Phase 3.9), `tools/quality_probe.py`
(+23 uncommitted, Phase 4 HyDE channel), and `tools/excluded_hybrid_search.py`
(+105 uncommitted, Phase 4 HyDE refactor) must be reconciled (committed as their own
commit, deferred, or explicitly discarded) BEFORE any new behavior edit is made to those
files. Mixing a new edit with prior-session uncommitted work in a single commit is
prohibited.

**Rationale:**
These three files carry additive prior-session uncommitted changes that represent real work
(Phase 3.9 judge-package hook and Phase 4 HyDE evaluation channel). A naive `git add -A`
or an edit that touches these files without reconciling the prior work would either
(a) lose the prior work or (b) entangle it with a new commit in a way that makes it
unreviable. The COST_BANKING_READINESS.md analysis confirmed these are the explicit gate
for cost banking and any retrieval refactor.

**Evidence:**
`AI_Studio/Reports/system_inventory_2026-05-26/COST_BANKING_READINESS.md` (§3 entanglement,
§4 safe patch plan)
`AI_Studio/Reports/system_inventory_2026-05-26/EXISTING_SYSTEMS_MAP.md` (A4, A5, E4, E5 rows)
`AI_Studio/Reports/system_inventory_2026-05-26/BUILD_VS_IMPROVE_DECISION.md` (Q9)

**Consequences:**
- Item 0 (repo hygiene) gates all downstream items that touch these files
- Per-file decisions are required from Adam: commit as-is / defer / discard. These are not
  Claude's decisions to make unilaterally
- `tools/batch_eval.py` is built as a NEW file to avoid touching the entangled paths even
  for cost banking (Item 1)
- Any session that opens citation_scorer.py, quality_probe.py, or excluded_hybrid_search.py
  must first check `git diff <file>` to verify entanglement status

**Revisit trigger:**
When all three files have been reconciled (committed or discarded), this constraint is
resolved. Document the resolution in the next commit message referencing this decision.

---

## ADR promotion candidates

The following decisions may warrant formal ADRs in `docs/architecture/decisions/` given
their code-level consequences. Promoting requires writing the full ADR template (context /
decision / alternatives considered / consequences / references).

| Decision | Candidate ADR | Rationale for promotion |
|----------|---------------|------------------------|
| DEC-003: Batch API as the real cost lever; caching is a no-op | ADR 0008 | Code-level: affects every future tool that calls Anthropic API; alternatives considered are documented in COST_BANKING_READINESS.md |
| DEC-008: Untrusted content delimiter pattern | ADR 0009 | Code-level: affects all prompt construction; cross-references ADR 0004 |
| HyDE killed as net-negative (−10pp, existing finding from Phase 4) | ADR 0008 or 0010 | Already decided; worth a formal ADR to prevent re-litigation; evidence is in `reporting/PARETO_2026-05-04.md` |

Note: ADR numbering as of 2026-05-26: 0001–0007 exist. ADR 0005 and 0006 exist
(citation-precision pipeline and pdfplumber/pypdfium2); check `docs/architecture/decisions/`
for the current highest number before assigning 0008+.
