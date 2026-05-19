//! Declarative macros for consolidating repeated `impl From<Core...>` / mirror
//! conversion blocks between protocol DTOs and their core counterparts.
//!
//! Pattern observed: many protocol DTOs are 1:1 mirrors of a core struct and
//! the only thing the hand-written `impl From` does is copy each field
//! verbatim, sometimes with a `.into()` to bridge a nested core/protocol pair.
//! These macros let us collapse those blocks to a single line.
//!
//! # Examples
//! ```ignore
//! // Pure copy: every field of the destination is `value.field`.
//! mirror_from!(CoreCreditsSnapshot => CreditsSnapshot { has_credits, unlimited, balance });
//!
//! // Mixed: bare ident = pure copy, `field: into` = `value.field.into()`.
//! mirror_from!(CoreHookOutputEntry => HookOutputEntry { kind: into, text });
//! ```

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

/// Internal helper: expands the field list of `mirror_from!`. Each comma-
/// separated entry is either `field` (pure) or `field: into` (call `.into()`).
/// Arms with the `: into` tag are listed before bare-ident arms so the macro
/// matcher picks the more specific form first.
#[macro_export]
#[doc(hidden)]
macro_rules! __mirror_from_fields {
    // `field: into`, more to follow.
    ($value:ident, $field:ident : into, $($rest:tt)+) => {
        $field: $value.$field.into(),
        $crate::__mirror_from_fields!($value, $($rest)+)
    };
    // Trailing `field: into` (with optional trailing comma).
    ($value:ident, $field:ident : into $(,)?) => {
        $field: $value.$field.into()
    };
    // Pure field, more to follow.
    ($value:ident, $field:ident, $($rest:tt)+) => {
        $field: $value.$field,
        $crate::__mirror_from_fields!($value, $($rest)+)
    };
    // Trailing pure field (with optional trailing comma).
    ($value:ident, $field:ident $(,)?) => {
        $field: $value.$field
    };
}
