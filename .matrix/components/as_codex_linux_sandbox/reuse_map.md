# Reuse Map - as_codex_linux_sandbox

Source: `codex-rs/linux-sandbox`

Expected plan hash: `6610974b1f6990e6251417c840da407af5440f244aaae6bdaca32c0ee386791e`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/linux-sandbox/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/linux-sandbox/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/linux-sandbox/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/linux-sandbox/build.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/bazel_bwrap.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/bundled_bwrap.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/bwrap.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/exec_util.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/landlock.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/launcher.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/linux_run_main.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/linux_run_main_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/linux-sandbox/src/main.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/src/proxy_routing.rs` | forager | USE | rust source - forager target |
| `codex-rs/linux-sandbox/tests/all.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/linux-sandbox/tests/suite/landlock.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/linux-sandbox/tests/suite/managed_proxy.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/linux-sandbox/tests/suite/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
