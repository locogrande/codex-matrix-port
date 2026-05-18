# Reuse Map - as_codex_rollout

Source: `codex-rs/rollout`

Expected plan hash: `017aa7fc5e0d4746c31f8d91ec66b933d5e64bcdc49cc602922acc3535deb3ea`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/rollout/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/rollout/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/rollout/src/config.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/list.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/metadata.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/metadata_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rollout/src/policy.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/recorder.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/recorder_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rollout/src/session_index.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/session_index_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rollout/src/sqlite_metrics.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/state_db.rs` | forager | USE | rust source - forager target |
| `codex-rs/rollout/src/state_db_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rollout/src/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
