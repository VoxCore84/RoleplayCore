# Session 288b — 2026-09-22 (evening) — Claude Code audit v3: review, execute, verify, wrap

**Session:** 288b (same day as 288, same model Fable 5.1 xhigh, session id 6dce2cb5) · **Duration:** ~17:10–19:50 local (review + v3 authoring ~60 min, execution ~90 min incl. one user interruption, wrap-up ~20 min) · **Commits:** `acd8ed1f06` (audit infra), `047fad20cc` (CLAUDE.md dedupe), wrap-up docs commit follows this file (see `docs/VOXCORE_HANDOFF_INDEX.md`) · **API spend:** plan usage only, no usage credits; 5 headless sessions + 5 subagents; dollars not measured.

## What happened this session

**Round 1, review.** Adam handed over an externally authored optimization prompt (v2). Instead of running it, every claim was grounded against the machine: settings files, today's sweep ledger, the 2.1.280 changelog, binary string counts, session-stats latency, Defender state, Bash spawn timing, and a claude-code-guide agent that checked 22 doc claims (7 came back false). v3 was written to `Desktop/Excluded/claude-code-optimization-prompt-v3.md`: it drops what v2 got wrong for this box (auto mode, per-Bash Python hooks, a build filter that matches nothing here, commands-to-skills migration, a login-shell premise), keeps what was right, and bakes in house tooling and lessons.

**Round 2, decisions.** Adam set the standing priority "most powerful responses first, efficiency second" (`memory/feedback_power_over_efficiency.md`), which fixed Fable 5.1 at xhigh, kept the permission posture and the non-essential-traffic flag, and approved the three sweep leftovers. Step 0 shrank from four questions to none.

**Round 3, execution.** Phase 1 baseline (61.1k live), Phase 2 fifteen items, Phase 3 verification, Phase 4 reports. One interruption mid-wave (all 13 calls rejected cleanly, nothing half-written); resumed with the Explore override dropped after the probe showed the built-in already runs Opus 5.5. The new guard blocked the audit's own test loop and a ledger append, which led to the heredoc-aware fix. A Sonnet subagent ported the dead test suite (22/22) and found a latent release-gate bug, fixed. Three context captures isolate each change class; an experiment capture prices the unshipped option.

**Round 4, wrap-up.** Two commits (audit infra; CLAUDE.md separately because it carries 31 pre-existing uncommitted lines), memory + ledger + resume evidence, four quick wins built at the gate (`PYTHONUTF8=1` env pin, `tools/daemon_restart.ps1`, checklist items 11–12, agent-practices report-to-file line).

## Headline numbers

| Claim | Value | Confidence | Evidence |
|---|---|---|---|
| Live per-turn context | 61.1k → 57.8k (−5.4%) | MEASURED, two-capture method | `AI_Studio/Reports/context_captures/20260922_180418_v3_before.md`, `..._190315_v3_mid_alwaysload.md`, `..._190535_v3_after.md` |
| Unshipped option: defer last 3 MCP servers | 57.8k → 52.0k | MEASURED, reverted | `..._190915_v3_exp_all_deferred.md` |
| Hook regression suite | 0/17 → 22/22 scenarios (+13/13 HTTP) | FUNCTIONALLY VERIFIED | `test-hooks.py --all`, ledger row 27 |
| Destructive-command guard | 21/21 route matrix; 3 real-path proofs | FUNCTIONALLY VERIFIED | `cc_audit_v3_20260922-1804/guard_smoke.py`, ledger rows 19–20, 26 |
| Docs verification of the external prompt | 22 claims, 7 false | VERIFIED against live docs | v3 file § Docs verification |
| Latent bug fixed | release gate never matched PowerShell archive commands | FUNCTIONALLY VERIFIED (blocked a command after the fix) | ledger rows 28, 30 |

## State-of-the-world warnings

- **Guard semantics:** the daemon now blocks force-push, hard reset, `git clean`, whole-tree checkout, recursive deletes outside `_scratch/`, `.claude/worktrees/`, `AI_Studio/Reports/tmp/`, and game-DB imports without `db_snapshot.py` in the same command. It also matches those phrases when they appear as quoted data on a Bash command line (heredoc bodies fed to files are exempt; interpreter-fed bodies are not). Write such text with the Write/Edit tool. CalmCore gets the route only after the handoff registers it.
- **Uncommitted, deliberately:** `tools/citation_scorer.py`, `tools/excluded_hybrid_search.py`, `tools/quality_probe.py`, `tools/sync_canonical_state.py`, six `_canonical_state/*` files, `.claude/commands/deep-investigate.md`, `.claude/commands/ex-ask.md`, `doc/session_state.md`, `AI_Studio/Handoffs/voxcore/_INDEX.md` — all pre-date this session (owner decision, s.286 consolidation arc). `CLAUDE.md` WAS committed (its 31 pre-existing pointer lines plus the dedupe, in one commit `047fad20cc`; separate diffs in the audit folder if you want to split it).
- **Gitignored but changed:** `.mcp.json` (two WoW servers deferred), `.claude/settings.local.json` (13 shadowed rules removed, `local-llm` allow-listed). Backups beside each file and in `cc_audit_v3_20260922-1804/backup/`.
- **User scope changed for both repos:** `~/.claude/settings.json` (inert keys removed, Opus 5.5 effort `high`, fast-mode per-session opt-in, `enableAllProjectMcpServers=false`, `PYTHONUTF8=1`), `~/.claude/statusline-command.py`, `~/CLAUDE.md`. CalmCore's allowlist was widened to all 8 servers BEFORE the flag flip; do not roll one back without the other.
- **`session_state_live.md` was overwritten once** by a headless `/doctor` probe that ran the project skill; rewritten at 19:30. Headless slash probes are unsafe except `/context` and `/usage` (checklist item 11).
- **The Section 1983 statute of limitations entry is due 2026-09-23; four deadline entries are past due.** Not touched by this session.

## What's real (measured)

| Dimension | Value | Source |
|---|---|---|
| Claude Code | 2.1.280 npm-global; `claude doctor` clean | `claude --version`, `claude doctor` |
| Model pins | main `claude-fable-5-1` xhigh (modelSettings); subagents `claude-sonnet-5`; built-in Explore inherits → `claude-opus-5-5[1m]` | headless canary, gp-canary, explore-probe-before |
| Live context | 57.8k of 1M (MCP live 6.4k, memory files 30.9k, system tools 10.5k, skills 4.4k, system prompt 3.8k, agents 1.7k) | capture 190535 |
| Hooks | VoxCore 40 handler entries / 13 events; daemon v1.3.1 | `check_hook_sync.py`, `/health` |
| Tests | Health 2/0, Scenarios 22/0, HTTP 13/0 | `test-hooks.py --all` |
| 30-day tool latency | Bash p50 0.42 s (n=154); WebFetch p50 7.4 s; WebSearch p50 13.4 s | `session-stats.jsonl` |
| Defender | RT on; 15 path + 19 process exclusions; missing CalmCore, Git dir, bash.exe | `Get-MpPreference` |
| Plugins | clangd-lsp, lua-lsp, github enabled; code-review disabled | `claude plugin list` |

## Files to read at session start

```
Read docs/VOXCORE_HANDOFF_INDEX.md
Read AI_Studio/Handoffs/voxcore/2026-09-22_session_288b_cc-audit-v3.md
Read AI_Studio/Reports/cc_audit_v3_20260922-1804/REPORT.md
Read AI_Studio/Handoffs/voxcore/2026-09-22_cc_audit_v3_followup_prompt.md
Read tasks/windows-shell-checklist.md
Read tasks/lessons.md
Read ~/.claude/projects/C--Users-atayl-VoxCore/memory/claude-code-config-state.md
Read ~/.claude/projects/C--Users-atayl-VoxCore/memory/feedback_power_over_efficiency.md
Read ~/.claude/projects/C--Users-atayl-VoxCore/memory/todo.md   (## Next Session)
```

## Top priorities for next session (from todo.md § Next Session)

1. `/start-up`, then the USER-RUN checks (`/status`, `/model`, `/effort status`, `/hooks`, `/mcp`, `/permissions`, `/plugin`, `/usage`) and confirm Python stdout is utf-8.
2. CalmCore tab: paste the follow-up prompt (fill its three answers): guard registration, status rename, `.clangd` LSP test, allowlist prune, duplicate hook blocks, `/sync-infra`, optional defer of the last three MCP servers (−5.8k measured) and `askUserQuestionTimeout`.
3. Adam decisions: Defender block; rules demotion (recommended against); one home for the `session_state.md` protocol; Remote Control / auto mode (currently no).
4. Owner-decision uncommitted files (s.286 consolidation arc), then Memory Control Plane v0.1 integration.
5. GO on the 28 `tools/` scripts still on Claude 4.x model IDs.
6. Deadlines: four past-due entries + Section 1983 SOL.
7. Carry-over s.287: counsel cockpit review; encrypted transmission to Nancy; 13 missing-evidence files. Nothing sent.

## Standing directives (unchanged, plus this session's)

- Legal accuracy: 100%; cite statutes; distinguish known/told/documented; never fabricate. The 3 CRITICAL corrections must never regress (DoDSER = non-completion not falsification; OPB 121 not 164; Taylor signed rebuttal / Tolin transmitted).
- No production code changes without Adam GO. Triad for non-trivial implementation. Cite source on every measured claim.
- `Case_Reference/` READ-ONLY. Clinical (L5) verbatim only. Confidence tiers on evidentiary claims.
- `VoxCore_File_System_Map.md` desktop-only — never git-add. Memory repo: never push.
- External POD build NOT distributable without counsel redaction policy.
- From 288: keep `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`; never recommend `/skill-doctor` (use `tools/skill_audit.py`); `excluded-corpus.md` untouchable; `skillOverrides` is for behaviour, not tokens; grep `claude.exe` before removing/renaming any env key; for git-tracked JSON edit lines, never `json.dump`.
- **New (288b):** power first, efficiency second (`memory/feedback_power_over_efficiency.md`): Fable 5.1 xhigh everyday, no auto mode, savings only via subagent routing / effort tiers / session-only effort drops. Built-in Explore stays on its inherited model (no override). Token claims need `cc_context_capture.py` totals. Verify externally authored Claude Code claims with a docs agent before executing them. Restart the daemon only with `tools/daemon_restart.ps1`.

## Workflow reminders for the next tab

- Subagents run Sonnet 5 natively at 1M; no credit gate. Built-in Explore/Plan ignore the subagent pin.
- Headless `/context` from PowerShell only (`tools/cc_context_capture.py` handles it); other headless slash commands run project skills of the same name.
- Background-agent mailbox reports arrive at the lead's turn end; mid-turn, parse `subagents/agent-*.jsonl`. Give report agents a file path.
- A guard-blocked Bash command means the phrase was on the command line; move it to a file or use Write/Edit.
- Bash tool spawn is 90 ms; the 3.3 s all-time median was history. Don't chase shell speed.

## Provenance

Generated 2026-09-22 ~19:50 by session 6dce2cb5 (Fable 5.1). Session totals: 1 spec authored (v3, 282 lines) + 1 follow-up prompt; 22 doc claims verified; 31 ledger rows; 4 context captures; 3 subagent probes + 2 verification/port agents; 2 commits + wrap-up docs commit; 4 quick wins; files written/edited: 24 in-repo and user-scope, 6 memory files.
