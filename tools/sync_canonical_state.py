#!/usr/bin/env python3
"""Sync Desktop trackers + key memory files into the repo at _canonical_state/.

Solves the "code is in GitHub but evidence/audit-trail isn't" gap.
Files stay in their working locations (Desktop, ~/.claude/.../memory/);
this script COPIES them into the repo so a clone has the full audit trail.

Run:
- Manually before any acquirer-relevant commit
- Automatically by /wrap-up Step 1 (added to skill)

NOT synced (intentionally):
- 60+ operational topic memory files (case-status.md, finances-overview.md, etc.) —
  high churn, not diligence-relevant; would pollute history
- AI_Studio/Reports/ measurement JSONs (78MB) — separate problem, needs git-LFS or
  separate repo
- .cache/ databases — rebuildable artifacts

Usage:
    python tools/sync_canonical_state.py             # dry-run (default)
    python tools/sync_canonical_state.py --apply     # actually copy
    python tools/sync_canonical_state.py --apply --quiet
"""
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_DIR = REPO_ROOT / "_canonical_state"
DESKTOP = Path(os.path.expanduser("~/Desktop"))
MEMORY_DIR = Path(os.path.expanduser("~/.claude/projects/C--Users-atayl-VoxCore/memory"))


# (source_path, repo_dest_relative_path) — explicit, no globs in main set
DESKTOP_FILES = [
    ("VoxCore_Verification_Master_Checklist.md", "desktop/"),
    ("VoxCore_Decisions_Log.md", "desktop/"),
    ("VoxCore_Benchmark_Results.md", "desktop/"),
    ("VoxCore_Open_Questions.md", "desktop/"),
]

DESKTOP_FOLDER_FILES = [
    # ("Do NOT Delete These/<filename>", "desktop/Do_NOT_Delete_These/")
    ("Do NOT Delete These/VoxCore_Adam_HumanActions_PrepPack.md", "desktop/Do_NOT_Delete_These/"),
    ("Do NOT Delete These/VoxCore_JAG_Meeting_Agenda_and_Questions.md", "desktop/Do_NOT_Delete_These/"),
    ("Do NOT Delete These/VoxCore_Economic_Impact_Analysis_v3.1.md", "desktop/Do_NOT_Delete_These/"),
    ("Do NOT Delete These/VoxCore_Verification_Summary_3page.md", "desktop/Do_NOT_Delete_These/"),
]

# Diligence-relevant memory files (curated, not the full 60+)
MEMORY_FILES = [
    "MEMORY.md",                              # the index
    "recent-work.md",                         # session activity log
    "automation-ledger.md",                   # pain→fix retros + compounding
    "resume-evidence.md",                     # STAR bullets per session
    "improvements.md",                        # older history (read-only)
    "feedback_calibration_overfit.md",        # methodology rule
    "feedback_mcp_restart_pain.md",           # operational rule
    "feedback_sme_master_files.md",           # operational rule
    "voxcore-acquihire-track.md",             # acquihire context
    "user-profile.md",                        # operator context
    "system-architecture-snapshot.md",        # high-level architecture pointer
    "ai-strategy.md",                         # decision rationale
    "claude-code-internals.md",               # platform context
    "topic-index.md",                         # navigation
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true",
                   help="Actually copy (default is dry-run)")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()

    CANONICAL_DIR.mkdir(parents=True, exist_ok=True)
    desktop_dest = CANONICAL_DIR / "desktop"
    memory_dest = CANONICAL_DIR / "memory"
    desktop_dest.mkdir(exist_ok=True)
    (desktop_dest / "Do_NOT_Delete_These").mkdir(exist_ok=True)
    memory_dest.mkdir(exist_ok=True)

    plan: list[tuple[Path, Path, int]] = []
    skipped: list[tuple[Path, str]] = []

    # Desktop top-level
    for src_name, dest_subdir in DESKTOP_FILES:
        src = DESKTOP / src_name
        dest = CANONICAL_DIR / dest_subdir / src_name
        if not src.exists():
            skipped.append((src, "source missing"))
            continue
        plan.append((src, dest, src.stat().st_size))

    # Desktop "Do NOT Delete These/"
    for src_name, dest_subdir in DESKTOP_FOLDER_FILES:
        src = DESKTOP / src_name
        # dest path: replace the source folder name (with spaces) with the repo-friendly version
        dest = CANONICAL_DIR / dest_subdir / src.name
        if not src.exists():
            skipped.append((src, "source missing"))
            continue
        plan.append((src, dest, src.stat().st_size))

    # Memory files (curated subset)
    for memname in MEMORY_FILES:
        src = MEMORY_DIR / memname
        dest = memory_dest / memname
        if not src.exists():
            skipped.append((src, "source missing"))
            continue
        plan.append((src, dest, src.stat().st_size))

    # Output plan
    total_bytes = sum(sz for _, _, sz in plan)
    if not args.quiet:
        print(f"=== Sync plan ({len(plan)} files, {total_bytes:,} bytes total) ===")
        for src, dest, sz in plan:
            print(f"  {sz:>8} bytes  {src} -> {dest.relative_to(REPO_ROOT)}")
        if skipped:
            print(f"\n=== Skipped ({len(skipped)}) ===")
            for src, reason in skipped:
                print(f"  {src} ({reason})")

    if not args.apply:
        print(f"\nDry-run only. Pass --apply to actually copy.")
        return

    # Actually copy
    copied = 0
    for src, dest, _sz in plan:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        copied += 1

    # Write a README in _canonical_state/ explaining what this is
    readme = CANONICAL_DIR / "README.md"
    readme.write_text(f"""# _canonical_state — Synced audit-trail snapshot

This directory is **NOT the working location** for these files. It is a periodic
sync from their primary locations into the repo so a `git clone` has the full
diligence audit trail.

## What's in here

- `desktop/` — copies of the 4 Desktop canonical trackers (`VoxCore_Verification_Master_Checklist.md`,
  `VoxCore_Decisions_Log.md`, `VoxCore_Benchmark_Results.md`, `VoxCore_Open_Questions.md`)
- `desktop/Do_NOT_Delete_These/` — copies of active prep docs (Economic Impact v3.1,
  Verification Summary 3-page, JAG Meeting Agenda, Adam HumanActions Prep)
- `memory/` — curated subset of `~/.claude/projects/C--Users-atayl-VoxCore/memory/` files
  diligence-relevant ones: MEMORY.md, recent-work.md, automation-ledger.md, resume-evidence.md,
  improvements.md (history), feedback_*.md (methodology/ops rules), voxcore-acquihire-track.md,
  user-profile.md, system-architecture-snapshot.md, ai-strategy.md, claude-code-internals.md,
  topic-index.md

## What's NOT in here

- The 60+ operational topic memory files (case-status.md, finances-overview.md, etc.) —
  high-churn operational state, not diligence-relevant
- `AI_Studio/Reports/` measurement JSONs (78MB+) — separate gap; needs git-LFS or
  separate diligence repo
- `.cache/` databases — rebuildable artifacts

## How it stays in sync

`tools/sync_canonical_state.py --apply` copies the source files into this directory.
`/wrap-up` Step 1 calls this script before staging changes, so each session-end commit
includes the latest snapshot.

To verify a snapshot is current: compare a file here against its source location.

## DO NOT edit files in this directory

Edits should happen in the source locations (Desktop or `~/.claude/.../memory/`).
This directory is overwritten on every sync. Edits made here will be lost.

Generated by `tools/sync_canonical_state.py`.
""", encoding="utf-8")
    copied += 1

    if not args.quiet:
        print(f"\nCopied {copied} files (incl. README) to {CANONICAL_DIR}")
        print(f"Next: `git add _canonical_state/` and commit.")


if __name__ == "__main__":
    main()
