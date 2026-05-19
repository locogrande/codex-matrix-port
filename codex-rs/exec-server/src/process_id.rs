// Canonical `ProcessId` lives in `codex-common-types`. The bespoke
// definition that used to live here (impl Deref/Borrow/AsRef + a handful
// of `From` impls + custom `new`/`as_str`/`into_inner` helpers) was
// folded into the shared `string_id!` macro so every transparent String
// ID gets the same surface area.
pub use codex_common_types::ProcessId;
