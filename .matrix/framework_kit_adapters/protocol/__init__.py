from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_protocol"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "4040024239034908c5a66aded992eea62706aa4def42d52d13d501c4404065bd"
EXPECTED_COUNT = 34
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/account.rs', 'src/agent_path.rs', 'src/approvals.rs', 'src/auth.rs', 'src/config_types.rs', 'src/dynamic_tools.rs', 'src/error.rs', 'src/error_tests.rs', 'src/exec_output.rs', 'src/exec_output_tests.rs', 'src/items.rs', 'src/lib.rs', 'src/mcp.rs', 'src/mcp_approval_meta.rs', 'src/memory_citation.rs', 'src/models.rs', 'src/network_policy.rs', 'src/num_format.rs', 'src/openai_models.rs', 'src/parse_command.rs', 'src/permissions.rs', 'src/plan_tool.rs', 'src/prompts/base_instructions/default.md', 'src/protocol.rs', 'src/request_permissions.rs', 'src/request_user_input.rs', 'src/session_id.rs', 'src/shell_environment.rs', 'src/thread_id.rs', 'src/tool_name.rs', 'src/user_input.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
