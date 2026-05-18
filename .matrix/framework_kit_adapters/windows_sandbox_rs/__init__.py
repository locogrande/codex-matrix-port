from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = 'as_codex_windows_sandbox_rs'
COMPONENT_ID = ASSET_ID
ACCEPTED_VERSION = 'v0001_initial'
EXPECTED_PLAN_HASH = '2fb124b9698e80d7e05a1a56ddc5e6c9c0814225ef216825e557ff8b86123c89'
EXPECTED_COUNT = 56
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library/source_assets/components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'build.rs', 'codex-windows-sandbox-setup.manifest', 'sandbox_smoketests.py', 'src/acl.rs', 'src/allow.rs', 'src/audit.rs', 'src/bin/command_runner/main.rs', 'src/bin/command_runner/win.rs', 'src/bin/command_runner/win/cwd_junction.rs', 'src/bin/setup_main/main.rs', 'src/bin/setup_main/win.rs', 'src/bin/setup_main/win/firewall.rs', 'src/bin/setup_main/win/read_acl_mutex.rs', 'src/bin/setup_main/win/sandbox_users.rs', 'src/bin/setup_main/win/setup_runtime_bin.rs', 'src/cap.rs', 'src/conpty/mod.rs', 'src/deny_read_acl.rs', 'src/deny_read_resolver.rs', 'src/deny_read_state.rs', 'src/desktop.rs', 'src/dpapi.rs', 'src/elevated/ipc_framed.rs', 'src/elevated/mod.rs', 'src/elevated/runner_client.rs', 'src/elevated/runner_pipe.rs', 'src/elevated_impl.rs', 'src/env.rs', 'src/helper_materialization.rs', 'src/hide_users.rs', 'src/identity.rs', 'src/lib.rs', 'src/logging.rs', 'src/path_normalization.rs', 'src/policy.rs', 'src/proc_thread_attr.rs', 'src/process.rs', 'src/sandbox_utils.rs', 'src/setup.rs', 'src/setup_error.rs', 'src/spawn_prep.rs', 'src/ssh_config_dependencies.rs', 'src/token.rs', 'src/unified_exec/backends/elevated.rs', 'src/unified_exec/backends/legacy.rs', 'src/unified_exec/backends/mod.rs', 'src/unified_exec/backends/windows_common.rs', 'src/unified_exec/mod.rs', 'src/unified_exec/tests.rs', 'src/wfp.rs', 'src/wfp/filter_specs.rs', 'src/wfp_setup.rs', 'src/winutil.rs', 'src/workspace_acl.rs')

def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r.get("sha256")) for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
