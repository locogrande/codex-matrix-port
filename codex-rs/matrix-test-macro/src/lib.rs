//! `#[matrix::test]` proc-macro: drop-in replacement for `#[tokio::test]`
//! that owns the per-test scaffolding (tempdir, tracer span, Voltmeter
//! probe) so the call sites do not have to repeat 5-15 lines of setup.
//!
//! Layer-6 refactor pass F (May 2026). Background: a folder-5 scan
//! counted 2,401 `#[tokio::test]` + 1,774 `#[test]` hits across
//! `codex-rs`. Even capturing 30% of them collapses 800-2,400 LOC.
//!
//! This first pass is intentionally minimal: the expansion is a
//! transparent passthrough to `#[tokio::test]` plus a `_matrix_test_name`
//! binding that downstream passes will use to register tracer spans and
//! voltmeter probes without touching the call sites again.
//!
//! Future expansion points (gated by `attr` flags):
//!   * `#[matrix::test(tempdir)]` — bind `let tempdir = TempDir::new()?;`
//!     and dispose it at the end of the test scope.
//!   * `#[matrix::test(tracer = "...")]` — open a named tracer span over
//!     the whole test body and close on exit.
//!   * `#[matrix::test(probe)]` — emit a Voltmeter probe registration
//!     for the test name so dashboards see per-test telemetry.
//!
//! Usage:
//! ```ignore
//! use matrix_test_macro as matrix; // local alias gives `#[matrix::test]`
//!
//! #[matrix::test]
//! async fn it_works() {
//!     // body
//! }
//! ```

use proc_macro::TokenStream;
use quote::quote;
use syn::ItemFn;
use syn::parse_macro_input;

/// Drop-in replacement for `#[tokio::test]` that emits a stable
/// `_matrix_test_name` binding for downstream passes (tracer spans,
/// voltmeter probes, tempdir auto-cleanup).
///
/// The expansion is currently a passthrough: the only generated state is
/// the test-name binding. The call sites are stable across follow-up
/// passes that flesh out tracer/voltmeter/tempdir support.
#[proc_macro_attribute]
pub fn test(_attr: TokenStream, item: TokenStream) -> TokenStream {
    let input = parse_macro_input!(item as ItemFn);
    let attrs = &input.attrs;
    let vis = &input.vis;
    let sig = &input.sig;
    let body = &input.block;
    let name = &input.sig.ident;

    let expanded = quote! {
        #(#attrs)*
        #[::tokio::test]
        #vis #sig {
            // Stable per-test handle reserved for tracer span / voltmeter
            // probe registration in follow-up Layer-6 passes. Suppressed
            // for now to keep the passthrough call sites quiet.
            #[allow(dead_code, non_snake_case)]
            let _matrix_test_name: &'static str = stringify!(#name);
            #body
        }
    };

    TokenStream::from(expanded)
}
