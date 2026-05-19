//! Shared test-time prelude for codex-rs integration tests.
//!
//! Test files across the workspace repeat the same handful of `use`
//! statements (Path/PathBuf, Arc, HashMap, Duration, anyhow::*,
//! pretty_assertions::assert_eq, tempfile::*, ...). Importing
//! [`prelude`] with a glob collapses those lines to one per file.
//!
//! Usage in a test file:
//!
//! ```ignore
//! use codex_test_support::prelude::*;
//! ```
//!
//! The prelude is intentionally conservative: only types/macros that are
//! universally applicable in test bodies and unlikely to collide with
//! domain-specific imports.

pub mod prelude;
