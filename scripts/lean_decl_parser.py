"""Top-level Lean 4 declaration splitter and Definition vs Proof bucketizer."""

from __future__ import annotations

import re
from dataclasses import dataclass

# Top-level declaration starter at column 0 (with optional modifiers/attributes on same line)
_DECL_START_RE = re.compile(
    r"^(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe|local|scoped)\s+)*"
    r"(def|abbrev|structure|class|instance|inductive|theorem|lemma|axiom|opaque)\b\s*([^\s:({\[⦃]*)?"
)

# Top-level boundary commands that terminate a prior declaration block
_BOUNDARY_RE = re.compile(
    r"^(?:import|open|namespace|section|end|variable|universe|attribute|set_option|#|mutual|"
    r"run_cmd|initialize|example|macro|macro_rules|syntax|declare_syntax_cat|elab|notation|"
    r"infix|prefix|postfix|deriving|omit|include)\b"
)
_ATTR_ONLY_RE = re.compile(r"^(?:@\[[^\]]*\]\s*)+$")

DEF_KINDS = frozenset({"def", "abbrev", "structure", "class", "instance", "inductive"})
PROOF_KINDS = frozenset({"theorem", "lemma"})
AXIOM_KINDS = frozenset({"axiom", "opaque"})


@dataclass(slots=True)
class LeanDecl:
    kind: str          # def, abbrev, structure, theorem, lemma, ...
    layer: str         # "definition" | "proof" | "axiom"
    name: str
    start_line: int    # 1-based
    end_line: int      # 1-based inclusive
    raw_text: str
    header_text: str
    body_text: str
    is_tactic_mode: bool


def _split_header_body(decl_text: str, kind: str) -> tuple[str, str, bool]:
    """Split declaration text into (header, body, is_tactic_mode) tracking bracket depth."""
    if kind in ("structure", "class", "inductive"):
        m_where = re.search(r"\bwhere\b", decl_text)
        if m_where:
            header = decl_text[: m_where.start()]
            body = decl_text[m_where.end() :]
            return header, body, False

    paren = 0
    brace = 0
    bracket = 0
    guil_brace = 0
    i = 0
    n = len(decl_text)
    while i < n:
        ch = decl_text[i]
        if ch == "(":
            paren += 1
        elif ch == ")" and paren > 0:
            paren -= 1
        elif ch == "{":
            brace += 1
        elif ch == "}" and brace > 0:
            brace -= 1
        elif ch == "[":
            bracket += 1
        elif ch == "]" and bracket > 0:
            bracket -= 1
        elif ch == "⦃":
            guil_brace += 1
        elif ch == "⦄" and guil_brace > 0:
            guil_brace -= 1
        elif paren == 0 and brace == 0 and bracket == 0 and guil_brace == 0:
            if ch == ":" and i + 1 < n and decl_text[i + 1] == "=":
                # Ensure not followed by something else, though ':=' is unambiguous at depth 0
                header = decl_text[:i]
                body = decl_text[i + 2 :]
                stripped_body = body.lstrip()
                is_tactic = bool(re.match(r"^by(?:\s|$|·)", stripped_body))
                return header, body, is_tactic
            # `where` at depth 0 for def/instance
            if decl_text[i : i + 5] == "where" and (i == 0 or not decl_text[i - 1].isalnum()) and (
                i + 5 == n or not decl_text[i + 5].isalnum()
            ):
                header = decl_text[:i]
                body = decl_text[i + 5 :]
                return header, body, False
        i += 1

    return decl_text, "", False


def parse_declarations(masked_src: str) -> list[LeanDecl]:
    """Parse top-level declarations from comment/string-masked Lean 4 source."""
    lines = masked_src.splitlines()
    decls: list[LeanDecl] = []

    cur_kind: str | None = None
    cur_name: str = ""
    cur_start: int = 0
    cur_lines: list[str] = []

    def _flush(end_idx_1based: int) -> None:
        nonlocal cur_kind, cur_name, cur_start, cur_lines
        if cur_kind is None:
            return
        raw = "\n".join(cur_lines).rstrip()
        header, body, is_tactic = _split_header_body(raw, cur_kind)
        if cur_kind in DEF_KINDS:
            layer = "definition"
        elif cur_kind in PROOF_KINDS:
            layer = "proof"
        else:
            layer = "axiom"
        decls.append(
            LeanDecl(
                kind=cur_kind,
                layer=layer,
                name=cur_name or "<anonymous>",
                start_line=cur_start,
                end_line=end_idx_1based,
                raw_text=raw,
                header_text=header,
                body_text=body,
                is_tactic_mode=is_tactic,
            )
        )
        cur_kind = None
        cur_name = ""
        cur_lines = []

    pending_attrs: list[str] = []
    for idx, line in enumerate(lines, start=1):
        if line and not line[0].isspace():
            if _ATTR_ONLY_RE.match(line):
                _flush(idx - 1)
                pending_attrs.append(line)
                continue
            m = _DECL_START_RE.match(line)
            if m:
                _flush(idx - 1)
                cur_kind = m.group(1)
                cur_name = m.group(2) or ""
                cur_start = idx - len(pending_attrs) if pending_attrs else idx
                cur_lines = pending_attrs + [line]
                pending_attrs = []
                continue
            if _BOUNDARY_RE.match(line):
                _flush(idx - 1)
                pending_attrs = []
                continue
        if cur_kind is not None:
            cur_lines.append(line)
        elif line.strip():
            pending_attrs = []

    _flush(len(lines))
    return decls
