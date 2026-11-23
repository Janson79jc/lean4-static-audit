"""Multi-process L1+L2 static audit runner for Lean 4 corpora."""

from __future__ import annotations

import argparse
import json
import os
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from audit_provenance import collect_provenance, sanitize_root_label
from lean_probes import FileAuditResult, audit_lean_source


def _process_batch(args: tuple[str, list[str]]) -> list[FileAuditResult]:
    root_str, rel_paths = args
    root = Path(root_str)
    out: list[FileAuditResult] = []
    for rp in rel_paths:
        raw = (root / rp).read_text(encoding="utf-8", errors="replace")
        out.append(audit_lean_source(rp, raw))
    return out


def _bucket_lines(n: int) -> str:
    if n < 50:
        return "01_<50_lines"
    if n < 200:
        return "02_50-199_lines"
    if n < 500:
        return "03_200-499_lines"
    return "04_500+_lines"


def _bucket_imports(n: int) -> str:
    if n <= 3:
        return "01_1-3_imports"
    if n <= 8:
        return "02_4-8_imports"
    if n <= 15:
        return "03_9-15_imports"
    return "04_16+_imports"


def main() -> None:
    ap = argparse.ArgumentParser(description="Run Lean 4 L1+L2 static audit")
    ap.add_argument("--root", required=True, help="Root src directory containing .lean files")
    ap.add_argument("--out-dir", required=True, help="Directory for markdown and json reports")
    ap.add_argument("--prefix", default="pilot", help="Report filename prefix")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 4) - 1))
    args = ap.parse_args()

    t0 = time.perf_counter()
    root = Path(args.root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    rel_paths = sorted(str(p.relative_to(root)) for p in root.rglob("*.lean"))
    t_glob = time.perf_counter()

    batch_size = max(50, len(rel_paths) // (args.workers * 4) + 1)
    batches = [(str(root), rel_paths[i : i + batch_size]) for i in range(0, len(rel_paths), batch_size)]

    results: list[FileAuditResult] = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for batch_res in pool.map(_process_batch, batches):
            results.extend(batch_res)
    t_scan = time.perf_counter()

    total_raw_lines = 0
    total_code_lines = 0
    total_defs = 0
    total_thms = 0
    total_thm_trivial = 0
    total_thm_rfl = 0

    rule_counts: Counter[str] = Counter()
    findings_by_rule: dict[str, list[dict]] = defaultdict(list)
    thm_info_hits: list[dict] = []
    escape_totals: Counter[str] = Counter()
    meta_totals: Counter[str] = Counter()

    by_module: dict[str, Counter] = defaultdict(Counter)
    by_line_bucket: dict[str, Counter] = defaultdict(Counter)
    by_import_bucket: dict[str, Counter] = defaultdict(Counter)

    # Clone tracking: (layer, hash) -> list[(file, line, name)]
    exact_clones: dict[tuple[str, str], list[tuple[str, int, str]]] = defaultdict(list)
    type2_clones: dict[tuple[str, str], list[tuple[str, int, str]]] = defaultdict(list)
    type2_short_clones: dict[tuple[str, str], list[tuple[str, int, str]]] = defaultdict(list)
    type2_ge20_clones: dict[tuple[str, str], list[tuple[str, int, str]]] = defaultdict(list)
    decl_totals_by_layer: Counter[str] = Counter()
    decl_totals_short: Counter[str] = Counter()
    decl_totals_ge20: Counter[str] = Counter()

    all_findings_compact: list[dict] = []
    module_index: dict[str, dict] = {}

    for r in results:
        total_raw_lines += r.raw_lines
        total_code_lines += r.code_lines
        total_defs += r.def_count
        total_thms += r.thm_count
        total_thm_trivial += r.thm_by_trivial
        total_thm_rfl += r.thm_rfl

        mod_name = r.rel_path[:-5].replace("/", ".") if r.rel_path.endswith(".lean") else r.rel_path.replace("/", ".")
        module_index[mod_name] = {
            "file": r.rel_path,
            "code_lines": r.code_lines,
            "raw_lines": r.raw_lines,
            "imports": r.imports,
            "defs": r.def_count,
            "thms": r.thm_count,
        }

        for k, v in r.escape_counts.items():
            escape_totals[k] += v
        for k, v in r.meta_counts.items():
            meta_totals[k] += v

        def_hits_in_file = len(r.findings)
        for f in r.findings:
            rule_counts[f.rule] += 1
            f_dict = {
                "rule": f.rule,
                "file": f.file,
                "module": mod_name,
                "line": f.line,
                "kind": f.decl_kind,
                "name": f.decl_name,
                "detail": f.detail,
                "snippet": f.snippet,
            }
            all_findings_compact.append(f_dict)
            if len(findings_by_rule[f.rule]) < 150:
                findings_by_rule[f.rule].append(f_dict)
        for f in r.thm_info_hits:
            if len(thm_info_hits) < 100:
                thm_info_hits.append(
                    {
                        "rule": f.rule,
                        "file": f.file,
                        "line": f.line,
                        "kind": f.decl_kind,
                        "name": f.decl_name,
                        "detail": f.detail,
                        "snippet": f.snippet,
                    }
                )

        for bucket_map, bkey in (
            (by_module, r.top_module),
            (by_line_bucket, _bucket_lines(r.code_lines)),
            (by_import_bucket, _bucket_imports(r.import_count)),
        ):
            c = bucket_map[bkey]
            c["files"] += 1
            c["code_lines"] += r.code_lines
            c["defs"] += r.def_count
            c["thms"] += r.thm_count
            c["findings"] += def_hits_in_file

        for cr in r.clone_records:
            layer_buckets = [cr.layer]
            if cr.layer == "proof":
                layer_buckets.append("proof_shim" if cr.is_shim else "proof_substantive")
            for lb in layer_buckets:
                decl_totals_by_layer[lb] += 1
                exact_clones[(lb, cr.exact_hash)].append((cr.file, cr.line, cr.name))
                type2_clones[(lb, cr.type2_hash)].append((cr.file, cr.line, cr.name))
                if cr.token_count < 20:
                    decl_totals_short[lb] += 1
                    type2_short_clones[(lb, cr.type2_hash)].append((cr.file, cr.line, cr.name))
                else:
                    decl_totals_ge20[lb] += 1
                    type2_ge20_clones[(lb, cr.type2_hash)].append((cr.file, cr.line, cr.name))

    def _clone_stats(
        clone_map: dict[tuple[str, str], list[tuple[str, int, str]]],
        totals_counter: Counter[str],
    ) -> dict[str, dict]:
        stats: dict[str, dict] = {}
        for layer in ("definition", "proof", "proof_shim", "proof_substantive"):
            total_eligible = totals_counter[layer]
            dup_instances = 0
            clusters = 0
            top_clusters = []
            size_buckets: Counter[str] = Counter()
            spread_buckets: Counter[str] = Counter()
            exact_size_hist: Counter[int] = Counter()

            for (ly, h), items in clone_map.items():
                if ly != layer or len(items) < 2:
                    continue
                k = len(items)
                clusters += 1
                dup_instances += k - 1
                exact_size_hist[k] += 1
                if k == 2:
                    size_buckets["01_size_2"] += 1
                elif k <= 5:
                    size_buckets["02_size_3-5"] += 1
                elif k <= 10:
                    size_buckets["03_size_6-10"] += 1
                elif k <= 50:
                    size_buckets["04_size_11-50"] += 1
                elif k <= 500:
                    size_buckets["05_size_51-500"] += 1
                else:
                    size_buckets["06_size_501+"] += 1

                distinct_files = {it[0] for it in items}
                distinct_top_dirs = {it[0].split("/", 1)[0] if "/" in it[0] else "(root)" for it in items}
                if len(distinct_files) == 1:
                    spread_buckets["single_file_only"] += 1
                elif len(distinct_top_dirs) == 1:
                    spread_buckets["multi_file_same_top_dir"] += 1
                else:
                    spread_buckets["cross_top_dir"] += 1

                if k >= 3:
                    top_clusters.append((k, h, items[:5]))
            top_clusters.sort(reverse=True)
            stats[layer] = {
                "eligible_decls": total_eligible,
                "clone_clusters": clusters,
                "redundant_duplicate_decls": dup_instances,
                "duplication_rate_pct": round(dup_instances / total_eligible * 100, 2) if total_eligible else 0.0,
                "size_buckets": dict(sorted(size_buckets.items())),
                "spread_buckets": dict(sorted(spread_buckets.items())),
                "exact_size_histogram_top50": [
                    {"size": sz, "clusters": cnt} for sz, cnt in sorted(exact_size_hist.items())[:50]
                ],
                "top_clusters": [
                    {"count": cnt, "hash": h, "samples": [{"file": f, "line": ln, "name": nm} for f, ln, nm in smp]}
                    for cnt, h, smp in top_clusters[:20]
                ],
            }
        return stats

    exact_clone_stats = _clone_stats(exact_clones, decl_totals_by_layer)
    type2_clone_stats = _clone_stats(type2_clones, decl_totals_by_layer)
    type2_short_stats = _clone_stats(type2_short_clones, decl_totals_short)
    type2_ge20_stats = _clone_stats(type2_ge20_clones, decl_totals_ge20)

    def _cross_bucket_collision_dups(
        stats_map: dict[str, dict],
    ) -> int:
        return (
            stats_map["proof"]["redundant_duplicate_decls"]
            - stats_map["proof_shim"]["redundant_duplicate_decls"]
            - stats_map["proof_substantive"]["redundant_duplicate_decls"]
        )

    exact_cross_bucket = _cross_bucket_collision_dups(exact_clone_stats)
    type2_total_cross_bucket = _cross_bucket_collision_dups(type2_clone_stats)
    type2_short_cross_bucket = _cross_bucket_collision_dups(type2_short_stats)
    type2_ge20_cross_bucket = _cross_bucket_collision_dups(type2_ge20_stats)

    # PG-05 Conservation invariants before emitting output
    assert sum(c["files"] for c in by_module.values()) == len(results), "by_module files mismatch"
    assert sum(c["code_lines"] for c in by_module.values()) == total_code_lines, "by_module code_lines mismatch"
    assert sum(c["files"] for c in by_line_bucket.values()) == len(results), "by_line_bucket files mismatch"
    assert sum(c["files"] for c in by_import_bucket.values()) == len(results), "by_import_bucket files mismatch"
    assert (
        type2_clone_stats["proof_shim"]["eligible_decls"] + type2_clone_stats["proof_substantive"]["eligible_decls"]
        == type2_clone_stats["proof"]["eligible_decls"]
    ), "proof_shim + proof_substantive != proof"
    assert (
        type2_short_stats["proof"]["eligible_decls"] + type2_ge20_stats["proof"]["eligible_decls"]
        == type2_clone_stats["proof"]["eligible_decls"]
    ), "short_8_19 + ge_20 != proof"
    assert type2_total_cross_bucket == type2_short_cross_bucket + type2_ge20_cross_bucket, (
        "cross-bucket hash overlap decomposition mismatch"
    )

    provenance = collect_provenance(root)
    corpus_label = sanitize_root_label(root)

    elapsed_total = time.perf_counter() - t0
    summary = {
        "corpus_label": corpus_label,
        "provenance": provenance,
        "invariants_checked": {
            "by_module_files_conservation": True,
            "by_module_code_lines_conservation": True,
            "by_line_bucket_files_conservation": True,
            "by_import_bucket_files_conservation": True,
            "proof_shim_partition_conservation": True,
            "token_length_partition_conservation": True,
            "cross_bucket_hash_reconciliation": True,
            "all_passed": True,
        },
        "timing_sec": {
            "glob": round(t_glob - t0, 2),
            "scan": round(t_scan - t_glob, 2),
            "total": round(elapsed_total, 2),
            "lines_per_sec": int(total_raw_lines / max(0.01, (t_scan - t_glob))),
        },
        "corpus": {
            "files": len(results),
            "raw_lines": total_raw_lines,
            "code_lines_nonempty_stripped": total_code_lines,
            "top_level_col0_definitions": total_defs,
            "top_level_col0_theorems_lemmas": total_thms,
            "proof_baseline_standalone_by_trivial": total_thm_trivial,
            "proof_baseline_rfl": total_thm_rfl,
        },
        "def_rule_counts": dict(rule_counts),
        "thm_stmt_fun_true_info_count": sum(len(r.thm_info_hits) for r in results),
        "escape_primitives": dict(escape_totals),
        "metaprogramming_primitives": dict(meta_totals),
        "clone_cross_bucket_hash_collisions": {
            "exact_clones": exact_cross_bucket,
            "type2_total": type2_total_cross_bucket,
            "type2_short_8_19": type2_short_cross_bucket,
            "type2_ge_20": type2_ge20_cross_bucket,
        },
        "exact_clones": exact_clone_stats,
        "type2_clones": type2_clone_stats,
        "type2_clones_short_8_19": type2_short_stats,
        "type2_clones_ge_20": type2_ge20_stats,
        "by_module": {k: dict(v) for k, v in sorted(by_module.items())},
        "by_line_bucket": {k: dict(v) for k, v in sorted(by_line_bucket.items())},
        "by_import_bucket": {k: dict(v) for k, v in sorted(by_import_bucket.items())},
        "sample_findings": dict(findings_by_rule),
        "sample_thm_info_hits": thm_info_hits,
    }

    json_path = out_dir / f"{args.prefix}_findings.json"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    dag_input_path = out_dir / f"{args.prefix}_dag_index.json"
    dag_input_path.write_text(
        json.dumps({"provenance": provenance, "modules": module_index, "findings": all_findings_compact}, ensure_ascii=False),
        encoding="utf-8",
    )

    src_arc = provenance.get("source_archive") or {}
    arc_sha = src_arc.get("sha256", "N/A")
    md: list[str] = [
        f"# Lean 4 Static Corpus Audit Report ({args.prefix})",
        "",
        f"- **Corpus**: `{corpus_label}` | **Toolchain**: `{provenance.get('lean_toolchain')}` | **Archive SHA256**: `{arc_sha[:12]}` | **Probe SHA256**: `{provenance['probe_bundle_sha256'][:12]}`",
        f"- **Files**: `{len(results):,}` | **Raw lines**: `{total_raw_lines:,}` | **Non-empty code lines**: `{total_code_lines:,}`",
        f"- **Speed**: `{summary['timing_sec']['lines_per_sec']:,} lines/sec` (glob `{summary['timing_sec']['glob']}s`, scan `{summary['timing_sec']['scan']}s`, total `{summary['timing_sec']['total']}s`)",
        f"- **Top-Level (Column-0) Declarations**: `definitions = {total_defs:,}` | `theorems/lemmas = {total_thms:,}` (standalone `by trivial = {total_thm_trivial:,}`, `rfl = {total_thm_rfl:,}`)",
        "",
        "## 1. Definition-Layer Syntactic Pattern Counts",
        "",
        "| Pattern Rule | Count |",
        "|---|---:|",
    ]
    for rule, cnt in rule_counts.most_common():
        md.append(f"| `{rule}` | {cnt:,} |")
    md.append(f"| *(Info)* `THM_STMT_FUN_TRUE` (theorem signature) | {summary['thm_stmt_fun_true_info_count']:,} |")

    md.extend(["", "## 2. Trust-Boundary & Metaprogramming Primitives", ""])
    md.append(f"- Trust-boundary primitives: `{dict(escape_totals)}`")
    md.append(f"- Metaprogramming primitives: `{dict(meta_totals)}`")

    md.extend(["", "## 3. Clone Decomposition (Exact vs Type-2 Parameterized Identifier Normalization, Shim vs Substantive)", ""])
    md.append("| Mode | Layer | Eligible Decls | Clusters | Redundant Dup Decls | Dup Rate |")
    md.append("|---|---|---:|---:|---:|---:|")
    for mode_name, stats in (
        ("Exact-Token (>=8)", exact_clone_stats),
        ("Type-2 Total (>=8)", type2_clone_stats),
        ("Type-2 Short (8-19)", type2_short_stats),
        ("Type-2 Substantive (>=20)", type2_ge20_stats),
    ):
        for ly in ("definition", "proof", "proof_shim", "proof_substantive"):
            s = stats[ly]
            md.append(
                f"| {mode_name} | {ly} | {s['eligible_decls']:,} | {s['clone_clusters']:,} | {s['redundant_duplicate_decls']:,} | {s['duplication_rate_pct']}% |"
            )
    md.append("")
    md.append(
        f"- Cross-bucket hash collisions (`proof_total - proof_shim - proof_substantive`): "
        f"`Type-2 Total = {type2_total_cross_bucket}` (`8-19 tokens = {type2_short_cross_bucket}`, `>=20 tokens = {type2_ge20_cross_bucket}`)"
    )

    def _append_bucket_table(title: str, bmap: dict[str, Counter]) -> None:
        md.extend(["", f"## {title}", "", "| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |", "|---|---:|---:|---:|---:|---:|---:|"])
        for bk in sorted(bmap):
            c = bmap[bk]
            kloc10 = (c["findings"] / c["code_lines"] * 10000) if c["code_lines"] else 0.0
            kdef1 = (c["findings"] / c["defs"] * 1000) if c["defs"] else 0.0
            md.append(f"| `{bk}` | {c['files']:,} | {c['code_lines']:,} | {c['defs']:,} | {c['findings']:,} | {kloc10:.2f} | {kdef1:.2f} |")

    _append_bucket_table("4. Complexity Bucket: By Non-Empty Code Lines", by_line_bucket)
    _append_bucket_table("5. Complexity Bucket: By Import Count", by_import_bucket)
    _append_bucket_table("6. Breakdown: By Top-Level Module", by_module)

    md_path = out_dir / f"{args.prefix}_summary.md"
    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"DONE in {elapsed_total:.2f}s -> {md_path} & {json_path}")


if __name__ == "__main__":
    main()
