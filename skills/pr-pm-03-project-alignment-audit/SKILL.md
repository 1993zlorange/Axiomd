---
name: pr-pm-03-project-alignment-audit
description: Audit an existing software, data, or research project for drift from its approved requirements, architecture, and design using repository, test, runtime, and project-log evidence. Use when a project manager must determine whether implementation or current work has deviated, distinguish implementation drift from stale specifications or unapproved scope, and produce a prioritized correction plan. Do not use as authorization to implement the corrections.
---

# Project Alignment Audit

For a retained audit document, start from [assets/output-template.md](assets/output-template.md) and name it `YYYYMMDD-内容简述-对齐审计.md`.

Perform a read-only, evidence-backed alignment audit. Determine whether the project is still building the approved outcome, not merely whether files exist or tests pass.

## Audit modes

- **Baseline audit:** compare the current repository and documented status with the authoritative requirements and design.
- **Change audit:** assess a proposed or recent change for requirement, architecture, scope, and verification drift.
- **Phase-gate audit:** decide whether a milestone or release can pass its stated gate.

If the repository is the `scienceresearch` project or contains its named SRS/SDD/ARCH files, read [references/scienceresearch-profile.md](references/scienceresearch-profile.md) before auditing.

## Evidence hierarchy

Resolve the target truth before calling anything drifted. Use this precedence unless the user supplies another governance rule:

1. The user's current explicit decision or an approved change record.
2. Approved requirements and acceptance criteria.
3. Approved architecture, SDD, ADRs, and interface/data contracts that realize those requirements.
4. Approved milestone scope and qualification gates.
5. Implementation, tests, deployment configuration, user documentation, and logs as evidence of the actual state.

Draft or proposed documents are candidate baselines, not silently approved contracts. If all available baselines are draft, audit against the named candidate and label the verdict `PROVISIONAL`. Implementation does not automatically override an approved requirement; a newer user decision may instead mean the specification is stale.

## Workflow

### 1. Establish scope and baseline

- Read project instructions, requirements, architecture/SDD, ADRs, milestone or task plans, acceptance criteria, status/user documentation, and relevant demand/engineering logs.
- Record document IDs, versions, status, dates, and explicit precedence or approval state.
- Identify the project objective and the phase being assessed.
- State exclusions and evidence that is unavailable. Do not pretend completeness when the baseline or actual state cannot be inspected.

### 2. Inspect the actual project

- Inspect manifests, configuration, entry points, module boundaries, interfaces, persistence, migrations, tests, deployment/runtime files, documentation, and recent project logs.
- Use `rg`/`rg --files` first. Run safe existing tests or diagnostics when they materially strengthen the verdict and the user asked for a project audit rather than a document-only review.
- Use `scripts/collect_alignment_evidence.py` to inventory document versions, stable requirement IDs, trace references, and production placeholders when those artifacts exist. Treat its output as evidence signals, never as the verdict.
- Verify behavior and data flow where a requirement could appear implemented while a downstream path, UI, export, persistence write, or failure case is missing.

### 3. Build bidirectional traceability

For each relevant Must requirement and each phase-gate item, trace:

```text
source decision -> requirement/acceptance -> architecture/design element
                -> implementation/runtime path -> test or qualification evidence
                -> documented status and retained evidence
```

Also trace backward from major implemented capabilities to a requirement, approved decision, or architecture rationale. Do not declare a requirement missing only because its ID is absent from source comments; inspect observable behavior and tests. Conversely, a matching class name, route, table, or screenshot is not proof that the required behavior and failure paths exist.

Use these coverage states:

- `COVERED`: behavior, design, implementation, and verification evidence agree.
- `PARTIAL`: some required behavior, boundary, failure path, or evidence is missing.
- `MISSING`: no credible implementation or design response exists.
- `CONTRADICTORY`: actual behavior or design conflicts with the controlling baseline.
- `UNJUSTIFIED`: implemented scope has no approved requirement or rationale.
- `UNVERIFIED`: implementation may exist, but evidence is insufficient.
- `DEFERRED`: explicitly deferred with a valid phase/scope decision.
- `NOT_APPLICABLE`: explicitly justified and approved, not merely skipped.

### 4. Classify the drift

Assign one primary type to each finding:

- `IMPLEMENTATION_DRIFT`: code/runtime behavior contradicts or omits an approved requirement.
- `ARCHITECTURE_DRIFT`: module dependency, data ownership, trust boundary, deployment unit, or interface contract violates the approved architecture/design.
- `DESIGN_DRIFT`: SDD/architecture no longer realizes the approved SRS or leaves Must requirements unowned.
- `SPECIFICATION_DRIFT`: a newer approved decision is implemented or required, but SRS/SDD/ARCH were not updated consistently.
- `SCOPE_DRIFT`: unapproved capability, abstraction, infrastructure, or polish displaces higher-priority required outcomes.
- `VERIFICATION_DRIFT`: a capability is claimed complete without the required test, qualification, or retained evidence.
- `STATUS_DRIFT`: README, user manual, milestone, or logs claim a state that conflicts with repository/runtime evidence.
- `PLAN_DRIFT`: active work is not traceable to approved priorities, or lower-priority work blocks an unmet Must path.

Do not collapse all mismatches into “code is wrong.” First decide which artifact should change: implementation, tests, requirements, architecture/design, plan, or status documentation.

### 5. Rate severity and confidence

- `Critical`: violates a mandatory safety, authorization, scientific-integrity, data-integrity, or irreversible-loss constraint; or makes the claimed project objective impossible.
- `High`: a core Must workflow is missing/contradicted, a major boundary is broken, or a release/milestone claim is false.
- `Medium`: partial Must/Should coverage, meaningful verification gap, maintainability risk, or localized scope drift.
- `Low`: documentation hygiene, weak trace labels, or a localized improvement with limited outcome impact.

Give every finding `High`, `Medium`, or `Low` confidence. Confidence is based on source authority and directness of evidence, not rhetorical certainty. Never fabricate approval, runtime results, test outcomes, or stakeholder intent.

### 6. Recommend the smallest safe correction

For each confirmed drift, choose the correction route:

- Wrong implementation -> update implementation and tests against the unchanged approved contract.
- Stale requirement -> project manager proposes the requirement change; freeze it before architecture/design changes.
- Stale or inadequate design -> architect updates architecture/SDD after the requirement baseline is fixed.
- Unapproved scope -> pause, defer, remove, or explicitly seek approval; preserve useful artifacts when practical.
- Missing evidence -> add the smallest qualification/test that proves the behavior; do not mark complete based on activity.
- Conflicting baselines -> stop irreversible work and request the decision that selects the target truth.

Order corrections by dependency and outcome. Prefer restoring one end-to-end Must path before expanding breadth. Each correction item must name affected requirement/design IDs, files or modules, expected result, verification evidence, dependencies, and rollback/recovery considerations. Do not implement fixes unless the user separately authorizes implementation.

## Required output

Lead with one verdict:

- `ALIGNED`: no Critical/High drift; mandatory paths are covered with evidence.
- `AT_RISK`: no confirmed Critical drift, but material partial/verification gaps exist.
- `DRIFTED`: at least one confirmed Critical/High mismatch with the controlling baseline.
- `UNVERIFIABLE`: baseline or actual-state evidence is too incomplete or contradictory for a responsible verdict.

Then provide:

1. **Audit basis:** baseline documents/versions/status, inspected implementation/test/runtime evidence, and limitations.
2. **Outcome summary:** what remains aligned, what has drifted, and the affected project objective or phase gate.
3. **Findings:** stable IDs such as `DRIFT-001`, ordered by severity, with type, requirement/design references, expected versus actual, file/line or command evidence, impact, and confidence.
4. **Traceability matrix:** prioritize Must requirements and phase gates; summarize large fully covered areas instead of dumping every low-risk row.
5. **Root causes:** distinguish symptom from cause, such as stale baselines, priority inversion, missing ownership, weak qualification, or uncontrolled side work.
6. **Correction plan:** `Now`, `Next`, and `Deferred`, with verification and decision dependencies.
7. **Decisions required:** only choices that materially alter scope, design, permissions, schedule, or acceptance.

When no drift is found, still list the evidence inspected and the highest residual risks. When findings rely only on indirect evidence, label them `UNVERIFIED` rather than presenting them as defects.

## Boundaries

- The audit is read-only unless the user explicitly asks to apply corrections.
- Do not treat draft architecture preferences as approved requirements.
- Do not use test count, code volume, completed task count, or UI presence as a substitute for requirement outcomes.
- Do not recommend discarding working code solely to make documents look consistent; first identify the authoritative target and reuse compatible work.
- Do not broaden the audit into security, performance, or code-style review unless those qualities are required by the governing baseline or are the source of drift.
