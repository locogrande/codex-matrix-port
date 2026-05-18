from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_rmcp_client"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "22fecb0951594ad055a2d963ba102cfd483453f69943aea01e29222a163ad4b0"
EXPECTED_COUNT = 23
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/auth_status.rs', 'src/bin/rmcp_test_server.rs', 'src/bin/test_stdio_server.rs', 'src/bin/test_streamable_http_server.rs', 'src/elicitation_client_service.rs', 'src/executor_process_transport.rs', 'src/http_client_adapter.rs', 'src/in_process_transport.rs', 'src/lib.rs', 'src/logging_client_handler.rs', 'src/oauth.rs', 'src/perform_oauth_login.rs', 'src/program_resolver.rs', 'src/rmcp_client.rs', 'src/stdio_server_launcher.rs', 'src/utils.rs', 'tests/process_group_cleanup.rs', 'tests/resources.rs', 'tests/streamable_http_recovery.rs', 'tests/streamable_http_remote.rs', 'tests/streamable_http_test_support.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
