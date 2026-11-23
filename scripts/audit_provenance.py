"""Shared provenance (PG-04) & path sanitization (PG-03) helpers for Lean audit scripts."""

from __future__ import annotations

import hashlib
from pathlib import Path

_CORE_SCRIPTS = (
    "lean_lexer.py",
    "lean_decl_parser.py",
    "lean_probes.py",
    "run_audit.py",
    "se_topology.py",
    "lean_dag.py",
    "run_l25_audit.py",
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def sanitize_root_label(root: Path) -> str:
    """Return a relative/logical corpus label without leaking host drive or user home paths (PG-03)."""
    parts = root.resolve().parts
    for anchor in ("corpus", "lean", "src"):
        if anchor in parts:
            idx = parts.index(anchor)
            return "/".join(parts[idx:])
    return root.name or "corpus"


def collect_provenance(root: Path) -> dict:
    scripts_dir = Path(__file__).resolve().parent
    script_hashes = {
        name: sha256_file(scripts_dir / name)
        for name in _CORE_SCRIPTS
        if (scripts_dir / name).is_file()
    }
    combined = hashlib.sha256(
        "\n".join(f"{k}:{v}" for k, v in sorted(script_hashes.items())).encode("utf-8")
    ).hexdigest()

    toolchain = None
    for candidate in (root.parent / "lean-toolchain", root / "lean-toolchain"):
        if candidate.is_file():
            toolchain = candidate.read_text(encoding="utf-8").strip()
            break

    archive_info = None
    for parent in root.resolve().parents:
        tar_candidate = parent / "raw" / "lean.tar.gz"
        if tar_candidate.is_file():
            archive_info = {
                "file": "raw/lean.tar.gz",
                "bytes": tar_candidate.stat().st_size,
                "sha256": sha256_file(tar_candidate),
            }
            break

    return {
        "corpus_label": sanitize_root_label(root),
        "probe_bundle_sha256": combined,
        "script_sha256": script_hashes,
        "lean_toolchain": toolchain,
        "source_archive": archive_info,
    }
