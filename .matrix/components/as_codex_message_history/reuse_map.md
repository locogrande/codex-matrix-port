# Reuse Map - as_codex_message_history

Source: `codex-rs/message-history`

Expected plan hash: `6b07d8f7b9dc810f0393bcd277b342ec4d3981263645ecc9fab86a0bf667b2c8`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/message-history/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/message-history/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/message-history/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/message-history/src/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
