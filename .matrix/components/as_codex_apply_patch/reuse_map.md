# Reuse Map - as_codex_apply_patch

Source: `codex-rs/apply-patch`

Expected plan hash: `51adcee6c1f9cb44049fafb982c414b979d2b2be6199c593746e283694a72d24`

| path | framework | verdict | reason |
|---|---|---|---|
| `codex-rs/apply-patch/BUILD.bazel` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/apply-patch/Cargo.toml` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `codex-rs/apply-patch/apply_patch_tool_instructions.md` | tightrope | USE | markdown source - tightrope target |
| `codex-rs/apply-patch/src/invocation.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/src/lib.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/src/main.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/src/parser.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/src/seek_sequence.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/src/standalone_executable.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/src/streaming_parser.rs` | tightrope | USE | rust source - tightrope target |
| `codex-rs/apply-patch/tests/all.rs` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/.gitattributes` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/001_add_file/expected/bar.md` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/001_add_file/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/002_multiple_operations/expected/modify.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/002_multiple_operations/expected/nested/new.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/002_multiple_operations/input/delete.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/002_multiple_operations/input/modify.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/002_multiple_operations/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/003_multiple_chunks/expected/multi.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/003_multiple_chunks/input/multi.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/003_multiple_chunks/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/004_move_to_new_directory/expected/old/other.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/004_move_to_new_directory/expected/renamed/dir/name.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/004_move_to_new_directory/input/old/name.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/004_move_to_new_directory/input/old/other.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/004_move_to_new_directory/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/005_rejects_empty_patch/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/005_rejects_empty_patch/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/005_rejects_empty_patch/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/006_rejects_missing_context/expected/modify.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/006_rejects_missing_context/input/modify.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/006_rejects_missing_context/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/007_rejects_missing_file_delete/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/007_rejects_missing_file_delete/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/007_rejects_missing_file_delete/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/008_rejects_empty_update_hunk/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/008_rejects_empty_update_hunk/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/008_rejects_empty_update_hunk/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/009_requires_existing_file_for_update/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/009_requires_existing_file_for_update/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/009_requires_existing_file_for_update/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/010_move_overwrites_existing_destination/expected/old/other.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/010_move_overwrites_existing_destination/expected/renamed/dir/name.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/010_move_overwrites_existing_destination/input/old/name.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/010_move_overwrites_existing_destination/input/old/other.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/010_move_overwrites_existing_destination/input/renamed/dir/name.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/010_move_overwrites_existing_destination/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/011_add_overwrites_existing_file/expected/duplicate.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/011_add_overwrites_existing_file/input/duplicate.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/011_add_overwrites_existing_file/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/012_delete_directory_fails/expected/dir/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/012_delete_directory_fails/input/dir/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/012_delete_directory_fails/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/013_rejects_invalid_hunk_header/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/013_rejects_invalid_hunk_header/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/013_rejects_invalid_hunk_header/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/014_update_file_appends_trailing_newline/expected/no_newline.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/014_update_file_appends_trailing_newline/input/no_newline.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/014_update_file_appends_trailing_newline/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/015_failure_after_partial_success_leaves_changes/expected/created.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/015_failure_after_partial_success_leaves_changes/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/016_pure_addition_update_chunk/expected/input.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/016_pure_addition_update_chunk/input/input.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/016_pure_addition_update_chunk/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/017_whitespace_padded_hunk_header/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/017_whitespace_padded_hunk_header/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/017_whitespace_padded_hunk_header/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/018_whitespace_padded_patch_markers/expected/file.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/018_whitespace_padded_patch_markers/input/file.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/018_whitespace_padded_patch_markers/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/019_unicode_simple/expected/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/019_unicode_simple/input/foo.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/019_unicode_simple/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_delete_file_success/expected/keep.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_delete_file_success/input/keep.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_delete_file_success/input/obsolete.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_delete_file_success/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_whitespace_padded_patch_marker_lines/expected/file.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_whitespace_padded_patch_marker_lines/input/file.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/020_whitespace_padded_patch_marker_lines/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/021_update_file_deletion_only/expected/lines.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/021_update_file_deletion_only/input/lines.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/021_update_file_deletion_only/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/022_update_file_end_of_file_marker/expected/tail.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/022_update_file_end_of_file_marker/input/tail.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/022_update_file_end_of_file_marker/patch.txt` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/fixtures/scenarios/README.md` | readme | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/suite/cli.rs` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/suite/mod.rs` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/suite/scenarios.rs` | tightrope | USE | test file - preserve for Tester framework integration |
| `codex-rs/apply-patch/tests/suite/tool.rs` | tightrope | USE | test file - preserve for Tester framework integration |
