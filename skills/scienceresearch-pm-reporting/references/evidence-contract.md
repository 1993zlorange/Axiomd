# Evidence Contract

Use this reference when building the requirement-to-journey matrix and deciding whether a claim is supportable.

## Required row fields

Each meaningful function or journey must identify:

| Field | Required content |
|---|---|
| Primary location | The integrated stage-report journey anchor/card containing this evidence; the compatibility book may mirror it |
| Requirement | Stable SRS/quality/operations IDs, or an explicit `design-only` label |
| User outcome | The decision or work the user can complete |
| Preconditions | Required Context, Week, Item, file, approval, or environment state |
| Action | The exact visible click, form submission, or documented API/CLI step |
| Expected result | Visible feedback plus required server-side change |
| Actual result | What the current run or archived run actually observed |
| UI evidence | Screenshot path and original run ID/date |
| State evidence | API response, database observation, log event, exported artifact, trace, or hash |
| Result | `PASS`, `FAIL`, `PARTIAL`, `MANUAL_REQUIRED`, or `NOT_TESTED` |
| Limitation | Missing baseline, untested branch, future scope, or known constraint |

## Evidence strength

Use the strongest available combination:

1. visible user action and result in a real browser;
2. server/API or persisted-state observation;
3. generated artifact/hash when output files are claimed;
4. automated test result for repeatability;
5. requirement/design trace for scope correctness.

No single evidence type proves every layer. For example, a success banner does not prove persistence, and a database row does not prove that the button works for a user.

Every evidence row must be present in the authoritative integrated stage report. A row that exists only in the compatibility evidence book does not satisfy the reporting contract.

## Function grouping for ScienceResearch

Unless the current SRS changes, start with these outcome groups and adjust from evidence:

1. main workbench and work-package discovery;
2. Context and 68 Workflow lifecycle;
3. weekly plan and work-item constraints;
4. execution and Evidence lifecycle;
5. six completion gates and Recommendation decisions;
6. ReportModel, author confirmation, outcome card, and PPTX;
7. Skill registration, manual guidance, approvals, and safety fallback;
8. governance candidates, project-log projection, health, import, and backup;
9. accessibility, keyboard operation, responsive behavior, offline behavior, and error feedback.

## Archived evidence

Archived evidence may be reused only when all of these match:

- the relevant code has not changed in a way that invalidates the observation;
- the screenshot visibly contains the claimed result;
- the run used isolated data or otherwise did not contaminate formal data;
- the original run/report is identifiable;
- any historical failure has a later explicit closure result.

If one condition is unknown, label the evidence `archived/supporting` and capture a fresh screenshot for final acceptance.

When the same page screenshot supports more than one related step, only the state it visibly contains may be marked as UI evidence. Other steps must call it `page-level supporting evidence` and cite the API, database, automated test, trace, export, or later QA observation that proves the distinct result.
