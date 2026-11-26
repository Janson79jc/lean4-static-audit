# Lean 4 Extended Trust-Boundary & Dual-Pattern Audit (grh_readable_l25)

- **Files scanned**: `803` in `28.64s` | **Probe SHA256**: `43501e2c8041`

## 1. Extended Trust-Boundary & Kernel-Bypass Primitives

| Primitive | Count |
|---|---:|
| `debug_skipKernelTC` | 0 |
| `csimp_attr` | 0 |
| `trustCompiler` | 0 |
| `env_addDecl` | 0 |
| `env_addAndCompile` | 0 |
| `env_modifyEnv` | 0 |
| `env_setEnv` | 0 |
| `sorry` | 0 |
| `admit` | 0 |
| `sorryAx` | 0 |
| `mkSorry` | 0 |
| `native_decide` | 0 |
| `ofReduceBool` | 0 |
| `ofReduceNat` | 0 |
| `implemented_by` | 0 |
| `extern_attr` | 0 |
| `unsafe_kw` | 0 |
| `axiom_decl` | 0 |
| `opaque_decl` | 0 |

## 2. Metaprogramming & Command Inventory (`0` distinct `run_tac`/`liftMetaTactic`/`partial` locations = `0` raw hits; `0` env mutation calls)

- `run_cmd`: `0`
- `elab_decl`: `0`
- `macro_decl`: `0`
- `initialize_decl`: `0`
- `import_lean_meta`: `0`

## 3. Logical Duals, Dummy Witnesses & Shadowing

| Rule | Count |
|---|---:|
| `DEF_SYMBOL_SHADOWING` | 4 |

### Symbol Shadowing Hits

- `Statements.lean:3` (`def RiemannZetaZerosOnLine`): `def RiemannZetaZerosOnLine : Prop :=   ∀ s : ℂ, riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * ((n : ℂ) + 1)) → s ≠ 1 → s.re = 1 / 2`
- `Statements.lean:6` (`def DirichletLNonvanishingRightOfHalf`): `def DirichletLNonvanishingRightOfHalf : Prop :=   ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),`
- `Statements.lean:10` (`def DirichletLZerosOnLine`): `def DirichletLZerosOnLine : Prop :=   ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),`
- `Statements.lean:14` (`def PrimitiveDirichletLZerosOnLine`): `def PrimitiveDirichletLZerosOnLine : Prop :=   ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N), χ.IsPrimitive →`
