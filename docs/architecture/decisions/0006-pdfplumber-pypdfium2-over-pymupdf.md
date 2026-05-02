# ADR 0006: pdfplumber + pypdfium2 over PyMuPDF

**Status:** Accepted
**Date:** 2026-05-01 (decision), 2026-05-02 (executed)

## Context

PyMuPDF (`fitz`) is the de facto Python PDF library — mature, fast, supports text extraction, layout analysis, drawing inspection, and page rendering all in one package. VoxCore originally used it across 9 files (8 in `tools/unredact/` plus the `read-any` slash command).

PyMuPDF is licensed **AGPL**. AGPL is GPL with the additional requirement that distribution-via-network counts as distribution — meaning if VoxCore ever serves PDF processing over an API, the AGPL viral provision attaches to the entire surrounding system. Acquirer counsel will flag this immediately and demand either (a) commercial-license purchase (~$500–$2000/year per Artifex) or (b) replacement.

Acquihire-grade IP transfer cannot ship with an AGPL-encumbered hot path.

## Decision

Replace PyMuPDF with a thin compatibility shim (`tools/pdf_lib.py`) backed by:

- **pdfplumber** (MIT) — text extraction, layout, chars, rects, page geometry. Drop-in for `fitz.Page.get_text("text"/"dict"/"words")` and `page.get_drawings()`.
- **pypdfium2** (Apache 2.0) — page rendering to PIL.Image. Drop-in for `fitz.Page.get_pixmap(dpi=N)`.

The shim exposes the subset of fitz APIs VoxCore actually used: `open()`, `Doc.pages`, `len(doc)`, `doc[i]`, `doc.metadata`, `Page.get_text(mode)`, `Page.get_drawings()`, `Page.get_pixmap(dpi)`, `Page.chars`, `Page.lines`, `Page.rects`, `Page.width/height`, `Rect.{x0,y0,x1,y1,width,height}`, plus stubs for `xref_xml_metadata()`, `xref_stream()`, `get_ocgs()`, `layer_ui_configs()`, `annots()`, `get_images()` that degrade gracefully (return safe-empty values).

All 9 consumers updated to `from tools import pdf_lib; pdf_lib.open(path)`. Runtime PyMuPDF dependency dropped from VoxCore code; the system pip-installed `PyMuPDF` may remain for ad-hoc scripts but no VoxCore pipeline invokes it.

## Alternatives considered

1. **Buy a commercial PyMuPDF license.** Artifex offers commercial licensing at ~$500–$2000/year. Rejected: the per-year cost compounds, the swap takes ~one engineering-day, and the resulting code has zero AGPL exposure forever.

2. **Swap to `pypdf` (BSD) only.** pypdf handles text extraction but not layout/rect/render. Insufficient for the unredact pipeline which needs `page.get_drawings()` (filled-rect detection for redaction boxes) and `page.get_pixmap()` (rendering for OCR).

3. **Subprocess isolation** — run PyMuPDF in a subprocess so the AGPL boundary doesn't cross. Legally defensible-but-contested approach used by some commercial products. Rejected: complicates testing, adds latency, doesn't actually eliminate diligence concern.

4. **`unstructured.io`.** Too heavy a dependency for what VoxCore needs. Brings in ~50 transitive packages; some are themselves AGPL-adjacent.

## Consequences

**Positive:**
- Zero AGPL exposure in any VoxCore code path. Diligence answer: clean.
- pdfplumber + pypdfium2 are both actively maintained, MIT/Apache-2.0 licensed.
- Shim layer means future swaps are contained — only `pdf_lib.py` changes if we move backends again.
- Validated on 50/50 random PDFs from the case archive (open + extract clean).

**Negative:**
- pdfplumber's chars/words layout extraction is slightly different from PyMuPDF's. The `box_width.py` font/char-width measurement code needed minor adjustment (uses pdfplumber's `chars`/`extract_words(extra_attrs=...)`).
- pypdfium2 rendering is fast (Apache 2.0, Google Chromium PDFium engine) but produces PNG outputs that look slightly different from PyMuPDF at the pixel level. OCR results agree closely (Tesseract output is robust to small rendering differences); validated on the diagnose pipeline end-to-end.
- pdfplumber doesn't expose XMP / OCG / annotation streams. The diagnose pipeline's relevant code paths now degrade gracefully via shim stubs (return empty/0). Acceptable for the diagnostic use case which already had fallback handling.

**Neutral:**
- Slight per-call overhead from the shim layer. Not measurable in any production benchmark.

## References

- `tools/pdf_lib.py` — the shim
- `docs/acquihire/03_IP_Chain_of_Title/04_Open_Source_Inventory/license_remediation.md` — full Cat 9 record
- ADR 0003 — local-GPU OCR pipeline depends on `pdf_lib.Page.get_pixmap()` rendering
