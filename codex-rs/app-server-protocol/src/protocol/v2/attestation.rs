use crate::derives::*;

#[derive(Serialize, Deserialize, Debug, Clone, PartialEq, JsonSchema, TS, Default)]
#[serde(rename_all = "camelCase")]
#[ts(export_to = "v2/")]
pub struct AttestationGenerateParams {}

#[derive(Serialize, Deserialize, Debug, Clone, PartialEq, JsonSchema, TS)]
#[serde(rename_all = "camelCase")]
#[ts(export_to = "v2/")]
pub struct AttestationGenerateResponse {
    /// Opaque client attestation token.
    pub token: String,
}
