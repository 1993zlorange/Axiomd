---
name: scienceresearch-user-manual
description: Create, revise, and verify the scienceresearch user manual from the current requirements, design, implementation, tests, and real-browser evidence. Use when engineering changes user-visible behavior, commands, APIs, errors, installation, operations, or acceptance steps, or when the user asks to write/update `科研工作台用户手册_20260828.md`. Keep result screenshots and visible legends beside the relevant chapter workflow rather than in a separate screenshot chapter unless explicitly requested.
---

# ScienceResearch User Manual

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. The current `科研工作台用户手册_20260828.md`, when present, is the structural reference for chapter order and evidence placement; it is not permission to copy stale claims. Name each new manual `YYYYMMDD-内容简述-用户手册.md` and retain the stable document ID and governing baseline in frontmatter.

Maintain `doc/科研工作台用户手册_20260828.md` as an executable, evidence-backed guide to the current product. The manual must help a user start the application, finish each supported workflow, understand expected feedback and failure behavior, and distinguish implemented capability from proposed or manual-only scope.

## Sources

Read the current repository before editing, in this order:

1. `doc/科研工作台需求文档_20260828.md`;
2. `doc/科研工作台架构与设计方案_20260828.md` and `doc/科研工作台项目架构_20260828.md`;
3. current `README.md`, `serve.py`, `src/`, routes, CLI commands, tests, and fixtures;
4. `log/demand_log.md`, `log/engineer_log.md`, and `log/test_log.md`;
5. latest applicable `output/project-test/` and `output/pm-chain-*/` evidence.

Do not copy claims from an older manual without confirming them against current code and evidence.

## Mandatory workflow

1. Identify what changed: installation, navigation, user journey, input constraints, visible results, errors, CLI/API contract, security boundary, operations, or acceptance status.
2. Map the change to the existing manual chapter. Preserve the established chapter order and update the smallest coherent section. Read [references/manual-structure.md](references/manual-structure.md) for ScienceResearch chapter routing.
3. Write steps in user order. For each workflow state prerequisites, exact action, expected visible result, persisted/server-side effect when relevant, failure behavior, and recovery.
4. Place actual result screenshots immediately after the workflow they demonstrate. Do not create a separate screenshot/evidence chapter unless the user explicitly asks for one. Read [references/figure-evidence.md](references/figure-evidence.md) before adding or reusing images.
5. Give every image a visible legend on the next non-empty line. Use chapter-scoped numbering such as `图例 7-2` and state the page/state, what the image verifies, requirement or quality IDs when useful, and any evidence limitation.
6. If an adequate image does not exist, run the application with an isolated data directory under `output/pm-chain-<YYYYMMDD>/data/`, execute the real user journey in a browser, and save the screenshot under the matching run directory. Never modify formal `data/` merely to create documentation.
7. Keep references repository-relative. From `doc/`, screenshots under `output/` normally use `../output/...`.
8. Update the manual's implementation/test status when evidence changes. Preserve `draft`, `proposed`, `approved`, `PARTIAL`, `NOT_TESTED`, and `MANUAL_REQUIRED` honestly.
9. Append a precise timestamped paragraph to `log/engineer_log.md` for the documentation change. Update `log/test_log.md` only if testing or browser verification was actually run.
10. Run the completion checks below before handoff.

## Writing rules

- Use the interface's actual Chinese labels, route names, field names, commands, error codes, and file paths.
- Explain user intent before low-level syntax. Put commands in fenced blocks and explain their observable result.
- Distinguish browser form behavior from JSON API behavior.
- State prerequisites before actions that depend on Context, Workflow, Week, Item, Evidence, approval, files, or permissions.
- Explain constraints at the point they matter: two-item weekly limit, relation requirement, artifact path boundary, author confirmation, six completion gates, safe Skill capabilities, and isolated/offline behavior.
- `localStorage` may be described only as storage for unsubmitted summary drafts. Business state remains server-side.
- `MANUAL_REQUIRED` means controlled manual fallback, not successful automation.
- Do not call a minimal PPTX a final presentation template, a displayed route a complete workflow, or a technical test pass customer acceptance.
- Do not duplicate the same procedural text in a later evidence chapter. Link to the separate HTML evidence book when deeper traceability is useful.

## Completion checks

The manual update is complete only when:

- chapter numbering and heading hierarchy remain coherent;
- the changed behavior is described in the relevant workflow chapter;
- every Markdown image path exists and points to a valid image format;
- every image's next non-empty line is a visible `图例`;
- every chapter from 4 through 15 that currently contains user-facing or acceptance content has at least one relevant result image when evidence exists;
- historical failure images are explicitly labeled and are not presented as final passing evidence;
- commands, routes, filenames, IDs, status labels, and test counts match current evidence;
- links to the project-stage report or requirements journey evidence book resolve correctly when present;
- UTF-8 text renders correctly and no accidental mojibake was introduced;
- the final response names the changed sections, image/legend counts, missing or unverified evidence, and the log entry.

If the current repository cannot provide a truthful result image, state `缺少当前通过截图` and cite the strongest available API/database/test evidence. Do not use an unrelated screenshot as if it proved the workflow.
