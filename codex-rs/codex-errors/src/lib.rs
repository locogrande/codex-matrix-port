//! Shared error helpers for the codex workspace.
//!
//! Tiny declarative macros that emit the `impl From<...>` shapes recurring
//! across 40+ error enums in the workspace, plus a `String`-newtype shape
//! several crates re-implemented by hand.

/// Implement `From<std::io::Error>` for an error enum with an `Io(...)` variant.
#[macro_export]
macro_rules! impl_io_from {
    ($error:ty) => {
        impl ::core::convert::From<::std::io::Error> for $error {
            fn from(e: ::std::io::Error) -> Self { <$error>::Io(e) }
        }
    };
}

/// Implement `From<serde_json::Error>` for an error enum with a `Json(...)` variant.
#[macro_export]
macro_rules! impl_json_from {
    ($error:ty) => {
        impl ::core::convert::From<::serde_json::Error> for $error {
            fn from(e: ::serde_json::Error) -> Self { <$error>::Json(e) }
        }
    };
}

/// Both `From<std::io::Error>` and `From<serde_json::Error>` — the most repeated combination.
#[macro_export]
macro_rules! impl_io_json_from {
    ($error:ty) => {
        $crate::impl_io_from!($error);
        $crate::impl_json_from!($error);
    };
}

/// Single-variant `Display`/`Error`/`From<String>`/`From<&str>` newtype.
/// Replaces hand-rolled `pub enum FooError { Invalid(String) }` shapes.
#[macro_export]
macro_rules! string_error_enum {
    ($vis:vis $name:ident) => {
        #[derive(Debug, Clone, PartialEq, Eq)]
        $vis struct $name(pub ::std::string::String);
        impl ::core::fmt::Display for $name {
            fn fmt(&self, f: &mut ::core::fmt::Formatter<'_>) -> ::core::fmt::Result {
                f.write_str(&self.0)
            }
        }
        impl ::std::error::Error for $name {}
        impl ::core::convert::From<::std::string::String> for $name {
            fn from(s: ::std::string::String) -> Self { Self(s) }
        }
        impl<'a> ::core::convert::From<&'a str> for $name {
            fn from(s: &'a str) -> Self { Self(s.to_string()) }
        }
    };
}

/// Common accessor for error types that carry a single human-readable message.
pub trait StringError: std::error::Error {
    fn as_message(&self) -> Option<&str> { None }
}

#[cfg(test)]
mod tests {
    use thiserror::Error;
    #[derive(Debug, Error)]
    enum DemoError {
        #[error(transparent)] Io(std::io::Error),
        #[error(transparent)] Json(serde_json::Error),
    }
    impl_io_json_from!(DemoError);

    #[test]
    fn io_routes() {
        let err: DemoError = std::io::Error::other("boom").into();
        assert!(matches!(err, DemoError::Io(_)));
    }
    #[test]
    fn json_routes() {
        let parse_err: serde_json::Error = serde_json::from_str::<serde_json::Value>("x").unwrap_err();
        let err: DemoError = parse_err.into();
        assert!(matches!(err, DemoError::Json(_)));
    }

    string_error_enum!(pub TestStrErr);
    #[test]
    fn string_enum_works() {
        let a: TestStrErr = "boom".into();
        let b: TestStrErr = "boom".to_string().into();
        assert_eq!(a, b);
        assert_eq!(a.to_string(), "boom");
    }
}
