from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_ext"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "a5678f3919bb1ed6b337e7c82c7f998b75a05f578baa1f7aaa8094a9a1eaddcf"
EXPECTED_COUNT = 33
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('extension-api/BUILD.bazel', 'extension-api/Cargo.toml', 'extension-api/examples/enabled_extensions.rs', 'extension-api/examples/enabled_extensions/shared_state_extension.rs', 'extension-api/notes.md', 'extension-api/src/capabilities/agent.rs', 'extension-api/src/capabilities/mod.rs', 'extension-api/src/contributors.rs', 'extension-api/src/contributors/prompt.rs', 'extension-api/src/contributors/thread_lifecycle.rs', 'extension-api/src/contributors/turn_lifecycle.rs', 'extension-api/src/lib.rs', 'extension-api/src/registry.rs', 'extension-api/src/state.rs', 'guardian/BUILD.bazel', 'guardian/Cargo.toml', 'guardian/src/lib.rs', 'memories/BUILD.bazel', 'memories/Cargo.toml', 'memories/src/backend.rs', 'memories/src/extension.rs', 'memories/src/lib.rs', 'memories/src/local.rs', 'memories/src/local/list.rs', 'memories/src/local/path.rs', 'memories/src/local/read.rs', 'memories/src/local/search.rs', 'memories/src/schema.rs', 'memories/src/tests.rs', 'memories/src/tools/list.rs', 'memories/src/tools/mod.rs', 'memories/src/tools/read.rs', 'memories/src/tools/search.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
