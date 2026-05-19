//! Shared ID types lifted from codex crates (layer-6 pass E).
//! Repr-compatible duplicates only; wire format preserved bit-for-bit.
//! `SessionId`/`ThreadId` stay in `codex-protocol` (Uuid-backed).

use std::borrow::Borrow;
use std::fmt;
use std::ops::Deref;

use schemars::JsonSchema;
use schemars::r#gen::SchemaGenerator;
use schemars::schema::Schema;
use serde::Deserialize;
use serde::Serialize;
use ts_rs::TS;

// ---------------------------------------------------------------------------
// RequestId
// ---------------------------------------------------------------------------
//
// JSON-RPC request identifier. Same shape was duplicated in
// `app-server-protocol/src/jsonrpc_lite.rs` and `protocol/src/mcp.rs`.
// Both wire encodings are `#[serde(untagged)]` so a String or i64 round-
// trips identically.

/// ID of a JSON-RPC request, either a string or an integer.
#[derive(
    Debug,
    Clone,
    PartialEq,
    PartialOrd,
    Ord,
    Eq,
    Hash,
    Serialize,
    Deserialize,
    JsonSchema,
    TS,
)]
#[serde(untagged)]
pub enum RequestId {
    String(String),
    #[ts(type = "number")]
    Integer(i64),
}

impl fmt::Display for RequestId {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::String(value) => f.write_str(value),
            Self::Integer(value) => write!(f, "{value}"),
        }
    }
}

// ---------------------------------------------------------------------------
// String-newtype IDs
// ---------------------------------------------------------------------------
//
// Each of the structs below is a `#[serde(transparent)]` newtype over
// `String`. Wire encoding is identical to a bare JSON string. The macro
// folds the impl boilerplate so adding a sixth/seventh ID later costs a
// single line.

macro_rules! string_id {
    ($(#[$meta:meta])* $vis:vis struct $name:ident;) => {
        $(#[$meta])*
        #[derive(Debug, Clone, PartialEq, Eq, Hash, PartialOrd, Ord, Serialize, Deserialize)]
        #[serde(transparent)]
        $vis struct $name(pub String);

        impl $name {
            pub fn new(v: impl Into<String>) -> Self { Self(v.into()) }
            pub fn as_str(&self) -> &str { &self.0 }
            pub fn into_inner(self) -> String { self.0 }
        }
        impl fmt::Display for $name {
            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result { self.0.fmt(f) }
        }
        impl Deref       for $name { type Target = str; fn deref(&self) -> &str { &self.0 } }
        impl Borrow<str> for $name { fn borrow(&self) -> &str { &self.0 } }
        impl AsRef<str>  for $name { fn as_ref(&self) -> &str { &self.0 } }
        impl From<String>  for $name { fn from(v: String)  -> Self { Self(v) } }
        impl From<&str>    for $name { fn from(v: &str)    -> Self { Self(v.to_string()) } }
        impl From<&String> for $name { fn from(v: &String) -> Self { Self(v.clone()) } }
        impl From<$name> for String  { fn from(v: $name)   -> Self { v.0 } }
        impl JsonSchema for $name {
            fn schema_name() -> String { stringify!($name).to_string() }
            fn json_schema(g: &mut SchemaGenerator) -> Schema { <String>::json_schema(g) }
        }
    };
}

// Per-crate origins (pre-unification):
//   ClientId, StreamId  → app-server-transport/src/transport/remote_control/protocol.rs
//   TaskId              → cloud-tasks-client/src/api.rs
//   ProcessId           → exec-server/src/process_id.rs   (had 8 hand-rolled trait impls)
//   AppConnectorId      → plugin/src/lib.rs                (was non-serde; macro adds it as a superset)
string_id! { pub struct ClientId; }
string_id! { pub struct StreamId; }
string_id! { pub struct TaskId; }
string_id! { pub struct ProcessId; }
string_id! { pub struct AppConnectorId; }

impl StreamId {
    /// Mint a fresh stream id backed by a UUIDv7 string (was: `app-server-transport`).
    pub fn new_random() -> Self { Self(uuid::Uuid::now_v7().to_string()) }
}

// ---------------------------------------------------------------------------
// Reduced-rollout trace ID aliases
// ---------------------------------------------------------------------------
//
// The reduced rollout-trace model in `rollout-trace/src/model/mod.rs`
// declared 16 `pub type X = String` aliases for reducer-owned identifiers.
// They moved here so any downstream replay/inspect crate can name them
// without taking a heavyweight dependency on `codex-rollout-trace`.

pub mod trace_ids {
    //! Reduced-rollout trace string-typed IDs.
    pub type AgentThreadId         = String; // conversation/session UUID
    pub type AgentPath             = String; // routing path e.g. /root/search_docs
    pub type CodexTurnId           = String; // submission/activation UUID
    pub type ConversationItemId    = String; // reducer-assigned transcript item
    pub type InferenceCallId       = String; // upstream inference request
    pub type McpCallId             = String; // concrete MCP backend request
    pub type ToolCallId            = String; // reducer-owned tool-call
    pub type ModelVisibleCallId    = String; // Responses call_id
    pub type CodeModeRuntimeToolId = String; // code-mode JS runtime call
    pub type CodeCellId            = String; // model-authored exec cell
    pub type TerminalId            = String; // terminal runtime session
    pub type TerminalOperationId   = String; // terminal cmd/write/poll
    pub type CompactionId          = String; // history checkpoint
    pub type CompactionRequestId   = String; // compaction upstream req
    pub type EdgeId                = String; // info-flow edge
    pub type CorrelationId         = String; // log correlation
    pub type RawPayloadId          = String; // raw payload bundle ref
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test] fn request_id_string()  { let _ = RequestId::String("a".into()); }
    #[test] fn request_id_integer() { let _ = RequestId::Integer(7); }
    #[test] fn task_id_round_trip() {
        let t = TaskId::new("t-42");
        assert_eq!(t.as_str(), "t-42");
    }
    #[test] fn stream_id_random()   { assert!(!StreamId::new_random().as_str().is_empty()); }
}
