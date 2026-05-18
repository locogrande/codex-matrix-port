from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_models_manager"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "9128b3eb740a3abc4b4f0b0a9794d8d7779269bfeea0adc1dcd6e3e9625e426e"
EXPECTED_COUNT = 16
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'models.json', 'prompt.md', 'src/cache.rs', 'src/collaboration_mode_presets.rs', 'src/collaboration_mode_presets_tests.rs', 'src/config.rs', 'src/lib.rs', 'src/manager.rs', 'src/manager_tests.rs', 'src/model_info.rs', 'src/model_info_overrides_tests.rs', 'src/model_info_tests.rs', 'src/model_presets.rs', 'src/test_support.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
