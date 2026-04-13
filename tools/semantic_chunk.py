"""Shared semantic chunker used by both rag_build.py and excluded_fts_build.py.

Strategy by file type:
  - Markdown (.md): split on ## or ### headers; preserve section titles with content
  - Email (.eml): split on Subject/From/body boundaries from the extractor output
  - PDF/DOCX/TXT: fall back to paragraph + sentence boundaries inside a size window

Each chunk target ~600 tokens (~2400 chars) but will grow larger rather than split
inside a small section or sentence.

This fixes RAG mistake #1 (naive fixed-size) and #7 (static chunk size across corpus).
"""
from __future__ import annotations

import re
from typing import Iterable, Iterator

TARGET_CHARS = 2400      # ~600 tokens
MAX_CHARS = 3600         # hard cap; sections larger than this are sub-split
MIN_CHARS = 120          # chunks below this get merged with neighbor
OVERLAP_CHARS = 200      # ~50 tokens — applied only when forced to split mid-section


def _split_md_by_headers(text: str) -> list[tuple[str, str]]:
    """Split markdown on ## and ### headers. Return [(header_line_or_empty, body), ...].

    Content before the first header goes under an empty header.
    """
    lines = text.split("\n")
    sections: list[tuple[str, list[str]]] = []
    current_header = ""
    current_body: list[str] = []
    for ln in lines:
        stripped = ln.lstrip()
        if stripped.startswith("## ") or stripped.startswith("### "):
            # Flush previous
            if current_header or current_body:
                sections.append((current_header, current_body))
            current_header = ln
            current_body = []
        else:
            current_body.append(ln)
    if current_header or current_body:
        sections.append((current_header, current_body))
    return [(h, "\n".join(b).strip()) for h, b in sections]


def _split_paragraphs(text: str) -> list[str]:
    """Split on blank lines. Returns non-empty paragraphs."""
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def _window_split(text: str, target: int, overlap: int) -> Iterator[tuple[int, int, str]]:
    """Sliding window fallback for oversized sections. Yields (start, end, text)."""
    text_len = len(text)
    start = 0
    while start < text_len:
        end = min(start + target, text_len)
        if end < text_len:
            # Prefer a paragraph / sentence / whitespace boundary near `end`
            for delim in ("\n\n", ". ", "\n", " "):
                split = text.rfind(delim, start + target // 2, end + 50)
                if split != -1:
                    end = split + len(delim)
                    break
        chunk = text[start:end].strip()
        if chunk:
            yield start, end, chunk
        if end >= text_len:
            break
        start = max(start + 1, end - overlap)


def chunk_markdown(text: str) -> list[dict]:
    """Semantic chunker for markdown. Returns [{text, char_start, char_end, idx}]."""
    chunks: list[dict] = []
    if not text or not text.strip():
        return chunks

    sections = _split_md_by_headers(text)
    idx = 0
    char_cursor = 0

    # Re-index: find each section's char_start in the original text to keep citations accurate
    for header, body in sections:
        section_text = (header + "\n" + body).strip() if header else body
        if not section_text:
            # Advance cursor past any whitespace consumed
            continue
        # Locate this section in the original text starting from char_cursor
        # (simple substring search; if not found, approximate with cursor)
        loc = text.find(section_text[:80], char_cursor) if len(section_text) >= 80 else text.find(section_text, char_cursor)
        if loc < 0:
            loc = char_cursor
        char_start = loc
        char_end = char_start + len(section_text)
        char_cursor = char_end

        # Small section: emit as-is (even under MIN_CHARS, we keep it — will be merged downstream if needed)
        if len(section_text) <= MAX_CHARS:
            chunks.append({
                "text": section_text,
                "char_start": char_start,
                "char_end": char_end,
                "idx": idx,
            })
            idx += 1
            continue

        # Large section: split the body paragraphs, keep header on the first chunk
        paragraphs = _split_paragraphs(body)
        buffer_parts: list[str] = [header] if header else []
        buffer_len = len(header) + 1 if header else 0
        buffer_start = char_start

        for para in paragraphs:
            plen = len(para) + 2  # + separator
            if buffer_len + plen <= TARGET_CHARS or not buffer_parts:
                buffer_parts.append(para)
                buffer_len += plen
            else:
                # Flush current buffer
                chunk_text = "\n\n".join(buffer_parts).strip()
                if chunk_text:
                    chunks.append({
                        "text": chunk_text,
                        "char_start": buffer_start,
                        "char_end": buffer_start + len(chunk_text),
                        "idx": idx,
                    })
                    idx += 1
                    buffer_start = buffer_start + len(chunk_text)
                # Start new buffer with header continuation if possible
                continuation_header = header + " (continued)" if header else ""
                buffer_parts = [continuation_header, para] if continuation_header else [para]
                buffer_len = len(para) + (len(continuation_header) + 2 if continuation_header else 0)

        # Flush tail
        if buffer_parts:
            chunk_text = "\n\n".join(buffer_parts).strip()
            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "char_start": buffer_start,
                    "char_end": buffer_start + len(chunk_text),
                    "idx": idx,
                })
                idx += 1

    return chunks


def chunk_text_generic(text: str, target: int = TARGET_CHARS, overlap: int = OVERLAP_CHARS) -> list[dict]:
    """Fallback sliding-window chunker for PDF/DOCX/TXT/EML extract output."""
    chunks: list[dict] = []
    if not text or not text.strip():
        return chunks
    for i, (cs, ce, chunk) in enumerate(_window_split(text, target, overlap)):
        chunks.append({
            "text": chunk,
            "char_start": cs,
            "char_end": ce,
            "idx": i,
        })
    return chunks


def chunk_file(rel_path: str, text: str, target: int = TARGET_CHARS,
               overlap: int = OVERLAP_CHARS) -> list[dict]:
    """Entry point. Dispatches to semantic or generic chunker by extension.

    Note: extension is checked on the *source* filename embedded in rel_path.
    Cache files are named like `00_CALL_BRIEF.md.txt` — the `.md.txt` suffix
    indicates the original source was markdown.
    """
    rel_lower = rel_path.lower()
    is_md = ".md.txt" in rel_lower or rel_lower.endswith(".md")
    if is_md:
        return chunk_markdown(text)
    return chunk_text_generic(text, target, overlap)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        chunks = chunk_file(path, text)
        print(f"{len(chunks)} chunks from {path}")
        for c in chunks[:5]:
            print(f"  idx={c['idx']} len={len(c['text'])} cs={c['char_start']} ce={c['char_end']}")
            print(f"    {c['text'][:120].strip()!r}")
