from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_exec_server"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "5714e398dfa64c50bb2528f6ac326c473bc8b5c6aaa46cd4f9ee466a8eb05c30"
EXPECTED_COUNT = 54
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/client.rs', 'src/client/http_client.rs', 'src/client/http_response_body_stream.rs', 'src/client/reqwest_http_client.rs', 'src/client/rpc_http_client.rs', 'src/client_api.rs', 'src/client_transport.rs', 'src/connection.rs', 'src/environment.rs', 'src/environment_provider.rs', 'src/environment_toml.rs', 'src/fs_helper.rs', 'src/fs_helper_main.rs', 'src/fs_sandbox.rs', 'src/lib.rs', 'src/local_file_system.rs', 'src/local_process.rs', 'src/process.rs', 'src/process_id.rs', 'src/proto/codex.exec_server.relay.v1.proto', 'src/proto/codex.exec_server.relay.v1.rs', 'src/protocol.rs', 'src/relay.rs', 'src/relay_proto.rs', 'src/remote.rs', 'src/remote_file_system.rs', 'src/remote_process.rs', 'src/rpc.rs', 'src/runtime_paths.rs', 'src/sandboxed_file_system.rs', 'src/server.rs', 'src/server/file_system_handler.rs', 'src/server/handler.rs', 'src/server/handler/tests.rs', 'src/server/process_handler.rs', 'src/server/processor.rs', 'src/server/registry.rs', 'src/server/session_registry.rs', 'src/server/transport.rs', 'src/server/transport_tests.rs', 'tests/common/exec_server.rs', 'tests/common/mod.rs', 'tests/exec_process.rs', 'tests/file_system.rs', 'tests/health.rs', 'tests/http_client.rs', 'tests/http_request.rs', 'tests/initialize.rs', 'tests/process.rs', 'tests/relay.rs', 'tests/websocket.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
