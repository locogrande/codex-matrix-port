# Reuse Map - as_codex_aws_auth

Source: `codex-rs/aws-auth`

Expected plan hash: `5ebd8533f2735482acc09fc855fc48d04c4d9c89d97c570ace8424c60aa1e26e`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/aws-auth/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/aws-auth/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/aws-auth/src/config.rs` | forager | USE | rust source - forager target |
| `codex-rs/aws-auth/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/aws-auth/src/signing.rs` | forager | USE | rust source - forager target |
