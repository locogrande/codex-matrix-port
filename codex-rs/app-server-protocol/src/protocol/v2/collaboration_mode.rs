use crate::derives::*;
use crate::mirror_from;
use codex_protocol::config_types::CollaborationModeMask as CoreCollaborationModeMask;
use codex_protocol::config_types::ModeKind;
use codex_protocol::openai_models::ReasoningEffort;

/// EXPERIMENTAL - list collaboration mode presets.
#[derive(Serialize, Deserialize, Debug, Clone, PartialEq, Default, JsonSchema, TS)]
#[serde(rename_all = "camelCase")]
#[ts(export_to = "v2/")]
pub struct CollaborationModeListParams {}

/// EXPERIMENTAL - collaboration mode preset metadata for clients.
#[derive(Serialize, Deserialize, Debug, Clone, PartialEq, JsonSchema, TS)]
#[serde(rename_all = "camelCase")]
#[ts(export_to = "v2/")]
pub struct CollaborationModeMask {
    pub name: String,
    pub mode: Option<ModeKind>,
    pub model: Option<String>,
    #[serde(rename = "reasoning_effort")]
    #[ts(rename = "reasoning_effort")]
    pub reasoning_effort: Option<Option<ReasoningEffort>>,
}

mirror_from!(CoreCollaborationModeMask => CollaborationModeMask {
    name, mode, model, reasoning_effort,
});

/// EXPERIMENTAL - collaboration mode presets response.
#[derive(Serialize, Deserialize, Debug, Clone, PartialEq, JsonSchema, TS)]
#[serde(rename_all = "camelCase")]
#[ts(export_to = "v2/")]
pub struct CollaborationModeListResponse {
    pub data: Vec<CollaborationModeMask>,
}
