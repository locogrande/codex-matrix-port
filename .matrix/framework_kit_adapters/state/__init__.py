from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_state"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "30b3be8b5e935a0ecd2047c711921322d61be9064254d430910ca7a582dce6a2"
EXPECTED_COUNT = 60
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'logs_migrations/0001_logs.sql', 'logs_migrations/0002_logs_feedback_log_body.sql', 'migrations/0001_threads.sql', 'migrations/0002_logs.sql', 'migrations/0003_logs_thread_id.sql', 'migrations/0004_thread_dynamic_tools.sql', 'migrations/0005_threads_cli_version.sql', 'migrations/0006_memories.sql', 'migrations/0007_threads_first_user_message.sql', 'migrations/0008_backfill_state.sql', 'migrations/0009_stage1_outputs_rollout_slug.sql', 'migrations/0010_logs_process_id.sql', 'migrations/0011_logs_partition_prune_indexes.sql', 'migrations/0012_logs_estimated_bytes.sql', 'migrations/0013_threads_agent_nickname.sql', 'migrations/0014_agent_jobs.sql', 'migrations/0015_agent_jobs_max_runtime_seconds.sql', 'migrations/0016_memory_usage.sql', 'migrations/0017_phase2_selection_flag.sql', 'migrations/0018_phase2_selection_snapshot.sql', 'migrations/0019_thread_dynamic_tools_defer_loading.sql', 'migrations/0020_threads_model_reasoning_effort.sql', 'migrations/0021_thread_spawn_edges.sql', 'migrations/0022_threads_agent_path.sql', 'migrations/0023_drop_logs.sql', 'migrations/0024_remote_control_enrollments.sql', 'migrations/0025_thread_timestamps_millis.sql', 'migrations/0026_thread_dynamic_tools_namespace.sql', 'migrations/0027_threads_cwd_sort_indexes.sql', 'migrations/0028_device_key_bindings.sql', 'migrations/0029_thread_goals.sql', 'migrations/0030_threads_thread_source.sql', 'migrations/0031_drop_device_key_bindings.sql', 'migrations/0032_threads_preview.sql', 'src/bin/logs_client.rs', 'src/extract.rs', 'src/lib.rs', 'src/log_db.rs', 'src/migrations.rs', 'src/model/agent_job.rs', 'src/model/backfill_state.rs', 'src/model/graph.rs', 'src/model/log.rs', 'src/model/memories.rs', 'src/model/mod.rs', 'src/model/thread_goal.rs', 'src/model/thread_metadata.rs', 'src/paths.rs', 'src/runtime.rs', 'src/runtime/agent_jobs.rs', 'src/runtime/backfill.rs', 'src/runtime/goals.rs', 'src/runtime/logs.rs', 'src/runtime/memories.rs', 'src/runtime/remote_control.rs', 'src/runtime/test_support.rs', 'src/runtime/threads.rs', 'src/telemetry.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
