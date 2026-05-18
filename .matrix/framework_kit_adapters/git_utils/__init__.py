from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_git_utils"
COMPONENT_DIR = "git_utils"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "f15a1ce1550192e5d9c1b45df3ae9e646042254ac4331f9f3cc647931cd55af7"
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / COMPONENT_DIR / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ("BUILD.bazel", "Cargo.toml", "README.md", "src/apply.rs", "src/baseline.rs", "src/branch.rs", "src/errors.rs", "src/info.rs", "src/lib.rs", "src/operations.rs", "src/platform.rs")


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def manifest() -> dict:
    return _load(MANIFEST_PATH)


def source_map() -> dict:
    return _load(SOURCE_MAP_PATH)


def source_paths() -> list[Path]:
    return [ENGINE_ROOT / p for p in SOURCE_FILES]


def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return (ENGINE_ROOT.is_dir() and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == 11
            and all((p := ENGINE_ROOT / (r.get("target_relpath") or r["path"])).is_file()
                    and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r["sha256"]) for r in rows))


__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_DIR", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
