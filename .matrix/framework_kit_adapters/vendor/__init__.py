from __future__ import annotations
import hashlib, json
from pathlib import Path

ASSET_ID = 'as_codex_vendor'
COMPONENT_ID = ASSET_ID
ACCEPTED_VERSION = 'v0001_initial'
EXPECTED_PLAN_HASH = '63c52e1584f1339742579a8e869af9f4d0f1cc22ccf4a4139ef7c45d6cc0d896'
EXPECTED_COUNT = 51
_ROOT = Path(__file__).resolve().parents[3]
_VERSION_ROOT = _ROOT / "library/source_assets/components" / ASSET_ID / "versions" / ACCEPTED_VERSION
ENGINE_ROOT = _VERSION_ROOT / "source"
MANIFEST_PATH = _VERSION_ROOT / "manifest.json"
SOURCE_MAP_PATH = _VERSION_ROOT / "source_map.json"
SOURCE_FILES = ('BUILD.bazel', 'bubblewrap/.dir-locals.el', 'bubblewrap/.editorconfig', 'bubblewrap/.github/workflows/check.yml', 'bubblewrap/CODE-OF-CONDUCT.md', 'bubblewrap/COPYING', 'bubblewrap/LICENSE', 'bubblewrap/NEWS.md', 'bubblewrap/README.md', 'bubblewrap/SECURITY.md', 'bubblewrap/bind-mount.c', 'bubblewrap/bind-mount.h', 'bubblewrap/bubblewrap.c', 'bubblewrap/bubblewrap.jpg', 'bubblewrap/bwrap.xml', 'bubblewrap/ci/builddeps.sh', 'bubblewrap/ci/enable-userns.sh', 'bubblewrap/completions/bash/bwrap', 'bubblewrap/completions/bash/meson.build', 'bubblewrap/completions/meson.build', 'bubblewrap/completions/zsh/_bwrap', 'bubblewrap/completions/zsh/meson.build', 'bubblewrap/demos/bubblewrap-shell.sh', 'bubblewrap/demos/flatpak-run.sh', 'bubblewrap/demos/flatpak.bpf', 'bubblewrap/demos/userns-block-fd.py', 'bubblewrap/meson.build', 'bubblewrap/meson_options.txt', 'bubblewrap/network.c', 'bubblewrap/network.h', 'bubblewrap/packaging/bubblewrap.spec', 'bubblewrap/release-checklist.md', 'bubblewrap/tests/libtest-core.sh', 'bubblewrap/tests/libtest.sh', 'bubblewrap/tests/meson.build', 'bubblewrap/tests/test-run.sh', 'bubblewrap/tests/test-seccomp.py', 'bubblewrap/tests/test-specifying-pidns.sh', 'bubblewrap/tests/test-specifying-userns.sh', 'bubblewrap/tests/test-utils.c', 'bubblewrap/tests/try-syscall.c', 'bubblewrap/tests/use-as-subproject/.gitignore', 'bubblewrap/tests/use-as-subproject/README', 'bubblewrap/tests/use-as-subproject/assert-correct-rpath.py', 'bubblewrap/tests/use-as-subproject/config.h', 'bubblewrap/tests/use-as-subproject/dummy-config.h.in', 'bubblewrap/tests/use-as-subproject/meson.build', 'bubblewrap/uncrustify.cfg', 'bubblewrap/uncrustify.sh', 'bubblewrap/utils.c', 'bubblewrap/utils.h')

def _load(path: Path) -> dict: return json.loads(path.read_text(encoding="utf-8"))
def manifest() -> dict: return _load(MANIFEST_PATH)
def source_map() -> dict: return _load(SOURCE_MAP_PATH)
def source_paths() -> list[Path]: return [ENGINE_ROOT / p for p in SOURCE_FILES]
def gate_probe() -> bool:
    rows = source_map().get("mappings", []) if SOURCE_MAP_PATH.is_file() else []
    return ENGINE_ROOT.is_dir() and manifest().get("status") == "accepted" and manifest().get("expected_plan_hash") == EXPECTED_PLAN_HASH and len(rows) == EXPECTED_COUNT and all((p := ENGINE_ROOT / r["target_relpath"]).is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == (r.get("sha256_full") or r.get("sha256")) for r in rows)
__all__ = ["ACCEPTED_VERSION", "ASSET_ID", "COMPONENT_ID", "ENGINE_ROOT", "EXPECTED_PLAN_HASH", "MANIFEST_PATH", "SOURCE_FILES", "SOURCE_MAP_PATH", "gate_probe", "manifest", "source_map", "source_paths"]
