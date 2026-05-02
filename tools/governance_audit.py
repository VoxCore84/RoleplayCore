"""Append-only governance audit log.

Every governance decision (security refusal, readonly-write block, scope
quarantine, classification gate) writes a single JSONL row to
``.cache/governance_audit.jsonl`` so the diligence team can answer
"prove you didn't process this sealed document" by grepping the log.

Schema:
    {
      "ts":            "2026-05-02T01:23:45Z",
      "ts_unix":       1745540625,
      "decision":      "SECURITY_REFUSE_FILENAME" | "SECURITY_REFUSE_CONTENT" |
                       "READONLY_WRITE_BLOCKED" | "SKIP_FOLDER" |
                       "EXTRACT" | "OCR" | "TRANSCRIBE" | "EMBED" |
                       "QUARANTINE_OOS" | "QUARANTINE_SEALED",
      "path":          "<rel_path or absolute>",
      "reason":        "<short reason string>",
      "source":        "extract_cache" | "router" | "<other module>",
      "pipeline":      "<Pipeline.* enum value, optional>",
      "model_version": "<embedder/asr/judge model id, optional>",
      "extra":         { ... },     # any additional context
    }

The log is append-only. There is NO rotation by design — diligence wants the
full history. If the file gets large (>100MB), archive monthly with
``governance_audit_YYYYMM.jsonl`` rename, but never delete.
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG_PATH = REPO_ROOT / ".cache" / "governance_audit.jsonl"

_lock = Lock()
_log_path: Path = DEFAULT_LOG_PATH


def set_log_path(path: str | os.PathLike) -> None:
    """Override the audit log destination (mainly for tests)."""
    global _log_path
    _log_path = Path(path)


def get_log_path() -> Path:
    return _log_path


def log_decision(
    decision: str,
    path: str | os.PathLike,
    reason: str = "",
    *,
    source: str = "",
    pipeline: str = "",
    model_version: str = "",
    **extra: Any,
) -> None:
    """Append one governance decision row.

    Failure to log is logged to stderr but never raises — governance must not
    block work because of disk-full or rotation issues. (The diligence story
    survives a partial log; it does not survive a daemon that crashed because
    its audit log was full.)
    """
    record = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ts_unix": int(time.time()),
        "decision": decision,
        "path": str(path),
        "reason": reason,
    }
    if source:
        record["source"] = source
    if pipeline:
        record["pipeline"] = pipeline
    if model_version:
        record["model_version"] = model_version
    if extra:
        record["extra"] = extra
    line = json.dumps(record, ensure_ascii=False)
    try:
        _log_path.parent.mkdir(parents=True, exist_ok=True)
        with _lock, _log_path.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception as e:
        import sys
        print(f"[governance_audit] log write failed: {e}", file=sys.stderr)


def query(
    decisions: list[str] | None = None,
    path_substr: str | None = None,
    since_ts: int | None = None,
    limit: int = 1000,
) -> list[dict]:
    """Read the audit log into memory and filter. For ad-hoc queries; not for hot paths."""
    if not _log_path.exists():
        return []
    out: list[dict] = []
    decision_set = set(decisions) if decisions else None
    with _log_path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                record = json.loads(line)
            except Exception:
                continue
            if decision_set and record.get("decision") not in decision_set:
                continue
            if path_substr and path_substr.lower() not in record.get("path", "").lower():
                continue
            if since_ts and record.get("ts_unix", 0) < since_ts:
                continue
            out.append(record)
            if len(out) >= limit:
                break
    return out


def stats() -> dict:
    """Aggregate counts by decision type. Useful for monthly calibration scorecard."""
    from collections import Counter
    if not _log_path.exists():
        return {"total": 0, "by_decision": {}, "by_source": {}}
    decisions = Counter()
    sources = Counter()
    total = 0
    with _log_path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            total += 1
            decisions[rec.get("decision", "UNKNOWN")] += 1
            if rec.get("source"):
                sources[rec["source"]] += 1
    return {
        "total": total,
        "by_decision": dict(decisions),
        "by_source": dict(sources),
        "log_path": str(_log_path),
    }


# CLI for ad-hoc queries
def _main():
    import argparse
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("stats")
    q = sub.add_parser("query")
    q.add_argument("--decision", action="append")
    q.add_argument("--path", help="substring match")
    q.add_argument("--since-days", type=int, default=None)
    q.add_argument("--limit", type=int, default=100)
    args = p.parse_args()

    if args.cmd == "stats":
        st = stats()
        print(json.dumps(st, indent=2))
    elif args.cmd == "query":
        since = None
        if args.since_days:
            since = int(time.time()) - args.since_days * 86400
        rows = query(decisions=args.decision, path_substr=args.path, since_ts=since, limit=args.limit)
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))
        print(f"\n[{len(rows)} rows]")


if __name__ == "__main__":
    _main()
