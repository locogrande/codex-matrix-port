# Reuse Map - as_codex_sdk_typescript

Source: `sdk/typescript`

Expected plan hash: `4f87fbbca91d16f3530123c189d2d5acf4209108a54d50f582b2612bc00abf08`

| path | framework | verdict | reason |
|---|---|---|---|
| `sdk/typescript/.prettierignore` | framework_kit_adapter | REJECT | tiny non-code file - likely empty or marker |
| `sdk/typescript/.prettierrc` | framework_kit_adapter | USE | other source - framework_kit_adapter target |
| `sdk/typescript/README.md` | readme | USE | documentation - preserve as docs asset |
| `sdk/typescript/eslint.config.js` | framework_kit_adapter | USE | javascript source - framework_kit_adapter target |
| `sdk/typescript/jest.config.cjs` | framework_kit_adapter | USE | javascript source - framework_kit_adapter target |
| `sdk/typescript/package.json` | build_config | REFACTOR | build config - adapt for Matrix import structure |
| `sdk/typescript/samples/basic_streaming.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/samples/helpers.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/samples/structured_output.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/samples/structured_output_zod.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/codex.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/codexOptions.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/events.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/exec.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/index.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/items.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/outputSchemaFile.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/thread.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/threadOptions.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/src/turnOptions.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
| `sdk/typescript/tests/abort.test.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/codexExecSpy.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/exec.test.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/responsesProxy.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/run.test.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/runStreamed.test.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/setupCodexHome.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tests/testCodex.ts` | framework_kit_adapter | USE | test file - preserve for Tester framework integration |
| `sdk/typescript/tsconfig.json` | framework_kit_adapter | USE | json source - framework_kit_adapter target |
| `sdk/typescript/tsup.config.ts` | framework_kit_adapter | USE | typescript source - framework_kit_adapter target |
