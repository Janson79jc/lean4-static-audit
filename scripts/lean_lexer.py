"""L1 Lean 4 lexical state-machine comment/string masker.

Preserves exact line numbers (newlines inside block comments or strings are kept)
while safely handling:
  - `--` line comments
  - nested `/- ... -/` block comments & `/-- ... -/` docstrings
  - `"..."` string literals with escapes
  - `«...»` guillemet identifiers (preserving content, blocking comment/string triggers)
  - `'c'` / `'\\x'` char literals WITHOUT swallowing prime identifiers like `x'`, `Q'`, `x''`
"""

from __future__ import annotations

import re

_IMPORT_LINE_RE = re.compile(
    r"^\s*(?:(?:public|private|meta)\s+)*import\s+(?:all\s+)?([^\s]+)"
)
_HEADER_SKIP_RE = re.compile(r"^\s*(?:module|prelude)?\s*$")


def is_ident_char(ch: str) -> bool:
    if not ch:
        return False
    if ch.isalnum() or ch in ("_", "'", "»", "₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"):
        return True
    # Subscripts / superscripts / prime-like Unicode ranges (e.g. ⁺ U+207A)
    o = ord(ch)
    return (0x2070 <= o <= 0x209F) or (0x02B0 <= o <= 0x02FF)


def _match_char_literal(src: str, i: int, n: int) -> int:
    """Return end index (exclusive) if src[i:] is a valid Lean char literal, else -1."""
    if i + 2 >= n or src[i] != "'":
        return -1
    # Never start a char literal immediately after an identifier char (e.g. x', x'', α', x₁', x⁺')
    if i > 0 and is_ident_char(src[i - 1]):
        return -1
    nxt = src[i + 1]
    if nxt == "\n" or nxt == "\r" or nxt == "'":
        return -1
    if nxt == "\\":
        # Escaped char literal: '\n', '\'', '\\', '\xHH', '\uHHHH'
        if i + 3 >= n:
            return -1
        esc = src[i + 2]
        if esc in ("'", '"', "\\", "n", "t", "r", "0"):
            if src[i + 3] == "'":
                return i + 4
            return -1
        if esc == "x" and i + 5 < n and src[i + 5] == "'":
            hex_part = src[i + 3 : i + 5]
            if all(c in "0123456789abcdefABCDEF" for c in hex_part):
                return i + 6
        if esc == "u" and i + 7 < n and src[i + 7] == "'":
            hex_part = src[i + 3 : i + 7]
            if all(c in "0123456789abcdefABCDEF" for c in hex_part):
                return i + 8
        return -1
    # Single unescaped char: 'c'
    if src[i + 2] == "'":
        return i + 3
    return -1


def strip_lean_comments_and_strings(src: str) -> str:
    """Return source with comments and string/char contents replaced by spaces, preserving newlines."""
    out: list[str] = []
    i = 0
    n = len(src)
    block_depth = 0
    in_line_comment = False
    in_string = False
    in_guillemet = False

    while i < n:
        ch = src[i]

        if in_line_comment:
            if ch == "\n":
                in_line_comment = False
                out.append("\n")
            else:
                out.append(" ")
            i += 1
            continue

        if block_depth > 0:
            if ch == "/" and i + 1 < n and src[i + 1] == "-":
                block_depth += 1
                out.append("  ")
                i += 2
                continue
            if ch == "-" and i + 1 < n and src[i + 1] == "/":
                block_depth -= 1
                out.append("  ")
                i += 2
                continue
            out.append("\n" if ch == "\n" else " ")
            i += 1
            continue

        if in_string:
            if ch == "\\" and i + 1 < n:
                nxt = src[i + 1]
                out.append(" ")
                out.append("\n" if nxt == "\n" else " ")
                i += 2
                continue
            if ch == '"':
                in_string = False
                out.append('"')
                i += 1
                continue
            out.append("\n" if ch == "\n" else " ")
            i += 1
            continue

        if in_guillemet:
            out.append(ch)
            if ch == "»":
                in_guillemet = False
            i += 1
            continue

        # Normal code state
        if ch == "-" and i + 1 < n and src[i + 1] == "-":
            in_line_comment = True
            out.append("  ")
            i += 2
            continue
        if ch == "/" and i + 1 < n and src[i + 1] == "-":
            block_depth = 1
            out.append("  ")
            i += 2
            continue
        if ch == '"':
            in_string = True
            out.append('"')
            i += 1
            continue
        if ch == "«":
            in_guillemet = True
            out.append(ch)
            i += 1
            continue
        if ch == "'":
            end = _match_char_literal(src, i, n)
            if end != -1:
                out.append("'" + " " * (end - i - 2) + "'")
                i = end
                continue

        out.append(ch)
        i += 1

    return "".join(out)


def extract_imports(masked_src: str) -> list[str]:
    """Extract imported module names from the header of masked Lean 4.33+ source.

    Stops at the first non-blank, non-`module`/`prelude`, non-`import` line.
    """
    imports: list[str] = []
    for line in masked_src.splitlines():
        m = _IMPORT_LINE_RE.match(line)
        if m:
            imports.append(m.group(1))
            continue
        if _HEADER_SKIP_RE.match(line):
            continue
        break
    return imports
