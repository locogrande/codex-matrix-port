# Reuse Map - as_codex_memories

Source: `codex-rs/memories`

Expected plan hash: `99aab31bec737ca281525d94608d7e85106376b86b8eba9c8cf19bbe0e0ac86f`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/memories/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/memories/mcp/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/memories/mcp/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/memories/mcp/src/backend.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/mcp/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/mcp/src/local.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/mcp/src/local_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/mcp/src/schema.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/mcp/src/server.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/read/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/memories/read/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/memories/read/src/citations.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/read/src/citations_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/read/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/read/src/metrics.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/read/src/prompts.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/read/src/prompts_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/read/src/usage.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/read/templates/memories/read_path.md` | docs | USE | documentation |
| `codex-rs/memories/write/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/memories/write/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/memories/write/src/control.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/extensions/ad_hoc.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/extensions/ad_hoc_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/src/extensions/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/extensions/prune.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/extensions/prune_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/src/guard.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/guard_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/metrics.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/phase1.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/phase2.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/prompts.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/prompts_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/src/runtime.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/start.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/startup_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/src/storage.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/storage_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/src/workspace.rs` | forager | USE | rust source - forager target |
| `codex-rs/memories/write/src/workspace_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/memories/write/templates/extensions/ad_hoc/instructions.md` | docs | USE | documentation |
| `codex-rs/memories/write/templates/memories/consolidation.md` | docs | USE | documentation |
| `codex-rs/memories/write/templates/memories/stage_one_input.md` | docs | USE | documentation |
| `codex-rs/memories/write/templates/memories/stage_one_system.md` | docs | USE | documentation |
