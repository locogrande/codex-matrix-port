from __future__ import annotations
import hashlib, json
from pathlib import Path
ASSET_ID = "as_codex_skills"
ACCEPTED_VERSION = "v0001_initial"
EXPECTED_PLAN_HASH = "cac7389e788ac2c25f4ff640d2e63452837ae2957d193bf18b5095774d7158d8"
EXPECTED_COUNT = 48
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library" / "source_assets" / "components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'Cargo.toml', 'build.rs', 'src/assets/samples/imagegen/LICENSE.txt', 'src/assets/samples/imagegen/SKILL.md', 'src/assets/samples/imagegen/agents/openai.yaml', 'src/assets/samples/imagegen/assets/imagegen-small.svg', 'src/assets/samples/imagegen/assets/imagegen.png', 'src/assets/samples/imagegen/references/cli.md', 'src/assets/samples/imagegen/references/codex-network.md', 'src/assets/samples/imagegen/references/image-api.md', 'src/assets/samples/imagegen/references/prompting.md', 'src/assets/samples/imagegen/references/sample-prompts.md', 'src/assets/samples/imagegen/scripts/image_gen.py', 'src/assets/samples/imagegen/scripts/remove_chroma_key.py', 'src/assets/samples/openai-docs/LICENSE.txt', 'src/assets/samples/openai-docs/SKILL.md', 'src/assets/samples/openai-docs/agents/openai.yaml', 'src/assets/samples/openai-docs/assets/openai-small.svg', 'src/assets/samples/openai-docs/assets/openai.png', 'src/assets/samples/openai-docs/references/latest-model.md', 'src/assets/samples/openai-docs/references/prompting-guide.md', 'src/assets/samples/openai-docs/references/upgrade-guide.md', 'src/assets/samples/openai-docs/scripts/resolve-latest-model-info.js', 'src/assets/samples/plugin-creator/SKILL.md', 'src/assets/samples/plugin-creator/agents/openai.yaml', 'src/assets/samples/plugin-creator/assets/plugin-creator-small.svg', 'src/assets/samples/plugin-creator/assets/plugin-creator.png', 'src/assets/samples/plugin-creator/references/plugin-json-spec.md', 'src/assets/samples/plugin-creator/scripts/create_basic_plugin.py', 'src/assets/samples/skill-creator/SKILL.md', 'src/assets/samples/skill-creator/agents/openai.yaml', 'src/assets/samples/skill-creator/assets/skill-creator-small.svg', 'src/assets/samples/skill-creator/assets/skill-creator.png', 'src/assets/samples/skill-creator/license.txt', 'src/assets/samples/skill-creator/references/openai_yaml.md', 'src/assets/samples/skill-creator/scripts/generate_openai_yaml.py', 'src/assets/samples/skill-creator/scripts/init_skill.py', 'src/assets/samples/skill-creator/scripts/quick_validate.py', 'src/assets/samples/skill-installer/LICENSE.txt', 'src/assets/samples/skill-installer/SKILL.md', 'src/assets/samples/skill-installer/agents/openai.yaml', 'src/assets/samples/skill-installer/assets/skill-installer-small.svg', 'src/assets/samples/skill-installer/assets/skill-installer.png', 'src/assets/samples/skill-installer/scripts/github_utils.py', 'src/assets/samples/skill-installer/scripts/install-skill-from-github.py', 'src/assets/samples/skill-installer/scripts/list-skills.py', 'src/lib.rs')
def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == r["sha256_full"] for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
