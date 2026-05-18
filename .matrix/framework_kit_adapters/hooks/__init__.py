from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_hooks"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "496fefbb089fba41026a6a94ab3b55c26c7ce17a1be0fefaf1fa4b07f1efcdba"
EXPECTED_COUNT = 44
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'schema/generated/permission-request.command.input.schema.json', 'schema/generated/permission-request.command.output.schema.json', 'schema/generated/post-compact.command.input.schema.json', 'schema/generated/post-compact.command.output.schema.json', 'schema/generated/post-tool-use.command.input.schema.json', 'schema/generated/post-tool-use.command.output.schema.json', 'schema/generated/pre-compact.command.input.schema.json', 'schema/generated/pre-compact.command.output.schema.json', 'schema/generated/pre-tool-use.command.input.schema.json', 'schema/generated/pre-tool-use.command.output.schema.json', 'schema/generated/session-start.command.input.schema.json', 'schema/generated/session-start.command.output.schema.json', 'schema/generated/stop.command.input.schema.json', 'schema/generated/stop.command.output.schema.json', 'schema/generated/user-prompt-submit.command.input.schema.json', 'schema/generated/user-prompt-submit.command.output.schema.json', 'src/bin/write_hooks_schema_fixtures.rs', 'src/config_rules.rs', 'src/declarations.rs', 'src/engine/command_runner.rs', 'src/engine/discovery.rs', 'src/engine/dispatcher.rs', 'src/engine/mod.rs', 'src/engine/mod_tests.rs', 'src/engine/output_parser.rs', 'src/engine/schema_loader.rs', 'src/events/common.rs', 'src/events/compact.rs', 'src/events/mod.rs', 'src/events/permission_request.rs', 'src/events/post_tool_use.rs', 'src/events/pre_tool_use.rs', 'src/events/session_start.rs', 'src/events/stop.rs', 'src/events/user_prompt_submit.rs', 'src/legacy_notify.rs', 'src/lib.rs', 'src/output_spill.rs', 'src/output_spill_tests.rs', 'src/registry.rs', 'src/schema.rs', 'src/types.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
