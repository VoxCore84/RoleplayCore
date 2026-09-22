# Documentation Discipline — Per-Checkpoint Cadence (P1 Audit-Trail)

> Long form + history: docs/rules-reference/documentation-discipline.md

## When this rule applies
- Completing any phase of multi-phase work, BEFORE moving to the next
- Writing any closeout report at `AI_Studio/Reports/PHASE_*_CLOSEOUT_*.md`
- Editing any audit-trail file (`SL_Vault/01_Achievement_Record.md`, `02_Decisions_Log.md`, `06_Working_Documents/*`)
- Authoring a scaffold / plan document (vs an execution-approved ticket)
- Detecting that a previously-stated number / claim was wrong

## Canonical docs over scattered reports
When an inventory / architecture / consolidation session produces findings, update the canonical docs in `docs/` (System Registry, Architecture Map, Build Roadmap, Decision Log, Dormant-Systems register) — do NOT leave findings only in `AI_Studio/Reports/` (gitignored; not where future sessions look). The reports are the evidence base; `docs/VOXCORE_*.md` is the committed source of truth. Entry point: `docs/VOXCORE_HANDOFF_INDEX.md`. A finding not reflected in the registry will be rediscovered.

## Per-checkpoint cadence — never per-session
After each phase closes (work complete, stop conditions met, output rendered): update the achievement record AND write the closeout report AND add an update log row BEFORE moving to the next phase. Do NOT batch documentation to session end.

## Achievement record bullet format
- **Action-quantified-impact** format with date suffix `[YYYY-MM-DD]`
- **Subhead consistency**: bullets land under "Architecture and engineering execution" / "Calibration discipline and measurement" / "QA and engineering judgment" / "Documentation and communication" / "Domain context"
- **Numbers verbatim**: "Cohen's kappa = 0.497", not "moderate agreement"; "+632 bytes annotation", not "small annotation"
- **Provenance inline**: schema_version, snapshot_id, run_id, gold-set name+version when the bullet describes a measurement
- **Inline artifact citations**: `path/to/file.md` not "the closeout report"

## Closeout report template
1. Header (date / phase / status / cost / wall time)
2. Operations executed (table format with paths)
3. Verification results (SHA-256 confirmations, post-flight reads, etc.)
4. Anything unexpected during execution (surface findings)
5. Final state (file listings or measurement tables)
6. Stop conditions met (checklist with ✅)
7. Cost ledger (estimated vs actual, cumulative session)
8. Recommended next step

## Update log discipline
- Append above the "When updating, append a row above this line" sentinel — never below
- Format: `| date | author | one-paragraph change description with key numbers inline |`
- Mention which subhead the new bullet went under
- Confirm cost at the bottom
- Document mid-phase corrections OPENLY in the entry rather than silently fixing them

## Supersession discipline (Theranos pattern)

Audit-trail documents are NOT retroactively edited when reality changes. They preserve truth-as-of-write-time. New entries supersede old ones.

When a previously-stated fact / measurement / path is later corrected:
- Strikethrough the original: `~~original text~~`
- Append a dated note: `**[Correction YYYY-MM-DD]:** see <new path or value> per <source>. Original preserved as audit trail.`
- Add a row to the update log documenting the correction
- Never overwrite a measurement claim without strikethrough — the audit trail is part of the artifact's value

## Anti-fabrication: verify before summarizing

When writing a summary that contains numbers, CALL the function that computed the numbers and check before committing the summary.

- OK: re-run `compute_metrics()` on the actual Run record before writing the per-category lift bullet
- BAD: free-recall numbers from short-term memory

The verification call uses the same code path that produced the numbers. A different code path may give a different answer due to bugs in either path.

## Plans vs tickets vocabulary
- **Plan / scaffold** — pre-approved-work document; can be revised before execution; cost estimates and acceptance criteria are tentative; explicit Adam GO required to execute
- **Ticket** — approved-work document; revising it triggers re-approval

Future scaffolds keep the distinction explicit at the document header.
