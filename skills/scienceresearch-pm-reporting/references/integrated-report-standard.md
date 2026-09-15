# Integrated project-stage report standard

Use this reference whenever creating or refreshing `output/YYYYMMDD-科研工作台项目阶段汇报-项目阶段汇报.html`.

## Authority model

The project-stage report is the authoritative acceptance-reading surface. It must be usable offline as one HTML file plus relative evidence assets. The separate requirements journey evidence book is a compatibility extract for focused reading and historical links; it is never the only source of detailed evidence.

## Required information architecture

Keep the current ScienceResearch visual language and use this content order unless a changed baseline requires a clearly documented variation:

1. **Management conclusion** — lead with the scoped conclusion and distinguish technical validation from customer acceptance.
2. **Scope and stage** — show current/relevant release slices and what is deferred.
3. **Delivered capabilities** — list only capabilities supported by current implementation evidence.
4. **Main demonstration flow** — summarize the end-to-end research workflow before detailed evidence.
5. **Quality and acceptance evidence** — compilation/tests, independent QA, browser, responsive, artifact, and data-isolation evidence.
6. **Requirements/design/implementation alignment** — stable requirement/design IDs to implementation and result.
7. **Risks and open gaps** — include baseline, qualification, safety, operations, or evidence risks.
8. **Customer decisions** — identify the decision, impact, recommendation, and owner.
9. **Next actions** — order work by dependency; do not promise dates without authority.
10. **Integrated requirements journey evidence** — the complete evidence-book content inside the report.
11. **Evidence index** — source documents, QA runs, browser evidence, logs, exports, and compatibility links.

The sidebar/table of contents must link directly to the integrated journey chapter. The hero's primary evidence action should also lead to that chapter, not to the compatibility file.

## Integrated journey chapter

Group by user outcome. Unless the SRS changes, begin with:

1. workbench and work-package discovery;
2. Context and Workflow lifecycle;
3. weekly planning, execution, and Evidence;
4. six completion gates and Recommendation decisions;
5. ReportModel, author confirmation, outcome card, and PPTX;
6. Skill registration, manual guidance, and safety fallback;
7. governance, logs, health, and backup;
8. usability, accessibility, responsive behavior, and report reading.

Every step must display, in the report itself:

- stable requirement/quality/operations IDs;
- user action and prerequisites when not obvious;
- expected visible and server-side result;
- actual observed result;
- screenshot with figure number, state, run/date source, and historical/supporting limitation when applicable;
- state evidence such as API/database/test/export/hash/trace;
- `PASS`, `FAIL`, `PARTIAL`, `MANUAL_REQUIRED`, `NOT_TESTED`, or an equally explicit status;
- remaining limitation or baseline caveat.

A screenshot of an unchanged page cannot prove a mutation. A repeated page screenshot can support navigation or control location only; label it `supporting evidence` and cite the stronger state evidence. Historical failure screenshots must say `修复前/历史缺陷` in visible text and must identify later closure evidence.

## Compatibility evidence book

`output/YYYYMMDD-科研工作台需求链路证据册-证据册.html` must:

- state prominently that its content is integrated into the stage report;
- link to `YYYYMMDD-科研工作台项目阶段汇报-项目阶段汇报.html#journeys` or the current stable journey anchor;
- mirror or extract the same journeys without stronger claims;
- retain old paths when needed for one compatibility cycle;
- never become the only home of final screenshots, state evidence, limitations, or acceptance language.

## User manual synchronization

The user manual must link primarily to the integrated report journey anchor and may also link to the compatibility evidence book. Replace stale report screenshots after material report-layout changes. Every manual image must retain its visible chapter-scoped legend.

## Browser acceptance

Check at least 1440×900, 900×900, and 390×844. At every viewport verify whole-page width, sidebar/mobile navigation, journey cards, captions, tables, anchor navigation, focus visibility, and print/PDF action visibility. If images use lazy loading, scroll all journey groups before declaring success and report total image count, `pending`, and `broken` counts. Capture current report screenshots under the approved `output/pm-chain-<date>/browser/` run path, close the browser/server, and archive tool caches rather than leaving root-level output.
