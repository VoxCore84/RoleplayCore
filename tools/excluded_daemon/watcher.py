"""Filesystem watcher for the Excluded/ corpus.

Uses watchdog.observers.Observer to monitor all file events under EXCLUDED_ROOT.
Applies debouncing so word-processor saves don't fire N times. Pushes routing
decisions into an asyncio event queue consumed by workers.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileSystemEvent
except ImportError:  # pragma: no cover
    Observer = None
    FileSystemEventHandler = object
    FileSystemEvent = None

from . import config
from .router import Pipeline, RoutingDecision, route, in_high_priority_folder

log = logging.getLogger(__name__)

# Dirty flag — set when any new event is enqueued, cleared by daemon after queue drain.
# Lets daemon skip full-rescan on restart if no work happened.
DIRTY_FLAG = config.DAEMON_CACHE / "excluded_dirty.flag"


def touch_dirty_flag() -> None:
    try:
        DIRTY_FLAG.parent.mkdir(parents=True, exist_ok=True)
        DIRTY_FLAG.touch()
    except Exception:
        pass


def clear_dirty_flag() -> None:
    try:
        DIRTY_FLAG.unlink()
    except FileNotFoundError:
        pass
    except Exception:
        pass


def is_dirty() -> bool:
    return DIRTY_FLAG.exists()


@dataclass(order=True)
class WorkItem:
    priority: int
    ts: float                   # event timestamp; used as tiebreaker
    path: Path = field(compare=False)
    action: str = field(default="created", compare=False)
    pipeline: Pipeline = field(default=Pipeline.SKIP, compare=False)
    reason: str = field(default="", compare=False)


class _DebounceMap:
    """Maps path → last-event timestamp. Caller decides when to fire."""
    def __init__(self, window: float):
        self._map: dict[Path, float] = {}
        self._window = window

    def touch(self, path: Path) -> None:
        self._map[path] = time.time()

    def is_quiet(self, path: Path) -> bool:
        """True if `window` seconds have elapsed since last touch."""
        t = self._map.get(path)
        if t is None:
            return True
        return (time.time() - t) >= self._window

    def pop_quiet(self) -> list[Path]:
        """Return paths that have gone quiet, removing them from the map."""
        now = time.time()
        ready = [p for p, t in self._map.items() if (now - t) >= self._window]
        for p in ready:
            del self._map[p]
        return ready


class _Handler(FileSystemEventHandler):
    """watchdog callback bridge → debounce map."""
    def __init__(self, debounce: _DebounceMap, on_delete: Callable[[Path], None]):
        super().__init__()
        self._debounce = debounce
        self._on_delete = on_delete

    def on_created(self, event):   # type: ignore[override]
        if not event.is_directory:
            self._debounce.touch(Path(event.src_path))

    def on_modified(self, event):  # type: ignore[override]
        if not event.is_directory:
            self._debounce.touch(Path(event.src_path))

    def on_moved(self, event):     # type: ignore[override]
        if not event.is_directory:
            # Treat as create at new path + delete at old
            self._debounce.touch(Path(event.dest_path))
            self._on_delete(Path(event.src_path))

    def on_deleted(self, event):   # type: ignore[override]
        if not event.is_directory:
            self._on_delete(Path(event.src_path))


class ExcludedWatcher:
    """Main watcher. Emits WorkItems into an asyncio PriorityQueue."""
    def __init__(self, root: Path = config.EXCLUDED_ROOT,
                 queue: asyncio.PriorityQueue | None = None,
                 debounce_sec: float = config.DEBOUNCE_SECONDS):
        if Observer is None:
            raise RuntimeError("watchdog package not installed. pip install watchdog")
        self.root = root
        self.queue = queue or asyncio.PriorityQueue()
        self._debounce = _DebounceMap(debounce_sec)
        self._debounce_window = debounce_sec
        self._observer = Observer()
        self._stopping = asyncio.Event()
        self._deleted_paths: set[Path] = set()

    def _on_delete(self, path: Path) -> None:
        self._deleted_paths.add(path)

    async def start(self) -> None:
        """Start the watchdog observer and the debounce-flush loop."""
        handler = _Handler(self._debounce, self._on_delete)
        self._observer.schedule(handler, str(self.root), recursive=True)
        self._observer.start()
        log.info(f"Watching: {self.root} (recursive, debounce={self._debounce_window}s)")

        # Flush loop: every half-debounce-window, drain quiet paths and enqueue
        try:
            while not self._stopping.is_set():
                await asyncio.sleep(self._debounce_window / 2)
                for path in self._debounce.pop_quiet():
                    if not path.exists():
                        continue
                    decision = route(path, self.root)
                    if decision.pipeline in (Pipeline.SKIP,):
                        log.debug(f"skip {path}: {decision.reason}")
                        continue
                    item = WorkItem(
                        priority=decision.priority,
                        ts=time.time(),
                        path=path,
                        action="upsert",
                        pipeline=decision.pipeline,
                        reason=decision.reason,
                    )
                    if decision.pipeline == Pipeline.SECURITY:
                        log.warning(f"security-skip {path}: {decision.reason}")
                        # Do NOT enqueue. Just record.
                        continue
                    await self.queue.put(item)
                    touch_dirty_flag()
                    hp_tag = " [HIGH-PRIORITY]" if in_high_priority_folder(path, self.root) else ""
                    log.info(f"enqueue {decision.pipeline.value} prio={decision.priority}{hp_tag} {path.relative_to(self.root)}")
                # Handle deletes
                for path in list(self._deleted_paths):
                    await self.queue.put(WorkItem(
                        priority=1, ts=time.time(), path=path,
                        action="delete", pipeline=Pipeline.SKIP,
                        reason="deletion",
                    ))
                    self._deleted_paths.discard(path)
        finally:
            self._observer.stop()
            self._observer.join(timeout=5)
            log.info("watcher stopped")

    async def stop(self) -> None:
        self._stopping.set()
