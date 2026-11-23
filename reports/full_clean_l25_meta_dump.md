# Meta & Partial Context Dump (64 raw primitive hits / 34 distinct locations in 175,187 files)

## 1. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsBoundAbsLocalLatticeCompletionEntries.lean:12`
```lean
    8: theorem absFin_latLoc_le : ∀ {F E : Type} [Field F] [NumberField F] [Field E] [NumberField E] [Algebra F E] {n : ℕ}
    9:     (L : Submodule (𝓞 E) (Fin n → E)) [Submodule.IsLattice E L] (v : HeightOneSpectrum (𝓞 F)),
   10:     ∃ C : ℝ≥0, ∀ y ∈ latLoc F L v, ∀ i, absFin F v (y i) ≤ C := by
   11:   first
   12:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   13:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   14:   | exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   15:   | exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   16:   | (apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   17:   | (intros; apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   18:   | (intros; apply @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> first | assumption | infer_instance)
   19:   | (intros; exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc ..)
   20: 
```

## 2. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsBoundAbsLocalLatticeCompletionEntries.lean:13`
```lean
    9:     (L : Submodule (𝓞 E) (Fin n → E)) [Submodule.IsLattice E L] (v : HeightOneSpectrum (𝓞 F)),
   10:     ∃ C : ℝ≥0, ∀ y ∈ latLoc F L v, ∀ i, absFin F v (y i) ≤ C := by
   11:   first
   12:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   13:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   14:   | exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   15:   | exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   16:   | (apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   17:   | (intros; apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   18:   | (intros; apply @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> first | assumption | infer_instance)
   19:   | (intros; exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc ..)
   20: 
   21: example : ∀ {F E : Type} [Field F] [NumberField F] [Field E] [NumberField E] [Algebra F E] {n : ℕ} (L : Submodule (𝓞 E) (Fin n → E)) [Submodule.IsLattice E L] (v : HeightOneSpectrum (𝓞 F)), ∃ C : ℝ≥0, ∀ y ∈ latLoc F L v, ∀ i, absFin F v (y i) ≤ C := @absFin_latLoc_le
```

## 3. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/BoundedPowerSeriesEvaluationDivisibility.lean:24`
```lean
   20:   GlobalTheory.BoundedPowerSeriesDisc.evalBounded π h
   21: 
   22: theorem main : ∀ (C : Type) [NontriviallyNormedField C] [IsUltrametricDist C] [CompleteSpace C] (π : C), ‖π‖ < 1 → ∃ (B : Subring (PowerSeries C)) (ev : B →+* C) (t : B), (∀ Φ, Φ ∈ B ↔ ∃ b : ℝ, ∀ n, ‖PowerSeries.coeff n Φ‖ ≤ b) ∧ (∀ Φ : B, ev Φ = ∑' n, PowerSeries.coeff n (Φ : PowerSeries C) * π ^ n) ∧ t ≠ 0 ∧ (∀ Φ, ev Φ = 0 ↔ t ∣ Φ) ∧ ∀ Φ : B, Φ ≠ 0 → ∃ n : ℕ, ¬ t ^ n ∣ Φ := by
   23:   first
   24:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SummableSeriesBounds.main
   25:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SummableSeriesBounds.main
   26:   | exact @_root_.GlobalTheory.SummableSeriesBounds.main
   27:   | exact _root_.GlobalTheory.SummableSeriesBounds.main
   28:   | (apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   29:   | (intros; apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   30:   | (intros; apply @_root_.GlobalTheory.SummableSeriesBounds.main <;> first | assumption | infer_instance)
   31:   | (intros; exact _root_.GlobalTheory.SummableSeriesBounds.main ..)
   32: 
```

## 4. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/BoundedPowerSeriesEvaluationDivisibility.lean:25`
```lean
   21: 
   22: theorem main : ∀ (C : Type) [NontriviallyNormedField C] [IsUltrametricDist C] [CompleteSpace C] (π : C), ‖π‖ < 1 → ∃ (B : Subring (PowerSeries C)) (ev : B →+* C) (t : B), (∀ Φ, Φ ∈ B ↔ ∃ b : ℝ, ∀ n, ‖PowerSeries.coeff n Φ‖ ≤ b) ∧ (∀ Φ : B, ev Φ = ∑' n, PowerSeries.coeff n (Φ : PowerSeries C) * π ^ n) ∧ t ≠ 0 ∧ (∀ Φ, ev Φ = 0 ↔ t ∣ Φ) ∧ ∀ Φ : B, Φ ≠ 0 → ∃ n : ℕ, ¬ t ^ n ∣ Φ := by
   23:   first
   24:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SummableSeriesBounds.main
   25:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SummableSeriesBounds.main
   26:   | exact @_root_.GlobalTheory.SummableSeriesBounds.main
   27:   | exact _root_.GlobalTheory.SummableSeriesBounds.main
   28:   | (apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   29:   | (intros; apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   30:   | (intros; apply @_root_.GlobalTheory.SummableSeriesBounds.main <;> first | assumption | infer_instance)
   31:   | (intros; exact _root_.GlobalTheory.SummableSeriesBounds.main ..)
   32: 
   33: end GlobalTheory.MBLow.BddPS
```

## 5. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsJetExtensionSquareZero.lean:22`
```lean
   18:     ∃ χ : K.jet k ⟶ T, χ.deg = f₁.deg ∧ jet0 k ≫ χ = f₁ ∧ jet1 k ≫ χ = f₂ ∧
   19:       ∀ x : TrivSqZeroExt (Hol (K.W k)) (Fin g → Hol (K.W k)),
   20:         χ.φ x = f₁.φ (x.fst : Hol (K.W k)) + ∑ a, f₁.φ (x.snd a : Hol (K.W k)) * n a := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   24:   | exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   25:   | exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   26:   | (apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet ..)
   30: 
```

## 6. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsJetExtensionSquareZero.lean:23`
```lean
   19:       ∀ x : TrivSqZeroExt (Hol (K.W k)) (Fin g → Hol (K.W k)),
   20:         χ.φ x = f₁.φ (x.fst : Hol (K.W k)) + ∑ a, f₁.φ (x.snd a : Hol (K.W k)) * n a := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   24:   | exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   25:   | exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   26:   | (apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet ..)
   30: 
   31: end GlobalTheory.AnPer.Charts
```

## 7. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRootMapMinpolyIffExistsRingHomExtension.lean:10`
```lean
    6: theorem exists_ringHom_extension_algClosed_of_isIntegral_injective {R S K : Type*} [CommRing R] [CommRing S] [Field K] [IsAlgClosed K]
    7:     [Algebra R S] [Algebra.IsIntegral R S] (hinj : Function.Injective (algebraMap R S))
    8:     (ψ : R →+* K) : ∃ x : S →+* K, x.comp (algebraMap R S) = ψ := by
    9:   first
   10:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   11:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   12:   | exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   13:   | exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   14:   | (apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   15:   | (intros; apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   16:   | (intros; apply @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> first | assumption | infer_instance)
   17:   | (intros; exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq ..)
   18: 
```

## 8. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRootMapMinpolyIffExistsRingHomExtension.lean:11`
```lean
    7:     [Algebra R S] [Algebra.IsIntegral R S] (hinj : Function.Injective (algebraMap R S))
    8:     (ψ : R →+* K) : ∃ x : S →+* K, x.comp (algebraMap R S) = ψ := by
    9:   first
   10:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   11:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   12:   | exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   13:   | exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   14:   | (apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   15:   | (intros; apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   16:   | (intros; apply @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> first | assumption | infer_instance)
   17:   | (intros; exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq ..)
   18: 
   19: theorem isRoot_map_minpoly_iff_exists_ringHom : ∀ (A B : Type) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [CommRing B] [IsDomain B] [Algebra A B] [Algebra.IsIntegral A B], Function.Injective (algebraMap A B) → ∀ (g : B) (φ : A →+* ℂ) (z : ℂ), ((minpoly A g).map φ).IsRoot z ↔ ∃ x : B →+* ℂ, x.comp (algebraMap A B) = φ ∧ x g = z := by
```

## 9. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:38`
```lean
   34:     (hA : Aα.comp (algebraMap R₀ LR) = (algebraMap B₀ LB).comp α)
   35:     (hK : Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ) :
   36:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   37:   first
   38:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   39:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   40:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   41:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   42:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   43:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   44:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   45:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   46: 
```

## 10. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:39`
```lean
   35:     (hK : Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ) :
   36:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   37:   first
   38:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   39:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   40:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   41:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   42:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   43:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   44:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   45:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   46: 
   47: theorem locPullback : ∀ {A R₀ A' B₀ : Type} [CommRing A] [CommRing R₀] [CommRing A'] [CommRing B₀]
```

## 11. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:61`
```lean
   57:     Aα.comp (algebraMap R₀ LR) = (algebraMap B₀ LB).comp α →
   58:     Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ →
   59:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   60:   first
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   62:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   63:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   64:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   65:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   66:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   67:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   68:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   69: 
```

## 12. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:62`
```lean
   58:     Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ →
   59:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   60:   first
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   62:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   63:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   64:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   65:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   66:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   67:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   68:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   69: 
   70: end GlobalTheory
```

## 13. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/MatchedDiffsInvariantSubspace.lean:31`
```lean
   27: 
   28: theorem gen_stable {ρ : ι → V →ₗ[ℂ] V} {N : Submodule ℂ V} (hN : ∀ y, ∀ x ∈ N, ρ y x ∈ N)
   29:     {s : Module.End ℂ V} (hs : s ∈ gen ρ) : ∀ x ∈ N, s x ∈ N := by
   30:   first
   31:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   32:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SpectralLemmaFirst.main
   33:   | exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   34:   | exact _root_.GlobalTheory.SpectralLemmaFirst.main
   35:   | (apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   36:   | (intros; apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   37:   | (intros; apply @_root_.GlobalTheory.SpectralLemmaFirst.main <;> first | assumption | infer_instance)
   38:   | (intros; exact _root_.GlobalTheory.SpectralLemmaFirst.main ..)
   39: 
```

## 14. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/MatchedDiffsInvariantSubspace.lean:32`
```lean
   28: theorem gen_stable {ρ : ι → V →ₗ[ℂ] V} {N : Submodule ℂ V} (hN : ∀ y, ∀ x ∈ N, ρ y x ∈ N)
   29:     {s : Module.End ℂ V} (hs : s ∈ gen ρ) : ∀ x ∈ N, s x ∈ N := by
   30:   first
   31:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   32:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SpectralLemmaFirst.main
   33:   | exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   34:   | exact _root_.GlobalTheory.SpectralLemmaFirst.main
   35:   | (apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   36:   | (intros; apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   37:   | (intros; apply @_root_.GlobalTheory.SpectralLemmaFirst.main <;> first | assumption | infer_instance)
   38:   | (intros; exact _root_.GlobalTheory.SpectralLemmaFirst.main ..)
   39: 
   40: def lift (ρ : ι → V →ₗ[ℂ] V) (N : Submodule ℂ V) (hN : ∀ y, ∀ x ∈ N, ρ y x ∈ N) : Submodule (gen ρ) V where
```

## 15. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BasedFlagPairLatticeContainment.lean:131`
```lean
  127: 
  128: theorem exists_nat_smul_mem (Λ : LV D) (hΛ : Submodule.IsLattice D.host.E Λ) (v : (VS D).V) :
  129:     ∃ n : ℕ, 0 < n ∧ (n : D.host.E) • v ∈ Λ := by
  130:   first
  131:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  132:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  133:   | exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  134:   | exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  135:   | (apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  136:   | (intros; apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  137:   | (intros; apply @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> first | assumption | infer_instance)
  138:   | (intros; exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem ..)
  139: 
```

## 16. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BasedFlagPairLatticeContainment.lean:132`
```lean
  128: theorem exists_nat_smul_mem (Λ : LV D) (hΛ : Submodule.IsLattice D.host.E Λ) (v : (VS D).V) :
  129:     ∃ n : ℕ, 0 < n ∧ (n : D.host.E) • v ∈ Λ := by
  130:   first
  131:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  132:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  133:   | exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  134:   | exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  135:   | (apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  136:   | (intros; apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  137:   | (intros; apply @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> first | assumption | infer_instance)
  138:   | (intros; exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem ..)
  139: 
  140: end GlobalTheory.CompScale
```

## 17. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/DetMatrixSandwichLinearMap.lean:14`
```lean
   10:     (L : (ι → Fin j → Fin j → ℂ) →ₗ[ℝ] (ι → Fin j → Fin j → ℂ))
   11:     (hL : ∀ h w, Matrix.of (L h w) = A w * Matrix.of (h w) * B w) :
   12:     LinearMap.det L = ∏ w, (‖(A w).det‖ ^ 2 * ‖(B w).det‖ ^ 2) ^ j := by
   13:   first
   14:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   15:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   16:   | exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   17:   | exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   18:   | (apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   19:   | (intros; apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   20:   | (intros; apply @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> first | assumption | infer_instance)
   21:   | (intros; exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family ..)
   22: 
```

## 18. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/DetMatrixSandwichLinearMap.lean:15`
```lean
   11:     (hL : ∀ h w, Matrix.of (L h w) = A w * Matrix.of (h w) * B w) :
   12:     LinearMap.det L = ∏ w, (‖(A w).det‖ ^ 2 * ‖(B w).det‖ ^ 2) ^ j := by
   13:   first
   14:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   15:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   16:   | exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   17:   | exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   18:   | (apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   19:   | (intros; apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   20:   | (intros; apply @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> first | assumption | infer_instance)
   21:   | (intros; exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family ..)
   22: 
   23: end GlobalTheory.MatMulDet
```

## 19. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/PowLePowRatio.lean:153`
```lean
  149: theorem span_inner {n : ℕ} (L M : Hn n →L[ℂ] Hn n) (s t : Set (Hn n))
  150:     (h : ∀ u ∈ s, ∀ z ∈ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0) :
  151:     ∀ u ∈ Submodule.span ℂ s, ∀ z ∈ Submodule.span ℂ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0 := by
  152:   first
  153:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  154:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InnerSumZeroSpan.main
  155:   | exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  156:   | exact _root_.GlobalTheory.InnerSumZeroSpan.main
  157:   | (apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  158:   | (intros; apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  159:   | (intros; apply @_root_.GlobalTheory.InnerSumZeroSpan.main <;> first | assumption | infer_instance)
  160:   | (intros; exact _root_.GlobalTheory.InnerSumZeroSpan.main ..)
  161: 
```

## 20. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/PowLePowRatio.lean:154`
```lean
  150:     (h : ∀ u ∈ s, ∀ z ∈ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0) :
  151:     ∀ u ∈ Submodule.span ℂ s, ∀ z ∈ Submodule.span ℂ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0 := by
  152:   first
  153:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  154:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InnerSumZeroSpan.main
  155:   | exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  156:   | exact _root_.GlobalTheory.InnerSumZeroSpan.main
  157:   | (apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  158:   | (intros; apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  159:   | (intros; apply @_root_.GlobalTheory.InnerSumZeroSpan.main <;> first | assumption | infer_instance)
  160:   | (intros; exact _root_.GlobalTheory.InnerSumZeroSpan.main ..)
  161: 
  162: theorem sp_orth (w : InfinitePlace I.E) {A B : Submodule (𝓞 I.E) (Fin I.n → I.E)}
```

## 21. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtTwistedPlaces.lean:60`
```lean
   56: 
   57: theorem exists_below_of_range (D D' : D7) (h : Set.range D.what₂.embLL ⊆ Set.range D'.what₂.embLL) (v' : D'.what₂.places.Pl) :
   58:     ∃ v : D.what₂.places.Pl, Below D D' v v' := by
   59:   first
   60:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.PrimeBelow.exists_below
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.PrimeBelow.exists_below
   62:   | exact @_root_.GlobalTheory.PrimeBelow.exists_below
   63:   | exact _root_.GlobalTheory.PrimeBelow.exists_below
   64:   | (apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   65:   | (intros; apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   66:   | (intros; apply @_root_.GlobalTheory.PrimeBelow.exists_below <;> first | assumption | infer_instance)
   67:   | (intros; exact _root_.GlobalTheory.PrimeBelow.exists_below ..)
   68: 
```

## 22. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtTwistedPlaces.lean:61`
```lean
   57: theorem exists_below_of_range (D D' : D7) (h : Set.range D.what₂.embLL ⊆ Set.range D'.what₂.embLL) (v' : D'.what₂.places.Pl) :
   58:     ∃ v : D.what₂.places.Pl, Below D D' v v' := by
   59:   first
   60:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.PrimeBelow.exists_below
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.PrimeBelow.exists_below
   62:   | exact @_root_.GlobalTheory.PrimeBelow.exists_below
   63:   | exact _root_.GlobalTheory.PrimeBelow.exists_below
   64:   | (apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   65:   | (intros; apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   66:   | (intros; apply @_root_.GlobalTheory.PrimeBelow.exists_below <;> first | assumption | infer_instance)
   67:   | (intros; exact _root_.GlobalTheory.PrimeBelow.exists_below ..)
   68: 
   69: theorem resChar_of_below {D D' : D7} {v : D.what₂.places.Pl} {v' : D'.what₂.places.Pl} (hB : Below D D' v v') :
```

## 23. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicLatticeSmulMemOfAgreeAwayFromPlace.lean:70`
```lean
   66: 
   67: theorem exists_nsmul_mem_of_mem_span {N : ℕ} (Lb : Submodule (𝓞 E) (Fin N → E)) {v : Fin N → E}
   68:     (hv : v ∈ Submodule.span E (Lb : Set (Fin N → E))) : ∃ n : ℕ, 0 < n ∧ n • v ∈ Lb := by
   69:   first
   70:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   71:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   72:   | exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   73:   | exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   74:   | (apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   75:   | (intros; apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   76:   | (intros; apply @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> first | assumption | infer_instance)
   77:   | (intros; exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem ..)
   78: 
```

## 24. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicLatticeSmulMemOfAgreeAwayFromPlace.lean:71`
```lean
   67: theorem exists_nsmul_mem_of_mem_span {N : ℕ} (Lb : Submodule (𝓞 E) (Fin N → E)) {v : Fin N → E}
   68:     (hv : v ∈ Submodule.span E (Lb : Set (Fin N → E))) : ∃ n : ℕ, 0 < n ∧ n • v ∈ Lb := by
   69:   first
   70:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   71:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   72:   | exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   73:   | exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   74:   | (apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   75:   | (intros; apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   76:   | (intros; apply @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> first | assumption | infer_instance)
   77:   | (intros; exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem ..)
   78: 
   79: end GlobalTheory.TwV.Xc
```

## 25. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/UnramifiedWeierstrassCurveTransformCoefficientsW.lean:20`
```lean
   16: variable {p : ℕ} [Fact p.Prime]
   17: 
   18: theorem inWf_of_kur {x : ℂ_[p]} (hx : x ∈ Formalism.L2.Th1.CM.MaximalUnramifiedExtension p) : InWf x := by
   19:   first
   20:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   21:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   22:   | exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   23:   | exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   24:   | (apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   25:   | (intros; apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   26:   | (intros; apply @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> first | assumption | infer_instance)
   27:   | (intros; exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur ..)
   28: 
```

## 26. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/UnramifiedWeierstrassCurveTransformCoefficientsW.lean:21`
```lean
   17: 
   18: theorem inWf_of_kur {x : ℂ_[p]} (hx : x ∈ Formalism.L2.Th1.CM.MaximalUnramifiedExtension p) : InWf x := by
   19:   first
   20:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   21:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   22:   | exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   23:   | exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   24:   | (apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   25:   | (intros; apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   26:   | (intros; apply @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> first | assumption | infer_instance)
   27:   | (intros; exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur ..)
   28: 
   29: theorem coefWf_phW_of_kur (W : WeierstrassCurve ℂ_[p]) (h1 : W.a₁ ∈ Formalism.L2.Th1.CM.MaximalUnramifiedExtension p)
```

## 27. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/ValuationRingModel.lean:206`
```lean
  202:   exact ⟨s, Finset.mem_insert_of_mem hs, hgs⟩
  203: 
  204: theorem res_algClosed [IsAlgClosed K] : IsAlgClosed (IsLocalRing.ResidueField O) := by
  205:   first
  206:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  207:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  208:   | exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  209:   | exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  210:   | (apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  211:   | (intros; apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  212:   | (intros; apply @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> first | assumption | infer_instance)
  213:   | (intros; exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField ..)
  214: 
```

## 28. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/ValuationRingModel.lean:207`
```lean
  203: 
  204: theorem res_algClosed [IsAlgClosed K] : IsAlgClosed (IsLocalRing.ResidueField O) := by
  205:   first
  206:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  207:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  208:   | exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  209:   | exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  210:   | (apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  211:   | (intros; apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  212:   | (intros; apply @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> first | assumption | infer_instance)
  213:   | (intros; exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField ..)
  214: 
  215: end Top
```

## 29. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/TwistedOperators/RelIndexTwoBlockParahoricConjTorusDiagElement.lean:22`
```lean
   18:     (((parahoric k A D).map (MulAut.conj (mtor (A := A) ϖ e)).toMonoidHom).relIndex (parahoric k A D) : ℝ) =
   19:       (resCard k : ℝ) ^ ((Fintype.card A : ℤ) * sumAbs e) *
   20:         (((KO k D).map (MulAut.conj (torusElt k D ϖ e)).toMonoidHom).relIndex (KO k D) : ℝ) := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   24:   | exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   25:   | exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   26:   | (apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric ..)
   30: 
```

## 30. [liftMetaTactic] `Development/AbelianVarietyTheory/Proofs/TwistedOperators/RelIndexTwoBlockParahoricConjTorusDiagElement.lean:23`
```lean
   19:       (resCard k : ℝ) ^ ((Fintype.card A : ℤ) * sumAbs e) *
   20:         (((KO k D).map (MulAut.conj (torusElt k D ϖ e)).toMonoidHom).relIndex (KO k D) : ℝ) := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   24:   | exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   25:   | exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   26:   | (apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric ..)
   30: 
   31: end GlobalTheory.ParIdx
```

## 31. [partial_def] `Formalism/HermitianCurvature/HermitianCurvatureProofs/CutCptCopy.lean:40`
```lean
   36:   | n => .str n "Cpt"
   37: 
   38: def proposals (ci : ConstantInfo) : Array Name :=
   39:   ci.type.getUsedConstants ++ ((ci.value? (allowOpaque := true)).map (·.getUsedConstants) |>.getD #[])
   40: 
   41: partial def go (env : Environment) (n : Name) (st : NameSet × NameSet × Array Name) : NameSet × NameSet × Array Name :=
   42:   let (seen, tainted, order) := st
   43:   if seen.contains n || terminal n then st else
   44:   let seen := seen.insert n
   45:   match env.find? n with
   46:   | none => (seen, tainted, order)
   47:   | some ci =>
   48:     let us := proposals ci
```

## 32. [partial_def] `Formalism/LocalToGlobal/NumberFieldFamilies/OwnStruct.lean:17`
```lean
   13:   | .error _ => return false
   14: 
   15: def ownStruct (env : Environment) (S : Name) : Bool :=
   16:   isStructure env S && (S.getRoot == `Formalism || [``And, ``Prod, ``PProd, ``Sigma, ``PSigma, ``Subtype, ``Iff].contains S)
   17: 
   18: partial def copyAt (probe : Bool) (e tgt : Expr) (path : String) (fuel : Nat) : StateT (Array String) MetaM Expr := do
   19:   let tgt ← instantiateMVars tgt
   20:   let srcTy ← instantiateMVars (← inferType e)
   21:   if srcTy == tgt then return e
   22:   if fuel = 0 then
   23:     modify (·.push path); return e
   24:   let env ← getEnv
   25: 
```

## 33. [run_tac] `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsBoundAbsLocalLatticeCompletionEntries.lean:12`
```lean
    8: theorem absFin_latLoc_le : ∀ {F E : Type} [Field F] [NumberField F] [Field E] [NumberField E] [Algebra F E] {n : ℕ}
    9:     (L : Submodule (𝓞 E) (Fin n → E)) [Submodule.IsLattice E L] (v : HeightOneSpectrum (𝓞 F)),
   10:     ∃ C : ℝ≥0, ∀ y ∈ latLoc F L v, ∀ i, absFin F v (y i) ≤ C := by
   11:   first
   12:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   13:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   14:   | exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   15:   | exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   16:   | (apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   17:   | (intros; apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   18:   | (intros; apply @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> first | assumption | infer_instance)
   19:   | (intros; exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc ..)
   20: 
```

## 34. [run_tac] `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsBoundAbsLocalLatticeCompletionEntries.lean:13`
```lean
    9:     (L : Submodule (𝓞 E) (Fin n → E)) [Submodule.IsLattice E L] (v : HeightOneSpectrum (𝓞 F)),
   10:     ∃ C : ℝ≥0, ∀ y ∈ latLoc F L v, ∀ i, absFin F v (y i) ≤ C := by
   11:   first
   12:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   13:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   14:   | exact @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   15:   | exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc
   16:   | (apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   17:   | (intros; apply _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> assumption)
   18:   | (intros; apply @_root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc <;> first | assumption | infer_instance)
   19:   | (intros; exact _root_.GlobalTheory.LocalLatticeBound.exists_bound_latLoc ..)
   20: 
   21: example : ∀ {F E : Type} [Field F] [NumberField F] [Field E] [NumberField E] [Algebra F E] {n : ℕ} (L : Submodule (𝓞 E) (Fin n → E)) [Submodule.IsLattice E L] (v : HeightOneSpectrum (𝓞 F)), ∃ C : ℝ≥0, ∀ y ∈ latLoc F L v, ∀ i, absFin F v (y i) ≤ C := @absFin_latLoc_le
```

## 35. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/BoundedPowerSeriesEvaluationDivisibility.lean:24`
```lean
   20:   GlobalTheory.BoundedPowerSeriesDisc.evalBounded π h
   21: 
   22: theorem main : ∀ (C : Type) [NontriviallyNormedField C] [IsUltrametricDist C] [CompleteSpace C] (π : C), ‖π‖ < 1 → ∃ (B : Subring (PowerSeries C)) (ev : B →+* C) (t : B), (∀ Φ, Φ ∈ B ↔ ∃ b : ℝ, ∀ n, ‖PowerSeries.coeff n Φ‖ ≤ b) ∧ (∀ Φ : B, ev Φ = ∑' n, PowerSeries.coeff n (Φ : PowerSeries C) * π ^ n) ∧ t ≠ 0 ∧ (∀ Φ, ev Φ = 0 ↔ t ∣ Φ) ∧ ∀ Φ : B, Φ ≠ 0 → ∃ n : ℕ, ¬ t ^ n ∣ Φ := by
   23:   first
   24:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SummableSeriesBounds.main
   25:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SummableSeriesBounds.main
   26:   | exact @_root_.GlobalTheory.SummableSeriesBounds.main
   27:   | exact _root_.GlobalTheory.SummableSeriesBounds.main
   28:   | (apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   29:   | (intros; apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   30:   | (intros; apply @_root_.GlobalTheory.SummableSeriesBounds.main <;> first | assumption | infer_instance)
   31:   | (intros; exact _root_.GlobalTheory.SummableSeriesBounds.main ..)
   32: 
```

## 36. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/BoundedPowerSeriesEvaluationDivisibility.lean:25`
```lean
   21: 
   22: theorem main : ∀ (C : Type) [NontriviallyNormedField C] [IsUltrametricDist C] [CompleteSpace C] (π : C), ‖π‖ < 1 → ∃ (B : Subring (PowerSeries C)) (ev : B →+* C) (t : B), (∀ Φ, Φ ∈ B ↔ ∃ b : ℝ, ∀ n, ‖PowerSeries.coeff n Φ‖ ≤ b) ∧ (∀ Φ : B, ev Φ = ∑' n, PowerSeries.coeff n (Φ : PowerSeries C) * π ^ n) ∧ t ≠ 0 ∧ (∀ Φ, ev Φ = 0 ↔ t ∣ Φ) ∧ ∀ Φ : B, Φ ≠ 0 → ∃ n : ℕ, ¬ t ^ n ∣ Φ := by
   23:   first
   24:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SummableSeriesBounds.main
   25:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SummableSeriesBounds.main
   26:   | exact @_root_.GlobalTheory.SummableSeriesBounds.main
   27:   | exact _root_.GlobalTheory.SummableSeriesBounds.main
   28:   | (apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   29:   | (intros; apply _root_.GlobalTheory.SummableSeriesBounds.main <;> assumption)
   30:   | (intros; apply @_root_.GlobalTheory.SummableSeriesBounds.main <;> first | assumption | infer_instance)
   31:   | (intros; exact _root_.GlobalTheory.SummableSeriesBounds.main ..)
   32: 
   33: end GlobalTheory.MBLow.BddPS
```

## 37. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsJetExtensionSquareZero.lean:22`
```lean
   18:     ∃ χ : K.jet k ⟶ T, χ.deg = f₁.deg ∧ jet0 k ≫ χ = f₁ ∧ jet1 k ≫ χ = f₂ ∧
   19:       ∀ x : TrivSqZeroExt (Hol (K.W k)) (Fin g → Hol (K.W k)),
   20:         χ.φ x = f₁.φ (x.fst : Hol (K.W k)) + ∑ a, f₁.φ (x.snd a : Hol (K.W k)) * n a := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   24:   | exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   25:   | exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   26:   | (apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet ..)
   30: 
```

## 38. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsJetExtensionSquareZero.lean:23`
```lean
   19:       ∀ x : TrivSqZeroExt (Hol (K.W k)) (Fin g → Hol (K.W k)),
   20:         χ.φ x = f₁.φ (x.fst : Hol (K.W k)) + ∑ a, f₁.φ (x.snd a : Hol (K.W k)) * n a := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   24:   | exact @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   25:   | exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet
   26:   | (apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.SquareLiftLemmas.exists_hom_jet ..)
   30: 
   31: end GlobalTheory.AnPer.Charts
```

## 39. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/FramesTildeGammaValues.lean:70`
```lean
   66:       Formalism.HermitianLatticesTheory.normAt (Pi.basisFun Xf.K (Fin ((A3.side3 Ps ψs Zs).nV A3.fam3.base3.μ0))) X0 v F ^ 2 := by
   67:   subst gEq
   68:   have hg : grp = (Pi.group : Group (G0 Xf.E Pr.vGs Rk.r)) := eq_of_heq hgrp
   69:   subst hg
   70:   run_tac do
   71:     let g ← Lean.Elab.Tactic.getMainGoal
   72:     let g' ← g.withContext do
   73:       let lctx ← Lean.getLCtx
   74:       let some fe := lctx.findFromUserName? `famEq | throwError "famEq"
   75:       let some fi := lctx.findFromUserName? `fin | throwError "fin"
   76:       let t ← Lean.instantiateMVars fe.type
   77:       let ty ← Lean.Meta.whnf (← Lean.Meta.inferType t.appArg!)
   78:       let inst := ty.getAppArgs[6]!
```

## 40. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRootMapMinpolyIffExistsRingHomExtension.lean:10`
```lean
    6: theorem exists_ringHom_extension_algClosed_of_isIntegral_injective {R S K : Type*} [CommRing R] [CommRing S] [Field K] [IsAlgClosed K]
    7:     [Algebra R S] [Algebra.IsIntegral R S] (hinj : Function.Injective (algebraMap R S))
    8:     (ψ : R →+* K) : ∃ x : S →+* K, x.comp (algebraMap R S) = ψ := by
    9:   first
   10:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   11:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   12:   | exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   13:   | exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   14:   | (apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   15:   | (intros; apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   16:   | (intros; apply @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> first | assumption | infer_instance)
   17:   | (intros; exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq ..)
   18: 
```

## 41. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsRootMapMinpolyIffExistsRingHomExtension.lean:11`
```lean
    7:     [Algebra R S] [Algebra.IsIntegral R S] (hinj : Function.Injective (algebraMap R S))
    8:     (ψ : R →+* K) : ∃ x : S →+* K, x.comp (algebraMap R S) = ψ := by
    9:   first
   10:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   11:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   12:   | exact @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   13:   | exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq
   14:   | (apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   15:   | (intros; apply _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> assumption)
   16:   | (intros; apply @_root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq <;> first | assumption | infer_instance)
   17:   | (intros; exact _root_.GlobalTheory.InjectiveAlgebraHomExistence.exists_ringHom_comp_algebraMap_eq ..)
   18: 
   19: theorem isRoot_map_minpoly_iff_exists_ringHom : ∀ (A B : Type) [CommRing A] [IsDomain A] [IsIntegrallyClosed A] [CommRing B] [IsDomain B] [Algebra A B] [Algebra.IsIntegral A B], Function.Injective (algebraMap A B) → ∀ (g : B) (φ : A →+* ℂ) (z : ℂ), ((minpoly A g).map φ).IsRoot z ↔ ∃ x : B →+* ℂ, x.comp (algebraMap A B) = φ ∧ x g = z := by
```

## 42. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:38`
```lean
   34:     (hA : Aα.comp (algebraMap R₀ LR) = (algebraMap B₀ LB).comp α)
   35:     (hK : Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ) :
   36:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   37:   first
   38:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   39:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   40:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   41:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   42:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   43:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   44:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   45:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   46: 
```

## 43. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:39`
```lean
   35:     (hK : Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ) :
   36:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   37:   first
   38:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   39:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   40:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   41:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   42:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   43:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   44:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   45:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   46: 
   47: theorem locPullback : ∀ {A R₀ A' B₀ : Type} [CommRing A] [CommRing R₀] [CommRing A'] [CommRing B₀]
```

## 44. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:61`
```lean
   57:     Aα.comp (algebraMap R₀ LR) = (algebraMap B₀ LB).comp α →
   58:     Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ →
   59:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   60:   first
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   62:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   63:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   64:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   65:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   66:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   67:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   68:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   69: 
```

## 45. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/LocalizationPreservesRingPullbackSquare.lean:62`
```lean
   58:     Kκ.comp (algebraMap A' LA') = (algebraMap B₀ LB).comp κ →
   59:     (∀ t, Φ t = 0 → Ψ t = 0 → t = 0) ∧ ∀ a b, Aα a = Kκ b → ∃ t, Φ t = a ∧ Ψ t = b := by
   60:   first
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.QuotientMapComposition.main
   62:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.QuotientMapComposition.main
   63:   | exact @_root_.GlobalTheory.QuotientMapComposition.main
   64:   | exact _root_.GlobalTheory.QuotientMapComposition.main
   65:   | (apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   66:   | (intros; apply _root_.GlobalTheory.QuotientMapComposition.main <;> assumption)
   67:   | (intros; apply @_root_.GlobalTheory.QuotientMapComposition.main <;> first | assumption | infer_instance)
   68:   | (intros; exact _root_.GlobalTheory.QuotientMapComposition.main ..)
   69: 
   70: end GlobalTheory
```

## 46. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/MatchedDiffsInvariantSubspace.lean:31`
```lean
   27: 
   28: theorem gen_stable {ρ : ι → V →ₗ[ℂ] V} {N : Submodule ℂ V} (hN : ∀ y, ∀ x ∈ N, ρ y x ∈ N)
   29:     {s : Module.End ℂ V} (hs : s ∈ gen ρ) : ∀ x ∈ N, s x ∈ N := by
   30:   first
   31:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   32:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SpectralLemmaFirst.main
   33:   | exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   34:   | exact _root_.GlobalTheory.SpectralLemmaFirst.main
   35:   | (apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   36:   | (intros; apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   37:   | (intros; apply @_root_.GlobalTheory.SpectralLemmaFirst.main <;> first | assumption | infer_instance)
   38:   | (intros; exact _root_.GlobalTheory.SpectralLemmaFirst.main ..)
   39: 
```

## 47. [run_tac] `Development/AbelianVarietyTheory/Proofs/DivisorProofs/MatchedDiffsInvariantSubspace.lean:32`
```lean
   28: theorem gen_stable {ρ : ι → V →ₗ[ℂ] V} {N : Submodule ℂ V} (hN : ∀ y, ∀ x ∈ N, ρ y x ∈ N)
   29:     {s : Module.End ℂ V} (hs : s ∈ gen ρ) : ∀ x ∈ N, s x ∈ N := by
   30:   first
   31:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   32:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.SpectralLemmaFirst.main
   33:   | exact @_root_.GlobalTheory.SpectralLemmaFirst.main
   34:   | exact _root_.GlobalTheory.SpectralLemmaFirst.main
   35:   | (apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   36:   | (intros; apply _root_.GlobalTheory.SpectralLemmaFirst.main <;> assumption)
   37:   | (intros; apply @_root_.GlobalTheory.SpectralLemmaFirst.main <;> first | assumption | infer_instance)
   38:   | (intros; exact _root_.GlobalTheory.SpectralLemmaFirst.main ..)
   39: 
   40: def lift (ρ : ι → V →ₗ[ℂ] V) (N : Submodule ℂ V) (hN : ∀ y, ∀ x ∈ N, ρ y x ∈ N) : Submodule (gen ρ) V where
```

## 48. [run_tac] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BasedFlagPairLatticeContainment.lean:131`
```lean
  127: 
  128: theorem exists_nat_smul_mem (Λ : LV D) (hΛ : Submodule.IsLattice D.host.E Λ) (v : (VS D).V) :
  129:     ∃ n : ℕ, 0 < n ∧ (n : D.host.E) • v ∈ Λ := by
  130:   first
  131:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  132:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  133:   | exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  134:   | exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  135:   | (apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  136:   | (intros; apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  137:   | (intros; apply @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> first | assumption | infer_instance)
  138:   | (intros; exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem ..)
  139: 
```

## 49. [run_tac] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/BasedFlagPairLatticeContainment.lean:132`
```lean
  128: theorem exists_nat_smul_mem (Λ : LV D) (hΛ : Submodule.IsLattice D.host.E Λ) (v : (VS D).V) :
  129:     ∃ n : ℕ, 0 < n ∧ (n : D.host.E) • v ∈ Λ := by
  130:   first
  131:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  132:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  133:   | exact @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  134:   | exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem
  135:   | (apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  136:   | (intros; apply _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> assumption)
  137:   | (intros; apply @_root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem <;> first | assumption | infer_instance)
  138:   | (intros; exact _root_.GlobalTheory.NatSmulMemOfSpan.exists_nat_smul_mem ..)
  139: 
  140: end GlobalTheory.CompScale
```

## 50. [run_tac] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/DetMatrixSandwichLinearMap.lean:14`
```lean
   10:     (L : (ι → Fin j → Fin j → ℂ) →ₗ[ℝ] (ι → Fin j → Fin j → ℂ))
   11:     (hL : ∀ h w, Matrix.of (L h w) = A w * Matrix.of (h w) * B w) :
   12:     LinearMap.det L = ∏ w, (‖(A w).det‖ ^ 2 * ‖(B w).det‖ ^ 2) ^ j := by
   13:   first
   14:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   15:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   16:   | exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   17:   | exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   18:   | (apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   19:   | (intros; apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   20:   | (intros; apply @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> first | assumption | infer_instance)
   21:   | (intros; exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family ..)
   22: 
```

## 51. [run_tac] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/DetMatrixSandwichLinearMap.lean:15`
```lean
   11:     (hL : ∀ h w, Matrix.of (L h w) = A w * Matrix.of (h w) * B w) :
   12:     LinearMap.det L = ∏ w, (‖(A w).det‖ ^ 2 * ‖(B w).det‖ ^ 2) ^ j := by
   13:   first
   14:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   15:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   16:   | exact @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   17:   | exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family
   18:   | (apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   19:   | (intros; apply _root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> assumption)
   20:   | (intros; apply @_root_.GlobalTheory.DeterminantRealSandwich.det_real_family <;> first | assumption | infer_instance)
   21:   | (intros; exact _root_.GlobalTheory.DeterminantRealSandwich.det_real_family ..)
   22: 
   23: end GlobalTheory.MatMulDet
```

## 52. [run_tac] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/PowLePowRatio.lean:153`
```lean
  149: theorem span_inner {n : ℕ} (L M : Hn n →L[ℂ] Hn n) (s t : Set (Hn n))
  150:     (h : ∀ u ∈ s, ∀ z ∈ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0) :
  151:     ∀ u ∈ Submodule.span ℂ s, ∀ z ∈ Submodule.span ℂ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0 := by
  152:   first
  153:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  154:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InnerSumZeroSpan.main
  155:   | exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  156:   | exact _root_.GlobalTheory.InnerSumZeroSpan.main
  157:   | (apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  158:   | (intros; apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  159:   | (intros; apply @_root_.GlobalTheory.InnerSumZeroSpan.main <;> first | assumption | infer_instance)
  160:   | (intros; exact _root_.GlobalTheory.InnerSumZeroSpan.main ..)
  161: 
```

## 53. [run_tac] `Development/AbelianVarietyTheory/Proofs/FlagMeasures/PowLePowRatio.lean:154`
```lean
  150:     (h : ∀ u ∈ s, ∀ z ∈ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0) :
  151:     ∀ u ∈ Submodule.span ℂ s, ∀ z ∈ Submodule.span ℂ t, ⟪L u, z⟫_ℂ + ⟪u, M z⟫_ℂ = 0 := by
  152:   first
  153:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  154:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.InnerSumZeroSpan.main
  155:   | exact @_root_.GlobalTheory.InnerSumZeroSpan.main
  156:   | exact _root_.GlobalTheory.InnerSumZeroSpan.main
  157:   | (apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  158:   | (intros; apply _root_.GlobalTheory.InnerSumZeroSpan.main <;> assumption)
  159:   | (intros; apply @_root_.GlobalTheory.InnerSumZeroSpan.main <;> first | assumption | infer_instance)
  160:   | (intros; exact _root_.GlobalTheory.InnerSumZeroSpan.main ..)
  161: 
  162: theorem sp_orth (w : InfinitePlace I.E) {A B : Submodule (𝓞 I.E) (Fin I.n → I.E)}
```

## 54. [run_tac] `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtTwistedPlaces.lean:60`
```lean
   56: 
   57: theorem exists_below_of_range (D D' : D7) (h : Set.range D.what₂.embLL ⊆ Set.range D'.what₂.embLL) (v' : D'.what₂.places.Pl) :
   58:     ∃ v : D.what₂.places.Pl, Below D D' v v' := by
   59:   first
   60:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.PrimeBelow.exists_below
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.PrimeBelow.exists_below
   62:   | exact @_root_.GlobalTheory.PrimeBelow.exists_below
   63:   | exact _root_.GlobalTheory.PrimeBelow.exists_below
   64:   | (apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   65:   | (intros; apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   66:   | (intros; apply @_root_.GlobalTheory.PrimeBelow.exists_below <;> first | assumption | infer_instance)
   67:   | (intros; exact _root_.GlobalTheory.PrimeBelow.exists_below ..)
   68: 
```

## 55. [run_tac] `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsExtTwistedPlaces.lean:61`
```lean
   57: theorem exists_below_of_range (D D' : D7) (h : Set.range D.what₂.embLL ⊆ Set.range D'.what₂.embLL) (v' : D'.what₂.places.Pl) :
   58:     ∃ v : D.what₂.places.Pl, Below D D' v v' := by
   59:   first
   60:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.PrimeBelow.exists_below
   61:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.PrimeBelow.exists_below
   62:   | exact @_root_.GlobalTheory.PrimeBelow.exists_below
   63:   | exact _root_.GlobalTheory.PrimeBelow.exists_below
   64:   | (apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   65:   | (intros; apply _root_.GlobalTheory.PrimeBelow.exists_below <;> assumption)
   66:   | (intros; apply @_root_.GlobalTheory.PrimeBelow.exists_below <;> first | assumption | infer_instance)
   67:   | (intros; exact _root_.GlobalTheory.PrimeBelow.exists_below ..)
   68: 
   69: theorem resChar_of_below {D D' : D7} {v : D.what₂.places.Pl} {v' : D'.what₂.places.Pl} (hB : Below D D' v v') :
```

## 56. [run_tac] `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsGIs.lean:81`
```lean
   77: set_option maxHeartbeats 4000000 in
   78: 
   79: theorem isLocalFamily_stages (sc : Scale) (Z Z' : Later B C) (L0 : LevelData (recOf Z)) (T : ∀ u, Forms0 (recOf Z) u) (g)
   80:     (h : IsLocalFamily sc (recOf Z) L0 T g) : IsLocalFamily sc (recOf Z') L0 (fun u => forms0Re Z' (T u)) g := by
   81:   run_tac do
   82:     let m ← Lean.Elab.Tactic.getMainGoal
   83:     m.withContext do m.assign (← Lean.Meta.getFVarFromUserName `h)
   84: 
   85: end Stages
   86: 
   87: section Main
   88: 
   89: open Formalism.MainNotions.G Formalism.L2.G IsDedekindDomain Formalism.UG Formalism.L2.Forms GlobalTheory.Mem.ConcreteRecord GlobalTheory.Mem.Top.ColOwe GlobalTheory.Mem.Col2 GlobalTheory.Mem.Col2.TC
```

## 57. [run_tac] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicLatticeSmulMemOfAgreeAwayFromPlace.lean:70`
```lean
   66: 
   67: theorem exists_nsmul_mem_of_mem_span {N : ℕ} (Lb : Submodule (𝓞 E) (Fin N → E)) {v : Fin N → E}
   68:     (hv : v ∈ Submodule.span E (Lb : Set (Fin N → E))) : ∃ n : ℕ, 0 < n ∧ n • v ∈ Lb := by
   69:   first
   70:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   71:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   72:   | exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   73:   | exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   74:   | (apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   75:   | (intros; apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   76:   | (intros; apply @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> first | assumption | infer_instance)
   77:   | (intros; exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem ..)
   78: 
```

## 58. [run_tac] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicLatticeSmulMemOfAgreeAwayFromPlace.lean:71`
```lean
   67: theorem exists_nsmul_mem_of_mem_span {N : ℕ} (Lb : Submodule (𝓞 E) (Fin N → E)) {v : Fin N → E}
   68:     (hv : v ∈ Submodule.span E (Lb : Set (Fin N → E))) : ∃ n : ℕ, 0 < n ∧ n • v ∈ Lb := by
   69:   first
   70:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   71:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   72:   | exact @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   73:   | exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem
   74:   | (apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   75:   | (intros; apply _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> assumption)
   76:   | (intros; apply @_root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem <;> first | assumption | infer_instance)
   77:   | (intros; exact _root_.GlobalTheory.NatMulIsIntegralSatakeParameters.exists_nsmul_mem ..)
   78: 
   79: end GlobalTheory.TwV.Xc
```

## 59. [run_tac] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/UnramifiedWeierstrassCurveTransformCoefficientsW.lean:20`
```lean
   16: variable {p : ℕ} [Fact p.Prime]
   17: 
   18: theorem inWf_of_kur {x : ℂ_[p]} (hx : x ∈ Formalism.L2.Th1.CM.MaximalUnramifiedExtension p) : InWf x := by
   19:   first
   20:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   21:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   22:   | exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   23:   | exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   24:   | (apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   25:   | (intros; apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   26:   | (intros; apply @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> first | assumption | infer_instance)
   27:   | (intros; exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur ..)
   28: 
```

## 60. [run_tac] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/UnramifiedWeierstrassCurveTransformCoefficientsW.lean:21`
```lean
   17: 
   18: theorem inWf_of_kur {x : ℂ_[p]} (hx : x ∈ Formalism.L2.Th1.CM.MaximalUnramifiedExtension p) : InWf x := by
   19:   first
   20:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   21:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   22:   | exact @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   23:   | exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur
   24:   | (apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   25:   | (intros; apply _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> assumption)
   26:   | (intros; apply @_root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur <;> first | assumption | infer_instance)
   27:   | (intros; exact _root_.GlobalTheory.WittRootsOfUnity.inWf_of_mem_Kur ..)
   28: 
   29: theorem coefWf_phW_of_kur (W : WeierstrassCurve ℂ_[p]) (h1 : W.a₁ ∈ Formalism.L2.Th1.CM.MaximalUnramifiedExtension p)
```

## 61. [run_tac] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/ValuationRingModel.lean:206`
```lean
  202:   exact ⟨s, Finset.mem_insert_of_mem hs, hgs⟩
  203: 
  204: theorem res_algClosed [IsAlgClosed K] : IsAlgClosed (IsLocalRing.ResidueField O) := by
  205:   first
  206:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  207:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  208:   | exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  209:   | exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  210:   | (apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  211:   | (intros; apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  212:   | (intros; apply @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> first | assumption | infer_instance)
  213:   | (intros; exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField ..)
  214: 
```

## 62. [run_tac] `Development/AbelianVarietyTheory/Proofs/SatakeParameters/ValuationRingModel.lean:207`
```lean
  203: 
  204: theorem res_algClosed [IsAlgClosed K] : IsAlgClosed (IsLocalRing.ResidueField O) := by
  205:   first
  206:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  207:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  208:   | exact @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  209:   | exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField
  210:   | (apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  211:   | (intros; apply _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> assumption)
  212:   | (intros; apply @_root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField <;> first | assumption | infer_instance)
  213:   | (intros; exact _root_.GlobalTheory.AlgClosedResidueField.isAlgClosed_residueField ..)
  214: 
  215: end Top
```

## 63. [run_tac] `Development/AbelianVarietyTheory/Proofs/TwistedOperators/RelIndexTwoBlockParahoricConjTorusDiagElement.lean:22`
```lean
   18:     (((parahoric k A D).map (MulAut.conj (mtor (A := A) ϖ e)).toMonoidHom).relIndex (parahoric k A D) : ℝ) =
   19:       (resCard k : ℝ) ^ ((Fintype.card A : ℤ) * sumAbs e) *
   20:         (((KO k D).map (MulAut.conj (torusElt k D ϖ e)).toMonoidHom).relIndex (KO k D) : ℝ) := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   24:   | exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   25:   | exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   26:   | (apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric ..)
   30: 
```

## 64. [run_tac] `Development/AbelianVarietyTheory/Proofs/TwistedOperators/RelIndexTwoBlockParahoricConjTorusDiagElement.lean:23`
```lean
   19:       (resCard k : ℝ) ^ ((Fintype.card A : ℤ) * sumAbs e) *
   20:         (((KO k D).map (MulAut.conj (torusElt k D ϖ e)).toMonoidHom).relIndex (KO k D) : ℝ) := by
   21:   first
   22:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   23:   | (run_tac Lean.Elab.Tactic.liftMetaTactic (fun g => do pure [← g.revertAll])); exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   24:   | exact @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   25:   | exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric
   26:   | (apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   27:   | (intros; apply _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> assumption)
   28:   | (intros; apply @_root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric <;> first | assumption | infer_instance)
   29:   | (intros; exact _root_.GlobalTheory.ParahoricConjugateOpen.relIndex_conj_parahoric ..)
   30: 
   31: end GlobalTheory.ParIdx
```
