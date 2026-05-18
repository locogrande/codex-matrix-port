# Reuse Map - as_codex_login

Source: `codex-rs/login`

Expected plan hash: `e345b66faa030288a67a5b6cc607280754008db7de9820e543fcb56b18f7c81e`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/login/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/login/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/login/src/assets/error.html` | office_framework | USE | html source - office_framework target |
| `codex-rs/login/src/assets/success.html` | office_framework | USE | html source - office_framework target |
| `codex-rs/login/src/assets/success_legacy.html` | office_framework | USE | html source - office_framework target |
| `codex-rs/login/src/auth/agent_identity.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/auth_tests.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/src/auth/default_client.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/default_client_tests.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/src/auth/error.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/external_bearer.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/manager.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/mod.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/revoke.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/storage.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth/storage_tests.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/src/auth/util.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/auth_env_telemetry.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/device_code_auth.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/lib.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/pkce.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/server.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/token_data.rs` | office_framework | USE | rust source - office_framework target |
| `codex-rs/login/src/token_data_tests.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/tests/all.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/tests/suite/auth_refresh.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/tests/suite/device_code_login.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/tests/suite/login_server_e2e.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/tests/suite/logout.rs` | office_framework | USE | test file - preserve for Tester framework integration |
| `codex-rs/login/tests/suite/mod.rs` | office_framework | USE | test file - preserve for Tester framework integration |
