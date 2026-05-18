from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_codex_backend_openapi_models"
COMPONENT_ID = "codex_backend_openapi_models"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "4aa6947ba4a6d242b57a3e3101cd4705eedfe4e8e676253cd8d4796488414659"
ROOT = Path(__file__).resolve().parents[3]
VERSION_ROOT = ROOT / "library/source_assets/components/codex_backend_openapi_models/versions" / ACCEPTED_VERSION
SOURCE_ROOT = VERSION_ROOT / "source"
MANIFEST_PATH = VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/lib.rs', 'src/models/additional_rate_limit_details.rs', 'src/models/code_task_details_response.rs', 'src/models/config_file_response.rs', 'src/models/credit_status_details.rs', 'src/models/external_pull_request_response.rs', 'src/models/git_pull_request.rs', 'src/models/mod.rs', 'src/models/paginated_list_task_list_item_.rs', 'src/models/rate_limit_status_details.rs', 'src/models/rate_limit_status_payload.rs', 'src/models/rate_limit_window_snapshot.rs', 'src/models/task_list_item.rs', 'src/models/task_response.rs')

def _load(p: Path) -> dict: return json.loads(p.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [SOURCE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == len(SOURCE_FILES) and all((p := SOURCE_ROOT / (r.get("target_relpath") or r["path"])).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256") or r.get("sha256_full")) for r in rows)

__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "EXPECTED_PLAN_HASH", "SOURCE_ROOT", "SOURCE_FILES", "gate_probe", "manifest", "source_map", "source_paths"]
