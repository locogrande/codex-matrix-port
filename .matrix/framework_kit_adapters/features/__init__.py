from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_features"
COMPONENT_ID = ASSET_ID
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "5a5ed69042c7fcebac4c4c109971e0f319d3985d468f1a9164d6f4ae4a5e77e6"
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
_ENGINE_ROOT = _VERSION_ROOT / "source"
ENGINE_ROOT = _ENGINE_ROOT
_MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
MANIFEST_PATH = _MANIFEST_PATH
_SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_MAP_PATH = _SOURCE_MAP_PATH
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/feature_configs.rs', 'src/legacy.rs', 'src/lib.rs', 'src/tests.rs')

def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return (ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == 6
            and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows))

__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
