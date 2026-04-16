---
allowed-tools: WebSearch, WebFetch, Write, Read
description: Retrieve a USAJobs announcement via WebSearch (WebFetch blocked) and extract structured fields — grade, salary, closing, duties, specialized experience, selective factors, clearance. Bypasses the ECONNRESET WebFetch failure class.
argument-hint: <announcement number or USAJobs URL>
---

# /usajobs-fetch — Structured USAJobs Announcement Retrieval

**Evidence for this skill:** In session 257, WebFetch to `usajobs.gov` returned ECONNRESET or timeout three separate times. The research agent had to fall back to WebSearch mid-task, and a second research agent timed out entirely with no deliverable. USAJobs actively blocks automated WebFetch, but WebSearch with specific announcement-number queries returns usable snippets. This skill codifies that workaround.

## Input

`$ARGUMENTS` — one of:
- A bare announcement number (e.g. `858700600`)
- A USAJobs URL (e.g. `https://www.usajobs.gov/job/858700600`)
- A USAJobs URL with query params (strip them)

## Next Step

After extracting the posting, tailor the resume:
- Run `/tailor-resume` with the extracted fields
- Or run `/apply-job <url>` to do both in one command

## Workflow

### Phase 1 — Normalize

Extract the 9-digit announcement number. If the input is a URL, grab the numeric segment after `/job/`.

### Phase 2 — Search

Do NOT attempt WebFetch directly (it will fail). Instead run WebSearch queries. Two queries in parallel:

1. `"<number>" USAJobs announcement duties responsibilities specialized experience`
2. `"<number>" USAJobs closing date salary GS grade selective factor`

The WebSearch results typically include a Claude-summarized snippet of the posting that contains most fields we need. If the snippets are thin, run a third query:

3. `"<number>" USAJobs "how you will be evaluated" OR "selective factor" OR "clearance"`

### Phase 3 — Extract

From the combined snippets, extract the following fields verbatim where possible:

| Field | Typical source |
|---|---|
| Title | First line of the announcement header |
| Agency / Sub-agency | "Department of X" or "Office of Y" |
| Announcement number | Already have it |
| Grade range | "GS-XX to GS-YY" or "GS-XX only" |
| Salary range | "$A to $B per year" — watch for locality variance |
| Closing date | "Open MM/DD/YYYY to MM/DD/YYYY" — pull the close |
| Location | Specific city, "Anywhere in the U.S.", or "negotiable" |
| Term type | Permanent / Term (N years) / Temporary |
| Direct Hire Authority (DHA) | Y/N — check for "Direct Hire" wording |
| Citizenship requirement | Usually "U.S. citizens" — note if stricter |
| Clearance level | Public Trust / SECRET / TS/SCI / Not required |
| Specialized Experience (per grade) | Full paragraph quoted verbatim |
| Selective Factors | Any "You must be able to..." knock-out statements |
| Duties | Bullet list of responsibilities |
| Unusual application requirements | Essays, writing samples, etc. (see Treasury #858700600 "Great Gatsby" precedent) |
| Veterans preference | Notes on 5/10-point preference or DHA waiver |

If a field isn't findable in the search snippets, mark it `<unknown — see posting>` and include the URL.

### Phase 4 — Write structured output

Save extracted data to `AI_Studio/Reports/career/postings/<number>.md` with this frontmatter:

```markdown
---
announcement: <number>
title: <title>
agency: <agency>
grade: <GS-XX to GS-YY>
salary: <$A to $B>
closing: <YYYY-MM-DD>
closes_in_days: <calculated from today>
dha: <true/false>
clearance: <level>
citizenship: <requirement>
location: <city or negotiable>
term: <permanent/term-N-years>
url: https://www.usajobs.gov/job/<number>
fetched: <timestamp>
---

# <Title> — Announcement #<number>

## Agency & Type
...

## Salary & Grade
...

## Location & Term
...

## Specialized Experience
### GS-XX
> <verbatim paragraph>

### GS-YY
> <verbatim paragraph>

## Selective Factors
> <verbatim quote>

## Duties
- <duty>
- <duty>

## Unusual Application Requirements
<or "None observed" if nothing stood out>

## Clearance & Citizenship
<details>

## Candidate Fit (optional — skip if running for research only)
<use the candidate's master resume and the resume-tailor agent's keyword pool to assess>

## Links
- Primary: https://www.usajobs.gov/job/<number>
- Related announcements (same agency, similar title, similar grade): <list if surfaced>
```

### Phase 5 — Report

Output a concise summary to the chat:

```
USAJobs #<number> — <title> (<agency>)
  Grade: GS-XX–YY | Salary: $A–$B | Closing: YYYY-MM-DD (<N> days)
  Clearance: <level> | DHA: <Y/N> | Location: <city>
  Selective factor: <one-line summary or "none">

Structured extract → AI_Studio/Reports/career/postings/<number>.md
```

## Rules

1. **Never attempt WebFetch to usajobs.gov.** Empirically ECONNRESET / timeout. Use WebSearch only.
2. **Quote specialized-experience language verbatim.** Federal applications require mirroring this language in the cover letter's equivalency block — paraphrasing loses the keyword match.
3. **Run the 3 WebSearch queries in parallel** (single message, multiple tool uses).
4. **Flag unknowns, don't guess.** If a field isn't findable in snippets, say so. The user can open the URL in a browser if they need the field urgently.
5. **Respect staleness.** USAJobs announcements can close early (e.g. FSA's 200-app cap) or be pulled. Always include `fetched: <timestamp>` so re-fetching later can detect drift.
6. **Batch mode.** If the user passes multiple announcement numbers, run parallel WebSearch for each and write one file per posting.

## When to run

- Before tailoring a resume for a specific federal posting (upstream of `/tailor-resume`)
- When reviewing a list of target postings to prioritize by deadline / fit
- When re-checking a posting close to its deadline (closing date may have moved up due to application cap)
- Batch-import when building a quarterly federal-opportunity watch list

## Related

- `/tailor-resume` — consumes the structured output from this skill as input
- `AI_Studio/Reports/career/gs14-15-keyword-analysis.md` — built on output from this same method, manually
- resume-tailor agent — has the 2026 federal + private keyword pool that pairs with this extraction
