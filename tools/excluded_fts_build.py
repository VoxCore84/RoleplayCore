#!/usr/bin/env python3
"""Build a SQLite FTS5 index over the Excluded/ extracted text cache.

Sidecar to the ChromaDB semantic index — gives BM25/trigram keyword search
without requiring Ollama. Used by hybrid retrieval in the ExcludedDaemon.

Design:
  - SQLite at .cache/excluded_fts.db, WAL mode, mmap 4GB
  - chunks table: primary content (same granularity as ChromaDB chunks)
  - chunks_fts virtual table: contentless FTS5 with trigram tokenizer
  - Chunks keyed by same stable ID scheme as rag_build.py (sha1 of source:rel:idx)
  - Incremental: re-runs only add/update chunks whose source sha256 changed
  - Sources: auto-discovered from .cache/extracted/*, .cache/ocr/*, .cache/audio/*

Usage:
  python tools/excluded_fts_build.py                     # incremental build
  python tools/excluded_fts_build.py --drop              # nuke and rebuild
  python tools/excluded_fts_build.py --stats             # show counts
  python tools/excluded_fts_build.py --query "TERMS"     # ad hoc query test
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sqlite3
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = REPO_ROOT / ".cache" / "excluded_fts.db"
CHUNK_SIZE_CHARS = 2400  # ~600 tokens at 4 chars/token (matches rag_build.py)
CHUNK_OVERLAP_CHARS = 400  # ~100 tokens

SCHEMA = """
CREATE TABLE IF NOT EXISTS chunks (
    id           TEXT PRIMARY KEY,
    doc_type     TEXT NOT NULL,
    source_root  TEXT NOT NULL,
    rel_path     TEXT NOT NULL,
    chunk_idx    INTEGER NOT NULL,
    char_start   INTEGER NOT NULL,
    char_end     INTEGER NOT NULL,
    content      TEXT NOT NULL,
    source_sha   TEXT,
    indexed_at   INTEGER
);

CREATE INDEX IF NOT EXISTS idx_chunks_rel ON chunks(rel_path);
CREATE INDEX IF NOT EXISTS idx_chunks_type ON chunks(doc_type);
CREATE INDEX IF NOT EXISTS idx_chunks_source ON chunks(source_root, rel_path);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    rel_path, content,
    content='chunks',
    content_rowid='rowid',
    tokenize='trigram'
);

-- Triggers to keep FTS in sync (external content table)
CREATE TRIGGER IF NOT EXISTS chunks_ai AFTER INSERT ON chunks BEGIN
    INSERT INTO chunks_fts(rowid, rel_path, content) VALUES (new.rowid, new.rel_path, new.content);
END;

CREATE TRIGGER IF NOT EXISTS chunks_ad AFTER DELETE ON chunks BEGIN
    INSERT INTO chunks_fts(chunks_fts, rowid, rel_path, content) VALUES('delete', old.rowid, old.rel_path, old.content);
END;

CREATE TRIGGER IF NOT EXISTS chunks_au AFTER UPDATE ON chunks BEGIN
    INSERT INTO chunks_fts(chunks_fts, rowid, rel_path, content) VALUES('delete', old.rowid, old.rel_path, old.content);
    INSERT INTO chunks_fts(rowid, rel_path, content) VALUES (new.rowid, new.rel_path, new.content);
END;

CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
);
"""


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA mmap_size=4294967296")  # 4GB mmap
    conn.execute("PRAGMA cache_size=-262144")    # 256MB page cache
    conn.executescript(SCHEMA)
    return conn


# Import shared semantic chunker (header-aware for .md, paragraph-aware fallback for others)
try:
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from semantic_chunk import chunk_file as _semantic_chunk_file
    _SEMANTIC_AVAILABLE = True
except Exception as _e:
    _SEMANTIC_AVAILABLE = False


def chunk_text(text: str, size: int = CHUNK_SIZE_CHARS, overlap: int = CHUNK_OVERLAP_CHARS, rel_path: str = ""):
    """Yield (idx, char_start, char_end, chunk_text).

    Prefers semantic chunker for .md files (splits on ## headers). Falls back to
    sliding-window for PDF/DOCX/TXT/EML where natural boundaries are less reliable.
    """
    if _SEMANTIC_AVAILABLE and rel_path:
        for c in _semantic_chunk_file(rel_path, text, target=size, overlap=overlap):
            yield c["idx"], c["char_start"], c["char_end"], c["text"]
        return

    # Legacy fallback
    if not text or not text.strip():
        return
    text_len = len(text)
    start = 0
    idx = 0
    while start < text_len:
        end = min(start + size, text_len)
        if end < text_len:
            for delim in ("\n\n", ". ", "\n", " "):
                split = text.rfind(delim, start + size // 2, end + 50)
                if split != -1:
                    end = split + len(delim)
                    break
        chunk = text[start:end].strip()
        if chunk:
            yield idx, start, end, chunk
            idx += 1
        if end >= text_len:
            break
        start = max(start + 1, end - overlap)


def discover_sources():
    """Yield (doc_type, root_dir) for every cache bucket."""
    cache_root = REPO_ROOT / ".cache"
    for doc_type, sub in (("extracted", "extracted"), ("ocr", "ocr"), ("transcribed", "transcribed")):
        root = cache_root / sub
        if not root.exists():
            continue
        for bucket in root.iterdir():
            files = bucket / "files"
            if files.exists():
                yield doc_type, files


def iter_text_files(root: Path):
    """Yield (rel_path, text, source_sha) for every .txt under root."""
    for dirpath, _dirs, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".txt"):
                continue
            abs_path = Path(dirpath) / fn
            rel = str(abs_path.relative_to(root)).replace("\\", "/")
            try:
                text = abs_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"  WARN: {rel}: {e}", file=sys.stderr)
                continue
            source_sha = hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()[:16]
            yield rel, text, source_sha


def build(drop: bool = False) -> int:
    if drop and DB_PATH.exists():
        DB_PATH.unlink()
        for sidecar in (DB_PATH.with_suffix(DB_PATH.suffix + "-wal"), DB_PATH.with_suffix(DB_PATH.suffix + "-shm")):
            if sidecar.exists():
                sidecar.unlink()
        print(f"Dropped existing {DB_PATH}", file=sys.stderr)

    conn = connect(DB_PATH)
    cur = conn.cursor()

    # Pre-load existing IDs + source shas for skip decisions
    cur.execute("SELECT id, source_sha FROM chunks")
    existing = dict(cur.fetchall())

    sources = list(discover_sources())
    print(f"Discovered {len(sources)} source buckets", file=sys.stderr)

    new_count = 0
    updated_count = 0
    skipped_count = 0
    file_count = 0
    t0 = time.perf_counter()

    for doc_type, root in sources:
        for rel, text, sha in iter_text_files(root):
            file_count += 1
            if len(text.strip()) < 20:
                continue
            # Check if any chunk for this file has a different source_sha → re-chunk
            cur.execute(
                "SELECT DISTINCT source_sha FROM chunks WHERE source_root=? AND rel_path=?",
                (str(root), rel),
            )
            row = cur.fetchone()
            cached_sha = row[0] if row else None
            if cached_sha == sha:
                skipped_count += 1
                continue
            # If stale, delete old chunks for this file
            if cached_sha is not None:
                cur.execute(
                    "DELETE FROM chunks WHERE source_root=? AND rel_path=?",
                    (str(root), rel),
                )
                updated_count += 1
            else:
                new_count += 1
            # Insert new chunks (semantic chunker gets rel_path to dispatch .md-aware logic)
            now = int(time.time())
            for idx, cs, ce, chunk in chunk_text(text, rel_path=rel):
                chunk_id = hashlib.sha1(f"{root}:{rel}:{idx}".encode("utf-8")).hexdigest()
                cur.execute(
                    """INSERT OR REPLACE INTO chunks
                       (id, doc_type, source_root, rel_path, chunk_idx,
                        char_start, char_end, content, source_sha, indexed_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (chunk_id, doc_type, str(root), rel, idx, cs, ce, chunk, sha, now),
                )
        conn.commit()

    # Rebuild FTS index if drop was used (triggers handle incremental)
    if drop:
        cur.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
        conn.commit()

    cur.execute("SELECT COUNT(*) FROM chunks")
    total_chunks = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT rel_path) FROM chunks")
    total_files = cur.fetchone()[0]

    # Record meta
    cur.execute("INSERT OR REPLACE INTO meta(key, value) VALUES('last_build', ?)",
                (str(int(time.time())),))
    cur.execute("INSERT OR REPLACE INTO meta(key, value) VALUES('chunk_size', ?)",
                (str(CHUNK_SIZE_CHARS),))
    conn.commit()
    conn.close()

    elapsed = time.perf_counter() - t0
    print(f"\nFiles scanned: {file_count}", file=sys.stderr)
    print(f"New:           {new_count}", file=sys.stderr)
    print(f"Updated:       {updated_count}", file=sys.stderr)
    print(f"Unchanged:     {skipped_count}", file=sys.stderr)
    print(f"Total chunks:  {total_chunks}", file=sys.stderr)
    print(f"Total files:   {total_files}", file=sys.stderr)
    print(f"Elapsed:       {elapsed:.1f}s", file=sys.stderr)
    print(f"DB:            {DB_PATH}  ({DB_PATH.stat().st_size / 1_048_576:.1f} MB)", file=sys.stderr)
    return 0


def stats() -> int:
    if not DB_PATH.exists():
        print(f"DB does not exist: {DB_PATH}", file=sys.stderr)
        return 1
    conn = connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM chunks")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT rel_path) FROM chunks")
    files = cur.fetchone()[0]
    cur.execute("SELECT doc_type, COUNT(*) FROM chunks GROUP BY doc_type")
    by_type = cur.fetchall()
    cur.execute("SELECT value FROM meta WHERE key='last_build'")
    lb = cur.fetchone()
    print(f"DB:           {DB_PATH} ({DB_PATH.stat().st_size / 1_048_576:.1f} MB)")
    print(f"Total chunks: {total}")
    print(f"Total files:  {files}")
    print(f"Last build:   {lb[0] if lb else '?'}")
    print(f"By doc_type:")
    for dt, n in by_type:
        print(f"  {dt}: {n}")
    conn.close()
    return 0


def query(q: str, limit: int = 10) -> int:
    if not DB_PATH.exists():
        print(f"DB does not exist: {DB_PATH}", file=sys.stderr)
        return 1
    conn = connect(DB_PATH)
    cur = conn.cursor()
    t0 = time.perf_counter()
    try:
        cur.execute(
            """SELECT c.doc_type, c.rel_path, c.chunk_idx, snippet(chunks_fts, 1, '**', '**', '...', 15)
               FROM chunks_fts
               JOIN chunks c ON c.rowid = chunks_fts.rowid
               WHERE chunks_fts MATCH ?
               ORDER BY rank LIMIT ?""",
            (q, limit),
        )
        results = cur.fetchall()
    except sqlite3.OperationalError as e:
        print(f"FTS query error (bad syntax?): {e}", file=sys.stderr)
        return 2
    elapsed = (time.perf_counter() - t0) * 1000
    print(f"Query: {q!r}  [{len(results)} results, {elapsed:.1f}ms]")
    for dt, rel, idx, snip in results:
        print(f"  [{dt}] {rel} (chunk {idx})")
        print(f"    {snip[:300]}")
        print()
    conn.close()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drop", action="store_true", help="Nuke DB and rebuild from scratch")
    ap.add_argument("--stats", action="store_true", help="Show stats and exit")
    ap.add_argument("--query", help="Run an ad-hoc FTS5 query")
    args = ap.parse_args()

    if args.stats:
        return stats()
    if args.query:
        return query(args.query)
    return build(drop=args.drop)


if __name__ == "__main__":
    sys.exit(main())
