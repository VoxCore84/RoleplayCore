"""LLM worker — runs NER on extracted text and populates the Knowledge Graph.

Called AFTER extract/OCR completes. Reads the extracted .txt sidecar, sends
chunks to Ollama for entity extraction, and upserts into the KG.

Follows the same async pattern as extract_worker.py.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from .. import config

log = logging.getLogger(__name__)


def _find_extracted_txt(source_path: Path) -> Path | None:
    """Given a source file path, find its extracted .txt sidecar in .cache/extracted/."""
    cache = config.REPO_ROOT / ".cache" / "extracted"
    if not cache.exists():
        return None

    try:
        rel = source_path.relative_to(config.EXCLUDED_ROOT)
    except ValueError:
        return None

    rel_str = str(rel).replace("\\", "/")

    for bucket in cache.iterdir():
        manifest_path = bucket / "manifest.json"
        if not manifest_path.exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            continue

        source_root = manifest.get("source", "")
        try:
            file_rel = source_path.relative_to(Path(source_root))
        except (ValueError, TypeError):
            continue

        candidate = bucket / "files" / (str(file_rel).replace("\\", "/") + ".txt")
        if candidate.exists():
            return candidate

    return None


async def ner_process(path: Path) -> dict:
    """Run NER on a file's extracted text and populate the KG.

    Returns a status dict matching other worker patterns.
    """
    txt_path = _find_extracted_txt(path)
    if not txt_path:
        return {"ok": False, "error": f"no extracted txt found for {path}"}

    try:
        text = txt_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"ok": False, "error": f"read error: {e}"}

    if len(text.strip()) < 50:
        return {"ok": True, "skipped": True, "reason": "text too short"}

    try:
        from tools.excluded_daemon.kg.build import (
            init_db, _chunk_text, _ollama_ner, process_ner_result,
            _load_persons_roster,
        )
    except ImportError as e:
        return {"ok": False, "error": f"import error: {e}"}

    conn = init_db(config.KG_DB)
    roster = _load_persons_roster()

    try:
        rel = path.relative_to(config.EXCLUDED_ROOT)
    except ValueError:
        rel = path
    doc_path = str(rel).replace("\\", "/")

    chunks = _chunk_text(text)
    total_entities = 0
    ner_failures = 0

    for ci, (start, chunk_text) in enumerate(chunks):
        chunk_id = f"{doc_path}::{ci}"
        ner = _ollama_ner(chunk_text)
        if ner is None:
            ner_failures += 1
            continue
        eids = process_ner_result(conn, ner, chunk_id, doc_path,
                                  chunk_text[:200], roster)
        total_entities += len(eids)

    conn.commit()
    conn.close()

    return {
        "ok": True,
        "chunks": len(chunks),
        "entities_found": total_entities,
        "ner_failures": ner_failures,
        "doc_path": doc_path,
    }
