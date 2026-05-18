# Reuse Map - as_codex_analytics

Source: `codex-rs/analytics`

Expected plan hash: `cf3b41b225189a9fb5e0e1f887935b6d49f31daed7cfc67307069232aa866cf1`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/analytics/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/analytics/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/analytics/src/accepted_lines.rs` | forager | USE | rust source - forager target |
| `codex-rs/analytics/src/analytics_client_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/analytics/src/client.rs` | forager | USE | rust source - forager target |
| `codex-rs/analytics/src/client_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/analytics/src/events.rs` | forager | USE | rust source - forager target |
| `codex-rs/analytics/src/facts.rs` | forager | USE | rust source - forager target |
| `codex-rs/analytics/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/analytics/src/reducer.rs` | forager | USE | rust source - forager target |
