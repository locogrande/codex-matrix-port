from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_README.md"
COMPONENT_ID = "root_readme_md"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "93cfe0b63efcb334bb09f8cfe7c46e19043deee08825a5582631f20cd3d89eeb"
ROOT = Path(__file__).resolve().parents[3]
VERSION_ROOT = ROOT / "library/source_assets/components/root_readme_md/versions" / ACCEPTED_VERSION
SOURCE_ROOT = VERSION_ROOT / "source"
MANIFEST_PATH = VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('README.md',)

def _load(p: Path) -> dict: return json.loads(p.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [SOURCE_ROOT / p for p in SOURCE_FILES]
def asset_info() -> dict: return {'asset_id': ASSET_ID, 'component_id': COMPONENT_ID, 'version_id': ACCEPTED_VERSION, 'files': SOURCE_FILES}
def gate_probe() -> bool:
    rows = source_map().get("mappings", [])
    return manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == len(SOURCE_FILES) and all((p := SOURCE_ROOT / (r.get("target_relpath") or r["path"])).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256"] for r in rows)

__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "EXPECTED_PLAN_HASH", "SOURCE_ROOT", "SOURCE_FILES", "asset_info", "gate_probe", "manifest", "source_map", "source_paths"]
