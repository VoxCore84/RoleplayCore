"""PreToolUse hook: block Write of unreasonably large content.

Evidence for this hook:
    3 documented sessions stalled 60-70 minutes attempting single-shot Writes
    of large documents (vocab reference, architecture doc x2). 7+ sessions hit
    output-token-limit errors. Single-shot Writes over ~1500 lines reliably fail.

Fires on PreToolUse for the Write tool. Blocks when the proposed content exceeds
BLOCK_THRESHOLD_LINES unless a bypass signal is present:
  - Environment variable CLAUDE_WRITE_SIZE_BYPASS=1 (session-level override)
  - A bypass marker in the content's first 20 lines: "# BYPASS_WRITE_SIZE"
    or "<!-- BYPASS_WRITE_SIZE -->"
  - The target file path matches an exemption pattern (see KNOWN_LARGE_PATHS)

When blocked, returns JSON instructing Claude Code to deny the tool call and
shows a clear error pointing to /write-large-doc.

This is a soft rail, not a wall: explicit bypass is always available. The
goal is to catch accidents, not hostile action.
"""

from __future__ import annotations

import json
import os
import re
import sys


# Block when proposed Write content is this many lines or more. 1500 is set
# well below the ~2000-line empirical stall threshold so there's safety margin.
BLOCK_THRESHOLD_LINES = 1500

# File-path patterns exempted from the check. These are expected to be large
# and aren't the monolithic-stall failure mode.
KNOWN_LARGE_PATHS = (
    # Generated / assembled files
    r"parts/[0-9]+-.*\.md$",          # /write-large-doc output
    r"\.cache/",                       # cache artifacts
    # Upstream / imported
    r"dep/",                           # vendored dependencies
    r"wago/",                          # DB2 CSV imports
    # Config baselines
    r"worldserver\.conf\.dist$",
    r"bnetserver\.conf\.dist$",
    # Digest artifacts
    r"AI_Studio/Reports/SME/digests/", # Gemini digest outputs
    # Generated SQL
    r"sql/updates/.*\.sql$",
)

BYPASS_MARKER_RE = re.compile(
    r"(?:# |<!-- )BYPASS_WRITE_SIZE(?: -->|\b)",
    re.IGNORECASE,
)


def _should_exempt(file_path: str) -> bool:
    for pattern in KNOWN_LARGE_PATHS:
        if re.search(pattern, file_path):
            return True
    return False


def _has_bypass_marker(content: str) -> bool:
    # Check only the first ~20 lines so a hostile embedded marker mid-content
    # can't accidentally bypass. Author intent is expressed at the top.
    head = "\n".join(content.splitlines()[:20])
    return bool(BYPASS_MARKER_RE.search(head))


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # If we can't parse, don't block — fail open.
        return 0

    if payload.get("tool_name") != "Write":
        return 0

    # Session-level bypass via env var
    if os.environ.get("CLAUDE_WRITE_SIZE_BYPASS") == "1":
        return 0

    tool_input = payload.get("tool_input", {}) or {}
    content = tool_input.get("content", "") or ""
    file_path = tool_input.get("file_path", "") or ""

    if not content:
        return 0

    if _should_exempt(file_path):
        return 0

    if _has_bypass_marker(content):
        return 0

    line_count = content.count("\n") + (0 if content.endswith("\n") else 1)
    if line_count < BLOCK_THRESHOLD_LINES:
        return 0

    # Over threshold, no bypass. Deny the call.
    message = (
        f"Write blocked: content is {line_count} lines (threshold: {BLOCK_THRESHOLD_LINES}).\n"
        f"\n"
        f"Monolithic Writes over ~1500 lines reliably stall in Claude Code. "
        f"This has cost 60-70 minutes each in 3 prior sessions (see ~/CLAUDE.md "
        f"'Writing Large Documents' rules).\n"
        f"\n"
        f"Options:\n"
        f"  1. Use /write-large-doc to produce this via outline -> parts/ -> assembly.\n"
        f"  2. Split manually: write each section to parts/NN-slug.md in a separate\n"
        f"     Write call, then concatenate via Bash.\n"
        f"  3. Add '# BYPASS_WRITE_SIZE' as the first or second line of the content\n"
        f"     if you genuinely need a single-shot write (rare).\n"
        f"  4. Set CLAUDE_WRITE_SIZE_BYPASS=1 in the environment for a session-wide\n"
        f"     opt-out (generated artifacts, one-time migrations).\n"
    )

    response = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": message,
        }
    }
    print(json.dumps(response))
    return 0


if __name__ == "__main__":
    sys.exit(main())
