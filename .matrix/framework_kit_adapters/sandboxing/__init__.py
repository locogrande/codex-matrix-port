from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_sandboxing"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "efc3576d1d9c7030a6a73a958560ac01166e19e47c2974569f10c337d1745aa3"
EXPECTED_COUNT = 16
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/bwrap.rs', 'src/bwrap_tests.rs', 'src/landlock.rs', 'src/landlock_tests.rs', 'src/lib.rs', 'src/manager.rs', 'src/manager_tests.rs', 'src/policy_transforms.rs', 'src/policy_transforms_tests.rs', 'src/restricted_read_only_platform_defaults.sbpl', 'src/seatbelt.rs', 'src/seatbelt_base_policy.sbpl', 'src/seatbelt_network_policy.sbpl', 'src/seatbelt_tests.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
