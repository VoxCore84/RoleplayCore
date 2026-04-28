---
description: "Triad AI pipeline — review, spec generation, endpoint testing, and orchestration"
---

# /triad — Unified Triad Pipeline Skill

Parse `$ARGUMENTS` to determine which subcommand to run. If no arguments or unrecognized, show the help text below.

## Subcommands

### `test` — Test all 4 reviewer endpoints
Run: `python tools/ai_studio/review_cycle.py --test`
Report results inline. All 4 should say OK (Codex, ChatGPT, Gemini, Claude).

### `review <file> [options]` — Run the parallel review cycle
Run: `python tools/ai_studio/review_cycle.py --file <file> [flags]`

Options to pass through:
- `--rounds N` — limit to N rounds (default 5)
- `--skip-claude` — skip Claude API cold-reader
- `--use-chatgpt-api` — use ChatGPT API instead of Codex CLI
- `--sequential` — use old sequential pipeline instead of parallel
- `--context-files FILE [FILE ...]` — prepend context files for reviewers

After the script completes:
1. Read the summary file it created in `AI_Studio/Reports/Audits/`
2. Report the final verdict (PASS/FAIL), wall time, and per-round results
3. If FAIL, list the CRITICAL and HIGH findings from the summary

### `spec <intake-file>` — Generate a spec via ChatGPT API Architect
Run: `python tools/api_architect/run_architect.py --intake <intake-file> --mode spec`
The spec lands in `AI_Studio/1_Inbox/`. Report the output path.

### `spec-dry <intake-file>` — Dry-run spec generation (no API call)
Run: `python tools/api_architect/run_architect.py --intake <intake-file> --mode dry-run`
Validates the pipeline without spending API credits.

### `bridge [file]` — Review spec(s) via ChatGPT bridge
If `<file>` provided: `python tools/ai_studio/chatgpt_bridge.py --file <file>`
If no file: `python tools/ai_studio/chatgpt_bridge.py` (processes all specs in Inbox)
Report which specs were APPROVED vs REJECTED.

### `orchestrate <prompt>` — Run the full Triad orchestrator
Run: `python tools/ai_studio/orchestrator.py "<prompt>"`
This runs Gemini (Architect) -> Claude (Executor) -> Gemini (Auditor) loop.
Report each phase result and whether the auditor passed.

### `review-subagent <file>` — Review with Claude Code subagent as 5th reviewer
1. First run the standard review cycle: `python tools/ai_studio/review_cycle.py --file <file> --skip-claude`
2. Read the generated summary from `AI_Studio/Reports/Audits/`
3. Spawn a Claude Code subagent (using the Agent tool) with this prompt:

```
You are the 5th reviewer in the VoxCore Triad review pipeline. You have FULL repo access.
Your unique value: You can read any file in the project, verify claims against actual code,
and check integration points that API-only reviewers cannot.

Review this artifact with repo-aware fresh eyes:

<artifact>
{file contents}
</artifact>

Prior feedback from other reviewers:
{condensed findings from the review cycle summary}

Instructions:
- Read referenced source files to verify claims
- Check that SQL column names match actual schema
- Verify function signatures exist where referenced
- List findings as: **[SEVERITY]** (CRITICAL/HIGH/MEDIUM/LOW/INFO) — description
- Group by: Verification, Integration, Correctness, Edge Cases
- End with VERDICT: PASS or FAIL
```

4. Combine the subagent's review with the review_cycle summary
5. Report the combined verdict

## Help Text (shown when no args)
```
/triad — VoxCore Triad AI Pipeline

Usage:
  /triad test                     Test all 4 reviewer endpoints
  /triad review <file>            5-round parallel review (Codex + Gemini + Claude)
  /triad review-subagent <file>   Review + Claude Code subagent as 5th reviewer
  /triad spec <intake-file>       Generate spec via ChatGPT API Architect
  /triad spec-dry <intake-file>   Dry-run spec (no API call)
  /triad bridge [file]            Review spec via ChatGPT bridge
  /triad orchestrate "<prompt>"   Full Triad loop (Gemini->Claude->Gemini)

Reports saved to: AI_Studio/Reports/Audits/
Fleet: ChatGPT (gpt-5.4) | Gemini (gemini-3.1-pro) | Claude (claude-opus-4-7) | Codex CLI
```
