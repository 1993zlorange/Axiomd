---
name: scienceresearch-pm-reporting
description: Generate or refresh an integrated scienceresearch project-stage HTML report that contains both management status and complete requirements-linked, step-by-step screenshot evidence, while maintaining a compatibility evidence-book extract. Use when the project manager must report status, demonstrate implemented functions as user journeys, prepare acceptance evidence, or synchronize the report with the user manual. Do not produce a link-only management report or declare formal acceptance without an approved baseline and explicit customer sign-off.
---

# ScienceResearch PM Reporting

Use [assets/output-template.html](assets/output-template.html) as the blank HTML architecture. When present, use `scienceresearch项目阶段汇报_20260830.html` as the visual and information-architecture reference, then reconcile it with current evidence. Name the authoritative report `YYYYMMDD-内容简述-项目阶段汇报.html`; name any compatibility extract with the same date-prefix convention and link it back to the authoritative report.

Create one authoritative integrated report and one compatibility extract without overstating implementation or acceptance:

- **Authoritative:** `output/YYYYMMDD-科研工作台项目阶段汇报-项目阶段汇报.html`
- **Compatibility extract:** `output/YYYYMMDD-科研工作台需求链路证据册-证据册.html`

The authoritative stage report must answer both questions in one offline-readable HTML:

1. “Where is the project, what is delivered, what remains, and what decision is needed?”
2. “For each currently operable requirement, what complete user journey was executed, what happened at every step, and where is the screenshot or lower-level evidence?”

The compatibility evidence book may mirror or extract the journey chapter for existing links and focused reading. It must point back to the integrated report and must not contain material passing evidence that is absent from the authoritative report.

## Source-of-truth order

Read the current files rather than relying on an older report:

1. `doc/科研工作台需求文档_20260828.md`
2. `doc/科研工作台架构与设计方案_20260828.md`
3. `doc/科研工作台项目架构_20260828.md`
4. `doc/科研工作台用户手册_20260828.md`
5. `README.md`, `src/`, `tests/`, `log/demand_log.md`, `log/engineer_log.md`, and `log/test_log.md`
6. the newest applicable `output/project-test/<run-id>/` reports, screenshots, API observations, database observations, traces, and exports
7. a fresh isolated browser run when existing evidence cannot prove the requested step

Treat document status labels such as `draft`, `proposed`, and `approved` as facts. A passing technical slice does not convert a draft requirement or proposed design into an approved baseline.

## Mandatory workflow

1. Establish the reporting date, repository root, document versions/statuses, latest implementation event, and latest independent QA run.
2. Build a truth ledger with four categories: `Fact`, `User/customer decision`, `Inference`, and `Unknown`. Every material status statement in the HTML must be supportable by this ledger.
3. Map stable requirement identifiers to design response, implemented route/API/module, observable user journey, acceptance result, and evidence path. Read [references/evidence-contract.md](references/evidence-contract.md) for the required evidence fields and claim rules.
4. Create or refresh the authoritative project-stage report. Preserve the visual language of the existing ScienceResearch workbench and the latest integrated report unless the user asks for a redesign. The report must contain the management chapters and the complete requirements journey evidence chapter in the same document; a link to another file does not satisfy this step. Read [references/integrated-report-standard.md](references/integrated-report-standard.md) before editing its structure.
5. Build the integrated journey chapter by real user outcome rather than by source file. For every step record the requirement IDs, user action, expected result, actual result, screenshot with source/run caption, server/API/database/test evidence when relevant, result state, and limitation. The user must be able to review the complete chain without leaving the stage report.
6. Create or refresh the compatibility evidence book as a mirror/extract of the integrated journey chapter. Add a prominent link to the integrated report's journey anchor. Do not let the compatibility file become the only location of a screenshot, result, limitation, or acceptance caveat.
7. Capture missing screenshots in a fresh isolated data directory under `output/pm-chain-<YYYYMMDD>/data/`. Use a real browser against the running application. Never modify the formal `data/` directory for a reporting demonstration.
8. Cross-link both HTML files and the user manual. Update `doc/科研工作台用户手册_20260828.md` so the integrated report journey anchor is the primary acceptance link; retain the compatibility evidence-book path, test-data warning, service-side source-of-truth rule, and current limitations.
9. Append one timestamped paragraph to `log/test_log.md` only when tests/browser checks were actually run. Append an engineering-log paragraph when repository files, agent configuration, or reusable reporting automation were changed. Preserve all existing log content.
10. Validate every local image/link, cross-file anchor, required section, document encoding, responsive layout, and browser console before handoff. Follow [references/html-quality-gate.md](references/html-quality-gate.md).

## Integrated-report invariant

The stage report is incomplete if any of these are true:

- it merely links to the evidence book instead of embedding the complete journey evidence;
- an in-scope journey step, screenshot, actual result, state evidence, failure label, or limitation appears only in the compatibility file;
- the report shows screenshots without requirement IDs and expected/actual outcomes;
- management status and functional evidence use different baseline or test-status claims;
- the user manual treats the compatibility evidence book as the only authoritative acceptance path.

The current accepted content pattern is an 11-part report: management conclusion, scope/stage, delivered capabilities, demonstration flow, quality/acceptance evidence, requirements/design/implementation alignment, risks/gaps, customer decisions, next actions, integrated requirements journey evidence, and evidence index. Adapt wording and subsection count when the baseline changes, but preserve this information architecture and keep the integrated journey chapter directly navigable.

## Screenshot and evidence rules

- One screenshot must correspond to the actual state claimed by that step. Do not duplicate a generic page screenshot and describe it as a distinct intermediate state.
- When a page-level screenshot legitimately supports multiple related steps, label later uses `supporting evidence` and add separate API/database/test evidence; never imply the duplicate image proves a distinct state transition.
- Reusing an archived screenshot is allowed only when it visibly proves the same state and the caption identifies its original QA run. Otherwise run the flow again and capture a new image.
- Historical failure screenshots must be labeled `修复前/历史缺陷` and kept separate from final passing evidence.
- A screenshot proves visible UI state only. Use API, database, exported file, trace, or log evidence for persistence, idempotency, hashes, generated files, and server-side state transitions.
- HTTP 200, element existence, or an unchanged page is not sufficient proof of a successful action.
- `MANUAL_REQUIRED` is a controlled safety fallback, not a successful automatic execution.
- `localStorage` may prove only an unsubmitted summary draft. Catalog, Context, Workflow, Item, Evidence, Gate, Recommendation, Report, governance, and operational state must be attributed to the server.

## Reporting language

Lead with the management conclusion and state its scope. Prefer wording such as:

`核心人工闭环和当前技术垂直切片已验证；正式需求/架构基线和仍标记为 MANUAL_REQUIRED 的资格事项待确认。`

Do not write `R1 全量验收完成`, `正式交付通过`, `pytest 通过`, or equivalent unless the exact evidence and approval exist. If pytest is unavailable but boundary functions were invoked directly, say exactly that.

Separate these concepts:

- implemented;
- demonstrated in a browser;
- independently tested;
- technically passed in the tested scope;
- approved by the customer;
- accepted against an approved baseline.

## Completion contract

The task is complete only when:

- the authoritative stage report contains both management status and every in-scope journey step with honest evidence;
- the compatibility evidence book exists, mirrors/extracts the same evidence, and cross-links to the integrated journey anchor;
- no material screenshot, actual result, state evidence, failure label, limitation, or baseline caveat exists only in the compatibility file;
- all referenced local files exist and image files have valid formats;
- the user manual links primarily to the integrated report journey chapter and reflects the demonstrated journeys and limitations;
- applicable logs contain a precise timestamp and concise action summary;
- desktop, intermediate, and mobile widths have been checked without whole-page horizontal overflow;
- all lazy-loaded images have been scrolled/loaded and checked for `pending=0` and `broken=0` when lazy loading is used;
- browser `ConsoleError`, `Warning`, and `PageError` results are reported;
- the final response lists the deliverable paths, covered scope, test results, unverified items, and baseline status.

If a requirement has no operable journey or lacks evidence, list it as `未实现`, `部分实现`, `MANUAL_REQUIRED`, or `未验证`; do not fabricate a screenshot or silently omit it.
