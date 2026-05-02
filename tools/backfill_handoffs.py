#!/usr/bin/env python3
"""Backfill reconstructed session handoffs from memory files.

Deterministic template fill — NO LLM synthesis. Reads:
  - ~/.claude/projects/.../memory/recent-work.md (per-session activity)
  - ~/.claude/projects/.../memory/automation-ledger.md (retro entries)
  - ~/.claude/projects/.../memory/resume-evidence.md (STAR bullets)
  - ~/.claude/projects/.../memory/improvements.md (older history)
  - git log --grep="session N" (commit hashes)

Writes to AI_Studio/Handoffs/voxcore/<date>_session_<N>_RECONSTRUCTED.md
with explicit [RECONSTRUCTED] frontmatter + source-pointer footer so
readers know they're looking at a back-fill, not a contemporaneous handoff.

Usage:
    python tools/backfill_handoffs.py --last 15        # backfill 15 most recent sessions
    python tools/backfill_handoffs.py --sessions 273 274 275 277
    python tools/backfill_handoffs.py --skip-existing  # don't overwrite real handoffs
    python tools/backfill_handoffs.py --dry-run        # show what would be written
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MEMORY_DIR = Path(os.path.expanduser("~/.claude/projects/C--Users-atayl-VoxCore/memory"))
HANDOFFS_DIR = REPO_ROOT / "AI_Studio" / "Handoffs" / "voxcore"

# Match recent-work.md headers: "## May 2 2026 (session 277b — title)"
_RW_HEADER_RE = re.compile(
    r"^## (?P<date_str>[A-Z][a-z]+ \d+(?:-\d+)? \d{4}) \(session (?P<num>[\w]+)\s*[—\-]\s*(?P<title>.+?)\)\s*$",
    re.MULTILINE,
)
# Match ledger headers: "### Session 277b — 2026-05-02 — title"
_LEDGER_HEADER_RE = re.compile(
    r"^### Session (?P<num>[\w]+)\s*[—\-]\s*(?P<date_iso>\d{4}-\d{2}-\d{2})\s*[—\-]\s*(?P<title>.+?)$",
    re.MULTILINE,
)


def parse_blocks(text: str, header_re: re.Pattern, kind: str) -> dict[str, dict]:
    """Return {session_num: {header_match_dict, body}}."""
    out: dict[str, dict] = {}
    matches = list(header_re.finditer(text))
    for i, m in enumerate(matches):
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        # body line numbers for source-pointer footer
        line_start = text[: m.start()].count("\n") + 1
        line_end = text[: body_end].count("\n") + 1
        out[m.group("num")] = {
            "kind": kind,
            "header": m.group(0).strip(),
            "body": body,
            "line_start": line_start,
            "line_end": line_end,
            "title": m.group("title").strip(),
            **({"date_str": m.group("date_str")} if "date_str" in m.groupdict() and m.group("date_str") else {}),
            **({"date_iso": m.group("date_iso")} if "date_iso" in m.groupdict() and m.group("date_iso") else {}),
        }
    return out


def normalize_date(date_str: str | None, date_iso: str | None) -> str:
    """Return YYYY-MM-DD. Prefer ISO from ledger; fall back to parsing recent-work format."""
    if date_iso:
        return date_iso
    if not date_str:
        return "UNKNOWN"
    # "May 2 2026" or "Apr 12-14 2026" — take the first day if range
    m = re.match(r"([A-Z][a-z]+) (\d+)(?:-\d+)? (\d{4})", date_str)
    if not m:
        return "UNKNOWN"
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05",
              "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10",
              "Nov": "11", "Dec": "12"}
    return f"{m.group(3)}-{months.get(m.group(1), '00')}-{int(m.group(2)):02d}"


def get_commit_for_session(session_num: str) -> str | None:
    """Find commit by `git log --grep=session\\ N`. Returns hash or None."""
    try:
        result = subprocess.run(
            ["git", "log", "--all", "--oneline", "--grep", f"session {session_num}\\b"],
            cwd=str(REPO_ROOT), capture_output=True, text=True, timeout=15,
            encoding="utf-8", errors="replace",
        )
        # Take the first match — typically the commit FROM that session
        for line in result.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            return line.split(maxsplit=1)[0]
    except (subprocess.TimeoutExpired, OSError):
        pass
    return None


HANDOFF_TEMPLATE = """# VoxCore Session Handoff — {date_str} (Session {session_num}) — RECONSTRUCTED

> **[RECONSTRUCTED on {today_iso}]** — This handoff was NOT written contemporaneously at the end of session {session_num}.
> It is a deterministic template fill from the memory files listed in the Sources footer.
> A reader citing facts from this document should cross-verify against the primary sources.
> This is a back-fill so the `AI_Studio/Handoffs/voxcore/` folder has a complete audit trail; it is not a substitute for a real handoff.

**Session:** {session_num}
**Date:** {date_str}
**Title:** {title}
**Commit (best-guess from `git log --grep`):** {commit_hash}
**Source provenance:** see footer

---

## What Happened (from recent-work.md)

{recent_work_body}

{automation_section}{resume_section}

---

## Sources

This reconstructed handoff was generated by `tools/backfill_handoffs.py` on {today_iso} from:

{sources_block}

To verify any specific claim, open the cited file at the cited line range and read the primary entry.

---

*Reconstructed handoff — DO NOT cite externally without verification against the primary memory files. For going-forward sessions, `/wrap-up` Step 6.5 writes contemporaneous handoffs to this folder automatically.*
"""

AUTOMATION_TEMPLATE = """
---

## Automation Ledger Entry (from automation-ledger.md)

{ledger_body}
"""

RESUME_TEMPLATE = """
---

## Resume Evidence (from resume-evidence.md)

{resume_body}
"""


def render_handoff(session_num: str, recent_work_entry: dict,
                    ledger_entry: dict | None, resume_entry: dict | None,
                    commit_hash: str | None, today_iso: str) -> tuple[str, str]:
    """Returns (filename, rendered_markdown)."""
    date_iso = normalize_date(
        recent_work_entry.get("date_str"),
        ledger_entry["date_iso"] if ledger_entry else (resume_entry["date_iso"] if resume_entry else None),
    )
    date_str = recent_work_entry.get("date_str", date_iso)
    title = recent_work_entry["title"]

    # Sanitize filename tag — first 3 words of title, lowercased, alphanum + hyphen only
    title_words = re.sub(r"[^\w\s-]", "", title.lower()).split()[:3]
    tag = "-".join(title_words) or "untitled"
    filename = f"{date_iso}_session_{session_num}_RECONSTRUCTED_{tag}.md"

    sources = []
    sources.append(f"- `memory/recent-work.md` lines {recent_work_entry['line_start']}-{recent_work_entry['line_end']} — primary activity log")
    if ledger_entry:
        sources.append(f"- `memory/automation-ledger.md` lines {ledger_entry['line_start']}-{ledger_entry['line_end']} — pain→fix entries + compounding score")
    if resume_entry:
        sources.append(f"- `memory/resume-evidence.md` lines {resume_entry['line_start']}-{resume_entry['line_end']} — STAR bullet + measurables")
    if commit_hash:
        sources.append(f"- git commit `{commit_hash}` — found via `git log --all --grep \"session {session_num}\"`")
    else:
        sources.append(f"- git commit: NOT FOUND via `git log --all --grep \"session {session_num}\"` — session may not have produced a single named commit")
    sources_block = "\n".join(sources)

    automation_section = (
        AUTOMATION_TEMPLATE.format(ledger_body=ledger_entry["body"]) if ledger_entry else ""
    )
    resume_section = (
        RESUME_TEMPLATE.format(resume_body=resume_entry["body"]) if resume_entry else ""
    )

    rendered = HANDOFF_TEMPLATE.format(
        date_str=date_str,
        session_num=session_num,
        today_iso=today_iso,
        title=title,
        commit_hash=commit_hash or "NOT FOUND",
        recent_work_body=recent_work_entry["body"],
        automation_section=automation_section,
        resume_section=resume_section,
        sources_block=sources_block,
    )
    return filename, rendered


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group()
    g.add_argument("--last", type=int, help="Backfill the N most recent sessions in recent-work.md")
    g.add_argument("--sessions", nargs="+", help="Specific session numbers to backfill")
    p.add_argument("--skip-existing", action="store_true",
                   help="Don't overwrite handoffs that already exist (matches by session number prefix)")
    p.add_argument("--dry-run", action="store_true", help="Show what would be written, no writes")
    p.add_argument("--out-dir", default=str(HANDOFFS_DIR))
    args = p.parse_args()

    today_iso = date.today().isoformat()

    print(f"Reading memory files from {MEMORY_DIR}")
    recent_work_text = (MEMORY_DIR / "recent-work.md").read_text(encoding="utf-8")
    ledger_text = (MEMORY_DIR / "automation-ledger.md").read_text(encoding="utf-8")
    resume_text = (MEMORY_DIR / "resume-evidence.md").read_text(encoding="utf-8")

    rw_blocks = parse_blocks(recent_work_text, _RW_HEADER_RE, "recent-work")
    ledger_blocks = parse_blocks(ledger_text, _LEDGER_HEADER_RE, "ledger")
    resume_blocks = parse_blocks(resume_text, _LEDGER_HEADER_RE, "resume")

    print(f"  recent-work.md: {len(rw_blocks)} sessions")
    print(f"  automation-ledger.md: {len(ledger_blocks)} sessions")
    print(f"  resume-evidence.md: {len(resume_blocks)} sessions")

    # Decide which sessions to process
    if args.sessions:
        target_sessions = args.sessions
    elif args.last:
        # Take the first N sessions from recent-work (top is most-recent)
        target_sessions = list(rw_blocks.keys())[: args.last]
    else:
        target_sessions = list(rw_blocks.keys())

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    existing = {p.name for p in out_dir.iterdir() if p.is_file() and p.suffix == ".md"}

    written = 0
    skipped = 0
    for snum in target_sessions:
        if snum not in rw_blocks:
            print(f"  [skip] session {snum}: not in recent-work.md")
            continue
        if args.skip_existing and any(f"_session_{snum}_" in fn for fn in existing):
            print(f"  [skip] session {snum}: existing handoff matches")
            skipped += 1
            continue
        commit = get_commit_for_session(snum)
        filename, rendered = render_handoff(
            snum,
            rw_blocks[snum],
            ledger_blocks.get(snum),
            resume_blocks.get(snum),
            commit,
            today_iso,
        )
        out_path = out_dir / filename
        if args.dry_run:
            print(f"  [dry-run] would write {filename} ({len(rendered)} chars)")
        else:
            out_path.write_text(rendered, encoding="utf-8")
            print(f"  [ok] wrote {filename} ({len(rendered)} chars; commit={commit or 'NOT FOUND'})")
            written += 1

    print(f"\nDone. Written: {written}, Skipped: {skipped}, Targeted: {len(target_sessions)}")


if __name__ == "__main__":
    main()
