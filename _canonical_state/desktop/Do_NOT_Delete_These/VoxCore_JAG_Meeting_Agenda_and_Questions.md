# JAG Ethics Counsel Meeting — Agenda & 20 Prep Questions

**Purpose:** Standalone artifact for Adam to bring to the JAG ethics meeting. Hand the SJA a copy at the start of the meeting; this is what Adam needs answered.

**Meeting goal:** obtain a written ethics opinion confirming what activities are permitted during the ADSC tail period (ADSCD 10 Aug 2026) for acquihire planning. Specifically: outside-employment activities, IP transfer planning, term-sheet discussions, due-diligence cooperation, post-employment restrictions.

**Meeting scope:** ~60 minutes. Take notes; request the written opinion within 14 days of the meeting.

---

## Suggested 60-min Agenda

| Minute | Topic |
|---|---|
| 0-5 | Introductions; confirm scope (off-duty employment + acquihire-specific activities, NOT case-related ethics) |
| 5-10 | Hand SJA the System Description one-pager (next section of this doc) — establish context |
| 10-25 | Walk through the 20 prep questions (group A: outside-employment; group B: acquihire-specific; group C: post-separation) |
| 25-40 | SJA's questions back to Adam — answer fully |
| 40-50 | Discuss disclosure obligations to chain of command — explicit yes/no |
| 50-55 | Confirm written-opinion timeline (target: within 14 days) |
| 55-60 | Note any follow-up needed (additional documentation, second meeting, etc.) |

---

## System Description — One-Pager for SJA

**To hand to the SJA at the start of the meeting:**

> **Software Project: VoxCore (Personal Off-Duty Development)**
>
> **What it is:** A local-only retrieval and citation system for high-stakes evidence work. Built solo on personally-owned hardware during off-duty hours. No DoD or Air Force data. No government-furnished equipment. No .mil network access. No employer-paid software subscriptions.
>
> **When built:** Roughly February 2026 to present (3 months as of meeting date).
>
> **Hardware:** Personally-owned workstation (Ryzen 9 9950X3D / RTX 5090 / 128GB RAM / NVMe). Documented in `docs/ENVIRONMENT.md`. No GFE.
>
> **Software:** Open-source C++/Python/SQLite stack plus personally-paid AI subscriptions (Claude Max, ChatGPT Pro, Google AI Ultra, Anthropic API). Documented in `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/subscription_summary.md`.
>
> **Network:** Home internet only. No work-from-anywhere DoD VPN. No CAC-required services.
>
> **Data:** Personal corpus only — Captain Taylor's own legal case files, personal financial documents, personal correspondence. No DoD, no .mil, no government-owned data.
>
> **Current status:** Working software with measured performance metrics. Held-out hallucination rate 24.7% with 100% fabricated-quote detection (per the project's verification artifacts). Documented for diligence-grade external review.
>
> **Acquihire interest:** Captain Taylor is exploring private-sector acquihire conversations for skills demonstrated by the system, with separation 10 Aug 2026 (ADSCD). NO outbound contact has been made pending this ethics consultation.

---

## The 20 Questions (Group A: Outside-Employment Activities)

1. Is the act of building this software during off-duty time permissible under DoDD 5500.07-R, 5 CFR Part 2635, and JFTR § 5400-5499?

2. Does building this software in anticipation of post-separation commercialization constitute "outside employment" requiring command notification or approval, or is it strictly permitted personal-time activity?

3. May Captain Taylor publish open-source components of the system (e.g., the MCP server modules) on GitHub during the ADSC tail period without command approval?

4. May Captain Taylor write blog posts, conference submissions, or social-media content describing the system's architecture during the ADSC tail period?

5. May Captain Taylor accept payment for personal-time consulting on related topics (e.g., legal-tech retrieval systems for non-DoD clients) during the ADSC tail period?

## The 20 Questions (Group B: Acquihire-Specific Activities)

6. May Captain Taylor enter into preliminary conversations with potential private-sector acquirers during the ADSC tail period? Conversations vs. signed agreements — what's the line?

7. May Captain Taylor engage M&A counsel and tax counsel during the ADSC tail period to prepare for negotiation? Engagement letters require signature — is signing prior to separation permissible?

8. May Captain Taylor share due-diligence materials (the 7 ADRs, benchmark results, audit trail, Decisions Log) with prospective acquirers during the ADSC tail period?

9. If a term sheet is offered prior to 10 Aug 2026, may Captain Taylor (a) review it, (b) negotiate redlines, (c) sign it (with closing conditional on or after separation)?

10. Are there specific company-types or industries that are categorically off-limits for acquihire conversations (e.g., DoD prime contractors, defense-tech firms, federal-contractor-status companies)?

11. May Captain Taylor accept a $75,000 transaction-expense reimbursement from an acquirer to cover M&A counsel and tax advisor fees, paid at closing?

12. What disclosure obligations to the chain of command attach to (a) preliminary conversations, (b) engagement of M&A counsel, (c) signed term-sheet review, (d) closed deal?

13. If Captain Taylor's clearance posture is in question (DCSA SIR pending), does that change any of the above answers?

## The 20 Questions (Group C: Post-Separation Restrictions)

14. Under 18 USC § 207, what activities are restricted during the 1-year cooling-off period following 10 Aug 2026? Are these restrictions different for acquirers that do or do not hold DoD contracts?

15. May Captain Taylor accept a position at a company that does separate, ongoing business with the Air Force or DoD post-separation, provided the role itself does not involve DoD-facing matters?

16. Are there any "lifetime" restrictions under 18 USC § 207(a) that would apply to particular subject matters or particular former colleagues that Captain Taylor would need to identify and avoid?

17. May Captain Taylor open-source the system in full following 10 Aug 2026 without restriction, or do post-separation IP-disclosure rules apply?

18. If retained as a consultant by a DoD prime contractor post-separation, what are the rules for working on contracts where Captain Taylor had no prior involvement during active duty?

## The 20 Questions (Group D: Carry-Over from Active Duty)

19. Captain Taylor's role during active duty has been clinical (LCSW). The software has no operational connection to that role. Does the no-connection-to-duty status protect the system from any "developed in the course of employment" claims?

20. Are there records-retention obligations Captain Taylor must satisfy regarding the system's development during the ADSC tail (e.g., off-duty employment logs, time-on-task records)?

---

## What Adam Needs From the SJA

1. **A written ethics opinion** within 14 days of the meeting, addressed to Captain Taylor, citing the regulations consulted and giving go/no-go answers to each of the 20 questions above.

2. **A specific list of activities permitted without further consultation** (e.g., "may continue solo development; may engage civilian ethics counsel; may engage M&A counsel after notifying chain of command").

3. **A specific list of activities requiring further consultation or formal approval** (e.g., "any signed term sheet must be routed through SJA review prior to signature").

4. **An identified point-of-contact for follow-up questions** during the ADSC tail period.

---

## Pre-Meeting Checklist for Adam

- [ ] Confirm SJA name and meeting time (in person or virtual)
- [ ] Bring printed copy of this document + the System Description one-pager
- [ ] Bring printed copy of `docs/acquihire/03_IP_Chain_of_Title/02_Subscriptions/subscription_summary.md` (proves no employer/government funding)
- [ ] Bring printed copy of `docs/ENVIRONMENT.md` (proves personal hardware)
- [ ] Bring printed copy of `docs/DEPLOYMENT_MODEL.md` (proves local-only, no DoD network)
- [ ] Note current ADSCD (10 Aug 2026) and current rank/AFSC at top of all printed documents
- [ ] Have a notepad ready — take notes on every answer; the SJA will not write a comprehensive opinion from memory
- [ ] Have follow-up email template ready to send within 24 hr of the meeting confirming the opinion timeline

---

## Post-Meeting Action Items

1. Within 24 hr of meeting: send a confirmation email to the SJA summarizing the 20 questions and the SJA's verbal answers, requesting written confirmation.
2. Within 7 days: forward the SJA's written opinion to civilian ethics counsel for redundant review.
3. Within 14 days: file the SJA opinion in `docs/acquihire/01_JAG_Ethics/` for diligence-grade reference.
4. Update `Desktop/VoxCore_Open_Questions.md` Cat "Ethics & Legal" with: (a) opinion received yes/no, (b) date received, (c) summary of go/no-go items.
