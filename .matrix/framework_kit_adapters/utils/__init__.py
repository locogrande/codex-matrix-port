from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = 'as_codex_utils'
COMPONENT_ID = ASSET_ID
ACCEPTED_VERSION = 'v0001_initial'
EXPECTED_PLAN_HASH = 'eccd759e0aca25b189fffbc3cd4ec30a3666e612dfe779139b589a1b08c2b009'
EXPECTED_COUNT = 111
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library/source_assets/components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('absolute-path/BUILD.bazel', 'absolute-path/Cargo.toml', 'absolute-path/src/absolutize.rs', 'absolute-path/src/lib.rs', 'approval-presets/BUILD.bazel', 'approval-presets/Cargo.toml', 'approval-presets/src/lib.rs', 'cache/BUILD.bazel', 'cache/Cargo.toml', 'cache/src/lib.rs', 'cargo-bin/BUILD.bazel', 'cargo-bin/Cargo.toml', 'cargo-bin/README.md', 'cargo-bin/repo_root.marker', 'cargo-bin/src/lib.rs', 'cli/BUILD.bazel', 'cli/Cargo.toml', 'cli/src/approval_mode_cli_arg.rs', 'cli/src/config_override.rs', 'cli/src/format_env_display.rs', 'cli/src/lib.rs', 'cli/src/resume_command.rs', 'cli/src/sandbox_mode_cli_arg.rs', 'cli/src/shared_options.rs', 'elapsed/BUILD.bazel', 'elapsed/Cargo.toml', 'elapsed/src/lib.rs', 'fuzzy-match/BUILD.bazel', 'fuzzy-match/Cargo.toml', 'fuzzy-match/src/lib.rs', 'home-dir/BUILD.bazel', 'home-dir/Cargo.toml', 'home-dir/src/lib.rs', 'image/BUILD.bazel', 'image/Cargo.toml', 'image/src/error.rs', 'image/src/lib.rs', 'json-to-toml/BUILD.bazel', 'json-to-toml/Cargo.toml', 'json-to-toml/src/lib.rs', 'oss/BUILD.bazel', 'oss/Cargo.toml', 'oss/src/lib.rs', 'output-truncation/BUILD.bazel', 'output-truncation/Cargo.toml', 'output-truncation/src/lib.rs', 'output-truncation/src/truncate_tests.rs', 'path-utils/BUILD.bazel', 'path-utils/Cargo.toml', 'path-utils/src/env.rs', 'path-utils/src/lib.rs', 'path-utils/src/path_utils_tests.rs', 'plugins/BUILD.bazel', 'plugins/Cargo.toml', 'plugins/src/lib.rs', 'plugins/src/mcp_connector.rs', 'plugins/src/mention_syntax.rs', 'plugins/src/plugin_namespace.rs', 'pty/BUILD.bazel', 'pty/Cargo.toml', 'pty/README.md', 'pty/src/lib.rs', 'pty/src/pipe.rs', 'pty/src/process.rs', 'pty/src/process_group.rs', 'pty/src/pty.rs', 'pty/src/tests.rs', 'pty/src/win/conpty.rs', 'pty/src/win/mod.rs', 'pty/src/win/procthreadattr.rs', 'pty/src/win/psuedocon.rs', 'readiness/BUILD.bazel', 'readiness/Cargo.toml', 'readiness/src/lib.rs', 'rustls-provider/BUILD.bazel', 'rustls-provider/Cargo.toml', 'rustls-provider/src/lib.rs', 'sandbox-summary/BUILD.bazel', 'sandbox-summary/Cargo.toml', 'sandbox-summary/src/config_summary.rs', 'sandbox-summary/src/lib.rs', 'sandbox-summary/src/sandbox_summary.rs', 'sleep-inhibitor/BUILD.bazel', 'sleep-inhibitor/Cargo.toml', 'sleep-inhibitor/src/dummy.rs', 'sleep-inhibitor/src/iokit_bindings.rs', 'sleep-inhibitor/src/lib.rs', 'sleep-inhibitor/src/linux_inhibitor.rs', 'sleep-inhibitor/src/macos.rs', 'sleep-inhibitor/src/windows_inhibitor.rs', 'stream-parser/BUILD.bazel', 'stream-parser/Cargo.toml', 'stream-parser/README.md', 'stream-parser/src/assistant_text.rs', 'stream-parser/src/citation.rs', 'stream-parser/src/inline_hidden_tag.rs', 'stream-parser/src/lib.rs', 'stream-parser/src/proposed_plan.rs', 'stream-parser/src/stream_text.rs', 'stream-parser/src/tagged_line_parser.rs', 'stream-parser/src/utf8_stream.rs', 'string/BUILD.bazel', 'string/Cargo.toml', 'string/src/json.rs', 'string/src/lib.rs', 'string/src/truncate.rs', 'string/src/truncate/tests.rs', 'template/BUILD.bazel', 'template/Cargo.toml', 'template/README.md', 'template/src/lib.rs')

def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r.get("sha256")) for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
