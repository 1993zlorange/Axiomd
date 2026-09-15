# Evidence-Linked Architecture and Design Standard

Use this standard when an architecture or SDD belongs to a coordinated PRD/SRS/design/user-manual baseline. It directly encodes the requested document architecture and does not require access to an external reference project.

## Internalized pattern and authority

Apply the following internalized structural patterns:

- frontmatter plus visible document-control, approval, change-history, baseline, owner, encoding, and status sections;
- stable separation of requirement IDs from design IDs;
- system context, trust boundaries, deployment units, module ownership, concrete interface families, state/data design, error/config contracts, migration, rollback, qualification, ADRs, and review gates;
- consistent detailed structure for each substantial module;
- actual browser evidence placed next to manual workflows, with explicit requirements and qualification captions;
- honest separation of current implementation facts, target design, open decisions, automated tests, browser observation, UAT, and formal acceptance.

These are reusable format and governance patterns, not a portable product architecture. Do not seek external exemplar files during ordinary use; inspect one only when the user explicitly requests source comparison. The target repository's instructions, approved requirements, code, tests, runtime, data sensitivity, and deployment constraints are authoritative. Never copy another project's modules, fixed counts, technology choices, UI layout, schema versions, paths, approval records, or test totals unless the target project independently requires and proves them.

## Document control and evidence labels

An SDD or architecture proposal should declare:

- stable document ID, version, date, status, governing SRS/architecture baseline, decision owner and affected IDs;
- approval record and change history that distinguish confirmed deltas from overall document approval;
- current-state evidence, target design and unresolved decisions;
- encoding/time conventions and related PRD/SRS/manual/UAT artifacts;
- scope and non-goals, especially remote access, multi-tenancy, external cost, scientific correctness, data retention and availability commitments.

Use unambiguous labels such as:

- **Fact / current implementation:** directly supported by repository or recorded runtime evidence.
- **Recommendation / target design:** proposed response to an approved requirement; not yet implemented.
- **Approved decision:** approved by the named decision owner for the named scope only.
- **Open decision:** cannot be treated as a constraint or commitment until closed.
- **Qualification result:** tied to a named method, environment, threshold and retained evidence.

Do not use “verified”, “complete”, “production-ready” or “accepted” without defining which of these states is meant.

## Cross-document identifier model

Preserve the governing project's established vocabulary. A common division is:

| Layer | Typical identifiers | Meaning |
| --- | --- | --- |
| Product/software requirement | `PRD-*`, `UC-*`, `FR-*`, `DATA-*`, `INT-*`, `NFR-*`, `OPS-*`, `CON-*`, `QUAL-*` | Normative outcome, behavior, data, boundary, constraint or qualification. |
| Architecture/design | `MOD-*`, `SM-*`, `CLS-*`, `DATA-DES-*`, `ALG-*`, `FLOW-*`, `API-*`, `ERR-*`, `CFG-*`, `DEP-*`, `ADR-*`, `DTO-*` | Design realization of approved requirements. |
| User navigation/evidence | `F-*`, manual chapter/step, `UAT-*`, figure/evidence ID | User-facing explanation and actual proof. |

`INT-*` states what a boundary must guarantee; `API-*` identifies the route, function, message, file or port that implements it. `DATA-*` states logical data requirements; `DATA-DES-*` defines their physical or implementable design. Design identifiers must not create normative product behavior by implication.

Maintain both directions:

```text
feature/user outcome -> PRD/SRS -> MOD/SM -> API/DATA-DES/FLOW/ERR
                     -> manual chapter/step -> UAT/QUAL -> evidence
```

and:

```text
interface/table/job/diagram -> owning module -> requirement rationale
                            -> qualification -> manual impact where user-visible
```

Add a feature-to-design-to-manual matrix for substantial document suites. Classify coverage as direct, combined, internal adaptation, not applicable with rationale, or missing. Do not let a facade, shell, adapter, controller, gateway or bridge conceal a missing domain interface.

## Recommended SDD architecture

Adapt the following structure to the project and remove genuinely inapplicable sections with rationale:

1. Document control, approvals, changes, baseline, status and evidence legend.
2. Goals, non-goals, inputs, terminology, constraints and open decisions.
3. Current-state evidence and architecture decisions.
4. Requirement-to-design and feature-to-manual traceability.
5. System context, actors, trust boundaries and external systems.
6. Containers/processes/deployment units, startup, shutdown and recovery.
7. Modules/submodules, responsibility, non-responsibility, ownership and allowed dependencies.
8. Technology stack described as fact, approved constraint, recommendation or replaceable implementation detail.
9. Detailed design per substantial module.
10. Cross-module data, state, concurrency, transaction, event and recovery design.
11. Unified APIs, errors, configuration, secrets, resources and compatibility rules.
12. Security, privacy, reliability, observability, performance and accessibility strategies where required.
13. Migration, backup, rollback and degraded/read-only behavior.
14. Qualification, architecture fitness functions and retained evidence.
15. ADRs, risks, unresolved decisions, implementation phases and review conclusion.

Do not append chronological design deltas without reconciling them into the authoritative sections. Keep history, but state which rule supersedes older language and update every affected mapping.

## Per-module completeness

Use the same reviewable shape for every substantial module:

1. Background and purpose.
2. Definitions and module-specific vocabulary.
3. Governing references and requirement IDs.
4. Task/use-case overview and operating flow.
5. Submodules with stable IDs, concrete function inventory, inputs, outputs and failure boundaries.
6. Module design: responsibility, non-responsibility, owned data/resources, lifecycle, dependencies, concurrency, transactions, errors, recovery and observability.
7. Interface design: exact functions/routes/messages/files/ports and their contracts.
8. Qualification hooks, evidence location and manual chapters affected.

If a module does not persist data, state why and identify the module that owns relevant state. If it does persist or mutate data, define complete entities/tables/fields, physical types, keys, null/default/check/unique constraints, indexes and query rationale, transactions, retention/deletion, schema version, migration/backfill/rollback and requirement/API/test trace.

For each interface function specify at least:

- stable design ID and exact name/signature or route/message/file contract;
- provider and consumer;
- purpose, inputs, validation and outputs;
- named errors and partial/unknown outcomes;
- transaction, execution, ordering, timeout, cancellation and idempotency semantics as applicable;
- authorization/trust boundary and secret handling;
- versioning, compatibility and deprecation behavior;
- owning requirement/submodule, qualification case, evidence, and manual impact.

## User manual and screenshot alignment

The architecture owns the technical truth that the manual must reflect: authoritative state, identifiers, persistence, file ownership, external effects, cancellation, retry, recovery, trust boundaries and error semantics. It does not own new product workflows.

For every user-visible feature, give the manual writer enough information to state:

- prerequisites and authorization;
- user action and visible/authoritative result;
- persisted data and external effects;
- what closing the browser/session/process does and does not stop;
- retry, idempotency, conflict, rollback and recovery behavior;
- which failure states must be visible;
- which UAT/QUAL and evidence demonstrate the workflow.

Architecture diagrams, prototypes, DOM snapshots, source inspection, unit tests and browser screenshots are different evidence types. If actual screenshots are requested, they must come from the installed/running product, use isolated test data where possible, appear beside the manual step they prove, and carry an immediate caption with action, expected and actual result, environment, date, trace IDs and redaction state. A failure screenshot remains failure evidence. A menu or empty page proves only that visible state, not persistence, external calls, recovery or scientific correctness.

Do not run credentialed, paid, destructive, publishing, remote-compute or external mutations solely to fill an evidence gap. Leave the feature `not run`, `blocked` or `partial`, and specify the fixture, authorization, action, expected state, logs/IDs/screenshots and recovery evidence required.

## Change propagation and validation

For every approved delta:

1. Identify affected PRD/SRS IDs and confirm scope authority.
2. Update modules, APIs, data, flows, errors, config, deployment, migration and ADRs as applicable.
3. Update feature overview, user-manual chapters, UAT/QUAL and release/documentation impact.
4. Reconcile superseded design text instead of leaving contradictory current rules.
5. Validate exact ID/link resolution in both directions.
6. Run applicable schema, contract, migration, architecture-boundary and documentation checks.
7. Report unrelated baseline failures separately and do not rewrite generated or external material merely to make checks green.

An evidence-linked design is ready for review only when every normative SRS submodule maps to implementable design or an explicit justified gap; every public or privileged operation has requirement rationale and qualification; every persistent state owner has migration/recovery design; every user-visible feature has a manual impact; and status claims match retained evidence.
