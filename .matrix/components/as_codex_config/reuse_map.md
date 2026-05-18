# Reuse Map - as_codex_config

Source: `codex-rs/config`

Expected plan hash: `74305282525989fd0c4c0b7fc7de5c09a36b4e17d07e66b6b7b22bcc46e7570b`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/config/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/config/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/config/examples/generate-proto.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/scripts/generate-proto.sh` | automation_tools | USE | shell source - automation_tools target |
| `codex-rs/config/src/cloud_requirements.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/config_requirements.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/config_toml.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/constraint.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/diagnostics.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/fingerprint.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/hook_config.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/hooks_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/host_name.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/key_aliases.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/loader/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/config/src/loader/layer_io.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/loader/macos.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/loader/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/loader/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/marketplace_edit.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/mcp_edit.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/mcp_edit_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/mcp_types.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/mcp_types_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/merge.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/merge_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/overrides.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/permissions_toml.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/plugin_edit.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/profile_toml.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/project_root_markers.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/requirements_exec_policy.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/schema.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/skills_config.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/state.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/state_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/strict_config.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/strict_config_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/config/src/thread_config.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/thread_config/proto/codex.thread_config.v1.proto` | unmapped | USE | protobuf source - unmapped target |
| `codex-rs/config/src/thread_config/proto/codex.thread_config.v1.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/thread_config/remote.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/tui_keymap.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/types.rs` | forager | USE | rust source - forager target |
| `codex-rs/config/src/types_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
