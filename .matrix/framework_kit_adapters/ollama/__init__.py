from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_ollama"
COMPONENT_ID = "ollama"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "bf2af29a405ca0e5383fa00fc8990700a8bdf9612971b48e6bd3082df1307e52"
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / COMPONENT_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ("BUILD.bazel", "Cargo.toml", "src/client.rs", "src/lib.rs", "src/parser.rs", "src/pull.rs", "src/url.rs")


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def manifest() -> dict:
    return _load(MANIFEST_PATH)


def source_map() -> dict:
    return _load(SOURCE_MAP_PATH)


def source_paths() -> list[Path]:
    return [ENGINE_ROOT / p for p in SOURCE_FILES]


def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    if not (ENGINE_ROOT.is_dir()
            and manifest().get("status") == "accepted"
            and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH
            and len(rows) == 7):
        return False
    for r in rows:
        p = ENGINE_ROOT / r["target_relpath"]
        expected = r.get("sha256_full") or r.get("sha256")
        if not p.is_file() or not expected or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
            return False
    return True


__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
