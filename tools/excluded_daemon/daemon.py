"""Main entry point — watches Excluded/ and dispatches events to workers.

Phase B minimum: file watcher + security-gated routing + extract_worker +
ocr_worker + index_worker (FTS5 rebuild batching). No tray UI, no IPC, no
agent loop yet. Stdout logging, Ctrl+C to stop.

Run:
    python -m tools.excluded_daemon
    python -m tools.excluded_daemon --log-level DEBUG
"""
from __future__ import annotations

import argparse
import asyncio
import logging
import os
import signal
import sys
import time
from pathlib import Path

# Allow running as `python -m tools.excluded_daemon` from repo root
if __package__ is None or __package__ == "":
    # pragma: no cover
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.excluded_daemon import config
from tools.excluded_daemon.router import Pipeline
from tools.excluded_daemon.watcher import ExcludedWatcher, WorkItem
from tools.excluded_daemon.workers.extract_worker import extract
from tools.excluded_daemon.workers.ocr_worker import ocr
from tools.excluded_daemon.workers.index_worker import rebuild_fts, on_indexed
from tools.excluded_daemon.watcher import clear_dirty_flag, is_dirty


log = logging.getLogger("excluded_daemon")


def setup_logging(level: str) -> None:
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    fmt = "%(asctime)s %(name)s %(levelname)s: %(message)s"
    handlers = [logging.StreamHandler(sys.stdout)]
    try:
        fh = logging.FileHandler(config.LOG_FILE, encoding="utf-8")
        handlers.append(fh)
    except Exception as e:
        print(f"WARN: could not open log file {config.LOG_FILE}: {e}", file=sys.stderr)
    logging.basicConfig(level=level, format=fmt, handlers=handlers, force=True)


async def worker_loop(name: str, queue: asyncio.PriorityQueue,
                      stopping: asyncio.Event,
                      batch_flush_interval: float = 30.0) -> None:
    """Consume WorkItems. Batches FTS rebuilds by firing a coalesced rebuild
    every N seconds or when the queue drains."""
    dirty = False
    last_flush = time.time()

    while not stopping.is_set():
        try:
            item: WorkItem = await asyncio.wait_for(queue.get(), timeout=batch_flush_interval)
        except asyncio.TimeoutError:
            item = None

        if item is not None:
            try:
                if item.pipeline == Pipeline.EXTRACT:
                    result = await extract(item.path)
                    log.info(f"[{name}] extract {item.path.name}: ok={result.get('ok')}")
                    if result.get("ok", False):
                        dirty = True
                        await on_indexed(item.path)
                elif item.pipeline == Pipeline.OCR:
                    result = await ocr(item.path)
                    log.info(f"[{name}] ocr {item.path.name}: ok={result.get('ok')}")
                    if result.get("ok", False):
                        dirty = True
                        await on_indexed(item.path)
                elif item.pipeline == Pipeline.AUDIO:
                    log.info(f"[{name}] audio {item.path.name}: deferred (no GPU venv yet)")
                elif item.pipeline == Pipeline.MBOX:
                    log.info(f"[{name}] mbox {item.path.name}: deferred (use tools/mbox/index.py manually)")
                else:
                    log.debug(f"[{name}] nop {item.pipeline.value} {item.path.name}")
            except Exception as e:
                log.exception(f"[{name}] worker error: {e}")
            finally:
                queue.task_done()

        # Batched FTS rebuild
        if dirty and (time.time() - last_flush) >= batch_flush_interval:
            result = await rebuild_fts()
            if result.get("ok"):
                log.info(f"[{name}] fts rebuild done")
            else:
                log.warning(f"[{name}] fts rebuild failed: {result}")
            dirty = False
            last_flush = time.time()

    # Final flush on shutdown
    if dirty:
        await rebuild_fts()
    clear_dirty_flag()


async def amain(args) -> int:
    setup_logging(args.log_level)
    config.DAEMON_CACHE.mkdir(parents=True, exist_ok=True)

    # PID file
    pid = os.getpid()
    config.PID_FILE.write_text(str(pid), encoding="utf-8")
    log.info(f"pid={pid} root={config.EXCLUDED_ROOT}")

    # Dirty flag check — if cleanly shut down last run, we can skip full startup rescan
    if is_dirty():
        log.info("dirty flag present — previous run did not complete cleanly")
    else:
        log.info("clean startup — no dirty flag")

    queue: asyncio.PriorityQueue[WorkItem] = asyncio.PriorityQueue()
    watcher = ExcludedWatcher(config.EXCLUDED_ROOT, queue=queue)
    stopping = asyncio.Event()

    # Signal handlers — Windows supports SIGINT; SIGTERM is POSIX-only
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT,):
        try:
            loop.add_signal_handler(sig, lambda: stopping.set())
        except NotImplementedError:
            # Windows proactor event loop — handle Ctrl+C via KeyboardInterrupt
            pass

    async def _watcher_task():
        try:
            await watcher.start()
        except Exception as e:
            log.exception(f"watcher crashed: {e}")
            stopping.set()

    tasks = [
        asyncio.create_task(_watcher_task(), name="watcher"),
        asyncio.create_task(worker_loop("w0", queue, stopping), name="worker-0"),
        asyncio.create_task(worker_loop("w1", queue, stopping), name="worker-1"),
    ]

    # Wait on stop signal
    try:
        await stopping.wait()
    except KeyboardInterrupt:
        stopping.set()

    log.info("shutting down")
    await watcher.stop()

    # Give workers a chance to drain
    try:
        await asyncio.wait_for(queue.join(), timeout=30)
    except asyncio.TimeoutError:
        log.warning("workers did not drain in 30s; forcing exit")

    for t in tasks:
        t.cancel()
    for t in tasks:
        try:
            await t
        except (asyncio.CancelledError, Exception):
            pass

    try:
        config.PID_FILE.unlink()
    except FileNotFoundError:
        pass

    log.info("stopped cleanly")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--log-level", default="INFO",
                    choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    args = ap.parse_args()
    try:
        return asyncio.run(amain(args))
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
