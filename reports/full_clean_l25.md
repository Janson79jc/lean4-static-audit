# Lean 4 Extended Trust-Boundary & Dual-Pattern Audit (full_clean_l25)

- **Files scanned**: `175,187` in `478.97s` | **Probe SHA256**: `43501e2c8041`

## 1. Extended Trust-Boundary & Kernel-Bypass Primitives

| Primitive | Count |
|---|---:|
| `debug_skipKernelTC` | 0 |
| `csimp_attr` | 0 |
| `trustCompiler` | 0 |
| `env_addDecl` | 2 |
| `env_addAndCompile` | 0 |
| `env_modifyEnv` | 5 |
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

## 2. Metaprogramming & Command Inventory (`34` distinct `run_tac`/`liftMetaTactic`/`partial` locations = `64` raw hits; `7` env mutation calls)

- `liftMetaTactic`: `30`
- `partial_def`: `2`
- `run_tac`: `32`
- `run_cmd`: `5`
- `elab_decl`: `4`
- `macro_decl`: `87`
- `initialize_decl`: `0`
- `import_lean_meta`: `12`

## 3. Logical Duals, Dummy Witnesses & Shadowing

| Rule | Count |
|---|---:|
| `DEF_PARAM_DUMMY_CONST_OR_DEFAULT` | 17 |
| `DEF_CONST_FALSE` | 1 |
| `DEF_FUN_FALSE` | 1 |
| `DEF_SYMBOL_SHADOWING` | 8 |

### Samples: `DEF_CONST_FALSE` (1)

- `Development/AutomorphicArithmetic/Foundations/UnitarySphericalFixing/SatakeParameters/SwOn.lean:3` (`UpperTheory.One.M.Sw`): `def UpperTheory.One.M.Sw : Prop := False`

### Samples: `DEF_FUN_FALSE` (1)

- `Formalism/LocalToGlobal/Divisibility/JetBounds/IsExpansion.lean:81` (`noQ`): `def noQ (l : ℕ) [Fact l.Prime] : OrbSys ℂ_[l] → ℝ → Prop := fun _ _ => False`

### Samples: `DEF_PARAM_DUMMY_CONST_OR_DEFAULT` (17)

- `Development/AbelianVarietyTheory/BlockTheory/ExistenceTori/ConjugateFieldNorm.lean:253` (`frI`): `def frI (_Q : CorePar F R) : FractionalIdeal (nonZeroDivisors (𝓞 E)) E := 1`
- `Development/AbelianVarietyTheory/Definitions/Divisors/AdelicAdmissibleSmul.lean:21` (`J₁`): `def J₁ (K : Type) [Field K] : Matrix Unit Unit (K × K) := 1`
- `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LiftToGlobalDescentData.lean:12` (`NTiedGPlaceholder.liftToGlobalDescentData`): `def NTiedGPlaceholder.liftToGlobalDescentData {D : D7} (_T : NormalizedHeckeDataPlaceholder D) : NTiedGPlaceholder D := ⟨⟩`
- `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ShortExactMulPrimeZmodTensorComplex.lean:63` (`oneZ`): `def oneZ (p : ℕ) : zmodOverInt p := (1 : ZMod p)`
- `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExponentAndTwistData.lean:457` (`twDelT`): `def twDelT (i : T.Tw) (j : ℕ) (b : Bool) (Q : Finset (PlE D.host)) (M : ℕ) :     FmT D T S i j b →ₗ[T.O i] FmT D T S i j b ⊗[T.O i] AddMonoidAlgebra (T.O i) (DelQM D.host (T.l i) Q`
- `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExponentAndTwistData.lean:460` (`eHT`): `def eHT (i : T.Tw) (j : ℕ) (b : Bool) : Module.End (FractionRing (T.O i)) (FmT D T S i j b) := 1`
- `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/FiniteDoubleCosetsDefiniteUnitaryMaximalLevel.lean:69` (`Jn`): `abbrev Jn (n : ℕ) : Matrix (Fin n) (Fin n) L := 1`
- `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SecondStepNoFormsOutsideLiftRange.lean:204` (`twDelC`): `def twDelC (i : D.ntw.Tw) (j : ℕ) (b : Bool) (Q : Finset (PlE D.host)) (M : ℕ) :     FmC D i j b →ₗ[D.ntw.O i] (FmC D i j b ⊗[D.ntw.O i] AddMonoidAlgebra (D.ntw.O i) (DelQM D.host `
- `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/SecondStepNoFormsOutsideLiftRange.lean:207` (`thPC`): `def thPC (i : D.ntw.Tw) (j : ℕ) (b : Bool) (k : ℕ) (Q : Finset (PlE D.host))     (ψ : Formalism.ConjugateSelfDual.G D.host.E D.nd.Om →* (D.ntw.Ok i k)ˣ) :`
- `Formalism/LocalRingCardinality/SpanPowerMembership/ExampleWeightMiddleEntries.lean:327` (`jZero`): `def jZero (embLL : K →+* ℂ) : (zeroHLat K).V →ₛₗ[embLL] Z0 := 0`
- `Formalism/LocalRingCardinality/SpanPowerMembership/NZTypeH.lean:60` (`zL`): `def zL (k : Fin 2) : GL (Fin R.r) (ZMod (H.g k)) := -1`
- `Formalism/LocalToGlobal/Columns/ReferenceActionRationalLevels.lean:657` (`ScNum.CY`): `def ScNum.CY (_ : ScNum) : ℝ := 9`
- `Formalism/LocalToGlobal/Divisibility/Tuples.lean:120` (`mu0`): `def mu0 (S : Set ℕ) : Tup F E L S := 1`
- `Formalism/LocalToGlobal/ProjectiveLattices/CuspidalL2Subspace.lean:52` (`frI`): `def frI (_T : Core D) : FractionalIdeal (nonZeroDivisors (𝓞 D.host.E)) D.host.E := 1`
- `Formalism/SharpRestriction/CuspSpanNormBounds/LatticeGluingRadicals.lean:8265` (`k_O`): `abbrev k_O (E : Type) [Field E] [NumberField E] : Submodule (𝓞 E) E := 1`
- `Formalism/SharpRestriction/InertJacobiLevels/HostFam.lean:243` (`Arith.QS`): `abbrev Arith.QS {B N : ℕ} (_ : Arith B N) : ℕ := 16`
- `PositivityTheory/AutomorphicForms/PublishedInputs/HilbertEisenstein/SSmooth.lean:52` (`w0`): `def w0 (F : Type) [Field F] [NumberField F] : InfinitePlace F := Classical.arbitrary _`

### Symbol Shadowing Hits

- `Development/AutomorphicArithmetic/DedekindLFunctions/CharFamily.lean:38` (`def ZeroFree`): `def ZeroFree (F : CharFamily) (θ : ℝ) : Prop :=   ∀ i, ∀ s : ℂ, θ < s.re → DirichletCharacter.LFunction (F.χ i) s ≠ 0`
- `Development/AutomorphicArithmetic/DedekindLFunctions/RunBaseDimensionLeRankAddGenusTerm.lean:159` (`def ZeroFree`): `def ZeroFree (θ : ℝ) : Prop := ∀ ξ ∈ T.KEPT, ∀ s : ℂ, θ < s.re → ξ.L s ≠ 0`
- `GroundTheory/AutomorphicForms/GL2/GJLocalZeta.lean:431` (`def LFunction`): `def LFunction (s : ℂ) : ℂ :=   ((LPolynomial π).eval (qs F s))⁻¹`
- `GroundTheory/GlobalFields/TateThesis/HeckeLFunction.lean:363` (`def LFunction`): `def LFunction (s : ℂ) : ℂ :=   LSeries χ.LCoeff s`
- `Statements.lean:3` (`def RiemannZetaZerosOnLine`): `def RiemannZetaZerosOnLine : Prop :=   ∀ s : ℂ, riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * ((n : ℂ) + 1)) → s ≠ 1 → s.re = 1 / 2`
- `Statements.lean:6` (`def DirichletLNonvanishingRightOfHalf`): `def DirichletLNonvanishingRightOfHalf : Prop :=   ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),`
- `Statements.lean:10` (`def DirichletLZerosOnLine`): `def DirichletLZerosOnLine : Prop :=   ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),`
- `Statements.lean:14` (`def PrimitiveDirichletLZerosOnLine`): `def PrimitiveDirichletLZerosOnLine : Prop :=   ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N), χ.IsPrimitive →`
