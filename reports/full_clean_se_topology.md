# Lean 4 SE Maintainability & Topology Report (full_clean_se_topology)

- **Modules**: `175,187` | **Acyclic DAG**: `True` (`175,187/175,187`) | **Max DAG Depth**: `202` (`p90=98`)
- **Zero-Declaration Files (`defs=0 & thms=0`)**: `174` (`0.1%`) | **Elapsed**: `12.22s`

## 1. Gini Concentration & Quantiles

| Metric | Total | Gini | Top 1% Share | Top 5% Share | Top 10% Share | P50 | P90 | P99 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `code_lines` | 15,531,759 | 0.5631 | 9.14% | 25.34% | 39.03% | 51 | 210 | 498 | 14,814 |
| `raw_lines` | 17,374,215 | 0.5626 | 9.18% | 25.3% | 38.93% | 58 | 233 | 560 | 17,981 |
| `defs` | 242,670 | 0.8989 | 30.65% | 65.7% | 82.45% | 0 | 3 | 24 | 226 |
| `thms` | 818,755 | 0.6273 | 13.1% | 33.34% | 48.59% | 1 | 12 | 35 | 1,518 |
| `direct_fan_in` | 753,261 | 0.6966 | 36.63% | 58.49% | 67.62% | 1 | 5 | 54 | 3,088 |
| `local_fan_out` | 753,261 | 0.4626 | 7.03% | 20.99% | 33.2% | 3 | 9 | 20 | 370 |
| `transitive_blast_radius` | 545,942,223 | 0.8905 | 22.93% | 64.49% | 86.02% | 87 | 6,888 | 49,494 | 108,056 |

## 2. Top-25 Hub Bottlenecks (by Exact Transitive Blast Radius)

| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |
|---|---:|---:|---:|---:|---:|---:|
| `Formalism.RealPlaceAnalysis.StatementA` | 23 | 108,056 | 61.68% | 0 | 0 | 129 |
| `Formalism.LatticeTheta.Statement` | 19 | 106,548 | 60.82% | 0 | 0 | 67 |
| `Formalism.SatakeDualWeyl.Statement` | 120 | 106,175 | 60.61% | 0 | 0 | 463 |
| `Formalism.FockGram.StatementLat` | 4 | 106,007 | 60.51% | 0 | 0 | 65 |
| `Formalism.FockGram.StatementHerm` | 4 | 106,002 | 60.51% | 1 | 1 | 31 |
| `Formalism.HermitianLattices.StatementLat` | 47 | 105,999 | 60.51% | 1 | 2 | 180 |
| `Formalism.RealPlaceAnalysis.FockPairGl` | 6 | 105,785 | 60.38% | 1 | 1 | 45 |
| `Formalism.RealPlaceAnalysis.RealPlaceTaylor.ProdFactorialSupportSubSingle` | 10 | 105,631 | 60.3% | 1 | 2 | 135 |
| `Formalism.TameInertiaTowers.StatementGroup` | 8 | 105,469 | 60.2% | 0 | 0 | 107 |
| `Formalism.TameInertiaTowers.StatementField` | 5 | 105,458 | 60.2% | 1 | 1 | 77 |
| `Formalism.FrobeniusOrbits.Statement` | 31 | 105,452 | 60.19% | 1 | 2 | 202 |
| `Formalism.SharpRestriction.RamificationFrobenius.TotientGaloisClasses.ZsmulGeneratorEqZeroOfProjection` | 7 | 105,362 | 60.14% | 1 | 3 | 92 |
| `Formalism.CoboundaryTransfers.Statement` | 24 | 105,218 | 60.06% | 0 | 0 | 148 |
| `Formalism.ConjugateSelfDual.Statement` | 13 | 105,014 | 59.94% | 0 | 0 | 24 |
| `ReciprocityTheory.GaloisValuations.SeparatedDvrSecondCohomologyMem` | 6 | 104,976 | 59.92% | 0 | 0 | 231 |
| `ReciprocityTheory.GaloisValuations.ContinuousConstSMulQuotient` | 14 | 104,971 | 59.92% | 1 | 1 | 166 |
| `Formalism.WeaklyAdmissibleFiltrations.Statement` | 49 | 104,938 | 59.9% | 1 | 1 | 456 |
| `ReciprocityTheory.GaloisValuations.GlobalA` | 8 | 104,932 | 59.9% | 0 | 0 | 152 |
| `Formalism.WeaklyAdmissibleFiltrations.StatementPC` | 3 | 104,900 | 59.88% | 1 | 2 | 70 |
| `Formalism.SharpRestriction.LevelLetterCocycles.DataNLoc` | 188 | 104,894 | 59.88% | 3 | 3 | 972 |
| `ReciprocityTheory.GaloisValuations.GlobalB` | 8 | 104,892 | 59.87% | 1 | 1 | 279 |
| `ReciprocityTheory.GaloisValuations.Global` | 67 | 104,890 | 59.87% | 3 | 2 | 353 |
| `Formalism.SharpRestriction.RamificationFrobenius.TotientGaloisClasses.EvalFrameOrd` | 1 | 104,780 | 59.81% | 1 | 4 | 14 |
| `Formalism.LocalRingCardinality.Params` | 47 | 104,779 | 59.81% | 1 | 5 | 79 |
| `Formalism.HermitianLattices.DefsCS` | 10 | 104,778 | 59.81% | 1 | 3 | 53 |

## 3. Top-25 Hub Bottlenecks (by Direct Fan-In)

| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |
|---|---:|---:|---:|---:|---:|---:|
| `Development.AbelianVarietyTheory.Definitions.Divisors.CTSmallCone` | 3,088 | 12,106 | 6.91% | 2 | 42 | 292 |
| `Development.AbelianVarietyTheory.Definitions.Divisors.SiegelWeilAnisotropicHermitian` | 2,972 | 9,718 | 5.55% | 23 | 53 | 53 |
| `Development.AbelianVarietyTheory.Definitions.Divisors.DiscreteSeriesHermitianUnique` | 2,518 | 13,112 | 7.48% | 62 | 50 | 128 |
| `Development.AbelianVarietyTheory.PublishedTheorems.AutomorphicForms₂.ExistsNormLeHeightPow` | 2,426 | 34,259 | 19.56% | 4 | 42 | 88 |
| `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.UniformisationConclusion` | 2,390 | 83,899 | 47.89% | 5 | 9 | 193 |
| `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ExtensionDescent.UnifUniqSt` | 2,284 | 58,347 | 33.31% | 1 | 15 | 54 |
| `Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.CohomologicalCsdTempered` | 2,242 | 2,251 | 1.28% | 0 | 0 | 1 |
| `Development.AbelianVarietyTheory.Definitions.Divisors.ToKnownTheoremsOf` | 1,838 | 9,534 | 5.44% | 20 | 87 | 66 |
| `Development.AbelianVarietyTheory.PublishedTheorems.TwistedTraceFormula.HarishChandraModulesOn` | 1,653 | 21,456 | 12.25% | 4 | 34 | 177 |
| `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.HeckeKer` | 1,429 | 78,914 | 45.05% | 1 | 6 | 77 |
| `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.ExtensionDescent.SecBaseChangeAnySt` | 1,340 | 83,414 | 47.61% | 1 | 11 | 63 |
| `Development.AbelianVarietyTheory.PublishedTheorems.TwistedTraceFormula.AdmissibleDiscreteSeriesOfHasParam` | 1,323 | 16,544 | 9.44% | 5 | 30 | 233 |
| `Development.AbelianVarietyTheory.BlockTheory.DivisorBase.WeilTensorModels` | 1,307 | 17,277 | 9.86% | 5 | 40 | 419 |
| `ReciprocityTheory.ReductiveGroups.ArithmeticGeometry.BirationalGeometry.ToroidalCompactification.IsHolPeriods` | 1,206 | 89,172 | 50.9% | 2 | 7 | 98 |
| `Development.AbelianVarietyTheory.Definitions.Degenerations.AdmissibleBaseOfCompleteDvr` | 1,063 | 30,304 | 17.3% | 6 | 34 | 218 |
| `Development.AbelianVarietyTheory.PublishedTheorems.AutomorphicForms₂.HasDRepIffHasDerivAt` | 1,020 | 19,056 | 10.88% | 1 | 28 | 89 |
| `Development.AbelianVarietyTheory.Definitions.AbelianSchemeLaws.FirstCohomologyVanishesSpecOfIsLocalRing` | 963 | 54,873 | 31.32% | 3 | 12 | 196 |
| `Development.AbelianVarietyTheory.PublishedTheorems.Divisors₂.GeometricallyConnectedOfIsIsoRestrict` | 937 | 12,149 | 6.93% | 3 | 7 | 102 |
| `Formalism.LocalRingCardinality.RhoDetPrimeEqMuTildeMulChiPow` | 921 | 103,013 | 58.8% | 15 | 14 | 266 |
| `Development.AbelianVarietyTheory.PublishedTheorems.GaloisGeometry₂.HoweUnram` | 884 | 18,317 | 10.46% | 1 | 37 | 18 |
| `Formalism.SharpRestriction.Divisibility.GeneratorPowers.ThExprUniqOfChartIndep2` | 873 | 44,629 | 25.48% | 1 | 12 | 34 |
| `Development.AbelianVarietyTheory.PublishedTheorems.Divisors₂.CrysToDRBijective` | 859 | 18,459 | 10.54% | 1 | 23 | 70 |
| `Development.AbelianVarietyTheory.Definitions.Divisors.DivisorSupportCondition` | 858 | 3,761 | 2.15% | 3 | 5 | 121 |
| `Development.AbelianVarietyTheory.Definitions.Foundations.NormSumPairRankZeroOfCurveCoordNorm` | 829 | 43,389 | 24.77% | 1 | 25 | 381 |
| `Development.AbelianVarietyTheory.PublishedTheorems.AutomorphicForms₂.HarishChandraFinite` | 813 | 28,397 | 16.21% | 4 | 37 | 118 |

## 4. Cross-Directory Coupling Matrix (Source -> Imported Target, Deduplicated Edges)

| Source \\ Target | (root) | BuildAid | CompanionTheory | Development | Formalism | GroundTheory | Lemmata | PositivityTheory | ReciprocityTheory | Supplements |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `(root)` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| `BuildAid` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `CompanionTheory` | 0 | 3 | 5,034 | 1,437 | 762 | 65 | 0 | 0 | 154 | 0 |
| `Development` | 0 | 35 | 1,874 | 577,034 | 41,857 | 7,532 | 0 | 1,057 | 38,051 | 0 |
| `Formalism` | 0 | 0 | 1 | 236 | 44,412 | 1 | 118 | 0 | 348 | 0 |
| `GroundTheory` | 0 | 0 | 2 | 57 | 10 | 20,797 | 0 | 0 | 1,161 | 0 |
| `Lemmata` | 0 | 0 | 0 | 0 | 634 | 0 | 0 | 0 | 7 | 0 |
| `PositivityTheory` | 0 | 0 | 0 | 632 | 8 | 111 | 0 | 773 | 2 | 0 |
| `ReciprocityTheory` | 0 | 0 | 1 | 17 | 266 | 0 | 50 | 0 | 8,711 | 0 |
| `Supplements` | 0 | 0 | 0 | 6 | 1 | 0 | 0 | 0 | 0 | 2 |
