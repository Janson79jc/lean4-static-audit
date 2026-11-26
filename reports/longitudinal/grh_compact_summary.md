# Lean 4 Static Corpus Audit Report (grh_compact)

- **Corpus**: `corpus/grh-lean/grh-compact/src` | **Toolchain**: `leanprover/lean4:v4.35.0` | **Archive SHA256**: `9631b4f02019` | **Probe SHA256**: `43501e2c8041`
- **Files**: `794` | **Raw lines**: `112,827` | **Non-empty code lines**: `76,149`
- **Speed**: `16,992 lines/sec` (glob `0.04s`, scan `6.64s`, total `7.54s`)
- **Top-Level (Column-0) Declarations**: `definitions = 3,855` | `theorems/lemmas = 7,088` (standalone `by trivial = 0`, `rfl = 119`)

## 1. Definition-Layer Syntactic Pattern Counts

| Pattern Rule | Count |
|---|---:|
| `DEF_EXPLICIT_WILDCARD_PARAM` | 14 |
| *(Info)* `THM_STMT_FUN_TRUE` (theorem signature) | 0 |

## 2. Trust-Boundary & Metaprogramming Primitives

- Trust-boundary primitives: `{}`
- Metaprogramming primitives: `{}`

## 3. Clone Decomposition (Exact vs Type-2 Parameterized Identifier Normalization, Shim vs Substantive)

| Mode | Layer | Eligible Decls | Clusters | Redundant Dup Decls | Dup Rate |
|---|---|---:|---:|---:|---:|
| Exact-Token (>=8) | definition | 2,370 | 1 | 1 | 0.04% |
| Exact-Token (>=8) | proof | 5,716 | 0 | 0 | 0.0% |
| Exact-Token (>=8) | proof_shim | 0 | 0 | 0 | 0.0% |
| Exact-Token (>=8) | proof_substantive | 5,716 | 0 | 0 | 0.0% |
| Type-2 Total (>=8) | definition | 2,370 | 34 | 50 | 2.11% |
| Type-2 Total (>=8) | proof | 5,716 | 93 | 236 | 4.13% |
| Type-2 Total (>=8) | proof_shim | 0 | 0 | 0 | 0.0% |
| Type-2 Total (>=8) | proof_substantive | 5,716 | 93 | 236 | 4.13% |
| Type-2 Short (8-19) | definition | 1,034 | 33 | 49 | 4.74% |
| Type-2 Short (8-19) | proof | 1,564 | 92 | 235 | 15.03% |
| Type-2 Short (8-19) | proof_shim | 0 | 0 | 0 | 0.0% |
| Type-2 Short (8-19) | proof_substantive | 1,564 | 92 | 235 | 15.03% |
| Type-2 Substantive (>=20) | definition | 1,336 | 1 | 1 | 0.07% |
| Type-2 Substantive (>=20) | proof | 4,152 | 1 | 1 | 0.02% |
| Type-2 Substantive (>=20) | proof_shim | 0 | 0 | 0 | 0.0% |
| Type-2 Substantive (>=20) | proof_substantive | 4,152 | 1 | 1 | 0.02% |

- Cross-bucket hash collisions (`proof_total - proof_shim - proof_substantive`): `Type-2 Total = 0` (`8-19 tokens = 0`, `>=20 tokens = 0`)

## 4. Complexity Bucket: By Non-Empty Code Lines

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `01_<50_lines` | 224 | 6,666 | 490 | 0 | 0.00 | 0.00 |
| `02_50-199_lines` | 509 | 53,435 | 2,824 | 12 | 2.25 | 4.25 |
| `03_200-499_lines` | 61 | 16,048 | 541 | 2 | 1.25 | 3.70 |

## 5. Complexity Bucket: By Import Count

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `01_1-3_imports` | 749 | 69,751 | 3,613 | 13 | 1.86 | 3.60 |
| `02_4-8_imports` | 45 | 6,398 | 242 | 1 | 1.56 | 4.13 |

## 6. Breakdown: By Top-Level Module

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `(root)` | 2 | 19 | 4 | 0 | 0.00 | 0.00 |
| `Lib` | 573 | 51,280 | 2,812 | 10 | 1.95 | 3.56 |
| `New` | 219 | 24,850 | 1,039 | 4 | 1.61 | 3.85 |
