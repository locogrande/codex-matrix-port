from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_codex_api"
COMPONENT_ID = ASSET_ID
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "0585b2aa659501a3d18de2c0640894505b9acd86817f2e36e76654e78ee6a9f4"
EXPECTED_COUNT = 39
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/api_bridge.rs', 'src/api_bridge_tests.rs', 'src/auth.rs', 'src/common.rs', 'src/endpoint/compact.rs', 'src/endpoint/memories.rs', 'src/endpoint/mod.rs', 'src/endpoint/models.rs', 'src/endpoint/realtime_call.rs', 'src/endpoint/realtime_websocket/methods.rs', 'src/endpoint/realtime_websocket/methods_common.rs', 'src/endpoint/realtime_websocket/methods_v1.rs', 'src/endpoint/realtime_websocket/methods_v2.rs', 'src/endpoint/realtime_websocket/mod.rs', 'src/endpoint/realtime_websocket/protocol.rs', 'src/endpoint/realtime_websocket/protocol_common.rs', 'src/endpoint/realtime_websocket/protocol_v1.rs', 'src/endpoint/realtime_websocket/protocol_v2.rs', 'src/endpoint/responses.rs', 'src/endpoint/responses_websocket.rs', 'src/endpoint/session.rs', 'src/error.rs', 'src/files.rs', 'src/lib.rs', 'src/provider.rs', 'src/rate_limits.rs', 'src/requests/headers.rs', 'src/requests/mod.rs', 'src/requests/responses.rs', 'src/sse/mod.rs', 'src/sse/responses.rs', 'src/telemetry.rs', 'tests/clients.rs', 'tests/models_integration.rs', 'tests/realtime_websocket_e2e.rs', 'tests/sse_end_to_end.rs')

def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r.get("sha256")) for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
