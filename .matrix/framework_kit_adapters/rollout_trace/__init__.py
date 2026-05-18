from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_rollout_trace"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "8133d902e952487f51e4d5f3b7cca2c1d1960cafb47696c677bb3d7d89cf1cb1"
EXPECTED_COUNT = 36
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/bundle.rs', 'src/code_cell.rs', 'src/compaction.rs', 'src/inference.rs', 'src/lib.rs', 'src/mcp.rs', 'src/model/conversation.rs', 'src/model/mod.rs', 'src/model/runtime.rs', 'src/model/session.rs', 'src/payload.rs', 'src/protocol_event.rs', 'src/raw_event.rs', 'src/reducer/code_cell.rs', 'src/reducer/code_cell_tests.rs', 'src/reducer/compaction.rs', 'src/reducer/conversation.rs', 'src/reducer/conversation/normalize.rs', 'src/reducer/conversation_tests.rs', 'src/reducer/inference.rs', 'src/reducer/inference_tests.rs', 'src/reducer/mod.rs', 'src/reducer/test_support.rs', 'src/reducer/thread.rs', 'src/reducer/tool.rs', 'src/reducer/tool/agents.rs', 'src/reducer/tool/agents_tests.rs', 'src/reducer/tool/terminal.rs', 'src/reducer/tool/terminal_tests.rs', 'src/thread.rs', 'src/thread_tests.rs', 'src/tool_dispatch.rs', 'src/writer.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
