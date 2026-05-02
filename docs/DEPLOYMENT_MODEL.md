# Deployment Model — Local-Only by Design

**Written:** 2026-05-02.
**Scope:** Closes Verification Master Checklist Cat 8 item: "Dev → staging → production path documented (or explicit 'local-only' decision)".

## Decision: VoxCore is single-machine local-only software.

There is no dev → staging → production deployment pipeline. The production environment IS the development environment IS the operator's workstation. This is an explicit architectural choice, not an absence of decision.

## Why local-only

1. **The corpus is privileged legal evidence.** Adam's case files include MHS Genesis records, OSI / SAPR investigation outputs, congressional correspondence, and clinical documentation. Pushing this to a hosted deployment — even a private VPC — multiplies the attack surface, the audit-trail burden, and the chain-of-custody risk. The defensible posture is: it never leaves the machine that owns it.
2. **All compute is on-machine.** Local Ollama (gemma4:26b, qwen3.5:27b, nomic-embed-text), local Whisper for audio, local Tesseract for OCR, local SQLite + ChromaDB. The only network calls are explicit cloud-API invocations the operator triggers (Anthropic / Google for Triad orchestration, never for ingest).
3. **The user is the operator.** Adam is the only intended user. There is no multi-tenant story, no shared session state, no team collaboration layer to maintain.
4. **Reproducibility is per-machine.** Pinned dependencies (`*.pinned.txt` from `tools/deps_audit.py`) plus the environment manifest (`docs/ENVIRONMENT.md`) let the same machine — or a clone of it — reproduce any historical state. That's the only deployment target.

## What replaces dev/staging/prod

| Concern usually solved by staging | How VoxCore handles it |
|---|---|
| Test changes before prod sees them | `docs/architecture/decisions/` ADRs + `tools/validate_deliverable.py` checks before merging code |
| Roll back a bad release | Git revert; everything is in `VoxCore84/VoxCore-legacy` |
| Test with realistic data without polluting prod | `Excluded/` is the data; tests run against it directly because there's nowhere else to run them |
| Catch regressions before they hit users | LLM-as-judge measurement (`citation_scorer.py --judge claude`) on held-out batches before declaring an improvement shipped |
| Coordinate multiple deployers | Single operator; `doc/session_state.md` for multi-tab coordination, not multi-user |

## What changes if a future buyer wants a hosted deployment

This decision is reversible but not casually. To go hosted, the build would need:
- Tenant isolation in the corpus index (currently single-corpus, single-database)
- Network auth on the MCP server fleet (currently stdio-local, see `MCP_TRANSPORT.md`)
- Encrypted-at-rest storage with key management (currently raw SQLite + Chroma on disk)
- A real CI/CD pipeline (currently zero CI; `.github/workflows/` empty)
- Monitoring + alerting (currently `tail_log` on demand)
- A separation of test data from production data that doesn't exist today

Each of these is a 2-week-to-2-month build. Architecture-wise none of them are blocked by current code; the decision is whether the buyer wants a single-machine appliance (current) or a hosted product (significant rebuild).

## Operational reality (the "production runtime")

- **Hardware:** documented in `docs/ENVIRONMENT.md` (Ryzen 9 9950X3D, RTX 5090 32GB, 128GB DDR5, NVMe).
- **OS:** Windows 11 Pro 10.0.26200, Python 3.14.3.
- **Models:** see `docs/ENVIRONMENT.md`.
- **Backup:** GitHub private repo (`VoxCore84/VoxCore-legacy`) for code; the corpus itself is on the operator's NVMe and is intentionally NOT backed off-site (privacy posture). This is a known, accepted gap — see Verification Master Checklist Cat 8 "Off-site backup of test corpora and trained artifacts".
- **Monitoring:** none in the deployed sense; `mcp__voxcore-server__tail_log` and `mcp__voxcore-server__status` provide on-demand observability.
- **Pause and resume:** the system pauses when the workstation is off and resumes when it is on. No 24/7 uptime requirement.

## Verification

| Question | Answer | Evidence |
|---|---|---|
| Is there a staging environment? | No | No `staging/` config, no separate hosts, no `*.staging.env` files |
| Is there a CI/CD pipeline? | No | `.github/workflows/` empty; no GitHub Actions configured |
| Is there a monitoring stack? | No | No Datadog/Prometheus/Sentry configs in repo |
| Is the operator the only user? | Yes | No auth layer, no user table, no multi-tenant config |
| Is this an explicit decision or an oversight? | Explicit decision | This document, written 2026-05-02 |
