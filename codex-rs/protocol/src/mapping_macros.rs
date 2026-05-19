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
    ($src:ty => $dst:ty { $($spec:tt)+ }) => {
        impl ::core::convert::From<$src> for $dst {
            fn from(value: $src) -> Self {
                Self {
                    $crate::__mirror_from_fields!(value, $($spec)+)
                }
            }
        }
    };
}

/// Internal helper: expands the field list of `mirror_from!`. Arms with
/// `: into` are listed first so the matcher picks the more specific form.
#[macro_export]
#[doc(hidden)]
macro_rules! __mirror_from_fields {
    ($value:ident, $field:ident : into, $($rest:tt)+) => {
        $field: $value.$field.into(),
        $crate::__mirror_from_fields!($value, $($rest)+)
    };
    ($value:ident, $field:ident : into $(,)?) => {
        $field: $value.$field.into()
    };
    ($value:ident, $field:ident, $($rest:tt)+) => {
        $field: $value.$field,
        $crate::__mirror_from_fields!($value, $($rest)+)
    };
    ($value:ident, $field:ident $(,)?) => {
        $field: $value.$field
    };
}
