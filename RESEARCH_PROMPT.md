# Deep Research Prompt — Codex × Matrix Funneling and Refactor Ceiling

**Repo under study**: this repo (`codex-matrix-port`) — 110 sealed assets / 4,886 files / 53 MB. The 4,339-file source tree under `codex-cli/`, `codex-rs/`, `sdk/`, `docs/` is the upstream OpenAI codex code; the `.matrix/` subdir holds Matrix-native provenance, registry, adapter stubs, **and concrete pipeline evidence** (see `.matrix/pipeline_evidence/INDEX.md`).

**Before researching, read the evidence pack.** The Matrix F4 acceptance pipeline has been run end-to-end against the codex source at `--budget-agents=0` (no agent in the critical path). The 10 JSON files + INDEX in `.matrix/pipeline_evidence/` show exactly what the deterministic pipeline produces today. Ground every claim in these numbers, not in speculation. The pipeline:

- Classifies all 3,953 codex files into 8 deterministic slots with 0 ORPHAN escalations (`01_collector_classification.json`)
- Indexes 113 codex registry rows reducing to 110 unique asset_ids (`02_codex_registry_snapshot.json`)
- Builds a tightrope form bundle of 7 forms with 0 missing for any task class (`03_codex_form_bundle.json`)
- Tracks 68 caps across 2 boards with 0 path violations (`07_caps_cutover.json`)
- Probes assets via 5 classes (cap/form/signal/ui_event/code), correctly flagging real misses (`08_codex_voltmeter_probes.json`)
- Surfaces a real export bug: `codex-rs/Cargo.lock/Cargo.lock` (Cargo.lock got copied as a directory) (`14_codex_artifact_guard.json`)
- Replays 13 accepted F4 phases from event sources with 0 divergence vs live state (`12_replay_state.json`)

The F4 acceptance chassis (P0 conformance + P1 receipt validator + P12 replay + P14 artifact guard) is live and gating today. The 6-axis **funnel adapters** that would route codex runtime through Matrix frameworks at runtime are still stubs — that is what this research is for.

**Two open questions** the research must address. They are **orthogonal** — please answer both, do not collapse one into the other.

---

## Seven open questions

The research must answer all seven. Q1 and Q2 are the architectural core (funneling + refactor ceiling). Q3-Q7 are smaller-scope but were surfaced by running the F4 acceptance chassis against codex — they share the same evidence pack as input.

## Question 1 — Mechanical funneling: codex behavior → Matrix frameworks

### What we have

Codex is currently *registered* in Matrix (every asset has an `asset_id`, a `primary_framework`, and an adapter stub) but is **not wired** into Matrix at runtime. The adapter stubs at `.matrix/framework_kit_adapters/<framework>/__init__.py` are skeletons — they import their framework but do not translate codex events into Matrix calls.

The six funnel axes that need mechanical bridges:

| Codex primitive (assets) | Matrix framework target | Today |
|--|--|--|
| `as_codex_app_server` + `as_codex_app_server_protocol` (JSON-RPC over stdio/uds) | **Circuts** signal routing (signals + routes + relays) | stub only |
| `as_codex_rollout` + `as_codex_rollout_trace` | **Tracer** records (`tracer_record_trace`, `tracer_emit_conduit_transform`) | stub only |
| `as_codex_tools` (tool definitions + handlers) | **Forager** tool registry + `tightrope_dispatch_worker` | parallel registries, no bridge |
| `as_codex_thread_store` + `as_codex_thread_manager_sample` + `as_codex_message_history` | **Library** canon (`library_submit_promotion`, `library_record_lesson`) | not wired |
| `as_codex_memories` + `as_codex_skills` + `as_codex_core_skills` | **Forager** asset registry (`forager_submit_asset`, `forager_compose`) | not wired |
| `as_codex_sandboxing` + `as_codex_bwrap` + `as_codex_linux_sandbox` + `as_codex_windows_sandbox_rs` + `as_codex_process_hardening` | **Truarch** boundary enforcement (`truarch_check_invariants`, `truarch_scan_boundaries`) | not wired |

### Research task 1.1 — Architecture options for each axis

For each of the six axes above, lay out 2-3 concrete adapter architectures and rank them by:

- **Round-trip fidelity** — can the bridge carry events *back* (Matrix → codex), or is it one-way?
- **Statefulness** — does the adapter need its own store, or can it stay stateless and trust both sides?
- **Failure isolation** — if the Matrix framework call fails, does codex's local action still complete? (P1 — preserve principal authority)
- **Schema cost** — do we need a new shared contract type, or can we reuse existing codex protocol types verbatim?
- **Implementation order** — which axis must land first so the others can dogfood through it? (Hypothesis: `app_server_protocol → Circuts` is the chassis, then `rollout → Tracer` rides on top.)

Required output: a 6-axis table with the ranked architecture per axis and an explicit dependency DAG.

### Research task 1.2 — Existing prior art

Find and rank existing **inspired-code** sources (we adapt, we don't vendor — license is not blocking). Cover **two generations** of prior art and explicitly compare them:

**2015-2020 generation** (protocol-level adapters):
- LSP / DAP adapters between editors and language servers (closest non-LLM pattern to codex's app-server)
- Erlang/OTP `gen_server` ↔ external protocol bridges
- Temporal / Cadence workflow engines (rollout-trace analogue)
- OpenTelemetry collectors (tracer adapter analogue)
- WASM component-model bindings (sandbox boundary analogue)

**2024-2025 generation** (LLM-agent interop — these are likely *much* closer to codex's actual shape):
- **Model Context Protocol (MCP)** — Anthropic's open spec for tool servers; codex's own app-server speaks an MCP-shaped protocol on the wire. Likely the cleanest funnel-axis-1 adapter pattern.
- **Letta** (formerly MemGPT) — persistent agent memory store, archival + recall semantics. Direct analogue for `as_codex_memories` + `as_codex_message_history` → Library/Forager funnel.
- **LangGraph** — explicit state-machine checkpointing for agent workflows. Analogue for `as_codex_rollout` + `as_codex_thread_manager_sample` → Tracer.
- **OpenAI function-calling proxy patterns** (e.g. `function-call-bridge`, `litellm`'s tool routing) — proxy-shaped adapters between agent tool calls and arbitrary backends. Analogue for `as_codex_tools` → Forager+Tightrope.
- **Sigstore / in-toto attestations** — supply-chain proof shape that matches the dogfood receipt envelope (relevant to Q7 below).

For each, give: repo + one-line mechanism + which codex axis it informs + the specific file/function/commit-SHA to study. **Explicitly state whether the 2020-era pattern is dominated by a 2025-era pattern for each axis** — Matrix should not reinvent LSP if MCP already solves the same shape.

---

## Question 2 — Codex internal refactor: what's the real ceiling, and which techniques unlock it?

### What we already measured

Two independent scans of the 110-asset codex source, ~1.018M LOC across 4,339 files:

**Miro deterministic scan** (`runtime/codex_refactor_miro_scan.json` — published method: count import statements appearing ≥5 times across distinct assets):

| Metric | Value |
|--|--|
| Assets scanned | 89 (Rust crates with `Cargo.toml`) |
| Files scanned | 3,061 |
| Total LOC | 1,018,475 |
| Unique import statements | 11,125 |
| Total import occurrences | 35,646 |
| Hoistable patterns (≥5 distinct assets) | 1,155 |
| Estimated lines saved by hoisting | 20,627 |
| **Ceiling from imports alone** | **2.03 %** |

**gpt deeper-pattern scan** (`managers/miro/inbox/note_from_gpt_codex_refactor_patterns.md` — adds non-import patterns: Cargo manifest templates, test prelude / fixture builders, protocol DTO derive aliases, path constants, error wrappers, Display/FromStr macros, registry hygiene):

| Rank | Pattern | Lines saved | Determinism |
|---:|--|---:|--|
| 1 | Test support prelude + fixture builders (`pretty_assertions::assert_eq` 765 hits, `MockServer::start` 202, `#[tokio::test]` 2,401, tempdir 600+) | 700–1,200 | counts deterministic, grouping AI |
| 2 | Cargo manifest template/generator (117/118 Cargo.toml share package + workspace + lint blocks) | 350–460 | fully deterministic |
| 3 | Protocol DTO derive alias / proc macro (300 + 115 + 47 exact derive-stack repeats) | 900–1,300 | AI judgment |
| 4 | Codex path constants (`.join("config.toml")` 272, `.join(".git")` 201, `.join(".codex")` 178, `.join("repo")` 119) | 120–220 | deterministic |
| 5 | Test aggregator generator (`tests/all.rs` style + `mod suite;` 11 assets) | 80–140 | deterministic |
| 6 | Package JSON metadata template (4 packages share module/license/repo) | 30–60 | deterministic |
| 7 | Error-wrapper helpers (`pub enum *Error` 77, `thiserror::Error` 29, transparent/string wrappers 54) | 80–180 | AI judgment |
| 8 | Display/Error/FromStr impl macros (`Default` 82, display 62, error 12, FromStr 10) | 80–160 | AI judgment |
| 9 | Protocol mapper macro (dense `impl From<Core...>` in app-server protocol) | 150–300 | AI judgment |
| 10 | Registry/source-map hygiene (duplicate `as_codex_cli` rows, missing `source_root`) | 0 code, audit-time savings | deterministic |

**Summed gpt-scan ceiling**: ~2,490–4,020 lines (~0.24–0.39 % of total). Combined with the Miro import ceiling: **~23–25 K lines, ~2.3 %**.

### The actual question

Both scans report a ceiling **under 3 %**. That feels low for a ~1M LOC monorepo with strong upstream evolution patterns. Three hypotheses for *why*:

- **H1 — The codex code is already lean.** Upstream maintainers have already deduplicated. Anything left is intentional inline.
- **H2 — Our techniques only see syntactic surface.** Import counts + literal joins + derive-stack repeats are the easy 3 %. The real centralization gains are *semantic*: parallel implementations of the same algorithm in different crates, structurally-equivalent functions, repeated state-machine shapes.
- **H3 — Many candidates are intentionally inline.** Hoisting them would help line count but hurt readability/dependency-locality (P5 — don't hide dependencies).

### Research task 2.1 — Find the bigger gains (or prove they don't exist)

Evaluate these techniques against the codex source in this repo:

- **AST-level clone detection** (Type-1/Type-2/Type-3 clones) — tools: `nicad`, `simian`, `pmd-cpd`, `jscpd`, `sourcerer-cc`, `oreo`. Which run on Rust + TypeScript + Python? Report: 5–10 highest-value clones with file paths and ceilings.
- **Embedding-based semantic clone detection** — `code2vec`, `infercode`, CodeBERT, treesitter-AST embedding + cosine. Report whether the embeddings find Type-4 clones (semantically equivalent, syntactically different) that the deterministic scans missed.
- **Cargo workspace dedup** — codex-rs has 110+ crates. How many share dependency *version pins*, *feature flags*, *lint configs*? What does `cargo-machete` + `cargo-udeps` + `cargo-features-manager` actually save? Quantify.
- **Modern monorepo tooling** (the F4 evidence shows codex has Cargo + npm + pnpm + pyproject mixed in 130 manifest dirs — syntactic scans miss this):
  - `nx`, `turborepo` — TypeScript monorepo dep graph + task caching; would find unused TS deps the import-only scan can't see
  - `bazel`, `pants` — Python monorepo build with strict dep declaration; surfaces over-declared dependencies
  - `cargo-udeps`, `cargo-machete` — Rust unused-dependency detection per crate
  - `cargo-features-manager` — feature flag dedup across workspace
  - `verdaccio` + `dependency-cruiser` — npm dep boundary enforcement
  Report quantified savings from running each on this repo, **separated from the import-scan ceiling** (so we know what's additive vs overlapping).
- **Macro consolidation surveys** — tools to find macro candidates: `dylint`, custom `syn` walks. Specifically: do the 1,400+ `#[tokio::test]` + `#[test]` attribute occurrences hide a `#[matrix::test]` candidate that captures setup + teardown + tracer-span + Voltmeter probe in one attribute?
- **Cross-crate type unification** — count distinct definitions of `Result<T,E>` aliases, error chains, ID types (`SessionId`, `ThreadId`, `WorkOrderId`-equivalents). Report the unification savings if the duplicates are merged into a `codex-common-types` crate.
- **Documentation/markdown dedup** — there are 433 manifest-equivalent markdown files. How much duplicate prose (READMEs that copy each other)?

For each technique: did it run on this codebase, what did it find numerically, what's the *additional* ceiling on top of the Miro+gpt scans, and what specifically does it cost in P5 terms (dependency hiding)?

### Research task 2.2 — Combine with the funneling axis

The most valuable refactors are the ones that *also enable* funneling. Examples:

- A `codex-common-types` crate with shared `SessionId` / `ThreadId` is also the schema chassis for `Library` canon entries (axis 4) and `Forager` asset IDs (axis 5).
- A `#[matrix::test]` attribute macro is also the entry-point for Tracer span emission (axis 2).
- The Cargo manifest template (rank 2) is what lets us inject `[dependencies.matrix-framework-kit-adapter]` consistently — the funneling bootstrap.

Rank the refactor opportunities by **funnel-leverage** (does this refactor also reduce funneling-adapter cost?) in addition to raw line savings.

---

## Constraints, principles, and conventions

- **No licensing concern** — we adapt patterns and *reimplement* in Matrix; we do not vendor whole packages. Inspired-code citations are fine.
- **Principle P3** — centralize repeated source contracts; **P5** — never centralize at the cost of hiding production dependencies. A scoped test-prelude is acceptable; a global production prelude is not.
- **Dogfood-only** — every refactor must be testable through the existing Matrix dogfood pipeline (`tools/seal_worker.py` + `tools/validate_dogfood_receipt.py`); receipt-less changes are rejected.
- **Inspired-code sources** must include the specific file/function/commit-SHA you'd study, not just the repo name.

---

## Companion datasets in this repo

- `.matrix/registry/assets.jsonl` — 113 codex registry rows, all 110 asset_ids, primary_framework distribution
- `.matrix/components/<asset_id>/source_map.json` — per-file SHA256s + paths for each asset (use as ground-truth when proposing structural changes)
- `.matrix/components/<asset_id>/manifest.json` — sealed contract per asset
- `codex-rs/Cargo.toml` (workspace root) + 117 per-crate `Cargo.toml`s — Cargo workspace structure
- `codex-cli/package.json` + sibling `sdk/typescript/package.json` etc. — npm metadata

## Expected output format

1. **Executive summary** (≤ 300 words) — both questions answered as crisp numbers + a one-sentence verdict per axis.
2. **Funneling architecture table** — 6 rows × ranked options.
3. **Refactor-ceiling refinement** — updated table with the techniques you ran, additional ceiling each unlocked, and the P5 cost per technique.
4. **Cross-axis leverage** — the 5 refactors that also reduce funneling cost, with implementation order.
5. **Inspired-code bibliography** — repo + file + commit-SHA + 1-line mechanism for each citation.
6. **Open questions still unresolved** — what *you* couldn't answer with the data in this repo, framed as crisp follow-up prompts.

**Tone**: short sentences, dense numbers, no marketing prose. If a technique didn't pan out, say so explicitly.

---

## Question 3 — Pre-commit hook policy refinement

**Surfaced by**: `.matrix/pipeline_evidence/14_codex_artifact_guard.json` showing **2 real findings**:
1. `codex-rs/Cargo.lock/Cargo.lock` — a genuine export bug (Cargo.lock got copied as a directory). P14 surfaced it correctly.
2. `sdk/python/uv.lock` — a guard over-trigger. `uv.lock` is a legitimate Python dependency lock for reproducibility, not a runtime sentinel.

The current `runtime_artifact_guard.py` rule `BLOCKED_SUFFIXES = {.log, .pyc, .pyo, .tmp, .pid, .lock}` is too coarse. It conflates:

- **Project lockfiles we want tracked**: `Cargo.lock`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `uv.lock`, `poetry.lock`, `Gemfile.lock`, `composer.lock`, `Pipfile.lock`, `go.sum`
- **Runtime sentinel locks we want blocked**: `*.jsonl.lock`, `*.queue.lock`, `*.pid` lock files used by daemons for mutex

### Research task 3.1 — Survey prior art

Survey production-grade pre-commit hook systems and document their classification rules:

- `pre-commit` framework (`pre-commit/pre-commit-hooks`) — `check-added-large-files`, `forbid-new-submodules`, etc.
- `husky` + `lint-staged` (npm)
- `lefthook` (Go-based, multi-language)
- `gitleaks` (secret detection)
- `talisman` (secret + key detection)
- `pre-commit-hooks/pre-commit-hooks` (the repo, not the framework)
- GitHub's native `.gitattributes` `filter` + `diff` rules
- `git-secrets` (AWS Labs)

For each: what's their lockfile policy? Allowlist? Suffix-blocklist with name-allowlist override? AST-based?

### Research task 3.2 — Propose Matrix's refined rule

Specifically propose:
- Updated `BLOCKED_SUFFIXES` keeping `.log`, `.pyc`, `.pyo`, `.tmp`, `.pid` but excluding `.lock`
- New `LOCKFILE_ALLOWLIST = {Cargo.lock, package-lock.json, pnpm-lock.yaml, yarn.lock, uv.lock, poetry.lock, Gemfile.lock, composer.lock, Pipfile.lock, go.sum}` — match exact basenames
- New `LOCKFILE_BLOCKLIST = {*.jsonl.lock, *.queue.lock, *.daemon.lock}` — match patterns
- Test cases that validate both findings stay caught/cleared correctly

Output: minimal patch to `scripts/runtime_artifact_guard.py` plus a regression test list.

---

## Question 4 — Routing heuristic generalization

**Surfaced by**: `scripts/workorder_materializer.py` lines 35-47, where the routing rule is hard-coded:

```python
def _route_manager(phase: dict[str, Any]) -> str:
    if mgr := phase.get("manager"):
        return mgr
    priority = (phase.get("priority") or "").lower()
    p = (phase.get("phase") or "").upper()
    if p in {"P0", "P1", "P2", "P3", "P4", "P8", "P14"}:
        return "cl_miro"
    if priority == "critical":
        return "gpt_miro"
    return "cl_miro"
```

This breaks the moment work doesn't have F4 phase IDs — which is exactly what will happen when the funnel adapters land and codex sub-work routes through Tightrope without P0-P14 framing.

### Research task 4.1 — Survey production schedulers

For each, document the routing primitive + DSL shape:

- **Kubernetes**: nodeSelector, taints/tolerations, affinity rules, topology spread constraints
- **Nomad**: constraint stanzas, datacenter/region matching, weighted preferences
- **Apache Airflow**: executor types (LocalExecutor / CeleryExecutor / KubernetesExecutor), task queues, pools
- **Temporal**: task queues + worker affinity, sticky cache semantics
- **Apache Mesos / Apache YARN**: resource offer model
- **Slurm**: partition + QOS + features model

For each, give: smallest expressible routing rule, how it composes, what fails when it doesn't match.

### Research task 4.2 — Propose Matrix routing DSL

Matrix-shaped routing must handle:

- Manager capability matching (`cl_miro` = Claude xhigh, `gpt_miro` = codex xhigh)
- Per-manager caps (`cl_miro=3`, `gpt_miro=4`) — already in `scripts/worker_control.py`
- Priority bands (critical / high / normal)
- Cost-aware preference (codex cheaper for trivial; Opus required for principle-cited decisions)
- Locality (sticky-session affinity when codex pool already has thread state)
- Failure-fallback (gpt failure → cl_miro per `feedback_budget_and_tier_policy`)

Propose:
- A DSL (YAML or JSON) for declaring routes
- A reference resolver (drop-in replacement for `_route_manager()`)
- Migration plan from the current heuristic to the DSL

---

## Question 5 — Event store maturity

**Surfaced by**: `scripts/replay_matrix_state.py` walks 4 filesystem sources (receipts, recycle reports, voltmeter probes, materializer reports) every time and reduces in-memory. The evidence pack's `12_replay_state.json` shows this works for 18 events. **What's the scaling ceiling?**

### Research task 5.1 — Survey event stores

Document each on these axes: append throughput, query latency, schema evolution, projection support, divergence/CRDT semantics:

- **KurrentDB** (formerly EventStoreDB) — the canonical OSS event store
- **Marten** — Postgres-backed event sourcing for .NET (relevant pattern even if we don't use .NET)
- **Axon Framework** — JVM event-sourcing CQRS
- **NATS JetStream** — append-only streams with replay
- **Apache Kafka + ksqlDB** — streaming events with materialized views
- **Datomic** — immutable database with time-travel queries
- **rqlite** — lightweight raft-replicated SQLite (potential bridge)
- **EventStoreDB v23+** — projections + persistent subscriptions
- **Differential Dataflow** / **Materialize** — incremental view maintenance over event streams

### Research task 5.2 — Threshold analysis

Given the F4 pipeline's expected event rate (estimate: 10–50 events/hour today, scaling to 1k–10k/hour when funnel adapters fire on every codex tool call), at what event count does the filesystem-walk become unsustainable? What divergence/merge scenarios arise once two managers can emit events into the same stream?

Output: an event-count threshold (e.g. "≤100k events: filesystem-walk fine; >100k: graduate to KurrentDB-style"), plus a migration plan that preserves `replay_matrix_state.py`'s pure-reducer semantics.

---

## Question 6 — Threshold calibration for flow health

**Surfaced by**: `scripts/flow_health_check.py` hard-codes:

```python
THRESHOLDS = {
    "wip_per_manager_warn": 4,
    "queue_age_warn_s": 7200,
    "queue_age_critical_s": 21600,
    "blocker_age_critical_s": 3600,
    "review_latency_warn_s": 3600,
    "rework_24h_warn": 5,
    "acceptance_rate_min": 0.7,
}
```

These are guesses informed by `managers/shared/routing_and_caps.md`. They will be wrong for some workloads.

### Research task 6.1 — Survey industry baselines

Document the relevant industry frameworks and their numeric defaults:

- **DORA metrics** (Google's State of DevOps): deployment frequency, lead time for changes, change failure rate, mean time to recovery — what are 2024-2025 elite / high / medium / low thresholds?
- **SPACE framework** (GitHub research): Satisfaction, Performance, Activity, Communication, Efficiency
- **Toyota Production System / Lean** WIP limits — formulas, not just numbers
- **Theory of Constraints** queue-length thresholds
- **Kanban** lead-time vs cycle-time distinguishing rules

### Research task 6.2 — Adaptive vs fixed thresholds

Decide: should `flow_health_check.py` thresholds be:

- **(a) Fixed** — current; predictable but wrong for workload shifts
- **(b) Rolling baseline** — 30/60/90-day rolling p95 (like Datadog/Dynatrace anomaly detection); adapts but adds state
- **(c) Hybrid** — fixed hard limits + rolling soft limits

Output: chosen approach + the specific formula + a migration patch.

---

## Question 7 — Supply-chain attestation federation

**Surfaced by**: the dogfood receipt envelope (`library/source_assets/components/contracts/versions/v0001_initial/source/dogfood_receipt.schema.json`) is *isomorphic* to in-toto / SLSA provenance attestations. Should it federate?

### Research task 7.1 — Map Matrix receipts to existing standards

For each, document the schema overlap with Matrix's `{deliverables, gate_ref, dogfood_activation_ref, next_task_use_ref, notes}`:

- **SLSA v1.0 provenance** (Build L1-L4) — `predicateType`, `builder`, `buildDefinition`, `runDetails`
- **in-toto attestation** v1.0 — `subject`, `predicateType`, `predicate`
- **Sigstore Rekor** transparency log entries — what a Matrix receipt would look like as a Rekor entry
- **SBOM standards**: SPDX, CycloneDX — for declaring sealed-asset contents
- **Cosign attestation** — `cosign attest` workflow
- **The Update Framework (TUF)** — for receipt integrity over time

### Research task 7.2 — Federation proof of concept

If Matrix receipts federated as SLSA L3 attestations:

- A downstream consumer could run `cosign verify-attestation` against an exported asset to prove it came from a sealed Matrix pipeline run
- The codex export bundles in `exports/matrix_app_<ts>/` could carry an `attestation.intoto.jsonl` file
- Receipts could land in a Sigstore Rekor log for tamper-evident audit

Output:
- A `dogfood_receipt → in-toto predicate` translator schema
- The Sigstore commands a downstream user would run to verify a Matrix export
- A trust boundary diagram showing where Matrix's sealed-source-asset registry intersects with industry attestation chains

---

## Cross-question synthesis

After answering Q1-Q7 independently, produce **one** synthesis section that:

1. Lists the **top 3 leverage points** — research findings where solving one question makes 2+ others easier (e.g. "MCP adapter for Q1 also gives Q7 the natural in-toto subject ID")
2. Lists the **top 3 conflicts** — places where the answer to one question contradicts another (e.g. "Q4 routing DSL implies Q5 event store, but Q5 says filesystem is fine until 100k events")
3. Lists the **5 build orders** the Matrix team could pick from, ordered by total time-to-value
