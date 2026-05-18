from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_terminal_detection"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "5ea5e4b199e2769174b9b6871e87e65dcc41a438e856d606dbb026110822bae6"
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ("BUILD.bazel", "Cargo.toml", "src/lib.rs", "src/terminal_tests.rs")


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
    return (ENGINE_ROOT.is_dir() and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == 4
            and all((p := ENGINE_ROOT / r["target_relpath"]).is_file()
                    and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows))


__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
