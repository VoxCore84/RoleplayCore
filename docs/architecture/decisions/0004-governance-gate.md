# ADR 0004: Governance Gate by Construction

**Status:** Accepted
**Date:** 2026-04

## Context

The case archive contains 1,760+ files spanning legal correspondence, clinical records, congressional filings, and personal evidence. A subset is sensitive in ways that are non-negotiable: SSN-bearing documents, private credentials, attorney-client privileged exchanges, court-sealed material, classified-banner documents.

The default behavior of "extract everything, embed everything, search everything" is wrong for this corpus. A bug — or even just a careless sweep — that puts sealed material into a cloud-bound vector index is hard to reverse and creates real exposure.

The governance gate has to block ingestion at the front door, not paper over leaks downstream.

## Decision

**Multi-layer pre-ingest filter** in `tools/extract_cache.py` and `tools/excluded_daemon/router.py`:

1. **Stage 1 — filename/folder filter** (`_is_security_sensitive` in extract_cache, `_hits_security_filter` in router). Blocks `Pword.txt`, `*recovery-codes*`, `*credentials*`, `.env`, `id_rsa`, `*apikey*`, plus folder names `Credentials/`, `Secrets/`, `.ssh/`, `.gnupg/`. Documents matching get refused before extraction.
2. **Stage 2 — post-extraction content scan** (`scan_extracted_text`). Regex+entropy check on the first 8KB of extracted text. Catches SSNs, password assignments, AWS keys, GitHub PATs, OpenAI keys, private-key PEMs, high-entropy credential-shaped tokens. The "The Master.txt" failure mode (filename-safe file with a password embedded on line 2) gets caught here.
3. **Stage 3 — classification marking detection** (`scan_classification_markers`, added 2026-05-02). Banners (`SECRET//`, `TOP SECRET//`, `CONFIDENTIAL//NOFORN`, `CUI//PRVCY`, `UNCLASSIFIED//FOUO`), sealing markers (`UNDER SEAL`, `PROTECTIVE ORDER`), grand-jury secrecy (`Rule 6(e)`, `GRAND JURY MATERIAL`). Quarantines the document; never enters the index.
4. **Stage 4 — readonly-path enforcement** (`assert_writable` in router). `Case_Reference/` is structurally read-only — any worker writing under that root raises `PermissionError`. Chain-of-custody bedrock for the legal evidence.

Every refusal/quarantine/block writes one row to **`.cache/governance_audit.jsonl`** (added 2026-05-02). The log is queryable: `python tools/governance_audit.py stats|query`. The diligence answer to "prove you didn't process this sealed document" is `grep`.

## Alternatives considered

1. **Post-hoc filtering** — let everything in, scrub the index later. Rejected: once a sensitive chunk is in ChromaDB or FTS, removing it requires careful index surgery and you can never prove a query didn't return it before scrubbing. Pre-ingest is the only honest answer.

2. **Marker-only filter** (filenames + folders, no content scan). Rejected after the "The Master.txt" incident — a file with a credential-irrelevant name had a password embedded in its body. Stage 1 alone doesn't catch this.

3. **Detect classification at the document level only** (banner-on-page-1 rule). Rejected: real-world classified material doesn't always banner consistently across pages, and our scan covers the first 16KB to catch most real banners while avoiding noise.

4. **No structural readonly enforcement on `Case_Reference/`.** Rejected after a near-miss where an automation could have appended to a Master document. Chain-of-custody requires evidence files be untouchable by tooling.

## Consequences

**Positive:**
- The governance gate is **structural** (PermissionError, JSONL audit log) rather than **policy** (a human remembering to check). Diligence-grade answer to the privilege question.
- Audit log is queryable. "Show me every classified-banner document the system has ever quarantined" is a one-line CLI invocation.
- False-positive analysis on the existing 1,484 cached extracts: 0 hits after pattern tightening (validated 2026-05-02).

**Negative:**
- Stage 3 (classification markings) was tightened twice during initial deployment to eliminate false positives from OCR noise (`Cell #: C//v` → caught as `C//`) and from data fields (`SECRET` as a clearance-level value on a personnel form). The bare-letter shorthand patterns and standalone-line patterns were dropped; all remaining patterns require `//` caveat slashes per DoDM 5200.01 vol 2.
- The audit log grows monotonically — no rotation by design. Diligence wants the full history. Acceptable up to ~100MB; archive monthly beyond that.

**Neutral:**
- False-negative rate not measured on a red-team test set (Cat 3 follow-on item).

## References

- `tools/extract_cache.py` — `_is_security_sensitive`, `scan_extracted_text`, `scan_classification_markers`
- `tools/excluded_daemon/router.py` — `assert_writable`, `route`
- `tools/governance_audit.py` — append-only JSONL audit log
- `.claude/rules/excluded-corpus.md` Rule 1 — Case_Reference read-only constitution
