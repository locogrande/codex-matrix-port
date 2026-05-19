# matrix-test-macro

`#[matrix::test]` — proc-macro replacement for `#[tokio::test]` that owns the
per-test scaffolding (tempdir, tracer span, Voltmeter probe) so call sites do
not have to repeat 5–15 boilerplate lines.

Introduced in **Layer-6 refactor pass F (May 2026)**. The folder-5 duplicate-
attribute scan counted 2,401 `#[tokio::test]` + 1,774 `#[test]` hits across
`codex-rs`. Converting 30% of them collapses an estimated 800–2,400 LOC; the
goal of this crate is to give that conversion a single attribute point that
later passes can extend without re-touching the call sites.

## Status

* Pass F (this pass): macro exists, behaves as a transparent passthrough,
  adopted in a small beachhead (`async-utils`, `aws-auth`, `agent-graph-store`).
* Pass G+ (planned): tracer-span / voltmeter-probe / auto-tempdir flag support,
  followed by batched conversion of remaining call sites.

## Usage

Add as a dev-dependency:

```toml
[dev-dependencies]
matrix-test-macro = { workspace = true }
```

Alias the crate to `matrix` inside the test module so the attribute reads as
`#[matrix::test]` instead of the longer `#[matrix_test_macro::test]`:

```rust
#[cfg(test)]
mod tests {
    use matrix_test_macro as matrix;

    #[matrix::test]
    async fn it_works() {
        // body
    }
}
```

The expansion is currently equivalent to:

```rust
#[tokio::test]
async fn it_works() {
    let _matrix_test_name: &'static str = "it_works";
    // body
}
```

## Upgrade path for follow-up passes

1. **Batch-convert mechanical sites** — files where every `#[tokio::test]` can
   be replaced with `#[matrix::test]` without changing the body. Add
   `matrix-test-macro = { workspace = true }` to the crate's `dev-dependencies`
   and `use matrix_test_macro as matrix;` once per test module. Target ~50
   files per PR.
2. **Add flag support to the macro** — extend `pub fn test` to parse an
   attribute argument list (`tempdir`, `tracer = "..."`, `probe`). Each flag
   injects its block prologue/epilogue into the expansion. Call sites stay
   stable; the additions are opt-in per test.
3. **Generalize beyond tokio** — when a sufficient mass of sync `#[test]` sites
   share boilerplate, add a second proc-macro entrypoint (or detect `async fn`
   vs `fn` inside the existing one) that wraps `#[test]` instead of
   `#[tokio::test]`.

## Why a proc-macro and not a declarative one?

Declarative `macro_rules!` cannot emit `#[tokio::test]` on a function the
caller wrote without restructuring the call site (`tokio_test! { async fn ... }`).
A proc-macro attribute keeps the call site idiomatic — `#[matrix::test]
async fn it_works()` — and gives us the future flexibility to inspect the
function body for setup hooks.
