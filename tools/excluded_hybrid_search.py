#!/usr/bin/env python3
"""Hybrid retrieval — fuse FTS5 (keyword) and ChromaDB (semantic) via RRF.

Reciprocal Rank Fusion: for each document that appears in either result list,
score = sum(weight / (K + rank_i)) across all retrievers. K=60 is the canonical
constant from the original RRF paper.

Retrieval pipeline (v2 — 2026-04-13):
  1. Query expansion — acronym/abbreviation resolution
  2. Entity detection — match known persons from roster
  3. FTS5 OR-mode search — partial-match ranking (not implicit AND)
  4. ChromaDB vector search — semantic similarity
  5. Cross-chunk document aggregation — best chunk per file for each retriever
  6. RRF fusion with adaptive FTS boost + noise penalties + entity boost
  7. Optional LLM reranker — Ollama re-scores top-N for precision

Usage:
    python tools/excluded_hybrid_search.py "query text"
    python tools/excluded_hybrid_search.py "query" --top-k 10 --rerank
    python tools/excluded_hybrid_search.py "query" --json
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
PERSONS_FILE = REPO_ROOT / ".cache" / "persons" / "persons.json"
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
EMBED_MODEL = os.environ.get("EMBED_MODEL", "nomic-embed-text")
RERANK_MODEL = os.environ.get("RERANK_MODEL", "gemma4:26b")
RRF_K = 60

# ---------------------------------------------------------------------------
# Noise folder penalties
# ---------------------------------------------------------------------------
NOISE_PENALTIES = [
    ("_Needs Sorted/_Archive/Images", 0.3),
    ("cr_pages/page_", 0.3),
    ("_Needs Sorted/_Archive", 0.5),
    ("Finances/04_Credit_AMEX_PayPal", 0.5),
    ("__Archive/DUP_", 0.5),
    ("__Archive/Session_Logs", 0.5),
    ("paypal_statement", 0.5),
]

# ---------------------------------------------------------------------------
# Acronym / abbreviation expansion for query enrichment
# ---------------------------------------------------------------------------
ACRONYM_MAP = {
    "NPDB": "National Practitioner Data Bank",
    "MEB": "Medical Evaluation Board",
    "IDES": "Integrated Disability Evaluation System",
    "PRHP": "Privileging and Re-Privileging of Health Professionals",
    "NARSUM": "Narrative Summary",
    "ADSCD": "Active Duty Service Commitment Date",
    "AFBCMR": "Air Force Board for Correction of Military Records",
    "SAPR": "Sexual Assault Prevention and Response",
    "VWAP": "Victim Witness Assistance Program",
    "VLC": "Victims Legal Counsel",
    "ADC": "Area Defense Counsel",
    "CDE": "Commander-Directed Evaluation",
    "IHPP": "Impaired Healthcare Providers Program",
    "TDIU": "Total Disability Individual Unemployability",
    "DCSA": "Defense Counterintelligence and Security Agency",
    "SIR": "Statement of Intent to Revoke",
    "LCSW": "Licensed Clinical Social Worker",
    "NJP": "Non-Judicial Punishment",
    "AFOSI": "Air Force Office of Special Investigations",
    "OSC": "Office of Special Counsel",
    "DHA": "Defense Health Agency",
    "IRILO": "Involuntary Release from Active Duty",
    "NMDVS": "New Mexico Department of Veterans Services",
    "VSO": "Veterans Service Organization",
    "AFW2": "Air Force Wounded Warrior",
    "DD214": "Certificate of Release or Discharge from Active Duty",
    "FRNO": "File Reference Number",
    "IG": "Inspector General",
}

# ---------------------------------------------------------------------------
# Stopwords
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Persons roster (lazy-loaded)
# ---------------------------------------------------------------------------
_persons_cache: list[dict] | None = None


def _load_persons() -> list[dict]:
    global _persons_cache
    if _persons_cache is not None:
        return _persons_cache
    if not PERSONS_FILE.exists():
        _persons_cache = []
        return _persons_cache
    try:
        data = json.loads(PERSONS_FILE.read_text(encoding="utf-8"))
        _persons_cache = data.get("persons", [])
    except Exception:
        _persons_cache = []
    return _persons_cache


def _match_persons(query: str) -> list[str]:
    """Return canonical names of persons mentioned in the query."""
    ql = query.lower()
    matched = []
    for person in _load_persons():
        canonical = person.get("canonical", "")
        aliases = person.get("aliases", [])
        all_names = [canonical.lower()] + [a.lower() for a in aliases]
        for name in all_names:
            if len(name) >= 3 and name in ql:
                matched.append(canonical)
                break
    return matched


# ---------------------------------------------------------------------------
# Query preparation
# ---------------------------------------------------------------------------
def _expand_query(query: str) -> str:
    """Expand acronyms in the query for better vector search coverage.

    The original query is kept intact; expansions are appended. This helps
    the embedding model understand domain-specific abbreviations.
    """
    expansions = []
    for tok in query.split():
        clean = tok.strip(".,;:!?()[]{}")
        if clean.upper() in ACRONYM_MAP:
            expansions.append(ACRONYM_MAP[clean.upper()])
    if not expansions:
        return query
    return query + " " + " ".join(expansions)


def _prep_fts_query(q: str) -> str:
    """Build an FTS5 OR query from natural language.

    Uses OR between content words so partial matches rank by term coverage
    (BM25 naturally scores docs with more matching terms higher). This is
    a massive improvement over the implicit-AND default where ONE missing
    term in a chunk causes zero results.

    Tokens with dashes are quoted to prevent FTS5 column-reference syntax.
    """
    if '"' in q:
        return q
    tokens = []
    for tok in q.split():
        stripped = tok.strip(".,;:!?()[]{}")
        if not stripped:
            continue
        # Keep capitalized and non-stopword tokens
        if stripped[0].isupper() or stripped.lower() not in _STOPWORDS:
            if "-" in stripped:
                tokens.append(f'"{stripped}"')
            else:
                tokens.append(stripped)
    if not tokens:
        return q
    # OR between all terms — BM25 ranks by coverage
    return " OR ".join(tokens)


# ---------------------------------------------------------------------------
# Retrieval backends
# ---------------------------------------------------------------------------
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


def _prep_fts_and(q: str) -> str:
    """Build an implicit-AND FTS5 query (all terms must match in chunk)."""
    if '"' in q:
        return q
    tokens = []
    for tok in q.split():
        stripped = tok.strip(".,;:!?()[]{}")
        if not stripped:
            continue
        if stripped[0].isupper() or stripped.lower() not in _STOPWORDS:
            tokens.append(f'"{stripped}"' if "-" in stripped else stripped)
    return " ".join(tokens) if tokens else q


def fts_search(query: str, limit: int) -> list[dict]:
    """AND-preferred FTS5 search with OR fallback.

    Tries AND first (all terms must co-occur in chunk). If AND returns fewer
    than `limit // 3` results, supplements with OR results (partial matches
    ranked by BM25 term coverage). This gives precise results when all terms
    match, and broader coverage when they don't.
    """
    if not FTS_DB.exists():
        return []
    conn = sqlite3.connect(str(FTS_DB))
    conn.row_factory = sqlite3.Row

    # Phase 1: AND query
    and_query = _prep_fts_and(query)
    and_rows = []
    try:
        and_rows = conn.execute(
            """SELECT c.id, c.doc_type, c.source_root, c.rel_path, c.chunk_idx,
                      c.content,
                      snippet(chunks_fts, 1, '**', '**', '...', 18) AS snippet
               FROM chunks_fts
               JOIN chunks c ON c.rowid = chunks_fts.rowid
               WHERE chunks_fts MATCH ?
               ORDER BY rank LIMIT ?""",
            (and_query, limit),
        ).fetchall()
    except sqlite3.OperationalError:
        pass

    # Phase 2: OR fallback only when AND is truly sparse
    or_rows = []
    if len(and_rows) < 10:
        or_query = _prep_fts_query(query)  # OR mode
        try:
            or_rows = conn.execute(
                """SELECT c.id, c.doc_type, c.source_root, c.rel_path, c.chunk_idx,
                          c.content,
                          snippet(chunks_fts, 1, '**', '**', '...', 18) AS snippet
                   FROM chunks_fts
                   JOIN chunks c ON c.rowid = chunks_fts.rowid
                   WHERE chunks_fts MATCH ?
                   ORDER BY rank LIMIT ?""",
                (or_query, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            pass

    conn.close()

    # Merge: AND results first (they're more precise), then OR results not in AND
    seen_ids = set()
    merged = []
    for row in and_rows:
        d = dict(row)
        d["_fts_mode"] = "and"
        seen_ids.add(d["id"])
        merged.append(d)
    for row in or_rows:
        d = dict(row)
        if d["id"] not in seen_ids:
            d["_fts_mode"] = "or"
            seen_ids.add(d["id"])
            merged.append(d)

    return merged[:limit]


def vector_search(query: str, limit: int) -> list[dict]:
    """ChromaDB semantic search with expanded query for better coverage."""
    if not CHROMA_DIR.exists():
        return []
    try:
        import chromadb
    except ImportError:
        print("WARN: chromadb not installed; skipping vector search", file=sys.stderr)
        return []
    expanded = _expand_query(query)
    vec = embed_query(expanded)
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


# ---------------------------------------------------------------------------
# Cross-chunk document aggregation
# ---------------------------------------------------------------------------
def _aggregate_to_docs(hits: list[dict]) -> list[dict]:
    """Collapse chunk-level results to document-level.

    For each unique rel_path, keeps the best-ranked chunk as representative
    but gives a small bonus for additional matching chunks from the same doc.
    Returns a document-level ranked list preserving the original rank order.
    """
    doc_best: dict[str, dict] = {}
    doc_count: dict[str, int] = defaultdict(int)

    for hit in hits:
        rp = hit["rel_path"]
        doc_count[rp] += 1
        if rp not in doc_best:
            doc_best[rp] = hit

    # Return in original rank order (best chunk per doc)
    seen = set()
    result = []
    for hit in hits:
        rp = hit["rel_path"]
        if rp not in seen:
            seen.add(rp)
            rep = doc_best[rp]
            rep["_doc_chunk_count"] = doc_count[rp]
            result.append(rep)
    return result


# ---------------------------------------------------------------------------
# Fusion
# ---------------------------------------------------------------------------
def _query_entity_density(query: str) -> float:
    """Fraction of non-stopword tokens that look like entities or identifiers."""
    tokens = []
    for tok in query.split():
        stripped = tok.strip(".,;:!?()[]{}")
        if not stripped:
            continue
        if stripped.lower() in _STOPWORDS:
            continue
        tokens.append(stripped)
    if not tokens:
        return 0.0
    entity_count = 0
    for tok in tokens:
        if tok[0].isupper():
            entity_count += 1
        elif any(c.isdigit() for c in tok):
            entity_count += 1
        elif "-" in tok and len(tok) > 3:
            entity_count += 1
        elif tok.isupper() and len(tok) >= 2:
            entity_count += 1
    return entity_count / len(tokens)


def _noise_penalty(rel_path: str) -> float:
    """Return a multiplier (0.0-1.0) for known noise paths."""
    for pattern, penalty in NOISE_PENALTIES:
        if pattern in rel_path:
            return penalty
    return 1.0


def rrf_fuse(
    fts_docs: list[dict],
    vec_docs: list[dict],
    k: int = RRF_K,
    fts_weight: float = 1.0,
    entity_names: list[str] | None = None,
) -> list[dict]:
    """Merge two document-level ranked lists via reciprocal rank fusion.

    Enhancements:
    - fts_weight: boost FTS5 for entity-heavy queries
    - Noise penalties: down-weight junk folders
    - Entity boost: boost docs whose path matches a detected person name
    - Multi-chunk bonus: docs with more matching chunks get a small bonus
    """
    scores: dict[str, float] = defaultdict(float)
    representatives: dict[str, dict] = {}
    sources: dict[str, set] = defaultdict(set)

    for rank, hit in enumerate(fts_docs):
        rp = hit["rel_path"]
        # Base RRF score with FTS weight
        base = fts_weight * (1.0 / (k + rank + 1))
        # Multi-chunk bonus: additional matching chunks boost score slightly
        chunk_bonus = 1.0 + 0.05 * (hit.get("_doc_chunk_count", 1) - 1)
        scores[rp] += base * chunk_bonus
        sources[rp].add("fts")
        if rp not in representatives:
            representatives[rp] = hit

    for rank, hit in enumerate(vec_docs):
        rp = hit["rel_path"]
        base = 1.0 / (k + rank + 1)
        chunk_bonus = 1.0 + 0.05 * (hit.get("_doc_chunk_count", 1) - 1)
        scores[rp] += base * chunk_bonus
        sources[rp].add("vec")
        if rp not in representatives:
            representatives[rp] = hit
        else:
            representatives[rp].setdefault("distance", hit.get("distance"))

    # Apply noise penalties
    for rp in scores:
        scores[rp] *= _noise_penalty(rp)

    # Entity boost: if a detected person name appears in the rel_path, boost 1.5x
    if entity_names:
        for rp in scores:
            rp_lower = rp.lower()
            for name in entity_names:
                # Match last name or full canonical in the path
                parts = name.lower().split()
                if any(part in rp_lower for part in parts if len(part) >= 3):
                    scores[rp] *= 1.5
                    break

    merged = []
    for rp, rrf in sorted(scores.items(), key=lambda kv: -kv[1]):
        r = representatives[rp]
        merged.append({
            **r,
            "rrf_score": rrf,
            "sources": sorted(sources[rp]),
        })
    return merged


# ---------------------------------------------------------------------------
# Reranker (Ollama-based)
# ---------------------------------------------------------------------------
def _rerank_with_ollama(query: str, hits: list[dict], top_n: int = 10) -> list[dict]:
    """Re-score top candidates using Ollama LLM for relevance judgment.

    Sends a concise prompt for each candidate and parses a 0-10 score.
    Combines LLM score with original RRF score for final ranking.
    """
    if not hits:
        return hits

    candidates = hits[:top_n]
    rest = hits[top_n:]

    for hit in candidates:
        passage = (hit.get("content") or hit.get("snippet") or "")[:400]
        prompt = (
            f"Rate how relevant this passage is to the query. "
            f"Reply with ONLY a number 0-10.\n\n"
            f"Query: {query}\n\n"
            f"Passage: {passage}\n\n"
            f"Relevance score:"
        )
        try:
            req = urllib.request.Request(
                f"{OLLAMA_URL}/api/generate",
                data=json.dumps({
                    "model": RERANK_MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"num_predict": 10, "temperature": 0.0},
                }).encode("utf-8"),
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            response_text = result.get("response", "").strip()
            # Parse first number from response
            score = 0.0
            for word in response_text.split():
                cleaned = word.strip(".,;:!/()[]")
                try:
                    score = float(cleaned)
                    break
                except ValueError:
                    continue
            hit["rerank_score"] = min(max(score, 0.0), 10.0)
        except Exception:
            hit["rerank_score"] = 5.0  # neutral default on failure

    # Combine: normalized rerank score (0-1) blended with RRF score
    max_rrf = max((h["rrf_score"] for h in candidates), default=1.0)
    for hit in candidates:
        rrf_norm = hit["rrf_score"] / max_rrf if max_rrf > 0 else 0
        rerank_norm = hit["rerank_score"] / 10.0
        # 60% reranker, 40% original RRF — reranker dominates but RRF breaks ties
        hit["combined_score"] = 0.6 * rerank_norm + 0.4 * rrf_norm

    candidates.sort(key=lambda h: -h["combined_score"])
    return candidates + rest


# ---------------------------------------------------------------------------
# Main search
# ---------------------------------------------------------------------------
def hybrid_search(
    query: str,
    top_k: int = 10,
    fts_k: int = 150,
    vec_k: int = 100,
    rerank: bool = False,
) -> dict:
    """Top-level: expand, retrieve, aggregate, fuse, optionally rerank."""
    entity_density = _query_entity_density(query)
    fts_weight = 2.5 if entity_density > 0.6 else 1.0
    entity_names = _match_persons(query)

    t0 = time.perf_counter()
    fts_hits = fts_search(query, fts_k)
    fts_docs = _aggregate_to_docs(fts_hits)
    fts_ms = (time.perf_counter() - t0) * 1000

    t1 = time.perf_counter()
    vec_hits = vector_search(query, vec_k)
    vec_docs = _aggregate_to_docs(vec_hits)
    vec_ms = (time.perf_counter() - t1) * 1000

    merged = rrf_fuse(fts_docs, vec_docs, fts_weight=fts_weight, entity_names=entity_names)

    rerank_ms = 0.0
    if rerank and merged:
        t2 = time.perf_counter()
        merged = _rerank_with_ollama(query, merged, top_n=min(10, len(merged)))
        rerank_ms = (time.perf_counter() - t2) * 1000

    merged = merged[:top_k]
    return {
        "query": query,
        "top_k": top_k,
        "fts_weight": fts_weight,
        "entity_density": round(entity_density, 2),
        "entity_names": entity_names,
        "fts_hits_count": len(fts_hits),
        "fts_docs_count": len(fts_docs),
        "vec_hits_count": len(vec_hits),
        "vec_docs_count": len(vec_docs),
        "merged_count": len(merged),
        "fts_ms": round(fts_ms, 1),
        "vec_ms": round(vec_ms, 1),
        "rerank_ms": round(rerank_ms, 1),
        "total_ms": round(fts_ms + vec_ms + rerank_ms, 1),
        "reranked": rerank,
        "hits": merged,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def format_result(res: dict) -> str:
    lines = [
        f"**Query**: {res['query']!r}",
        f"**FTS5**: {res['fts_docs_count']} docs from {res['fts_hits_count']} chunks ({res['fts_ms']}ms) "
        f"| **Vector**: {res['vec_docs_count']} docs from {res['vec_hits_count']} chunks ({res['vec_ms']}ms)",
    ]
    if res.get("entity_names"):
        lines.append(f"**Entities**: {', '.join(res['entity_names'])}")
    if res.get("reranked"):
        lines.append(f"**Reranked**: top-10 ({res['rerank_ms']}ms)")
    lines.append(f"**Merged top-{res['top_k']}**: {res['merged_count']} results")
    lines.append("")
    for i, hit in enumerate(res["hits"], 1):
        src_tags = ",".join(hit["sources"])
        score_str = f"rrf={hit['rrf_score']:.4f}"
        if "combined_score" in hit:
            score_str += f" rerank={hit.get('rerank_score', '?')}"
        lines.append(
            f"**[{i}]** {score_str} sources=[{src_tags}] | "
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
    ap.add_argument("--fts-k", type=int, default=150, help="FTS5 candidate pool size")
    ap.add_argument("--vec-k", type=int, default=100, help="Vector candidate pool size")
    ap.add_argument("--rerank", action="store_true", help="Enable LLM reranker on top-10")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of formatted text")
    args = ap.parse_args()

    res = hybrid_search(args.query, args.top_k, args.fts_k, args.vec_k, rerank=args.rerank)
    if args.json:
        for h in res["hits"]:
            h.pop("content", None)
        print(json.dumps(res, indent=2))
    else:
        print(format_result(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
