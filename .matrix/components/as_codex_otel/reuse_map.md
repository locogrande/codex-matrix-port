# Reuse Map - as_codex_otel

Source: `codex-rs/otel`

Expected plan hash: `09de9efa0ca5b64d77d2746b5750624386f6ea061147d08ed966c519a709ab12`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/otel/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/otel/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/otel/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/otel/src/config.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/events/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/events/session_telemetry.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/events/shared.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/client.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/config.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/error.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/names.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/process.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/runtime_metrics.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/tags.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/timer.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/metrics/validation.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/otlp.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/provider.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/targets.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/src/trace_context.rs` | forager | USE | rust source - forager target |
| `codex-rs/otel/tests/harness/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/manager_metrics.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/otel_export_routing_policy.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/otlp_http_loopback.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/runtime_summary.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/send.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/snapshot.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/timing.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/suite/validation.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/otel/tests/tests.rs` | tester | USE | test file - preserve for Tester framework integration |
