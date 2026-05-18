# Deep Research Prompt — Codex × Matrix Funneling and Refactor Ceiling

**Repo under study**: this repo (`codex-matrix-port`) — 110 sealed assets / 4,886 files / 53 MB. The 4,339-file source tree under `codex-cli/`, `codex-rs/`, `sdk/`, `docs/` is the upstream OpenAI codex code; the `.matrix/` subdir holds Matrix-native provenance, registry, and adapter stubs.

**Two open questions** the research must address. They are **orthogonal** — please answer both, do not collapse one into the other.

---

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

Find and rank existing **inspired-code** sources (we adapt, we don't vendor — license is not blocking):

- LSP / DAP adapters between editors and language servers (closest pattern to codex's app-server)
- Erlang/OTP `gen_server` ↔ external protocol bridges
- Temporal / Cadence workflow engines (rollout-trace analogue)
- OpenTelemetry collectors (tracer adapter analogue)
- WASM component-model bindings (sandbox boundary analogue)

For each, give: repo + one-line mechanism + which codex axis it informs + the specific file/function to study.

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
