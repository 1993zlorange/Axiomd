# Coverage model

Build the inventory from requirements, user-visible implementation, and claims intended for sign-off. Every item must have an expected result, actual result, evidence, and final status.

## Required coverage groups

### Pages and navigation

- `/`
- `/work-packages` and at least one detail page
- `/contexts` and a created context detail page
- `/weeks` and a created week detail page
- `/reports`
- `/skills`
- `/governance`
- `/operations`

Check active navigation, browser history, direct deep links, missing IDs, UTF-8 text, and reload behavior.

### Main workbench controls

- aspect filtering and text search;
- all 68 work-package cards remain addressable;
- work-package detail switching and ordinary-link fallback;
- five-field weekly summary generation;
- copy success and manual-copy fallback;
- draft persistence without business-state pollution;
- formal-report navigation.

### Forms and state-changing controls

- create Context and instantiate 68 workflows;
- start a Workflow and reject stale/invalid transitions;
- create Week and enforce the two-item limit;
- add and execute a work item;
- register, confirm, expire, and revalidate Evidence;
- set completion gates and reject premature completion;
- generate and decide Recommendation candidates;
- create and strictly bind Manual Skill artifacts and steps;
- confirm reports and export Card/PPTX from the frozen snapshot;
- submit demand/engineering events, rebuild projections, and preserve human text;
- run health, backup, restore, and path-boundary checks.

### API response contract

For every exercised endpoint verify:

- documented method and route;
- success and failure status;
- `Content-Type`;
- JSON keys or redirect target;
- stable error `code` and readable detail;
- idempotency or version-conflict behavior where required;
- no mutation after a rejected request.

### Interaction and visual states

Test at representative widths near 1440 px, 900 px, and 390 px. Check initial view, densest reachable view, post-click detail state, long text, empty result, validation error, focus visibility, keyboard order, horizontal overflow, clipping, and controls hidden behind internal scroll containers.

### Exploratory cases

Always add at least two run-specific exploratory cases. Favor double submit, reload after mutation, malformed JSON, missing file, malicious HTML text, stale row version, conflicting log edit, replaced report image, or disabled JavaScript.

## Inventory row

Use these fields:

`ID | Requirement | Page/API | Control/Action | Prerequisite | Expected | Actual | HTTP/Console | Persisted State | Evidence | Status | Severity`

Allowed statuses: `Passed`, `Failed`, `Blocked`, `NotApplicable`.
