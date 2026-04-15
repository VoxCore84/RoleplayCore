"""
folder_index.py — Walk a directory tree and generate a structured JSON manifest.

Usage:
    python tools/folder_index.py <dir> [options]

Options:
    -o, --output <path>     Write JSON manifest to this file (default: stdout)
    --summary               Print a human-readable summary instead of full JSON
    --types <exts>          Comma-separated extension filter, e.g. .pdf,.docx,.eml
    --max-depth <n>         Limit directory recursion depth (0 = unlimited)
    --preview <n>           Include first N bytes of each text file as a preview field
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone


def human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"


def read_preview(path: str, max_bytes: int) -> str | None:
    """Return first max_bytes of a file as a UTF-8 string, or None on failure."""
    try:
        with open(path, "rb") as fh:
            raw = fh.read(max_bytes)
        return raw.decode("utf-8", errors="replace")
    except OSError:
        return None


def walk_tree(
    root: str,
    allowed_exts: set[str] | None,
    max_depth: int,
    preview_bytes: int,
) -> tuple[dict, dict]:
    """
    Returns (tree, stats).

    tree is a nested dict:
        {
            "path": "<abs>",
            "name": "<basename>",
            "type": "directory" | "file",
            "size": <bytes>,          # files only
            "mtime": "<iso8601>",     # files only
            "ext": ".pdf",            # files only
            "preview": "...",         # files only, if --preview requested
            "children": [...]         # directories only
        }

    stats is a flat summary dict.
    """
    stats: dict = {
        "total_files": 0,
        "total_dirs": 0,
        "total_bytes": 0,
        "by_extension": {},
        "skipped_by_filter": 0,
    }

    def _walk(path: str, depth: int) -> dict:
        node: dict = {
            "path": path.replace("\\", "/"),
            "name": os.path.basename(path),
            "type": "directory",
            "children": [],
        }
        stats["total_dirs"] += 1

        try:
            entries = sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError as exc:
            print(f"[WARN] Cannot read {path}: {exc}", file=sys.stderr)
            return node

        for entry in entries:
            if entry.is_dir(follow_symlinks=False):
                if max_depth == 0 or depth < max_depth:
                    node["children"].append(_walk(entry.path, depth + 1))
                else:
                    # Emit a stub so agents know the subtree exists
                    node["children"].append({
                        "path": entry.path.replace("\\", "/"),
                        "name": entry.name,
                        "type": "directory",
                        "truncated": True,
                    })
                    stats["total_dirs"] += 1
            elif entry.is_file(follow_symlinks=False):
                ext = os.path.splitext(entry.name)[1].lower()
                if allowed_exts is not None and ext not in allowed_exts:
                    stats["skipped_by_filter"] += 1
                    continue
                try:
                    st = entry.stat()
                except OSError:
                    continue
                mtime = datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat()
                file_node: dict = {
                    "path": entry.path.replace("\\", "/"),
                    "name": entry.name,
                    "type": "file",
                    "ext": ext,
                    "size": st.st_size,
                    "size_human": human_size(st.st_size),
                    "mtime": mtime,
                }
                if preview_bytes > 0:
                    preview = read_preview(entry.path, preview_bytes)
                    if preview is not None:
                        file_node["preview"] = preview
                node["children"].append(file_node)
                stats["total_files"] += 1
                stats["total_bytes"] += st.st_size
                stats["by_extension"][ext] = stats["by_extension"].get(ext, 0) + 1

        return node

    tree = _walk(root, 0)
    return tree, stats


def print_summary(stats: dict, root: str, output_path: str | None) -> None:
    print(f"\nFolder: {root}")
    print(f"  Files   : {stats['total_files']:,}")
    print(f"  Dirs    : {stats['total_dirs']:,}")
    print(f"  Size    : {human_size(stats['total_bytes'])}")
    if stats["skipped_by_filter"]:
        print(f"  Skipped : {stats['skipped_by_filter']:,}  (type filter)")
    if stats["by_extension"]:
        print("  By extension:")
        for ext, count in sorted(stats["by_extension"].items(), key=lambda x: -x[1]):
            print(f"    {ext or '(no ext)':>10}  {count:>6,}")
    if output_path:
        print(f"\n  Manifest : {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Walk a directory tree and emit a JSON manifest for agent consumption."
    )
    parser.add_argument("dir", help="Root directory to index")
    parser.add_argument("-o", "--output", metavar="PATH", help="Write JSON to this file")
    parser.add_argument("--summary", action="store_true", help="Print human-readable summary only")
    parser.add_argument("--types", metavar="EXTS", help="Comma-separated extensions to include, e.g. .pdf,.docx")
    parser.add_argument("--max-depth", metavar="N", type=int, default=0, help="Max recursion depth (0 = unlimited)")
    parser.add_argument("--preview", metavar="N", type=int, default=0, help="Embed first N bytes of each file as preview text")
    args = parser.parse_args()

    root = os.path.abspath(args.dir)
    if not os.path.isdir(root):
        print(f"ERROR: '{root}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    allowed_exts: set[str] | None = None
    if args.types:
        allowed_exts = {e.strip().lower() if e.strip().startswith(".") else f".{e.strip().lower()}"
                        for e in args.types.split(",")}

    print(f"Indexing: {root}", file=sys.stderr)
    if allowed_exts:
        print(f"  Filter : {', '.join(sorted(allowed_exts))}", file=sys.stderr)
    if args.max_depth:
        print(f"  Depth  : {args.max_depth}", file=sys.stderr)

    tree, stats = walk_tree(root, allowed_exts, args.max_depth, args.preview)

    manifest = {
        "generated": datetime.now(tz=timezone.utc).isoformat(),
        "root": root.replace("\\", "/"),
        "stats": stats,
        "tree": tree,
    }

    if args.summary:
        print_summary(stats, root, args.output)
    else:
        json_str = json.dumps(manifest, indent=2, ensure_ascii=False)
        if args.output:
            os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as fh:
                fh.write(json_str)
            print_summary(stats, root, args.output)
        else:
            print(json_str)

    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
