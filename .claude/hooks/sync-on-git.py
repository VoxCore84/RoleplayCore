"""Hook: sync bridge after git commit/push operations."""
import json
import subprocess
import sys

try:
    data = json.load(sys.stdin)
    cmd = data.get("tool_input", {}).get("command", "")
    if any(kw in cmd for kw in ("git commit", "git push", "git merge")):
        subprocess.Popen(
            [sys.executable, "C:/Users/atayl/cowork/sync_bridge.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
except Exception:
    pass
