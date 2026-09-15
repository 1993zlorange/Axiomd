# Engineering Workflow

Read this reference for any implementation, defect fix, migration, or implementation-readiness review that spans more than one trivial file.

## 1. Evidence collection

Start with read-only discovery:

1. Record the project root and inspect repository instructions.
2. Inspect version-control status when available; preserve user-owned changes. If version control is unavailable, say so and use file inventories and hashes where helpful.
3. Read the selected SRS and SDD completely. Record document IDs, versions, statuses, hashes, references, open decisions, and approval state.
4. Inspect manifests, locks, configuration, source, composition root, schemas, migrations, tests, CI, packaging, and runtime/deployment scripts.
5. Trace the current runtime path for the requested behavior from interface to application/domain to adapter and back.
6. Compare code evidence with the documents. Classify observations as `Implemented`, `Partial`, `Missing`, `Drift`, `Blocked`, or `Not in scope`.

Do not start from a proposed directory tree when an existing repository already establishes a different valid convention. Do not infer implementation from document prose alone.

## 2. Requirement-to-code packet

Create a compact working packet before editing. It may remain in the conversation unless the repository requires a persistent plan.

| Field | Required content |
|---|---|
| Scope | User request and exact in-scope behavior |
| Requirement IDs | `UC/FR/DATA/INT/NFR/OPS/CON` IDs |
| Design IDs | `MOD/CLS/DATA-DES/FLOW/ALG/API/ERR/CFG/DEP/ADR` IDs |
| Existing evidence | Current symbols, routes, tables, migrations, tests, or explicit absence |
| Compatibility | Public behavior and stored data that must remain valid |
| Failure behavior | Invalid input, missing dependency, timeout, cancellation, conflict, rollback |
| Verification | Qualification IDs, test layers, commands, fixtures, thresholds, evidence path |
| Exclusions | Nearby behavior intentionally not implemented |
| Decisions | Open questions, owner, evidence, and closure condition |

Maintain forward and reverse traceability:

```text
SRS ID -> SDD element -> source symbol/file -> test/qualification -> evidence
source change -> design reason -> SRS behavior or approved technical rationale
```

A requirement range is acceptable only when every member has the same design and test path. Use explicit rows when one member differs.

## 3. Implementation strategy

Prefer this vertical-slice order when dependencies allow:

1. public behavior and qualification fixture;
2. domain types, invariants, policies, and state transitions;
3. application command/query and transaction boundary;
4. port contracts and typed errors;
5. persistence, file, external service, or process adapters;
6. HTTP/CLI/UI presenter and composition root;
7. observability, operations, migration, backup, and offline packaging;
8. focused verification, full gates, and requirement trace review.

Do not create every layer for a tiny utility. Preserve the SDD's approved boundaries and introduce only elements needed by the slice.

Continue directly for reversible implementation detail inside the SDD. Escalate when evidence requires new behavior or acceptance, breaking API/schema changes, stable ID meaning changes, module ownership changes, new persistence/process/network/privilege boundaries, weaker security/recovery/offline/compatibility guarantees, or destructive migration without rollback.

## 4. Python design and coding checks

Read the target coding standard in full. If no project-specific standard exists, ask the user to approve one or use the repository's documented baseline while avoiding product-specific examples from unrelated projects:

- runtime, encoding, dependency lock, import, and naming baseline;
- domain/application/adapter/interface dependencies;
- function responsibility, pure calculation, parameters, returns, side effects, and abstraction criteria;
- narrow Protocols, public APIs, typed models, UTC time, units, nullability, and validation;
- error taxonomy, exception translation, transaction ownership, and resource lifetime;
- safe database/file/subprocess behavior, concurrency, cancellation, bounded retries, and atomic output;
- HTTP/CLI/UI boundaries, accessibility, structured logging, configuration, secrets, and offline assets;
- test layers, coverage, documentation, review checklist, Definition of Done, and exception process.

Project-approved configuration overrides tool names and thresholds shown as examples in the fallback standard.

For each changed function, verify one clear responsibility; separation of I/O, calculation, and presentation; explicit types, units, nullability, ownership, and errors; injected time/random/state/external access; retry safety; and focused testability.

For each public interface, verify exact signature/schema/version; preconditions and side effects; invalid, missing, conflict, dependency, timeout, cancellation, and partial-success behavior; ordering, pagination, idempotency, concurrency, transaction, compatibility, and contract tests.

## 5. Test strategy

| Level | Primary evidence |
|---|---|
| Unit | Pure rules, invariants, state transitions, algorithms, handlers |
| Contract | Port implementations, serializers, file/API schemas, error mapping |
| Integration | Transactions/migrations, file atomicity, subprocess runner, templates, HTTP |
| Architecture | Forbidden imports, dependency cycles, boundary leakage |
| End to end | Critical user workflows, offline behavior, accessibility |
| Qualification | SRS thresholds and retained acceptance evidence |

For defects, prove the defect with a failing regression test or controlled probe and confirm the failure reason. For features, start from the nearest public qualification contract. A test that mirrors private branches is not acceptance evidence.

Run focused checks during development, then all repository-required gates on the final state. If no commands exist, derive candidates from the manifest rather than guessing. Do not claim unavailable checks passed.

## 6. Debugging and migration

Root-cause debugging:

1. reproduce with a minimal stable case;
2. trace inputs and state across the boundary where behavior diverges;
3. form one falsifiable hypothesis and test it with the smallest safe probe;
4. correct the owning invariant or translation boundary, not only the symptom;
5. retain the regression test and check adjacent supported cases.

Before persistent migration, identify versions and compatibility, build old/boundary/malformed/interrupted fixtures, verify backup and recovery, validate before switching, inject failures at consequential steps, compare counts/IDs/references/checksums/invariants, and retain evidence.

## 7. Final review and handoff

Freeze the task-owned file set. Re-read the request, SRS/SDD scope, and complete changes. Review requirement fit, public compatibility, state/concurrency/lifecycle, cancellation/cleanup/recovery, trust boundaries, persistence/migration/idempotency, dependency direction, unnecessary complexity, negative tests, generated artifacts, and offline packaging.

For high-risk changes, use an independent reviewer when available and authorized. Supply the frozen requirement/design packet, complete task-owned changes, and raw verification evidence. If independent review is unavailable, label the result best-effort.

Handoff in this order:

1. delivered behavior and requirement/design IDs;
2. important source, migration, configuration, and test files;
3. verification commands and actual results;
4. data/deployment/rollback actions;
5. unresolved decisions, unverified behavior, and residual risk.
