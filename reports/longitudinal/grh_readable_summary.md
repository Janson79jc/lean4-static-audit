# Lean 4 Static Corpus Audit Report (grh_readable)

- **Corpus**: `corpus/grh-lean/grh/src` | **Toolchain**: `leanprover/lean4:v4.35.0` | **Archive SHA256**: `9631b4f02019` | **Probe SHA256**: `43501e2c8041`
- **Files**: `803` | **Raw lines**: `477,124` | **Non-empty code lines**: `299,902`
- **Speed**: `18,414 lines/sec` (glob `0.04s`, scan `25.91s`, total `27.77s`)
- **Top-Level (Column-0) Declarations**: `definitions = 5,612` | `theorems/lemmas = 18,227` (standalone `by trivial = 0`, `rfl = 445`)

## 1. Definition-Layer Syntactic Pattern Counts

| Pattern Rule | Count |
|---|---:|
| `DEF_EXPLICIT_WILDCARD_PARAM` | 16 |
| `DEF_UNUSED_EXPLICIT_UNDERSCORE_PARAM` | 1 |
| *(Info)* `THM_STMT_FUN_TRUE` (theorem signature) | 0 |

## 2. Trust-Boundary & Metaprogramming Primitives

- Trust-boundary primitives: `{}`
- Metaprogramming primitives: `{}`

## 3. Clone Decomposition (Exact vs Type-2 Parameterized Identifier Normalization, Shim vs Substantive)

| Mode | Layer | Eligible Decls | Clusters | Redundant Dup Decls | Dup Rate |
|---|---|---:|---:|---:|---:|
| Exact-Token (>=8) | definition | 3,655 | 0 | 0 | 0.0% |
| Exact-Token (>=8) | proof | 16,058 | 27 | 29 | 0.18% |
| Exact-Token (>=8) | proof_shim | 42 | 0 | 0 | 0.0% |
| Exact-Token (>=8) | proof_substantive | 16,016 | 27 | 29 | 0.18% |
| Type-2 Total (>=8) | definition | 3,655 | 61 | 94 | 2.57% |
| Type-2 Total (>=8) | proof | 16,058 | 256 | 817 | 5.09% |
| Type-2 Total (>=8) | proof_shim | 42 | 0 | 0 | 0.0% |
| Type-2 Total (>=8) | proof_substantive | 16,016 | 256 | 817 | 5.1% |
| Type-2 Short (8-19) | definition | 1,442 | 50 | 83 | 5.76% |
| Type-2 Short (8-19) | proof | 2,830 | 233 | 793 | 28.02% |
| Type-2 Short (8-19) | proof_shim | 19 | 0 | 0 | 0.0% |
| Type-2 Short (8-19) | proof_substantive | 2,811 | 233 | 793 | 28.21% |
| Type-2 Substantive (>=20) | definition | 2,213 | 11 | 11 | 0.5% |
| Type-2 Substantive (>=20) | proof | 13,228 | 23 | 24 | 0.18% |
| Type-2 Substantive (>=20) | proof_shim | 23 | 0 | 0 | 0.0% |
| Type-2 Substantive (>=20) | proof_substantive | 13,205 | 23 | 24 | 0.18% |

- Cross-bucket hash collisions (`proof_total - proof_shim - proof_substantive`): `Type-2 Total = 0` (`8-19 tokens = 0`, `>=20 tokens = 0`)

## 4. Complexity Bucket: By Non-Empty Code Lines

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `01_<50_lines` | 9 | 230 | 13 | 0 | 0.00 | 0.00 |
| `02_50-199_lines` | 143 | 19,228 | 495 | 1 | 0.52 | 2.02 |
| `03_200-499_lines` | 438 | 150,059 | 2,935 | 10 | 0.67 | 3.41 |
| `04_500+_lines` | 213 | 130,385 | 2,169 | 6 | 0.46 | 2.77 |

## 5. Complexity Bucket: By Import Count

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `01_1-3_imports` | 696 | 248,464 | 4,729 | 16 | 0.64 | 3.38 |
| `02_4-8_imports` | 107 | 51,438 | 883 | 1 | 0.19 | 1.13 |

## 6. Breakdown: By Top-Level Module

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `(root)` | 2 | 19 | 4 | 0 | 0.00 | 0.00 |
| `Lib` | 495 | 177,492 | 3,576 | 10 | 0.56 | 2.80 |
| `New` | 306 | 122,391 | 2,032 | 7 | 0.57 | 3.44 |
