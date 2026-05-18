# Reuse Map - as_codex_app_server_transport

Source: `codex-rs/app-server-transport`

Expected plan hash: `6296cdb6aec46f02b4ec5a51c8944e28d89dbb42527a165c4acd9f55affa3b2b`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/app-server-transport/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/app-server-transport/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/app-server-transport/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/outgoing_message.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/auth.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/remote_control/client_tracker.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/remote_control/enroll.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/remote_control/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/remote_control/protocol.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/remote_control/segment.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/remote_control/segment_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/app-server-transport/src/transport/remote_control/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/app-server-transport/src/transport/remote_control/websocket.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/stdio.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/unix_socket.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-transport/src/transport/unix_socket_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/app-server-transport/src/transport/websocket.rs` | forager | USE | rust source - forager target |
