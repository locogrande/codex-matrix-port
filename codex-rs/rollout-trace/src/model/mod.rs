//! Reduced rollout trace model.
//!
//! These types describe the deterministic replay output. They intentionally
//! separate model-visible conversation from runtime/debug objects.

use std::collections::BTreeMap;

use serde::Deserialize;
use serde::Serialize;

use crate::payload::RawPayloadId;
use crate::payload::RawPayloadRef;
mod conversation;
mod runtime;
mod session;

pub use conversation::*;
pub use runtime::*;
pub use session::*;

// Canonical trace-id aliases live in `codex_common_types::trace_ids`.
// Re-exported here so downstream consumers can keep saying e.g.
// `rollout_trace::model::AgentThreadId`.
pub use codex_common_types::trace_ids::AgentPath;
pub use codex_common_types::trace_ids::AgentThreadId;
pub use codex_common_types::trace_ids::CodeCellId;
pub use codex_common_types::trace_ids::CodeModeRuntimeToolId;
pub use codex_common_types::trace_ids::CodexTurnId;
pub use codex_common_types::trace_ids::CompactionId;
pub use codex_common_types::trace_ids::CompactionRequestId;
pub use codex_common_types::trace_ids::ConversationItemId;
pub use codex_common_types::trace_ids::CorrelationId;
pub use codex_common_types::trace_ids::EdgeId;
pub use codex_common_types::trace_ids::InferenceCallId;
pub use codex_common_types::trace_ids::McpCallId;
pub use codex_common_types::trace_ids::ModelVisibleCallId;
pub use codex_common_types::trace_ids::TerminalId;
pub use codex_common_types::trace_ids::TerminalOperationId;
pub use codex_common_types::trace_ids::ToolCallId;

/// Canonical reduced graph for one Codex rollout.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct RolloutTrace {
    pub schema_version: u32,
    /// Unique identity for this trace capture.
    ///
    /// `rollout_id` names the Codex rollout/session being observed. `trace_id`
    /// names the diagnostic artifact produced for that rollout, which keeps
    /// storage/replay identity separate from the product-level session identity.
    pub trace_id: String,
    /// CLI-visible rollout/run identity. Higher-level experiment/sample IDs wrap this object.
    pub rollout_id: String,
    pub started_at_unix_ms: i64,
    /// Wall-clock timestamp for terminal rollout status. `None` means running or partial trace.
    pub ended_at_unix_ms: Option<i64>,
    pub status: RolloutStatus,
    pub root_thread_id: AgentThreadId,
    pub threads: BTreeMap<AgentThreadId, AgentThread>,
    pub codex_turns: BTreeMap<CodexTurnId, CodexTurn>,
    pub conversation_items: BTreeMap<ConversationItemId, ConversationItem>,
    pub inference_calls: BTreeMap<InferenceCallId, InferenceCall>,
    /// Model-authored `exec` JavaScript cells keyed by reducer-owned cell ID.
    pub code_cells: BTreeMap<CodeCellId, CodeCell>,
    pub tool_calls: BTreeMap<ToolCallId, ToolCall>,
    /// Terminal runtime sessions keyed by process/session ID returned by the runtime.
    pub terminal_sessions: BTreeMap<TerminalId, TerminalSession>,
    /// Commands/writes/polls against terminals keyed by reducer-owned operation ID.
    pub terminal_operations: BTreeMap<TerminalOperationId, TerminalOperation>,
    /// Installed compaction checkpoints keyed by checkpoint ID.
    pub compactions: BTreeMap<CompactionId, Compaction>,
    /// Upstream remote compaction calls keyed by local request ID.
    pub compaction_requests: BTreeMap<CompactionRequestId, CompactionRequest>,
    /// Information-flow edges between threads, cells, tools, and runtime resources.
    pub interaction_edges: BTreeMap<EdgeId, InteractionEdge>,
    /// Raw JSON payloads keyed by raw-payload ID. Most point at files outside this object.
    pub raw_payloads: BTreeMap<RawPayloadId, RawPayloadRef>,
}

impl RolloutTrace {
    /// Builds an empty reduced trace that a reducer can populate.
    pub(crate) fn new(
        schema_version: u32,
        trace_id: String,
        rollout_id: String,
        root_thread_id: AgentThreadId,
        started_at_unix_ms: i64,
    ) -> Self {
        Self {
            schema_version,
            trace_id,
            rollout_id,
            started_at_unix_ms,
            ended_at_unix_ms: None,
            status: RolloutStatus::Running,
            root_thread_id,
            threads: BTreeMap::new(),
            codex_turns: BTreeMap::new(),
            conversation_items: BTreeMap::new(),
            inference_calls: BTreeMap::new(),
            code_cells: BTreeMap::new(),
            tool_calls: BTreeMap::new(),
            terminal_sessions: BTreeMap::new(),
            terminal_operations: BTreeMap::new(),
            compactions: BTreeMap::new(),
            compaction_requests: BTreeMap::new(),
            interaction_edges: BTreeMap::new(),
            raw_payloads: BTreeMap::new(),
        }
    }
}
