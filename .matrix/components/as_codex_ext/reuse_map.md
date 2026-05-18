# Reuse Map - as_codex_ext

Source: `codex-rs/ext`

Expected plan hash: `a5678f3919bb1ed6b337e7c82c7f998b75a05f578baa1f7aaa8094a9a1eaddcf`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/ext/extension-api/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/ext/extension-api/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/ext/extension-api/examples/enabled_extensions.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/examples/enabled_extensions/shared_state_extension.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/notes.md` | docs | USE | documentation |
| `codex-rs/ext/extension-api/src/capabilities/agent.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/capabilities/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/contributors.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/contributors/prompt.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/contributors/thread_lifecycle.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/contributors/turn_lifecycle.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/registry.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/extension-api/src/state.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/guardian/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/ext/guardian/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/ext/guardian/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/ext/memories/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/ext/memories/src/backend.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/extension.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/local.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/local/list.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/local/path.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/local/read.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/local/search.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/schema.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/ext/memories/src/tools/list.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/tools/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/tools/read.rs` | forager | USE | rust source - forager target |
| `codex-rs/ext/memories/src/tools/search.rs` | forager | USE | rust source - forager target |
