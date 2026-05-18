from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_chatgpt"
COMPONENT_ID = "chatgpt"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "fd64d535850f29b5c45fddf6ca2dc1bc55b40410e05f56c5cc8458f4f4484ad7"
ROOT = Path(__file__).resolve().parents[3]
VERSION_ROOT = ROOT / "library/source_assets/components/chatgpt/versions" / ACCEPTED_VERSION
SOURCE_ROOT = VERSION_ROOT / "source"
MANIFEST_PATH = VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/apply_command.rs', 'src/chatgpt_client.rs', 'src/connectors.rs', 'src/get_task.rs', 'src/lib.rs', 'src/workspace_settings.rs', 'src/workspace_settings_tests.rs', 'tests/all.rs', 'tests/suite/apply_command_e2e.rs', 'tests/suite/mod.rs', 'tests/task_turn_fixture.json')

def _load(p: Path) -> dict: return json.loads(p.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [SOURCE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", [])
    return manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == len(SOURCE_FILES) and all((p := SOURCE_ROOT / (r.get("target_relpath") or r["path"])).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256"] for r in rows)

__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "EXPECTED_PLAN_HASH", "SOURCE_ROOT", "SOURCE_FILES", "gate_probe", "manifest", "source_map", "source_paths"]
