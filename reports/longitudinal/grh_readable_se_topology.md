# Lean 4 SE Maintainability & Topology Report (grh_readable_se_topology)

- **Modules**: `803` | **Acyclic DAG**: `True` (`803/803`) | **Max DAG Depth**: `53` (`p90=39`)
- **Zero-Declaration Files (`defs=0 & thms=0`)**: `0` (`0.0%`) | **Elapsed**: `0.02s`

## 1. Gini Concentration & Quantiles

| Metric | Total | Gini | Top 1% Share | Top 5% Share | Top 10% Share | P50 | P90 | P99 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `code_lines` | 299,902 | 0.2794 | 2.33% | 10.16% | 18.94% | 355 | 627 | 791 | 1,002 |
| `raw_lines` | 477,124 | 0.2632 | 2.2% | 9.76% | 18.29% | 565 | 978 | 1,211 | 1,491 |
| `defs` | 5,612 | 0.5760 | 7.88% | 25.29% | 40.18% | 4 | 17 | 39 | 97 |
| `thms` | 18,227 | 0.3199 | 3.58% | 13.27% | 22.8% | 20 | 40 | 70 | 113 |
| `direct_fan_in` | 1,733 | 0.3583 | 5.14% | 17.31% | 27.87% | 2 | 4 | 8 | 20 |
| `local_fan_out` | 1,733 | 0.2982 | 3.12% | 12.75% | 22.22% | 2 | 4 | 6 | 8 |
| `transitive_blast_radius` | 95,514 | 0.6336 | 6.01% | 25.53% | 43.07% | 38 | 349 | 660 | 801 |

## 2. Top-25 Hub Bottlenecks (by Exact Transitive Blast Radius)

| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |
|---|---:|---:|---:|---:|---:|---:|
| `Lib.Speed` | 1 | 801 | 99.75% | 0 | 0 | 56 |
| `Lib.Base` | 20 | 800 | 99.63% | 1 | 1 | 7 |
| `Lib.General.Groups.CongruenceSubgroups` | 10 | 712 | 88.67% | 1 | 2 | 254 |
| `Lib.General.Measure.IdempotentKernel` | 1 | 690 | 85.93% | 1 | 2 | 121 |
| `Lib.Adelic.QuotientMeasure.Basic` | 7 | 689 | 85.8% | 1 | 3 | 482 |
| `Lib.General.Topology` | 6 | 684 | 85.18% | 1 | 2 | 114 |
| `Lib.Adelic.Hecke.Basic` | 5 | 680 | 84.68% | 1 | 2 | 241 |
| `Lib.Adelic.Adeles.Basic` | 3 | 680 | 84.68% | 1 | 2 | 663 |
| `Lib.Adelic.Adeles.AdditiveCharacter` | 4 | 668 | 83.19% | 3 | 4 | 269 |
| `Lib.ClassField.Places.GaloisDefs` | 1 | 660 | 82.19% | 1 | 2 | 126 |
| `Lib.ClassField.GaloisCohomology.ContinuousCocycles` | 3 | 659 | 82.07% | 1 | 3 | 340 |
| `Lib.Adelic.Unitary.Defs` | 8 | 635 | 79.08% | 3 | 5 | 291 |
| `Lib.General.Groups.BesselGroups` | 6 | 633 | 78.83% | 1 | 3 | 138 |
| `Lib.General.NumberTheory.EmbeddingsAndDifferent` | 3 | 632 | 78.7% | 1 | 5 | 158 |
| `Lib.General.Analysis.FourierTransforms` | 2 | 632 | 78.7% | 1 | 4 | 207 |
| `Lib.General.LinearAlgebra.IntegralLattices` | 2 | 619 | 77.09% | 2 | 4 | 455 |
| `Lib.General.Measure.HaarModulus` | 3 | 616 | 76.71% | 1 | 5 | 275 |
| `Lib.General.Groups.ProfiniteCharacters` | 3 | 614 | 76.46% | 2 | 4 | 234 |
| `Lib.Adelic.Adeles.StrongApproximation` | 2 | 608 | 75.72% | 3 | 6 | 437 |
| `Lib.ClassField.Places.Ideles` | 4 | 603 | 75.09% | 3 | 7 | 237 |
| `Lib.GaloisRep.BaseChange.Defs` | 1 | 595 | 74.1% | 1 | 6 | 101 |
| `Lib.General.LinearAlgebra.MatrixPolynomials` | 4 | 594 | 73.97% | 1 | 7 | 125 |
| `Lib.Weil.DualPair.Kronecker` | 1 | 587 | 73.1% | 1 | 3 | 25 |
| `Lib.Adelic.Adeles.IdeleModulus` | 4 | 586 | 72.98% | 2 | 8 | 311 |
| `Lib.GaloisRep.Hilbert90.TameActions` | 2 | 583 | 72.6% | 1 | 8 | 500 |

## 3. Top-25 Hub Bottlenecks (by Direct Fan-In)

| Module | Direct Fan-In | Blast Radius | Blast % | Local Fan-Out | Depth | Code Lines |
|---|---:|---:|---:|---:|---:|---:|
| `Lib.Base` | 20 | 800 | 99.63% | 1 | 1 | 7 |
| `Lib.Shimura.Uniformisation.HolomorphicFamilies` | 11 | 249 | 31.01% | 5 | 11 | 590 |
| `Lib.General.NumberTheory.PadicLimitsValuation` | 11 | 189 | 23.54% | 3 | 17 | 202 |
| `Lib.General.Groups.CongruenceSubgroups` | 10 | 712 | 88.67% | 1 | 2 | 254 |
| `Lib.Cohomology.Etale.Basic` | 10 | 484 | 60.27% | 1 | 3 | 581 |
| `Lib.General.Analysis.HolomorphicIntegrals` | 9 | 544 | 67.75% | 4 | 4 | 456 |
| `Lib.General.LinearAlgebra.Eigenvalues` | 9 | 348 | 43.34% | 1 | 3 | 507 |
| `Lib.General.LinearAlgebra.BlockEmbeddings` | 9 | 148 | 18.43% | 2 | 23 | 241 |
| `New.UpperBound.Objects.Rows` | 9 | 82 | 10.21% | 4 | 37 | 541 |
| `Lib.Adelic.Unitary.Defs` | 8 | 635 | 79.08% | 3 | 5 | 291 |
| `Lib.Adelic.Witt.WittTheorem` | 8 | 579 | 72.1% | 2 | 10 | 461 |
| `Lib.Weil.Unramified.HeckeGL` | 8 | 365 | 45.45% | 2 | 13 | 402 |
| `Lib.PadicComparison.Descent.TestCategory` | 8 | 316 | 39.35% | 2 | 7 | 356 |
| `Lib.Shimura.HeckeTower.HeckeData` | 8 | 201 | 25.03% | 3 | 14 | 576 |
| `Lib.Adelic.QuotientMeasure.Basic` | 7 | 689 | 85.8% | 1 | 3 | 482 |
| `Lib.Adelic.Adeles.LocalFactors` | 7 | 432 | 53.8% | 3 | 15 | 254 |
| `Lib.General.NumberTheory.FrobeniusOrbits` | 7 | 412 | 51.31% | 1 | 3 | 146 |
| `Lib.GLn.SchurModule.Basic` | 7 | 387 | 48.19% | 1 | 2 | 407 |
| `Lib.General.Algebra.MultivariatePolynomials` | 7 | 320 | 39.85% | 1 | 4 | 286 |
| `Lib.ClassField.Global.CMSplittingCharacters` | 7 | 270 | 33.62% | 2 | 18 | 593 |
| `Lib.ClassField.HeckeCharacter.SplitTameCharacters` | 7 | 178 | 22.17% | 2 | 23 | 230 |
| `Lib.Analytic.EntireLFunction` | 7 | 151 | 18.8% | 1 | 7 | 123 |
| `Lib.ClassField.HeckeCharacter.TameModulus` | 7 | 139 | 17.31% | 4 | 28 | 222 |
| `Lib.Shimura.HeckeTower.Model` | 7 | 48 | 5.98% | 5 | 15 | 562 |
| `Lib.General.Topology` | 6 | 684 | 85.18% | 1 | 2 | 114 |

## 4. Cross-Directory Coupling Matrix (Source -> Imported Target, Deduplicated Edges)

| Source \\ Target | (root) | Lib | New |
|---|---:|---:|---:|
| `(root)` | 0 | 0 | 1 |
| `Lib` | 0 | 999 | 0 |
| `New` | 1 | 208 | 524 |
