"""Contradiction scanner — compares memory files against the Knowledge Graph.

Reads each memory/*.md file, extracts factual claims (names, dates, amounts,
statuses), queries the KG for matching entities, and flags discrepancies.

v1 (date co-occurrence) was overly aggressive — produced ~58 candidates per
scan, mostly false positives. v2 adds an optional semantic-compare filter
that calls sonnet-4-6 on each candidate and only keeps verdicts of YES.

Runs as an asyncio job inside the daemon (semantic OFF by default — keeps the
daemon's autopilot scans free), or standalone:
    python -m tools.excluded_daemon.jobs.contradiction              # semantic ON (manual default)
    python -m tools.excluded_daemon.jobs.contradiction --no-semantic # v1 raw output
"""
from __future__ import annotations

import asyncio
import json
import logging
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from pathlib import Path

import sys
if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.excluded_daemon import config
from tools.excluded_daemon.kg.build import _load_anthropic_key

log = logging.getLogger("contradiction")

SEMANTIC_MODEL = "claude-sonnet-4-6"
SEMANTIC_TIMEOUT = 30
SEMANTIC_WORKERS = 5  # parallel API calls; sonnet handles bursts well

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
    # Populated by _filter_semantic() when semantic_filter=True; empty otherwise.
    semantic_verdict: str = ""        # YES / NO / UNRELATED / ERROR / ""
    semantic_explanation: str = ""    # one-sentence rationale on YES


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


# ---------------------------------------------------------------------------
# Semantic compare (v2) — sonnet-4-6 binary classifier over v1 candidates
# ---------------------------------------------------------------------------

_SEMANTIC_PROMPT = """\
Determine if these two statements CONTRADICT each other.

Statement A (from memory synthesis): "{claim}"
Statement B (from source document): "{source_text}"

A CONTRADICTION (verdict YES) requires ALL of:
  1. Both statements make a claim about the SAME event, entity, fact, status, or measurement.
  2. The two claims DISAGREE on the value, date, status, or fact.
  3. Both claims are unambiguously about the SAME instance — not analogous events that share a date or label.

Two dates, amounts, or statuses that refer to DIFFERENT artifacts or DIFFERENT events are UNRELATED, not YES — even if the wording sounds similar. Examples:
  - "Memory file last_refreshed: 2026-04-08" vs "Master document synthesized 2026-04-11" → UNRELATED. Different artifacts (memory file vs master document), different events (refresh stamp vs synthesis run). They do not constrain each other.
  - "Adam's ADSCD: 2026-08-10" vs "ADSCD: 2026-09-01" → YES. Same fact (Adam's ADSCD), disagreeing values.
  - "Filing submitted 2026-04-01" vs "Filing received 2026-04-03" → UNRELATED. Different events (submission vs receipt) about the same filing.
  - "NARSUM PTSD downgraded" vs "NARSUM PTSD upheld" → YES. Same event (NARSUM PTSD outcome), opposing claims.
  - "Amy works at HAF/A1ZA" vs "Amy is a HAF/A1ZA analyst" → NO. Same fact, agreeing.

Bias: when in doubt between YES and UNRELATED, choose UNRELATED. False UNRELATEDs cost less than false YESes (which create noise in legal review).

Answer format (exact, no markdown, no preamble):
VERDICT: YES
EXPLANATION: <one sentence: which fact is shared, and how do the values disagree>

OR

VERDICT: NO

OR

VERDICT: UNRELATED
"""


def _semantic_compare(claim: str, source_text: str) -> tuple[str, str]:
    """Ask sonnet-4-6 if two statements actually contradict.

    Returns:
        (verdict, explanation):
            verdict in {"YES", "NO", "UNRELATED", "ERROR"}
            explanation is a short rationale (one sentence) on YES; otherwise "".
    """
    key = _load_anthropic_key()
    if not key:
        return ("ERROR", "ANTHROPIC_API_KEY not configured")

    payload = json.dumps({
        "model": SEMANTIC_MODEL,
        "max_tokens": 200,
        "messages": [{
            "role": "user",
            "content": _SEMANTIC_PROMPT.format(claim=claim, source_text=source_text),
        }],
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=SEMANTIC_TIMEOUT) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        raw = ""
        for block in data.get("content", []):
            if block.get("type") == "text":
                raw += block.get("text", "")

        verdict = "ERROR"
        explanation = ""
        for line in raw.splitlines():
            s = line.strip()
            if s.upper().startswith("VERDICT:"):
                v = s.split(":", 1)[1].strip().upper()
                if v.startswith("YES"):
                    verdict = "YES"
                elif v.startswith("UNRELATED"):
                    verdict = "UNRELATED"
                elif v.startswith("NO"):
                    verdict = "NO"
            elif s.upper().startswith("EXPLANATION:"):
                explanation = s.split(":", 1)[1].strip()
        return (verdict, explanation)
    except (urllib.error.URLError, json.JSONDecodeError, KeyError, TimeoutError) as e:
        log.debug(f"semantic_compare failed: {e}")
        return ("ERROR", f"{type(e).__name__}: {e}")
    except Exception as e:
        log.debug(f"semantic_compare unexpected error: {e}")
        return ("ERROR", f"{type(e).__name__}: {e}")


def _filter_semantic(
    contradictions: list[Contradiction],
    workers: int = SEMANTIC_WORKERS,
) -> tuple[list[Contradiction], dict]:
    """Filter v1 candidates through _semantic_compare. Keeps only YES verdicts.

    Returns (survivors, stats) where stats has counts by verdict.
    """
    if not contradictions:
        return [], {"input": 0, "YES": 0, "NO": 0, "UNRELATED": 0, "ERROR": 0}

    annotated: list[Contradiction] = []

    def _check(c: Contradiction) -> Contradiction:
        verdict, explanation = _semantic_compare(c.claim, c.source_text)
        c.semantic_verdict = verdict
        c.semantic_explanation = explanation
        return c

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(_check, c) for c in contradictions]
        for fut in as_completed(futures):
            annotated.append(fut.result())

    stats = {
        "input": len(contradictions),
        "YES": sum(1 for c in annotated if c.semantic_verdict == "YES"),
        "NO": sum(1 for c in annotated if c.semantic_verdict == "NO"),
        "UNRELATED": sum(1 for c in annotated if c.semantic_verdict == "UNRELATED"),
        "ERROR": sum(1 for c in annotated if c.semantic_verdict == "ERROR"),
    }
    survivors = [c for c in annotated if c.semantic_verdict == "YES"]
    return survivors, stats


# ---------------------------------------------------------------------------
# v1 scan + optional v2 filter
# ---------------------------------------------------------------------------

def scan_memory_files() -> list[Contradiction]:
    """Scan all memory files for potential contradictions against the KG.

    Returns raw v1 output (date co-occurrence heuristic, ~58 candidates per
    scan with high false-positive rate). To apply the v2 semantic filter,
    call `run_once(semantic_filter=True)` — that orchestrator captures
    filter stats and threads them into the report header.
    """
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


def write_report(
    contradictions: list[Contradiction],
    semantic_filter: bool = False,
    semantic_stats: dict | None = None,
) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d")
    path = REPORT_DIR / f"contradiction_{stamp}.md"

    header_mode = "v2 (semantic-filtered)" if semantic_filter else "v1 (raw co-occurrence)"
    lines = [
        f"# Contradiction scan — {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        f"Mode: **{header_mode}**",
        f"Memory files scanned: {len(list(MEMORY_DIR.glob('*.md')))}",
        f"Contradictions found: {len(contradictions)}",
        "",
    ]

    if semantic_stats:
        lines.extend([
            "## Semantic filter stats",
            "",
            f"- v1 candidates submitted: **{semantic_stats['input']}**",
            f"- YES (real contradiction): {semantic_stats['YES']}",
            f"- NO (statements agree): {semantic_stats['NO']}",
            f"- UNRELATED (different topics): {semantic_stats['UNRELATED']}",
            f"- ERROR (API failures): {semantic_stats['ERROR']}",
            "",
        ])
        if semantic_stats["ERROR"] > semantic_stats["input"] * 0.5:
            lines.extend([
                "> **WARNING**: more than half of semantic compare calls returned ERROR.",
                "> The filter is degraded — likely an API key, network, or billing issue.",
                "> The 'Contradictions found' count above is NOT a clean signal. Run with",
                "> `--no-semantic` to see the raw v1 output until the issue is resolved.",
                "",
            ])

    if contradictions:
        lines.append("| Severity | Memory File | Line | Claim | Source Doc | Verdict |")
        lines.append("|----------|------------|------|-------|-----------|---------|")
        for c in sorted(contradictions, key=lambda x: ("HIGH", "MEDIUM", "LOW").index(x.severity)):
            verdict = c.semantic_verdict or "—"
            lines.append(
                f"| {c.severity} | `{c.memory_file}` | {c.memory_line} | "
                f"{c.claim[:80]}... | `{c.source_doc[:60]}` | {verdict} |"
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
            if c.semantic_verdict:
                lines.append(f"- **Semantic verdict**: {c.semantic_verdict}")
                if c.semantic_explanation:
                    lines.append(f"- **Why**: {c.semantic_explanation}")
            lines.append("")
    else:
        if semantic_filter:
            lines.append("No contradictions survived semantic filter.")
        else:
            lines.append("No contradictions detected.")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


async def run_once(semantic_filter: bool = False) -> dict:
    contradictions = scan_memory_files()
    semantic_stats: dict | None = None

    if semantic_filter and contradictions:
        log.info(f"v1 produced {len(contradictions)} candidates; applying semantic filter...")
        contradictions, semantic_stats = _filter_semantic(contradictions)
        log.info(
            f"semantic filter: {semantic_stats['input']} input -> "
            f"{semantic_stats['YES']} YES / {semantic_stats['NO']} NO / "
            f"{semantic_stats['UNRELATED']} UNRELATED / {semantic_stats['ERROR']} ERROR"
        )
        if semantic_stats["ERROR"] > semantic_stats["input"] * 0.5:
            log.warning(
                f"semantic filter DEGRADED: {semantic_stats['ERROR']}/{semantic_stats['input']} "
                f"calls failed. Check ANTHROPIC_API_KEY and account credits. "
                f"Re-run with --no-semantic for v1 raw output."
            )

    path = write_report(
        contradictions,
        semantic_filter=semantic_filter,
        semantic_stats=semantic_stats,
    )
    return {
        "contradictions": len(contradictions),
        "semantic_filter": semantic_filter,
        "semantic_stats": semantic_stats,
        "report": str(path),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


async def run_forever(interval_seconds: int = DEFAULT_INTERVAL,
                      stop_event: asyncio.Event | None = None,
                      semantic_filter: bool = False) -> None:
    """Daemon entry — semantic_filter defaults to False to avoid burning API credits.

    The daemon's autopilot scan is for early-warning surveillance; the user runs
    `/kg-query scan` (semantic ON) when they actually want to act on results.
    """
    while stop_event is None or not stop_event.is_set():
        try:
            result = await run_once(semantic_filter=semantic_filter)
            log.info(
                f"contradiction scan ({'semantic' if semantic_filter else 'raw'}): "
                f"{result['contradictions']} found — {result['report']}"
            )
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
    import argparse
    ap = argparse.ArgumentParser(description="Contradiction scanner — v1 raw or v2 semantic-filtered")
    ap.add_argument(
        "--no-semantic",
        action="store_true",
        help="Skip semantic filter — emit raw v1 candidates (faster but ~58 false positives expected)",
    )
    ap.add_argument(
        "--semantic",
        action="store_true",
        help="Force semantic filter ON (this is the manual default — flag exists for explicitness)",
    )
    args = ap.parse_args()

    # Manual CLI default: semantic ON. --no-semantic opts out.
    semantic = not args.no_semantic

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s: %(message)s")
    result = asyncio.run(run_once(semantic_filter=semantic))
    print(json.dumps(result, indent=2))
