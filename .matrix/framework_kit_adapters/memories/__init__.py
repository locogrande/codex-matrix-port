from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_memories"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "99aab31bec737ca281525d94608d7e85106376b86b8eba9c8cf19bbe0e0ac86f"
EXPECTED_COUNT = 46
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('README.md', 'mcp/BUILD.bazel', 'mcp/Cargo.toml', 'mcp/src/backend.rs', 'mcp/src/lib.rs', 'mcp/src/local.rs', 'mcp/src/local_tests.rs', 'mcp/src/schema.rs', 'mcp/src/server.rs', 'read/BUILD.bazel', 'read/Cargo.toml', 'read/src/citations.rs', 'read/src/citations_tests.rs', 'read/src/lib.rs', 'read/src/metrics.rs', 'read/src/prompts.rs', 'read/src/prompts_tests.rs', 'read/src/usage.rs', 'read/templates/memories/read_path.md', 'write/BUILD.bazel', 'write/Cargo.toml', 'write/src/control.rs', 'write/src/extensions/ad_hoc.rs', 'write/src/extensions/ad_hoc_tests.rs', 'write/src/extensions/mod.rs', 'write/src/extensions/prune.rs', 'write/src/extensions/prune_tests.rs', 'write/src/guard.rs', 'write/src/guard_tests.rs', 'write/src/lib.rs', 'write/src/metrics.rs', 'write/src/phase1.rs', 'write/src/phase2.rs', 'write/src/prompts.rs', 'write/src/prompts_tests.rs', 'write/src/runtime.rs', 'write/src/start.rs', 'write/src/startup_tests.rs', 'write/src/storage.rs', 'write/src/storage_tests.rs', 'write/src/workspace.rs', 'write/src/workspace_tests.rs', 'write/templates/extensions/ad_hoc/instructions.md', 'write/templates/memories/consolidation.md', 'write/templates/memories/stage_one_input.md', 'write/templates/memories/stage_one_system.md')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
