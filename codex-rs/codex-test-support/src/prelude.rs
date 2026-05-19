//! Glob-importable re-exports of the most repeated test-time imports.
//!
//! Each entry below corresponds to a `use ...;` line that appears in
//! 30+ codex-rs test files (per the folder-5 duplicate-import scan).
//! Domain-specific types (codex_protocol::*, mock_model_server::*, ...)
//! are deliberately NOT re-exported — those stay in the individual test
//! files where they make their meaning clear.

// pretty_assertions::{assert_eq, assert_ne} are deliberately NOT re-exported:
// a glob import that includes them is ambiguous with std's prelude assert_eq /
// assert_ne. Test files that want pretty output must `use pretty_assertions::*;`
// directly (named imports shadow std prelude; glob does not).

// std::path
pub use std::path::Path;
pub use std::path::PathBuf;

// std::sync
pub use std::sync::Arc;

// std::collections
pub use std::collections::HashMap;

// std::time
pub use std::time::Duration;

// anyhow — every test file that uses Result/Context pulls these in.
pub use anyhow::Context;
pub use anyhow::Result;
pub use anyhow::anyhow;
pub use anyhow::bail;

// tempfile — temp dirs/files are universal in tests.
pub use tempfile::NamedTempFile;
pub use tempfile::TempDir;
pub use tempfile::tempdir;
