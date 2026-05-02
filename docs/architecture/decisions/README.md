# Architecture Decision Records

Short decision records for the non-obvious choices in VoxCore. Each ADR follows the standard template:

- **Context** — what problem prompted the decision
- **Decision** — what was chosen
- **Alternatives considered** — what was rejected and why
- **Consequences** — what changed downstream

ADRs are the canonical answer to acquirer-diligence questions of the form "why did you build it this way?" Senior engineers on the diligence team will read these before reviewing code.

## Index

| # | Title | Status | Date |
|---|-------|--------|------|
| 0001 | Triad orchestration with epistemic isolation | Accepted | 2026-04-30 |
| 0002 | MCP-first protocol surface | Accepted | 2026-03 |
| 0003 | Local-GPU offload for privilege-sensitive operations | Accepted | 2026-04 |
| 0004 | Governance gate by construction (pre-ingest, content-scan) | Accepted | 2026-04 |
| 0005 | Citation-precision pipeline with LLM-as-judge | Accepted | 2026-05-01 |
| 0006 | pdfplumber + pypdfium2 over PyMuPDF | Accepted | 2026-05-01 |
| 0007 | Hybrid retrieval: FTS5 + ChromaDB + KG, RRF k=60 | Accepted | 2026-04 |
