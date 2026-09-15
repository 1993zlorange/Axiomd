---
name: scienceresearch-functional-qa
description: Independently test the scienceresearch workbench end to end when asked to verify every function, find buttons or forms that do nothing, validate API and visible responses, run release regression, or produce an evidence-backed defect report. Do not use this skill to implement fixes unless the user separately authorizes changes.
---

# Scienceresearch Functional QA

Test the running application as a user and as an API client. A passing unit test or HTTP 200 alone is not proof that a control works: verify the visible result, persisted state, response contract, and failure behavior that the requirements promise.

## Required inputs

Before testing, read the current versions of:

- `doc/科研工作台需求文档_20260828.md`
- `doc/科研工作台架构与设计方案_20260828.md`
- `doc/科研工作台项目架构_20260828.md`
- `doc/科研工作台用户手册_20260828.md`
- `src/scienceresearch/web.py`
- `src/scienceresearch/core.py`
- `tests/`

Use these sources to build the coverage inventory. Do not infer success criteria only from the current implementation.

## Test isolation

- Use a fresh temporary data directory and a non-conflicting localhost port. Do not test writes against the project's normal `data/` directory.
- Keep the server in a persistent terminal session and stop it after evidence is collected.
- Store browser screenshots, traces, response captures, and reports under `output/project-test/<run-id>/`. Do not write generated evidence into `doc/`, `idea/`, or production logs.
- Do not call external services or enable online Skill execution. Confirm that offline and `ManualRequired` behavior is explicit where designed.

## Browser and API workflow

Use the installed `$playwright` skill for real-browser navigation, snapshots, clicks, keyboard input, screenshots, console errors, and network observations. On Windows, use `npx.cmd` when PowerShell execution policy blocks `npx.ps1`.

1. Run `compileall`, the complete `unittest` suite, and the three architecture-boundary functions.
2. Start the application against isolated data.
3. Read [references/coverage-model.md](references/coverage-model.md) and create a run-specific inventory of pages, links, buttons, forms, JavaScript controls, API routes, state transitions, and failure paths.
4. Exercise every inventory item with normal user input. For stateful controls, verify the initial state, changed state, persisted state after reload, and any allowed return transition.
5. Exercise invalid, missing-prerequisite, duplicate, and stale-version paths where applicable. Verify stable error codes and that rejected actions do not silently mutate state.
6. Run desktop, medium, and narrow viewport passes. Check keyboard focus, overflow, disabled/no-JavaScript fallbacks, console errors, failed requests, and accidental external requests.
7. Reconcile browser observations with API responses and persisted state. If they disagree, report a defect even when one layer appears successful.
8. Produce the report using [references/report-template.md](references/report-template.md) and the blank output architecture in [assets/output-template.md](assets/output-template.md).

Name the report `YYYYMMDD-内容简述-功能测试报告.md` using the production date. Preserve the run ID, isolated evidence paths, baseline, verdict, and unverified items in the document.

## Detecting a no-response control

For every visible button, submit control, card, or link, record all of the following before and after interaction:

- URL and navigation outcome;
- visible DOM or state change;
- request method, path, status, content type, and response body shape;
- browser console and page errors;
- whether the control remains enabled or shows feedback;
- relevant server-side state after reload or API query.

Classify a control as `NO_RESPONSE` when a normal user action produces no documented navigation, visible feedback, request, state transition, or accessible explanation. Classify it as `WRONG_RESPONSE` when an action occurs but the status, body, redirect, visible result, persisted state, or error code does not match the requirement.

## Sign-off rules

- Never mark a function Passed solely because its route returns 200, its element exists, or a source-code string is present.
- Every Passed item needs an observable assertion and evidence reference.
- A blocked dependency must be `Blocked`, not Passed or Failed.
- Do not repair defects during an independent test run. Report the smallest reproducible case, likely layer, and suggested verification after a fix.
- Final verdict is `PASS` only when all Must inventory items pass and there are no Critical or High defects. Otherwise return `FAIL`; use `BLOCKED` only when the environment prevents a meaningful test after reasonable diagnostics.
