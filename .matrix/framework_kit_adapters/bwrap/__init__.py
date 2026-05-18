"""Adapter surface for as_codex_bwrap (codex-rs/bwrap)."""
from pathlib import Path

ASSET_ID = "as_codex_bwrap"
SOURCE_PATH_PREFIX = "library/source_assets/components/as_codex_bwrap/versions/v0001_initial/source"
SOURCE_FILES = [
    "BUILD.bazel",
    "Cargo.toml",
    "build.rs",
    "config.h",
    "src/main.rs",
]


def source_root(matrix_root: Path | str) -> Path:
    return Path(matrix_root) / SOURCE_PATH_PREFIX


def source_paths(matrix_root: Path | str) -> list[Path]:
    return [source_root(matrix_root) / p for p in SOURCE_FILES]


def adapter_probe() -> bool:  # forager_test_target entrypoint
    root = Path(__file__).resolve().parents[3]
    return all((root / SOURCE_PATH_PREFIX / p).is_file() for p in SOURCE_FILES)
