"""Targeted L2.5 Audit:
1) Extended Trust-Boundary & Kernel-Bypass Primitives (combined attributes, addDeclCore/WithoutChecking, etc.)
2) Full context dump of all `partial_def`, `run_tac`, `liftMetaTactic` hits + command/macro/elab inventory
3) Logical duals: `DEF_CONST_FALSE`, `DEF_FUN_FALSE`, narrow `Set.univ` / `∅` / tautological combinators
4) Parameterized `def`/`abbrev` returning bare numeric literals or dummy witnesses
5) Config-driven Target Symbol Shadowing (`--shadow-config` / `--shadow-target`)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from audit_provenance import collect_provenance
from lean_decl_parser import parse_declarations
from lean_lexer import strip_lean_comments_and_strings
from lean_probes import _extract_explicit_paren_params

_BASE_PREFILTER_KEYWORDS = (
    "skipKernelTC",
    "csimp",
    "trustCompiler",
    "--trust",
    "addDecl",
    "addAndCompile",
    "modifyEnv",
    "setEnv",
    "partial",
    "run_tac",
    "liftMetaTactic",
    "run_cmd",
    "elab",
    "macro",
    "initialize",
    "Lean",
    "sorry",
    "admit",
    "axiom",
    "opaque",
    "native_decide",
    "ofReduceBool",
    "ofReduceNat",
    "implemented_by",
    "extern",
    "unsafe",
    "False",
    "Empty",
    "PEmpty",
    "default",
    "arbitrary",
    "PUnit.unit",
    "Set.univ",
    "∅",
    ":=",
)

_MOD_PREFIX = r"(?m)^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|local|scoped|partial|unsafe)\s+)*"
_EXTENDED_ESCAPE_RE: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("debug_skipKernelTC", re.compile(r"\bdebug\.skipKernelTC\b|\bskipKernelTC\b")),
    ("csimp_attr", re.compile(r"@\[[^\]]*\bcsimp\b[^\]]*\]|\battribute\s+\[[^\]]*\bcsimp\b[^\]]*\]")),
    ("trustCompiler", re.compile(r"\btrustCompiler\b|--trust\b")),
    ("env_addDecl", re.compile(r"\b(?:Lean\.Environment\.|Environment\.)?addDecl(?:Core|WithoutChecking)?\b")),
    ("env_addAndCompile", re.compile(r"\baddAndCompile\b")),
    ("env_modifyEnv", re.compile(r"\bmodifyEnv\b")),
    ("env_setEnv", re.compile(r"\bsetEnv\b")),
    ("sorry", re.compile(r"\bsorry\b")),
    ("admit", re.compile(r"\badmit\b")),
    ("sorryAx", re.compile(r"\bsorryAx\b")),
    ("mkSorry", re.compile(r"\bmkSorry\b")),
    ("native_decide", re.compile(r"\bnative_decide\b")),
    ("ofReduceBool", re.compile(r"\bofReduceBool\b")),
    ("ofReduceNat", re.compile(r"\bofReduceNat\b")),
    ("implemented_by", re.compile(r"\bimplemented_by\b")),
    ("extern_attr", re.compile(r"@\[[^\]]*\bextern\b[^\]]*\]")),
    ("unsafe_kw", re.compile(_MOD_PREFIX + r"\bunsafe\b")),
    ("axiom_decl", re.compile(_MOD_PREFIX + r"\baxiom\b")),
    ("opaque_decl", re.compile(_MOD_PREFIX + r"\bopaque\b")),
)

_DUMP_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "partial_def",
        re.compile(
            r"(?m)^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|local|scoped|unsafe)\s+)*"
            r"\bpartial\s+(?:(?:private|protected|noncomputable|local|scoped|unsafe)\s+)*(?:def|abbrev|instance)\b"
        ),
    ),
    ("run_tac", re.compile(r"\brun_tac\b")),
    ("liftMetaTactic", re.compile(r"\bliftMetaTactic\b")),
)

_META_CMD_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("run_cmd", re.compile(r"(?m)^\s*run_cmd\b")),
    ("elab_decl", re.compile(r"(?m)^\s*(?:local\s+|scoped\s+)?(?:elab_rules|elab)\b")),
    ("macro_decl", re.compile(r"(?m)^\s*(?:local\s+|scoped\s+)?(?:macro_rules|macro)\b")),
    ("initialize_decl", re.compile(r"(?m)^\s*(?:builtin_)?initialize\b")),
    ("import_lean_meta", re.compile(r"(?m)^\s*(?:(?:public|private|meta)\s+)*import\s+(?:all\s+)?Lean(?:\.|\b)")),
)

_DEF_FALSE_WHOLE_RE = re.compile(r"^\s*(?:False|Empty|PEmpty)\s*$")
_DEF_FUN_FALSE_RE = re.compile(r"^\s*(?:fun|λ)\b[\s\S]*?=>\s*(?:False|Empty|PEmpty)\s*$")
_DEF_TAUT_COMB_RE = re.compile(
    r"^\s*(?:(?:fun|λ)\b[^=]*?=>\s*)?(?:Set\.univ|∅|∃\s+[^,]+,\s*True|[^\n]+\s∨\s*True|True\s*∨\s*[^\n]+|False\s*→\s*[^\n]+)\s*$"
)
_DEF_DUMMY_CONST_RE = re.compile(
    r"^\s*(?:-?\d+(?:\.\d+)?|\(\s*-?\d+(?:\.\d+)?\s*:\s*[^)]+\)|Inhabited\.default|default|Classical\.arbitrary(?:\s+[^\s]+)?|PUnit\.unit|⟨\s*⟩)\s*$"
)


def _line_of_offset(txt: str, pos: int) -> int:
    return txt.count("\n", 0, pos) + 1


def _scan_batch(args: tuple[str, list[str], tuple[str, ...]]) -> dict:
    root_str, rel_paths, shadow_targets_tuple = args
    shadow_targets = frozenset(shadow_targets_tuple)
    prefilter_kws = _BASE_PREFILTER_KEYWORDS + shadow_targets_tuple
    root = Path(root_str)

    escape_counts: Counter[str] = Counter()
    escape_hits: list[dict] = []
    dumps: list[dict] = []
    meta_cmd_counts: Counter[str] = Counter()
    meta_cmd_hits: list[dict] = []
    findings: list[dict] = []
    shadow_hits: list[dict] = []

    for rp in rel_paths:
        raw = (root / rp).read_text(encoding="utf-8", errors="replace")
        if not any(kw in raw for kw in prefilter_kws):
            continue

        masked = strip_lean_comments_and_strings(raw)
        raw_lines = raw.splitlines()
        rel_norm = rp.replace("\\", "/")

        for label, pat in _EXTENDED_ESCAPE_RE:
            for m in pat.finditer(masked):
                escape_counts[label] += 1
                if len(escape_hits) < 150:
                    ln = _line_of_offset(masked, m.start())
                    escape_hits.append(
                        {"kind": label, "file": rel_norm, "line": ln, "text": raw_lines[ln - 1].strip()[:180]}
                    )

        for label, pat in _DUMP_PATTERNS:
            for m in pat.finditer(masked):
                ln = _line_of_offset(masked, m.start())
                lo = max(0, ln - 5)
                hi = min(len(raw_lines), ln + 8)
                ctx = "\n".join(f"{idx+1:5d}: {raw_lines[idx]}" for idx in range(lo, hi))
                dumps.append({"kind": label, "file": rel_norm, "line": ln, "context": ctx})

        for label, pat in _META_CMD_PATTERNS:
            for m in pat.finditer(masked):
                meta_cmd_counts[label] += 1
                if len(meta_cmd_hits) < 150:
                    ln = _line_of_offset(masked, m.start())
                    meta_cmd_hits.append(
                        {"kind": label, "file": rel_norm, "line": ln, "text": raw_lines[ln - 1].strip()[:180]}
                    )

        if any(kw in masked for kw in ("def ", "abbrev ", "structure ", "class ", "instance ", "inductive ")):
            decls = parse_declarations(masked)
            for d in decls:
                if d.layer != "definition":
                    continue
                short_name = d.name.rsplit(".", 1)[-1]
                if shadow_targets and short_name in shadow_targets:
                    shadow_hits.append(
                        {
                            "file": rel_norm,
                            "line": d.start_line,
                            "kind": d.kind,
                            "name": d.name,
                            "snippet": " ".join(d.raw_text.splitlines()[:2])[:200],
                        }
                    )

                if d.kind not in ("def", "abbrev"):
                    continue
                body = d.body_text.strip()
                if not body:
                    continue
                snippet = " ".join(d.raw_text.splitlines()[:2])[:180]

                if _DEF_FALSE_WHOLE_RE.match(body):
                    findings.append(
                        {
                            "rule": "DEF_CONST_FALSE",
                            "file": rel_norm,
                            "line": d.start_line,
                            "kind": d.kind,
                            "name": d.name,
                            "snippet": snippet,
                        }
                    )
                elif _DEF_FUN_FALSE_RE.match(body):
                    findings.append(
                        {
                            "rule": "DEF_FUN_FALSE",
                            "file": rel_norm,
                            "line": d.start_line,
                            "kind": d.kind,
                            "name": d.name,
                            "snippet": snippet,
                        }
                    )
                elif _DEF_TAUT_COMB_RE.match(body):
                    findings.append(
                        {
                            "rule": "DEF_TAUTOLOGICAL_OR_UNIV_EMPTY",
                            "file": rel_norm,
                            "line": d.start_line,
                            "kind": d.kind,
                            "name": d.name,
                            "snippet": snippet,
                        }
                    )
                elif _DEF_DUMMY_CONST_RE.match(body):
                    named_p, wild_p = _extract_explicit_paren_params(d.header_text)
                    if len(named_p) + wild_p >= 1:
                        findings.append(
                            {
                                "rule": "DEF_PARAM_DUMMY_CONST_OR_DEFAULT",
                                "file": rel_norm,
                                "line": d.start_line,
                                "kind": d.kind,
                                "name": d.name,
                                "snippet": snippet,
                            }
                        )

    return {
        "escape_counts": dict(escape_counts),
        "escape_hits": escape_hits,
        "dumps": dumps,
        "meta_cmd_counts": dict(meta_cmd_counts),
        "meta_cmd_hits": meta_cmd_hits,
        "findings": findings,
        "shadow_hits": shadow_hits,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Run targeted L2.5 audit")
    ap.add_argument("--root", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--prefix", default="full_l25")
    ap.add_argument("--shadow-config", default="", help="Optional JSON config containing shadow_targets list")
    ap.add_argument("--shadow-target", action="append", default=[], help="Target symbol name for shadowing check (repeatable)")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 4) - 1))
    args = ap.parse_args()

    shadow_targets: list[str] = list(args.shadow_target)
    if args.shadow_config:
        cfg = json.loads(Path(args.shadow_config).read_text(encoding="utf-8"))
        shadow_targets.extend(cfg.get("shadow_targets", []))
    shadow_targets_tuple = tuple(dict.fromkeys(shadow_targets))

    t0 = time.perf_counter()
    root = Path(args.root)
    rel_paths = sorted(str(p.relative_to(root)) for p in root.rglob("*.lean"))

    batch_size = max(100, len(rel_paths) // (args.workers * 4) + 1)
    batches = [(str(root), rel_paths[i : i + batch_size], shadow_targets_tuple) for i in range(0, len(rel_paths), batch_size)]

    escape_counts: Counter[str] = Counter()
    escape_hits: list[dict] = []
    dumps: list[dict] = []
    meta_cmd_counts: Counter[str] = Counter()
    meta_cmd_hits: list[dict] = []
    findings: list[dict] = []
    shadow_hits: list[dict] = []

    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for res in pool.map(_scan_batch, batches):
            for k, v in res["escape_counts"].items():
                escape_counts[k] += v
            escape_hits.extend(res["escape_hits"])
            dumps.extend(res["dumps"])
            for k, v in res["meta_cmd_counts"].items():
                meta_cmd_counts[k] += v
            meta_cmd_hits.extend(res["meta_cmd_hits"])
            findings.extend(res["findings"])
            shadow_hits.extend(res["shadow_hits"])

    finding_counts = Counter(f["rule"] for f in findings)
    by_rule: dict[str, list[dict]] = defaultdict(list)
    for f in findings:
        by_rule[f["rule"]].append(f)

    distinct_meta_partial_locs = len({(x["file"], x["line"]) for x in dumps})
    env_mutation_calls = sum(escape_counts.get(k, 0) for k in ("env_addDecl", "env_addAndCompile", "env_modifyEnv", "env_setEnv"))

    assert sum(finding_counts.values()) == len(findings), "L2.5 finding conservation mismatch"
    assert distinct_meta_partial_locs <= len(dumps), "distinct locations cannot exceed raw hits"
    provenance = collect_provenance(root)
    elapsed = time.perf_counter() - t0
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    full_json = {
        "timing_sec": round(elapsed, 2),
        "provenance": provenance,
        "shadow_targets_configured": list(shadow_targets_tuple),
        "invariants_checked": {"finding_counts_conservation": True, "meta_location_dedup_valid": True},
        "files_scanned": len(rel_paths),
        "escape_counts_all_checked": {k: escape_counts.get(k, 0) for k, _ in _EXTENDED_ESCAPE_RE},
        "escape_hits": escape_hits,
        "meta_and_partial_summary": {
            "raw_primitive_hits": len(dumps),
            "distinct_source_locations": distinct_meta_partial_locs,
            "environment_mutation_calls": env_mutation_calls,
        },
        "meta_and_command_inventory": {k: meta_cmd_counts.get(k, 0) for k, _ in _META_CMD_PATTERNS},
        "meta_and_command_hits": meta_cmd_hits,
        "meta_and_partial_dumps": dumps,
        "l25_finding_counts": dict(finding_counts),
        "l25_findings_by_rule": dict(by_rule),
        "shadow_hits": shadow_hits,
    }
    (out_dir / f"{args.prefix}.json").write_text(json.dumps(full_json, ensure_ascii=False, indent=2), encoding="utf-8")

    dump_md = [
        f"# Meta & Partial Context Dump ({len(dumps)} raw primitive hits / {distinct_meta_partial_locs} distinct locations in {len(rel_paths):,} files)",
        "",
    ]
    for idx, dm in enumerate(sorted(dumps, key=lambda x: (x["kind"], x["file"], x["line"])), 1):
        dump_md.append(f"## {idx}. [{dm['kind']}] `{dm['file']}:{dm['line']}`")
        dump_md.append("```lean")
        dump_md.append(dm["context"])
        dump_md.append("```")
        dump_md.append("")
    (out_dir / f"{args.prefix}_meta_dump.md").write_text("\n".join(dump_md), encoding="utf-8")

    md = [
        f"# Lean 4 Extended Trust-Boundary & Dual-Pattern Audit ({args.prefix})",
        "",
        f"- **Files scanned**: `{len(rel_paths):,}` in `{elapsed:.2f}s` | **Probe SHA256**: `{provenance['probe_bundle_sha256'][:12]}`",
        "",
        "## 1. Extended Trust-Boundary & Kernel-Bypass Primitives",
        "",
        "| Primitive | Count |",
        "|---|---:|",
    ]
    for k, _ in _EXTENDED_ESCAPE_RE:
        md.append(f"| `{k}` | {escape_counts.get(k, 0):,} |")

    md.extend(
        [
            "",
            f"## 2. Metaprogramming & Command Inventory (`{distinct_meta_partial_locs}` distinct `run_tac`/`liftMetaTactic`/`partial` locations = `{len(dumps)}` raw hits; `{env_mutation_calls}` env mutation calls)",
            "",
        ]
    )
    dump_counts = Counter(x["kind"] for x in dumps)
    for k, v in sorted(dump_counts.items()):
        md.append(f"- `{k}`: `{v}`")
    for k, _ in _META_CMD_PATTERNS:
        md.append(f"- `{k}`: `{meta_cmd_counts.get(k, 0)}`")

    md.extend(["", "## 3. Logical Duals, Dummy Witnesses & Shadowing", "", "| Rule | Count |", "|---|---:|"])
    for r, cnt in finding_counts.most_common():
        md.append(f"| `{r}` | {cnt:,} |")
    md.append(f"| `DEF_SYMBOL_SHADOWING` | {len(shadow_hits):,} |")

    for r, items in sorted(by_rule.items()):
        md.extend(["", f"### Samples: `{r}` ({len(items)})", ""])
        for it in items[:25]:
            md.append(f"- `{it['file']}:{it['line']}` (`{it['name']}`): `{it['snippet']}`")

    if shadow_hits:
        md.extend(["", "### Symbol Shadowing Hits", ""])
        for sh in shadow_hits[:30]:
            md.append(f"- `{sh['file']}:{sh['line']}` (`{sh['kind']} {sh['name']}`): `{sh['snippet']}`")

    (out_dir / f"{args.prefix}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"DONE L2.5 in {elapsed:.2f}s -> {out_dir / (args.prefix + '.md')}", flush=True)


if __name__ == "__main__":
    main()
