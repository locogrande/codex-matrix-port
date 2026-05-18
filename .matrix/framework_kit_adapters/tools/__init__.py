from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_tools"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "155ce43c261a7b51aab24f1e6f773efe9ffc9e808f11a9447310ac5830396d2e"
EXPECTED_COUNT = 31
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/code_mode.rs', 'src/code_mode_tests.rs', 'src/dynamic_tool.rs', 'src/dynamic_tool_tests.rs', 'src/function_call_error.rs', 'src/image_detail.rs', 'src/image_detail_tests.rs', 'src/json_schema.rs', 'src/json_schema_tests.rs', 'src/lib.rs', 'src/mcp_tool.rs', 'src/mcp_tool_tests.rs', 'src/request_plugin_install.rs', 'src/request_plugin_install_tests.rs', 'src/responses_api.rs', 'src/responses_api_tests.rs', 'src/tool_call.rs', 'src/tool_config.rs', 'src/tool_config_tests.rs', 'src/tool_definition.rs', 'src/tool_definition_tests.rs', 'src/tool_discovery.rs', 'src/tool_discovery_tests.rs', 'src/tool_executor.rs', 'src/tool_output.rs', 'src/tool_payload.rs', 'src/tool_spec.rs', 'src/tool_spec_tests.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
