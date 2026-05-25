#!/usr/bin/env python3
"""Encrypted disaster-recovery backup for the LOCAL-ONLY memory repo.

Local git protects against bad edits; it does NOT protect against a dead disk.
This produces a single AES-256, header-encrypted 7-Zip archive of the ENTIRE
memory repo -- including .git, so the restored archive is a full repo with
history -- meant to be written to a DIFFERENT physical disk (and copied
off-machine for true DR).

NO remote. NO cloud. NO unencrypted copy. Filenames are encrypted too (-mhe=on),
because the filenames themselves may be sensitive.

Secrets handling: --backup and --verify are INTERACTIVE-ONLY. 7-Zip prompts for
the passphrase directly; this tool never accepts a passphrase via env var, argv,
or any AI transcript, and refuses to run unless attached to a real terminal.
--self-test uses a throwaway, non-secret password on a temp sample only. Store
your real passphrase in a password manager -- without it the backup is
unrecoverable. (Unattended backup needs a public-key flow; see v2 backlog.)

Modes:
  --self-test         create+verify+restore round-trip on a temp sample (throwaway pw)
  --backup            encrypt the memory repo (7-Zip prompts for the passphrase)
  --verify <archive>  integrity-test an existing archive (7-Zip prompts)

Restore (manual):
  & "C:\\Program Files\\7-Zip\\7z.exe" x memory_YYYYMMDD_HHMMSS.7z -o<restore_dir>
  then <restore_dir>\\memory is a full git repo: cd in, `git log`, `git checkout`.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import secrets
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MEMORY_DIR = Path(r"C:\Users\atayl\.claude\projects\C--Users-atayl-VoxCore\memory")
DEFAULT_DEST = Path(os.environ.get("MEMORY_BACKUP_DEST", r"D:\MemoryBackups"))
SEVENZIP = Path(os.environ.get("SEVENZIP", r"C:\Program Files\7-Zip\7z.exe"))


def _7z(*args: str) -> subprocess.CompletedProcess:
    """Captured (non-interactive) 7-Zip call. Used by --self-test only."""
    return subprocess.run([str(SEVENZIP), *args], capture_output=True, text=True)


def _7z_interactive(*args: str) -> int:
    """Interactive 7-Zip call -- inherits the terminal so 7-Zip can prompt for the
    passphrase. The passphrase never touches Python, argv, env, or any transcript."""
    return subprocess.run([str(SEVENZIP), *args]).returncode


def _require_7z() -> str | None:
    if not SEVENZIP.exists():
        return f"7-Zip not found at {SEVENZIP}. Install 7-Zip or set the SEVENZIP env var."
    return None


def _require_tty(mode: str) -> bool:
    if sys.stdin.isatty() and sys.stdout.isatty():
        return True
    print(f"[memory_backup] REFUSING: {mode} is interactive-only so 7-Zip can prompt "
          "for the passphrase. Never pass a passphrase via env, argv, or an AI "
          "transcript. Run this in a real terminal -- see "
          "AI_Studio/Reports/MEMORY_PERSISTENCE_V1.md.")
    return False


def self_test() -> int:
    """Prove the create+verify+restore mechanism on a temp sample. The password
    here is a throwaway, non-secret value used only for this self-contained test."""
    err = _require_7z()
    if err:
        print(f"[memory_backup] SELF-TEST FAIL: {err}")
        return 1
    tmp = Path(tempfile.mkdtemp(prefix="membackup_selftest_"))
    try:
        sample = tmp / "sample"
        (sample / "sub").mkdir(parents=True)
        marker = "round-trip-" + secrets.token_hex(8)
        (sample / "a.md").write_text(marker, encoding="utf-8")
        (sample / "sub" / "b.md").write_text("nested-" + marker, encoding="utf-8")

        pw = secrets.token_urlsafe(16)  # throwaway, non-secret -- self-test only
        arch = tmp / "test.7z"
        a = _7z("a", "-t7z", "-mhe=on", f"-p{pw}", str(arch), str(sample))
        if a.returncode != 0:
            print(f"[memory_backup] SELF-TEST FAIL (create): {(a.stderr or a.stdout).strip()}")
            return 1
        t = _7z("t", f"-p{pw}", str(arch))
        if t.returncode != 0:
            print(f"[memory_backup] SELF-TEST FAIL (integrity): {(t.stderr or t.stdout).strip()}")
            return 1
        out = tmp / "restored"
        x = _7z("x", f"-p{pw}", f"-o{out}", "-y", str(arch))
        if x.returncode != 0:
            print(f"[memory_backup] SELF-TEST FAIL (extract): {(x.stderr or x.stdout).strip()}")
            return 1
        got = (out / "sample" / "a.md").read_text(encoding="utf-8")
        got_nested = (out / "sample" / "sub" / "b.md").read_text(encoding="utf-8")
        if got != marker or got_nested != "nested-" + marker:
            print("[memory_backup] SELF-TEST FAIL: restored content mismatch")
            return 1
        bad = _7z("t", f"-pWRONG-{pw}", str(arch))  # wrong passphrase must fail
        print("[memory_backup] SELF-TEST PASS")
        print(f"  - AES-256 header-encrypted archive created ({arch.stat().st_size} bytes)")
        print("  - integrity test passed")
        print("  - extracted to a fresh dir; content matches (incl. nested file)")
        print(f"  - wrong passphrase rejected: {'yes' if bad.returncode != 0 else 'NO (!)'}")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def backup(dest_dir: Path) -> int:
    err = _require_7z()
    if err:
        print(f"[memory_backup] FAIL: {err}")
        return 1
    if not MEMORY_DIR.exists():
        print(f"[memory_backup] FAIL: memory dir not found: {MEMORY_DIR}")
        return 1
    if not _require_tty("--backup"):
        return 2
    drive = (dest_dir.drive or "").rstrip(":")
    if drive and not Path(dest_dir.drive + "\\").exists():
        print(f"[memory_backup] FAIL: backup drive {dest_dir.drive} not available. "
              f"Set MEMORY_BACKUP_DEST / --dest to an existing location.")
        return 1
    dest_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = dest_dir / f"memory_{stamp}.7z"

    print(f"[memory_backup] creating {dest} -- 7-Zip will prompt for the passphrase...")
    # -p with NO attached value -> 7-Zip prompts interactively (passphrase off argv).
    if _7z_interactive("a", "-t7z", "-mhe=on", "-p", str(dest), str(MEMORY_DIR)) != 0:
        print("[memory_backup] FAIL: archive creation failed or was cancelled.")
        return 1
    print("[memory_backup] verifying integrity -- 7-Zip will prompt again...")
    if _7z_interactive("t", "-p", str(dest)) != 0:
        print("[memory_backup] FAIL: created but integrity test failed.")
        return 1

    mb = dest.stat().st_size / 1_048_576
    print(f"[memory_backup] OK -> {dest} ({mb:.2f} MB, AES-256, headers encrypted, integrity verified)")
    print(f"  restore: & \"{SEVENZIP}\" x \"{dest}\" -o<restore_dir>")
    print("  REMINDER: copy this archive OFF-MACHINE (USB/external) -- both internal disks share one box.")
    print(f"  non-secret metadata: Get-FileHash \"{dest}\" -Algorithm SHA256")
    return 0


def verify(archive: str) -> int:
    err = _require_7z()
    if err:
        print(f"[memory_backup] FAIL: {err}")
        return 1
    if not _require_tty("--verify"):
        return 2
    if _7z_interactive("t", "-p", archive) != 0:
        print(f"[memory_backup] VERIFY FAIL: {archive}")
        return 1
    print(f"[memory_backup] VERIFY OK: {archive} -- integrity + passphrase confirmed")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true", help="round-trip test on a temp sample")
    g.add_argument("--backup", action="store_true", help="encrypt the memory repo (interactive)")
    g.add_argument("--verify", metavar="ARCHIVE", help="integrity-test an existing archive (interactive)")
    ap.add_argument("--dest", help="override backup directory (default D:\\MemoryBackups)")
    args = ap.parse_args()

    if args.self_test:
        return self_test()
    if args.backup:
        return backup(Path(args.dest) if args.dest else DEFAULT_DEST)
    return verify(args.verify)


if __name__ == "__main__":
    raise SystemExit(main())
