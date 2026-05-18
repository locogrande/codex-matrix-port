from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_otel"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "09de9efa0ca5b64d77d2746b5750624386f6ea061147d08ed966c519a709ab12"
EXPECTED_COUNT = 33
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'README.md', 'src/config.rs', 'src/events/mod.rs', 'src/events/session_telemetry.rs', 'src/events/shared.rs', 'src/lib.rs', 'src/metrics/client.rs', 'src/metrics/config.rs', 'src/metrics/error.rs', 'src/metrics/mod.rs', 'src/metrics/names.rs', 'src/metrics/process.rs', 'src/metrics/runtime_metrics.rs', 'src/metrics/tags.rs', 'src/metrics/timer.rs', 'src/metrics/validation.rs', 'src/otlp.rs', 'src/provider.rs', 'src/targets.rs', 'src/trace_context.rs', 'tests/harness/mod.rs', 'tests/suite/manager_metrics.rs', 'tests/suite/mod.rs', 'tests/suite/otel_export_routing_policy.rs', 'tests/suite/otlp_http_loopback.rs', 'tests/suite/runtime_summary.rs', 'tests/suite/send.rs', 'tests/suite/snapshot.rs', 'tests/suite/timing.rs', 'tests/suite/validation.rs', 'tests/tests.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
