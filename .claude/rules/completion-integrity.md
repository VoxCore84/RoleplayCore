# Completion Integrity — Anti-Theater Protocol (P0 Reliability)

This exists because Claude Code has a systemic pattern of reporting tasks as complete when they are not.

## Core Rule
**Never claim completion without showing evidence.** "I did X" requires tool output proving X happened. No tool output = no claim.

## Prohibitions

1. **No unverified success claims.** "Zero errors", "applied cleanly", "all passed" requires quoting actual tool output. If you didn't check, say "I didn't verify this."

2. **No tautological QA.** Before running a verification query, ask: "Can this query return a failure result?" If no — it's not verification. Examples of tautological QA:
   - Checking row counts after INSERT without knowing expected count
   - Running EXISTS on a table you just inserted into
   - Comparing counts that include pre-existing + new data

3. **No checklist amnesia.** Track each step in numbered lists. Before completion summary, re-read source document and enumerate which steps were done/skipped.

4. **No confidence inflation.** Match tone to evidence:
   - OK: "Applied 7 SQL files. mysql reported 0 warnings. DBErrors.log shows no new entries since [timestamp]."
   - BAD: "All 7 files applied cleanly — zero errors!"
   - OK: "I applied the file but didn't check the error log — want me to verify?"

5. **No omission-by-summary.** If 5 requested and 4 done, say "4 of 5 done — [item] not completed because [reason]."

6. **No unvalidated artifacts.** DESCRIBE target table and verify column count matches VALUES count before claiming SQL is correct.

## Mid-Task Verification Gates
Do NOT batch verification to the end. Each step is its own gate:
- After each SQL file: check output before next file
- After each code generation: verify column count NOW
- After reading coordination doc: extract actionable items NOW

## Default to Verification
If about to state a fact about schema/columns/counts without a tool call THIS session — verify now or flag as unverified. "I believe the column is X but haven't checked" is acceptable. Stating as fact is not.

## Ask Before Skipping
If a documented step exists and you're about to skip it, ASK. Never silently skip.

## Capture Corrections (lessons loop)
After ANY user correction, rejection, or surprising failure, append an entry to `tasks/lessons.md` (**Context** / **Lesson** / **Rule**) before continuing other work. This is not optional bookkeeping — it is how the same mistake is prevented next session. A correction that isn't written down recurs. Keep entries tight (the file is read every session). When a lesson recurs 3+ times, promote it into a `.claude/rules/*.md` file and leave a pointer.

## Verify-before-recommend (harvested-claim gate)
A claim from an external source — screenshot, blog, influencer post, another AI's output, a tool's README — is a **LEAD, not a fact**. Before it becomes an actionable recommendation ("build / use / enable / install X"), verify it against an authority:
- **Claude Code / API features** → live docs (spawn `claude-code-guide`) or context7, AND the actual `settings.json` / code.
- **Third-party tools** → the real repo / package registry (does it exist? maintained?).
- **Metrics / savings / benchmarks** → read the actual code path and measure (token counts, call shape) before quoting a number.
- **Anything from image OCR** → the source image or authoritative docs (bulk OCR garbles exact values — see `tasks/lessons.md`).

Tag every harvested claim **VERIFIED / UNVERIFIED / FALSE**. Unverified claims may be listed as EXPERIMENTAL but MUST NOT enter a Tier-1 "do this" recommendation. Applies to FINDINGS-style reports and any harvest/research output.

Why (2026-05-25 catches): `autoUpdaterStatus` was not a real key; `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` was misnamed (missing `_CODE_`); `CLAUDE_CODE_MAX_TURNS` unconfirmed; a "~$21/run caching saving" evaporated when the real prompt was 169 tok (< 1024 cache floor); 30% of dense harvested screenshots had major transcription errors. The gate caught all of these before they shipped as production changes.

## Mandatory Completion Checklist
Before ANY completion summary:
1. Re-read source instructions
2. Enumerate each step with evidence
3. Check for post-action verification steps
4. Check session_state.md
5. State what you did NOT do
