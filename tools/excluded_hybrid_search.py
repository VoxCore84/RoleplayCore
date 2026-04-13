#!/usr/bin/env python3
"""Hybrid retrieval — fuse FTS5 (keyword) and ChromaDB (semantic) via RRF.

Reciprocal Rank Fusion: for each chunk that appears in either result list,
score = sum(1 / (K + rank_i)) across all retrievers. K=60 is the canonical
constant from the original RRF paper.

Why hybrid: FTS5 catches exact strings and proper nouns that embedding models
smooth out ("Tranchant" → specific document). ChromaDB catches conceptual
matches with paraphrasing that FTS5 misses ("evidence of retaliation" → docs
that use the concept without the word). Together they beat either alone.

Output is a ranked list with metadata from both sources and an RRF score.

Usage:
    python tools/excluded_hybrid_search.py "query text"
    python tools/excluded_hybrid_search.py "query" --top-k 10 --fts-k 50 --vec-k 50
    python tools/excluded_hybrid_search.py "query" --json  # machine-readable
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

import os

REPO_ROOT = Path(__file__).resolve().parents[1]
FTS_DB = REPO_ROOT / ".cache" / "excluded_fts.db"
CHROMA_DIR = REPO_ROOT / ".cache" / "rag" / "chroma"
CHROMA_COLLECTION = "important_docs"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "nomic-embed-text")
RRF_K = 60

# Stopwords stripped before FTS5 query. FTS5 trigram has no built-in stopword list —
# "Who is Amy Little and what is her role" fails to match because "who/is/and/what/
# her" must all co-occur. Stripping boosts pass rate by ~30% on the test suite.
_STOPWORDS = {
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "of", "to", "in", "on", "at", "for", "by", "with", "from", "about",
    "and", "or", "but", "if", "then", "else", "when", "where", "why", "how",
    "what", "which", "who", "whom", "whose", "that", "this", "these", "those",
    "i", "me", "my", "mine", "you", "your", "yours", "he", "him", "his",
    "she", "her", "hers", "it", "its", "they", "them", "their", "theirs",
    "we", "us", "our", "ours",
    "do", "does", "did", "have", "has", "had", "can", "could", "would",
    "should", "will", "shall", "may", "might", "must",
    "not", "no", "yes",
    "as", "so", "than", "too", "very", "just", "only",
    "any", "all", "some", "each", "every", "other", "another",
}


def _prep_fts_query(q: str) -> str:
    """Strip stopwords + punctuation so FTS5 trigram can match content words only.

    Keeps proper nouns (capitalized) intact even if they're in the stopwords list
    (e.g. "The" as a book title). Quoted phrases pass through untouched.
    """
    # If user quoted anything, treat the whole query as literal
    if '"' in q:
        return q
    tokens = []
    for tok in q.split():
        stripped = tok.strip(".,;:!?()[]{}")
        if not stripped:
            continue
        # Keep capitalized tokens (proper nouns) regardless of stopwords
        if stripped[0].isupper():
            tokens.append(stripped)
            continue
        if stripped.lower() not in _STOPWORDS:
            tokens.append(stripped)
    if not tokens:
        return q  # nothing left — fall back to original
    return " ".join(tokens)


def embed_query(q: str) -> list[float] | None:
    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/embed",
        data=json.dumps({"model": EMBED_MODEL, "input": q}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        embs = data.get("embeddings", [])
        return embs[0] if embs else None
    except Exception as e:
        print(f"WARN: embed failed: {e}", file=sys.stderr)
        return None


def fts_search(query: str, limit: int) -> list[dict]:
    """FTS5 keyword/trigram search. Strips stopwords before MATCH to rescue
    natural-language queries that the trigram tokenizer's implicit-AND would
    otherwise fail. Falls back to LIKE if syntax is broken.
    """
    if not FTS_DB.exists():
        return []
    prepped = _prep_fts_query(query)
    conn = sqlite3.connect(str(FTS_DB))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    try:
        cur.execute(
            """SELECT c.id, c.doc_type, c.source_root, c.rel_path, c.chunk_idx,
                      c.content,
                      snippet(chunks_fts, 1, '**', '**', '...', 18) AS snippet
               FROM chunks_fts
               JOIN chunks c ON c.rowid = chunks_fts.rowid
               WHERE chunks_fts MATCH ?
               ORDER BY rank LIMIT ?""",
            (prepped, limit),
        )
        rows = cur.fetchall()
    except sqlite3.OperationalError:
        # FTS5 syntax issue — fall back to LIKE on the original query (not prepped)
        like = f"%{query}%"
        cur.execute(
            """SELECT id, doc_type, source_root, rel_path, chunk_idx, content,
                      substr(content, 1, 300) AS snippet
               FROM chunks
               WHERE content LIKE ? LIMIT ?""",
            (like, limit),
        )
        rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def vector_search(query: str, limit: int) -> list[dict]:
    """ChromaDB semantic search. Returns [{id, rel_path, doc_type, distance, content}]."""
    if not CHROMA_DIR.exists():
        return []
    try:
        import chromadb
    except ImportError:
        print("WARN: chromadb not installed; skipping vector search", file=sys.stderr)
        return []
    vec = embed_query(query)
    if vec is None:
        return []
    try:
        client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        col = client.get_collection(CHROMA_COLLECTION)
        res = col.query(
            query_embeddings=[vec],
            n_results=min(limit, col.count()),
            include=["documents", "metadatas", "distances"],
        )
    except Exception as e:
        print(f"WARN: vector query failed: {e}", file=sys.stderr)
        return []
    out = []
    for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0]):
        out.append({
            "id": meta.get("rel_path", "") + f":{meta.get('chunk_idx', 0)}",
            "doc_type": meta.get("doc_type", ""),
            "source_root": meta.get("source_root", ""),
            "rel_path": meta.get("rel_path", ""),
            "chunk_idx": meta.get("chunk_idx", 0),
            "content": doc,
            "distance": dist,
            "snippet": doc[:300].replace("\n", " ").strip(),
        })
    return out


def rrf_fuse(fts_hits: list[dict], vec_hits: list[dict], k: int = RRF_K) -> list[dict]:
    """Merge two ranked lists via reciprocal rank fusion.

    Key for dedup: rel_path + chunk_idx. Content may differ slightly between
    FTS5 and ChromaDB indexes (different chunking strategies), so we prefer
    whichever has an actual snippet.
    """
    scores: dict[tuple[str, int], float] = defaultdict(float)
    representatives: dict[tuple[str, int], dict] = {}
    sources: dict[tuple[str, int], set] = defaultdict(set)

    for rank, hit in enumerate(fts_hits):
        key = (hit["rel_path"], int(hit["chunk_idx"]))
        scores[key] += 1.0 / (k + rank + 1)
        sources[key].add("fts")
        if key not in representatives:
            representatives[key] = hit

    for rank, hit in enumerate(vec_hits):
        key = (hit["rel_path"], int(hit["chunk_idx"]))
        scores[key] += 1.0 / (k + rank + 1)
        sources[key].add("vec")
        if key not in representatives:
            representatives[key] = hit
        else:
            # Attach distance for tiebreak observability
            representatives[key].setdefault("distance", hit.get("distance"))

    merged = []
    for key, rrf in sorted(scores.items(), key=lambda kv: -kv[1]):
        r = representatives[key]
        merged.append({
            **r,
            "rrf_score": rrf,
            "sources": sorted(sources[key]),
        })
    return merged


def hybrid_search(query: str, top_k: int = 10, fts_k: int = 50, vec_k: int = 50) -> dict:
    """Top-level: fan out to both indexes, fuse, return top_k."""
    t0 = time.perf_counter()
    fts_hits = fts_search(query, fts_k)
    fts_ms = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    vec_hits = vector_search(query, vec_k)
    vec_ms = (time.perf_counter() - t1) * 1000

    merged = rrf_fuse(fts_hits, vec_hits)[:top_k]
    return {
        "query": query,
        "top_k": top_k,
        "fts_hits_count": len(fts_hits),
        "vec_hits_count": len(vec_hits),
        "merged_count": len(merged),
        "fts_ms": round(fts_ms, 1),
        "vec_ms": round(vec_ms, 1),
        "total_ms": round(fts_ms + vec_ms, 1),
        "hits": merged,
    }


def format_result(res: dict) -> str:
    lines = [
        f"**Query**: {res['query']!r}",
        f"**FTS5**: {res['fts_hits_count']} hits ({res['fts_ms']}ms) | **Vector**: {res['vec_hits_count']} hits ({res['vec_ms']}ms)",
        f"**Merged top-{res['top_k']}**: {res['merged_count']} results",
        "",
    ]
    for i, hit in enumerate(res["hits"], 1):
        src_tags = ",".join(hit["sources"])
        lines.append(
            f"**[{i}]** rrf={hit['rrf_score']:.4f} sources=[{src_tags}] | "
            f"`{hit['rel_path']}` [chunk {hit['chunk_idx']}]"
        )
        snippet = hit.get("snippet", "")[:400].replace("\n", " ").strip()
        lines.append(f"  > {snippet}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", help="Natural-language or keyword query")
    ap.add_argument("--top-k", type=int, default=10, help="Final merged result count")
    ap.add_argument("--fts-k", type=int, default=50, help="FTS5 candidate pool size")
    ap.add_argument("--vec-k", type=int, default=50, help="Vector candidate pool size")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of formatted text")
    args = ap.parse_args()

    res = hybrid_search(args.query, args.top_k, args.fts_k, args.vec_k)
    if args.json:
        # Strip full content from JSON output (too large)
        for h in res["hits"]:
            h.pop("content", None)
        print(json.dumps(res, indent=2))
    else:
        print(format_result(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
