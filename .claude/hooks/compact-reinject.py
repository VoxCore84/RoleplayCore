#!/usr/bin/env python3
"""SessionStart hook: re-inject context after compaction.

PROBLEM: Generic reminders ("don't forget X") are useless after compaction
because they don't tell Claude WHAT it was doing. The real loss is task state.

APPROACH: Two-tier context restoration:
1. STATIC reminders — critical rules Claude gets wrong without them
2. DYNAMIC state — read precompact-state.json (written by PreCompact hook)
   to restore ACTUAL work context: which files were being edited, what kind
   of work was happening, which agents were spawned.

The PreCompact hook saves this data BEFORE compaction destroys context.
This hook reads it back AFTER, giving Claude real continuity instead of
just generic rules.
"""
import json
import os
import sys

SNAPSHOT_FILE = os.path.expanduser("~/.claude/precompact-state.json")

STATIC_REMINDERS = """POST-COMPACTION CONTEXT REMINDER:
- DESCRIBE tables before writing SQL (Anti-Theater Protocol)
- Check doc/session_state.md before touching shared files (multi-tab locking)
- Use /wrap-up at end of session — NEVER skip
- 60+ skills in .claude/commands/ — proactively remind user of relevant ones
- 16+ custom agents in .claude/agents/ — use appropriate subagent_type
- 10+ rules files in .claude/rules/ — loaded on-demand when touching relevant code
- Re-read MEMORY.md routing table if unsure which topic files to consult
- Legal/case work: cite sources, use confidence tiers, Case_Reference is READ-ONLY"""


def load_dynamic_state() -> str:
    """Read the precompact snapshot and format as context."""
    try:
        with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
            snapshot = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return ""

    parts = []

    # Work signals — what was happening before compaction
    signals = snapshot.get("work_signals", [])
    if signals:
        parts.append("WORK IN PROGRESS before compaction:")
        for sig in signals:
            parts.append(f"  - {sig}")

    # Recent files — what Claude was touching
    recent = snapshot.get("recent_files", [])
    if recent:
        # Show last 10 files, basename only
        basenames = [os.path.basename(f) for f in recent[-10:]]
        parts.append(f"Recent files: {', '.join(basenames)}")

    # C++ files needing build
    cpp = snapshot.get("cpp_files_touched", [])
    if cpp:
        parts.append(f"C++ files edited (may need build): {', '.join(os.path.basename(f) for f in cpp[:5])}")

    # SQL files needing application
    sql = snapshot.get("sql_files_touched", [])
    if sql:
        parts.append(f"SQL files touched (may need /apply-sql): {', '.join(os.path.basename(f) for f in sql[:5])}")

    # Task state — the key addition for context continuity
    todo_items = snapshot.get("todo_items", [])
    if todo_items:
        parts.append("PENDING TASKS from todo.md:")
        for item in todo_items:
            parts.append(f"  - {item}")

    active_tab = snapshot.get("active_tab", "")
    if active_tab:
        parts.append(f"ACTIVE TAB ASSIGNMENT: {active_tab}")

    checkpoint = snapshot.get("checkpoint", "")
    if checkpoint:
        parts.append(f"SESSION CHECKPOINT available — read {checkpoint} to restore full state")

    return "\n".join(parts)


def main():
    output_parts = [STATIC_REMINDERS]

    dynamic = load_dynamic_state()
    if dynamic:
        output_parts.append("")
        output_parts.append(dynamic)

    # Print to stderr — Claude sees hook stderr as informational context
    print("\n".join(output_parts), file=sys.stderr)


if __name__ == "__main__":
    main()
