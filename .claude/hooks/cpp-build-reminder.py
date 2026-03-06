"""Hook: remind about building after C++ file edits."""
import json
import sys

try:
    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "")
    if path.endswith((".cpp", ".h")):
        print(f"[hook] C++ file modified: {path} — use /build-loop to iterate or build in VS")
except Exception:
    pass
