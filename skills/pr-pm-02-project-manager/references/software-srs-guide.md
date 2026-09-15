# Software Requirements Specification Guide

Read this reference when creating or reviewing a software requirements specification (SRS), a module requirements specification, or a document whose purpose is to contractually define software behavior for design, implementation, integration, test, and acceptance.

## Contents

1. SRS versus PRD
2. Required document structure
3. Identifier vocabulary and document semantics
4. Requirement records and IDs
5. Module, submodule, and use-case specification
6. Data and interface contracts
7. Non-functional requirements and constraints
8. Qualification and traceability
9. Review gate

## SRS versus PRD

A PRD establishes product outcomes, users, scope, priority, and success. An SRS defines what a software system or module must do under specified conditions and how compliance will be verified. Do not use implementation detail to compensate for missing product decisions.

If the user supplies a compiler, operating system, library, data format, build system, or host application, preserve it as `ENV-*`, `INT-*`, or `CON-*` only when it is fixed by the source. Mark an architect's proposed technology separately and do not present it as an approved requirement.

## Required document structure

Adapt the depth to project risk, but cover these decisions:

### 1. Introduction and document control

- machine-readable or visible document ID, version, date, status, target baseline, decision owner, related specifications, encoding/time convention when relevant;
- purpose, scope, target release or module, intended readers, owners, approval record, and change history;
- system context, boundary, stakeholders, external actors, assumptions, dependencies, and explicit exclusions;
- terms and abbreviations, identifier vocabulary, referenced documents, and applicable standards.

Every change record should identify the affected requirement, data, interface, qualification, module/submodule, and downstream design/test artifacts. Keep `draft`, `proposed`, `approved`, `implemented`, and `verified` distinct; editing a document or observing working code does not approve a baseline.

Do not write `none` for terms, references, or data dictionary until the available materials have been checked. If a section truly does not apply, write `Not applicable` with a reason.

### 2. Operating environment

Separate facts from proposals. Record only relevant dimensions:

- hardware class and resource limits;
- operating systems and versions;
- language/runtime, compiler, build system, and versions;
- frameworks, third-party libraries, drivers, and licenses;
- host application, database, file system, network, display, and offline constraints;
- deployment topology and coexistence/compatibility requirements.

Each fixed item needs a source or decision owner. Avoid ambiguous forms such as `Windows`, `C++11 or above`, or `fast GPU` when compatibility depends on an exact range.

### 3. Software and module requirements

For each module, use the following engineering skeleton when relevant:

1. document/module overview and responsibility;
2. module-specific terms and abbreviations;
3. referenced documents;
4. data dictionary;
5. submodules, concrete function inventory, and linked functional requirements;
6. use cases and use-case diagrams;
7. operating or processing flows;
8. interface descriptions;
9. non-functional requirements;
10. design, implementation, and experimental constraints when applicable;
11. qualification provisions.

Common terms, references, data types, interfaces, and constraints should be defined once at system level and referenced by modules. Avoid copying inconsistent definitions into every module.

After module sections, maintain system-level interface/data consistency, system quality requirements, common constraints, qualification/acceptance plan, uncovered items, risks/open decisions, milestones or release gates when relevant, and a requirements-quality checklist. A module-local edit is incomplete if it leaves those system-level views stale.

## Identifier vocabulary and document semantics

Define the identifier families used by the specification, preferably with English expansion, local-language name, normative meaning, and an example. Use only the families the project needs, but keep their boundaries explicit:

| Family | Typical meaning | Boundary |
|---|---|---|
| `SRS-*`, `REF-*`, `ENV-*` | specification identity, source/reference, operating environment | provenance and applicability, not feature behavior by themselves |
| `UC-*`, `FR-*`, `DATA-*`, `INT-*`, `OPS-*`, `NFR-*`, `CON-*`, `QUAL-*` | use cases and normative requirement/qualification contracts | define what must hold and how it is qualified |
| `Q-*`, `R-*` | open decisions and risks | never silently convert an unknown into an approved assumption |
| `MOD-*`, `SM-*` | module and submodule ownership views | organize requirements without replacing numbered normative contracts |
| `SDD-*`, `ARCH-*`, `CLS-*`, `DATA-DES-*`, `ALG-*`, `FLOW-*`, `API-*`, `ERR-*`, `CFG-*`, `DEP-*`, `ADR-*`, `DTO-*` | downstream design and architecture trace identifiers | may be referenced for traceability but do not create new SRS behavior |

The exact prefixes may vary, but a prefix must not be reused with a different meaning. Do not renumber stable IDs merely because headings move. Explicitly distinguish an SRS interface requirement (`INT-*`: what the boundary must guarantee) from a design interface (`API-*`: how a function, route, message, file, or port realizes it).

## Requirement records and IDs

Use stable IDs:

- `ENV-*`: operating environment;
- `UC-*`: user or external-system use case;
- `FR-*`: functional behavior;
- `DATA-*`: data definitions, schema, quality, lifecycle, and error handling;
- `INT-*`: user, software, hardware, file, network, or module interface;
- `NFR-*`: performance, capacity, reliability, safety, security, usability, maintainability, portability, and compatibility;
- `OPS-*`: deployment, configuration, observability, backup, recovery, and support;
- `CON-*`: fixed design or implementation constraint.
- `QUAL-*`: qualification method, environment, procedure, threshold, and evidence contract;
- `MOD-*` and `SM-*`: module and submodule ownership/organization identifiers, traced to normative requirements rather than used as substitutes for them.

For large systems, use a stable module prefix such as `VIS-FR-001`; do not encode volatile chapter numbers in IDs.

Each normative requirement must include:

| Field | Required content |
|---|---|
| ID and status | Stable ID; proposed, approved, implemented, verified, or deferred |
| Priority | Must, Should, Could, or Won't now when prioritization applies |
| Source and rationale | Stakeholder, contract, source document, regulation, defect, or decision |
| Requirement | Actor/system, trigger, precondition, observable behavior, output, and relevant failure behavior |
| Inputs and outputs | Data type, units, valid range, encoding, optionality, and ownership |
| Dependencies | Related use case, data, interface, environment, or constraint IDs |
| Verification | Method, environment/fixture, procedure or oracle, threshold, and retained evidence |

Use `shall`/`应` for normative requirements. Avoid compound requirements joined by multiple independent `and` clauses; split them when they can pass or fail independently. Avoid `support`, `appropriate`, `flexible`, `accurate`, `real-time`, `user-friendly`, or `etc.` unless bounded by an explicit list or measure.

## Module, submodule, and use-case specification

### Module responsibility

State what the module owns, what it does not own, its inputs, outputs, state, dependencies, and error boundary. A list of features is not a module contract.

### Submodule function inventory

For each named submodule, record at least:

| Field | Required content |
|---|---|
| Stable identity | `SM-*` or an equivalent stable project identifier and a precise name |
| Responsibility | the cohesive capability owned by the submodule and what it does not own |
| Concrete functions | explicit query, creation, validation, state-transition, calculation, rendering, import/export, recovery, or coordination behaviors; use verbs and list independently observable functions |
| Inputs | triggering actor/system, data, state, version, authorization, and prerequisite references |
| Outputs and failure boundary | returned data, state/event/artifact side effects, empty/partial result, rejection, rollback, and caller-visible failure |
| Trace | linked `FR/DATA/INT/OPS/NFR/CON/QUAL/UC` identifiers |

Do not treat `manage`, `support`, `process`, or a product-area noun as a complete function description. A reviewer should be able to derive functional requirements, interface needs, and qualification cases from the inventory. Preserve one clear owner for each behavior; cross-module workflows may compose submodules but must not duplicate ownership.

### Use case

Every material use case should define:

- ID and goal;
- primary and secondary actors;
- preconditions and trigger;
- main success flow with numbered steps;
- alternate, invalid-input, dependency-failure, cancellation, timeout, and recovery flows as relevant;
- postconditions and persistent side effects;
- linked requirements and qualification cases.

Use-case and activity/flow diagrams are supporting views. The text must remain sufficient for testing when the diagram is unavailable. Give diagrams a title, stable reference, decision nodes, failure exits, and matching terminology.

## Data and interface contracts

### Data dictionary

Define important data elements and structures with:

- canonical name and business/engineering meaning;
- type, shape, units, coordinate system, encoding, precision, range, nullability, and default;
- producer, consumer, owner, and lifecycle;
- validation, missing/invalid behavior, version, and compatibility;
- confidentiality or safety classification when relevant.

For engineering/scientific data, explicitly define vector/scalar/tensor meaning, component order, spatial/temporal reference, mesh/topology association, and provenance.

### Persistence-related requirements handoff

When a module creates, changes, queries, migrates, archives, or deletes persistent data, its SRS section must identify the logical persistence contract before architecture handoff:

- entities and business attributes, stable identifiers, ownership, cardinality, required/optional values, defaults, valid states, uniqueness, and referential/integrity rules;
- creation and update triggers, state transitions, retention, archival, deletion, audit, backup/restore, import/export, and migration outcomes visible to users or external systems;
- concurrency and consistency expectations, including which user-visible changes must be atomic and what the caller observes after partial or dependency failure;
- confidentiality, provenance, traceability, and qualification evidence where they affect acceptance;
- an explicit indication for each module of whether it persists data. If it does not, state the reason rather than omitting the topic.

Keep this at the logical requirement level. Physical table names, SQL column types, indexes, foreign-key actions, schema-version mechanics, and migration scripts belong in the SDD unless a user, compatibility baseline, regulation, or host system has already fixed them. The SRS-to-SDD handoff must nevertheless be detailed enough for the architect to design every required table and field without inventing product semantics.

### Interface description

Do not stop at `provides an interface`. For every external or module interface, define:

| Field | Examples |
|---|---|
| Interface ID/name | `VIS-INT-001 LoadDataset` |
| Provider/consumer/direction | caller and callee ownership |
| Invocation | function signature, command, HTTP path, message, file event, or UI action |
| Inputs | names, types, units, range, encoding, ownership, lifetime |
| Outputs | success result, partial result, side effects |
| Errors | invalid data, unsupported format, dependency failure, error code/message |
| Timing | timeout, cancellation, blocking/threading, latency when relevant |
| State | idempotency, ordering, concurrency, reentrancy, transaction boundary |
| Versioning | compatibility, deprecation, migration, extension rules |
| Verification | mock/fixture, conformance test, expected evidence |

## Non-functional requirements and constraints

### Non-functional requirements

Express each quality attribute as a measurable scenario:

```text
Given <reference environment and data/load>, when <stimulus>,
the system shall <response> within/at <threshold>, measured by <method>.
```

Cover only relevant categories:

- performance and resource use;
- capacity and scalability;
- reliability, availability, recovery, and data integrity;
- safety and failure containment;
- security, privacy, audit, and supply chain;
- usability and accessibility;
- maintainability, diagnosability, testability, extensibility, and portability;
- interoperability and backward compatibility.

Functional parameter controls, such as an adjustable threshold or sampling density, usually belong in functional/interface requirements. Their response-time, precision, range, or interaction constraints belong in NFRs.

### Design and implementation constraints

Record fixed constraints separately from requirements and recommendations. Each `CON-*` should state the constraint, source, rationale, scope, affected requirements, and what evidence proves compliance. Examples include mandated OS, compiler, library version, host build integration, data structure compatibility, language standard, or API-only integration.

Do not convert a source's current implementation into a permanent constraint without evidence that compatibility or contract requires it.

## Qualification and traceability

`The module shall be tested` is not a qualification provision. Map every normative requirement to one or more qualification cases.

Use one of these methods, with a precise procedure:

- **Inspection:** review a document, configuration, build artifact, UI, code property, or record.
- **Analysis:** calculate or statically analyze a property from evidence.
- **Demonstration:** operate a feature to show behavior where measurement precision is not the criterion.
- **Test:** execute controlled inputs and compare observable results to an oracle and threshold.

Each qualification case should include:

- `QUAL-*` ID, linked requirement IDs, method, preconditions, environment, fixture/test data;
- procedure, expected result/pass threshold, negative and boundary cases;
- retained evidence, owner, and status.

Maintain bidirectional traceability:

```text
source/stakeholder -> requirement -> use case/interface/data/constraint
                   -> module/submodule -> design component
                   -> qualification case -> evidence
```

Flag requirements with no verification and tests with no requirement. A requirement is not accepted merely because a module exists or a screenshot looks plausible.

## Review gate

Before handing off an SRS, verify:

- every heading contains decision-relevant content or an explained `Not applicable`;
- terms, abbreviations, references, data names, units, and API names are consistent;
- system and module boundaries do not overlap or leave behavior unowned;
- every named submodule has concrete functions, inputs, outputs/failure behavior, and valid requirement/qualification references;
- happy, alternate, invalid-input, dependency-failure, cancellation, and recovery paths are covered proportionally to risk;
- interfaces specify actual contracts and errors rather than feature lists;
- NFRs have environment, measure, threshold, and verification method;
- constraints have sources and are not disguised design preferences;
- every normative requirement has a source and qualification mapping;
- every normative requirement appears in the traceability view, and every qualification case points back to at least one requirement;
- diagrams and prose describe the same flow;
- unresolved items identify the decision owner, evidence needed, impact, and closure condition;
- the change record identifies affected requirement, interface, test, and downstream document IDs.
