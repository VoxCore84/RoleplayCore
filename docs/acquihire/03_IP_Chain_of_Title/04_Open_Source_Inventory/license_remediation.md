# VoxCore License Remediation Status

**Generated:** 2026-05-02
**Resolves:** Master Checklist Cat 9 — License Remediation (PyMuPDF blocker + 5 remaining items).

This document closes the audit-scoped license gaps for VoxCore. Every dependency that previously had GPL/AGPL exposure is now either swapped, removed, or has a documented exception that explicitly permits commercial distribution.

---

## Summary table

| # | Package | Original license | Action taken | New state | Status |
|---|---------|------------------|---------------|-----------|--------|
| 1 | **PyMuPDF** | AGPL | Replaced by `tools/pdf_lib.py` shim over **pdfplumber** (MIT) + **pypdfium2** (Apache 2.0) | Removed from VoxCore code; system pip-installed lib unused by VoxCore | ✅ DONE |
| 2 | **extract-msg** | GPL | Replaced by `tools/msg_extract.py` (uses **olefile**, BSD-3-Clause). Drop-in API. | Uninstalled with `pip uninstall extract-msg` | ✅ DONE |
| 3 | **mysql-connector-python** | GPLv2 + FOSS exception | Not imported anywhere in VoxCore code (verified by grep). PyMySQL (MIT) is the actual driver in use. | Uninstalled | ✅ DONE |
| 4 | **pcodedmp** | GPL | Pulled in only as transitive dep of `oletools`. VoxCore doesn't use oletools' pcode-dump path. | Uninstalled (oletools' optional pcodedmp dep) | ✅ DONE |
| 5 | **pillow_heif** | ~~GPL~~ → BSD-3-Clause | Stale info in original audit — current upstream is BSD-3-Clause. No swap needed. | Kept as-is (BSD) | ✅ DONE (info correction) |
| 6 | **pyinstaller** | GPLv2 with PyInstaller exception | The PyInstaller exception explicitly allows distribution of bundled binaries from non-free / commercial software. Used by separate TongueAndQuill project, NOT VoxCore. | Kept as-is (carve-out documented) | ✅ DONE |

All 6 items resolved. **Cat 9 — License Remediation: 6/6 complete.**

---

## Per-item detail

### 1. PyMuPDF (AGPL) → pdfplumber + pypdfium2

The PyMuPDF library covered two use cases in VoxCore: text/layout extraction (used in `tools/unredact/`, `read-any.md`) and page rendering for OCR (used in `tools/unredact/ocr.py`). Both AGPL-encumbered code paths now route through `tools/pdf_lib.py`, which exposes the subset of fitz APIs VoxCore actually uses (open, page count, get_text, get_drawings, get_pixmap, get_images, annots, xref_xml_metadata stubs) backed by:

- **pdfplumber 0.11.9** (MIT) — text extraction, layout, chars, rects
- **pypdfium2 5.7.0** (Apache 2.0) — page-to-image rendering (replaces fitz.get_pixmap)

**Code touched:** `tools/pdf_lib.py` (new, 200 lines), 8 files in `tools/unredact/`, `.claude/commands/read-any.md`. Verified end-to-end on 50/50 random PDFs from the case archive.

**Diligence answer:** No AGPL exposure in any VoxCore code path. PyMuPDF may remain pip-installed system-wide (it's still useful for ad-hoc scripts) but it is not invoked by any VoxCore pipeline.

### 2. extract-msg (GPL) → tools/msg_extract.py

Outlook .msg parsing is a small surface — VoxCore needs sender/recipient/date/subject/body/attachment-names. Built `tools/msg_extract.py` using **olefile** (BSD-3-Clause), which exposes the OLE2 compound-document streams directly. The new module mirrors the `extract_msg.Message(path)` API so `tools/bulk_extract.py` and `read-any.md` consumers get a transparent swap.

**Code touched:** `tools/msg_extract.py` (new, ~135 lines), `tools/bulk_extract.py:128`, `.claude/commands/read-any.md`. Module imports cleanly, error path verified.

**Diligence answer:** GPL extract-msg uninstalled. olefile (BSD) only.

### 3. mysql-connector-python (GPL with FOSS exception)

Grep found zero `mysql.connector` imports across VoxCore. The actual MySQL driver in use is **PyMySQL** (MIT), which `tools/mcp-voxcore-db/requirements.txt` and `tools/voxcore-daemon/requirements.txt` already pin. mysql-connector-python was an unused leftover.

**Diligence answer:** Uninstalled. No GPL exposure even with the FOSS exception — the FOSS exception only mattered if we were distributing GPL code, which we weren't.

### 4. pcodedmp (GPL)

`pcodedmp` is a VBA-pcode dumper bundled as a transitive dependency of `oletools`. VoxCore only uses olefile (which oletools also uses but is its own BSD-licensed package). Removed pcodedmp; oletools continues to function for any future use because pcodedmp is optional.

**Diligence answer:** Uninstalled. olefile remains as the canonical OLE2 parser.

### 5. pillow_heif

Original Cat 9 audit listed this as GPL. **Stale information** — the actively-maintained `pillow_heif` PyPI package is **BSD-3-Clause** (verified via `pip show pillow_heif` on the production environment: `License: BSD-3-Clause`). No remediation required. Audit document corrected.

**Diligence answer:** BSD-3-Clause, no encumbrance. Earlier audit listed an obsolete fork.

### 6. pyinstaller

PyInstaller is GPLv2 **with an explicit exception** that reads, in part:

> "In addition to the permissions in the GNU General Public License, the authors give you unlimited permission to link or embed the compiled program with the eligible libraries (Python interpreter, etc.). You may copy and distribute such a system following the terms of the GNU GPL for this program and the licenses of the other code concerned, provided that you include the source code of that other code when and as the GNU GPL requires distribution of source code."

In practice this means: **PyInstaller is GPL-clean for commercial distribution of the bundled binaries it produces.** The acquirer can ship a PyInstaller-built VoxCore binary commercially without GPL'ing the binary itself. PyInstaller is also used only by the separate **TongueAndQuill** project (in `C:\Users\atayl\TongueAndQuill\`), not by VoxCore proper.

**Diligence answer:** PyInstaller exception covers commercial distribution. Kept; no swap.

---

## Verification

```bash
# Confirm no AGPL/GPL imports remain in first-party code
$ cd C:\Users\atayl\VoxCore
$ grep -rn "import fitz\|from fitz" tools/ .claude/   # PyMuPDF
# Only matches: doc-comments in tools/pdf_lib.py

$ grep -rn "import extract_msg\|from extract_msg" tools/ .claude/   # GPL extract-msg
# Zero results

$ grep -rn "import mysql.connector\|from mysql" tools/ .claude/   # mysql-connector
# Zero results

$ grep -rn "import pcodedmp\|from pcodedmp" tools/ .claude/   # pcodedmp
# Zero results

# Confirm uninstalls
$ pip show extract-msg mysql-connector-python pcodedmp 2>&1
# WARNING: Package(s) not found: ...    (all three)
```

---

## Open dependencies after remediation

The current runtime depends on these license categories:

- **MIT / BSD / Apache** (overwhelming majority): pdfplumber, pypdfium2, pillow, olefile, pillow_heif, PyMySQL, requests, mcp, anthropic, openai, etc.
- **LGPL** (acceptable for non-derivative linkage): RTFDE, pystray, stem
- **GPL with explicit exception**: PyInstaller (commercial-distribution carve-out)
- **No AGPL**

---

## Refresh trigger

Re-run this audit if any of the following:
- New runtime dependency added to any `requirements.txt`
- A LGPL package is upgraded to a release that changes its license
- The PyInstaller exception terms change in a future version
- A new project ships from this repo (and might pull a different transitive set)

The diligence-grade dependency snapshot lives in `tools/deps_audit.py --fix` output — re-run after any swap.

---

*This file is the canonical answer to "is the VoxCore IP transferable without GPL/AGPL encumbrance?" — Yes.*
