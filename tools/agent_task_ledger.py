#!/usr/bin/env python3
"""Memory Control Plane v0.1 -- agent task/goal ledger (continuity aid).

A memory-backed record of what the agent is trying to do, why, current state,
and what's next -- so a fresh session resumes without reconstructing context.
This is the AGENT-CONTROL layer (separate from the memory layer); it references
memory by path via evidence_links, it does not embed memory content. NOT a
project-management system. Local-only: lives in the LOCAL-ONLY memory repo,
never pushed.

Ledger: <memory_dir>/agent_task_ledger.json

Usage:
  python tools/agent_task_ledger.py create --goal "..." [--next "..."] [--state ...] [--owner session-285] [--evidence path]
  python tools/agent_task_ledger.py update --id T-... [--state ...] [--next ...] [--status open|blocked|done] [--blocker "..."] [--evidence path]
  python tools/agent_task_ledger.py list [--status open]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

MEMORY_DIR = Path(r"C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory")
LEDGER = MEMORY_DIR / "agent_task_ledger.json"
STATUSES = ("open", "blocked", "done")


def _now() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _load() -> dict:
    if LEDGER.exists():
        try:
            return json.loads(LEDGER.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {"schema_version": 1, "tasks": []}
    return {"schema_version": 1, "tasks": []}


def _save(d: dict) -> None:
    LEDGER.write_text(json.dumps(d, indent=2), encoding="utf-8")


def _find(d: dict, tid: str):
    return next((t for t in d["tasks"] if t["task_id"] == tid), None)


def create(args) -> int:
    d = _load()
    tid = f"T-{dt.datetime.now():%Y%m%d}-{len(d['tasks']) + 1:03d}"
    d["tasks"].append({
        "task_id": tid, "user_goal": args.goal,
        "current_state": args.state or "created", "next_action": args.next or "",
        "blockers": [], "evidence_links": list(args.evidence or []),
        "status": "open", "owner": args.owner or "unknown-session",
        "created": _now(), "last_updated": _now(),
    })
    _save(d)
    print(f"[ledger] created {tid}: {args.goal}")
    return 0


def update(args) -> int:
    d = _load()
    t = _find(d, args.id)
    if not t:
        print(f"[ledger] task {args.id} not found")
        return 1
    if args.state:
        t["current_state"] = args.state
    if args.next is not None:
        t["next_action"] = args.next
    if args.status:
        if args.status not in STATUSES:
            print(f"[ledger] status must be one of {STATUSES}")
            return 1
        t["status"] = args.status
    if args.blocker:
        t["blockers"].append(args.blocker)
    for e in (args.evidence or []):
        t["evidence_links"].append(e)
    t["last_updated"] = _now()
    _save(d)
    print(f"[ledger] updated {args.id} (status={t['status']})")
    return 0


def list_tasks(args) -> int:
    d = _load()
    tasks = [t for t in d["tasks"] if not args.status or t["status"] == args.status]
    if not tasks:
        print("[ledger] no tasks")
        return 0
    for t in tasks:
        print(f"  {t['task_id']}  [{t['status']}]  {t['user_goal']}")
        print(f"      state: {t['current_state']} | next: {t['next_action'] or '-'} "
              f"| owner: {t['owner']} | updated: {t['last_updated']}")
        if t["blockers"]:
            print(f"      blockers: {'; '.join(t['blockers'])}")
        if t["evidence_links"]:
            print(f"      evidence: {', '.join(t['evidence_links'])}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("create")
    c.add_argument("--goal", required=True)
    c.add_argument("--next"); c.add_argument("--state"); c.add_argument("--owner")
    c.add_argument("--evidence", action="append")
    u = sub.add_parser("update")
    u.add_argument("--id", required=True)
    u.add_argument("--state"); u.add_argument("--next"); u.add_argument("--status")
    u.add_argument("--blocker"); u.add_argument("--evidence", action="append")
    ls = sub.add_parser("list")
    ls.add_argument("--status")
    args = ap.parse_args()
    return {"create": create, "update": update, "list": list_tasks}[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main())
