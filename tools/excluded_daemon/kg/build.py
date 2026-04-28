"""Cold-build the Knowledge Graph from the extracted text cache.

Walks .cache/extracted/*/files/**/*.txt, chunks each file, sends chunks to
Ollama for NER, and populates .cache/excluded_kg.db with entities, mentions,
and co-occurrence relations.

Usage:
    python -m tools.excluded_daemon.kg.build
    python -m tools.excluded_daemon.kg.build --limit 10
    python -m tools.excluded_daemon.kg.build --folder Case_Reference
    python -m tools.excluded_daemon.kg.build --reset
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sqlite3
import sys
import threading
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.excluded_daemon import config

log = logging.getLogger("kg.build")

NER_PROMPT = """\
Extract all named entities from this legal/military case document text.
Return ONLY valid JSON — no commentary, no markdown fences.

{
  "persons": [{"name": "Full Name", "role": "title or role if stated", "org": "organization if stated"}],
  "organizations": [{"name": "Org Name", "type": "military/government/legal/medical/other"}],
  "dates": [{"date": "YYYY-MM-DD or partial", "event": "what happened"}],
  "case_numbers": ["number as written"],
  "regulations": [{"citation": "e.g. 10 USC 1034", "section": "specific section if given"}],
  "amounts": [{"value": "dollar amount or quantity", "context": "what it refers to"}]
}

If a field has no entries, use an empty array. Dates should be ISO when possible.
Extract EVERY person mentioned, even in passing. Include military ranks.

TEXT:
"""


def init_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    schema_sql = config.KG_SCHEMA.read_text(encoding="utf-8")
    conn.executescript(schema_sql)
    return conn


def reset_db(db_path: Path) -> None:
    if db_path.exists():
        db_path.unlink()
    log.info(f"deleted {db_path}")


def _canonicalize(kind: str, name: str) -> str:
    """Normalize a name for dedup. Lowercase, strip ranks/titles, collapse whitespace."""
    c = name.strip().lower()
    c = re.sub(r"\b(capt|captain|col|colonel|lt col|lieutenant colonel|maj|major|"
               r"sgt|sergeant|msgt|master sergeant|tsgt|technical sergeant|"
               r"sra|senior airman|a1c|amn|cmsgt|smsgt|"
               r"mr|mrs|ms|dr|gen|brig gen|vadm|radm)\b\.?\s*", "", c)
    c = re.sub(r"\s+", " ", c).strip()
    if kind == "regulation":
        c = re.sub(r"[§ ]+", " ", c).strip()
    return c


def _load_persons_roster() -> dict[str, dict]:
    """Load the hand-curated persons roster for canonical name seeding."""
    if not config.PERSONS_ROSTER.exists():
        return {}
    try:
        data = json.loads(config.PERSONS_ROSTER.read_text(encoding="utf-8"))
        roster = {}
        for p in data.get("persons", []):
            canon = _canonicalize("person", p["canonical"])
            roster[canon] = p
            for alias in p.get("aliases", []):
                roster[_canonicalize("person", alias)] = p
        return roster
    except Exception as e:
        log.warning(f"could not load persons roster: {e}")
        return {}


def _resolve_canonical_person(name: str, roster: dict[str, dict]) -> str:
    """If the name matches a roster entry, return the roster's canonical form."""
    canon = _canonicalize("person", name)
    entry = roster.get(canon)
    if entry:
        return _canonicalize("person", entry["canonical"])
    for key, entry in roster.items():
        if canon in key or key in canon:
            return _canonicalize("person", entry["canonical"])
    return canon


def _ollama_ner(text: str) -> dict | None:
    """Call Ollama for NER. Returns parsed JSON or None on failure."""
    payload = json.dumps({
        "model": config.NER_MODEL,
        "prompt": NER_PROMPT + text,
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1, "num_predict": 2048},
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{config.OLLAMA_URL}/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=config.NER_TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        raw = data.get("response", "")
        if not raw or not raw.strip():
            raw = data.get("thinking", "")
        if not raw or not raw.strip():
            log.debug("ollama NER: empty response and thinking")
            return None
        return json.loads(raw)
    except (urllib.error.URLError, json.JSONDecodeError, KeyError, TimeoutError) as e:
        log.debug(f"ollama NER failed: {e}")
        return None


def _load_anthropic_key() -> str:
    """Load ANTHROPIC_API_KEY from env or tools/ai_studio/.env."""
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key:
        return key
    env_path = config.REPO_ROOT / "tools" / "ai_studio" / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() == "ANTHROPIC_API_KEY":
                return v.strip().strip("\"'")
    return ""


_ANTHROPIC_KEY = ""
_sonnet_call_count = 0
_sonnet_lock = threading.Lock()


def _sonnet_ner(text: str) -> dict | None:
    """Call Claude Sonnet 4.6 for NER via the Anthropic API. Fast cloud inference."""
    global _ANTHROPIC_KEY, _sonnet_call_count
    if not _ANTHROPIC_KEY:
        _ANTHROPIC_KEY = _load_anthropic_key()
    if not _ANTHROPIC_KEY:
        return None

    payload = json.dumps({
        "model": "claude-sonnet-4-6",
        "max_tokens": 2048,
        "messages": [{"role": "user", "content": NER_PROMPT + text}],
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": _ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        raw = ""
        for block in data.get("content", []):
            if block.get("type") == "text":
                raw += block.get("text", "")
        if not raw.strip():
            return None
        clean = raw.strip()
        if clean.startswith("```"):
            clean = re.sub(r"^```\w*\n?", "", clean)
            clean = re.sub(r"\n?```$", "", clean)
        with _sonnet_lock:
            _sonnet_call_count += 1
        return json.loads(clean)
    except Exception as e:
        log.debug(f"sonnet NER failed: {e}")
        return None


_backend_counter = 0
_backend_lock = threading.Lock()


_sonnet_ratio = 4  # out of every N calls, N-1 go to Sonnet, 1 goes to Ollama


def set_sonnet_ratio(ratio: int) -> None:
    global _sonnet_ratio
    _sonnet_ratio = max(1, ratio)


def _ner_dispatch(text: str) -> dict | None:
    """Round-robin between Ollama and Sonnet. Sonnet-heavy by default (4:1)."""
    global _backend_counter
    with _backend_lock:
        idx = _backend_counter
        _backend_counter += 1

    use_ollama = (idx % _sonnet_ratio == 0)
    if use_ollama:
        result = _ollama_ner(text)
        if result is None:
            result = _sonnet_ner(text)
    else:
        result = _sonnet_ner(text)
        if result is None:
            result = _ollama_ner(text)
    return result


def _chunk_text(text: str, size: int = config.NER_CHUNK_SIZE,
                overlap: int = config.NER_CHUNK_OVERLAP) -> list[tuple[int, str]]:
    """Split text into overlapping chunks. Returns (start_char, chunk_text) pairs."""
    chunks = []
    pos = 0
    while pos < len(text):
        end = min(pos + size, len(text))
        chunks.append((pos, text[pos:end]))
        pos = end - overlap if end < len(text) else end
    return chunks


def _upsert_entity(conn: sqlite3.Connection, kind: str, name: str,
                   canonical: str, metadata: dict | None = None,
                   date_str: str | None = None) -> int:
    """Insert or update an entity. Returns the entity id."""
    row = conn.execute(
        "SELECT id, first_seen, last_seen FROM entities WHERE kind=? AND canonical=?",
        (kind, canonical),
    ).fetchone()

    if row:
        eid, first, last = row
        updates = {}
        if date_str and (not first or date_str < first):
            updates["first_seen"] = date_str
        if date_str and (not last or date_str > last):
            updates["last_seen"] = date_str
        if metadata:
            old_meta = json.loads(conn.execute("SELECT metadata FROM entities WHERE id=?", (eid,)).fetchone()[0] or "{}")
            old_meta.update(metadata)
            updates["metadata"] = json.dumps(old_meta)
        if updates:
            sets = ", ".join(f"{k}=?" for k in updates)
            conn.execute(f"UPDATE entities SET {sets} WHERE id=?",
                         [*updates.values(), eid])
        return eid
    else:
        cur = conn.execute(
            "INSERT INTO entities (kind, name, canonical, first_seen, last_seen, metadata) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (kind, name, canonical, date_str, date_str,
             json.dumps(metadata or {})),
        )
        return cur.lastrowid


def _insert_mention(conn: sqlite3.Connection, entity_id: int,
                    chunk_id: str, doc_path: str, context: str,
                    confidence: float = 0.8) -> None:
    conn.execute(
        "INSERT INTO mentions (entity_id, chunk_id, doc_path, context, confidence) "
        "VALUES (?, ?, ?, ?, ?)",
        (entity_id, chunk_id, doc_path, context[:500], confidence),
    )


def _insert_relation(conn: sqlite3.Connection, subj: int, pred: str,
                     obj: int, source_chunk: str,
                     confidence: float = 0.7) -> None:
    existing = conn.execute(
        "SELECT 1 FROM relations WHERE subject_id=? AND predicate=? AND object_id=? LIMIT 1",
        (subj, pred, obj),
    ).fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO relations (subject_id, predicate, object_id, source_chunk, confidence) "
            "VALUES (?, ?, ?, ?, ?)",
            (subj, pred, obj, source_chunk, confidence),
        )


def process_ner_result(conn: sqlite3.Connection, ner: dict, chunk_id: str,
                       doc_path: str, context: str,
                       roster: dict[str, dict]) -> list[int]:
    """Process a single NER result, upserting entities and mentions. Returns entity IDs."""
    entity_ids = []

    for p in ner.get("persons", []):
        if isinstance(p, str):
            p = {"name": p}
        if not isinstance(p, dict):
            continue
        name = (p.get("name") or "").strip()
        if not name or len(name) < 2:
            continue
        canonical = _resolve_canonical_person(name, roster)
        meta = {}
        if p.get("role"):
            meta["role"] = str(p["role"])
        if p.get("org"):
            meta["org"] = str(p["org"])
        eid = _upsert_entity(conn, "person", name, canonical, meta)
        _insert_mention(conn, eid, chunk_id, doc_path, context)
        entity_ids.append(eid)

    for o in ner.get("organizations", []):
        if isinstance(o, str):
            o = {"name": o}
        if not isinstance(o, dict):
            continue
        name = (o.get("name") or "").strip()
        if not name or len(name) < 2:
            continue
        canonical = _canonicalize("org", name)
        meta = {"type": str(o.get("type", ""))} if o.get("type") else {}
        eid = _upsert_entity(conn, "org", name, canonical, meta)
        _insert_mention(conn, eid, chunk_id, doc_path, context)
        entity_ids.append(eid)

    for d in ner.get("dates", []):
        if isinstance(d, str):
            d = {"date": d}
        if not isinstance(d, dict):
            continue
        date_str = (d.get("date") or "").strip()
        event = (d.get("event") or "").strip()
        if not date_str:
            continue
        canonical = _canonicalize("date", date_str)
        meta = {"event": event} if event else {}
        eid = _upsert_entity(conn, "date", date_str, canonical, meta, date_str=date_str)
        _insert_mention(conn, eid, chunk_id, doc_path, context)
        entity_ids.append(eid)

    for cn in ner.get("case_numbers", []):
        if isinstance(cn, dict):
            cn = cn.get("number", cn.get("case_number", ""))
        if not isinstance(cn, str) or not cn.strip():
            continue
        canonical = _canonicalize("case_number", cn)
        eid = _upsert_entity(conn, "case_number", cn.strip(), canonical)
        _insert_mention(conn, eid, chunk_id, doc_path, context)
        entity_ids.append(eid)

    for r in ner.get("regulations", []):
        if isinstance(r, str):
            r = {"citation": r}
        if not isinstance(r, dict):
            continue
        citation = (r.get("citation") or "").strip()
        if not citation:
            continue
        canonical = _canonicalize("regulation", citation)
        meta = {"section": str(r.get("section", ""))} if r.get("section") else {}
        eid = _upsert_entity(conn, "regulation", citation, canonical, meta)
        _insert_mention(conn, eid, chunk_id, doc_path, context)
        entity_ids.append(eid)

    for a in ner.get("amounts", []):
        if isinstance(a, str):
            a = {"value": a}
        if not isinstance(a, dict):
            continue
        val = (a.get("value") or "").strip()
        if not val or len(val) <= 1:
            continue
        canonical = _canonicalize("amount", val)
        meta = {"context": str(a.get("context", ""))} if a.get("context") else {}
        eid = _upsert_entity(conn, "amount", val, canonical, meta)
        _insert_mention(conn, eid, chunk_id, doc_path, context)
        entity_ids.append(eid)

    # Co-occurrence relations (skip self-references, limit to avoid combinatorial explosion)
    unique_ids = list(set(entity_ids))
    pairs_inserted = 0
    for i, a in enumerate(unique_ids):
        for b in unique_ids[i + 1:]:
            if a != b:
                _insert_relation(conn, a, "mentioned_with", b, chunk_id)
                pairs_inserted += 1
                if pairs_inserted >= 50:
                    break
        if pairs_inserted >= 50:
            break

    return entity_ids


def collect_extracted_files(folder_filter: str | None = None) -> list[tuple[Path, str]]:
    """Walk .cache/extracted/ and return (txt_path, rel_doc_path) pairs."""
    cache = config.REPO_ROOT / ".cache" / "extracted"
    if not cache.exists():
        return []
    results = []
    for bucket in sorted(cache.iterdir()):
        files_dir = bucket / "files"
        if not files_dir.exists():
            continue
        manifest_path = bucket / "manifest.json"
        source_root = ""
        if manifest_path.exists():
            try:
                m = json.loads(manifest_path.read_text(encoding="utf-8"))
                source_root = m.get("source", "")
            except Exception:
                pass
        for txt in sorted(files_dir.rglob("*.txt")):
            rel = str(txt.relative_to(files_dir)).replace("\\", "/")
            if rel.endswith(".txt"):
                rel = rel[:-4]
            if folder_filter and folder_filter.lower() not in rel.lower():
                continue
            doc_path = f"{source_root}/{rel}" if source_root else rel
            doc_path = doc_path.replace("\\", "/")
            results.append((txt, doc_path))
    return results


def build(limit: int | None = None, folder: str | None = None,
          reset: bool = False, parallel: int = 3) -> dict:
    """Main build entry point. Returns stats dict."""
    if reset:
        reset_db(config.KG_DB)

    conn = init_db(config.KG_DB)
    roster = _load_persons_roster()
    log.info(f"roster: {len(roster)} entries")

    files = collect_extracted_files(folder)
    if limit:
        files = files[:limit]
    log.info(f"files to process: {len(files)}")

    stats = {
        "files_total": len(files),
        "files_processed": 0,
        "chunks_sent": 0,
        "ner_failures": 0,
        "entities_created": 0,
        "mentions_created": 0,
    }

    t0 = time.time()
    entity_count_before = conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
    mention_count_before = conn.execute("SELECT COUNT(*) FROM mentions").fetchone()[0]

    already_seen = set()
    if not reset:
        try:
            rows = conn.execute("SELECT DISTINCT doc_path FROM mentions").fetchall()
            already_seen = {r[0] for r in rows}
            if already_seen:
                log.info(f"resuming: {len(already_seen)} doc_paths already in KG, will skip")
        except Exception:
            pass

    for i, (txt_path, doc_path) in enumerate(files):
        if doc_path in already_seen:
            stats["files_processed"] += 1
            continue

        try:
            text = txt_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            log.warning(f"read error {txt_path}: {e}")
            continue

        if len(text.strip()) < 50:
            continue

        chunks = _chunk_text(text)

        def _process_chunk(ci_start_text):
            ci, start, ct = ci_start_text
            chunk_id = f"{doc_path}::{ci}"
            ner = _ner_dispatch(ct)
            return chunk_id, ct[:200], ner

        with ThreadPoolExecutor(max_workers=parallel) as pool:
            futures = [pool.submit(_process_chunk, (ci, s, ct))
                       for ci, (s, ct) in enumerate(chunks)]
            for fut in as_completed(futures):
                chunk_id, ctx, ner = fut.result()
                stats["chunks_sent"] += 1
                if ner is None:
                    stats["ner_failures"] += 1
                    continue
                process_ner_result(conn, ner, chunk_id, doc_path, ctx, roster)

        stats["files_processed"] += 1
        conn.commit()

        if (i + 1) % 10 == 0 or (i + 1) == len(files):
            elapsed = time.time() - t0
            rate = stats["chunks_sent"] / elapsed if elapsed > 0 else 0
            log.info(f"[{i+1}/{len(files)}] chunks={stats['chunks_sent']} "
                     f"ner_fail={stats['ner_failures']} "
                     f"rate={rate:.1f} chunks/s elapsed={elapsed:.0f}s "
                     f"sonnet_calls={_sonnet_call_count}")

    conn.commit()

    stats["entities_created"] = conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0] - entity_count_before
    stats["mentions_created"] = conn.execute("SELECT COUNT(*) FROM mentions").fetchone()[0] - mention_count_before
    stats["entities_total"] = conn.execute("SELECT COUNT(*) FROM entities").fetchone()[0]
    stats["mentions_total"] = conn.execute("SELECT COUNT(*) FROM mentions").fetchone()[0]
    stats["relations_total"] = conn.execute("SELECT COUNT(*) FROM relations").fetchone()[0]
    stats["elapsed_sec"] = round(time.time() - t0, 1)

    conn.close()
    return stats


def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s: %(message)s")
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=None, help="max files to process")
    ap.add_argument("--folder", type=str, default=None, help="filter by folder name substring")
    ap.add_argument("--reset", action="store_true", help="delete existing KG before building")
    ap.add_argument("--parallel", type=int, default=6, help="concurrent NER workers (default 6)")
    ap.add_argument("--sonnet-ratio", type=int, default=4, help="Sonnet:Ollama ratio — N means 1 Ollama per N calls (default 4)")
    args = ap.parse_args()

    set_sonnet_ratio(args.sonnet_ratio)
    stats = build(limit=args.limit, folder=args.folder, reset=args.reset,
                  parallel=args.parallel)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
