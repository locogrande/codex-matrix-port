from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_login"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "e345b66faa030288a67a5b6cc607280754008db7de9820e543fcb56b18f7c81e"
EXPECTED_COUNT = 30
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/assets/error.html', 'src/assets/success.html', 'src/assets/success_legacy.html', 'src/auth/agent_identity.rs', 'src/auth/auth_tests.rs', 'src/auth/default_client.rs', 'src/auth/default_client_tests.rs', 'src/auth/error.rs', 'src/auth/external_bearer.rs', 'src/auth/manager.rs', 'src/auth/mod.rs', 'src/auth/revoke.rs', 'src/auth/storage.rs', 'src/auth/storage_tests.rs', 'src/auth/util.rs', 'src/auth_env_telemetry.rs', 'src/device_code_auth.rs', 'src/lib.rs', 'src/pkce.rs', 'src/server.rs', 'src/token_data.rs', 'src/token_data_tests.rs', 'tests/all.rs', 'tests/suite/auth_refresh.rs', 'tests/suite/device_code_login.rs', 'tests/suite/login_server_e2e.rs', 'tests/suite/logout.rs', 'tests/suite/mod.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
