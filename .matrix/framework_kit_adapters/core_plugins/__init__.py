from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_core_plugins"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "5e5163ba0b7d04c271e143a442ddabda2b4e3644b4a0e5036a1ee7074d4755ac"
EXPECTED_COUNT = 35
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/installed_marketplaces.rs', 'src/lib.rs', 'src/loader.rs', 'src/loader_tests.rs', 'src/manager.rs', 'src/manager_tests.rs', 'src/manifest.rs', 'src/marketplace.rs', 'src/marketplace_add.rs', 'src/marketplace_add/install.rs', 'src/marketplace_add/metadata.rs', 'src/marketplace_add/source.rs', 'src/marketplace_remove.rs', 'src/marketplace_tests.rs', 'src/marketplace_upgrade.rs', 'src/marketplace_upgrade/activation.rs', 'src/marketplace_upgrade/git.rs', 'src/remote.rs', 'src/remote/remote_installed_plugin_sync.rs', 'src/remote/share.rs', 'src/remote/share/checkout.rs', 'src/remote/share/local_paths.rs', 'src/remote/share/tests.rs', 'src/remote_bundle.rs', 'src/remote_legacy.rs', 'src/startup_remote_sync.rs', 'src/startup_remote_sync_tests.rs', 'src/startup_sync.rs', 'src/startup_sync_tests.rs', 'src/store.rs', 'src/store_tests.rs', 'src/test_support.rs', 'src/toggles.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
