# Excluded/ Corpus Rules — Constitution for the Legal/Career/Finance Archive

These rules apply to **any** session, tool, agent, or daemon that reads, writes, cites, or indexes content under `C:\Users\atayl\Desktop\Excluded\`. They are non-negotiable.

## The Five Rules

### 1. `Case_Reference/` is READ-ONLY. Always.
- No tool, agent, slash command, or daemon may write into `C:\Users\atayl\Desktop\Excluded\IMPORTANT DOCS\Case_Reference\` or any subfolder.
- Additive synthesis files (`_MASTER.md`, `_INDEX.json`) are the ONLY permitted additions, and only when the user explicitly approves.
- Extracted text sidecars go to `.cache/extracted/`, not into Case_Reference.
- Chain of custody is the bedrock of legal evidence. A tool that accidentally overwrites an original exhibit invalidates months of work.
- **Enforcement:** `tools/excluded_daemon/router.py` security gate + `tools/excluded_daemon/config.py` `READONLY_PATHS` list. Any attempt raises `PermissionError`.

### 2. Every non-trivial claim requires a source citation.
- When stating a fact about the case, career, finances, or any Excluded/ content, cite `file_path:line` or `file_path:chunk_id`.
- "I believe X" without a citation is acceptable if explicitly flagged as memory/recall.
- "X is true" without a citation is a violation of Completion Integrity (see `.claude/rules/completion-integrity.md`).
- This applies to `/ex-ask` answers, `/filing-prep` drafts, memory updates, and any agent output.

### 3. Confidence tiers are mandatory on evidentiary claims.
- Every `/ex-ask`, `/evidence-xref`, `/filing-prep` output must rate each claim:
  - **PROVEN** — documentary evidence + regulation + timeline all agree
  - **WELL-SUPPORTED** — multiple independent sources
  - **PARTIALLY-SUPPORTED** — single documentary source or multiple secondary
  - **UNCERTAIN** — only reported/reported secondhand
  - **UNSUPPORTED** — not found in corpus
- UNSUPPORTED is a valid output and is better than inflated confidence.
- Never promote a claim to a higher tier than its evidence supports.

### 4. Clinical records are quoted verbatim — never paraphrased.
- MHS Genesis notes, inpatient records, CAPS-5 scores, PCL-5 trajectories, provider commentary, and anything under `Case_Reference/06_CLINICAL_RECORDS/` or `Mental Health Outpt Note/` must be quoted word-for-word when used as evidence.
- Summaries are permitted for briefing purposes, but any filing citation must include the verbatim quote AND the source file path.
- Paraphrasing clinical content introduces legal and factual risk. The exact wording is often outcome-determinative (e.g., "PTSD, unspecified" vs. "Other Specified Trauma- and Stressor-Related Disorder").

### 5. Memory updates require source citations on every edit.
- When any `/ex-absorb`, `/case-intake`, or memory-update flow proposes changes to files in `~/.claude/projects/C--Users-atayl-VoxCore/memory/`, each proposed edit must cite the source document that motivated it.
- Memory files are a curated synthesis layer. Drift from source = filing risk.
- Edits applied without citation are to be reverted by `/memory-audit`.

---

## Scope and Priorities

### Read-only by policy (no writes, indexing allowed)
- `Excluded/IMPORTANT DOCS/Case_Reference/` — 26 folders, 1,760+ files
- `Excluded/mbox/*.mbox` — 17 Gmail Takeout files
- `Excluded/Recordings/` — 45 audio files

### Additive-only (new files allowed, existing files untouchable)
- `Excluded/IMPORTANT DOCS/Monday_HAF_Call_13Apr2026/`
- `Excluded/IMPORTANT DOCS/Angel_VA/`
- `Excluded/IMPORTANT DOCS/Finances/`
- `Excluded/IMPORTANT DOCS/Career/`
- `Excluded/IMPORTANT DOCS/Brand/`
- `Excluded/IMPORTANT DOCS/Ethical_AI_Research/`
- `Excluded/IMPORTANT DOCS/Resume Stuff/`

### Free-rein (move, rename, delete, sort)
- `Excluded/_Needs Sorted/`
- `Excluded/_Archive/`

### Security-gated (never indexed, never embedded)
- Files matching `Pword.txt`, `*recovery-codes*`, `*backup-codes*`, `*credentials*`, `.env`, `id_rsa`, `id_ed25519`, `*apikey*`, `*access-token*`, `*private-key*`
- Folders named `Credentials/`, `Secrets/`, `.ssh/`, `.gnupg/`
- Enforced by `tools/extract_cache.py` `_is_security_sensitive()` + `tools/excluded_daemon/router.py` security gate

### Excluded from indexing (not sensitive, just not relevant)
- `Excluded/LoreWalkerTDB/` — CalmCore DB dumps parked here
- `Excluded/unredact/` — internal FOIA pipeline workspace
- `Excluded/takeout-20260411T200559Z-3-001/` — Google export (indexed separately if needed)

---

## Operational Directives

### Never auto-run maintenance mid-query
- `/ex-ask`, `/case-search`, `/evidence-xref`, `/filing-prep` must answer with the CURRENT state of indexes.
- If retrieval returns UNSUPPORTED, state it in the Gaps section. Do not auto-invoke `/ex-refresh`.
- Maintenance (`/ex-refresh`, `/ex-absorb`, ChromaDB rebuilds) is only ever run when the user explicitly requests it.
- **Reason**: Session Failure Retrospective documents a one-hour loss due to naive "index might be stale → refresh first" reasoning. Same failure mode in legal domain = missed filing deadline.

### NEVER use `CronCreate` for any scheduled behavior
- Recurring CronCreate has historically fired prompts into idle tabs and frozen Claude sessions.
- Scheduled behavior in the Excluded/ stack goes through one of:
  1. The daemon's asyncio loop (`tools/excluded_daemon/jobs/*`)
  2. Windows Task Scheduler (for external nightly jobs)
  3. Event-driven watchdog (no timer needed)
- If you think you need `CronCreate(recurring=true)`, you actually need a daemon asyncio task.

### Attribution matters even for trivial claims
- "Adam's ADSCD is 2026-08-10" — cite `memory/case-status.md` or the source document.
- "Amy Little is a HAF/A1ZA analyst" — cite `01_CONTACTS_AND_REFERENCES.md:17`.
- Uncited facts in legal drafts are rework at best, disciplinary at worst.

### Local-model delegation for triage
- Classification, tagging, and short-summary generation should use `mcp__local-llm__*` (Qwen 27B, local, $0).
- Reserve Claude's Opus API for final synthesis, drafting, and decisions requiring deep reasoning.

### Completion integrity applies to corpus operations
- `/ex-absorb` reports exact counts: N files absorbed, M OCR'd, K transcribed, L indexed, X failed.
- No "successfully ingested" without numbers.
- Partial success is partial — state what was NOT done.

---

## Priority Folders (daemon notification zone)

Files landing in these folders trigger a morning-briefing notification via `tools/excluded_daemon/workers/index_worker.py`:

```
IMPORTANT DOCS/Case_Reference/04_LEGAL_CORRESPONDENCE/
IMPORTANT DOCS/Case_Reference/01_APPEALS_AND_QAI/
IMPORTANT DOCS/Case_Reference/05_EVIDENCE_SCREENSHOTS/
IMPORTANT DOCS/Case_Reference/08_CONGRESSIONAL/
IMPORTANT DOCS/Case_Reference/09_SECURITY_CLEARANCE/
IMPORTANT DOCS/Monday_HAF_Call_13Apr2026/  (time-bounded: delete folder after call)
```

If the user drops a PDF or email into any of the above, the next session-start surfaces it.

---

## Gotchas (known failure modes)

1. **Mbox retrieval on deleted-then-archived messages** returns only headers — body is empty. False confidence risk. Always check `body_text` is non-empty before citing.
2. **ChromaDB semantic search ranks emotionally charged language high** regardless of legal relevance. "I was devastated" may outscore a dry DoDI paragraph. Use FTS5 (keyword) as a cross-check for regulatory claims.
3. **OCR on scanned military records misreads AFSC codes and dates frequently** (2→Z, 0→O, dates with slashes become dots). Quote the raw image when the AFSC/date matters.
4. **`extracted_legacy` paths may still appear in cache** from pre-consolidation indexing. Canonical paths live under `IMPORTANT DOCS/Case_Reference/`; legacy paths have `11_EMAILS__Takeout_Extracted__...` with double-underscores. Prefer the canonical.
5. **Markdown chunking splits tables** if naive fixed-size. The contacts table in `01_CONTACTS_AND_REFERENCES.md` is an especially painful case when split. Semantic chunker on `## ` headers fixes this.
6. **`Case_Reference/` chunks frequently duplicate across `extracted/` and `Case_Reference/extracted/` source roots** even after dedup — the same file is reachable via two paths. Not a bug; pick the shorter path for citation.

---

## Updates to These Rules

This file evolves with the case. Edits should:
- State the change + rationale
- Cite the source incident (e.g., "after session 260 incident where X occurred")
- Keep the file short — link out to longer docs rather than inline content

Last updated: 2026-04-12 (initial version).
