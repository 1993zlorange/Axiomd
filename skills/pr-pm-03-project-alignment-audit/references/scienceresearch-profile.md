# ScienceResearch alignment profile

Read this profile only when auditing the `scienceresearch` project.

## Controlling artifacts

Resolve the project root, then locate these files by name rather than assuming a drive letter:

| Role | Expected artifact |
|---|---|
| Product interaction baseline | `idea/科研工作分解与每周组会汇报模板_20260828.html` |
| Product intent | `idea/idea.md` |
| Work-package semantics | `idea/科研工作分解与每周组会汇报模板_20260828.md` |
| Requirements | `doc/科研工作台需求文档_20260828.md` (`SRS-SRW-001`) |
| Detailed design | `doc/科研工作台架构与设计方案_20260828.md` (`SDD-SRW-001`) |
| High-level architecture | `doc/科研工作台项目架构_20260828.md` (`ARCH-SRW-001`) |
| Product/status evidence | `README.md`, `doc/科研工作台用户手册_20260828.md` |
| Demand and engineering history | `log/demand_log.md`, `log/pr-en-00-engineer_log.md` |

Check current versions and approval status at audit time. Do not assume `v0.3` remains current merely because this profile was written against it.

## Mandatory product invariants

Unless superseded by a newer approved decision, treat these as high-risk alignment checks:

1. One project, topic, research point, or problem instantiates a complete eight-aspect research workflow.
2. The catalog contains 68 stable work packages. A workflow does not fake completeness by deleting packages; applicability and progress are separate state dimensions.
3. Every work package has a versioned template and one dedicated composite Skill. R1-A may use a manual-guidance composite Skill; missing automation must not block the human workflow.
4. Automatic, manual, and mixed execution preserve human intervention, approval, pause/resume, cancellation, and transfer-to-manual paths.
5. Completion requires evidence gates and author confirmation. `CompletionSuggested` is not automatic completion.
6. Project logs are imported read-only for a selected day/range; low-confidence work-package/stage classification is confirmed by the author.
7. A meeting slide centers on date, one-sentence evidence-bounded conclusion, and the directly corresponding real result image. Missing images use an explicit no-image layout; unrelated or fabricated images are forbidden.
8. Effect cards preserve date, context, work-package/stage, evidence, conclusion boundary, next step, and provenance.
9. New demand governance follows: demand event/log -> PM SRS candidate -> frozen SRS -> architect SDD+ARCH candidates -> joint trace/quality check -> author approval -> consistent/atomic application.
10. Demand and engineering Markdown logs clearly record local time/time zone, what changed, affected scope, and result.

## Delivery phases

- `R1-A 人工闭环`: complete human workflow, 68 templates/manual composite Skills, evidence, log import, PPT/effect card, completion confirmation, and document governance.
- `R1-B 受控自动化`: executable sub-Skills, explicit online discovery if approved, automatic/mixed operation, cancellation/recovery, and permission controls.
- `R1-C 稳定化`: approved performance/capacity targets, backup/restore, compatibility, cross-week statistics, and operational hardening.

Flag work as `SCOPE_DRIFT` or `PLAN_DRIFT` when R1-B/R1-C complexity displaces an unmet R1-A end-to-end path without an approved reprioritization.

## Project-specific audit matrix

At minimum, inspect these paths:

| Audit area | Requirements/design | Actual-state evidence |
|---|---|---|
| Catalog/template/composite Skill | FR-001～FR-005, FR-022～FR-024, FR-033, FR-045; MOD-01 | catalog loader/data, UI detail/actions, tests, fixtures |
| Context and complete workflow | FR-006～FR-009, FR-025～FR-028, FR-047; MOD-02 | context/workflow state, persistence, UI/CLI/API, tests |
| Controlled Skill execution | FR-029～FR-033; MOD-03 | manifest/approval/runner/cancel/recovery, boundary tests |
| Evidence and next work | FR-010～FR-013, FR-034～FR-036; MOD-04 | evidence records, six gates, recommendation decisions, tests |
| Log-to-report | FR-014～FR-019, FR-037～FR-040, FR-046; MOD-05 | log reader, classification/confirmation, real-image mapping, PPT/card artifacts |
| Demand/engineering governance | FR-041～FR-044; MOD-06 | both logs, agent ports or manual fallback, candidate/freeze/joint-check/apply evidence |
| Platform and operations | applicable OPS/NFR/CON/ENV; MOD-07 | configuration, paths, persistence, migrations, recovery, offline tests |

The current repository may contain earlier implementation work that predates the latest candidate SRS. Classify mismatches carefully:

- If implementation contradicts a still-controlling requirement, use `IMPLEMENTATION_DRIFT`.
- If the latest user-approved intent is implemented but one or more of SRS/SDD/ARCH are stale, use `SPECIFICATION_DRIFT` or `DESIGN_DRIFT`.
- If README/user manual claims more or less than tests/runtime evidence, use `STATUS_DRIFT`.
- If a feature exists without an approved requirement and displaced R1-A work, use `SCOPE_DRIFT`; do not automatically demand deletion if it can be safely deferred or reused.

## Correction governance

For requirement-changing corrections, the project manager updates the SRS candidate first. The architect then updates both SDD and ARCH from the frozen candidate. A correction proposal must not suggest independently editing only one of the three governing documents. Record demand and engineering changes in the project logs according to the current approved contract.
