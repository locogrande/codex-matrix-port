# Deep Research Prompt V2 — Codex × Matrix Runtime Funneling, Refactor Ceiling, Guard Policy, Routing, Event Store, Flow Metrics, Attestation

Repository under study: `locogrande/codex-matrix-port`.
Matrix platform reference: `locogrande/matrix`.

First read `.matrix/pipeline_evidence/INDEX.md` and all JSON evidence files. Every claim must cite the evidence file or a direct repo/doc prior-art source. Do not speculate when the evidence is missing; create a follow-up work item instead.

Output must be implementation-grade, not essay-grade.

## Required outputs

1. Executive summary ≤300 words: numbers + verdicts only.
2. Funneling architecture table: six axes; 2–3 adapter options each; ranked; dependency DAG.
3. Refactor-ceiling table: technique, tool, exact files examined, additional ceiling, overlap with existing 2.3%, P5 cost, funnel leverage.
4. Matrix implementation map: repo files to edit, new files, tests, gate evidence, TNT fixtures.
5. PatternCards: reusable mechanism cards for every adopted pattern.
6. ActionRecipes: deterministic scripts/actions to reuse without agent reasoning.
7. Inspired-code bibliography: repo URL + exact file/function/commit SHA + 1-line mechanism.
8. Open questions: only items not answerable from current evidence.

## Evidence anchors

Use these as factual inputs:
- `.matrix/pipeline_evidence/01_collector_classification.json`
- `.matrix/pipeline_evidence/02_codex_registry_snapshot.json`
- `.matrix/pipeline_evidence/03_codex_form_bundle.json`
- `.matrix/pipeline_evidence/07_caps_cutover.json`
- `.matrix/pipeline_evidence/08_codex_voltmeter_probes.json`
- `.matrix/pipeline_evidence/10_codex_export_dryrun_receipt.json`
- `.matrix/pipeline_evidence/12_replay_state.json`
- `.matrix/pipeline_evidence/13_flow_health.json`
- `.matrix/pipeline_evidence/14_codex_artifact_guard.json`

## Q1 — Runtime funneling

Answer each axis separately. For each, include: adapter architecture, event schema, failure semantics, state ownership, gate, TNT fixture, next-task dogfood use.

Axes:
1. `app_server` + `app_server_protocol` → Circuts.
2. rollout/trace → Tracer.
3. tools/tool handlers → Forager + Tightrope.
4. thread_store/message_history → Library canon.
5. memories/skills → Forager assets + reuse KB.
6. sandboxing/bwrap/windows/linux hardening → Truarch.

Prior-art minimum set:
- MCP spec/server implementations.
- LSP/DAP adapters.
- Temporal/Cadence event history.
- OpenTelemetry Collector pipeline.
- Letta memory store.
- LangGraph checkpointing.
- LiteLLM/function-call proxy.
- WASM component model.

## Q2 — Refactor ceiling

Run or specify exactly how to run:
- jscpd / PMD CPD / NiCad / Simian / SourcererCC.
- tree-sitter / ast-grep structural clone scan.
- CodeBERT/embedding semantic clone scan.
- cargo-machete / cargo-udeps / cargo metadata workspace audit.
- dependency-cruiser / nx / turborepo TS graph audit.
- macro/test prelude survey.
- type alias / ID type unification survey.
- markdown/prose dedupe scan.

Separate additive ceiling from already-measured 2.3%.

## Q3 — Artifact guard

Produce minimal patch and regression tests for lockfile policy:
- allow project lockfiles by basename.
- block runtime lock sentinels by pattern.
- block file-as-directory lockfile collision.
- preserve `.log`, `.pyc`, `.pyo`, `.tmp`, `.pid` blocking.

## Q4 — Routing DSL

Replace F4 phase heuristic with JSON routing policy.
Must support manager capability, cap, cost, priority, task class, framework, sticky locality, failure fallback, and blocked reason.

## Q5 — Event store threshold

Quantify when filesystem reducer fails. Preserve pure reducer semantics. Provide FS → JSONL stream → JetStream/Kurrent/Marten migration path.

## Q6 — Flow-health thresholds

Recommend fixed, rolling, or hybrid. Give formulas and patch targets.

## Q7 — Attestation federation

Map dogfood receipt → in-toto/SLSA/Cosign/Sigstore. Provide translator schema and commands.

## Constraints

- Matrix-native implementation only; no vendored code.
- Use external repos for mechanism study only.
- Every recommendation must include Matrix file targets and acceptance gate.
- Dense technical output only. No marketing prose.
