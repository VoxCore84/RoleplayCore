---
description: "AI subscription strategy and fleet management — Claude, ChatGPT, Gemini, Grok roles, budget allocation, automation plan with Anthropic API"
---

# AI Strategy & Automation Plan
Created: Session 115 (Mar 8 2026). Status: **PLANNING — not yet implemented.**

## Budget: ~$1,000/month

### Active Services

| Service | $/mo | What it does for us |
|---------|------|---------------------|
| **Claude Max (Account A)** | $200 | Primary dev — Claude Code (C++, SQL, debugging, 22 skills) + Cowork (when stable) |
| **ChatGPT Pro** | $200 | Codex CLI, second opinions, architecture reviews, deep research (e.g., Gemini Ultra writeup) |
| **Gemini Advanced** | $20 | 1M token context — paste entire subsystems and ask questions in one shot |
| **Grok (Super)** | current | General research, different reasoning perspective |

### TODO — Purchase

| Service | $/mo | Priority | Why |
|---------|------|----------|-----|
| **Claude Max (Account B)** | $200 | **#1 — do this first** | Overflow when Account A maxes out (~Wednesday). $200/mo vs $300-400/day on API |
| **Anthropic API credits** | ~$5-50 | #2 | For automation scripts (Sonnet is $3/$15 MTok — pennies per run) |

### Evaluated & Skipped

| Service | $/mo | Why skip |
|---------|------|----------|
| ~~GitHub Copilot~~ | $19 | User never types code in VS — Claude Code writes everything |
| ~~Perplexity Pro~~ | $20 | Local tooling (wago MCP, wow.tools.local, WebSearch) covers research |
| ~~Gemini Ultra~~ | $250 | Only unique win is NotebookLM at scale. Try at $125 intro if curious, skip at $250. Jules/CLI/Antigravity redundant with Claude Code |

---

## Claude Max Dual-Account Setup

1. Create second Anthropic account (different email)
2. Subscribe to Max ($200/mo)
3. Switch in Claude Code: `claude auth logout && claude auth login` (10 seconds)
4. Switch on web: use separate Chrome browser profiles (both stay logged in)
5. Local settings (CLAUDE.md, memory files, project config) persist across account switches
6. Conversation history is per-account on web; Claude Code sessions are local
7. Timing: Account A Mon–Wed, switch to Account B when A hits limit
8. Both reset on own weekly cycles (based on subscription start date)
9. Alternative: set `ANTHROPIC_API_KEY` env var to use API credits without switching OAuth login

---

## Which AI for What

| Task | Best Tool |
|------|-----------|
| C++ implementation, SQL gen, debugging, skills | **Claude Code** |
| Scheduled audits, overnight research, doc gen | **Cowork** (when stable — currently crashes, Mar 2026) |
| Paste 5000-line file and ask "what's wrong?" | **Gemini Advanced** (1M context) |
| Architecture review, second opinion, deep analysis | **ChatGPT Pro** |
| Automated DB health checks, nightly scripts | **Anthropic API (Sonnet)** via Task Scheduler |
| Quick questions when Claude is throttled | **ChatGPT / Gemini / Grok** |

---

## Automation Plan

### Path A: Cowork Scheduled Tasks (BLOCKED — app unstable)

Cowork now supports scheduled tasks (daily/weekly/hourly). Tasks designed in `cowork-setup.md` Step 5:
- Morning briefing (weekdays 7am)
- Weekly doc freshness audit (Sunday 10pm)
- Weekly code consistency scan (Saturday 11pm)
- On-demand gist sync check

**Blocked**: Cowork crashes / won't stay open. Revisit when Anthropic fixes stability.

### Path B: Anthropic API + Task Scheduler (READY when API key obtained)

Requires:
1. Anthropic account at console.anthropic.com
2. Add billing (credit card, pay-as-you-go)
3. Generate API key
4. `pip install anthropic`
5. Set `ANTHROPIC_API_KEY` environment variable
6. Write Python scripts (same pattern as existing 93 scripts in wago/)
7. Schedule with Windows Task Scheduler

**Model choice for automation:**

| Model | Input | Output | Use for |
|---|---|---|---|
| Sonnet 4.6 | $3/MTok | $15/MTok | Batch analysis, summaries, routine checks |
| Haiku 4.5 | $0.80/MTok | $4/MTok | Simple classification, formatting, routing |
| Opus 4.6 | $15/MTok | $75/MTok | Complex reasoning (only if needed) |

A nightly DB audit calling Sonnet costs ~$0.05-0.15 per run ($1.50-4.50/month).

**Example automation script pattern:**
```python
import anthropic
from pathlib import Path

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

# Run existing audit script or read log file
audit_output = Path("path/to/output.txt").read_text()

# Ask Sonnet to analyze
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    messages=[{"role": "user", "content": f"Analyze this audit:\n{audit_output}"}]
)

# Write summary
Path("doc/nightly_audit.md").write_text(response.content[0].text)
```

**Candidate automation scripts to build:**
- [ ] Nightly DB health check (run `world_health_check.py` → Sonnet analysis → `doc/nightly_audit.md`)
- [ ] DBErrors.log monitor (tail last 100 lines → categorize → alert if new error types)
- [ ] Weekly gist freshness check (diff gist source files → report which need updating)
- [ ] Batch spell audit (feed 84 YELLOW spells → prioritized fix list)
- [ ] Auto bridge sync with analysis (what changed since last sync)

---

## Gemini Ultra — Full Evaluation (from ChatGPT 5.4 review)

**Price**: $249.99/mo ($124.99/mo intro for 3 months)

**Features that matter for our workflow:**
- **NotebookLM** (best feature): 500 notebooks, 600 sources each, citation-grounded. Could load all transmog docs + DeepDive + packets. But we already have 26 memory files + Claude Code context.
- **Jules** (async coding agent): 300 tasks/day, 60 concurrent. But our project is too specialized — Jules lacks the 114-session context Claude Code has.
- **Gemini CLI / Code Assist**: 2,000 requests/day. Redundant with Claude Code.
- **Antigravity**: Multi-agent platform, preview. Interesting but not mature.
- **YouTube Premium + 30TB storage**: Nice perks, not dev value.

**Verdict**: Skip at $250/mo. Consider $125 intro to evaluate NotebookLM. The 1M context window (the killer feature) is already in the $20 Advanced plan.

---

## CLAUDE.md Changes Made (Session 115)

1. **Session Start auto-reads** `doc/session_state.md` + `todo.md` — no `/session-start` needed
2. **Multi-Tab Delegation** rewritten as BLOCKING OBLIGATION with 7 hard triggers
3. **Proactive Skill Reminders** table — 10 triggers that require Claude to remind/run slash commands

These are already live in CLAUDE.md.
