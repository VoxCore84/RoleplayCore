"""Append-only episodic log of corpus interactions.

Called by /ex-ask, /case-search, /evidence-xref at end of their output to leave
a breadcrumb: date | command | question | key files cited | confidence.

Legal audit-trail value: an attorney reviewer can see "when did you first surface
the ET obstruction email?" with one grep.

Storage: memory/excluded-session-log.md, append-only. Rotates to
.cache/excluded_session_log_archive/<timestamp>.md when it exceeds 500 lines.

Also writes JSON Lines for machine queries: memory/excluded-session-log.jsonl.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

MEMORY_DIR = Path.home() / ".claude/projects/C--Users-atayl-VoxCore/memory"
LOG_MD = MEMORY_DIR / "excluded-session-log.md"
LOG_JSONL = MEMORY_DIR / "excluded-session-log.jsonl"
ARCHIVE_DIR = Path(os.environ.get("VOXCORE_ROOT", "C:/Users/atayl/VoxCore")) / ".cache" / "excluded_session_log_archive"

MAX_LINES_BEFORE_ROTATE = 500


def _ensure_header() -> None:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_MD.exists():
        LOG_MD.write_text(
            "# Excluded/ Session Log — Append-only\n\n"
            "_One line per significant corpus interaction. Rotates at 500 lines._\n\n"
            "| Timestamp | Command | Summary | Files cited | Confidence |\n"
            "|-----------|---------|---------|-------------|------------|\n",
            encoding="utf-8",
        )


def _maybe_rotate() -> None:
    if not LOG_MD.exists():
        return
    try:
        lines = LOG_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return
    if len(lines) < MAX_LINES_BEFORE_ROTATE:
        return
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    archived = ARCHIVE_DIR / f"excluded-session-log-{stamp}.md"
    archived.write_text("\n".join(lines), encoding="utf-8")
    # Truncate original, keep header
    _ensure_header()


def append(command: str, summary: str, files_cited: list[str] | None = None,
           confidence: str = "", question: str = "") -> None:
    _ensure_header()
    _maybe_rotate()

    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    files_str = ", ".join(f"`{f}`" for f in (files_cited or [])[:5])
    summary_clean = summary.replace("|", "/").replace("\n", " ")[:200]
    row = f"| {ts} | {command} | {summary_clean} | {files_str} | {confidence} |\n"
    try:
        with LOG_MD.open("a", encoding="utf-8") as f:
            f.write(row)
    except Exception as e:
        print(f"WARN: session log append failed: {e}", file=sys.stderr)

    # JSONL for machine queries
    record = {
        "ts": int(time.time()),
        "date": ts,
        "command": command,
        "question": question,
        "summary": summary,
        "files_cited": files_cited or [],
        "confidence": confidence,
    }
    try:
        with LOG_JSONL.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, default=str) + "\n")
    except Exception as e:
        print(f"WARN: session log jsonl append failed: {e}", file=sys.stderr)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Append to Excluded session log")
    ap.add_argument("--command", required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--question", default="")
    ap.add_argument("--confidence", default="")
    ap.add_argument("--files", nargs="*", default=[])
    args = ap.parse_args()
    append(args.command, args.summary, args.files, args.confidence, args.question)
    print(f"Logged to {LOG_MD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
