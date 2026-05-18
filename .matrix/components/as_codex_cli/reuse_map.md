# Reuse Map - as_codex_cli

Source: `codex-cli`

Expected plan hash: `7284aa9ef1c33a402cf8c583e77963132fb92c572be50267dd8095625e93642a`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-cli/.gitignore` | tightrope | USE | compliance / SCM metadata - preserve verbatim |
| `codex-cli/bin/codex.js` | tightrope | USE | javascript source - tightrope target |
| `codex-cli/bin/rg` | tightrope | USE | other source - tightrope target |
| `codex-cli/package.json` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-cli/scripts/README.md` | readme | USE | documentation - preserve as docs asset |
| `codex-cli/scripts/build_npm_package.py` | tightrope | USE | python source - tightrope target |
| `codex-cli/scripts/init_firewall.sh` | tightrope | USE | shell source - tightrope target |
| `codex-cli/scripts/install_native_deps.py` | tightrope | USE | python source - tightrope target |
| `codex-cli/scripts/run_in_container.sh` | tightrope | USE | shell source - tightrope target |
