"""Index worker — updates the FTS5 sidecar incrementally + emits priority-folder notifications.

After Worker A/B deposit text into .cache/extracted or .cache/ocr, this worker
runs excluded_fts_build.py (incremental) so FTS5 stays current.

When a processed file lived in a HIGH_PRIORITY_FOLDERS entry, also append
a briefing line to AI_Studio/Reports/scheduled/new_items_<date>.md so the
next session-start surfaces it.

ChromaDB re-embedding is more expensive; it's triggered in larger batches
rather than per-file (see jobs/freshness.py).
"""
from __future__ import annotations

import asyncio
import logging
import sys
import time
from pathlib import Path

from .. import config
from ..router import in_high_priority_folder

log = logging.getLogger(__name__)

NEW_ITEMS_DIR = config.REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"


def _extract_first_heading(cache_txt_path: Path) -> str:
    """Best-effort: the first H1/H2 header or the first non-empty line, truncated."""
    try:
        with cache_txt_path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                if stripped.startswith("# "):
                    return stripped[2:].strip()[:120]
                if stripped.startswith("## "):
                    return stripped[3:].strip()[:120]
                # First non-header non-empty line
                return stripped[:120]
    except Exception:
        pass
    return ""


def emit_priority_notification(source_path: Path) -> None:
    """If source_path is in HIGH_PRIORITY_FOLDERS, append one line to today's new_items file."""
    if not in_high_priority_folder(source_path, config.EXCLUDED_ROOT):
        return
    try:
        rel = source_path.relative_to(config.EXCLUDED_ROOT)
    except ValueError:
        return
    # Derive the cache .txt sidecar path so we can pull a heading for the notice
    heading = ""
    try:
        rel_parts = list(rel.parts)
        # cache bucket is hashed by the top-level folder; scan for a .txt sidecar matching the filename
        for bucket in (config.REPO_ROOT / ".cache" / "extracted").iterdir() if (config.REPO_ROOT / ".cache" / "extracted").exists() else []:
            candidate = bucket / "files" / ("/".join(rel_parts[1:] if len(rel_parts) >= 2 else rel_parts) + ".txt")
            if candidate.exists():
                heading = _extract_first_heading(candidate)
                break
    except Exception:
        pass

    NEW_ITEMS_DIR.mkdir(parents=True, exist_ok=True)
    dated = NEW_ITEMS_DIR / f"new_items_{time.strftime('%Y%m%d')}.md"
    try:
        need_header = not dated.exists()
        with dated.open("a", encoding="utf-8") as f:
            if need_header:
                f.write(f"# New priority-folder items — {time.strftime('%Y-%m-%d')}\n\n")
                f.write("| Time | Folder | File | Heading |\n")
                f.write("|------|--------|------|---------|\n")
            top_folder = "/".join(rel.parts[:2]) if len(rel.parts) >= 2 else rel.parts[0] if rel.parts else "?"
            fname = rel.parts[-1]
            f.write(f"| {time.strftime('%H:%M')} | {top_folder} | `{rel}` | {heading or '-'} |\n")
    except Exception as e:
        log.warning(f"priority notification failed for {source_path}: {e}")


async def rebuild_fts() -> dict:
    cmd = [sys.executable, str(config.FTS_BUILD_PY)]
    log.info("fts5 incremental rebuild")
    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=120)
        return {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout_tail": stdout.decode("utf-8", errors="replace")[-500:],
            "stderr_tail": stderr.decode("utf-8", errors="replace")[-500:],
        }
    except asyncio.TimeoutError:
        return {"ok": False, "error": "fts rebuild timed out"}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}


async def on_indexed(source_path: Path) -> None:
    """Hook called by the main worker loop after a file is successfully processed.

    Emits a priority-folder notification if applicable. Non-blocking — any error
    is logged and swallowed.
    """
    try:
        emit_priority_notification(source_path)
    except Exception as e:
        log.warning(f"on_indexed hook error: {e}")
