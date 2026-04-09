"""
Arcanum logic module — all index-building and query functions.

Separated from arcanum_server.py so the MCP entry point can hot-reload this
module via importlib.reload(arcanum_logic) without restarting Claude Code.
Edit freely; call the arcanum_reload() MCP tool to pick up changes.

IMPORTANT: arcanum_server.py must call these functions via module-attribute
lookup (`arcanum_logic.arcanum_search(...)`), NOT via `from arcanum_logic
import arcanum_search`. The former hot-reloads; the latter binds at import.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ARCANUM_DIR = Path(os.environ.get(
    "ARCANUM_DIR",
    Path(__file__).resolve().parent.parent.parent / "doc" / "arcanum"
))

MEMORY_DIR = Path(os.environ.get(
    "MEMORY_DIR",
    Path.home() / ".claude" / "projects" / "C--Users-atayl-VoxCore" / "memory"
))

REPORTS_DIR = Path(os.environ.get(
    "REPORTS_DIR",
    Path(__file__).resolve().parent.parent.parent / "AI_Studio" / "Reports" / "ClaudeCodeInternals"
))

CASE_DIR = Path(os.environ.get(
    "CASE_DIR",
    Path.home() / "Desktop" / "IMPORTANT DOCS" / "Case_Reference"
))

IMPORTANT_DOCS_DIR = Path(os.environ.get(
    "IMPORTANT_DOCS_DIR",
    Path.home() / "Desktop" / "IMPORTANT DOCS"
))

# File extensions to index (beyond .md)
INDEX_EXTENSIONS = {".md", ".txt", ".log", ".csv", ".json", ".xml", ".html", ".htm"}

# ---------------------------------------------------------------------------
# Index state (module-level; reset by _build_index)
# ---------------------------------------------------------------------------

_index: dict[str, dict] = {}  # relative_path -> {path, title, headers, description, content, folder}
_folders: dict[str, list[str]] = defaultdict(list)  # folder -> [relative_paths]


def _index_file(prefix: str, base_dir: Path, filepath: Path):
    """Index a single file into the search index."""
    rel = filepath.relative_to(base_dir)
    key = f"{prefix}/{rel.as_posix()}"
    folder = f"{prefix}/{rel.parent.as_posix()}" if rel.parent != Path(".") else prefix

    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        content = ""

    # Extract title (first # heading for md, first non-empty line otherwise)
    title = rel.stem
    if filepath.suffix == ".md":
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
    else:
        for line in content.split("\n")[:5]:
            line = line.strip()
            if line and not line.startswith(("{", "<", "---")):
                title = line[:100]
                break

    # Extract all headers (markdown)
    headers = re.findall(r"^#{1,4}\s+(.+)$", content, re.MULTILINE)

    # Extract frontmatter description
    desc_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    description = desc_match.group(1) if desc_match else ""

    # Extract frontmatter tags (for case files)
    tags_match = re.search(r'^tags:\s*\[(.+?)\]\s*$', content, re.MULTILINE)
    tags = [t.strip().strip('"\'') for t in tags_match.group(1).split(",")] if tags_match else []

    # Extract frontmatter people
    people_match = re.search(r'^people:\s*\[(.+?)\]\s*$', content, re.MULTILINE)
    people = [p.strip().strip('"\'') for p in people_match.group(1).split(",")] if people_match else []

    # Extract frontmatter date
    date_match = re.search(r'^date:\s*["\']?(\d{4}[-/]\d{2}[-/]\d{2})["\']?\s*$', content, re.MULTILINE)
    date = date_match.group(1) if date_match else ""

    # Extract frontmatter doc_type
    doctype_match = re.search(r'^doc_type:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    doc_type = doctype_match.group(1).strip() if doctype_match else ""

    # Extract frontmatter filing_relevance
    filing_match = re.search(r'^filing_relevance:\s*\[(.+?)\]\s*$', content, re.MULTILINE)
    filing_relevance = [f.strip().strip('"\'') for f in filing_match.group(1).split(",")] if filing_match else []

    # Extract > blockquote lines (often contain source/status)
    meta_lines = re.findall(r"^>\s+(.+)$", content, re.MULTILINE)

    _index[key] = {
        "path": key,
        "abs_path": str(filepath),
        "title": title,
        "headers": headers,
        "description": description,
        "tags": tags,
        "people": people,
        "date": date,
        "doc_type": doc_type,
        "filing_relevance": filing_relevance,
        "meta": meta_lines[:3],
        "content": content,
        "folder": folder,
        "size": len(content),
        "lines": content.count("\n") + 1,
    }
    _folders[folder].append(key)


def _build_index():
    """Scan all source dirs. Build searchable index."""
    _index.clear()
    _folders.clear()

    # Markdown-only sources (existing behavior)
    md_sources = [
        ("arcanum", ARCANUM_DIR),
        ("memory", MEMORY_DIR),
        ("reports", REPORTS_DIR),
    ]

    for prefix, base_dir in md_sources:
        if not base_dir.exists():
            continue
        for md_file in base_dir.rglob("*.md"):
            _index_file(prefix, base_dir, md_file)

    # Case archive — index all text-readable files
    if CASE_DIR.exists():
        for filepath in CASE_DIR.rglob("*"):
            if filepath.is_file() and filepath.suffix.lower() in INDEX_EXTENSIONS:
                _index_file("case", CASE_DIR, filepath)

    # IMPORTANT DOCS — index all 7 folders (Angel_VA, Brand, Career, etc.)
    # Excludes Case_Reference (already indexed above with its own prefix)
    if IMPORTANT_DOCS_DIR.exists():
        for filepath in IMPORTANT_DOCS_DIR.rglob("*"):
            if filepath.is_file() and filepath.suffix.lower() in INDEX_EXTENSIONS:
                # Skip Case_Reference subtree (already indexed as "case" scope)
                try:
                    filepath.relative_to(CASE_DIR)
                    continue  # inside Case_Reference, skip
                except ValueError:
                    pass  # not inside Case_Reference, index it
                _index_file("important_docs", IMPORTANT_DOCS_DIR, filepath)


# ---------------------------------------------------------------------------
# Tool implementations (plain functions; arcanum_server.py wraps with @mcp.tool)
# ---------------------------------------------------------------------------


def arcanum_search(query: str, scope: str = "all", max_results: int = 10) -> str:
    """Full-text search across all indexed docs (arcanum, memory, reports, case, important_docs)."""
    max_results = min(max_results, 50)
    terms = query.lower().split()
    if not terms:
        return "Error: empty query"

    results = []
    for key, doc in _index.items():
        # Scope filter
        if scope != "all" and not key.startswith(scope):
            continue

        content_lower = doc["content"].lower()
        title_lower = doc["title"].lower()
        headers_lower = " ".join(doc["headers"]).lower()

        # All terms must match somewhere
        if not all(t in content_lower for t in terms):
            continue

        # Score: title > tags/people > header > description > content
        score = 0
        tags_lower = " ".join(doc.get("tags", [])).lower()
        people_lower = " ".join(doc.get("people", [])).lower()
        doc_type = doc.get("doc_type", "").lower()
        filing_lower = " ".join(doc.get("filing_relevance", [])).lower()

        for t in terms:
            if t in title_lower:
                score += 10
            if t in tags_lower:
                score += 8  # frontmatter tag match
            if t in people_lower:
                score += 8  # frontmatter people match
            if t in headers_lower:
                score += 5
            if t in doc["description"].lower():
                score += 3
            if t in doc_type:
                score += 2
            if t in filing_lower:
                score += 6  # filing relevance match

        # Extract context snippet (first matching line)
        snippet = ""
        for line in doc["content"].split("\n"):
            if all(t in line.lower() for t in terms):
                snippet = line.strip()[:200]
                break
        if not snippet:
            for line in doc["content"].split("\n"):
                if any(t in line.lower() for t in terms):
                    snippet = line.strip()[:200]
                    break

        results.append((score, key, doc["title"], snippet, doc["lines"]))

    results.sort(key=lambda x: -x[0])
    results = results[:max_results]

    if not results:
        return f"No results for '{query}' in scope '{scope}'. Try broader terms or scope='all'."

    lines = [f"## Search: '{query}' ({len(results)} results)\n"]
    for score, key, title, snippet, line_count in results:
        lines.append(f"**{key}** ({line_count} lines)")
        lines.append(f"  Title: {title}")
        if snippet:
            lines.append(f"  Match: {snippet}")
        lines.append("")

    return "\n".join(lines)


def arcanum_read(path: str) -> str:
    """Read a specific arcanum document by its path."""
    # Exact match
    if path in _index:
        doc = _index[path]
        return f"# {doc['title']}\n**Path**: {doc['path']} ({doc['lines']} lines)\n\n{doc['content']}"

    # Partial match — search by filename or path substring
    matches = []
    path_lower = path.lower().replace("\\", "/")
    for key, doc in _index.items():
        if path_lower in key.lower() or path_lower in doc["title"].lower():
            matches.append((key, doc))

    if not matches:
        return f"No document found for '{path}'. Use arcanum_index() to browse available docs."

    if len(matches) == 1:
        key, doc = matches[0]
        return f"# {doc['title']}\n**Path**: {doc['path']} ({doc['lines']} lines)\n\n{doc['content']}"

    # Multiple matches — list them
    lines = [f"Multiple matches for '{path}' — be more specific:\n"]
    for key, doc in matches[:10]:
        lines.append(f"  - **{key}** — {doc['title']}")
    return "\n".join(lines)


def arcanum_index(folder: str = "") -> str:
    """Browse the arcanum topic tree. Shows folders and their documents."""
    if not folder:
        # Top-level overview
        lines = ["# Arcanum Knowledge Base\n"]

        # Group by top-level prefix
        prefixes = defaultdict(lambda: {"folders": set(), "files": 0, "lines": 0})
        for key, doc in _index.items():
            prefix = key.split("/")[0]
            prefixes[prefix]["files"] += 1
            prefixes[prefix]["lines"] += doc["lines"]
            parts = key.split("/")
            if len(parts) > 2:
                prefixes[prefix]["folders"].add("/".join(parts[:2]))

        for prefix in sorted(prefixes):
            info = prefixes[prefix]
            folder_count = len(info["folders"])
            lines.append(f"**{prefix}/** — {info['files']} files, {info['lines']:,} lines"
                        + (f", {folder_count} subfolders" if folder_count else ""))

        lines.append(f"\n**Total**: {len(_index)} documents")
        lines.append("\nUse `arcanum_index(folder='arcanum/core')` to drill into a folder.")
        return "\n".join(lines)

    # Drill into specific folder
    folder_clean = folder.rstrip("/")
    matching = []
    subfolders = set()

    for key, doc in _index.items():
        if key.startswith(folder_clean + "/"):
            remaining = key[len(folder_clean) + 1:]
            if "/" in remaining:
                subfolders.add(remaining.split("/")[0])
            else:
                matching.append((key, doc))

    if not matching and not subfolders:
        return f"No folder '{folder}' found. Use arcanum_index() for top-level."

    lines = [f"# {folder}/\n"]

    if subfolders:
        lines.append("**Subfolders:**")
        for sf in sorted(subfolders):
            lines.append(f"  - {folder}/{sf}/")
        lines.append("")

    if matching:
        lines.append("**Documents:**")
        for key, doc in sorted(matching, key=lambda x: x[0]):
            status = ""
            if "STUB" in doc["content"][:200]:
                status = " [STUB]"
            lines.append(f"  - **{key.split('/')[-1]}** — {doc['title']}{status} ({doc['lines']}L)")
        lines.append("")

    return "\n".join(lines)


def arcanum_lookup(keyword: str, max_results: int = 15) -> str:
    """Find docs by keyword match in titles, headers, tags, people, and descriptions."""
    keyword_lower = keyword.lower()
    results = []

    for key, doc in _index.items():
        score = 0
        if keyword_lower in doc["title"].lower():
            score += 10
        if keyword_lower in " ".join(doc.get("tags", [])).lower():
            score += 8
        if keyword_lower in " ".join(doc.get("people", [])).lower():
            score += 8
        if keyword_lower in doc["description"].lower():
            score += 5
        if any(keyword_lower in h.lower() for h in doc["headers"]):
            score += 3
        if keyword_lower in key.lower():
            score += 2
        if keyword_lower in " ".join(doc.get("filing_relevance", [])).lower():
            score += 6

        if score > 0:
            results.append((score, key, doc["title"], doc["description"][:100]))

    results.sort(key=lambda x: -x[0])
    results = results[:max_results]

    if not results:
        return f"No docs match keyword '{keyword}'. Try arcanum_search for full-text."

    lines = [f"## Lookup: '{keyword}' ({len(results)} matches)\n"]
    for score, key, title, desc in results:
        lines.append(f"- **{key}** — {title}")
        if desc:
            lines.append(f"  {desc}")
    return "\n".join(lines)


def arcanum_rebuild() -> str:
    """Rebuild the arcanum index. Use after adding or modifying documents."""
    _build_index()
    folder_count = len(_folders)
    doc_count = len(_index)
    total_lines = sum(d["lines"] for d in _index.values())
    stubs = sum(1 for d in _index.values() if "STUB" in d["content"][:200])
    return (f"Index rebuilt: {doc_count} documents in {folder_count} folders, "
            f"{total_lines:,} total lines. {stubs} stubs, {doc_count - stubs} populated.")


# Build on module load (initial import AND every importlib.reload())
_build_index()
