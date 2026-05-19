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
