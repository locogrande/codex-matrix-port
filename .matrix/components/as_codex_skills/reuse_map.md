# Reuse Map - as_codex_skills

Source: `codex-rs/skills`

Expected plan hash: `cac7389e788ac2c25f4ff640d2e63452837ae2957d193bf18b5095774d7158d8`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/skills/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/skills/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/skills/build.rs` | forager | USE | rust source - forager target |
| `codex-rs/skills/src/assets/samples/imagegen/LICENSE.txt` | unmapped | USE | compliance / SCM metadata - preserve verbatim |
| `codex-rs/skills/src/assets/samples/imagegen/SKILL.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/imagegen/agents/openai.yaml` | unmapped | USE | yaml source - unmapped target |
| `codex-rs/skills/src/assets/samples/imagegen/assets/imagegen-small.svg` | unmapped | USE | other source - unmapped target |
| `codex-rs/skills/src/assets/samples/imagegen/assets/imagegen.png` | unmapped | USE | other source - unmapped target |
| `codex-rs/skills/src/assets/samples/imagegen/references/cli.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/imagegen/references/codex-network.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/imagegen/references/image-api.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/imagegen/references/prompting.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/imagegen/references/sample-prompts.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/imagegen/scripts/image_gen.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/imagegen/scripts/remove_chroma_key.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/openai-docs/LICENSE.txt` | unmapped | USE | compliance / SCM metadata - preserve verbatim |
| `codex-rs/skills/src/assets/samples/openai-docs/SKILL.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/openai-docs/agents/openai.yaml` | unmapped | USE | yaml source - unmapped target |
| `codex-rs/skills/src/assets/samples/openai-docs/assets/openai-small.svg` | unmapped | REJECT | tiny non-code file - likely empty or marker |
| `codex-rs/skills/src/assets/samples/openai-docs/assets/openai.png` | unmapped | USE | other source - unmapped target |
| `codex-rs/skills/src/assets/samples/openai-docs/references/latest-model.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/openai-docs/references/prompting-guide.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/openai-docs/references/upgrade-guide.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/openai-docs/scripts/resolve-latest-model-info.js` | forager | USE | javascript source - forager target |
| `codex-rs/skills/src/assets/samples/plugin-creator/SKILL.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/plugin-creator/agents/openai.yaml` | unmapped | USE | yaml source - unmapped target |
| `codex-rs/skills/src/assets/samples/plugin-creator/assets/plugin-creator-small.svg` | unmapped | REJECT | tiny non-code file - likely empty or marker |
| `codex-rs/skills/src/assets/samples/plugin-creator/assets/plugin-creator.png` | unmapped | USE | other source - unmapped target |
| `codex-rs/skills/src/assets/samples/plugin-creator/references/plugin-json-spec.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/plugin-creator/scripts/create_basic_plugin.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/skill-creator/SKILL.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/skill-creator/agents/openai.yaml` | unmapped | USE | yaml source - unmapped target |
| `codex-rs/skills/src/assets/samples/skill-creator/assets/skill-creator-small.svg` | unmapped | REJECT | tiny non-code file - likely empty or marker |
| `codex-rs/skills/src/assets/samples/skill-creator/assets/skill-creator.png` | unmapped | USE | other source - unmapped target |
| `codex-rs/skills/src/assets/samples/skill-creator/license.txt` | unmapped | USE | text source - unmapped target |
| `codex-rs/skills/src/assets/samples/skill-creator/references/openai_yaml.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/skill-creator/scripts/generate_openai_yaml.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/skill-creator/scripts/init_skill.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/skill-creator/scripts/quick_validate.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/skill-installer/LICENSE.txt` | unmapped | USE | compliance / SCM metadata - preserve verbatim |
| `codex-rs/skills/src/assets/samples/skill-installer/SKILL.md` | docs | USE | documentation |
| `codex-rs/skills/src/assets/samples/skill-installer/agents/openai.yaml` | unmapped | USE | yaml source - unmapped target |
| `codex-rs/skills/src/assets/samples/skill-installer/assets/skill-installer-small.svg` | unmapped | REJECT | tiny non-code file - likely empty or marker |
| `codex-rs/skills/src/assets/samples/skill-installer/assets/skill-installer.png` | unmapped | USE | other source - unmapped target |
| `codex-rs/skills/src/assets/samples/skill-installer/scripts/github_utils.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/skill-installer/scripts/install-skill-from-github.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/assets/samples/skill-installer/scripts/list-skills.py` | forager | USE | python source - forager target |
| `codex-rs/skills/src/lib.rs` | forager | USE | rust source - forager target |
