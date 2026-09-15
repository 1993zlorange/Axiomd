---
name: scienceresearch-repository-layout
description: Plan, validate, and document file placement for any scienceresearch implementation, refactor, test, browser-evidence, documentation, migration, or generated-artifact work. Use whenever the pr-en-00-engineer may create, move, rename, archive, or delete repository files. Prevent root-directory clutter, formal/test data mixing, broken evidence links, and unapproved directory structures; do not use it as authorization for an architecture migration.
---

# ScienceResearch Repository Layout

For a retained Placement Audit, start from [assets/placement-audit-template.md](assets/placement-audit-template.md) and name it `YYYYMMDD-内容简述-放置审计.md`.

Keep every file owned by a named project area and lifecycle. A convenient new folder is not sufficient justification for creating it.

## Mandatory entry check

Before writing files:

1. Read `doc/adr/ADR-008-仓库运行数据与证据目录分离.md`, the repository-layout section of `README.md`, and the affected architecture/design section.
2. Inspect the repository root and the destination's neighboring files. Reuse an existing owner and naming convention when one exists.
3. State a compact **Placement Plan** for every new, moved, renamed, or generated file:

```text
Artifact | owner | lifecycle | final path | references affected | cleanup/archive rule
```

4. If a proposed stable artifact has no owner in the directory contract, do not add a new root directory. Return the directory-boundary decision to the project manager and require an architecture review.
5. Treat moves of `doc/`, `idea/`, `data/`, `log/`, `output/project-test/`, `output/pm-chain-*`, or `output/playwright/` as migrations, not ordinary cleanup.

Read [references/repository-layout-contract.md](references/repository-layout-contract.md) for the authoritative placement matrix, prohibited placements, and migration protocol.

## During implementation

- Put product code under `src/scienceresearch/` according to the approved domain/application/adapters/interfaces boundaries.
- Put automated tests and immutable test fixtures under `tests/`; put test databases, browser profiles, screenshots, traces, and generated test artifacts under an isolated `output/.../<run-id>/` directory.
- Never use formal `data/` to create tests, screenshots, demos, or documentation evidence.
- Put maintained project documents under `doc/`, source ideas/prototypes under `idea/`, operator/developer entry scripts under `scripts/` or an already approved root entry point, and Agent/Skill definitions under `.codex/`.
- Put published reports and retained evidence under the currently approved `output/` contracts. Put disposable execution artifacts under `output/runs/<run-id>/`; archive historical retained artifacts under `output/archive/` with a manifest when their original location matters.
- Do not create root-level `tmp`, `smoke`, `audit`, `final`, browser-cache, test-data, database, screenshot, report, or duplicate source directories.
- Keep temporary material inside its run directory or an operating-system temporary directory, and remove it before handoff when it has no evidence value.
- Do not silently rename or relocate an active evidence path merely to make the tree look cleaner. Update every code, document, HTML, Skill, Agent, test, and log reference first, validate them, then retire the old path after the agreed compatibility cycle.

## Completion gate

Run the deterministic layout check from the repository root:

```powershell
python .codex/skills/scienceresearch-repository-layout/scripts/check_repository_layout.py .
```

Then verify the changed paths and references with `rg`, run the implementation's normal tests, and append one timestamped paragraph to `log/engineer_log.md` naming:

- what files were created, moved, renamed, archived, or deliberately left in place;
- why each path owns the artifact;
- the isolated run directory used for generated/test output;
- layout-check and reference-check results;
- any approved exception, migration compatibility path, or remaining risk.

Handoff must include a short **Placement Audit**: new paths, moved paths, generated paths, layout-check result, stale-reference result, and cleanup/archive result. The task is not complete while an unexplained root item, test database in `data/`, generated artifact in source/document directories, or broken old-path reference remains.
