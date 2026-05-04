# Session 278 Handoff — VoxCore Demo QA Cycle + Vault Build + File Reconciliation

**Date:** 2026-05-03
**Session scope:** Phase 3.5 closeout (post-restart recovery) → Phase 4 multimodal demo build + closeout → 3 post-Phase-4 housekeeping docs → QA Tier 5 cycle (Decisions Log audit, Q13 diagnosis, two retroactive corrections) → SL_Vault build → 5-tier vault QA → file reconciliation pass (Phase 1-3) + OPERATIONAL_DISCIPLINE.md
**Outgoing tab status:** Approaching compaction, handing off cleanly. Round 3 closed; reconciliation closed; vault live.
**Incoming tab status:** Fresh context. This document is what you read first.

---

## BOOT PROMPT FOR NEXT TAB (paste this as your first message)

```
You are picking up VoxCore work from session 278. Read these files in order before doing anything else:

1. THIS HANDOFF: C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\2026-05-03_session_278_RECONCILIATION_AND_QA_CYCLE.md
2. Operational discipline (READ-FIRST for any destructive op): C:\Users\atayl\Desktop\SL_Vault\_vault_only\OPERATIONAL_DISCIPLINE.md
3. Known issues log: C:\Users\atayl\Desktop\SL_Vault\_vault_only\known_issues.md
4. Decisions Log (canonical, with today's entries + retractions): C:\Users\atayl\VoxCore\_canonical_state\desktop\VoxCore_Decisions_Log.md
5. Phase closeouts at C:\Users\atayl\VoxCore\demo\PHASE_{1,3_5,4}_CLOSEOUT.md
6. Capability scope: C:\Users\atayl\VoxCore\demo\CAPABILITY_SCOPE.md
7. Vault index: C:\Users\atayl\Desktop\SL_Vault\00_Index.md

Do NOT start any new build phase, Round 4 work, or destructive operation until I (Adam) explicitly direct you. The previous tab made significant progress and surfaced several incidents documented in the OPERATIONAL_DISCIPLINE.md and known_issues.md files. Read those before suggesting next steps.

Standing rules from session 278:
- Pre-mortem checklist before any destructive operation (see OPERATIONAL_DISCIPLINE.md § "The pre-mortem checklist")
- Never `stat -c %s` on a symlink in Git Bash — use `wc -c < "$path"` (Tier 5 truncate incident)
- Never `truncate` for restore — use `cp -f` from a backup
- Never `ln -s` from Bash without `MSYS=winsymlinks:nativestrict` exported — use PowerShell `New-Item -ItemType SymbolicLink` instead (fake-symlink incident)
- Personal-corpus grep before any `git add` of files containing path strings — `Excluded`, `IMPORTANT DOCS`, `Case_Reference` (File System Map deferral)
- Cite source data for every claim that lands in a permanent artifact (Theranos CONTRADICTS confabulation)

If I ask you to "what should I work on next" — refer to the "Pending work — post-Phase-3 cleanup list" section of this handoff.
```

---

## What this session actually did

### 1. Phase 3.5 closeout (post-restart recovery)
- Phase 3.5 implementation had completed in a prior session (PDF extraction cleaning + per-corpus ChromaDB collections), interrupted by a machine restart before closeout.
- This session verified the on-disk results were structurally sound and wrote the closeout report.
- Three Decisions Log entries authored: Auditor-context-limitation, PDF extraction post-processing, Multi-corpus volume bias fixed.
- Output: `demo/PHASE_3_5_CLOSEOUT.md`.

### 2. Phase 4 multimodal demo (full build + closeout)
- Built fictional slip-and-fall corpus (Santos v. GreenLeaf Grocery) at `demo/corpora/slipfall_santos_v_greenleaf/`.
- 11 artifacts: 2 TTS audio, 4 PIL-rendered OCR images, 3 COCO content images, 2 plain text. License attribution captured at creation in `clients/04_multimodal_slipfall/case.toml`.
- Pipeline: faster-whisper large-v3 (ASR), Tesseract 5.4.0 + Sonnet vision fallback (OCR), Opus 4.7 vision (image content captioning).
- Case ran on Opus 4.7 with verify-retry + inline auditor. 13 queries, 13/13 produced answers. ~$4.55 total cost, ~12 min compute.
- **Headline results (honest, both numbers):**
  - All-queries: chunk-resolution 61.0%, verbatim 57.4%, 2 CONTRADICTS
  - Excluding Q11: 96.4%, 94.0%, 2 CONTRADICTS
  - Q11 dragged aggregate down — model used basename-only paths (`complaint.txt`) instead of rel_paths, all 53 citations failed verification. Quote text correct, paths wrong.
  - **Q12 IDK test PASSED:** explicit refusal in two sentences, 0 fabrication, 0 citations, 5.0s elapsed. Strongest single demo result.
  - Q13 had 2 CONTRADICTS (auditor false-positives on self-honesty disclosure — see QA Tier 5 below for the diagnosed root cause).
- Side audits: Whisper medium WER (8.09%) actually slightly *better* than large-v3 (8.75%) on synthetic TTS; Vision OCR 9× better than Tesseract on same images (23% CER → 2.6%).
- Output: `demo/PHASE_4_CLOSEOUT.md`, four Decisions Log entries.

### 3. Three post-Phase-4 housekeeping docs
Authored at `demo/`:
- **INSTALL_MANIFEST.md** — single source of truth for clean-Windows-11 install (system binaries, Python packages with version pins, APIs, models, disk budget). Found `demo/requirements.txt` is **severely out of date** (lists 2 packages, 10 actually used) — flagged but not fixed (doc-only task per instruction).
- **CAPABILITY_SCOPE.md** — what the demo demonstrates vs. what's deferred to production-only validation. Acquirer-facing artifact. Includes Demo Calibration Story with both Phase 4 numbers reported honestly. Updated mid-session with the corrected Phase 5 priority (auditor-direct-claim-context, not cited-chunk).
- **CORPUS_ENTITY_INVENTORY.md** — per-case entity types and relationships latent in each demo corpus. Input to a possible Round 4 Demo 2 build (KG-backed retrieval).

### 4. QA Tier 5 cycle — three retroactive corrections
The QA pass surfaced inconsistencies in claims I'd written into permanent artifacts. Each correction applied with strikethrough+retraction discipline (originals preserved, supersession entry added).

**Correction 1: Theranos CONTRADICTS confabulation.** Phase 3.5 closeout cited "Two Theranos CONTRADICTS verdicts in Phase 3 scoring" as the source observation for the auditor-context-limitation finding. JSON shows 0 CONTRADICTS in both current and Sonnet baseline. The claim was carried forward from prompt language without independent JSON verification.

**Correction 2: Q13 misdiagnosis (the bigger one).** Phase 4 closeout claimed Q13's 2 CONTRADICTS were caused by auditor-context-limitation (cited chunks outside retrieval window). I built a diagnostic (`demo/tools/diagnostics/diagnose_q13_contradicts.py`) that replayed retrieval + auditor on Q13. Result: **all 5 cited paths were already in the auditor's 8 input chunks.** The auditor saw the cited content and still flagged CONTRADICTS at 0.95 confidence. Real root cause: `tools/inline_auditor.py:68` constructs each audit triple with a literal placeholder `"CLAIM context: sentence containing the quote"` instead of the model's real surrounding sentence. **Phase 5 priority refined from "auditor-direct-cited-chunk fix" to "auditor-direct-claim-context fix"** — different code change targeting different root cause.

**Correction 3: Decisions Log truncation incident (Tier 5 self-inflicted).** During edit-propagation testing, a Bash script computed truncate target from `stat -c %s "$VAULT_PATH"` where `$VAULT_PATH` was a symlink. On Git Bash on Windows, `stat -c %s` returns the symlink's path-string length (72 bytes), not target file size (97,050 bytes). The `truncate -s 72` command followed the symlink and **destroyed the canonical Decisions Log**. Recovered via `git checkout HEAD` + reconstruction from conversation history. Reconstruction note appended to the file documenting the incident itself.

All three corrections live in `_canonical_state/desktop/VoxCore_Decisions_Log.md` with strikethrough on retracted text + dated retraction notes + new superseding entry "Auditor false-positive CONTRADICTS — corrected root cause and fix target" (2026-05-03).

### 5. SL_Vault build (Obsidian vault for VoxCore demo audit trail)
- Built at `C:\Users\atayl\Desktop\SL_Vault\` per the architecture in your earlier prompt.
- Structure: `00_Index.md`, `01_Achievement_Record.md` (canonical home), `02_Decisions_Log.md` (symlink), `03_Phase_Closeouts/` (3 symlinks), `04_Demo_Reference_Docs/` (3 symlinks), `05_Project_PDFs/` (6 symlinks), `_vault_only/`, `_attachments/`.
- 6 PDFs symlinked from `voxcore-portfolio/docs/pdfs/` (Acquihire Playbook v2, Benchmarking Methodology, Calibration Scorecard, Deal Funding, Economic Impact v2, Legal Case Intelligence System Comprehensive). Skipped: AI_Engineering_Relevance, Economic Impact v1, JAG_Ethics_Counsel_Question_List, Section 16.
- Pre-existing files preserved: `Adam_Taylor_Achievement_Record.md` (renamed to `01_Achievement_Record.md`), prompt practice files moved to `_vault_only/`. Default `Welcome.md` deleted.
- 5-tier QA pass run on the vault build itself (caught the truncate incident — see #4 above).

### 6. File reconciliation pass (today's last work)
You discovered that `C:\Users\atayl\Desktop\` had 6 markdown files plus `Do NOT Delete These/` content that diverged from `_canonical_state/desktop/`. Ran a 5-phase reconciliation plan:

- **Phase 1 (discovery):** All 6 desktop ↔ canonical pairs hashed. 3 IDENTICAL, 1 DIVERGENT (Decisions Log — desktop is May 2 baseline, canonical has today's session work; CRLF-normalized diff shows 0 lines unique to desktop), 2 DESKTOP-ONLY (File_System_Map, Acquirer_Readiness_Checklist).
- **Phase 1.7 Gates:** Diff verification PASSED (0 lines unique to desktop). Personal-corpus grep on the 2 desktop-only files: Acquirer_Readiness_Checklist CLEAN; **File_System_Map STOPPED AND FLAGGED** (50+ explicit personal-corpus path matches including HIPAA-protected paths). Per your direction: deferred File_System_Map promotion (stays desktop-only, not in git).
- **Phase 3 execution:**
  - 3× Option A (identical pairs): desktop replaced with symlinks to canonical
  - 1× Option B (Decisions Log): desktop replaced with symlink to canonical (desktop's May 2 baseline preserved in `user_desktop_20260503_170606/` backup)
  - 1× Option E (Acquirer_Readiness_Checklist): promoted to canonical, symlinked back, **staged via `git add` but NOT committed** (your call when to commit)
  - 1× Option 2 (File_System_Map): no canonical/git action, vault symlink only
  - Adjacent scope: 4 files in `Do NOT Delete These/` ↔ `Do_NOT_Delete_These/` reconciled (all byte-identical pairs, desktop replaced with symlinks)
- **Fake-symlink incident mid-Phase-3:** initial `ln -s` from Bash produced fake file copies (Mode=-a---, full content size, no LinkType). PowerShell verification caught it. Recovered by recreating with `New-Item -ItemType SymbolicLink`. All current vault and desktop symlinks confirmed `LinkType=SymbolicLink`.
- **Phase 4 deliverable:** `_vault_only/OPERATIONAL_DISCIPLINE.md` written, codifying the discipline lessons from today's three incidents.
- **All backups out-of-band, hash-verified:** `_vault_only/reconciliation_backups/{user_desktop,canonical_state_desktop,do_not_delete_these}_<timestamp>/`
- **Boundary tests post-reconciliation: 3/3 PASSED.**

---

## Critical state to know about

| Item | State | Action needed |
|------|-------|---------------|
| Decisions Log canonical | Has today's edits + reconstruction note + retraction strikethrough | Dirty in git — user commits when ready |
| Acquirer Readiness Checklist | Promoted to canonical, staged via `git add` | Not committed — user commits when ready |
| Decisions Log desktop | Symlink to canonical (real Windows symlink) | None |
| 4 other desktop VoxCore_*.md files | Symlinks to canonical (real Windows symlinks) | None |
| 4 Do NOT Delete These desktop files | Symlinks to canonical (real Windows symlinks) | None |
| File_System_Map.md | Desktop-only by deliberate choice (NOT in canonical, NOT in git) | Future acquirer diligence package must NOT include this file |
| SL_Vault | Live, structurally sound, all 18 symlinks confirmed | Tier 4 visual Obsidian stress test pending (user must run) |
| Demo workspace boundary tests | 3/3 PASSED | None |
| Synthesis-discipline failure pattern | Named pattern with 3 measured instances (Chevron Q5, Phase 4 Q11, Phase 1 Tier 4 Q04/Q10/Q11) | Could be elevated to dedicated artifact in next session |
| Phase 5 priority list | Refined to auditor-direct-claim-context (NOT cited-chunk) + citation-path verify-retry | Implementation work pending, ~5-10 LoC for auditor fix |

---

## Pending work — post-Phase-3 cleanup list

In rough priority order. None blocking, all surfaced during today's work.

1. **Fix `demo/requirements.txt`** (~5 min). Currently lists 2 packages; 10 actually used. Real chain-of-title problem — pip install from this file fails. Recommended replacement is in `demo/INSTALL_MANIFEST.md` § 2.

2. **Implement auditor-direct-claim-context fix + re-run Q13** (~30 min). Replace the placeholder `"sentence containing the quote"` at `demo/tools/inline_auditor.py:68` with the model's actual surrounding sentence (extractable via `inline_grounding.extract_inline_quotes()` span positions). Re-run Q13; expect CONTRADICTS to drop from 2 to 0 if the diagnosis is correct. This converts a *hypothesis with a diagnostic* into a *measured correction*.

3. **Author `demo/SYNTHESIS_DISCIPLINE_FAILURES.md`** — name and catalog the failure pattern. Three measured classes: paraphrase-while-quoting (Phase 3.5 Chevron Q5), basename-instead-of-rel-path (Phase 4 Q11), cite-or-refuse coin-flip (Phase 1 Tier 4 Q04/Q10/Q11). User flagged this as the most upstream-valuable item — reframes Phase 5 from "fix bugs" to "address a named class of failure."

4. **Verify scratch-dir tripwire concern.** `demo/tools_phase4_scratch/` exists and is not gitignored. Boundary tests scan `*.py` files but no one has confirmed they cover scratch dirs. If a scratch script has a personal-corpus path, the boundary tests should catch it. If they don't, that's a tripwire gap.

5. **Tier 4 visual Obsidian stress test** (user must run, not Code). Open the vault in Obsidian; click each symlink-rendered file; verify PDF renders; do an edit-and-save through Obsidian and confirm propagation to canonical.

6. **Commit staged + dirty git changes.** `_canonical_state/desktop/VoxCore_Acquirer_Readiness_Checklist.md` (staged) + `VoxCore_Decisions_Log.md` (modified). User's call when.

7. **Safe To Delete folder review.** Surfaced 8 .md files plus PDFs, mbox, takeout-*, dev-environment.rar (655 MB). Several items NOT obviously disposable (POD case briefing, May 1/2 session handoffs, Evidence Gap Matrix). User should review before any cleanup.

8. **Handoffs folder review.** 16 files at `AI_Studio/Handoffs/voxcore/`. Vault integration was deferred per your direction. Worth a 5-min browse to decide whether they belong in the vault, archived, or stay where they are.

9. **Vision-first OCR scope axis** in CAPABILITY_SCOPE.md. Phase 4 measured Tesseract 23% CER vs vision OCR 2.6% CER on same images. Production should consider vision-first; CAPABILITY_SCOPE could elevate vision OCR from "fallback" to its own demonstrated/deferred axis with the production back-port question explicit.

10. **Achievement Record Section 3 fold-in** (user authors). Today produced one judgment moment worth capturing — the Tier 5 truncate incident + recovery + discipline codification. The Q13 diagnosis is another. User indicated they'd fold these in personally.

---

## Where things live now (canonical answer to "where is X?")

| What | Where |
|------|-------|
| Demo workspace | `C:\Users\atayl\VoxCore\demo\` |
| Demo Phase closeouts | `demo/PHASE_{1,3_5,4}_CLOSEOUT.md` |
| Demo reference docs | `demo/{INSTALL_MANIFEST,CAPABILITY_SCOPE,CORPUS_ENTITY_INVENTORY}.md` |
| Q13 diagnostic script | `demo/tools/diagnostics/diagnose_q13_contradicts.py` |
| Q13 diagnostic output | `demo/results/04_multimodal_slipfall/q13_contradicts_diagnosis.json` |
| Decisions Log (canonical) | `C:\Users\atayl\VoxCore\_canonical_state\desktop\VoxCore_Decisions_Log.md` |
| Other canonical desktop files | `_canonical_state/desktop/VoxCore_*.md` and `_canonical_state/desktop/Do_NOT_Delete_These/` |
| Desktop VoxCore_*.md files | All symlinks to canonical EXCEPT `VoxCore_File_System_Map.md` (desktop-only, deliberate) |
| SL_Vault | `C:\Users\atayl\Desktop\SL_Vault\` |
| Achievement Record | `SL_Vault\01_Achievement_Record.md` (canonical home — NOT a symlink) |
| Operational discipline rules | `SL_Vault\_vault_only\OPERATIONAL_DISCIPLINE.md` |
| Known issues log | `SL_Vault\_vault_only\known_issues.md` |
| Reconciliation backups | `SL_Vault\_vault_only\reconciliation_backups\` (timestamped, append-only) |
| Reconciliation diffs | `SL_Vault\_vault_only\reconciliation_diffs\` |
| Project PDFs (canonical) | `C:\Users\atayl\voxcore-portfolio\docs\pdfs\` (vault has 6 symlinks) |
| Handoffs (canonical) | `C:\Users\atayl\VoxCore\AI_Studio\Handoffs\voxcore\` (this file lives here) |
| Handoffs shortcut | `C:\Users\atayl\Desktop\VoxCore Handoffs.lnk` (Windows shortcut) |

---

## What I'd do differently (the honest retro)

1. **Pre-mortem before every destructive operation, not just before "obviously" risky ones.** The Tier 5 truncate looked like verification, not destruction. The truncate incident cost significant session time to recover. The OPERATIONAL_DISCIPLINE.md pre-mortem checklist was authored in response — apply it to every destructive op, even "trivial" ones.

2. **Verify language before propagating it.** The Theranos CONTRADICTS finding came from prompt language; I wrote it into the closeout and Decisions Log without checking the JSON. Same for the "sync tool hypothesis" framing in known_issues.md (which Adam later confirmed was a manual copy, not a sync tool). Rule: every claim that lands in a permanent artifact gets a source citation BEFORE it ships, not after.

3. **Use PowerShell `New-Item -ItemType SymbolicLink` for ALL symlink creation on Windows, never Bash `ln -s`.** The latter silently produces fake file copies if `MSYS=winsymlinks:nativestrict` isn't exported. The first symlink creation in Phase 3 produced 4 fake files; PowerShell verification caught it. The second time around, used PowerShell native API and it worked first try. Don't switch back to bash for this.

4. **Backups before tests, not after.** The Tier 4 protocol (Phase 1 Enron rerun) backed up `scores.json` before the destructive replication test and avoided disaster. The Tier 5 protocol skipped that backup for the Decisions Log and committed exactly the disaster Tier 4 had prevented. Always backup the artifact under test before the test.

5. **Two QA tiers per artifact: Code-side and User-side.** Code can do Tier 1-3 + Tier 5 (file inspections, hashing, scripted edit-propagation tests). User must do Tier 4 (visual rendering in the actual application). Phase 4 vault QA had a clean Tier 1-3+5 but Tier 4 (Obsidian visual) is still pending — call this out earlier next time.

6. **The synthesis-discipline failure pattern needs its own artifact.** Three independent observations across two phases is enough to name a pattern. A dedicated `SYNTHESIS_DISCIPLINE_FAILURES.md` (item 3 in Pending) is upstream-valuable — reframes Phase 5 from "fix bugs" to "address a named class of failure" which is a stronger acquirer pitch.

7. **Don't promote files into git without personal-corpus grep.** The File_System_Map almost entered git as routine cleanup. Gate 2 caught it. The grep should be a standing pre-commit check on any file containing path strings.

---

## Standing rules (carry forward)

- **Boundary tests are sacred.** Run after any file system reconciliation. 3/3 PASSED is the gate.
- **Demo workspace boundary contract:** no personal-corpus paths in `demo/` for any reason. Code or content.
- **`_canonical_state/desktop/`** is the single source of truth for working trackers. Desktop versions are symlinks to it (except File_System_Map).
- **SL_Vault is for audit-trail and demo-planning artifacts only.** Personal-case material has its own future vault (deferred decision); not in scope here.
- **Decisions Log uses strikethrough+retraction discipline for corrections.** Never delete prior entries. Append a superseding entry with explicit "Supersedes" reference.
- **Triad still applies for non-trivial work** (per CLAUDE.md P0). ChatGPT for spec, Gemini for audit. Don't brute-force everything yourself.

---

## Cost summary for this session

Approximate Anthropic API spend across all of today's work:
- Phase 4 case run (Opus 4.7 + Sonnet auditor): ~$4.55
- Phase 1 Tier 4 Enron rerun (Opus 4.7): ~$6.10
- Q13 diagnostic auditor replay: ~$0.05
- Vision OCR side audit: ~$0.02
- All other API calls (corpus generation TTS, vision captions, ad hoc): ~$0.20
- **Total session: ~$11**

Plus ~43 min of local Ollama embedding rebuild during the Tier 4 replication (no API cost).

---

*Handoff complete. Boot prompt at the top is your first message to the next tab. If you (Adam) want me to do anything else before this tab closes, say so now — context is getting tight.*
