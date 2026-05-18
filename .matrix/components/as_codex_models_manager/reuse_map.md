# Reuse Map - as_codex_models_manager

Source: `codex-rs/models-manager`

Expected plan hash: `9128b3eb740a3abc4b4f0b0a9794d8d7779269bfeea0adc1dcd6e3e9625e426e`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/models-manager/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/models-manager/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/models-manager/models.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/models-manager/prompt.md` | docs | USE | documentation |
| `codex-rs/models-manager/src/cache.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/collaboration_mode_presets.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/collaboration_mode_presets_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/models-manager/src/config.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/manager.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/manager_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/models-manager/src/model_info.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/model_info_overrides_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/models-manager/src/model_info_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/models-manager/src/model_presets.rs` | forager | USE | rust source - forager target |
| `codex-rs/models-manager/src/test_support.rs` | forager | USE | test file - preserve for Tester framework integration |
