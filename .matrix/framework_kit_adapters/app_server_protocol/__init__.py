from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = 'as_codex_app_server_protocol'
ACCEPTED_VERSION = 'v0001_initial'
EXPECTED_PLAN_HASH = 'd6db0df4751c2d5065b31a56303a5d78183b581e84f0459a98e75359bc74d3aa'
EXPECTED_COUNT = 814
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8-sig"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / r["target_relpath"] for r in source_map().get("mappings", [])]
def gate_probe() -> bool:
    if not (MANIFEST_PATH.is_file() and SOURCE_MAP_PATH.is_file() and ENGINE_ROOT.is_dir()): return False
    m, sm = manifest(), source_map()
    rows = sm.get("mappings", [])
    return m.get("status") == "accepted" and m.get("expected_plan_hash") == EXPECTED_PLAN_HASH and m.get("content_hash_root") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r.get("sha256")) for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
