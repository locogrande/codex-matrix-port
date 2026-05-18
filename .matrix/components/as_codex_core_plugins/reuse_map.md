# Reuse Map - as_codex_core_plugins

Source: `codex-rs/core-plugins`

Expected plan hash: `5e5163ba0b7d04c271e143a442ddabda2b4e3644b4a0e5036a1ee7074d4755ac`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/core-plugins/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/core-plugins/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/core-plugins/src/installed_marketplaces.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/lib.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/loader.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/loader_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/manager.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/manager_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/manifest.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_add.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_add/install.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_add/metadata.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_add/source.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_remove.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/marketplace_upgrade.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_upgrade/activation.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/marketplace_upgrade/git.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote/remote_installed_plugin_sync.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote/share.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote/share/checkout.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote/share/local_paths.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote/share/tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/remote_bundle.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/remote_legacy.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/startup_remote_sync.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/startup_remote_sync_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/startup_sync.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/startup_sync_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/store.rs` | forager | USE | rust source - forager target |
| `codex-rs/core-plugins/src/store_tests.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/test_support.rs` | forager | USE | test file - preserve for Tester framework integration |
| `codex-rs/core-plugins/src/toggles.rs` | forager | USE | rust source - forager target |
