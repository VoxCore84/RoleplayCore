"""PDF compatibility layer — pdfplumber + pypdfium2 replacement for PyMuPDF.

PyMuPDF (fitz) is AGPL. This shim provides the subset of fitz APIs the VoxCore
codebase actually uses, backed by:
  * pdfplumber (MIT)         — text extraction, layout, rects, chars
  * pypdfium2 (Apache 2.0)   — page rendering to PIL.Image (replaces get_pixmap)

Use this instead of `import fitz` everywhere in the codebase.

API surface:
    pdf_lib.open(path) -> Doc                       (context-managed)
    Doc.pages                                       (list-like)
    Doc[i] -> Page
    len(doc)                                        (page count)
    doc.close()
    doc.metadata -> dict                            (best-effort)
    Page.get_text(mode="text") -> str               (mode: text | dict | words)
    Page.get_drawings() -> list[dict]               (filled rect items only — sufficient for redaction-box detection)
    Page.get_pixmap(dpi=N) -> Pixmap                (Pixmap.tobytes("png") -> bytes)
    Page.rect -> (x0, y0, x1, y1)
    Page.width / Page.height
    Page.chars / Page.lines                         (pdfplumber native passthrough for span work)

Mappings from fitz to this shim:
    fitz.open(p)                  -> pdf_lib.open(p)
    doc[i]                        -> doc[i]
    page.get_text("text")         -> page.get_text("text")
    page.get_text("dict")         -> page.get_text("dict")
    page.get_drawings()           -> page.get_drawings()
    page.get_pixmap(dpi=300)      -> page.get_pixmap(dpi=300)
    pix.tobytes("png")            -> pix.tobytes("png")

What's intentionally NOT supported (none of the VoxCore consumers use these):
    Annotations, form fields, write/save, redaction application, OCG layers,
    embedded files. If you need any of those, expand the shim.
"""
from __future__ import annotations

import io
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable

import pdfplumber
import pypdfium2 as pdfium


class Pixmap:
    """Minimal fitz.Pixmap replacement."""

    def __init__(self, image):
        self._image = image
        self.width = image.width
        self.height = image.height

    def tobytes(self, fmt: str = "png") -> bytes:
        buf = io.BytesIO()
        self._image.save(buf, format=fmt.upper())
        return buf.getvalue()

    @property
    def image(self):
        return self._image


class Page:
    """Wraps a pdfplumber page + its pypdfium2 counterpart for rendering."""

    def __init__(self, plumber_page, pdfium_page):
        self._pp = plumber_page
        self._pf = pdfium_page

    # ---- geometry ----
    @property
    def width(self) -> float:
        return self._pp.width

    @property
    def height(self) -> float:
        return self._pp.height

    @property
    def rect(self) -> tuple[float, float, float, float]:
        return (0.0, 0.0, self._pp.width, self._pp.height)

    # ---- diagnose.py compatibility stubs (return safe-empty values) ----
    def annots(self):
        """Annotations list. Not currently surfaced by pdfplumber. Returns []."""
        return []

    def get_images(self):
        """Image list. pdfplumber exposes ``page.images`` natively."""
        return list(self._pp.images or [])

    # ---- pdfplumber passthrough (chars, lines, words) ----
    @property
    def chars(self) -> list[dict]:
        return list(self._pp.chars or [])

    @property
    def lines(self) -> list[dict]:
        return list(self._pp.lines or [])

    @property
    def rects(self) -> list[dict]:
        return list(self._pp.rects or [])

    # ---- text extraction ----
    def get_text(self, mode: str = "text"):
        if mode in ("text", "", None):
            return self._pp.extract_text() or ""
        if mode == "words":
            return self._pp.extract_words() or []
        if mode == "dict":
            return self._dict_layout()
        if mode == "blocks":
            return self._dict_layout()["blocks"]
        if mode == "html":
            text = self._pp.extract_text() or ""
            return f"<html><body><pre>{text}</pre></body></html>"
        # fallback to plain text
        return self._pp.extract_text() or ""

    def _dict_layout(self) -> dict:
        """Approximate fitz dict format from pdfplumber chars/words.

        Returns {"width","height","blocks":[{"lines":[{"spans":[{"text","font","size","bbox"}]}]}]}.
        """
        words = self._pp.extract_words(extra_attrs=["fontname", "size"]) or []
        # group by approximate y0 line
        lines_by_y: dict[int, list[dict]] = {}
        for w in words:
            y_key = round(w.get("top", 0), 0)
            spans = lines_by_y.setdefault(y_key, [])
            spans.append({
                "text": w.get("text", ""),
                "font": w.get("fontname") or "",
                "size": float(w.get("size") or 0.0),
                "bbox": (
                    float(w.get("x0", 0)),
                    float(w.get("top", 0)),
                    float(w.get("x1", 0)),
                    float(w.get("bottom", 0)),
                ),
            })
        lines: list[dict] = []
        for y in sorted(lines_by_y):
            spans = lines_by_y[y]
            lines.append({
                "spans": spans,
                "bbox": (
                    min(s["bbox"][0] for s in spans),
                    y,
                    max(s["bbox"][2] for s in spans),
                    max(s["bbox"][3] for s in spans),
                ),
            })
        return {
            "width": self._pp.width,
            "height": self._pp.height,
            "blocks": [{"type": 0, "lines": lines, "bbox": (0, 0, self._pp.width, self._pp.height)}],
        }

    # ---- drawings (filled rects, used for redaction-box detection) ----
    def get_drawings(self) -> list[dict]:
        """Return drawings in a fitz-compatible shape.

        The unredact pipeline only inspects filled rectangles and reads
        ``d.get("type")`` (expects "f"/"fs"), ``d.get("fill")`` (RGB tuple),
        and ``d.get("items")`` (list of ("re", Rect, ...)).

        We synthesize that from pdfplumber's ``page.rects``, which gives us
        x0/y0/x1/y1 + non_stroking_color (fill) for filled rectangles.
        """
        out: list[dict] = []
        for r in (self._pp.rects or []):
            fill = r.get("non_stroking_color")
            if fill is None:
                fill = (0.0, 0.0, 0.0)
            elif isinstance(fill, (int, float)):
                fill = (float(fill), float(fill), float(fill))
            elif isinstance(fill, (list, tuple)):
                if len(fill) == 1:
                    fill = (float(fill[0]),) * 3
                elif len(fill) == 3:
                    fill = tuple(float(c) for c in fill)
                elif len(fill) == 4:
                    # CMYK -> approx grayscale -> RGB
                    c, m, y, k = (float(v) for v in fill)
                    g = 1.0 - min(1.0, c + m + y + k)
                    fill = (g, g, g)
            x0, y0, x1, y1 = (
                float(r.get("x0", 0)),
                float(r.get("y0", 0)),
                float(r.get("x1", 0)),
                float(r.get("y1", 0)),
            )
            rect = Rect(x0, y0, x1, y1)
            out.append({
                "type": "f",
                "fill": fill,
                "items": [("re", rect)],
                "rect": rect,
            })
        return out

    # ---- rendering (replaces get_pixmap) ----
    def get_pixmap(self, dpi: int = 150) -> Pixmap:
        scale = dpi / 72.0
        bitmap = self._pf.render(scale=scale)
        image = bitmap.to_pil()
        return Pixmap(image)


class Rect:
    """Minimal fitz.Rect replacement — exposes x0/y0/x1/y1 + width/height."""

    __slots__ = ("x0", "y0", "x1", "y1")

    def __init__(self, x0: float, y0: float, x1: float, y1: float):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    @property
    def width(self) -> float:
        return self.x1 - self.x0

    @property
    def height(self) -> float:
        return self.y1 - self.y0

    def __iter__(self):
        return iter((self.x0, self.y0, self.x1, self.y1))

    def __repr__(self) -> str:
        return f"Rect({self.x0!r}, {self.y0!r}, {self.x1!r}, {self.y1!r})"


class Doc:
    """Document handle. Wraps a pdfplumber.PDF and a pypdfium2.PdfDocument."""

    def __init__(self, path: str | Path):
        self._path = str(path)
        self._plumber = pdfplumber.open(self._path)
        self._pdfium = pdfium.PdfDocument(self._path)
        self._closed = False

    @property
    def metadata(self) -> dict:
        try:
            return dict(self._plumber.metadata or {})
        except Exception:
            return {}

    # ---- diagnose.py compatibility stubs ----
    def xref_xml_metadata(self) -> int:
        """fitz returns the xref of the XMP stream, or 0 if absent. Stub: 0."""
        return 0

    def xref_stream(self, xref: int) -> bytes:  # noqa: ARG002
        """No-op — pdfplumber doesn't expose xref streams."""
        return b""

    def get_ocgs(self) -> dict:
        """Optional Content Groups. Not exposed by pdfplumber. Returns {}."""
        return {}

    def layer_ui_configs(self) -> list:
        """Layer UI configs. Not exposed by pdfplumber. Returns []."""
        return []

    @property
    def pages(self) -> list[Page]:
        return [self[i] for i in range(len(self))]

    def __len__(self) -> int:
        return len(self._plumber.pages)

    def __getitem__(self, idx) -> Page:
        if isinstance(idx, slice):
            return [self[i] for i in range(*idx.indices(len(self)))]
        if idx < 0:
            idx += len(self)
        return Page(self._plumber.pages[idx], self._pdfium[idx])

    def __iter__(self) -> Iterable[Page]:
        for i in range(len(self)):
            yield self[i]

    def close(self) -> None:
        if self._closed:
            return
        try:
            self._plumber.close()
        except Exception:
            pass
        try:
            self._pdfium.close()
        except Exception:
            pass
        self._closed = True

    def __enter__(self) -> "Doc":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


def open(path: str | Path) -> Doc:  # noqa: A001 - mirroring fitz.open
    """Open a PDF. Use as a context manager or call .close() yourself."""
    return Doc(path)


# Convenience alias mirroring fitz module-level Rect
__all__ = ["open", "Doc", "Page", "Pixmap", "Rect"]
