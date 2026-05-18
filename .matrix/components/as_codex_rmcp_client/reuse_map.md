# Reuse Map - as_codex_rmcp_client

Source: `codex-rs/rmcp-client`

Expected plan hash: `22fecb0951594ad055a2d963ba102cfd483453f69943aea01e29222a163ad4b0`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/rmcp-client/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/rmcp-client/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/rmcp-client/src/auth_status.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/bin/rmcp_test_server.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/src/bin/test_stdio_server.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/src/bin/test_streamable_http_server.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/src/elicitation_client_service.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/executor_process_transport.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/http_client_adapter.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/in_process_transport.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/logging_client_handler.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/oauth.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/perform_oauth_login.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/program_resolver.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/rmcp_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/stdio_server_launcher.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/src/utils.rs` | forager | USE | rust source - forager target |
| `codex-rs/rmcp-client/tests/process_group_cleanup.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/tests/resources.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/tests/streamable_http_recovery.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/tests/streamable_http_remote.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/rmcp-client/tests/streamable_http_test_support.rs` | tester | USE | test file - preserve for Tester framework integration |
