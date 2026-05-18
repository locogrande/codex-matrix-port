# Reuse Map - as_codex_state

Source: `codex-rs/state`

Expected plan hash: `30b3be8b5e935a0ecd2047c711921322d61be9064254d430910ca7a582dce6a2`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/state/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/state/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/state/logs_migrations/0001_logs.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/logs_migrations/0002_logs_feedback_log_body.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0001_threads.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0002_logs.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0003_logs_thread_id.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0004_thread_dynamic_tools.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0005_threads_cli_version.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0006_memories.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0007_threads_first_user_message.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0008_backfill_state.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0009_stage1_outputs_rollout_slug.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0010_logs_process_id.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0011_logs_partition_prune_indexes.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0012_logs_estimated_bytes.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0013_threads_agent_nickname.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0014_agent_jobs.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0015_agent_jobs_max_runtime_seconds.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0016_memory_usage.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0017_phase2_selection_flag.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0018_phase2_selection_snapshot.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0019_thread_dynamic_tools_defer_loading.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0020_threads_model_reasoning_effort.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0021_thread_spawn_edges.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0022_threads_agent_path.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0023_drop_logs.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0024_remote_control_enrollments.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0025_thread_timestamps_millis.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0026_thread_dynamic_tools_namespace.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0027_threads_cwd_sort_indexes.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0028_device_key_bindings.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0029_thread_goals.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0030_threads_thread_source.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0031_drop_device_key_bindings.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/migrations/0032_threads_preview.sql` | netrix_extension | USE | sql source - netrix_extension target |
| `codex-rs/state/src/bin/logs_client.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/extract.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/lib.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/log_db.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/migrations.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/agent_job.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/backfill_state.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/graph.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/log.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/memories.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/mod.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/thread_goal.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/model/thread_metadata.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/paths.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/agent_jobs.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/backfill.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/goals.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/logs.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/memories.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/remote_control.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/runtime/test_support.rs` | netrix_extension | USE | test file - preserve for Tester framework integration |
| `codex-rs/state/src/runtime/threads.rs` | netrix_extension | USE | rust source - netrix_extension target |
| `codex-rs/state/src/telemetry.rs` | netrix_extension | USE | rust source - netrix_extension target |
