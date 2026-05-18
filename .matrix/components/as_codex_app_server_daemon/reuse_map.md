# Reuse Map - as_codex_app_server_daemon

Source: `codex-rs/app-server-daemon`

Expected plan hash: `08ce71efac33e0ccdb0d8a1916fec3d99eb0330ff782844cd04f70121e9a849a`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/app-server-daemon/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/app-server-daemon/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/app-server-daemon/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/app-server-daemon/src/backend/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/backend/pid.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/backend/pid_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/app-server-daemon/src/client.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/managed_install.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/managed_install_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/app-server-daemon/src/settings.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/update_loop.rs` | forager | USE | rust source - forager target |
| `codex-rs/app-server-daemon/src/update_loop_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
