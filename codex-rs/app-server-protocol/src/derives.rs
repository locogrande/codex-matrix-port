//! Common derive aliases for protocol DTOs.
//!
//! Rust does not allow aliasing the right-hand side of `#[derive(...)]`, but a
//! large number of files in this crate import the same four traits before each
//! derive block:
//!
//! ```ignore
//! use schemars::JsonSchema;
//! use serde::Deserialize;
//! use serde::Serialize;
//! use ts_rs::TS;
//! ```
//!
//! Bringing this module into scope with `use crate::derives::*;` replaces those
//! four `use` lines with one, while leaving the actual `#[derive(...)]` lines
//! untouched (and therefore still readable by anyone scanning for which traits
//! a given type implements).
//!
//! Note: This module re-exports rather than introduces aliases. Macro lookup at
//! derive-resolution time picks up the re-exported names exactly as if they
//! had been imported directly.

pub use schemars::JsonSchema;
pub use serde::Deserialize;
pub use serde::Serialize;
pub use ts_rs::TS;
