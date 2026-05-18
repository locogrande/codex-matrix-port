# Reuse Map - as_codex_execpolicy_legacy

Source: `codex-rs/execpolicy-legacy`

Expected plan hash: `5765848edd1c733748cbf585d1dbb85e39302dd12bbcc9d10cf8b463457b6c61`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/execpolicy-legacy/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/execpolicy-legacy/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/execpolicy-legacy/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-rs/execpolicy-legacy/build.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/arg_matcher.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/arg_resolver.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/arg_type.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/default.policy` | unmapped | USE | other source - unmapped target |
| `codex-rs/execpolicy-legacy/src/error.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/exec_call.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/execv_checker.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/main.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/opt.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/policy.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/policy_parser.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/program.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/sed_command.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/src/valid_exec.rs` | forager | USE | rust source - forager target |
| `codex-rs/execpolicy-legacy/tests/all.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/bad.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/cp.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/good.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/head.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/literal.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/ls.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/mod.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/parse_sed_command.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/pwd.rs` | tester | USE | test file - preserve for Tester framework integration |
| `codex-rs/execpolicy-legacy/tests/suite/sed.rs` | tester | USE | test file - preserve for Tester framework integration |
