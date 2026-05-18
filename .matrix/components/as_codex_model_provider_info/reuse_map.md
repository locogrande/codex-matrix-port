# Reuse Map - as_codex_model_provider_info

Source: `codex-rs/model-provider-info`

Expected plan hash: `7e8534817ff82bb0b2a87881f918102dde0f584ed3e75234e34c4930d10f8b25`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/model-provider-info/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/model-provider-info/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/model-provider-info/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/model-provider-info/src/model_provider_info_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
