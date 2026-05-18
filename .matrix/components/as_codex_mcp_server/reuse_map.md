# Reuse Map - as_codex_mcp_server

Source: `codex-rs/mcp-server`

Expected plan hash: `8f213ea72f95069baac6420d468047682a89c0193b598d392c403d2a4d8d97bc`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/mcp-server/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/mcp-server/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/mcp-server/src/codex_tool_config.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/codex_tool_runner.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/exec_approval.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/main.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/message_processor.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/outgoing_message.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/src/patch_approval.rs` | forager | USE | rust source - forager target |
| `codex-rs/mcp-server/tests/all.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/common/BUILD.bazel` | build_config | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/common/Cargo.toml` | build_config | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/common/lib.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/common/mcp_process.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/common/mock_model_server.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/common/responses.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/suite/codex_tool.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/mcp-server/tests/suite/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
