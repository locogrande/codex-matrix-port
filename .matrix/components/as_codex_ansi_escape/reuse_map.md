# as_codex_ansi_escape reuse map

- task_id: `WO_2026-05-18_codex-port_as_codex_ansi_escape_copy_register_gate`
- source: `codex-rs/ansi-escape`
- expected_plan_hash: `6bf83eb80c7807b756b299d9afb546c76acc19279bd390ae01a4f2973b072ff5`

| path | language | framework | verdict | reason |
|---|---|---|---|---|
| `codex-rs/ansi-escape/BUILD.bazel` | bazel | build_config | REFACTOR | preserve build config for Matrix import metadata |
| `codex-rs/ansi-escape/Cargo.toml` | cargo_manifest | build_config | REFACTOR | preserve crate manifest for Matrix import metadata |
| `codex-rs/ansi-escape/README.md` | readme | readme | USE | preserve docs asset |
| `codex-rs/ansi-escape/src/lib.rs` | rust | youmove | USE | preserve Rust source mapped to youmove/tui rendering domain |
