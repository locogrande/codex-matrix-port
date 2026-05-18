# Reuse Map - as_codex_shell_escalation

Source: `codex-rs/shell-escalation`

Expected plan hash: `b3530e55bfc1c9dfa358a5952b21a139d911d2d03d0a6a66a9c55c16eca043db`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/shell-escalation/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/shell-escalation/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/shell-escalation/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/shell-escalation/patches/zsh-exec-wrapper.patch` | unmapped | USE | other source - unmapped target |
| `codex-rs/shell-escalation/src/bin/main_execve_wrapper.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/escalate_client.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/escalate_protocol.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/escalate_server.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/escalation_policy.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/execve_wrapper.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/mod.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/socket.rs` | forager | USE | rust source - forager target |
| `codex-rs/shell-escalation/src/unix/stopwatch.rs` | forager | USE | rust source - forager target |
