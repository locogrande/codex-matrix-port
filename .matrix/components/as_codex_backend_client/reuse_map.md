# Reuse Map - as_codex_backend_client

Source: `codex-rs/backend-client`

Expected plan hash: `d8e2c457eff1754c7f4a48d4eb32e44a4551be8f2cb917141f005b23204f0ca6`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/backend-client/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/backend-client/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/backend-client/src/client.rs` | forager | USE | rust source - forager target |
| `codex-rs/backend-client/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/backend-client/src/types.rs` | forager | USE | rust source - forager target |
| `codex-rs/backend-client/tests/fixtures/task_details_with_diff.json` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/backend-client/tests/fixtures/task_details_with_error.json` | tester | USE | test file - preserve for Tester framework integration |
