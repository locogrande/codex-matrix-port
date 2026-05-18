# codex-matrix-port

A Matrix-ported view of the [codex](https://github.com/openai/codex) repo. Same source code at the top level; Matrix-native provenance and registration under `.matrix/`.

## Layout

```
codex-matrix-port/
├── codex-rs/                 # original codex Rust workspace (110+ crates)
├── codex-cli/                # codex CLI entrypoint
├── sdk/                      # codex SDKs
├── docs/                     # codex docs
└── .matrix/
    ├── registry/
    │   └── assets.jsonl              # 113 registry rows for 110 unique codex assets
    ├── components/<asset_id>/        # per-asset Matrix metadata (no source duplication)
    │   ├── manifest.json             # asset descriptor + sealed contract
    │   ├── source_map.json           # file-list + per-file hashes
    │   ├── provenance.json           # creation lineage
    │   ├── asset.json                # top-level asset envelope
    │   ├── reuse_map.md              # port classification (USE/REFACTOR/REJECT)
    │   └── evidence/                 # signatures + content-hashes + receipts
    └── framework_kit_adapters/<framework>/__init__.py   # per-framework adapter stubs
```

## What this is

The codex source code, organized identically to its upstream tree, with a parallel `.matrix/` envelope that:

- **Indexes** every asset (110 unique) with a stable `asset_id`
- **Tracks provenance** — every file linked to its `content_hash`, `source_path`, `sealed_at`, and `wo_id`
- **Reproduces** — the sealed contract guarantees `content_hash_root == expected_plan_hash` for each asset
- **Composes** — each asset has an adapter stub at `.matrix/framework_kit_adapters/<framework>/` that any Matrix instance can import

## Asset stats

- **110 unique asset_ids** sealed
- **113 registry rows** (3 collisions documented in `.matrix/registry/assets.jsonl` notes)
- **Primary frameworks** spanning: `automation_tools`, `build_config`, `contracts`, `docs`, `forager`, `framework_kit_adapter`, `lockfile`, `netrix_extension`, `office_framework`, `readme`, `tightrope`, `unmapped`, `youmove`
- ~4,300 source files mirrored at top-level
- Total: ~53 MB

## Provenance

- Source: `C:\Users\yonat\Desktop\codex\repo` (original codex 4,529-file repo)
- Port session: 2026-05-18, Matrix framework root at sealed via `tools/seal_worker.py` + `tools/collector_pipeline.py`
- Issue ledger: 42 entries documented during port (see `.matrix/migration_archive/` if attached)
- Dogfood test: Wave 33 pass — 4/4 assets verified `content_hash_root == expected_plan_hash`

## How to use

### As a codex consumer
Same as upstream codex: `cd codex-rs && cargo build`. The top-level layout is unmodified.

### As a Matrix consumer
```python
import json
registry = [json.loads(line) for line in open(".matrix/registry/assets.jsonl") if line.strip()]
codex_assets = {row["asset_id"]: row for row in registry if row["asset_id"].startswith("as_codex_")}
print(f"Loaded {len(codex_assets)} codex assets")
```

Then read manifests from `.matrix/components/<asset_id>/manifest.json` for full asset descriptors.

## License

Source under `codex-rs/`, `codex-cli/`, `sdk/`, `docs/` retains its upstream codex license (see `codex-rs/LICENSE`).

Matrix metadata under `.matrix/` is unlicensed-pending; the port pipeline itself is at https://github.com/<TBD>/matrix.
