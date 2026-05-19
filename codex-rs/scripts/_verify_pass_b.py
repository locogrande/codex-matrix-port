import json
from pathlib import Path

r = json.load(open(r"C:\Users\yonat\Desktop\codex-matrix-port\codex-rs\scripts\_apply_pass_b.report.json"))
for cargo in r["cargo_files_modified"]:
    crate_root = str(Path(cargo).parent).replace("\\", "/")
    matched = [f for f in r["modified_files"] if f["path"].startswith(crate_root + "/")]
    print(f"{crate_root}: {len(matched)} modified test files (sum removed={sum(f['removed'] for f in matched)})")

# Sample one before/after by re-reading sample original via grep stats
print()
print("Top 5 by lines removed:")
for f in sorted(r["modified_files"], key=lambda x: -x["removed"])[:5]:
    print(f"  -{f['removed']:>2}  {f['path']}")
