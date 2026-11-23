# Lean 4 Import DAG & Reachability Report (full_clean)

- **Elapsed**: `3.68s` | **Primary Entry**: `Main` (`entry_roots=['Main', 'Statements', 'Supplements.Kernels.MainTheoremsAll', 'Supplements.Kernels.MainTheorems']`)
- **Total Project Files**: `175,187` | **Reachable**: `175,187` (`100.0%`) | **Unimported**: `0` (`0.0%`)
- **Total Code Lines**: `15,531,759` | **Reachable**: `15,531,759` (`100.0%`) | **Unimported**: `0` (`0.0%`)

## 1. Reachability by Top-Level Module

| Top Dir | Total Files | Reachable Files | Unimported Files | Total Code Lines | Unimported Lines | Unimported % |
|---|---:|---:|---:|---:|---:|---:|
| `(root)` | 2 | 2 | 0 | 19 | 0 | 0.00% |
| `BuildAid` | 5 | 5 | 0 | 15 | 0 | 0.00% |
| `CompanionTheory` | 2,027 | 2,027 | 0 | 173,982 | 0 | 0.00% |
| `Development` | 141,928 | 141,928 | 0 | 11,050,038 | 0 | 0.00% |
| `Formalism` | 18,254 | 18,254 | 0 | 2,789,976 | 0 | 0.00% |
| `GroundTheory` | 8,507 | 8,507 | 0 | 963,283 | 0 | 0.00% |
| `Lemmata` | 167 | 167 | 0 | 8,561 | 0 | 0.00% |
| `PositivityTheory` | 449 | 449 | 0 | 47,696 | 0 | 0.00% |
| `ReciprocityTheory` | 3,845 | 3,845 | 0 | 498,172 | 0 | 0.00% |
| `Supplements` | 3 | 3 | 0 | 17 | 0 | 0.00% |

## 2. Definition-Layer Pattern Findings: Inside Entry Cone vs Outside Cone

| Rule | Total | In Entry Cone | Outside Cone |
|---|---:|---:|---:|
| `DEF_CONST_TRUE` | 8 | 8 | 0 |
| `DEF_EXPLICIT_WILDCARD_PARAM` | 77 | 77 | 0 |
| `DEF_FUN_TRUE` | 9 | 9 | 0 |
| `DEF_MULTIARG_FUN_TRUE` | 54 | 54 | 0 |
| `DEF_SINGLEARG_FUN_TRUE` | 162 | 162 | 0 |
| `DEF_TRIVIAL_STUB` | 2 | 2 | 0 |
| `DEF_UNUSED_EXPLICIT_NAMED_PARAM` | 210 | 210 | 0 |
| `DEF_UNUSED_EXPLICIT_UNDERSCORE_PARAM` | 881 | 881 | 0 |
