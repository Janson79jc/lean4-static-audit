"""Generate publication-ready vector figures directly from audited JSON reports.

Outputs (saved to `--out-dir`, default `reports/figures`):
  - `fig1_clones_and_density.pdf` / `.png`
  - `fig2_topology_concentration.pdf` / `.png`
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def _configure_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.titlesize": 10,
            "axes.titleweight": "bold",
            "axes.labelsize": 9,
            "xtick.labelsize": 8.5,
            "ytick.labelsize": 8.5,
            "legend.fontsize": 8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "grid.linestyle": "--",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def plot_fig1_clones_and_density(findings: dict, out_dir: Path) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.0), dpi=200)
    fig.subplots_adjust(wspace=0.28, bottom=0.20, top=0.86, left=0.07, right=0.98)

    # Panel (a): Proof Clone Rate & Single-Template Dominance
    ex_proof = findings["exact_clones"]["proof"]
    t2_short_sub = findings["type2_clones_short_8_19"]["proof_substantive"]
    t2_long_sub = findings["type2_clones_ge_20"]["proof_substantive"]
    t2_long_shim = findings["type2_clones_ge_20"]["proof_shim"]
    t2_all_shim = findings["type2_clones"]["proof_shim"]
    top_shim_cluster = t2_all_shim["top_clusters"][0]["count"]
    shim_share_all = top_shim_cluster / t2_all_shim["eligible_decls"] * 100.0
    shim_share_ge20 = top_shim_cluster / t2_long_shim["eligible_decls"] * 100.0

    labels = [
        f"Exact-Token\n(All ≥8)\nn={ex_proof['eligible_decls']:,}",
        f"Type-2 Short\n(8–19, Subst.)\nn={t2_short_sub['eligible_decls']:,}",
        f"Type-2 Long\n(≥20, Subst.)\nn={t2_long_sub['eligible_decls']:,}",
        f"Type-2 Long\n(≥20, Shim)\nn={t2_long_shim['eligible_decls']:,}",
    ]
    rates = [
        ex_proof["duplication_rate_pct"],
        t2_short_sub["duplication_rate_pct"],
        t2_long_sub["duplication_rate_pct"],
        t2_long_shim["duplication_rate_pct"],
    ]
    dups = [
        ex_proof["redundant_duplicate_decls"],
        t2_short_sub["redundant_duplicate_decls"],
        t2_long_sub["redundant_duplicate_decls"],
        t2_long_shim["redundant_duplicate_decls"],
    ]
    colors = ["#4c78a8", "#f58518", "#54a24b", "#e45756"]

    x = np.arange(len(labels))
    bars = ax1.bar(x, rates, width=0.56, color=colors, edgecolor="#222222", linewidth=0.6, zorder=3)
    ax1.set_ylim(0, 118)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("Redundant Clone Rate (%)")
    ax1.set_title(f"(a) Proof Clone Rate by Length & Role (N={ex_proof['eligible_decls']:,})")

    for bar, rate, dup in zip(bars, rates, dups):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2.0,
            f"{rate:.2f}%\n({dup:,})",
            ha="center",
            va="bottom",
            fontsize=8,
            fontweight="bold",
            color="#222222",
        )

    # Callout for single dominant template cluster d52746a3d7614f9d
    ax1.annotate(
        f"Single template cluster\n{t2_all_shim['top_clusters'][0]['hash']}:\n"
        f"{top_shim_cluster:,} decls ({shim_share_all:.1f}% of all shims;\n"
        f"{shim_share_ge20:.1f}% of ≥20-tok shims)",
        xy=(2.72, rates[3] * 0.65),
        xytext=(0.72, 83),
        fontsize=7.6,
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff5f5", edgecolor="#e45756", linewidth=0.9),
        arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.1, connectionstyle="arc3,rad=-0.12"),
        zorder=5,
    )

    # Panel (b): Syntactic Pattern Density by Non-Empty Code Lines
    bucket_order = ["01_<50_lines", "02_50-199_lines", "03_200-499_lines", "04_500+_lines"]
    bucket_labels = ["<50\nlines", "50–199\nlines", "200–499\nlines", "500+\nlines"]
    by_line = findings["by_line_bucket"]

    hits_per_1k_defs = []
    hits_per_10k_lines = []
    file_counts = []
    for k in bucket_order:
        b = by_line[k]
        file_counts.append(b["files"])
        hits_per_1k_defs.append(b["findings"] / max(1, b["defs"]) * 1000.0)
        hits_per_10k_lines.append(b["findings"] / max(1, b["code_lines"]) * 10000.0)

    bx = np.arange(len(bucket_order))
    b_labels_full = [f"{lbl}\n({cnt:,} files)" for lbl, cnt in zip(bucket_labels, file_counts)]
    b1 = ax2.bar(
        bx,
        hits_per_1k_defs,
        width=0.50,
        color="#4c78a8",
        edgecolor="#222222",
        linewidth=0.6,
        label="Findings / 1k defs (left)",
        zorder=3,
    )
    ax2.set_xticks(bx)
    ax2.set_xticklabels(b_labels_full)
    ax2.set_ylabel("Definition-Layer Hits / 1k Defs", color="#2c5282")
    ax2.set_ylim(0, max(hits_per_1k_defs) * 1.24)
    ax2.set_title(f"(b) Pattern Density vs. Module Size ({findings['corpus']['files']:,} files)")

    for bar, val in zip(b1, hits_per_1k_defs):
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.25,
            f"{val:.2f}",
            ha="center",
            va="bottom",
            fontsize=8,
            fontweight="bold",
            color="#1a365d",
        )

    ax2_r = ax2.twinx()
    ax2_r.spines["top"].set_visible(False)
    ax2_r.grid(False)
    ax2_r.plot(
        bx,
        hits_per_10k_lines,
        color="#d62728",
        marker="o",
        linewidth=2.0,
        markersize=5.5,
        label="Findings / 10k code lines (right)",
        zorder=4,
    )
    ax2_r.set_ylabel("Definition-Layer Hits / 10k Code Lines", color="#9b2c2c")
    ax2_r.set_ylim(0, max(hits_per_10k_lines) * 1.48)
    for xi, yi in zip(bx, hits_per_10k_lines):
        ax2_r.text(
            xi,
            yi - 0.16,
            f"{yi:.2f}",
            ha="center",
            va="top",
            fontsize=7.5,
            color="#9b2c2c",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="#d62728", linewidth=0.5, alpha=0.92),
            zorder=5,
        )

    h1, l1 = ax2.get_legend_handles_labels()
    h2, l2 = ax2_r.get_legend_handles_labels()
    ax2.legend(h1 + h2, l1 + l2, loc="upper left", frameon=True, facecolor="white", framealpha=0.9)

    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"fig1_clones_and_density.{ext}", bbox_inches="tight")
    plt.close(fig)


def plot_fig2_topology_concentration(topo: dict, out_dir: Path) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.0, 4.1), dpi=200)
    fig.subplots_adjust(wspace=0.30, bottom=0.17, top=0.86, left=0.14, right=0.97)

    # Panel (a): Gini Concentration & Top-k Shares
    gini_map = topo["gini_and_percentiles"]
    metrics = [
        ("local_fan_out", "Local Fan-Out"),
        ("code_lines", "Code Lines"),
        ("thms", "Theorems / Lemmas"),
        ("direct_fan_in", "Direct Fan-In"),
        ("transitive_blast_radius", "Transitive Blast Radius"),
        ("defs", "Definitions"),
    ]
    y = np.arange(len(metrics))
    top1 = [gini_map[k]["top_1pct_share_pct"] for k, _ in metrics]
    top5_delta = [gini_map[k]["top_5pct_share_pct"] - gini_map[k]["top_1pct_share_pct"] for k, _ in metrics]
    top10_delta = [gini_map[k]["top_10pct_share_pct"] - gini_map[k]["top_5pct_share_pct"] for k, _ in metrics]
    ginis = [gini_map[k]["gini"] for k, _ in metrics]

    ax1.barh(y, top1, height=0.56, color="#2b6cb0", label="Top 1% Modules", zorder=3)
    ax1.barh(y, top5_delta, left=top1, height=0.56, color="#63b3ed", label="Next 4% (Top 5%)", zorder=3)
    left10 = [a + b for a, b in zip(top1, top5_delta)]
    ax1.barh(y, top10_delta, left=left10, height=0.56, color="#bee3f8", edgecolor="#63b3ed", linewidth=0.5, label="Next 5% (Top 10%)", zorder=3)

    ax1.set_yticks(y)
    ax1.set_yticklabels([lbl for _, lbl in metrics])
    ax1.set_xlim(0, 114)
    ax1.set_xlabel("Share of Corpus Total Held by Top Modules (%)")
    ax1.set_title("(a) Structural Concentration & Gini Index")
    ax1.legend(loc="lower right", frameon=True, facecolor="white", framealpha=0.92, fontsize=7.6)

    for yi, a, b, c, g in zip(y, top1, top5_delta, top10_delta, ginis):
        total10 = a + b + c
        ax1.text(total10 + 1.5, yi, f"{total10:.1f}% (G={g:.2f})", va="center", ha="left", fontsize=7.8, fontweight="bold", color="#1a202c")

    # Panel (b): Direct Fan-In vs Transitive Blast Radius (%)
    by_blast = {m["module"]: m for m in topo["top_30_hubs_by_blast_radius"]}
    by_fanin = {m["module"]: m for m in topo["top_30_hubs_by_direct_fanin"]}
    both_mods = set(by_blast) & set(by_fanin)
    blast_only = [m for k, m in by_blast.items() if k not in both_mods]
    fanin_only = [m for k, m in by_fanin.items() if k not in both_mods]
    both_list = [by_blast[k] for k in both_mods]

    def _scatter_group(items: list[dict], color: str, marker: str, label: str, size: float = 42) -> None:
        if not items:
            return
        xs = [max(1, it["direct_fan_in"]) for it in items]
        ys = [it["blast_pct"] for it in items]
        ax2.scatter(xs, ys, c=color, marker=marker, s=size, alpha=0.88, edgecolors="#222222", linewidths=0.5, label=label, zorder=4)

    _scatter_group(blast_only, "#e45756", "o", "Top-30 Blast Radius")
    _scatter_group(fanin_only, "#4c78a8", "^", "Top-30 Direct Fan-In")
    _scatter_group(both_list, "#9b59b6", "D", "In Both Top-30 Lists", size=50)

    ax2.set_xscale("log")
    ax2.set_xlim(0.7, 6000)
    ax2.set_ylim(-2, 72)
    ax2.set_xlabel("Direct Fan-In (Importers, log scale)")
    ax2.set_ylabel(f"Transitive Blast Radius (% of {topo['module_count']:,} modules)")
    ax2.set_title("(b) Low-Fan-In Bottlenecks vs. Local Hubs")
    ax2.legend(loc="lower left", frameon=True, facecolor="white", framealpha=0.92, fontsize=7.6)

    # Annotate key structural outliers directly from JSON
    all_hubs = {**by_fanin, **by_blast}
    top_blast = max(by_blast.values(), key=lambda r: r["blast_pct"])
    top_fanin = max(by_fanin.values(), key=lambda r: r["direct_fan_in"])
    smallest_fanin_high_blast = min(by_blast.values(), key=lambda r: (r["direct_fan_in"], -r["blast_pct"]))
    is_hol = all_hubs.get("ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.IsHolPeriods")

    ax2.annotate(
        f"{top_blast['module'].rsplit('.', 1)[-1]}\n(fan-in={top_blast['direct_fan_in']}, {top_blast['blast_pct']:.1f}%)",
        xy=(top_blast["direct_fan_in"], top_blast["blast_pct"]),
        xytext=(55, 63),
        fontsize=7.3,
        arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8),
        zorder=5,
    )
    ax2.annotate(
        f"{smallest_fanin_high_blast['module'].rsplit('.', 1)[-1]}\n(fan-in={smallest_fanin_high_blast['direct_fan_in']}, {smallest_fanin_high_blast['blast_pct']:.1f}%)",
        xy=(smallest_fanin_high_blast["direct_fan_in"], smallest_fanin_high_blast["blast_pct"]),
        xytext=(1.1, 47),
        fontsize=7.3,
        arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8),
        zorder=5,
    )
    ax2.annotate(
        f"{top_fanin['module'].rsplit('.', 1)[-1]}\n(fan-in={top_fanin['direct_fan_in']:,}, {top_fanin['blast_pct']:.1f}%)",
        xy=(top_fanin["direct_fan_in"], top_fanin["blast_pct"]),
        xytext=(75, 16),
        fontsize=7.3,
        arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8, connectionstyle="arc3,rad=-0.16"),
        zorder=5,
    )
    if is_hol:
        ax2.annotate(
            f"IsHolPeriods\n(fan-in={is_hol['direct_fan_in']:,}, {is_hol['blast_pct']:.1f}%)",
            xy=(is_hol["direct_fan_in"], is_hol["blast_pct"]),
            xytext=(42, 42),
            fontsize=7.3,
            arrowprops=dict(arrowstyle="->", color="#333333", lw=0.8, connectionstyle="arc3,rad=-0.10"),
            zorder=5,
        )

    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"fig2_topology_concentration.{ext}", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    root_dir = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description="Generate Lean 4 audit vector figures from JSON outputs")
    ap.add_argument("--findings", default=str(root_dir / "reports" / "full_clean_findings.json"))
    ap.add_argument("--topology", default=str(root_dir / "reports" / "full_clean_se_topology.json"))
    ap.add_argument("--out-dir", default=str(root_dir / "reports" / "figures"))
    args = ap.parse_args()

    findings = json.loads(Path(args.findings).read_text(encoding="utf-8"))
    topo = json.loads(Path(args.topology).read_text(encoding="utf-8"))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    _configure_style()
    plot_fig1_clones_and_density(findings, out_dir)
    plot_fig2_topology_concentration(topo, out_dir)
    print(f"FIGURES_WRITTEN -> {out_dir}")


if __name__ == "__main__":
    main()
