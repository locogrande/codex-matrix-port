from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_app_server_test_client"
COMPONENT_ID = "app_server_test_client"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "48d6ee35ea649960211e93ba5cc2d4bcc651bbef90491bb011975d165cdde204"
ROOT = Path(__file__).resolve().parents[3]
VERSION_ROOT = ROOT / "library/source_assets/components" / COMPONENT_ID / "versions" / ACCEPTED_VERSION
SOURCE_ROOT = VERSION_ROOT / "source"
MANIFEST_PATH = VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'scripts/live_elicitation_hold.sh', 'src/lib.rs', 'src/main.rs')

def _load(p: Path) -> dict: return json.loads(p.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [SOURCE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", [])
    return manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == len(SOURCE_FILES) and all((p := SOURCE_ROOT / (r.get("target_relpath") or r["path"])).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256"] for r in rows)

__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "EXPECTED_PLAN_HASH", "SOURCE_ROOT", "SOURCE_FILES", "gate_probe", "manifest", "source_map", "source_paths"]
