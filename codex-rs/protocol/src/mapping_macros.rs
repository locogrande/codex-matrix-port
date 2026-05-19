//! Declarative macros for consolidating repeated `impl From<...>` mirror
//! conversion blocks between core protocol types.
//!
//! This is the `codex-protocol` counterpart of the macro in
//! `codex-app-server-protocol`. It is kept in sync intentionally so each crate
//! can use the same syntax without taking a cross-crate dependency that would
//! create a cycle (`codex-app-server-protocol` already depends on this crate).
//!
//! See `codex_app_server_protocol::mapping_macros` for usage examples.

/// Generate `impl From<$src> for $dst` where the destination is a struct and
/// each listed field is either copied verbatim from `value.<field>` (bare
/// ident) or piped through `.into()` when tagged `field: into`.
#[macro_export]
macro_rules! mirror_from {
    ($src:ty => $dst:ty { $($field:ident $(: $tag:ident)?),+ $(,)? }) => {
        impl ::core::convert::From<$src> for $dst {
            fn from(value: $src) -> Self {
                Self {
                    $( $field: $crate::__mirror_val!(value.$field $(, $tag)?) ),+
                }
            }
        }
    };
}

#[macro_export]
#[doc(hidden)]
macro_rules! __mirror_val {
    ($expr:expr) => { $expr };
    ($expr:expr, into) => { ($expr).into() };
}
