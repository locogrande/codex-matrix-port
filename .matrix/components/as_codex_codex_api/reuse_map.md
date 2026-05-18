# Reuse Map - as_codex_codex_api

Source: `codex-rs/codex-api`

Expected plan hash: `0585b2aa659501a3d18de2c0640894505b9acd86817f2e36e76654e78ee6a9f4`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/codex-api/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/codex-api/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/codex-api/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/codex-api/src/api_bridge.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/api_bridge_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-api/src/auth.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/common.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/compact.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/memories.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/models.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_call.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/methods.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/methods_common.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/methods_v1.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/methods_v2.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/protocol.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/protocol_common.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/protocol_v1.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/realtime_websocket/protocol_v2.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/responses.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/responses_websocket.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/endpoint/session.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/error.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/files.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/provider.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/rate_limits.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/requests/headers.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/requests/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/requests/responses.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/sse/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/sse/responses.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/src/telemetry.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-api/tests/clients.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-api/tests/models_integration.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-api/tests/realtime_websocket_e2e.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-api/tests/sse_end_to_end.rs` | tester | USE | test file - preserve for Tester framework integration |
