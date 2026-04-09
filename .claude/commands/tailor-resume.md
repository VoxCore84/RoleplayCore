---
allowed-tools: Read, Grep, Glob, Bash(ls:*), Bash(cat:*), WebFetch
description: Tailor a resume variant to a specific job posting — picks lane, flags security-sensitive content, drafts cover letter
argument-hint: <job posting URL or pasted text>
---

# Resume Tailoring

Tailor Capt Taylor's resume to a specific job posting. Takes a URL or pasted text as argument.

## Input

$ARGUMENTS — either a URL to fetch or a block of pasted job description text.

If URL: use WebFetch to get the posting (prompt: "Extract role title, responsibilities, required qualifications, preferred qualifications, company, location, and salary if listed").
If text: parse it directly.

## Instructions

### Step 1 — Read the resume package baseline
Read IN PARALLEL:
1. `C:/Users/atayl/.claude/projects/C--Users-atayl-VoxCore/memory/resume-package.md`
2. `C:/Users/atayl/.claude/projects/C--Users-atayl-VoxCore/memory/career-package.md`
3. `C:/Users/atayl/.claude/projects/C--Users-atayl-VoxCore/memory/user-profile.md`

### Step 2 — Pick the right variant
From resume-package.md, the 4 lanes are:

| Variant | Target | Key positioning |
|---|---|---|
| Clinical_LCSW | VA/community BH/private practice | 8 therapy modalities, suppresses tech |
| Federal_Contractor | GS-12+/cleared contractor | AFSOC ops + clearance + policy |
| Systems_Architect | Tech/defense-tech | VoxCore leads, military compressed |
| Wounded_Warrior | AFW2/OWF/peer support | Lived experience, explicitly names HWE filing |

Based on the posting, pick the LANE (one of: Clinical, Federal, Systems, Wounded Warrior). Justify in 1-2 sentences.

### Step 3 — Read the chosen variant source
Read `C:/Users/atayl/Desktop/IMPORTANT DOCS/Resume Stuff/Resume_<Variant>.md` in full.
Also read `Master_Resume.md` for additional content pool.

### Step 4 — Security hygiene checks (BLOCKING)

Check the chosen variant for:
- **Clearance status**: per memory, clearance is TERMINATED. Flag if variant leads with "Active TS/SCI" or similar — this must be softened or removed unless the posting specifically asks about cleared *experience* (past tense OK).
- **HWE filing reference**: only the Wounded_Warrior variant should mention Hostile Work Environment complaint. If you picked a different variant and the source contains HWE references, STRIP them.
- **LCSW portability**: LCSW is NC-only. If the posting is clinical in a non-NC state, add a portability note.
- **Retaliation language**: never include in Federal/Systems/Clinical variants.

Report security-hygiene findings BEFORE the tailored output.

### Step 5 — Tailor

Produce THREE outputs:

**A) Keyword match analysis** — which posting keywords already exist in the variant, which need to be added
**B) Tailored resume** (markdown) — the chosen variant with:
- Bullets reordered for relevance
- Keywords from posting woven in where truthful
- Non-relevant content compressed or removed
- Security hygiene corrections applied
**C) Cover letter draft** (3-4 paragraphs):
- Hook tied to the company/role
- 2-3 specific match points from the posting
- Call-to-action

### Step 6 — Flag gaps

Finally, list any **honest mismatches** — requirements in the posting that Capt Taylor does NOT meet. Never fabricate to cover gaps. The user needs to know whether to apply anyway or skip.

## Output structure

```
## Tailored Resume — [Role] @ [Company]

### Variant: [chosen lane]
**Why this lane:** [1-2 sentences]

### Security Hygiene
- Clearance: [OK / flagged and corrected]
- HWE: [OK / stripped]
- Other: [...]

### Keyword Match
- Already strong: [...]
- Added: [...]
- Missing (gap): [...]

### Tailored Resume
[markdown content]

### Cover Letter Draft
[markdown content]

### Honest Gaps
1. [requirement] — [do we meet it? if no, why]
2. ...
```

## Rules

- Never fabricate experience, certs, or dates
- Never include HWE or retaliation language in non-WW variants
- Never lead with "Active clearance" (it's terminated)
- CADC cert #2735 EXPIRED Feb 2024 — never list as current
- Apply for NC-state clinical only, or add portability caveat
