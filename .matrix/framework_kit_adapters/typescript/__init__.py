from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_sdk_typescript"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "4f87fbbca91d16f3530123c189d2d5acf4209108a54d50f582b2612bc00abf08"
EXPECTED_COUNT = 30
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('.prettierignore', '.prettierrc', 'README.md', 'eslint.config.js', 'jest.config.cjs', 'package.json', 'samples/basic_streaming.ts', 'samples/helpers.ts', 'samples/structured_output.ts', 'samples/structured_output_zod.ts', 'src/codex.ts', 'src/codexOptions.ts', 'src/events.ts', 'src/exec.ts', 'src/index.ts', 'src/items.ts', 'src/outputSchemaFile.ts', 'src/thread.ts', 'src/threadOptions.ts', 'src/turnOptions.ts', 'tests/abort.test.ts', 'tests/codexExecSpy.ts', 'tests/exec.test.ts', 'tests/responsesProxy.ts', 'tests/run.test.ts', 'tests/runStreamed.test.ts', 'tests/setupCodexHome.ts', 'tests/testCodex.ts', 'tsconfig.json', 'tsup.config.ts')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
