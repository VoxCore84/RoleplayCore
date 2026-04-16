---
allowed-tools: WebSearch, WebFetch, Read, Write, Grep, Glob, Bash(ls:*), Bash(cat:*)
description: Full job application workflow — fetch posting + tailor resume + draft cover letter
argument-hint: <USAJobs announcement number, URL, or pasted job description>
---

# Apply Job

End-to-end job application workflow: fetch the posting, extract structured fields, tailor the resume, and draft a cover letter. Chains `/usajobs-fetch` and `/tailor-resume`.

## Arguments

`$ARGUMENTS` — one of:
- A USAJobs announcement number (e.g., `858700600`)
- A USAJobs URL
- A non-USAJobs job posting URL
- Pasted job description text

## Pipeline

### Phase 1: Fetch and Extract

**If USAJobs** (argument is a number, or URL contains `usajobs.gov`):
Follow the instructions in `.claude/commands/usajobs-fetch.md` to:
1. Search for the announcement via WebSearch
2. Extract structured fields: grade, salary, closing date, duties, specialized experience, selective factors, clearance requirement
3. Write the extracted data to `AI_Studio/Reports/job_<announcement>_extracted.md`

**If other job posting URL**:
1. Use WebFetch to retrieve the posting
2. Extract: title, company, location, salary, responsibilities, required qualifications, preferred qualifications
3. Write to `AI_Studio/Reports/job_<company>_<title>_extracted.md`

**If pasted text**:
1. Parse directly — extract the same structured fields
2. Write to `AI_Studio/Reports/job_pasted_<date>_extracted.md`

### Phase 2: Tailor Resume

Follow the instructions in `.claude/commands/tailor-resume.md` using the extracted fields:
1. Read the master resume and career evidence file
2. Pick the right lane (technical, leadership, clinical, hybrid)
3. Map qualifications to Adam's experience
4. Flag any security-sensitive content
5. Generate the tailored resume variant
6. Draft a cover letter

### Phase 3: Report

Output a summary:
```
## Job Application Package

### Posting
- **Title**: [role]
- **Org**: [company/agency]
- **Grade/Salary**: [GS-XX / $XXk-$XXk]
- **Closes**: [date] ([N days])

### Resume
- **Lane**: [technical/leadership/clinical/hybrid]
- **File**: [path to tailored resume]
- **Fit Score**: [strong/moderate/stretch]

### Cover Letter
- **File**: [path]

### Flags
- [any security-sensitive content warnings]
- [any qualification gaps]
```

## After This

- Review and edit the tailored resume at the reported path
- Submit via USAJobs or the employer's portal (manual step)
