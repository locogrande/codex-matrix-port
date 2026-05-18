from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = "as_codex_exec"
COMPONENT_ID = "exec"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "13a802d80d909a7d75dd679ea64239be40b2b43764adb46cce99b82c2d650b90"
ROOT = Path(__file__).resolve().parents[3]
VERSION_ROOT = ROOT / "library/source_assets/components/exec/versions" / ACCEPTED_VERSION
SOURCE_ROOT = VERSION_ROOT / "source"
MANIFEST_PATH = VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'src/cli.rs', 'src/cli_tests.rs', 'src/event_processor.rs', 'src/event_processor_with_human_output.rs', 'src/event_processor_with_human_output_tests.rs', 'src/event_processor_with_jsonl_output.rs', 'src/event_processor_with_jsonl_output_tests.rs', 'src/exec_events.rs', 'src/lib.rs', 'src/lib_tests.rs', 'src/main.rs', 'src/main_tests.rs', 'tests/all.rs', 'tests/event_processor_with_json_output.rs', 'tests/fixtures/apply_patch_freeform_final.txt', 'tests/suite/add_dir.rs', 'tests/suite/apply_patch.rs', 'tests/suite/auth_env.rs', 'tests/suite/ephemeral.rs', 'tests/suite/mcp_required_exit.rs', 'tests/suite/mod.rs', 'tests/suite/originator.rs', 'tests/suite/output_schema.rs', 'tests/suite/prompt_stdin.rs', 'tests/suite/resume.rs', 'tests/suite/sandbox.rs', 'tests/suite/server_error_exit.rs')

def _load(p: Path) -> dict: return json.loads(p.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [SOURCE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", [])
    return manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == len(SOURCE_FILES) and all((p := SOURCE_ROOT / (r.get("target_relpath") or r["path"])).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256"] for r in rows)

__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "EXPECTED_PLAN_HASH", "SOURCE_ROOT", "SOURCE_FILES", "gate_probe", "manifest", "source_map", "source_paths"]
