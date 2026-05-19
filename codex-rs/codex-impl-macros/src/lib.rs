//! Declarative macros for common boilerplate impl blocks across the
//! codex-rs workspace.
//!
//! These macros collapse the most-repeated trait-impl shapes
//! (`Display`, `FromStr`, empty `std::error::Error`) into single-line
//! invocations. They are intentionally narrow: each macro encodes one
//! exact pattern that already appears verbatim multiple times in the
//! workspace. Use the long-form `impl` block whenever the body needs
//! to deviate from the captured shape.

/// Implements `std::fmt::Display` by writing a single expression
/// computed from `self`. The expression must implement `Display`.
///
/// # Examples
///
/// ```ignore
/// pub struct ConnectionId(pub u64);
/// codex_impl_macros::impl_display_via!(ConnectionId, |s| s.0);
///
/// pub struct Wrapper { inner: String }
/// codex_impl_macros::impl_display_via!(Wrapper, |s| &s.inner);
/// ```
#[macro_export]
macro_rules! impl_display_via {
    ($type:ty, |$s:ident| $expr:expr) => {
        impl ::std::fmt::Display for $type {
            fn fmt(
                &self,
                f: &mut ::std::fmt::Formatter<'_>,
            ) -> ::std::fmt::Result {
                let $s = self;
                ::std::write!(f, "{}", $expr)
            }
        }
    };
}

/// Implements `std::str::FromStr` whose error type is `Infallible` and
/// whose body is the supplied expression. The expression receives the
/// raw `&str` bound to the identifier from the closure-like header.
///
/// # Examples
///
/// ```ignore
/// pub struct Tag(String);
/// codex_impl_macros::impl_from_str_infallible!(Tag, |s| Tag(s.to_string()));
/// ```
#[macro_export]
macro_rules! impl_from_str_infallible {
    ($type:ty, |$s:ident| $expr:expr) => {
        impl ::std::str::FromStr for $type {
            type Err = ::std::convert::Infallible;

            fn from_str(
                s: &str,
            ) -> ::std::result::Result<Self, Self::Err> {
                let $s = s;
                ::std::result::Result::Ok($expr)
            }
        }
    };
}

/// Implements `std::str::FromStr` by delegating to
/// `serde_json::from_str`. The error type is `serde_json::Error`.
///
/// # Examples
///
/// ```ignore
/// #[derive(serde::Deserialize)]
/// pub struct Policy { ... }
/// codex_impl_macros::impl_from_str_via_serde_json!(Policy);
/// ```
#[macro_export]
macro_rules! impl_from_str_via_serde_json {
    ($type:ty) => {
        impl ::std::str::FromStr for $type {
            type Err = ::serde_json::Error;

            fn from_str(
                s: &str,
            ) -> ::std::result::Result<Self, Self::Err> {
                ::serde_json::from_str(s)
            }
        }
    };
}

/// Generates the empty `impl std::error::Error for $type {}` block.
/// Useful when `$type` already has a `Display` and `Debug` impl and
/// just needs to wear the `Error` marker trait.
#[macro_export]
macro_rules! impl_std_error {
    ($type:ty) => {
        impl ::std::error::Error for $type {}
    };
}
