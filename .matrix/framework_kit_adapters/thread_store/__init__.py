from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_thread_store"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "9ad7e6048abb1f74e9c90f1b6217a836d4d736e80b0a43f3ddd8aee17743e9b0"
EXPECTED_COUNT = 20
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/error.rs', 'src/in_memory.rs', 'src/lib.rs', 'src/live_thread.rs', 'src/local/archive_thread.rs', 'src/local/create_thread.rs', 'src/local/helpers.rs', 'src/local/list_threads.rs', 'src/local/live_writer.rs', 'src/local/mod.rs', 'src/local/read_thread.rs', 'src/local/test_support.rs', 'src/local/unarchive_thread.rs', 'src/local/update_thread_metadata.rs', 'src/store.rs', 'src/thread_metadata_sync.rs', 'src/types.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
