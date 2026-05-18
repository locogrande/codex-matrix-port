# Deep Research Prompt V3 — Codex × Matrix: audit live funnel + refactor ceiling + open architectural questions

**Repository under study**: `locogrande/codex-matrix-port` (this repo, 110 sealed codex assets)
**Matrix platform reference**: `locogrande/matrix` (`main = 781553982f` at prompt time)

## Read this first — what changed since V2

The V2 prompt asked the research to **design** the 6 funneling axes. **All 6 are now built and dogfood-passing.** Your job is no longer design; it is **audit + sharpen**.

| Axis | Codex primitive | Matrix target | Adapter | Live? |
|---|---|---|---|---|
| A1 | `app_server_protocol` (JSON-RPC) | Circuts signals | `scripts/codex_funnel_circuts_adapter.py` | ✅ 6/6 dogfood |
| A2 | `rollout` / `rollout_trace` | Tracer records | `scripts/codex_funnel_tracer_adapter.py` | ✅ 5/5 dogfood |
| A3 | `tools` registry | Forager + Tightrope (pair) | `scripts/codex_funnel_tools_adapter.py` | ✅ 6/6 dogfood |
| A4 | `thread_store` / `message_history` | Library canon | `scripts/codex_funnel_thread_adapter.py` | ✅ 6/6 dogfood |
| A5 | `memories` / `skills` | Forager assets | `scripts/codex_funnel_memory_adapter.py` | ✅ 6/6 dogfood |
| A6 | `sandboxing` / `bwrap` / harden | Truarch verdicts | `scripts/codex_funnel_sandbox_adapter.py` | ✅ 7/7 dogfood |

A single W3C `traceparent` (`4bf92f3577b34da6a3ce929d0e0e4736`) propagates from the originating A1 envelope through all 6 axes — proving they're one substrate, not silos.

Shared scaffold lives in `scripts/codex_funnel_base.py` (197 LOC). Consolidation pass landed **−46 % net LOC** across the 6 adapters.

Netrix verb chain executed for every axis: `flowing_record_decision` → `tightrope_create_workorder` → adapter build → `tightrope_submit_work` → `library_submit_promotion` (canon entry `ce_codex_funnel_adapter_pattern_v2` covers all 6).

## Required outputs

1. **Audit table** — for each of the 6 live adapters, list:
   - Strengths (what the implementation got right)
   - Specific gaps (line-numbered if possible) where the deterministic translator over-trusts envelope shape, misses an edge case, or skips an evidence field
   - Recommended patches with file targets and minimal diff sketches
   - At least one *failure mode* the dogfood probe doesn't currently catch
2. **Cross-axis correlation audit** — single trace_id propagation works on a fixture; does it survive real codex flows? Specifically: (a) when a single conversation produces multiple turns + multiple tool calls + a sandboxed exec, does every emitted record carry the same root trace_id? (b) what happens when codex sub-spawns a child agent — does it propagate the parent's trace_id or mint a new root? Recommend the policy.
3. **Refactor-ceiling table** — codex source (`codex-rs/`, `codex-cli/`, `sdk/`, `docs/`), **actually run the techniques** (do not desk-estimate):
   - jscpd / PMD CPD / NiCad / ast-grep structural clone scan
   - cargo-machete / cargo-udeps / cargo metadata workspace audit
   - dependency-cruiser / nx / turborepo TS graph audit
   - test prelude survey (`pretty_assertions::assert_eq` 765 hits, `#[tokio::test]` 2,401, `MockServer::start` 202, tempdir 600+ per the V1 scan)
   - cross-crate ID type unification (`SessionId`, `ThreadId`, `WorkOrderId`-equivalents)
   - markdown/prose dedup (MinHash on the 433 .md files)
   Report **additive ceiling separated from the existing 2.3% syntactic ceiling** + P5 cost (dependency-hiding risk) per technique.
4. **Matrix implementation map** — for every recommended patch: target file path(s), new files to create, tests to add, gate evidence required, TNT fixtures, expected receipt fields. No prose-only recommendations.
5. **PatternCards** — reusable mechanism cards for each adopted pattern. The funnel-adapter pattern already lives in canon as `ce_codex_funnel_adapter_pattern_v2`; propose follow-on PatternCards for: trace-id propagation policy, cross-axis idempotency keys, dead-letter triage SLOs, dogfood-probe minimum-set rules.
6. **ActionRecipes** — deterministic scripts/recipes that future agents can run without LLM reasoning. Each recipe: name, input parameters, output artifact, verification gate.
7. **Inspired-code bibliography** — for every external pattern cited, give: repo URL + exact file + function + commit SHA + 1-line mechanism. Cover both 2015-2020 generation (LSP/DAP, OTel, Temporal, gRPC) and 2024-2025 generation (MCP, Letta, LangGraph, LiteLLM proxy, WASM component-model).
8. **Open questions** — only items the current evidence cannot answer. Flag each as either "needs new evidence run" or "needs principal decision".

## Evidence anchors

Every claim must cite one of these (read all before writing):

- `.matrix/pipeline_evidence/INDEX.md` — pack overview
- `.matrix/pipeline_evidence/01_collector_classification.json` — 3,953 codex files / 8 slots / 0 ORPHAN escalations
- `.matrix/pipeline_evidence/02_codex_registry_snapshot.json` — 113 rows, 110 unique asset_ids
- `.matrix/pipeline_evidence/03_codex_form_bundle.json` — P3 resolver output for `ipr_submit + tightrope + high risk`
- `.matrix/pipeline_evidence/07_caps_cutover.json` — 68 caps, 0 violations
- `.matrix/pipeline_evidence/08_codex_voltmeter_probes.json` — 12 probes, mixed pass/fail correctly
- `.matrix/pipeline_evidence/10_codex_export_dryrun_receipt.json` — 110 unique asset_ids exportable
- `.matrix/pipeline_evidence/12_replay_state.json` — original P12 replay snapshot
- `.matrix/pipeline_evidence/13_flow_health.json` — 6 metrics + threshold policy + findings
- `.matrix/pipeline_evidence/14_codex_artifact_guard.json` — post-lockfile-policy refinement
- **NEW** `.matrix/pipeline_evidence/15_codex_funnel_axes_summary.json` — all 6 axis counts + flowing decisions + tightrope workorders + library canon
- **NEW** `.matrix/pipeline_evidence/16_codex_funnel_replay_state.json` — current replay reducer output (116 events, 0 divergence)
- **NEW** `.matrix/pipeline_evidence/17_codex_funnel_projection.json` — current MATRIX_APP_STATE.codex_funnel section
- **NEW** `.matrix/pipeline_evidence/18_codex_funnel_consolidation.json` — −46 % LOC consolidation stats

## Question chain

### Q1 (now an audit, not a design)

Per axis: what would you change about the live adapter? Where are its blind spots? Note that the dogfood-probe checks are deliberate over-fits; suggest a richer probe set per axis that exercises real codex traffic shapes, not just the fixture.

### Q2 — codex source refactor ceiling (unchanged)

The combined 2.3 % syntactic ceiling (Miro+gpt scans) was a back-of-envelope estimate. **Actually run the AST + monorepo + embedding tools listed in Required Output 3.** Separate the additive ceiling from the syntactic baseline. Identify the 5 highest funnel-leverage refactors (refactors that also reduce funnel-adapter cost).

### Q3 — pre-commit policy refinement (already partially solved)

The lockfile-collision detector landed (PR #11). What other systemic guard rules are missing? Survey: gitleaks, talisman, pre-commit framework, lefthook. Propose 3-5 new BLOCK rules + their `runtime_artifact_guard.py` patch.

### Q4 — routing DSL (already partially solved)

`library/policies/routing_rules.json` + `scripts/routing_policy_resolver.py` shipped in PR #12. **Critique the DSL** — what's missing for codex-funnel work specifically? Propose: per-axis routing affinities, sticky-session rules for trace-correlated work, fallback when a downstream framework is unhealthy.

### Q5 — event store maturity (unchanged)

`scripts/replay_matrix_state.py` filesystem walker handles 116 events today with 0 divergence. **Quantify** when it breaks: at what event rate? What divergence shapes appear under concurrent multi-manager writes? Propose the FS → JSONL append-stream → JetStream/Kurrent migration with explicit thresholds.

### Q6 — flow-health thresholds (unchanged)

`scripts/flow_health_check.py` thresholds are hardcoded. Propose hybrid policy: hard limits + rolling p90/p95/p99 over 30 days. Patch targets must be specific.

### Q7 — attestation federation (unchanged)

Map dogfood receipts → in-toto / SLSA / Sigstore / cosign / Rekor. Provide translator schema, verification commands, and the trust-boundary diagram.

## Constraints

- **Matrix-native implementation only.** Adapt patterns, do not vendor.
- **Every recommendation must include Matrix file targets + acceptance gate + TNT fixture.**
- **Dense technical output.** No marketing prose. If a technique didn't pan out, say so explicitly with the numbers.
- **Cite the evidence pack file for every claim.** Speculation without an anchor goes in "Open questions" (Required Output 8).
- **Inspired-code citations must include commit SHA.** Not just repo + filename.

## Synthesis section (after Q1-Q7)

1. **Top 3 leverage points** — recommendations where solving one question makes 2+ others easier
2. **Top 3 conflicts** — places where the answer to one question contradicts another
3. **5 ordered build paths** — time-to-value ranked, each path is a sequence of merge-able PRs
