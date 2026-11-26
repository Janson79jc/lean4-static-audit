# Lean 4 SE Maintainability & Topology Report (grh_compact_se_topology)

- **Modules**: `794` | **Acyclic DAG**: `True` (`794/794`) | **Max DAG Depth**: `54` (`p90=38`)
- **Zero-Declaration Files (`defs=0 & thms=0`)**: `0` (`0.0%`) | **Elapsed**: `0.02s`

## 1. Gini Concentration & Quantiles

| Metric | Total | Gini | Top 1% Share | Top 5% Share | Top 10% Share | P50 | P90 | P99 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `code_lines` | 76,149 | 0.3770 | 3.68% | 15.07% | 25.54% | 82 | 180 | 350 | 464 |
| `raw_lines` | 112,827 | 0.3565 | 3.56% | 14.32% | 24.61% | 121 | 262 | 511 | 619 |
| `defs` | 3,855 | 0.6898 | 8.72% | 32.43% | 49.7% | 2 | 14 | 40 | 60 |
| `thms` | 7,088 | 0.4947 | 5.11% | 20.26% | 33.47% | 6 | 20 | 43 | 64 |
| `direct_fan_in` | 1,398 | 0.2857 | 3.36% | 13.59% | 22.96% | 1 | 3 | 5 | 11 |
| `local_fan_out` | 1,398 | 0.2698 | 2.72% | 12.59% | 21.6% | 2 | 3 | 5 | 6 |
| `transitive_blast_radius` | 96,940 | 0.5156 | 4.53% | 20.22% | 35.01% | 78 | 299 | 533 | 792 |

## 2. Top-25 Hub Bottlenecks (by Exact Transitive Blast Radius)

| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |
|---|---:|---:|---:|---:|---:|---:|
| `Lib.General.LinearAlgebra.Base` | 11 | 792 | 99.75% | 0 | 0 | 140 |
| `Lib.General.Analysis.OstrowskiTaussky` | 6 | 682 | 85.89% | 1 | 1 | 65 |
| `Lib.General.Analysis.ZpowSum` | 4 | 649 | 81.74% | 1 | 1 | 59 |
| `Lib.General.Groups.ValuationPair` | 5 | 608 | 76.57% | 1 | 1 | 213 |
| `Lib.General.LinearAlgebra.PartialDerivComm` | 4 | 586 | 73.8% | 1 | 1 | 98 |
| `Lib.General.Measure.SubgroupIntegral` | 4 | 538 | 67.76% | 1 | 2 | 38 |
| `Lib.ClassField.GaloisCohomology.ContinuousCocycles` | 1 | 534 | 67.25% | 1 | 1 | 27 |
| `Lib.ClassField.Places.GaloisDefs` | 1 | 534 | 67.25% | 1 | 1 | 59 |
| `Lib.ClassField.GaloisCohomology.CyclicClass` | 2 | 533 | 67.13% | 2 | 2 | 23 |
| `Lib.Adelic.Adeles.CoprimeValuation` | 4 | 525 | 66.12% | 1 | 1 | 135 |
| `Lib.DiscreteSeries.CuspKernel.CircleMean` | 4 | 519 | 65.37% | 1 | 2 | 111 |
| `Lib.General.LinearAlgebra.ExtendColumns` | 2 | 518 | 65.24% | 1 | 2 | 80 |
| `Lib.General.LinearAlgebra.AdelicRingDefs` | 2 | 516 | 64.99% | 2 | 3 | 55 |
| `Lib.Adelic.QuotientMeasure.Packing` | 1 | 515 | 64.86% | 1 | 3 | 89 |
| `Lib.Adelic.QuotientMeasure.Unimodular` | 2 | 514 | 64.74% | 2 | 4 | 124 |
| `Lib.Adelic.Adeles.AdeleTopology` | 2 | 513 | 64.61% | 2 | 2 | 100 |
| `Lib.Adelic.Hecke.HeckeBasic` | 1 | 510 | 64.23% | 1 | 2 | 52 |
| `Lib.General.LinearAlgebra.ColumnLattices` | 4 | 509 | 64.11% | 2 | 4 | 112 |
| `Lib.Adelic.Adeles.AdeleIdempotent` | 5 | 490 | 61.71% | 1 | 3 | 39 |
| `Lib.Weil.Construction.SubmoduleNormedSpace` | 2 | 478 | 60.2% | 1 | 2 | 29 |
| `Lib.Adelic.Adeles.AdditiveCharDefs` | 3 | 477 | 60.08% | 2 | 3 | 35 |
| `Lib.General.LinearAlgebra.ValuedMatrix` | 4 | 475 | 59.82% | 1 | 2 | 52 |
| `Lib.General.LinearAlgebra.SubmersionZero` | 2 | 475 | 59.82% | 1 | 1 | 19 |
| `Lib.General.LinearAlgebra.CommonEigenvectors` | 6 | 466 | 58.69% | 1 | 2 | 85 |
| `Lib.Adelic.QuotientMeasure.PeriodicMean` | 1 | 466 | 58.69% | 2 | 3 | 40 |

## 3. Top-25 Hub Bottlenecks (by Direct Fan-In)

| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |
|---|---:|---:|---:|---:|---:|---:|
| `Lib.General.LinearAlgebra.Base` | 11 | 792 | 99.75% | 0 | 0 | 140 |
| `Lib.Cohomology.Etale.TestRings` | 7 | 173 | 21.79% | 1 | 3 | 50 |
| `Lib.General.Analysis.OstrowskiTaussky` | 6 | 682 | 85.89% | 1 | 1 | 65 |
| `Lib.General.LinearAlgebra.CommonEigenvectors` | 6 | 466 | 58.69% | 1 | 2 | 85 |
| `Lib.Adelic.Witt.FrameAction` | 6 | 437 | 55.04% | 1 | 5 | 111 |
| `Lib.Shimura.IntegralModel.NeatLevel` | 6 | 153 | 19.27% | 5 | 13 | 191 |
| `Lib.General.Groups.ValuationPair` | 5 | 608 | 76.57% | 1 | 1 | 213 |
| `Lib.Adelic.Adeles.AdeleIdempotent` | 5 | 490 | 61.71% | 1 | 3 | 39 |
| `Lib.General.Algebra.AdicRingHomExt` | 5 | 421 | 53.02% | 1 | 1 | 78 |
| `Lib.General.Analysis.HolomorphicIntegral` | 5 | 406 | 51.13% | 1 | 2 | 84 |
| `Lib.Adelic.Witt.SpaceOperations` | 5 | 348 | 43.83% | 3 | 9 | 122 |
| `Lib.ClassField.Places.UnramifiedCharacters` | 5 | 327 | 41.18% | 2 | 9 | 79 |
| `Lib.ClassField.Places.AdeleNorm` | 5 | 323 | 40.68% | 3 | 7 | 110 |
| `Lib.Weil.Unramified.SphericalHecke` | 5 | 259 | 32.62% | 2 | 10 | 143 |
| `Lib.General.LinearAlgebra.ExpSurjective` | 5 | 242 | 30.48% | 2 | 11 | 159 |
| `Lib.Adelic.CuspForms.Petersson` | 5 | 160 | 20.15% | 1 | 20 | 127 |
| `Lib.Weil.DualPair.PairSumNegation` | 5 | 140 | 17.63% | 1 | 26 | 151 |
| `Lib.Weil.DualPair.ThetaIntegralLaws` | 5 | 125 | 15.74% | 2 | 31 | 51 |
| `Lib.CM.FormalGroup.FormalHeight` | 5 | 117 | 14.74% | 3 | 14 | 151 |
| `Lib.Weil.MixedModel.EquivariantCoefficients` | 5 | 107 | 13.48% | 2 | 32 | 154 |
| `Lib.Weil.Lift.Staircase` | 5 | 97 | 12.22% | 2 | 33 | 142 |
| `New.Seesaw.IndexTypes` | 5 | 80 | 10.08% | 2 | 29 | 146 |
| `Lib.General.Analysis.ZpowSum` | 4 | 649 | 81.74% | 1 | 1 | 59 |
| `Lib.General.LinearAlgebra.PartialDerivComm` | 4 | 586 | 73.8% | 1 | 1 | 98 |
| `Lib.General.Measure.SubgroupIntegral` | 4 | 538 | 67.76% | 1 | 2 | 38 |

## 4. Cross-Directory Coupling Matrix (Source -> Imported Target, Deduplicated Edges)

| Source \\ Target | (root) | Lib | New |
|---|---:|---:|---:|
| `(root)` | 0 | 0 | 1 |
| `Lib` | 0 | 960 | 0 |
| `New` | 1 | 102 | 334 |
