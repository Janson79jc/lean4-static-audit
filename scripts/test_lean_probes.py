"""Unit and regression test suite for Lean 4 static audit probes, topology, DAG, and L2.5 checks."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPTS_DIR.parent / "configs" / "rh_archive.json"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from lean_probes import _strip_by_subblocks, audit_lean_source  # noqa: E402
from run_l25_audit import _scan_batch  # noqa: E402


def test_prime_and_unicode_identifiers_not_swallowed() -> None:
    src = """
import Foo.Bar₂
import Foo.Baz'

def okPrime (x : Nat) (x' : Nat) (α₁ : Nat) : Nat :=
  x + x' + α₁

def badPrime (x : Nat) (x' : Nat) : Nat :=
  x'
"""
    res = audit_lean_source("Test/Prime.lean", src)
    assert res.imports == ["Foo.Bar₂", "Foo.Baz'"], f"Bad imports: {res.imports}"
    unused = [f for f in res.findings if f.rule == "DEF_UNUSED_EXPLICIT_NAMED_PARAM"]
    assert len(unused) == 1, f"Expected 1 finding, got: {unused}"
    assert unused[0].decl_name == "badPrime" and "x" in unused[0].detail


def test_overix_and_multiarg_vs_singlearg_split() -> None:
    src = """
def goodWithSuffix (x : Nat) : Nat :=
  x' + 1

def goodReturnUsed (x : Nat) : Fin (x + 1) :=
  ⟨0, Nat.zero_lt_succ x⟩

def multiVacuous (f : (Nat → Nat → Prop) → Nat) : Nat :=
  f (fun _ _ => True)

def singleVacuous (f : (Nat → Prop) → Nat) : Nat :=
  f (fun _ => True)

def wholeVacuous : Nat → Nat → Prop :=
  fun _ _ => True
"""
    res = audit_lean_source("Test/Rules.lean", src)
    rules_by_name = {(f.decl_name, f.rule) for f in res.findings}
    assert ("goodWithSuffix", "DEF_UNUSED_EXPLICIT_NAMED_PARAM") in rules_by_name
    assert not any(f.decl_name == "goodReturnUsed" for f in res.findings)
    assert ("multiVacuous", "DEF_MULTIARG_FUN_TRUE") in rules_by_name
    assert ("singleVacuous", "DEF_SINGLEARG_FUN_TRUE") in rules_by_name
    assert ("wholeVacuous", "DEF_FUN_TRUE") in rules_by_name


def test_unicode_param_and_inline_by_and_strict_implicit() -> None:
    src = """
def unicodeUsed (α : Type) (β : α → Nat) (x : α) : Nat :=
  β x

def strictImplicitIgnored ⦃x : Nat⦄ (y : Nat) : Nat :=
  y

def inlineByProof (n : Nat) : { k : Nat // k = n } :=
  ⟨n, (by rfl)⟩
"""
    res = audit_lean_source("Test/UnicodeInline.lean", src)
    assert res.findings == [], f"Unexpected false positives: {res.findings}"


def test_postfix_math_operators_not_false_positive() -> None:
    src = """
def groupInv {G : Type} [Group G] (g : G) : G :=
  g⁻¹

def matTrans {M : Type} (A : M) (op : M → M) : M :=
  op Aᵀ
"""
    res = audit_lean_source("Test/PostfixOps.lean", src)
    assert res.findings == [], f"Postfix math operators flagged falsely: {res.findings}"


def test_by_subblock_inside_def_and_nested_paren_and_line0_indent() -> None:
    src = """
structure Pkg where
  val : Nat
  prop : True
  flag : Nat → Nat → Prop

def cleanStruct (n : Nat) : Pkg where
  val := n
  prop := by
    have h : (fun _ _ => True) 1 2 := trivial
    exact h
  flag := fun x y => x = y

def nestedParenBy (n : Nat) (h : n = n) : { x : Nat // x = x } :=
  ⟨n, (by exact (id h))⟩

def line0ByWithSibling : Pkg := {
  prop := by
    exact True.intro
  val := 1
  flag := fun _ _ => True
}

def inlineBySameIndentSibling : Pkg where
  prop := by rfl
  val := 1
  flag := fun _ _ => True

def inlineByLine0Sibling : Pkg := { prop := by rfl
  val := 1
  flag := fun _ _ => True
}
"""
    res = audit_lean_source("Test/Subblock.lean", src)
    names_rules = [(f.decl_name, f.rule) for f in res.findings]
    assert ("cleanStruct", "DEF_MULTIARG_FUN_TRUE") not in names_rules
    assert ("nestedParenBy", "DEF_FUN_TRUE") not in names_rules
    assert ("line0ByWithSibling", "DEF_MULTIARG_FUN_TRUE") in names_rules
    assert ("inlineBySameIndentSibling", "DEF_MULTIARG_FUN_TRUE") in names_rules
    assert ("inlineByLine0Sibling", "DEF_MULTIARG_FUN_TRUE") in names_rules

    masked_nested = _strip_by_subblocks("⟨n, (by exact (id h)), (fun _ => True)⟩")
    assert "id h" not in masked_nested
    assert "fun _ => True" in masked_nested


def test_decl_boundaries_example_macro_multiline_attr() -> None:
    src = """
@[simp]
def aDef (x : Nat) : Nat := x + 1

example : Nat :=
  let y := 1
  y

macro "my_tac" : tactic => `(tactic| trivial)

@[simp,
  inline]
theorem bThm : 1 = 1 := by
  rfl
"""
    res = audit_lean_source("Test/Boundaries.lean", src)
    assert res.def_count == 1, f"Expected 1 def, got {res.def_count}"
    assert res.thm_count == 1, f"Expected 1 thm, got {res.thm_count}"
    assert res.thm_rfl == 1


def test_combined_attributes_modifier_order_and_meta_inventory() -> None:
    src = """
import Lean

@[inline, extern "c_helper"]
opaque extFn : Nat → Nat

@[simp, csimp]
theorem simpSwap : 1 = 1 := rfl

attribute [csimp] simpSwap

partial noncomputable def loopHelper (n : Nat) : Nat :=
  loopHelper n

unsafe axiom badAx : False

def runAddDecl (env : Lean.Environment) : IO Unit := do
  let _ := env.addDeclCore 0 default none false
  let _ := env.addDeclWithoutChecking default
  pure ()

run_cmd Lean.logInfo "hi"
elab "custom_elab" : term => do pure (Lean.mkConst ``Nat)
macro "custom_macro" : term => `(1)
initialize myInit : IO.Ref Nat ← IO.mkRef 0
"""
    res = audit_lean_source("Test/TrustCombined.lean", src)
    assert res.escape_counts.get("extern_attr") == 1, res.escape_counts
    assert res.escape_counts.get("csimp_attr") == 2, res.escape_counts
    assert res.escape_counts.get("partial_def") == 1, res.escape_counts
    assert res.escape_counts.get("unsafe_kw") == 1, res.escape_counts
    assert res.escape_counts.get("axiom_decl") == 1, res.escape_counts
    assert res.escape_counts.get("opaque_decl") == 1, res.escape_counts

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        f_path = root / "Test" / "TrustCombined.lean"
        f_path.parent.mkdir(parents=True, exist_ok=True)
        f_path.write_text(src, encoding="utf-8")
        out = _scan_batch((str(root), ["Test/TrustCombined.lean"], ()))
        assert out["escape_counts"]["extern_attr"] == 1
        assert out["escape_counts"]["csimp_attr"] == 2
        assert out["escape_counts"]["env_addDecl"] == 2
        assert out["meta_cmd_counts"]["import_lean_meta"] == 1
        assert out["meta_cmd_counts"]["run_cmd"] == 1
        assert out["meta_cmd_counts"]["elab_decl"] >= 1
        assert out["meta_cmd_counts"]["macro_decl"] >= 1
        assert out["meta_cmd_counts"]["initialize_decl"] == 1

        # Verify prefilter does not skip `import all Lean` / `addAndCompile` even without `:=`
        pref_path = root / "Test" / "PrefilterOnly.lean"
        pref_path.write_text("import all Lean.Elab\n#check addAndCompile\n", encoding="utf-8")
        out_pref = _scan_batch((str(root), ["Test/PrefilterOnly.lean"], ()))
        assert out_pref["meta_cmd_counts"]["import_lean_meta"] == 1, out_pref
        assert out_pref["escape_counts"]["env_addAndCompile"] == 1, out_pref


def test_shim_vs_substantive_proof_and_tactic_keep_tokens_and_type2_hash() -> None:
    src = """
theorem shimA : 1 = 1 := by
  exact Eq.trans (foo bar baz) (qux quux corge)

theorem shimDotExt : True := by
  exact Submodule.ext a b c d e f

theorem shimDotCases : True := by
  exact Foo.cases u v w x y z

theorem shimDotSimpPrime : True := by
  exact Bar.simp' m n o p q r

theorem substA : 1 = 1 := by
  have h1 := foo bar
  rw [h1]
  linarith

theorem substB : 2 = 2 := by
  have z1 := alpha beta
  rw [z1]
  linarith
"""
    res = audit_lean_source("Test/Clones.lean", src)
    by_name = {c.name: c for c in res.clone_records}
    assert by_name["shimA"].is_shim is True
    assert by_name["shimDotExt"].is_shim is True
    assert by_name["shimDotCases"].is_shim is True
    assert by_name["shimDotSimpPrime"].is_shim is True
    assert by_name["substA"].is_shim is False
    assert by_name["substB"].is_shim is False
    assert by_name["substA"].type2_hash == by_name["substB"].type2_hash
    assert by_name["substA"].exact_hash != by_name["substB"].exact_hash


def test_se_topology_dedup_and_low_fanin_high_blast_hub() -> None:
    src_a = """
import Mod.Hub
import Mod.Hub
theorem tA : True := trivial
"""
    res_a = audit_lean_source("Mod/A.lean", src_a)
    assert res_a.imports == ["Mod.Hub", "Mod.Hub"]


def test_externalized_config_and_full_pipeline_pg03_04_05_and_reconciliation() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        root = tmp_path / "src"
        out_dir = tmp_path / "reports"
        root.mkdir(parents=True)
        out_dir.mkdir(parents=True)

        # Two dotted-lemma shims share Type-2 hash; two real tactic proofs stay substantive
        (root / "Main.lean").write_text(
            "import Core.Helper\nimport Core.Helper\ndef mainEntry : Nat := 1\n",
            encoding="utf-8",
        )
        (root / "Core").mkdir()
        (root / "Core" / "Helper.lean").write_text(
            "def vacHelper (x : Nat) : (Nat → Prop) → Nat := fun f => x\n"
            "def vacBad : Nat → Nat → Prop := fun _ _ => True\n"
            "theorem shimCol1 : True := by\n"
            "  exact Foo.qux a b c d e f g\n"
            "theorem shimCol2 : True := by\n"
            "  exact Foo.have u v w x y z w2\n"
            "theorem substCol1 : True := by\n"
            "  have h := a b c\n"
            "  rw [h]\n"
            "  linarith\n"
            "theorem substCol2 : True := by\n"
            "  have z := u v w\n"
            "  rw [z]\n"
            "  linarith\n",
            encoding="utf-8",
        )
        (root / "Dead.lean").write_text("def deadUnused (z : Nat) : Nat := 0\n", encoding="utf-8")

        def run_script(name: str, extra: list[str]) -> None:
            cmd = [sys.executable, "-B", str(SCRIPTS_DIR / name)] + extra
            proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
            assert proc.returncode == 0, f"{name} failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"

        run_script("run_audit.py", ["--root", str(root), "--out-dir", str(out_dir), "--prefix", "t", "--workers", "1"])
        run_script(
            "se_topology.py",
            ["--dag-index", str(out_dir / "t_dag_index.json"), "--out-dir", str(out_dir), "--prefix", "t_se"],
        )
        run_script(
            "lean_dag.py",
            [
                "--root",
                str(root),
                "--dag-index",
                str(out_dir / "t_dag_index.json"),
                "--out-dir",
                str(out_dir),
                "--prefix",
                "t",
                "--entry-config",
                str(CONFIG_PATH),
                "--l3a-only",
                "--workers",
                "1",
            ],
        )
        run_script(
            "run_l25_audit.py",
            [
                "--root",
                str(root),
                "--out-dir",
                str(out_dir),
                "--prefix",
                "t_l25",
                "--shadow-config",
                str(CONFIG_PATH),
                "--workers",
                "1",
            ],
        )

        findings = json.loads((out_dir / "t_findings.json").read_text(encoding="utf-8"))
        assert "provenance" in findings and "source_archive" in findings["provenance"]
        assert str(tmp_path) not in json.dumps(findings)
        coll = findings["clone_cross_bucket_hash_collisions"]
        assert coll["type2_short_8_19"] == 0, coll
        assert coll["type2_total"] == coll["type2_short_8_19"] + coll["type2_ge_20"]
        assert findings["type2_clones"]["proof_shim"]["redundant_duplicate_decls"] == 1
        assert findings["type2_clones"]["proof_substantive"]["redundant_duplicate_decls"] == 1

        summary_md = (out_dir / "t_summary.md").read_text(encoding="utf-8")
        dag_md = (out_dir / "t_l3_dag.md").read_text(encoding="utf-8")
        l25_md = (out_dir / "t_l25.md").read_text(encoding="utf-8")
        se_md = (out_dir / "t_se.md").read_text(encoding="utf-8")

        for label, txt in [("summary", summary_md), ("dag", dag_md), ("l25", l25_md), ("se", se_md)]:
            assert "SAHG" not in txt, f"SAHG brand leaked into {label}"
            assert "Alpha-Normalized" not in txt, f"Alpha-Normalized leaked into {label}"
        assert "## 3." not in dag_md, "Empty section 3 should be omitted under --l3a-only"

        dag_json = json.loads((out_dir / "t_l3_dag.json").read_text(encoding="utf-8"))
        reach = dag_json["reachability_main"]
        assert reach["total_files"] == 3, reach
        assert reach["reachable_files"] == 2, reach
        assert reach["dead_files"] == 1, reach

        se_json = json.loads((out_dir / "t_se.json").read_text(encoding="utf-8"))
        hubs = {h["module"]: h for h in se_json["top_30_hubs_by_blast_radius"]}
        assert hubs["Core.Helper"]["direct_fan_in"] == 1, hubs["Core.Helper"]
        assert hubs["Core.Helper"]["transitive_blast_radius"] == 1, hubs["Core.Helper"]
        assert se_json["max_dag_depth"] == 1, se_json


def main() -> None:
    tests = [
        test_prime_and_unicode_identifiers_not_swallowed,
        test_overix_and_multiarg_vs_singlearg_split,
        test_unicode_param_and_inline_by_and_strict_implicit,
        test_postfix_math_operators_not_false_positive,
        test_by_subblock_inside_def_and_nested_paren_and_line0_indent,
        test_decl_boundaries_example_macro_multiline_attr,
        test_combined_attributes_modifier_order_and_meta_inventory,
        test_shim_vs_substantive_proof_and_tactic_keep_tokens_and_type2_hash,
        test_se_topology_dedup_and_low_fanin_high_blast_hub,
        test_externalized_config_and_full_pipeline_pg03_04_05_and_reconciliation,
    ]
    for fn in tests:
        fn()
    print(f"ALL_UNIT_TESTS_PASSED ({len(tests)} tests)")


if __name__ == "__main__":
    main()
