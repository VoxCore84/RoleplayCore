#!/usr/bin/env python3
"""Auto-commit the Claude Code memory repo (LOCAL-ONLY, never pushes).

Two callers, one script (DRY):
  - Windows Task Scheduler (daily safety net): no --message, auto-generates one.
    Catches mid-session memory edits that never reach a /wrap-up.
  - /wrap-up Step 6.6: passes --message "session N wrap-up", so the bulk of
    memory changes land in one commit with a meaningful message.

Commits any dirty state in the memory repo. No-op (exit 0) if clean.
NEVER pushes -- the memory repo is local-only (HIPAA/legal/financial content)
and carries a .git/hooks/pre-push backstop regardless.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from runner import MEMORY_DIR, git, git_status_short, now_iso  # noqa: E402


def build_message(dirty: list[str]) -> str:
    """Auto-message for unattended runs: timestamp + changed-file preview."""
    names = [line[3:].strip() for line in dirty]
    preview = ", ".join(names[:5])
    suffix = f" (+{len(names) - 5} more)" if len(names) > 5 else ""
    plural = "s" if len(names) != 1 else ""
    return f"auto-snapshot {now_iso()} ({len(names)} file{plural}: {preview}{suffix})"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--message", "-m", default="",
                    help="commit message (wrap-up passes a meaningful one; "
                         "omit for an auto-generated snapshot message)")
    args = ap.parse_args()

    if not (MEMORY_DIR / ".git").exists():
        print(f"[memory_commit] no git repo at {MEMORY_DIR} -- skipping")
        return 0

    dirty = git_status_short(cwd=MEMORY_DIR)
    if not dirty:
        print(f"[memory_commit] clean -- nothing to commit ({now_iso()})")
        return 0

    msg = args.message.strip() or build_message(dirty)
    git("add", "-A", cwd=MEMORY_DIR)
    git("commit", "-m", msg, cwd=MEMORY_DIR)

    # Verify: tree should now be clean, and HEAD should be the new commit.
    still_dirty = git_status_short(cwd=MEMORY_DIR)
    head = git("log", "--oneline", "-1", cwd=MEMORY_DIR)
    if still_dirty:
        print(f"[memory_commit] WARNING: {len(still_dirty)} file(s) still dirty "
              f"after commit -- check the repo")
        return 1
    print(f"[memory_commit] committed {len(dirty)} file(s) -> {head}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
