# Static Structural Audit of the 17.37-Million-Line Lean 4 Riemann Hypothesis Archive

[![Code License: Apache-2.0](https://img.shields.io/badge/Code%20License-Apache--2.0-blue.svg)](LICENSE)
[![Data & Report License: CC BY 4.0](https://img.shields.io/badge/Data%20%26%20Report-CC%20BY%204.0-lightgrey.svg)](LICENSE-DATA)

An open-source, pure static lexical, syntactic-pattern, clone-decomposition, and import-topology audit suite for large-scale Lean 4 repositories, accompanied by full empirical artifacts on the 175,187-file (`17,374,215` raw lines / `15,531,759` stripped code lines) Lean 4 Riemann Hypothesis formalization archive (`leanprover/lean4:v4.33.1`).

> **Scope & Disclaimer.** This audit performs static lexical scanning, top-level (column-0) declaration parsing, and import-DAG topology analysis. It does **not** re-run the Lean 4 type checker or any external kernel, and neither certifies nor refutes the mathematical correctness of any target theorem. Syntactic patterns reported here (e.g., unused explicit parameters, constant `True`/`False` bodies, forwarding shims) represent structural indicators rather than guaranteed defects; manual inspection confirms benign instances such as legacy branch toggles (`SwOn.lean:3`) and vacuous base conditions (`IsExpansion.lean:81`).

## Key Audited Facts (`probe_bundle_sha256`: `43501e2c8041`)

- **Corpus Snapshot**: Package `tree`, toolchain `leanprover/lean4:v4.33.1`, `mathlib4` rev `0df444a360eaa60ab8c11dca51a86af692955474`, source archive `lean.tar.gz` (`239,275,554` bytes, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`).
- **Full Connectivity & Acyclicity**: `175,187 / 175,187` (`100.0%`) files reachable from `Main`; `753,261` deduplicated import edges; strict DAG (`max_depth = 202`, `p90 = 98`).
- **Trust Boundary**: `0` occurrences detected across 17 checked lexical trust-boundary primitives (`sorry`, `admit`, `sorryAx`, `mkSorry`, `native_decide`, `ofReduceBool`, `ofReduceNat`, `implemented_by`, `@[extern]`, `@[csimp]`, `debug.skipKernelTC`, `trustCompiler`, `unsafe`, `axiom`, `opaque`, `addAndCompile`, `setEnv`). Metaprogramming/environment activity concentrates in **34** deduplicated `run_tac`/`liftMetaTactic`/`partial` source sites (`64` raw hits) plus **7** environment calls (`5` `modifyEnv` in `BuildAid/D1..D5.lean`, `2` `addDecl` in `CutCptCopy.lean`), alongside `12` direct `import Lean` lines across 7 helper files (`BuildAid/D1..D5`: 10, `Imports.lean`: 1, `OwnStruct.lean`: 1; `CutCptCopy.lean` accesses `Lean` transitively), `5` `run_cmd`, `4` `elab`, and `87` `macro` rules (spot-checked samples are local `scoped macro` shorthands).
- **Type-2 Clone Stratification (`734,084` proofs $\ge 8$ tokens)**: Forwarding shims (`n=50,682`) collapse by `96.27%` (`97.99%` at $\ge 20$ tokens), with a single 3-branch forwarding template (`d52746a3d7614f9d`) accounting for **43,525** declarations (**85.9%** of all shims). By contrast, substantive proofs $\ge 20$ tokens (`n=571,274`) exhibit only **6.39%** Type-2 duplication (`cross_bucket_hash_collisions = 0`).
- **Concentration & Low-Fan-In Bottlenecks**: `transitive_blast_radius` has Gini `0.8905` (Top 10% hold `86.02%`). Top-30 blast-radius hubs (`59.70%–61.68%` impact) all have `direct_fan_in` between `1` and `188` and are completely disjoint from the Top-30 direct fan-in hubs (`775–3,088`).

> **Verification Note**: Audit and plotting scripts were developed in a human–AI collaborative workflow and validated via 10 deterministic unit/regression tests (`scripts/test_lean_probes.py`), pre-output conservation assertions (`invariants_checked.all_passed`), and raw-output cross-checks rather than line-by-line manual Python code review; all hashed scripts (`probe_bundle_sha256: 43501e2c8041...`) are included for independent inspection.

## Repository Structure

- `scripts/` — Static lexer (`lean_lexer.py`), column-0 parser (`lean_decl_parser.py`), probe engine (`lean_probes.py`), L1+L2 runner (`run_audit.py`), SE topology (`se_topology.py`), L3-A reachability (`lean_dag.py`), L2.5 extended trust/dual audit (`run_l25_audit.py`), provenance helper (`audit_provenance.py`), figure generator (`plot_figures.py`), and regression suite (`test_lean_probes.py`).
- `configs/rh_archive.json` — Externalized entry roots and target symbol list (keeps Python probes repository-agnostic).
- `reports/` — Audited Markdown summaries, aggregate JSON datasets, and publication vector figures (`reports/figures/`).
- `paper/` — 3-page LaTeX technical short paper (`paper/main.tex`, `paper/refs.bib`, `paper/main.pdf`).

## Reproducing the Audit

All core audit scripts (`scripts/run_audit.py`, `se_topology.py`, `lean_dag.py`, `run_l25_audit.py`, `test_lean_probes.py`) require **Python 3.10+ standard library only**; figure regeneration additionally requires `matplotlib` and `numpy`.

### 1. Run Deterministic Unit & Regression Tests (No Corpus Required)

```bash
python -B scripts/test_lean_probes.py
```

### 2. Regenerate Figures & Technical Report (From Committed JSONs)

```bash
pip install matplotlib numpy
python -B scripts/plot_figures.py
cd paper && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

### 3. Full End-to-End Pipeline (On the 175,187-File Archive)

1. Obtain the original release archive (`lean.tar.gz`, `239,275,554` bytes, SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`), place it at `raw/lean.tar.gz` (optional, for provenance hash verification), and extract the `.lean` source tree (e.g., under `corpus/src/`).
2. Run the 4-stage pipeline from the repository root:
   ```bash
   python -B scripts/run_audit.py --root corpus/src --out-dir reports --prefix full_clean
   python -B scripts/se_topology.py \
     --dag-index reports/full_clean_dag_index.json \
     --out-dir reports --prefix full_clean_se_topology
   python -B scripts/lean_dag.py \
     --root corpus/src --dag-index reports/full_clean_dag_index.json \
     --out-dir reports --prefix full_clean \
     --entry-config configs/rh_archive.json --l3a-only
   python -B scripts/run_l25_audit.py \
     --root corpus/src --out-dir reports --prefix full_clean_l25 \
     --shadow-config configs/rh_archive.json
   python -B scripts/plot_figures.py
   ```
   - `run_audit.py` writes a ~110 MB local intermediate `reports/full_clean_dag_index.json` consumed by `se_topology.py` and `lean_dag.py`; it is excluded from Git via `.gitignore` and can be removed after downstream stages finish.
   - Core script hashes lock to `probe_bundle_sha256 = 43501e2c8041ccdda6b59a4c324450c9f402c1913682be1f87d82d7562adfbce`.

## Citation

If you use the audit scripts, datasets, or technical report, please cite:

```bibtex
@misc{Jiang_2026_lean4_static_audit,
  author       = {Jiang, Chen},
  title        = {Static Structural Audit of the 17.37-Million-Line Lean 4
                  Riemann Hypothesis Archive: Trust Boundaries, Type-2 Clones,
                  and Dependency Topology},
  year         = {2026},
  month        = nov,
  doi          = {10.5281/zenodo.24465791},
  url          = {https://doi.org/10.5281/zenodo.24465791},
  howpublished = {Zenodo}
}
```

## Dual Licensing

Report and data (`reports/`, `paper/`) are licensed under **CC BY 4.0** ([`LICENSE-DATA`](LICENSE-DATA)); audit scripts and configuration (`scripts/`, `configs/`) are licensed under **Apache-2.0** ([`LICENSE`](LICENSE)). See [`NOTICE`](NOTICE) for attribution details.
