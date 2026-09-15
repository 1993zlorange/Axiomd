# Evidence-Linked Documentation Suite Guide

Use this guide when producing or revising a coordinated PRD, SRS, SDD, feature overview, user manual, UAT plan, status report, or evidence set. The objective is one coherent baseline in which readers can move from user intent to implementation responsibility and actual proof without confusing proposal, implementation, observation, qualification, or acceptance.

## Internalized writing structure

This guide already incorporates the reusable structure of the approved Chinese requirements, architecture/design, and user-manual documents. Do not seek or require access to external exemplar files during ordinary use. Read an external reference only when the user explicitly requests a source comparison or supplies a newer governing standard.

Apply these internalized patterns directly:

- requirements documents use visible document control, approval and change records, stable requirement vocabulary, module/submodule completeness, open decisions, qualification, and downstream impact;
- architecture/design documents use evidence labels, requirement-to-design mappings, module ownership, concrete API/data/error design, migration, rollback, ADRs, and review gates;
- user manuals state the current version and implementation status, organize content by workflow, place actual screenshots beside the operations they prove, connect captions to requirements/qualification, and disclose gaps honestly.

These are format and governance rules, not a portable product specification. Never copy another project's business requirements, module counts, database choices, UI styling, versions, approval claims, evidence paths, or test results. The target project's instructions, approved requirements, repository architecture, and actual runtime evidence are authoritative.

## Document roles

Keep the documents distinct and linked:

| Artifact | Primary question | Must not become |
| --- | --- | --- |
| PRD | Why does the product exist, for whom, and what outcomes are in scope? | A module/API design or an implementation status claim. |
| SRS | What observable behavior, data, interfaces, constraints, failures, and qualification are required? | A technology proposal presented as an approved requirement. |
| SDD / architecture | How do approved requirements map to boundaries, modules, state, interfaces, deployment, recovery, and verification? | A source of invented product scope. |
| Feature overview | What are the major user-visible functions and where are they specified and operated? | A second inconsistent requirements baseline. |
| User manual | How does a user perform and recover a currently supported workflow? | A wishlist, test plan without results, or marketing claim. |
| UAT/evidence | What was executed, in which environment, with what expected and actual result? | A screenshot gallery detached from requirements and steps. |

## Baseline and document control

Every governed document should identify, when applicable:

- title, stable document ID, version, status, date and encoding;
- governing upstream baseline and related downstream documents;
- decision owner and approval record without invented sign-off;
- change history stating affected requirement, design, manual, test, migration, and release IDs;
- current scope, non-goals, assumptions, dependencies, risks, and open decisions;
- evidence date/environment and the difference between current facts and target behavior.

When revising one document, check all affected documents before changing status. An editorial reorganization must not silently create a new requirement. A requirement change must identify downstream SRS/SDD/manual/UAT/release impacts before the suite is called aligned.

## Stable vocabulary and bidirectional traceability

Use stable identifiers whose namespaces preserve meaning:

- product and software requirements: `PRD-*`, `UC-*`, `FR-*`, `DATA-*`, `INT-*`, `NFR-*`, `OPS-*`, `CON-*`, `QUAL-*`;
- architecture and design: `MOD-*`, `SM-*`, `API-*`, `FLOW-*`, `DATA-DES-*`, `ERR-*`, `CFG-*`, `DEP-*`, `ADR-*`;
- feature navigation: `F-*` or an established project-specific equivalent;
- manual and acceptance: chapter/step identifiers, `UAT-*`, screenshot/evidence identifiers.

Never use a design ID to create a new normative requirement. Do not renumber or reinterpret a referenced ID merely because the document structure changes.

Maintain both directions:

```text
user outcome -> PRD -> SRS requirement -> module/submodule -> API/data/flow/error
             -> user-manual chapter/step -> UAT/QUAL -> retained evidence/status
```

and:

```text
evidence -> executed step -> UAT/QUAL -> requirement -> feature/user outcome
```

For a multi-document baseline, provide a feature overview or equivalent matrix. For each major feature state:

- user purpose and actor;
- trigger/prerequisites;
- main actions and visible result;
- persisted data or external effect;
- failure/recovery boundary;
- manual chapter and step;
- PRD/SRS IDs and owning design module/API;
- qualification and current evidence status.

## Status semantics

Use explicit, non-overlapping status language:

| Status | Meaning |
| --- | --- |
| Proposed / draft | Written as a candidate; not approved and not evidence of implementation. |
| Approved / confirmed | The authorized decision owner approved the named scope or delta only. |
| Implemented / code observed | Repository evidence exists; runtime behavior may still be unverified. |
| Automated test passed | Named tests passed in a recorded environment; does not prove visual behavior or external production integration. |
| Browser observed | A real browser exercised the stated visible path; it proves only what was performed and visible. |
| UAT passed | The full acceptance step met its stated threshold with retained evidence. |
| Formally accepted | The named customer/owner explicitly signed off the defined baseline. |
| Partial / blocked / not run | Some assertions or prerequisites are missing; the item is not passed. |

Do not collapse these into a generic “verified” or “done”. Historical screenshots, source inspection, mockups, API tests, browser evidence, and formal acceptance must remain distinguishable.

## User manual workflow standard

Organize the manual around user journeys rather than implementation packages. Typical chapters are document/status guidance, concepts and boundaries, installation/startup, navigation, project/work item setup, configuration, primary workflow, files/results, permissions/extensions, compute/external work, CLI/API, requirement status, troubleshooting, backup/recovery, UAT, and evidence limitations. Adapt this shape to the product; do not add empty chapters.

For each actionable workflow include:

1. Preconditions, authorization, environment, test data, and cost/data sensitivity.
2. Numbered user actions using current visible labels, commands, routes, or API operations.
3. Expected visible result and authoritative state/ID.
4. Persistence, file ownership, external effect, and whether closing the UI changes anything.
5. Failure diagnosis, retry rules, rollback or recovery, and situations where retry would duplicate work.
6. Requirement/UAT trace and current evidence status.

Do not state that a feature is usable merely because its menu exists. A configuration page does not prove connection success; an empty Results view does not prove save/restore; a running spinner or non-empty log does not prove task completion.

## Screenshot and runtime evidence

When the user requests actual screenshots, first install and run the real product in an isolated, disposable data root when this is authorized and supported. Use a real browser automation workflow where appropriate. Preserve production/formal user data and never weaken security controls solely to obtain a screenshot.

For every executed key step:

- capture the state immediately before or after the action that demonstrates the assertion;
- place the image beside that workflow, not in a detached screenshot chapter;
- use a stable evidence directory outside formal business data;
- immediately follow the image with a visible caption such as `Figure` or `图例`;
- state action, expected result, actual visible result, date, platform/browser/viewport when relevant, isolated data scenario, requirement/UAT/QUAL IDs, and whether sensitive information was redacted;
- retain failure-state screenshots and label them as failures;
- do not reuse one generic screenshot as proof of multiple distinct outcomes;
- validate that the referenced file exists, is a genuine nonblank image, and matches the caption.

If a step requires credentials, money, publishing, destructive mutation, remote compute, third-party messaging, sensitive data, or authority not granted by the user, do not execute it for documentation completeness. Mark it `not run` or `blocked`, explain why, and specify the account/fixture, action, expected assertion, logs, IDs, screenshots, and approver needed to close it.

## Validation and handoff

Before handoff:

- validate metadata, headings, tables, relative links, screenshot paths and immediate captions;
- verify every referenced requirement/design/evidence ID resolves to its owner document;
- compare feature-to-manual mappings in both directions and list orphan features or undocumented manual claims;
- run applicable documentation checks without rewriting unrelated generated material unless requested;
- report pre-existing or unrelated failures separately from defects introduced by the documentation change;
- summarize files changed, baseline/status, evidence added, unexecuted items, open decisions, and the next authorized qualification action.
