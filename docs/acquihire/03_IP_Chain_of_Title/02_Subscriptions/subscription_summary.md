# VoxCore — AI Subscription Audit

**Folder:** `03_IP_Chain_of_Title/02_Subscriptions/`
**Generated:** 2026-05-02
**Owner:** Adam Taylor
**Source-of-truth:** `~/.claude/projects/C--Users-atayl-VoxCore/memory/ai-subscription-audit.md` (consumer/cost) + this file (diligence format).

This document answers the diligence question: **"Were any subscriptions used in VoxCore development paid by the government or by a prior employer?"** Answer: No. Every subscription is personally paid; receipts available on request.

---

## Subscription Inventory

| # | Service | Tier | Monthly | Account Holder | Payment Method | Used in VoxCore |
|---|---------|------|---------|----------------|----------------|-----------------|
| 1 | **Anthropic Claude Max** | 20x | $200 | Adam Taylor (utiignis@gmail.com) | Personal credit card | YES — primary CLI orchestrator (Claude Code) |
| 2 | **Anthropic API** (console) | Pay-as-you-go | variable | Adam Taylor | Personal credit card | YES — citation-scorer LLM-as-judge fallback, Section 16 calibration |
| 3 | **OpenAI ChatGPT Pro** | Pro | $200 | Adam Taylor | Personal credit card | YES — Architect role in Triad orchestration |
| 4 | **OpenAI API** (platform) | Pay-as-you-go | variable | Adam Taylor | Personal credit card | YES — Codex on shared OpenAI API |
| 5 | **Google AI Ultra** | Ultra | $249.99 ($130.88 promo to Jun 9 2026) | Adam Taylor | Personal credit card | YES — Auditor role (Gemini), 30TB Drive backup |
| 6 | **Google Cloud Platform** | Free + signup credits | $0 (covered by credits) | Adam Taylor | Personal credit card on file | OPTIONAL — not currently used in VoxCore prod |
| 7 | **xAI SuperGrok** | Standard | $30 | Adam Taylor | Personal credit card | OPTIONAL — Grok 4.1 Fast as cheap reviewer (post-acquihire candidate) |
| 8 | **Oracle Cloud** | Always Free | $0 | Adam Taylor | N/A (free tier) | NOT USED — separate project (DraconicBot VM) |
| 9 | **AWS** | Free Tier (closing) | $0 | Adam Taylor (atayl05) | N/A | NOT USED — being closed |

**Total monthly out-of-pocket:** ~$680 (promo) / ~$800 (full) depending on Google Ultra promo state. Plus pay-as-you-go API spend (variable, typically $50-200/mo combined).

---

## Personal-Payment Confirmation

### Negative attestations (each verifiable from billing portal)

| Attestation | Evidence available |
|-------------|-------------------|
| Zero government-credit-card (GTC, GPC, IMPAC) charges on any AI service | Per-service billing history download |
| Zero government-procurement-system payments | Federal procurement systems (FPDS-NG, beta.SAM.gov) have no entries for any of these accounts |
| Zero employer/contractor-paid subscriptions | No prior tech-employer relationship; military duty positions are clinical (then administrative), no IT acquisition role |
| Zero shared-account access by anyone other than Adam | No team seats, no admin delegation, no SSO from any external org |

### Account-holder identity

All 9 accounts in the table above are registered to **Adam Taylor** at personal email addresses (primary: `utiignis@gmail.com`, secondary: `ataylor7176@gmail.com`). No `.mil` email anywhere in the account hierarchy.

---

## Per-Subscription Diligence Notes

### Anthropic Claude Max + API

- **Why it matters:** Claude Code is VoxCore's primary CLI / Executor role. Without Max, the system has no orchestrator.
- **Auth model:** Claude Code routes through OAuth on the Max sub (not API key). API key is used only for offline scripts (`citation_scorer.py --judge claude`, `legalbench_harness.py --model opus`).
- **Risk note:** If `ANTHROPIC_API_KEY` is in `os.environ`, Claude Code bypasses Max sub and bills API directly. Memory file documents the routing.
- **Documentation needed in folder 02:** Annual billing summary export, account-creation date, payment-method last-4.

### OpenAI ChatGPT Pro + API

- **Why it matters:** ChatGPT Pro funds the Architect role in the Triad. Codex CLI shares the same OpenAI API.
- **Pre-acquihire migration:** Assistants API sunsets 26 Aug 2026 — need to migrate to Responses API on the same timeline as the acquihire close.
- **Documentation needed:** Same — billing summary, payment method.

### Google AI Ultra + GCP

- **Why it matters:** Gemini = Auditor role. The 30TB Drive bundled with Ultra acts as off-machine backup for the case archive.
- **Promo expiry:** Discount drops 9 Jun 2026 (3 months pre-separation); expense rises ~$120/mo for the deal-close window.
- **Documentation needed:** Same.

### xAI SuperGrok

- **Why it matters:** Currently optional. Listed in case acquirers ask about reviewer fan-out posture.
- **Documentation needed:** Same.

### Oracle Cloud + AWS

- **Why it matters:** Out of scope for VoxCore. AWS is being closed; Oracle hosts an unrelated Discord bot.
- **Documentation:** Confirmation of zero VoxCore-related resources.

---

## Boundary statement

VoxCore was developed using consumer AI subscriptions at premium tiers, all paid from personal funds. No portion of the development used:

- Government-paid AI services (none exist for the user's commands)
- Employer-paid AI services (no concurrent civilian employer)
- Shared/team-account AI services (no team seats anywhere)
- Free-trial-credit access that would create vendor relationships at the deal close

The acquirer takes IP free of any subscription-derived encumbrance. Subscriptions remain personally-held post-close; the acquirer provisions their own equivalent infrastructure on Day 1.

---

## Refresh triggers

Update this file when:
- New subscription added to the development stack
- Existing subscription canceled
- Account email changes
- Payment method changes
- Any subscription moves from personal-funded to employer/government-funded (none expected)

---

*Companion to:* `03_IP_Chain_of_Title/01_Hardware/` (hardware receipts) and `03_IP_Chain_of_Title/00_Summary/` (summary affidavit). Affidavit point #3 ("Development conditions — affirmative") references this audit.
