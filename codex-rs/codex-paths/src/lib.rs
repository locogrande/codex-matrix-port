//! Shared path literals used throughout the codex workspace.
//!
//! These constants exist to deduplicate the string literals that describe
//! codex's on-disk layout (config file, home dir, auth file, sessions,
//! memories, plugin manifests, etc.). Crates should depend on
//! `codex-paths` and use the named constants rather than re-spelling the
//! literal string at every call site.

/// Codex top-level configuration file name (`config.toml`).
pub const CONFIG_TOML: &str = "config.toml";

/// Codex user home directory name (`.codex`).
pub const CODEX_HOME_DIR: &str = ".codex";

/// On-disk credentials filename (`auth.json`).
pub const AUTH_JSON: &str = "auth.json";

/// Sessions directory name under the codex home (`sessions`).
pub const SESSIONS_DIR: &str = "sessions";

/// Memories directory name under the codex home (`memories`).
pub const MEMORIES_DIR: &str = "memories";

/// Per-repo plugin manifest path (`.codex-plugin/plugin.json`).
pub const PLUGIN_JSON: &str = ".codex-plugin/plugin.json";

/// Per-repo marketplace manifest path (`.agents/plugins/marketplace.json`).
pub const MARKETPLACE_JSON: &str = ".agents/plugins/marketplace.json";

/// Git metadata directory name (`.git`).
pub const GIT_DIR: &str = ".git";
