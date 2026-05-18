# Reuse Map - as_codex_hooks

Source: `codex-rs/hooks`

Expected plan hash: `496fefbb089fba41026a6a94ab3b55c26c7ce17a1be0fefaf1fa4b07f1efcdba`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/hooks/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/hooks/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/hooks/schema/generated/permission-request.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/permission-request.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/post-compact.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/post-compact.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/post-tool-use.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/post-tool-use.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/pre-compact.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/pre-compact.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/pre-tool-use.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/pre-tool-use.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/session-start.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/session-start.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/stop.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/stop.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/user-prompt-submit.command.input.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/schema/generated/user-prompt-submit.command.output.schema.json` | unmapped | USE | json source - unmapped target |
| `codex-rs/hooks/src/bin/write_hooks_schema_fixtures.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/config_rules.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/declarations.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/engine/command_runner.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/engine/discovery.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/engine/dispatcher.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/engine/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/engine/mod_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/hooks/src/engine/output_parser.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/engine/schema_loader.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/common.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/compact.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/permission_request.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/post_tool_use.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/pre_tool_use.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/session_start.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/stop.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/events/user_prompt_submit.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/legacy_notify.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/output_spill.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/output_spill_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/hooks/src/registry.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/schema.rs` | forager | USE | rust source - forager target |
| `codex-rs/hooks/src/types.rs` | forager | USE | rust source - forager target |
