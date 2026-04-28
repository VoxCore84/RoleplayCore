"""Contradiction scanner — compares memory files against the Knowledge Graph.

Reads each memory/*.md file, extracts factual claims (names, dates, amounts,
statuses), queries the KG for matching entities, and flags discrepancies.

Runs as an asyncio job inside the daemon (like freshness.py), or standalone:
    python -m tools.excluded_daemon.jobs.contradiction
"""
from __future__ import annotations

import asyncio
import json
import logging
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path

import sys
if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.excluded_daemon import config

log = logging.getLogger("contradiction")

MEMORY_DIR = Path.home() / ".claude/projects/C--Users-atayl-VoxCore/memory"
REPORT_DIR = config.REPO_ROOT / "AI_Studio" / "Reports" / "scheduled"

DEFAULT_INTERVAL = getattr(config, "CONTRADICTION_INTERVAL", 21600)

DATE_RE = re.compile(r"\b(20\d{2}[-/]\d{1,2}[-/]\d{1,2})\b")
AMOUNT_RE = re.compile(r"\$[\d,]+(?:\.\d{2})?")
STATUS_KEYWORDS = [
    "ACTIVE", "ON HOLD", "COMPLETE", "PENDING", "CLOSED", "NOT FILING",
    "FILED", "TERMINATED", "OPERATIONAL", "BACK UNDER CONSIDERATION",
]


@dataclass
class Contradiction:
    memory_file: str
    memory_line: int
    claim: str
    entity_name: str
    entity_kind: str
    source_doc: str
    source_text: str
    severity: str  # HIGH, MEDIUM, LOW


def _extract_claims(memory_path: Path) -> list[tuple[int, str, str, str]]:
    """Extract (line_no, claim_text, entity_hint, claim_type) from a memory file."""
    claims = []
    try:
        lines = memory_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return claims

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("---") or stripped.startswith("#"):
            continue

        # Date claims
        for m in DATE_RE.finditer(stripped):
            context = stripped[max(0, m.start() - 40):m.end() + 40]
            claims.append((i, context, m.group(1), "date"))

        # Amount claims
        for m in AMOUNT_RE.finditer(stripped):
            context = stripped[max(0, m.start() - 40):m.end() + 40]
            claims.append((i, context, m.group(0), "amount"))

        # Status claims (keyword in a table row or bold text)
        for kw in STATUS_KEYWORDS:
            if kw in stripped:
                claims.append((i, stripped[:200], kw, "status"))
                break

    return claims


def _query_kg_for_claim(claim_type: str, hint: str) -> list[dict]:
    """Query the KG for entities matching a claim hint."""
    try:
        import sqlite3
        if not config.KG_DB.exists():
            return []
        conn = sqlite3.connect(str(config.KG_DB))
        conn.row_factory = sqlite3.Row

        if claim_type == "date":
            rows = conn.execute(
                "SELECT e.name, e.canonical, e.metadata, m.doc_path, m.context "
                "FROM entities e JOIN mentions m ON m.entity_id = e.id "
                "WHERE e.kind = 'date' AND e.canonical LIKE ? LIMIT 10",
                (f"%{hint}%",),
            ).fetchall()
        elif claim_type == "amount":
            clean = hint.replace("$", "").replace(",", "")
            rows = conn.execute(
                "SELECT e.name, e.canonical, e.metadata, m.doc_path, m.context "
                "FROM entities e JOIN mentions m ON m.entity_id = e.id "
                "WHERE e.kind = 'amount' AND e.canonical LIKE ? LIMIT 10",
                (f"%{clean}%",),
            ).fetchall()
        else:
            rows = []

        conn.close()
        return [dict(r) for r in rows]
    except Exception as e:
        log.debug(f"KG query failed: {e}")
        return []


def scan_memory_files() -> list[Contradiction]:
    """Scan all memory files for potential contradictions against the KG."""
    contradictions = []

    if not MEMORY_DIR.exists():
        log.warning(f"memory dir not found: {MEMORY_DIR}")
        return contradictions

    if not config.KG_DB.exists():
        log.warning(f"KG database not found: {config.KG_DB}")
        return contradictions

    import sqlite3
    conn = sqlite3.connect(str(config.KG_DB))
    conn.row_factory = sqlite3.Row

    for md_file in sorted(MEMORY_DIR.glob("*.md")):
        if md_file.name == "MEMORY.md":
            continue

        claims = _extract_claims(md_file)
        rel_name = md_file.name

        for line_no, claim_text, hint, claim_type in claims:
            kg_hits = _query_kg_for_claim(claim_type, hint)
            if not kg_hits:
                continue

            for hit in kg_hits:
                source_context = hit.get("context", "")
                doc_path = hit.get("doc_path", "")

                if claim_type == "date":
                    meta = json.loads(hit.get("metadata", "{}") or "{}")
                    kg_event = meta.get("event", "")
                    if kg_event and claim_text and kg_event.lower() not in claim_text.lower():
                        contradictions.append(Contradiction(
                            memory_file=rel_name,
                            memory_line=line_no,
                            claim=claim_text[:200],
                            entity_name=hit.get("name", ""),
                            entity_kind="date",
                            source_doc=doc_path,
                            source_text=source_context[:200],
                            severity="MEDIUM",
                        ))

    conn.close()

    # Deduplicate by (memory_file, memory_line, entity_name)
    seen = set()
    deduped = []
    for c in contradictions:
        key = (c.memory_file, c.memory_line, c.entity_name)
        if key not in seen:
            seen.add(key)
            deduped.append(c)

    return deduped


def write_report(contradictions: list[Contradiction]) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d")
    path = REPORT_DIR / f"contradiction_{stamp}.md"

    lines = [
        f"# Contradiction scan — {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Memory files scanned: {len(list(MEMORY_DIR.glob('*.md')))}",
        f"Contradictions found: {len(contradictions)}",
        "",
    ]

    if contradictions:
        lines.append("| Severity | Memory File | Line | Claim | Source Doc |")
        lines.append("|----------|------------|------|-------|-----------|")
        for c in sorted(contradictions, key=lambda x: ("HIGH", "MEDIUM", "LOW").index(x.severity)):
            lines.append(
                f"| {c.severity} | `{c.memory_file}` | {c.memory_line} | "
                f"{c.claim[:80]}... | `{c.source_doc[:60]}` |"
            )
        lines.append("")
        lines.append("## Details")
        lines.append("")
        for i, c in enumerate(contradictions, 1):
            lines.append(f"### {i}. {c.memory_file}:{c.memory_line}")
            lines.append(f"- **Claim**: {c.claim}")
            lines.append(f"- **Entity**: {c.entity_name} ({c.entity_kind})")
            lines.append(f"- **Source**: `{c.source_doc}`")
            lines.append(f"- **Source text**: {c.source_text}")
            lines.append(f"- **Severity**: {c.severity}")
            lines.append("")
    else:
        lines.append("No contradictions detected.")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


async def run_once() -> dict:
    contradictions = scan_memory_files()
    path = write_report(contradictions)
    return {
        "contradictions": len(contradictions),
        "report": str(path),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


async def run_forever(interval_seconds: int = DEFAULT_INTERVAL,
                      stop_event: asyncio.Event | None = None) -> None:
    while stop_event is None or not stop_event.is_set():
        try:
            result = await run_once()
            log.info(f"contradiction scan: {result['contradictions']} found — {result['report']}")
        except Exception as e:
            log.exception(f"contradiction scan error: {e}")
        try:
            await asyncio.wait_for(
                stop_event.wait() if stop_event else asyncio.sleep(interval_seconds),
                timeout=interval_seconds if stop_event else None,
            )
            break
        except asyncio.TimeoutError:
            continue


if __name__ == "__main__":
    import asyncio
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s: %(message)s")
    result = asyncio.run(run_once())
    print(json.dumps(result, indent=2))
