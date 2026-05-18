# Reuse Map - as_codex_exec_server

Source: `codex-rs/exec-server`

Expected plan hash: `5714e398dfa64c50bb2528f6ac326c473bc8b5c6aaa46cd4f9ee466a8eb05c30`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/exec-server/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/exec-server/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/exec-server/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/exec-server/src/client.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/client/http_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/client/http_response_body_stream.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/client/reqwest_http_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/client/rpc_http_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/client_api.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/client_transport.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/connection.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/environment.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/environment_provider.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/environment_toml.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/fs_helper.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/fs_helper_main.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/fs_sandbox.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/local_file_system.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/local_process.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/process.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/process_id.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/proto/codex.exec_server.relay.v1.proto` | unmapped | USE | protobuf source - unmapped target |
| `codex-rs/exec-server/src/proto/codex.exec_server.relay.v1.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/protocol.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/relay.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/relay_proto.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/remote.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/remote_file_system.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/remote_process.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/rpc.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/runtime_paths.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/sandboxed_file_system.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/file_system_handler.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/handler.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/handler/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/src/server/process_handler.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/processor.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/registry.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/session_registry.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/transport.rs` | forager | USE | rust source - forager target |
| `codex-rs/exec-server/src/server/transport_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/common/exec_server.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/common/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/exec_process.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/file_system.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/health.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/http_client.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/http_request.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/initialize.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/process.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/relay.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/exec-server/tests/websocket.rs` | tester | USE | test file - preserve for Tester framework integration |
