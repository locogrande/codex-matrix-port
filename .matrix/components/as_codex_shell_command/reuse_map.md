# Reuse Map - as_codex_shell_command

Source: `codex-rs/shell-command`

Expected plan hash: `c64d54cbeb2f0f00c002a99b1089545d3832ab23ecc98d6aac47667276514909`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/shell-command/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/shell-command/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/shell-command/src/bash.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/command_safety/is_dangerous_command.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/command_safety/is_safe_command.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/command_safety/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/command_safety/powershell_parser.ps1` | automation_tools | USE | powershell source - automation_tools target |
| `codex-rs/shell-command/src/command_safety/powershell_parser.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/command_safety/windows_dangerous_commands.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/command_safety/windows_safe_commands.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/parse_command.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/powershell.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-command/src/shell_detect.rs` | forager | USE | rust source - forager target |
