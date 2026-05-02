"""Minimal Outlook .msg extractor using olefile (BSD-3-Clause).

Drop-in replacement for the extract-msg library (GPL). VoxCore needs only
sender / recipient / date / subject / body / attachment-names from .msg
files. olefile gives us the OLE2 compound-document streams; the rest is
unicode/property decoding.

The Microsoft OLE2 / MAPI .msg format stores each property in a stream
named ``__substg1.0_<propTag>:<typeTag>`` where:
  - propTag is 4 hex chars identifying the property (PR_SUBJECT_W=0037, etc.)
  - typeTag is 4 hex chars identifying the data type
    (001F = unicode string, 001E = ASCII string, 0102 = binary)

References:
  - [MS-OXMSG] specification (Microsoft Open Specifications)
  - [MS-OXPROPS] property tag list

This implementation handles only the headers + body + attachment names.
HTML body, RTF body, and inline-image extraction are out of scope; we
target the same surface extract-msg's basic API exposed.
"""
from __future__ import annotations

import re
from typing import Any

import olefile

# MAPI property tags we care about (top 16 bits of the property tag)
PROPS = {
    "subject":          "0037",
    "body_plain":       "1000",
    "sender_name":      "0C1A",
    "sender_email":     "5D01",
    "sender_addr":      "5D02",
    "to":               "0E04",
    "cc":               "0E03",
    "bcc":              "0E02",
    "client_submit":    "0039",
    "message_delivery": "0E06",
    "display_to":       "0E04",
    "transport_headers": "007D",
}

# Type tags (low 16 bits)
TYPE_UNICODE = "001F"
TYPE_ASCII = "001E"
TYPE_BINARY = "0102"


def _read_stream(ole: olefile.OleFileIO, name_parts: list[str]) -> bytes | None:
    try:
        with ole.openstream(name_parts) as f:
            return f.read()
    except (OSError, KeyError, IOError):
        return None


def _decode(data: bytes, type_tag: str) -> str:
    if data is None:
        return ""
    if type_tag == TYPE_UNICODE:
        try:
            return data.decode("utf-16-le", errors="replace").rstrip("\x00").strip()
        except Exception:
            return ""
    if type_tag == TYPE_ASCII:
        try:
            return data.decode("latin-1", errors="replace").rstrip("\x00").strip()
        except Exception:
            return ""
    return data.decode("utf-8", errors="replace").rstrip("\x00").strip()


def _read_property(ole: olefile.OleFileIO, prop_tag: str,
                    parent: list[str] | None = None) -> str:
    """Read a string-typed property; tries unicode then ascii."""
    base = list(parent or [])
    for type_tag in (TYPE_UNICODE, TYPE_ASCII):
        stream = base + [f"__substg1.0_{prop_tag}{type_tag}"]
        data = _read_stream(ole, stream)
        if data is not None:
            return _decode(data, type_tag)
    return ""


def _list_attachment_dirs(ole: olefile.OleFileIO) -> list[list[str]]:
    out = []
    for entry in ole.listdir():
        if entry and entry[0].startswith("__attach_version1.0_"):
            if [entry[0]] not in out:
                out.append([entry[0]])
    return out


class MsgMessage:
    """Minimal stand-in for extract_msg.Message — same attribute names."""

    def __init__(self, path: str):
        self._path = path
        self._ole = olefile.OleFileIO(path)
        self.subject = _read_property(self._ole, PROPS["subject"])
        self.body = _read_property(self._ole, PROPS["body_plain"])
        sender_name = _read_property(self._ole, PROPS["sender_name"])
        sender_email = _read_property(self._ole, PROPS["sender_email"])
        if sender_name and sender_email:
            self.sender = f"{sender_name} <{sender_email}>"
        else:
            self.sender = sender_name or sender_email or ""
        self.to = _read_property(self._ole, PROPS["display_to"])
        self.date = (
            _read_property(self._ole, PROPS["client_submit"])
            or _read_property(self._ole, PROPS["message_delivery"])
            or ""
        )
        self.attachments = self._collect_attachments()

    def _collect_attachments(self) -> list[Any]:
        out = []
        for adir in _list_attachment_dirs(self._ole):
            long_name = _read_property(self._ole, "3707", parent=adir)
            short_name = _read_property(self._ole, "3704", parent=adir)
            display_name = _read_property(self._ole, "3001", parent=adir)
            name = long_name or display_name or short_name or "(unnamed)"
            out.append(_AttachmentStub(name))
        return out

    def close(self):
        try:
            self._ole.close()
        except Exception:
            pass


class _AttachmentStub:
    __slots__ = ("longFilename",)

    def __init__(self, name: str):
        self.longFilename = name


def Message(path: str) -> MsgMessage:  # noqa: N802 - mirroring extract_msg API
    """Drop-in for ``extract_msg.Message(path)``."""
    return MsgMessage(path)


__all__ = ["Message", "MsgMessage"]
