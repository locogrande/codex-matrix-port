# Reuse Map - as_codex_sandboxing

Source: `codex-rs/sandboxing`

Expected plan hash: `efc3576d1d9c7030a6a73a958560ac01166e19e47c2974569f10c337d1745aa3`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/sandboxing/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/sandboxing/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/sandboxing/src/bwrap.rs` | forager | USE | rust source - forager target |
| `codex-rs/sandboxing/src/bwrap_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/sandboxing/src/landlock.rs` | forager | USE | rust source - forager target |
| `codex-rs/sandboxing/src/landlock_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/sandboxing/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/sandboxing/src/manager.rs` | forager | USE | rust source - forager target |
| `codex-rs/sandboxing/src/manager_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/sandboxing/src/policy_transforms.rs` | forager | USE | rust source - forager target |
| `codex-rs/sandboxing/src/policy_transforms_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/sandboxing/src/restricted_read_only_platform_defaults.sbpl` | unmapped | USE | other source - unmapped target |
| `codex-rs/sandboxing/src/seatbelt.rs` | forager | USE | rust source - forager target |
| `codex-rs/sandboxing/src/seatbelt_base_policy.sbpl` | unmapped | USE | other source - unmapped target |
| `codex-rs/sandboxing/src/seatbelt_network_policy.sbpl` | unmapped | USE | other source - unmapped target |
| `codex-rs/sandboxing/src/seatbelt_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
