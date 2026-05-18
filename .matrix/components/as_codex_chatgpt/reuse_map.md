# Reuse Map - as_codex_chatgpt

Source: `codex-rs/chatgpt`

Expected plan hash: `fd64d535850f29b5c45fddf6ca2dc1bc55b40410e05f56c5cc8458f4f4484ad7`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/chatgpt/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/chatgpt/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/chatgpt/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/chatgpt/src/apply_command.rs` | forager | USE | rust source - forager target |
| `codex-rs/chatgpt/src/chatgpt_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/chatgpt/src/connectors.rs` | forager | USE | rust source - forager target |
| `codex-rs/chatgpt/src/get_task.rs` | forager | USE | rust source - forager target |
| `codex-rs/chatgpt/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/chatgpt/src/workspace_settings.rs` | forager | USE | rust source - forager target |
| `codex-rs/chatgpt/src/workspace_settings_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/chatgpt/tests/all.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/chatgpt/tests/suite/apply_command_e2e.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/chatgpt/tests/suite/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/chatgpt/tests/task_turn_fixture.json` | tester | USE | test file - preserve for Tester framework integration |
