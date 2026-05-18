# Pipeline Evidence — what the Matrix pipeline can determine about codex deterministically

Generated 2026-05-18. All artifacts in this directory were produced by running the F4-acceptance / coin-sorter pipeline against the codex source with `--budget-agents=0` (no agent in the critical path). The research prompt in `../../RESEARCH_PROMPT.md` should be evaluated against this evidence before speculating about what the pipeline could do.

## Provenance

- Codex source: `C:\Users\yonat\Desktop\codex\repo` (50 MB upstream codex)
- Matrix pipeline: `https://github.com/locogrande/matrix` (commit `76008f7c2` — F4 P0-P14 + followup gap closure merged)
- Tools used: `tools/collector_pipeline.py`, `tools/seal_worker.py`, `scripts/form_bundle_resolver.py`, `scripts/voltmeter_v2.py`, `scripts/build_matrix_app_state.py`, `scripts/replay_matrix_state.py`, `scripts/flow_health_check.py`, `tools/scan_codex_matrix_port_guard.py`

## What's here

### 01 — Collector classification (`01_collector_classification.json`)
Single-pass coin-sorter walk of the upstream codex source. Every file gets exactly one slot from `{MANIFEST, TEST, DOC, PATH, SEMANTIC, EXT, ORPHAN}`. Cross-language: Rust + TypeScript + Python + Markdown.

| Slot | Count | What it means |
|---|---|---|
| PATH | 2,269 | Files inside `src/`, `bin/`, `schema/`, `templates/`, `plugins/`, `packages/` |
| TEST | 601 | Matched `tests?/`, `spec/`, `__tests__/`, `test_*`, `*_test`, `*_tests` |
| DOC | 532 | `README*`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`, `LICENSE`, `NOTICE`, `AGENTS.md`, `.md`, `.rst`, `.txt` |
| MANIFEST | 253 | `Cargo.toml`, `package.json`, `pyproject.toml`, `go.mod`, `BUILD.bazel`, `MODULE.bazel`, `WORKSPACE`, `pnpm-workspace.yaml`, `yarn.lock` |
| SEMANTIC | 219 | Files with a known semantic parser (libcst / tree-sitter) |
| ORPHAN | 77 | Files no slot matched — at `--budget-agents=0` these flow through; with budget>0 they would escalate to agent classification |
| EXT | 2 | Recognised extension but no other slot fit |
| SKIP | 0 | Skipped during walk (`.git`, `node_modules`, `target`, etc. — never enter classifier) |

- **3,953 files** total (post-skip)
- **130 manifest directories** (Cargo.toml + package.json roots)
- **3,355 semantic-bridge candidates** (libcst+tree-sitter probed)
- **JS dep graph**: 553 JS/TS files, 1,055 import edges
- **0 agent escalations** — fully deterministic

### 02 — Codex registry snapshot (`02_codex_registry_snapshot.json`)
The 113 codex registry rows in `.matrix/registry/assets.jsonl` reduced to 110 unique `asset_id`s (3 collisions documented inline). Source-of-truth for what's been sealed.

### 03 — Codex form bundle (`03_codex_form_bundle.json`)
Output of `scripts/form_bundle_resolver.py` for `{action: 'ipr_submit', framework: 'tightrope', risk: 'high', work_order_id: 'WO_codex_app_server_demo'}` — the bundle codex would attach to a `tightrope_dispatch_workorder` call **if** its tools were Forager-registered through the funnel adapter.

- bundle: **7 forms** (`kernel.ipr_submission`, `kernel.review_record`, `kernel.acceptance_receipt`, `kernel.flow_event`, `kernel.form_proposal`, and the action addons)
- framework preload: also returns the tightrope-local form set
- 0 missing — every form_id resolves cleanly

### 07 — Caps cutover (`07_caps_cutover.json`)
68 caps across 2 boards (netrix_forms=59, pipeline_design=9), 0 path-canonicality violations, 0 waivers in flight. Caps are codex-agnostic right now; once the `app_server → Circuts` funnel is wired, codex would emit caps on its app-server protocol ports.

### 08 — Voltmeter probes (`08_codex_voltmeter_probes.json`)
12 probes across `form`, `code`, `signal`, `ui_event` classes targeting codex assets:
- 5 form-class probes against kernel + netrix forms → 5 gate_pass
- 4 code-class probes against existing codex manifest paths in the matrix mirror → 4 gate_pass
- 1 code-class probe against `as_codex_does_not_exist` (intentional miss) → gate_fail (correctness)
- 1 ui_event probe against MATRIX_APP_STATE staleness → gate_fail (real condition)
- 1 signal probe against `circuts://board/codex/app_server/in` → gate_pass (route discoverable)

### 09 — Reuse lookup (`09_reuse_lookup.json`)
PatternCard + ActionRecipe queries for keywords `port`, `receipt`, `gate`. Shows what the reuse KB returns for codex-relevant work today. Result: 3 PatternCards + 3 ActionRecipes seeded; lookup is deterministic; codex-port pattern matches `pc_coin_sorter_pipeline` + `ar_repo_port_first_seal`.

### 10 — Codex export dry-run receipt (`10_codex_export_dryrun_receipt.json`)
Pure dry-run derived from the codex-matrix-port registry. **113 eligible rows / 110 unique asset_ids**, 0 cap blockers. A real run (validated earlier on `as_codex_app_server_protocol`) copies 814 files per asset on average. Shows what the exporter would produce without actually copying ~50 MB into the evidence directory.

### 12 — Replay state (`12_replay_state.json`)
Pure reducer over 4 event sources (receipts + recycle reports + voltmeter probes + materializer reports). **13 accepted phases** (P2-P14), 0 divergence vs live MATRIX_APP_STATE. The receipts list includes the Wave 33 codex-port dogfood, so the replay reconstructs the codex-port history from structured events, not terminal text.

### 13 — Flow health (`13_flow_health.json`)
Production-management metrics: WIP per manager, queue age p95, blocker age, review latency, rework 24h, acceptance rate. Acceptance rate **1.0** (all 13 receipts validated). Real findings flagged: WIP over cap (52+94 historical worker dirs, cleanup deferred).

### 14 — Codex artifact guard (`14_codex_artifact_guard.json`)
Pre-commit-hook semantics run against the codex-matrix-port repo (4,889 tracked files). **2 real findings**:
1. `codex-rs/Cargo.lock/Cargo.lock` — `blocked_suffix:.lock`. This is a **genuine export bug** — the upstream `Cargo.lock` file got copied as a directory `Cargo.lock/` containing `Cargo.lock`. P14 surfaces it; would need to be fixed before any real downstream consumer.
2. `sdk/python/uv.lock` — `blocked_suffix:.lock`. This is a **guard over-trigger** — `uv.lock` is a legitimate Python dependency lock file for reproducibility, not a runtime sentinel. The `BLOCKED_SUFFIXES = {.lock, ...}` rule should be refined to exclude project-lock files (`Cargo.lock`, `uv.lock`, `package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`).

## What the evidence proves the pipeline can do deterministically (today)

- **Classify** any external repo's source files into 8 slots in a single pass (3,953 files / 0 ORPHAN escalations on codex)
- **Seal** files with content-hash-root verification (110 unique codex assets)
- **Build** a form-bundle envelope per task class (7 forms attached cleanly)
- **Probe** any matrix-resident artifact for existence + freshness (12 probes, correctly identifies real + missing targets)
- **Export** an asset filter to a tagged bundle (813 files copied per asset, exclusions enforced)
- **Replay** state from append-only event sources (13 accepted phases, 0 terminal-text trust)
- **Measure** flow health against fixed threshold policy (6 metrics + structured findings)
- **Catch** real export bugs (`Cargo.lock`-as-directory) and over-broad rule triggers (`uv.lock` should be allowlisted) before commit

## What's still architectural (not in evidence)

- The 6 funneling axes from `RESEARCH_PROMPT.md` are still adapter stubs — codex runtime behavior doesn't actually flow through Circuts/Tracer/Forager/Library/Truarch yet. This evidence pack shows what the **acceptance chassis** can do once the adapters land; designing those adapters is the research task.

## Reproducing

From the matrix repo (commit `76008f7c2` or later):

```bash
# 01
python tools/collector_pipeline.py C:/Users/yonat/Desktop/codex/repo --out runtime/codex_collector.json --budget-agents 0

# 03
python -c "import importlib.util,json; s=importlib.util.spec_from_file_location('r','scripts/form_bundle_resolver.py'); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); print(json.dumps(m.resolve({'action':'ipr_submit','framework':'tightrope','risk':'high'}), indent=2))"

# 07
python scripts/caps_cutover_report.py

# 08
python scripts/voltmeter_v2.py smoke

# 12
python scripts/build_matrix_app_state.py && python scripts/replay_matrix_state.py

# 13
python scripts/flow_health_check.py

# 14 (against codex-matrix-port)
python tools/scan_codex_matrix_port_guard.py
```
