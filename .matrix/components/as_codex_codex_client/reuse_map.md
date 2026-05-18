# Reuse Map - as_codex_codex_client

Source: `codex-rs/codex-client`

Expected plan hash: `5ec101f66c6a9affb57febe15e450d0b7309d327740d3c266741c2622995d7dd`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/codex-client/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/codex-client/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/codex-client/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/codex-client/src/bin/custom_ca_probe.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/chatgpt_cloudflare_cookies.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/chatgpt_hosts.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/custom_ca.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/default_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/error.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/request.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/retry.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/sse.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/telemetry.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/src/transport.rs` | forager | USE | rust source - forager target |
| `codex-rs/codex-client/tests/ca_env.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-client/tests/fixtures/test-ca-trusted.pem` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-client/tests/fixtures/test-ca.pem` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/codex-client/tests/fixtures/test-intermediate.pem` | tester | USE | test file - preserve for Tester framework integration |
