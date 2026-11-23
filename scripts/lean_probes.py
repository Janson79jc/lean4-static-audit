"""L2 Static Pattern Probes for Lean 4: Definition vs Proof separation, Term-mode param checks,
vacuous predicates, trust-boundary primitives, Exact & Type-2 parameterized clone hashing.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from lean_decl_parser import LeanDecl, parse_declarations
from lean_lexer import extract_imports, is_ident_char, strip_lean_comments_and_strings

_TOKEN_RE = re.compile(r"[^\W\d_][\w.'«»₀-₉⁺⁻]*|[0-9]+|:=|=>|↔|→|∀|∃|∧|∨|¬|≤|≥|≠|[^\s]")

# Lean keywords, core tactics, and standard operators preserved during Type-2 identifier normalization
_LEAN_KEEP_TOKENS = frozenset(
    {
        "fun",
        "λ",
        "let",
        "in",
        "have",
        "show",
        "if",
        "then",
        "else",
        "match",
        "with",
        "by",
        "do",
        "return",
        "where",
        "for",
        "unless",
        "True",
        "False",
        "Prop",
        "Type",
        "Sort",
        "Nat",
        "Int",
        "Real",
        "Complex",
        "PUnit",
        "Unit",
        "trivial",
        "True.intro",
        "PUnit.unit",
        "rfl",
        "simp",
        "simp_all",
        "only",
        "dsimp",
        "field_simp",
        "exact",
        "apply",
        "intro",
        "intros",
        "rintro",
        "refine",
        "rw",
        "erw",
        "change",
        "unfold",
        "ext",
        "rcases",
        "obtain",
        "cases",
        "induction",
        "constructor",
        "use",
        "exists",
        "left",
        "right",
        "split",
        "congr",
        "funext",
        "ring",
        "norm_num",
        "positivity",
        "gcongr",
        "linarith",
        "nlinarith",
        "omega",
        "aesop",
        "decide",
        "by_cases",
        "by_contra",
        "assumption",
        "push_cast",
        "norm_cast",
        "mod_cast",
        "exact_mod_cast",
        "subst",
        "symm",
        "trans",
        "calc",
        "clear",
        "rename_i",
        "revert",
        "generalize",
        "specialize",
        "contrapose",
        "push_neg",
        "exfalso",
        "contradiction",
        "absurd",
        "tauto",
        "abel",
        "group",
        "noncomm_ring",
        "continuity",
        "measurability",
        "fun_prop",
        "first",
        "all_goals",
        "any_goals",
        "repeat",
        "try",
        "done",
        "skip",
        "run_tac",
        "liftMetaTactic",
        "revertAll",
        "infer_instance",
        "sorry",
        "admit",
    }
)

_DEF_FUN_TRUE_WHOLE_RE = re.compile(r"^\s*(?:fun|λ)\b([\s\S]*?)=>\s*True\s*$")
_INLINE_WILDCARD_FUN_TRUE_RE = re.compile(r"(?:fun|λ)\s+((?:_\s+)+)=>\s*True\b")
_DEF_CONST_TRUE_RE = re.compile(r"^\s*True\s*$")
_DEF_TRIVIAL_STUB_RE = re.compile(r"^\s*(?:by\s+trivial|True\.intro|PUnit\.unit|default|⟨\s*⟩)\s*$")
_THM_BY_TRIVIAL_RE = re.compile(r"^\s*by\s+trivial\s*$")
_THM_RFL_RE = re.compile(r"^\s*(?:rfl|by\s+rfl)\s*$")
_HAS_BY_TACTIC_RE = re.compile(r"(?:^|[\s(])by(?:\s|$|·)")
_SHIM_NON_FORWARD_RE = re.compile(
    r"(?<![.\w])(?:have|let|rw|erw|simp|dsimp|ring|omega|linarith|aesop|calc|induction|cases|obtain|rcases|constructor|ext)(?![.\w'])"
)
_SHIM_FORWARD_HEAD_RE = re.compile(r"^\s*(?:by\s+)?(?:first\s*\||exact\s+)")

_MOD_PREFIX = r"(?m)^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|local|scoped|partial|unsafe)\s+)*"
_ESCAPE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("sorry", re.compile(r"\bsorry\b")),
    ("admit", re.compile(r"\badmit\b")),
    ("sorryAx", re.compile(r"\bsorryAx\b")),
    ("mkSorry", re.compile(r"\bmkSorry\b")),
    ("native_decide", re.compile(r"\bnative_decide\b")),
    ("ofReduceBool", re.compile(r"\bofReduceBool\b")),
    ("ofReduceNat", re.compile(r"\bofReduceNat\b")),
    ("implemented_by", re.compile(r"\bimplemented_by\b")),
    ("extern_attr", re.compile(r"@\[[^\]]*\bextern\b[^\]]*\]")),
    ("csimp_attr", re.compile(r"@\[[^\]]*\bcsimp\b[^\]]*\]|\battribute\s+\[[^\]]*\bcsimp\b[^\]]*\]")),
    ("unsafe_kw", re.compile(_MOD_PREFIX + r"\bunsafe\b")),
    (
        "partial_def",
        re.compile(
            r"(?m)^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|local|scoped|unsafe)\s+)*"
            r"\bpartial\s+(?:(?:private|protected|noncomputable|local|scoped|unsafe)\s+)*(?:def|abbrev|instance)\b"
        ),
    ),
    ("axiom_decl", re.compile(_MOD_PREFIX + r"\baxiom\b")),
    ("opaque_decl", re.compile(_MOD_PREFIX + r"\bopaque\b")),
)

_META_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("run_tac", re.compile(r"\brun_tac\b")),
    ("liftMetaTactic", re.compile(r"\bliftMetaTactic\b")),
)


@dataclass(slots=True)
class Finding:
    rule: str
    file: str
    line: int
    decl_kind: str
    decl_name: str
    detail: str
    snippet: str


@dataclass(slots=True)
class DeclHashRecord:
    layer: str
    is_shim: bool
    exact_hash: str
    type2_hash: str
    token_count: int
    file: str
    line: int
    name: str


@dataclass(slots=True)
class FileAuditResult:
    rel_path: str
    top_module: str
    dir_depth: int
    raw_lines: int
    code_lines: int
    import_count: int
    imports: list[str]
    def_count: int
    thm_count: int
    thm_by_trivial: int
    thm_rfl: int
    findings: list[Finding] = field(default_factory=list)
    thm_info_hits: list[Finding] = field(default_factory=list)
    escape_counts: dict[str, int] = field(default_factory=dict)
    meta_counts: dict[str, int] = field(default_factory=dict)
    clone_records: list[DeclHashRecord] = field(default_factory=list)


def _extract_explicit_paren_params(header_text: str) -> tuple[list[tuple[str, int]], int]:
    """Return ([(name, rest_start_idx)], explicit_wildcard_count) from top-level `(...)` groups.

    Strictly skips `{...}` implicit binders, `⦃...⦄` strict implicit binders, `[...]` instance binders,
    and anything after the top-level return type colon `:`.
    """
    named: list[tuple[str, int]] = []
    wildcards = 0
    i = 0
    n = len(header_text)

    m = re.match(
        r"^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|partial|unsafe|local|scoped)\s+)*"
        r"(?:def|abbrev|structure|class|instance|inductive)\s+(?:[^\s:({\[⦃]+)?",
        header_text,
    )
    if m:
        i = m.end()

    while i < n:
        ch = header_text[i]
        if ch.isspace():
            i += 1
            continue
        if ch == ":":
            break
        if ch in "{[⦃":
            close = {"{": "}", "[": "]", "⦃": "⦄"}[ch]
            depth = 1
            i += 1
            while i < n and depth > 0:
                if header_text[i] == ch:
                    depth += 1
                elif header_text[i] == close:
                    depth -= 1
                i += 1
            continue
        if ch == "(":
            depth = 1
            start = i + 1
            i += 1
            while i < n and depth > 0:
                if header_text[i] == "(":
                    depth += 1
                elif header_text[i] == ")":
                    depth -= 1
                i += 1
            inner = header_text[start : i - 1]
            if ":" in inner:
                lhs = inner.split(":", 1)[0].strip()
                for tok in lhs.split():
                    if tok == "_":
                        wildcards += 1
                    elif tok and (tok[0].isalpha() or tok[0] in ("_", "«")) and all(is_ident_char(c) for c in tok):
                        named.append((tok, i))
            continue
        i += 1

    return named, wildcards


def _compute_body_hashes(body_text: str) -> tuple[str, str, int]:
    """Compute (exact_token_hash, type2_parameterized_ident_hash, token_count)."""
    tokens = _TOKEN_RE.findall(body_text)
    if len(tokens) < 8:
        return "", "", len(tokens)
    exact_str = " ".join(tokens)
    exact_hash = hashlib.sha256(exact_str.encode("utf-8")).hexdigest()[:16]

    ident_map: dict[str, str] = {}
    type2_tokens: list[str] = []
    for tok in tokens:
        if tok in _LEAN_KEEP_TOKENS or not (tok[0].isalpha() or tok[0] in "_«"):
            type2_tokens.append(tok)
        else:
            mapped = ident_map.get(tok)
            if mapped is None:
                mapped = f"V{len(ident_map)}"
                ident_map[tok] = mapped
            type2_tokens.append(mapped)
    type2_hash = hashlib.sha256(" ".join(type2_tokens).encode("utf-8")).hexdigest()[:16]
    return exact_hash, type2_hash, len(tokens)


_POSTFIX_MATH_OPS = frozenset("⁻⁺ᵀᴴᗮᶜ⊥⊤")


def _is_ident_boundary_char(ch: str) -> bool:
    """Identifier char check for symbol usage boundary: excludes postfix math operators (⁻, ⁺, ᵀ, ᴴ, ᗮ, ᶜ)."""
    if not ch or ch in _POSTFIX_MATH_OPS:
        return False
    return is_ident_char(ch)


def _ident_used_in_body(name: str, text: str) -> bool:
    """Unicode-safe whole-identifier search (supports α', x₁', and postfix ops g⁻¹, Aᵀ, Wᗮ, Sᶜ)."""
    n = len(text)
    m = len(name)
    start = 0
    while True:
        idx = text.find(name, start)
        if idx == -1:
            return False
        left_ok = idx == 0 or not _is_ident_boundary_char(text[idx - 1])
        right_idx = idx + m
        right_ok = right_idx == n or not _is_ident_boundary_char(text[right_idx])
        if left_ok and right_ok:
            return True
        start = idx + 1


def _mask_paren_by_blocks(line: str) -> str:
    """Mask balanced `(by ...)` parenthesized tactic proofs even with nested parentheses."""
    out = list(line)
    i = 0
    n = len(line)
    while i < n:
        if line[i] == "(":
            j = i + 1
            while j < n and line[j].isspace():
                j += 1
            if line[j : j + 2] == "by" and (j + 2 == n or line[j + 2].isspace() or line[j + 2] == "·"):
                depth = 1
                k = i + 1
                while k < n and depth > 0:
                    if line[k] == "(":
                        depth += 1
                    elif line[k] == ")":
                        depth -= 1
                    k += 1
                if depth == 0:
                    for pos in range(i + 1, k - 1):
                        out[pos] = " "
                    i = k
                    continue
        i += 1
    return "".join(out)


def _strip_by_subblocks(raw_body_text: str) -> str:
    """Mask out `by <tactic block>` proof obligations inside unstripped `d.body_text`.

    Tracks actual line indentation (capturing the first indented tactic-body line when
    `by` appears on line 0) and masks balanced `(by ...)` inline tactic expressions.
    """
    if re.match(r"^\s*by(?:\s|$|·)", raw_body_text):
        return ""

    lines = raw_body_text.splitlines(keepends=True)
    out: list[str] = []
    # None = not in `by` block; -1 = waiting for first tactic line after `by`; >=0 = minimum indent inside `by`
    by_body_min_indent: int | None = None
    by_trigger_indent: int = 0
    by_had_inline_tac: bool = False

    for ln in lines:
        stripped = ln.lstrip()
        indent = len(ln) - len(stripped)

        if by_body_min_indent is not None:
            if not stripped:
                out.append(ln)
                continue
            if by_body_min_indent == -1:
                if indent > by_trigger_indent and not (
                    by_had_inline_tac and re.match(r"^(?:[^\W\d_][\w.'«»₀-₉]*)\s*:=", stripped)
                ):
                    by_body_min_indent = indent
                    out.append(" " * len(ln.rstrip("\r\n")) + ("\n" if ln.endswith("\n") else ""))
                    continue
                by_body_min_indent = None
            elif indent >= by_body_min_indent:
                out.append(" " * len(ln.rstrip("\r\n")) + ("\n" if ln.endswith("\n") else ""))
                continue
            else:
                by_body_min_indent = None

        cleaned = _mask_paren_by_blocks(ln)
        m_by = re.search(r"(?:^|[\s(])by(?:\s|$|·)", cleaned)
        if m_by:
            by_pos = m_by.start()
            after_by = cleaned[m_by.end() :].strip()
            prefix = cleaned[:by_pos]
            out.append(prefix + (" " * (len(cleaned.rstrip("\r\n")) - len(prefix))) + ("\n" if ln.endswith("\n") else ""))
            by_body_min_indent = -1
            by_trigger_indent = indent
            by_had_inline_tac = bool(after_by)
            continue
        out.append(cleaned)

    return "".join(out)


def _is_forwarding_shim(body: str) -> bool:
    if not _SHIM_FORWARD_HEAD_RE.match(body):
        return False
    if _SHIM_NON_FORWARD_RE.search(body):
        return False
    return True


def audit_lean_source(rel_path: str, raw_src: str) -> FileAuditResult:
    masked = strip_lean_comments_and_strings(raw_src)
    imports = extract_imports(masked)
    raw_lines = raw_src.count("\n") + (1 if raw_src and not raw_src.endswith("\n") else 0)
    code_lines = sum(1 for ln in masked.splitlines() if ln.strip())

    parts = rel_path.replace("\\", "/").split("/")
    top_module = parts[0] if len(parts) > 1 else "(root)"
    dir_depth = max(0, len(parts) - 1)

    decls: list[LeanDecl] = parse_declarations(masked)

    res = FileAuditResult(
        rel_path=rel_path.replace("\\", "/"),
        top_module=top_module,
        dir_depth=dir_depth,
        raw_lines=raw_lines,
        code_lines=code_lines,
        import_count=len(imports),
        imports=imports,
        def_count=0,
        thm_count=0,
        thm_by_trivial=0,
        thm_rfl=0,
    )

    for label, pat in _ESCAPE_PATTERNS:
        c = len(pat.findall(masked))
        if c:
            res.escape_counts[label] = c
    for label, pat in _META_PATTERNS:
        c = len(pat.findall(masked))
        if c:
            res.meta_counts[label] = c

    for d in decls:
        snippet = " ".join(d.raw_text.splitlines()[:2])[:180]
        if d.layer == "definition":
            res.def_count += 1
            body = d.body_text.strip()

            # Probe 1: Vacuous predicate / constant True in def/abbrev/instance (excluding `by` proof subblocks)
            if d.kind in ("def", "abbrev", "instance") and body:
                term_body = _strip_by_subblocks(d.body_text).strip()
                m_whole = _DEF_FUN_TRUE_WHOLE_RE.match(term_body)
                if m_whole:
                    arg_count = len(m_whole.group(1).strip().split())
                    res.findings.append(
                        Finding(
                            "DEF_FUN_TRUE",
                            res.rel_path,
                            d.start_line,
                            d.kind,
                            d.name,
                            f"Definition body reduces directly to `fun ... => True` ({arg_count} arg(s))",
                            snippet,
                        )
                    )
                else:
                    inline_matches = _INLINE_WILDCARD_FUN_TRUE_RE.findall(term_body)
                    if inline_matches:
                        max_wild = max(m.split().count("_") for m in inline_matches)
                        rule_name = "DEF_MULTIARG_FUN_TRUE" if max_wild >= 2 else "DEF_SINGLEARG_FUN_TRUE"
                        res.findings.append(
                            Finding(
                                rule_name,
                                res.rel_path,
                                d.start_line,
                                d.kind,
                                d.name,
                                f"Definition passes inline `fun {'_ ' * max_wild}=> True` ({max_wild} wildcard arg(s))",
                                snippet,
                            )
                        )
                    elif _DEF_CONST_TRUE_RE.match(term_body):
                        res.findings.append(
                            Finding(
                                "DEF_CONST_TRUE",
                                res.rel_path,
                                d.start_line,
                                d.kind,
                                d.name,
                                "Definition body is constant `True`",
                                snippet,
                            )
                        )
                    elif _DEF_TRIVIAL_STUB_RE.match(body) and d.kind in ("def", "abbrev"):
                        res.findings.append(
                            Finding(
                                "DEF_TRIVIAL_STUB",
                                res.rel_path,
                                d.start_line,
                                d.kind,
                                d.name,
                                "Definition body is a trivial/unit/default stub",
                                snippet,
                            )
                        )

            # Probe 2: Ignored explicit params ONLY in pure Term-mode def/abbrev (no `by`, including inline `(by ...)`)
            if (
                d.kind in ("def", "abbrev")
                and body
                and not d.is_tactic_mode
                and not _HAS_BY_TACTIC_RE.search(body)
            ):
                named_params, wildcard_cnt = _extract_explicit_paren_params(d.header_text)
                if wildcard_cnt > 0:
                    res.findings.append(
                        Finding(
                            "DEF_EXPLICIT_WILDCARD_PARAM",
                            res.rel_path,
                            d.start_line,
                            d.kind,
                            d.name,
                            f"{wildcard_cnt} explicit `(_ : T)` wildcard param(s) in pure term-mode {d.kind}",
                            snippet,
                        )
                    )
                unused = [
                    p
                    for p, rest_idx in named_params
                    if not _ident_used_in_body(p, body)
                    and not _ident_used_in_body(p, d.header_text[rest_idx:])
                ]
                if unused:
                    underscored = [p for p in unused if p.startswith("_")]
                    unprefixed = [p for p in unused if not p.startswith("_")]
                    if underscored:
                        res.findings.append(
                            Finding(
                                "DEF_UNUSED_EXPLICIT_UNDERSCORE_PARAM",
                                res.rel_path,
                                d.start_line,
                                d.kind,
                                d.name,
                                f"Unused `_`-prefixed explicit param(s): {', '.join(underscored)}",
                                snippet,
                            )
                        )
                    if unprefixed:
                        res.findings.append(
                            Finding(
                                "DEF_UNUSED_EXPLICIT_NAMED_PARAM",
                                res.rel_path,
                                d.start_line,
                                d.kind,
                                d.name,
                                f"Unused unprefixed explicit param(s) (absent in body, return type, and no `by` tactic): {', '.join(unprefixed)}",
                                snippet,
                            )
                        )

            # Clone hashing for definitions >= 8 tokens
            if d.kind in ("def", "abbrev") and body:
                eh, th, tcnt = _compute_body_hashes(body)
                if eh:
                    res.clone_records.append(
                        DeclHashRecord("definition", False, eh, th, tcnt, res.rel_path, d.start_line, d.name)
                    )

        elif d.layer == "proof":
            res.thm_count += 1
            body = d.body_text.strip()
            if _THM_BY_TRIVIAL_RE.match(body):
                res.thm_by_trivial += 1
            elif _THM_RFL_RE.match(body):
                res.thm_rfl += 1

            # Informational only: theorem statement header passes `fun _+ => True`
            if _INLINE_WILDCARD_FUN_TRUE_RE.search(d.header_text):
                res.thm_info_hits.append(
                    Finding(
                        "THM_STMT_FUN_TRUE",
                        res.rel_path,
                        d.start_line,
                        d.kind,
                        d.name,
                        "Theorem/lemma statement passes `fun _+ => True` (review separately from def)",
                        snippet,
                    )
                )

            if body:
                eh, th, tcnt = _compute_body_hashes(body)
                if eh:
                    is_shim = _is_forwarding_shim(body)
                    res.clone_records.append(
                        DeclHashRecord("proof", is_shim, eh, th, tcnt, res.rel_path, d.start_line, d.name)
                    )

    return res
