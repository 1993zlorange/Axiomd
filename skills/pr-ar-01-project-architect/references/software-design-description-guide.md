# Software Design Description Guide

Read this reference when creating or reviewing a software design description (SDD), detailed design specification, module design, class/API design, or implementation design derived from an approved SRS and architecture.

## Contents

1. SDD boundary and required inputs
2. Source-inspired document structure
3. Design identifiers and traceability
4. Requirement-module-interface coverage
5. System and module design views
6. Data, state, algorithm, and failure design
7. Interface contracts
8. Runtime and cross-cutting concerns
9. Verification and review gate

## SDD boundary and required inputs

An architecture proposal decides the system shape, major boundaries, deployment units, technology families, and cross-cutting strategies. An SDD specifies the internal design that developers implement. An SRS defines normative behavior and quality targets. Do not merge these responsibilities.

Before detailed design, identify:

- approved requirement IDs, use cases, data/interface requirements, quality scenarios, and implementation constraints;
- architecture decisions, module boundaries, dependency direction, runtime/deployment topology, and ADRs;
- repository evidence for existing systems, including actual classes/functions, data structures, threading, error handling, configuration, tests, and build integration;
- unresolved decisions that block interface, ownership, persistence, concurrency, or compatibility design.

Record these inputs in document control with document/version/status, decision owner, approval record, and change history. A change entry should identify affected requirements, modules/submodules, interfaces, data, tests, and downstream artifacts. An SDD can be a useful `proposed` candidate against a `draft` SRS, but it must not describe that input as an approved baseline.

If requirements are missing or contradictory, record the gap and return it to `pr-pm-02-project-manager`; do not invent contractual behavior. If architecture is absent, make and label the minimum architecture decisions required before writing class-level detail.

## Source-inspired document structure

For each substantial module, use this seven-part structure when relevant:

1. **Background**: why the module exists, its context, responsibility, and boundaries.
2. **Definitions**: module-specific terms, types, state names, units, and abbreviations.
3. **References**: SRS requirements, architecture sections, ADRs, standards, external API/data documents, and source files.
4. **Task overview**: goals, actors/callers, inputs, outputs, assumptions, dependencies, and constraints.
5. **Requirement/design mapping**: linked functional, precision, timing, I/O, fault-handling, environment, security, and compatibility requirements with an explicit design response.
6. **Module design**: internal components/classes/functions, dependencies, data/state, algorithms, workflows, errors, resources, concurrency, configuration, observability, and test seams.
7. **Interface design**: exact public/internal contracts, parameters, results, failures, side effects, lifecycle, timing, thread safety, versioning, and conformance tests.

Define common concepts once at system level and reference them from modules. Do not repeat inconsistent runtime constraints or type definitions in every module.

The seven sections are a useful module skeleton, not permission to omit system-level context, cross-module data ownership, deployment, security, or verification.

## Design identifiers and traceability

Give consequential design elements stable IDs:

- `MOD-*`: module/component;
- `CLS-*`: class, protocol, or cohesive internal type;
- `DATA-DES-*`: designed data structure/schema/storage mapping;
- `ALG-*`: algorithm and numerical method;
- `FLOW-*`: sequence, state, processing, or control flow;
- `API-*`: function, method, endpoint, event, file, or external interface;
- `ERR-*`: error taxonomy and recovery behavior;
- `CFG-*`: configuration item;
- `DEP-*`: runtime/deployment unit;
- `ADR-*`: durable architecture/design decision.

Define the identifier vocabulary in the SDD when several families are used. Include the English expansion, local-language name, project meaning, and usage boundary. Keep SRS identifiers and design identifiers distinct: `INT-*` states what an interface boundary must guarantee; `API-*` states the concrete function, route, message, event, file, protocol, or internal port that realizes it. Do not renumber stable IDs merely because sections move.

Do not encode volatile chapter numbers in IDs. Maintain bidirectional traceability:

```text
SRS requirement/use case/constraint
  -> architecture decision and module
  -> class/data/algorithm/flow/interface
  -> unit/contract/integration/qualification test
  -> retained evidence
```

Every Must requirement needs a design response or an explicitly tracked gap. Every public interface, persistent structure, privileged operation, and high-risk algorithm needs a requirement or architecture rationale; otherwise flag speculative design.

## Requirement-module-interface coverage

When the SRS defines modules and submodules, maintain an explicit matrix with at least:

| SRS module | SRS submodule | SRS interface or internal-boundary reason | Exact SDD API/function table | Relationship/boundary | Coverage state |
|---|---|---|---|---|---|
| `MOD-*` | `SM-*` | `INT-*` or justified absence of an independent external interface | one or more exact `API-*` function IDs | direct / combined / internal adaptation | covered / gap / proposed addition |

Apply these rules:

- Every SRS submodule appears exactly once as an ownership row, though the row may reference multiple functions for a composed workflow.
- **Direct** means the listed interface directly carries the submodule's principal contract. **Combined** means several real interfaces jointly form the complete behavior. **Internal adaptation** means no separate external interface is warranted, but an explicit application/domain port, renderer fallback, CLI entry, or internal caller contract still owns the behavior.
- A design interface family may contain several concrete functions; use stable suffixed or otherwise unique function IDs and make every exact matrix reference resolve to a function table.
- A UI shell, facade, controller, gateway, or generic bridge is routing infrastructure, not evidence that a missing domain/application interface exists. Do not map unrelated submodules to a bridge merely to make coverage look complete.
- If a submodule has no adequate interface, add the smallest coherent function/port to the owning module and document its inputs, outputs, failures, execution semantics, compatibility, and verification. Do not invent new product behavior; return genuine requirement gaps to the requirements owner.
- Re-run coverage whenever SRS modules/submodules, interface requirements, or module ownership changes. Report the derived count, duplicates, missing rows, unresolved API references, and intentional internal-only cases.

## System and module design views

Select only views that communicate real relationships:

- system context and external dependencies;
- container/process and deployment view;
- module/component dependency view;
- class/protocol composition view;
- data model, schema, ownership, and lifecycle view;
- sequence or collaboration view for consequential use cases;
- state machine for stateful behavior;
- processing/activity flow for branching algorithms;
- concurrency/resource view for threads, workers, GPU/device contexts, files, connections, and caches.

Diagrams support the design but are not the contract. Give every diagram a purpose, stable names, direction, boundaries, and a text/table counterpart. Make diagrams and interface tables use the same identifiers and terminology.

### Module responsibility record

For each module define:

- responsibility and non-responsibility;
- provided and required interfaces;
- inbound/outbound dependencies and allowed direction;
- owned data, state, resources, configuration, and errors;
- lifecycle: creation, initialization, steady state, shutdown, cleanup, and recovery;
- extension points and invariants;
- tests that can validate it independently.

A feature list or diagram of boxes is not sufficient design.

## Data, state, algorithm, and failure design

### Data and state

For every important data structure specify:

- name, semantic meaning, type/shape, units, coordinate system, encoding, range, nullability, precision, and invariants;
- producer, consumer, owner, mutability, copy/view semantics, memory or storage layout, lifetime, and cleanup;
- serialization/schema version, validation, migration, backward compatibility, and provenance where relevant;
- indexing, ordering, transaction, consistency, retention, backup, and restore behavior for persistent data.

For engineering and visualization software, define scalar/vector/tensor association, component order, mesh/topology relation, coordinate frame, precision, endian/format behavior, and behavior for missing vector components or invalid topology.

For stateful modules, provide a state machine and define legal transitions, idempotency, re-entry, cancellation, partial success, rollback, and crash recovery.

### Database and persistence design

Read and apply [database-design-standard.md](database-design-standard.md) whenever a module owns, queries, or mutates database state. The resulting design must be implementation-ready: engineers may translate syntax for the chosen migration framework, but must not have to invent columns, constraints, relationships, access patterns, transaction boundaries, concurrency behavior, migrations, rollback/restore policy, or qualification cases.

For every module that owns, queries, or mutates persistent data, include a module-local database design and a system-level consolidation. An entity name or ORM model alone is not an implementable database contract. Document at least:

- every table, its purpose, owning module, schema version, row identity, lifecycle, retention, backup/restore role, and linked SRS `DATA/FR/OPS` requirements;
- every field with physical database type, business meaning, nullability, default, validation or `CHECK`, confidentiality/provenance classification when relevant, and the application value or DTO field it maps to;
- primary keys, candidate/unique keys, foreign keys and their `ON DELETE`/`ON UPDATE` behavior, relationship cardinality, and invariants that span rows or tables;
- indexes, their column order and uniqueness, the exact queries or qualification thresholds they support, and the write/storage trade-off; do not add speculative indexes;
- transaction boundaries, isolation/locking assumptions, optimistic version fields, idempotency keys, ordering, outbox/trash/compensation behavior, and user-visible outcome after partial failure;
- schema creation and version detection, forward migration, data backfill, compatibility window, failed-migration rollback or restore, downgrade policy, and verification fixtures for both populated and empty databases;
- deletion, archival, audit retention, path/file coordination, and orphan detection when database rows own filesystem or external artifacts;
- traceability from requirement and submodule through API/function, table/field or view, migration, and unit/contract/integration/qualification evidence.

For each module that does not persist data, state this explicitly and name the module that owns any data it consumes. Cross-module code must call the owning module's interface rather than write another module's tables directly. At system level, provide a table-ownership matrix and check that every persistent SRS entity and every privileged mutation resolves to one owner, one transaction design, and a tested migration path.

### Algorithms and processing flows

For each consequential algorithm define:

- goal, linked requirement, mathematical contract, assumptions, inputs, outputs, units, and invariants;
- numbered steps or pseudocode, branching and termination conditions;
- numerical precision, tolerance, degeneracy, invalid data, and convergence behavior;
- time and space complexity, expected resource use, and performance-sensitive paths;
- determinism, random seeds, parallelism, device selection, and reproducibility where relevant;
- fallback, approximation, error bounds, and verification oracle.

Do not hide an algorithm behind `call library X`. Specify the preprocessing, library contract, parameters, output interpretation, error mapping, ownership, and version constraints that the application relies on.

### Errors and recovery

Define a stable error taxonomy. Each failure path needs source condition, detection, error/result, user/caller-visible behavior, logging/metrics, cleanup, retryability, and final state. Avoid `return false` when callers cannot distinguish invalid input, missing object, unsupported format, resource exhaustion, or internal failure.

## Interface contracts

For each public or cross-module interface, document more than name/input/output:

Start each concrete function with a compact, consistently named table so reviewers and automated checks can find the minimum contract:

| Field | Minimum content |
|---|---|
| Function name | exact signature, method/path, message/event, file operation, or port operation |
| Function description | observable purpose and the submodule/requirement behavior it realizes |
| Input | names, types/schema, units/encoding, validity, ownership, authorization, and prerequisite state |
| Output | success/empty/partial result, state/event/artifact side effects, version/hash, and final status |

Follow it with interface constraints covering stable errors, transaction or execution model, idempotency, timeout/cancellation, concurrency, rollback/cleanup, compatibility/versioning, boundary behavior, and requirement/submodule/qualification trace. A function table that contains only a name and happy-path prose is incomplete.

| Field | Required design information |
|---|---|
| Identity | API ID, exact signature/path/message/file event, visibility, version |
| Ownership | provider, caller/consumer, data/resource owner, lifetime |
| Traceability | linked requirement, use case, module, data, error, and tests |
| Preconditions | required state, valid ranges, permissions, initialized resources |
| Parameters | name, type, units, range, encoding, nullability, mutability, ownership/copy semantics |
| Result | type, meaning, units, partial result, postconditions, side effects |
| Failure | errors/exceptions/status, cleanup, caller action, retryability |
| Execution | sync/async, blocking, timeout/cancellation, ordering, idempotency |
| Concurrency | thread/process/device affinity, reentrancy, locks, race behavior |
| Compatibility | ABI/schema/protocol version, deprecation, extension, migration |
| Verification | unit/contract fixture, boundary and negative cases, retained evidence |

For C/C++ interfaces, additionally specify constness, pointer/reference validity, allocation/deallocation owner, buffer size, exception/`noexcept` behavior, ABI/export boundary, compiler/runtime compatibility, and thread safety. For Python, specify type hints/protocol, sync versus async, exception contract, mutable defaults, resource/context-manager behavior, and serialization boundary.

Use typed error/result contracts instead of an undifferentiated boolean when callers need actionable failure information. Preserve existing ABI signatures when compatibility is mandated, but document an error-query or richer wrapper strategy if the existing API cannot express the contract.

## Runtime and cross-cutting concerns

At system and module levels, address only applicable concerns:

- startup, initialization order, dependency injection, shutdown, and resource cleanup;
- threads, event loops, workers, GPU/device context, processes, queues, locks, and cancellation;
- memory, file handles, connections, caches, temporary files, and resource budgets;
- configuration source, validation, defaults, reload, secrets, and compatibility;
- logs, metrics, traces, correlation, health, diagnostics, and failure visibility;
- authentication, authorization, trust boundaries, input validation, least privilege, and sensitive-data handling;
- build targets, packaging, compiler flags, native dependencies, plugin/host integration, deployment, upgrade, and rollback;
- extension points, feature flags, migration, and backward compatibility.

Do not copy an environment statement from the SRS without resolving conflicts. If one source says Windows and another says Linux/DCU, record the conflict, affected modules, decision owner, and required compatibility evidence.

## Verification and review gate

Turn design promises into tests or checks:

- class/module unit tests for invariants, state, algorithms, and failure cleanup;
- interface contract tests for signatures, types, errors, ownership, versioning, and boundary values;
- integration tests for dependency chains, build/host integration, devices, files, and data formats;
- performance/resource tests tied to SRS thresholds;
- architecture tests for dependency direction and forbidden imports/calls;
- schema/ABI/OpenAPI compatibility checks;
- static analysis, sanitizers, race detection, leak checks, and numerical reference tests when applicable;
- deployment, startup/shutdown, rollback, and recovery exercises.

Before handing off an SDD, verify:

- all mandatory requirements and constraints map to design elements and verification;
- all SRS modules/submodules have an ownership row and map to exact interface functions or an explicit justified internal-only contract;
- every module has one clear responsibility, allowed dependencies, owned state/resources, and lifecycle;
- all important data structures define semantics, units, ownership, lifetime, validation, and compatibility;
- every persistent module has complete table/field/constraint/index/transaction/migration/rollback design, or an explicit non-persistent rationale; every physical table and privileged mutation traces to an owning module, requirement, interface, and verification case;
- all state transitions, alternate/failure paths, cleanup, retry, cancellation, and recovery behavior are explicit;
- each algorithm states assumptions, precision/tolerances, complexity, degeneracy, fallback, and oracle where relevant;
- interfaces specify exact signatures/contracts, not only functional descriptions;
- every exact API reference resolves to one unique function table containing function name, description, input, and output, plus the applicable constraints and trace;
- diagrams, prose, source names, APIs, data types, and requirement IDs are consistent;
- runtime environment and implementation constraints have sources and no unresolved contradictions;
- speculative classes, interfaces, caches, queues, or abstractions without a requirement or design rationale are removed;
- unresolved decisions include an owner, evidence needed, affected design elements, and closure condition;
- Critical/High design review findings are resolved or explicitly accepted by the accountable owner.
