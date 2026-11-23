"""SE Maintainability & Topology Metrics computed directly from `*_dag_index.json`.

Computes:
  1) Deduplicated Module DAG Fan-in / Fan-out percentiles & longest dependency depth
  2) Exact Transitive Blast Radius across ALL modules (chunked topological bitset, zero Top-150 blind spot)
  3) Cross-directory coupling matrix (top-level modules)
  4) Gini concentration & Lorenz top-1%/5%/10% shares for code_lines, raw_lines, defs, thms
  5) PG-04 provenance & PG-05 conservation invariants
"""

from __future__ import annotations

import argparse
import json
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

from audit_provenance import sha256_file


def _gini(values: list[int]) -> float:
    n = len(values)
    if n == 0:
        return 0.0
    s = sorted(values)
    total = sum(s)
    if total == 0:
        return 0.0
    weighted = sum((i + 1) * v for i, v in enumerate(s))
    return (2.0 * weighted) / (n * total) - (n + 1.0) / n


def _top_share(values: list[int], frac: float) -> float:
    if not values:
        return 0.0
    total = sum(values)
    if total == 0:
        return 0.0
    k = max(1, int(len(values) * frac))
    return sum(sorted(values, reverse=True)[:k]) / total * 100.0


def _pct(sorted_vals: list[int], q: float) -> int:
    if not sorted_vals:
        return 0
    idx = min(len(sorted_vals) - 1, int(q * (len(sorted_vals) - 1)))
    return sorted_vals[idx]


def _exact_blast_radius_all(
    mod_names: list[str],
    adj: dict[str, list[str]],
    topo_order: list[str],
    chunk_size: int = 8000,
) -> list[int]:
    """Compute exact transitive importer count (excluding self) for every module via chunked bitsets."""
    n = len(mod_names)
    idx_of = {m: i for i, m in enumerate(mod_names)}
    adj_idx = [[idx_of[imp] for imp in adj[m]] for m in mod_names]
    rev_topo_idx = [idx_of[m] for m in reversed(topo_order)]

    blast = [0] * n
    for start in range(0, n, chunk_size):
        end = min(n, start + chunk_size)
        bits = [0] * n
        for i in range(start, end):
            bits[i] = 1 << (i - start)
        for u in rev_topo_idx:
            bu = bits[u]
            if bu:
                for v in adj_idx[u]:
                    bits[v] |= bu
        for i in range(n):
            c = bits[i].bit_count()
            if start <= i < end:
                c -= 1  # exclude self
            blast[i] += c
    return blast


def main() -> None:
    ap = argparse.ArgumentParser(description="Compute SE topology & Gini metrics from dag_index.json")
    ap.add_argument("--dag-index", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--prefix", default="full_se_topology")
    args = ap.parse_args()

    t0 = time.perf_counter()
    dag_path = Path(args.dag_index)
    idx_data = json.loads(dag_path.read_text(encoding="utf-8"))
    modules: dict[str, dict] = idx_data["modules"]
    findings: list[dict] = idx_data.get("findings", [])
    provenance = idx_data.get("provenance", {})

    findings_by_mod: Counter[str] = Counter(f["module"] for f in findings)

    adj: dict[str, list[str]] = {}
    rev_adj: dict[str, list[str]] = defaultdict(list)
    ext_fanout: list[int] = []
    local_fanout: list[int] = []

    for mod, info in modules.items():
        # Deduplicate imports per module to prevent fake fan-in/fan-out inflation
        dedup_imps = list(dict.fromkeys(info["imports"]))
        local_imps = [imp for imp in dedup_imps if imp in modules]
        adj[mod] = local_imps
        local_fanout.append(len(local_imps))
        ext_fanout.append(len(dedup_imps) - len(local_imps))
        for imp in local_imps:
            rev_adj[imp].append(mod)

    direct_fanin = {mod: len(rev_adj.get(mod, ())) for mod in modules}

    # Kahn topological sort from leaf modules (0 local imports) upward
    rem_deps = {mod: len(adj[mod]) for mod in modules}
    q = deque([m for m, d in rem_deps.items() if d == 0])
    topo_order: list[str] = []
    dag_depth: dict[str, int] = {m: 0 for m in modules}
    while q:
        u = q.popleft()
        topo_order.append(u)
        du = dag_depth[u]
        for parent in rev_adj.get(u, ()):
            if du + 1 > dag_depth[parent]:
                dag_depth[parent] = du + 1
            rem_deps[parent] -= 1
            if rem_deps[parent] == 0:
                q.append(parent)

    has_cycle = len(topo_order) != len(modules)
    mod_names = sorted(modules.keys())

    if not has_cycle:
        blast_list = _exact_blast_radius_all(mod_names, adj, topo_order)
        blast_map = {m: b for m, b in zip(mod_names, blast_list)}
    else:
        blast_map = {}
        for mod in mod_names:
            vis: set[str] = set()
            dq = deque([mod])
            while dq:
                c = dq.popleft()
                for imp in rev_adj.get(c, ()):
                    if imp not in vis:
                        vis.add(imp)
                        dq.append(imp)
            blast_map[mod] = len(vis)

    def _hub_row(mod: str) -> dict:
        return {
            "module": mod,
            "file": modules[mod]["file"],
            "direct_fan_in": direct_fanin[mod],
            "transitive_blast_radius": blast_map[mod],
            "blast_pct": round(blast_map[mod] / len(modules) * 100, 2) if modules else 0.0,
            "local_fan_out": len(adj[mod]),
            "dag_depth": dag_depth.get(mod, -1),
            "code_lines": modules[mod]["code_lines"],
            "def_pattern_findings_in_file": findings_by_mod.get(mod, 0),
        }

    hubs_by_fanin = [_hub_row(m) for m in sorted(mod_names, key=lambda m: (direct_fanin[m], blast_map[m]), reverse=True)[:30]]
    hubs_by_blast = [_hub_row(m) for m in sorted(mod_names, key=lambda m: (blast_map[m], direct_fanin[m]), reverse=True)[:30]]

    # Cross-directory coupling matrix (top-level directories, deduplicated edges)
    coupling: dict[str, Counter] = defaultdict(Counter)
    for mod, local_imps in adj.items():
        src_top = modules[mod]["file"].split("/", 1)[0] if "/" in modules[mod]["file"] else "(root)"
        for imp in local_imps:
            dst_top = modules[imp]["file"].split("/", 1)[0] if "/" in modules[imp]["file"] else "(root)"
            coupling[src_top][dst_top] += 1

    # Gini & Lorenz concentration
    code_lines_list = [m["code_lines"] for m in modules.values()]
    raw_lines_list = [m["raw_lines"] for m in modules.values()]
    defs_list = [m["defs"] for m in modules.values()]
    thms_list = [m["thms"] for m in modules.values()]
    fanin_list = sorted(direct_fanin.values())
    fanout_list = sorted(local_fanout)
    blast_vals = sorted(blast_map.values())
    depth_list = sorted(dag_depth.values())

    zero_decl_files = sum(1 for m in modules.values() if m["defs"] == 0 and m["thms"] == 0)

    gini_stats = {}
    for label, arr in (
        ("code_lines", code_lines_list),
        ("raw_lines", raw_lines_list),
        ("defs", defs_list),
        ("thms", thms_list),
        ("direct_fan_in", fanin_list),
        ("local_fan_out", fanout_list),
        ("transitive_blast_radius", blast_vals),
    ):
        s_arr = sorted(arr)
        gini_stats[label] = {
            "total": sum(arr),
            "gini": round(_gini(arr), 4),
            "top_1pct_share_pct": round(_top_share(arr, 0.01), 2),
            "top_5pct_share_pct": round(_top_share(arr, 0.05), 2),
            "top_10pct_share_pct": round(_top_share(arr, 0.10), 2),
            "p50": _pct(s_arr, 0.50),
            "p90": _pct(s_arr, 0.90),
            "p99": _pct(s_arr, 0.99),
            "max": s_arr[-1] if s_arr else 0,
        }

    # PG-05 Conservation invariants
    total_edges_fanout = sum(local_fanout)
    total_edges_fanin = sum(direct_fanin.values())
    total_edges_coupling = sum(sum(row.values()) for row in coupling.values())
    assert total_edges_fanout == total_edges_fanin == total_edges_coupling, "Edge count conservation failed"

    elapsed = time.perf_counter() - t0
    report = {
        "timing_sec": round(elapsed, 2),
        "provenance": {
            "dag_index_name": dag_path.name,
            "se_topology_sha256": sha256_file(Path(__file__)),
            "upstream_provenance": provenance,
        },
        "invariants_checked": {
            "edge_conservation": True,
            "dag_acyclic": not has_cycle,
            "exact_all_nodes_blast_radius": not has_cycle,
        },
        "module_count": len(modules),
        "dag_acyclic": not has_cycle,
        "topo_sorted_count": len(topo_order),
        "max_dag_depth": depth_list[-1] if depth_list else 0,
        "p90_dag_depth": _pct(depth_list, 0.90),
        "zero_decl_wrapper_files": zero_decl_files,
        "zero_decl_wrapper_pct": round(zero_decl_files / len(modules) * 100, 2) if modules else 0.0,
        "gini_and_percentiles": gini_stats,
        "top_30_hubs_by_blast_radius": hubs_by_blast,
        "top_30_hubs_by_direct_fanin": hubs_by_fanin,
        "cross_dir_coupling_matrix": {k: dict(v) for k, v in sorted(coupling.items())},
    }

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{args.prefix}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        f"# Lean 4 SE Maintainability & Topology Report ({args.prefix})",
        "",
        f"- **Modules**: `{len(modules):,}` | **Acyclic DAG**: `{not has_cycle}` (`{len(topo_order):,}/{len(modules):,}`) | **Max DAG Depth**: `{report['max_dag_depth']}` (`p90={report['p90_dag_depth']}`)",
        f"- **Zero-Declaration Files (`defs=0 & thms=0`)**: `{zero_decl_files:,}` (`{report['zero_decl_wrapper_pct']}%`) | **Elapsed**: `{elapsed:.2f}s`",
        "",
        "## 1. Gini Concentration & Quantiles",
        "",
        "| Metric | Total | Gini | Top 1% Share | Top 5% Share | Top 10% Share | P50 | P90 | P99 | Max |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for label, g in gini_stats.items():
        md.append(
            f"| `{label}` | {g['total']:,} | {g['gini']:.4f} | {g['top_1pct_share_pct']}% | {g['top_5pct_share_pct']}% | {g['top_10pct_share_pct']}% | {g['p50']:,} | {g['p90']:,} | {g['p99']:,} | {g['max']:,} |"
        )

    md.extend(["", "## 2. Top-25 Hub Bottlenecks (by Exact Transitive Blast Radius)", "", "| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |", "|---|---:|---:|---:|---:|---:|---:|"])
    for h in hubs_by_blast[:25]:
        md.append(
            f"| `{h['module']}` | {h['direct_fan_in']:,} | {h['transitive_blast_radius']:,} | {h['blast_pct']}% | {h['local_fan_out']} | {h['dag_depth']} | {h['code_lines']:,} |"
        )

    md.extend(["", "## 3. Top-25 Hub Bottlenecks (by Direct Fan-In)", "", "| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |", "|---|---:|---:|---:|---:|---:|---:|"])
    for h in hubs_by_fanin[:25]:
        md.append(
            f"| `{h['module']}` | {h['direct_fan_in']:,} | {h['transitive_blast_radius']:,} | {h['blast_pct']}% | {h['local_fan_out']} | {h['dag_depth']} | {h['code_lines']:,} |"
        )

    md.extend(["", "## 4. Cross-Directory Coupling Matrix (Source -> Imported Target, Deduplicated Edges)", ""])
    all_dirs = sorted(set(coupling.keys()) | {d for row in coupling.values() for d in row})
    md.append("| Source \\\\ Target | " + " | ".join(all_dirs) + " |")
    md.append("|---|" + "|".join("---:" for _ in all_dirs) + "|")
    for s in all_dirs:
        row = coupling.get(s, {})
        md.append(f"| `{s}` | " + " | ".join(f"{row.get(t, 0):,}" for t in all_dirs) + " |")

    (out_dir / f"{args.prefix}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"DONE SE topology in {elapsed:.2f}s -> {out_dir / (args.prefix + '.md')}")


if __name__ == "__main__":
    main()
