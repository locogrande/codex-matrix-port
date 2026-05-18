"""Adapter for as_codex_agent_identity — exposes the ported codex-rs/agent-identity crate."""
from __future__ import annotations

import json
from pathlib import Path

ASSET_ID = "as_codex_agent_identity"
COMPONENT_ID = "agent_identity"
VERSION_ID = "v0001_initial"
PRIMARY_FRAMEWORK = "build_config"
ORIGIN = "codex-rs/agent-identity"

_HERE = Path(__file__).resolve()
_MATRIX_ROOT = next((p for p in _HERE.parents if (p / "MATRIX.md").is_file()), _HERE.parents[2])
_ASSET_ROOT = _MATRIX_ROOT / "library/source_assets/components/agent_identity/versions" / VERSION_ID
SOURCE_ROOT = _ASSET_ROOT / "source"
MANIFEST_REF = _ASSET_ROOT / "manifest.json"
SOURCE_MAP_REF = _ASSET_ROOT / "source_map.json"


def asset_info() -> dict:
    return {"asset_id": ASSET_ID, "component_id": COMPONENT_ID, "version_id": VERSION_ID,
            "primary_framework": PRIMARY_FRAMEWORK, "origin": ORIGIN,
            "source_root": str(SOURCE_ROOT), "manifest_ref": str(MANIFEST_REF),
            "source_map_ref": str(SOURCE_MAP_REF)}


def load_source_map() -> dict:
    return json.loads(SOURCE_MAP_REF.read_text(encoding="utf-8"))


def source_files() -> list[Path]:
    return [SOURCE_ROOT / m["path"] for m in load_source_map().get("mappings", [])]


__all__ = ["ASSET_ID", "COMPONENT_ID", "VERSION_ID", "PRIMARY_FRAMEWORK", "ORIGIN",
           "SOURCE_ROOT", "MANIFEST_REF", "SOURCE_MAP_REF",
           "asset_info", "load_source_map", "source_files"]
