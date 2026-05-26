---
allowed-tools: Read, Write, Edit, Glob, Bash(ls:*), Bash(cat:*), Bash(wc:*), Bash(mkdir:*), Bash(rm:*), Agent
description: Produce large documents via outline → parts/ folder → assembly. Prevents the monolithic-Write stall pattern (60+ min hangs on vocab/architecture docs).
argument-hint: <topic or path to spec>
---

# /write-large-doc — Large Document Assembly

**Evidence for this skill:** 3 documented sessions stalled 60–70 minutes each attempting single-shot Writes of large documents (vocabulary reference, architecture doc x2). 7+ sessions hit output-token-limit errors. This skill enforces the batch-first pattern that works reliably instead of the monolithic pattern that reliably fails.

## Input

`$ARGUMENTS` — the document topic or a path to a spec/outline file.

## Contract

**Never write more than 500 lines in a single Write call.** Never attempt a single consolidated Write of the final document until all parts exist in the `parts/` folder. If this contract would be violated, split further.

## Workflow

### Phase 1 — Plan the outline

1. Determine the output location:
   - If user specified a path, use it
   - Otherwise, ask: "Where should this land? (e.g. `AI_Studio/Reports/`, `doc/`, `Desktop/`)"
2. Create `<output_dir>/parts/` via `mkdir -p`.
3. Draft the section outline as markdown:
   ```markdown
   # <Title>

   ## Sections
   1. <section name> — <1-line purpose> (~<N> lines estimated)
   2. ...
   ```
4. Write the outline to `parts/00-outline.md` (single small Write, always fine).
5. **Pause and tell the user:** "Outline drafted at `parts/00-outline.md`. Review and approve/adjust before I launch writers. If approved as-is, reply 'go'."

### Phase 2 — Writer dispatch

After approval, choose ONE of two modes based on document size:

**Mode A — Sequential (≤6 sections, not time-critical):**
Write each section to `parts/NN-section-slug.md` in order. One Write call per file. Under 500 lines per file.

**Mode B — Parallel (7+ sections OR time-critical):**
Launch N parallel writer agents using the Agent tool, one per section. Each agent:
- Gets the outline + its section assignment + word budget
- Reads any cited source material via Read (not included in the prompt if large — give the path)
- Writes ONE file: `parts/NN-section-slug.md`
- Must stay under 500 lines or it has failed the contract

Example parallel dispatch: "Use 8 parallel general-purpose agents, one per vocab category. Agent N writes only `parts/NN-category-slug.md`. Word budget 800 per file. Required citation format: `[source: filename]`."

### Phase 3 — Verification

After all `parts/NN-*.md` files exist:
1. Run `wc -l parts/*.md` to confirm sizes.
2. If any part exceeds 500 lines, split it further — do not proceed.
3. Run a verifier pass: read each part, confirm it matches its outline section. If a section is missing, dispatch a fix agent for just that section.
4. Check cross-references — if section 3 references section 5 terminology, confirm consistency.

### Phase 4 — Assembly

1. Determine final filename (ask user if unclear).
2. Concatenate in order:
   ```bash
   cat parts/00-outline.md parts/01-*.md parts/02-*.md ... > <final>.md
   ```
   Or use a Python script if reflow/TOC generation is needed.
3. **Assembly is a Bash concat, not a Write.** The final document is the union of already-written small files — we do NOT re-Write it all at once.
4. Report: final path, total lines, and a 3-bullet summary of coverage.

## Hard Rules

1. **Never skip the outline-approval pause.** The 70-minute stalled sessions happened because Claude started writing without confirming structure.
2. **Never write a single part larger than 500 lines.** If a section would exceed that, split it into `NN-section-A.md`, `NN-section-B.md`.
3. **Never attempt a single consolidated Write of the final document.** Assembly is Bash concat.
4. **Never lose a part.** If a writer agent returns partial output, re-dispatch that ONE section, do not restart the whole doc.
5. **When citation fidelity matters** (resumes, legal filings, federal applications), use Mode A sequential — parallel agents can drift on cited facts.

## When NOT to use this skill

- Documents under ~500 lines total — just Write directly.
- Content that must be a single logical stream with no section breaks (rare).
- When the user has explicitly said "write it inline" or "just show me."

## Follow-on patterns

- For the Treasury Gatsby analysis: use Mode A sequential (citation fidelity matters, only 10 pages ≈ 6-8 sections).
- For the CalmCore architecture doc that stalled twice: use Mode B parallel (many independent subsystems).
- For generated reference material (vocab, API digests): Mode B parallel.

## Related

- `PreToolUse:Write` hook `check_write_size.py` enforces the 1500-line ceiling automatically. This skill works BELOW that ceiling by design (500-line soft cap).
- `/mega-doc` (not yet built) will be a more automated version of this workflow with a planner agent + verifier agent baked in.
