# Lean 4 Static Corpus Audit Report (full_clean)

- **Corpus**: `corpus/lean/src` | **Toolchain**: `leanprover/lean4:v4.33.1` | **Archive SHA256**: `9631b4f02019` | **Probe SHA256**: `43501e2c8041`
- **Files**: `175,187` | **Raw lines**: `17,374,215` | **Non-empty code lines**: `15,531,759`
- **Speed**: `40,384 lines/sec` (glob `6.62s`, scan `430.22s`, total `459.33s`)
- **Top-Level (Column-0) Declarations**: `definitions = 242,670` | `theorems/lemmas = 818,755` (standalone `by trivial = 0`, `rfl = 20,023`)

## 1. Definition-Layer Syntactic Pattern Counts

| Pattern Rule | Count |
|---|---:|
| `DEF_UNUSED_EXPLICIT_UNDERSCORE_PARAM` | 881 |
| `DEF_UNUSED_EXPLICIT_NAMED_PARAM` | 210 |
| `DEF_SINGLEARG_FUN_TRUE` | 162 |
| `DEF_EXPLICIT_WILDCARD_PARAM` | 77 |
| `DEF_MULTIARG_FUN_TRUE` | 54 |
| `DEF_FUN_TRUE` | 9 |
| `DEF_CONST_TRUE` | 8 |
| `DEF_TRIVIAL_STUB` | 2 |
| *(Info)* `THM_STMT_FUN_TRUE` (theorem signature) | 1,218 |

## 2. Trust-Boundary & Metaprogramming Primitives

- Trust-boundary primitives: `{'partial_def': 2}`
- Metaprogramming primitives: `{'run_tac': 32, 'liftMetaTactic': 30}`

## 3. Clone Decomposition (Exact vs Type-2 Parameterized Identifier Normalization, Shim vs Substantive)

| Mode | Layer | Eligible Decls | Clusters | Redundant Dup Decls | Dup Rate |
|---|---|---:|---:|---:|---:|
| Exact-Token (>=8) | definition | 204,234 | 7,767 | 10,646 | 5.21% |
| Exact-Token (>=8) | proof | 734,084 | 22,941 | 33,184 | 4.52% |
| Exact-Token (>=8) | proof_shim | 50,682 | 146 | 170 | 0.34% |
| Exact-Token (>=8) | proof_substantive | 683,402 | 22,795 | 33,014 | 4.83% |
| Type-2 Total (>=8) | definition | 204,234 | 15,544 | 33,294 | 16.3% |
| Type-2 Total (>=8) | proof | 734,084 | 35,921 | 150,567 | 20.51% |
| Type-2 Total (>=8) | proof_shim | 50,682 | 277 | 48,791 | 96.27% |
| Type-2 Total (>=8) | proof_substantive | 683,402 | 35,644 | 101,776 | 14.89% |
| Type-2 Short (8-19) | definition | 54,364 | 6,778 | 20,792 | 38.25% |
| Type-2 Short (8-19) | proof | 114,015 | 11,725 | 66,264 | 58.12% |
| Type-2 Short (8-19) | proof_shim | 1,887 | 190 | 979 | 51.88% |
| Type-2 Short (8-19) | proof_substantive | 112,128 | 11,535 | 65,285 | 58.22% |
| Type-2 Substantive (>=20) | definition | 149,870 | 8,766 | 12,502 | 8.34% |
| Type-2 Substantive (>=20) | proof | 620,069 | 24,196 | 84,303 | 13.6% |
| Type-2 Substantive (>=20) | proof_shim | 48,795 | 87 | 47,812 | 97.99% |
| Type-2 Substantive (>=20) | proof_substantive | 571,274 | 24,109 | 36,491 | 6.39% |

- Cross-bucket hash collisions (`proof_total - proof_shim - proof_substantive`): `Type-2 Total = 0` (`8-19 tokens = 0`, `>=20 tokens = 0`)

## 4. Complexity Bucket: By Non-Empty Code Lines

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `01_<50_lines` | 85,891 | 1,711,258 | 27,881 | 86 | 0.50 | 3.08 |
| `02_50-199_lines` | 69,936 | 7,381,196 | 114,941 | 535 | 0.72 | 4.65 |
| `03_200-499_lines` | 17,618 | 5,023,991 | 74,048 | 485 | 0.97 | 6.55 |
| `04_500+_lines` | 1,742 | 1,415,314 | 25,800 | 297 | 2.10 | 11.51 |

## 5. Complexity Bucket: By Import Count

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `01_1-3_imports` | 74,694 | 6,538,354 | 142,647 | 528 | 0.81 | 3.70 |
| `02_4-8_imports` | 74,203 | 5,725,358 | 78,159 | 658 | 1.15 | 8.42 |
| `03_9-15_imports` | 21,020 | 2,349,282 | 17,250 | 192 | 0.82 | 11.13 |
| `04_16+_imports` | 5,270 | 918,765 | 4,614 | 25 | 0.27 | 5.42 |

## 6. Breakdown: By Top-Level Module

| Bucket | Files | Code Lines | Defs | Findings | Hits / 10k Code Lines | Hits / 1k Defs |
|---|---:|---:|---:|---:|---:|---:|
| `(root)` | 2 | 19 | 4 | 0 | 0.00 | 0.00 |
| `BuildAid` | 5 | 15 | 0 | 0 | 0.00 | 0.00 |
| `CompanionTheory` | 2,027 | 173,982 | 2,356 | 3 | 0.17 | 1.27 |
| `Development` | 141,928 | 11,050,038 | 130,664 | 457 | 0.41 | 3.50 |
| `Formalism` | 18,254 | 2,789,976 | 77,981 | 892 | 3.20 | 11.44 |
| `GroundTheory` | 8,507 | 963,283 | 20,891 | 42 | 0.44 | 2.01 |
| `Lemmata` | 167 | 8,561 | 6 | 0 | 0.00 | 0.00 |
| `PositivityTheory` | 449 | 47,696 | 2,044 | 3 | 0.63 | 1.47 |
| `ReciprocityTheory` | 3,845 | 498,172 | 8,724 | 6 | 0.12 | 0.69 |
| `Supplements` | 3 | 17 | 0 | 0 | 0.00 | 0.00 |
