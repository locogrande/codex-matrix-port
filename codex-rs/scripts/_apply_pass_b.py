"""Layer-6 refactor pass B: replace duplicate test-time `use` lines with
`use codex_test_support::prelude::*;`.

Touches ONLY files under */tests/* directories. Skips files where the
prelude would save fewer than 3 lines (the minimum-impact threshold).

Stats are written to scripts/_apply_pass_b.report.json.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Tuple

ROOT = Path(r"C:\Users\yonat\Desktop\codex-matrix-port\codex-rs")

# Exact `use ...;` lines that the prelude re-exports. Whitespace-stripped.
PRELUDE_LINES = {
    "use pretty_assertions::assert_eq;",
    "use pretty_assertions::assert_ne;",
    "use std::path::Path;",
    "use std::path::PathBuf;",
    "use std::sync::Arc;",
    "use std::collections::HashMap;",
    "use std::time::Duration;",
    "use anyhow::Context;",
    "use anyhow::Result;",
    "use anyhow::anyhow;",
    "use anyhow::bail;",
    "use tempfile::NamedTempFile;",
    "use tempfile::TempDir;",
    "use tempfile::tempdir;",
}

PRELUDE_IMPORT = "use codex_test_support::prelude::*;"

# Minimum lines that must match for a file to be worth modifying.
MIN_HITS = 3


def process_file(path: Path) -> Tuple[int, int, bool]:
    """Return (lines_removed, lines_added, modified)."""
    original = path.read_text(encoding="utf-8")
    # Skip if the file already imports the prelude.
    if PRELUDE_IMPORT in original:
        return (0, 0, False)
    lines = original.splitlines(keepends=False)

    matching_indices = []
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped in PRELUDE_LINES:
            matching_indices.append(i)

    if len(matching_indices) < MIN_HITS:
        return (0, 0, False)

    # Drop the matching lines and insert prelude at first match position.
    first_match = matching_indices[0]
    matching_set = set(matching_indices)
    new_lines = []
    inserted = False
    for i, raw in enumerate(lines):
        if i in matching_set:
            if not inserted:
                # Preserve leading whitespace of the line we're replacing.
                indent = raw[: len(raw) - len(raw.lstrip())]
                new_lines.append(f"{indent}{PRELUDE_IMPORT}")
                inserted = True
            # else: drop the duplicate use line
        else:
            new_lines.append(raw)

    # Preserve trailing newline if original had one.
    trailing_nl = original.endswith("\n")
    new_text = "\n".join(new_lines) + ("\n" if trailing_nl else "")
    path.write_text(new_text, encoding="utf-8")

    removed = len(matching_indices)
    added = 1  # one new prelude line
    return (removed, added, True)


def find_owner_crate(test_file: Path) -> Path | None:
    """Walk upward until we find a Cargo.toml/Cargo.toml file (the codex-matrix
    layout wraps top-level files in folders of the same name). For member
    crates the layout is normal: <crate>/Cargo.toml as a real file.
    """
    cur = test_file.parent
    while cur != cur.parent and ROOT in cur.parents or cur == ROOT:
        candidate = cur / "Cargo.toml"
        if candidate.is_file():
            return candidate
        # codex-rs/Cargo.toml is a directory in this port; never the owner of
        # a tests/ file deep inside a member crate, so skip.
        cur = cur.parent
        if cur == ROOT:
            break
    return None


def ensure_dev_dep(cargo_toml: Path) -> bool:
    """Add codex-test-support to [dev-dependencies] if missing.
    Returns True if file modified.
    """
    text = cargo_toml.read_text(encoding="utf-8")
    if "codex-test-support" in text:
        return False
    line = 'codex-test-support = { workspace = true }\n'
    if "[dev-dependencies]" in text:
        # Insert right after the [dev-dependencies] header.
        new_text = re.sub(
            r"(\[dev-dependencies\]\s*\n)",
            r"\1" + line,
            text,
            count=1,
        )
    else:
        # Append a new [dev-dependencies] section.
        if not text.endswith("\n"):
            text = text + "\n"
        new_text = text + "\n[dev-dependencies]\n" + line
    cargo_toml.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    test_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # skip the codex-test-support crate itself
        if "codex-test-support" in dirpath.replace("\\", "/").split("/"):
            continue
        parts = Path(dirpath).parts
        if "tests" not in parts:
            continue
        for fn in filenames:
            if fn.endswith(".rs"):
                test_files.append(Path(dirpath) / fn)

    stats = {
        "files_scanned": len(test_files),
        "files_modified": 0,
        "use_lines_removed": 0,
        "prelude_lines_added": 0,
        "cargo_files_modified": [],
        "modified_files": [],
    }

    owner_crates = set()
    for tf in test_files:
        try:
            removed, added, modified = process_file(tf)
        except Exception as e:
            print(f"ERR {tf}: {e}", file=sys.stderr)
            continue
        if modified:
            stats["files_modified"] += 1
            stats["use_lines_removed"] += removed
            stats["prelude_lines_added"] += added
            stats["modified_files"].append(
                {
                    "path": str(tf).replace("\\", "/"),
                    "removed": removed,
                    "added": added,
                }
            )
            owner = find_owner_crate(tf)
            if owner:
                owner_crates.add(owner)

    for cargo in sorted(owner_crates):
        if ensure_dev_dep(cargo):
            stats["cargo_files_modified"].append(
                str(cargo).replace("\\", "/")
            )

    stats["net_loc_delta"] = stats["prelude_lines_added"] - stats["use_lines_removed"]
    report_path = ROOT / "scripts" / "_apply_pass_b.report.json"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in stats.items() if k != "modified_files"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
