from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_shell_command"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "c64d54cbeb2f0f00c002a99b1089545d3832ab23ecc98d6aac47667276514909"
EXPECTED_COUNT = 14
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/bash.rs', 'src/command_safety/is_dangerous_command.rs', 'src/command_safety/is_safe_command.rs', 'src/command_safety/mod.rs', 'src/command_safety/powershell_parser.ps1', 'src/command_safety/powershell_parser.rs', 'src/command_safety/windows_dangerous_commands.rs', 'src/command_safety/windows_safe_commands.rs', 'src/lib.rs', 'src/parse_command.rs', 'src/powershell.rs', 'src/shell_detect.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
