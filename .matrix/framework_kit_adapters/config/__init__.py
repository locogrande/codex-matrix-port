from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_config"
COMPONENT_ID = ASSET_ID
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "74305282525989fd0c4c0b7fc7de5c09a36b4e17d07e66b6b7b22bcc46e7570b"
EXPECTED_COUNT = 46
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'examples/generate-proto.rs', 'scripts/generate-proto.sh', 'src/cloud_requirements.rs', 'src/config_requirements.rs', 'src/config_toml.rs', 'src/constraint.rs', 'src/diagnostics.rs', 'src/fingerprint.rs', 'src/hook_config.rs', 'src/hooks_tests.rs', 'src/host_name.rs', 'src/key_aliases.rs', 'src/lib.rs', 'src/loader/README.md', 'src/loader/layer_io.rs', 'src/loader/macos.rs', 'src/loader/mod.rs', 'src/loader/tests.rs', 'src/marketplace_edit.rs', 'src/mcp_edit.rs', 'src/mcp_edit_tests.rs', 'src/mcp_types.rs', 'src/mcp_types_tests.rs', 'src/merge.rs', 'src/merge_tests.rs', 'src/overrides.rs', 'src/permissions_toml.rs', 'src/plugin_edit.rs', 'src/profile_toml.rs', 'src/project_root_markers.rs', 'src/requirements_exec_policy.rs', 'src/schema.rs', 'src/skills_config.rs', 'src/state.rs', 'src/state_tests.rs', 'src/strict_config.rs', 'src/strict_config_tests.rs', 'src/thread_config.rs', 'src/thread_config/proto/codex.thread_config.v1.proto', 'src/thread_config/proto/codex.thread_config.v1.rs', 'src/thread_config/remote.rs', 'src/tui_keymap.rs', 'src/types.rs', 'src/types_tests.rs')

def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r.get("sha256")) for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
