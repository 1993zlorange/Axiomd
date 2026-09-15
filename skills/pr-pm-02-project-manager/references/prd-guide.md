# PRD Guide

Read this reference when creating or reviewing a project requirements document.

## Required reasoning

Before drafting, identify:

1. **Problem:** What observable pain or missed outcome exists now?
2. **User/stakeholder:** Who experiences it, operates the solution, approves it, and maintains it?
3. **Outcome:** What changes for the user or project when the solution succeeds?
4. **Evidence:** What facts support the problem and proposed priority?
5. **Boundary:** What is in scope now, explicitly out of scope, and deferred?
6. **Constraints:** Time, data, compatibility, security, offline use, platforms, budget, skills, and policy.
7. **Verification:** What behavior or metric proves each requirement is satisfied?

Do not let a proposed solution replace the problem statement. When the user starts with a technology choice, preserve it as a constraint or assumption and still define the outcome it serves.

## Requirement taxonomy

- `FR-*`: User-visible or system functional behavior.
- `NFR-*`: Performance, reliability, accessibility, security, maintainability, portability, or usability.
- `DATA-*`: Source, schema, quality, lineage, retention, privacy, migration, and failure behavior.
- `INT-*`: External interface, protocol, version, authentication, timeout, idempotency, and error contract.
- `OPS-*`: Deployment, configuration, observability, backup, recovery, support, and offline operation.

Each requirement should contain:

- ID and priority;
- statement using a specific actor and observable behavior;
- rationale or linked outcome;
- acceptance criteria;
- dependencies and assumptions where relevant;
- status: proposed, approved, implemented, verified, or deferred.

## Acceptance criteria

For a workflow:

```text
Given <starting state>
When <actor action or event>
Then <observable result>
And <failure/edge behavior when material>
```

For a quality attribute, name the environment and measurement method:

```text
On <reference environment>, <operation> completes within <threshold>
for <percentile/sample size>, measured by <method>.
```

Avoid `fast`, `easy`, `user-friendly`, `robust`, `intelligent`, `seamless`, or `supports` unless the document defines how each is measured.

## Scope and priority

Use MoSCoW carefully:

- **Must:** The release cannot meet its objective without it.
- **Should:** High value, but a documented workaround exists.
- **Could:** Useful if time and risk budget remain.
- **Won't now:** Explicitly deferred to prevent accidental scope growth.

Every Must requirement needs a verification method. If everything is Must, prioritization has failed.

## Planning conversion

After requirements are approved:

1. Group requirements into outcome-based milestones.
2. Define a gate for each milestone using artifacts and evidence.
3. Split implementation into 1-2 day tasks when practical.
4. Give every task an action title, context, output, acceptance criteria, dependencies, and requirement IDs.
5. Identify the critical path and decisions that block multiple tasks.
6. Track requirement changes by impact on tasks, tests, interfaces, documents, and schedule.

## Review checklist

- The problem can be understood without reading the solution section.
- Users, operators, approvers, and maintainers are not conflated.
- In-scope, out-of-scope, and deferred work are explicit.
- Every Must requirement has observable acceptance criteria.
- Failure states, permissions, data quality, and offline/degraded behavior are addressed when relevant.
- Functional and non-functional requirements do not contradict each other.
- Architecture decisions are separated from requirements unless the user fixed them as constraints.
- Assumptions and open questions have closure evidence or a decision owner.
- Success metrics measure outcomes, not only activity or output volume.
