# Implementation-Ready Database Design Standard

Apply this reference whenever an architecture proposal or SDD introduces, owns, queries, changes, migrates, or retires database-backed state. The design is complete only when an pr-en-00-engineer can implement schema, repositories/queries, transactions, migrations, and tests without deciding unspecified business semantics.

## Required inputs and decision gate

Before defining tables, identify:

- governing `FR/DATA/INT/NFR/OPS/CON/QUAL` requirements and use cases;
- authoritative entities, commands, queries, state transitions, retention, audit and recovery rules;
- selected database engine, supported version range, driver/ORM/migration tool, deployment topology and backup mechanism, when already constrained;
- expected access patterns, data volume, concurrency, latency or availability thresholds when approved;
- existing schema, migrations, production data characteristics and compatibility obligations for an existing system.

Do not invent missing product policy. If retention, deletion, uniqueness, tenancy, time semantics, conflict resolution, audit immutability or migration downtime would change user-visible behavior, record a blocking open decision with owner and closure evidence. The design may still describe safe options, but cannot present one as approved.

## Database-wide conventions

State the following once for the database and apply it consistently:

| Concern | Required decision |
| --- | --- |
| Engine and version | Exact engine and supported version/range; enabled extensions/features; reason and approval status. |
| Schema namespace | Database/schema names, ownership boundaries and whether modules share a database or communicate through APIs. |
| Naming | Table, column, key, index, constraint, trigger and migration naming conventions. |
| Identifier strategy | UUID/ULID/integer/natural key generation, storage type, ordering assumptions and collision handling. |
| Time | UTC or offset policy, physical type/precision, clock source and serialization contract. |
| Text and encoding | Encoding, collation, case sensitivity, normalization and maximum lengths. |
| Numeric values | Physical precision/scale, units, rounding and overflow behavior; money must include currency semantics. |
| Boolean/enums | Physical representation, allowed values, forward compatibility and invalid-value behavior. |
| JSON/blob | Schema validation, size limits, canonicalization, indexing, encryption and migration strategy. |
| Secrets and personal data | Classification, encryption/tokenization, access, masking, audit and deletion requirements. |
| Soft delete and audit | Whether permitted, authoritative active-row rule, uniqueness interaction and retention. |
| Schema version | Version storage, migration identity/checksum, ordering and unknown-future-version behavior. |
| Connection policy | Pool size, timeouts, retry rules, transaction defaults, read-only mode and health checks. |

If a convention is inherited from the repository, cite the source. If it is proposed, label it and record the decision owner.

## Logical model and ownership

Provide an ER diagram or relationship table plus a text counterpart. For every relationship specify cardinality, optionality, ownership, lifecycle dependency and delete/update behavior.

| Parent/entity | Child/entity | Cardinality | Optionality | Ownership/lifecycle | Delete/update rule | Requirement |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | 1:N / 1:1 / N:M | required/optional |  | CASCADE/RESTRICT/SET NULL/application saga | DATA-* |

Provide a system ownership matrix:

| Table/view | Owning module | Allowed writers | Allowed readers | Public API/port | Cross-module direct SQL allowed? |
| --- | --- | --- | --- | --- | --- |
|  | MOD-* |  |  | API-* | No, unless an approved exception is recorded |

Every table has one owner. Cross-module mutation goes through the owner's contract unless an ADR explicitly defines shared ownership and its concurrency rules.

## Table and field specification

For every base table, join table, history/audit table, outbox, projection, view or materialized view, state:

| Item | Required content |
| --- | --- |
| Identity | Stable `DATA-DES-*`, exact physical name and object kind. |
| Purpose | Business responsibility and why persistence is required. |
| Ownership | Owning module, writer APIs and reader APIs. |
| Lifecycle | Creation, updates, terminal/archive/delete states, retention and restore. |
| Volume | Expected rows/growth when known; otherwise the decision needed, not an invented number. |
| Requirements | Linked DATA/FR/OPS/CON and qualification IDs. |

Then provide every physical field. Do not use “metadata”, “status”, “config” or “payload” without defining its schema and constraints.

| Column | Physical type | Business meaning | NULL | Default/generated | Validation/CHECK | PK/UNIQUE | FK and actions | Application/DTO mapping | Classification/provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | NOT NULL/NULL | exact expression | exact predicate/range/enum |  | target column; ON DELETE/UPDATE |  |  |

Specify composite keys in column order. Define whether string uniqueness is case-sensitive and how soft-deleted rows affect uniqueness. For derived values, choose one authoritative source: generated column, trigger, application write, view or runtime calculation. Do not require multiple writers to keep the same fact synchronized without a repair rule.

## Constraints, indexes and access patterns

List all primary, foreign, unique, check, exclusion and trigger-enforced constraints with exact names and expressions. Identify invariants that cannot be enforced by the database and the application transaction that enforces them.

Derive indexes from real access paths:

| Query/command ID | API/use case | Operation and predicate | Join/order/page shape | Expected cardinality/threshold | Required index and column order | Lock/write effect | Qualification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QRY-001 | API-* / UC-* | SELECT/UPDATE ... WHERE ... |  | approved value or Open | IDX-* (`a`, `b`) |  | QUAL-* |

For each index state uniqueness, sort direction, included/covering columns, partial predicate or expression where supported, and why the leading-column order matches the query. Note write amplification and storage cost. Do not add indexes “for performance” without a named query or constraint.

Define pagination (cursor/keyset or offset), deterministic order and tie-breaker. Define empty results, not-found, duplicate, conflict and partial result behavior at the API boundary.

## Executable schema definition

Include engine-specific DDL or a mechanically equivalent migration/ORM schema for every object. It must name columns, types, defaults, constraints, keys, references and indexes exactly. Example placeholders are not sufficient in a final SDD.

```sql
-- Migration <stable-id>: <purpose>; dialect=<engine/version>
CREATE TABLE <table_name> (
    <column> <physical_type> <nullability> <default>,
    CONSTRAINT <pk_name> PRIMARY KEY (<columns>),
    CONSTRAINT <uq_name> UNIQUE (<columns>),
    CONSTRAINT <ck_name> CHECK (<predicate>),
    CONSTRAINT <fk_name> FOREIGN KEY (<columns>)
        REFERENCES <parent> (<columns>)
        ON UPDATE <action> ON DELETE <action>
);

CREATE INDEX <index_name> ON <table_name> (<ordered_columns>);
```

When the repository requires migrations through an ORM or migration framework, provide the exact migration operations and model/schema definitions instead of unsupported raw SQL, while preserving the same physical contract. State generated-name behavior if the tool controls constraint names.

## Transaction and concurrency design

Define transactions per user-visible command, not only per table:

| Command/FLOW/API | Reads and writes in order | Transaction boundary | Isolation/lock | Conflict/idempotency rule | Failure point and final state | Retry/compensation | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | BEGIN...COMMIT |  | version/idempotency key |  |  | QUAL-* |

Specify:

- optimistic version columns or pessimistic locks and the exact conflict response;
- uniqueness-race behavior and error translation;
- deadlock/serialization retry owner, maximum attempts and backoff only when requirements permit retry;
- idempotency-key scope, request fingerprint, retention and response replay;
- event/outbox ordering and atomicity relative to business data;
- filesystem/object-store/external-service coordination, staging, checksum, compensation and orphan repair;
- crash points before/after commit and the recovery result visible to users;
- read consistency for replicas, caches, projections or materialized views.

Never claim a distributed operation is atomic without an actual protocol. Preserve `unknown` or `indeterminate` when an external outcome cannot be proven.

## Migration, backfill and rollback

Give every schema change a stable migration ID and deterministic sequence:

| Step | Precondition/version | Exact DDL/DML or framework operation | Backfill/batch/order | Validation checkpoint | Failure recovery | Compatibility impact |
| --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |  |

Define:

- how current and future schema versions are detected and rejected or migrated;
- upgrade path from every supported source version, including empty and populated databases;
- online/offline behavior, locks, estimated resource needs when evidence exists, and maintenance/read-only mode;
- backfill determinism, batch key, restart checkpoint, duplicate handling and null-to-not-null sequence;
- dual-read/dual-write compatibility only when necessary, with removal criteria;
- verification after each step: counts, constraints, checksums, foreign-key/integrity checks and representative queries;
- rollback policy: transactional downgrade, compensating migration, or restore from a named backup/snapshot;
- preservation of old data on conflict or interruption; never use destructive cleanup as an implicit recovery;
- application rollout order and the first/last compatible application and schema versions.

Include executable upgrade verification and, when downgrade is supported, downgrade verification. If downgrade is intentionally unsupported, state why and specify the restore procedure and retained backup.

## Retention, deletion, audit and recovery

For each entity define deletion authority, soft/hard delete, cascade/restrict behavior, retention clock, legal/business holds if required, purge job ownership, retry/idempotency, audit record and user-visible state. Define recovery objectives only when approved.

When rows reference files or external artifacts, specify path/key derivation, staging, content identity/hash, database-to-file commit order, orphan detection, quarantine, restore and garbage collection. A database rollback cannot be described as restoring an already completed external deletion.

Define backup format, consistency mechanism, encryption, location, retention, restore procedure, restore verification and schema compatibility. A backup claim requires a restoration exercise, not only successful archive creation.

## Implementation handoff package

An implementation-ready database section contains:

1. Engine/version and database-wide conventions.
2. ER/relationship and ownership diagrams/tables.
3. Complete object and field dictionaries.
4. Named constraints and index/access-pattern matrix.
5. Exact DDL or migration-framework definitions.
6. Command-level transaction/concurrency/idempotency matrix.
7. Versioned migration/backfill/compatibility/rollback procedure.
8. Retention, deletion, audit, backup, restore and external-artifact coordination.
9. Repository placement: schema/model/migration/query/fixture/test files and ownership.
10. Traceability from requirement to API, table/field, migration and qualification.

Do not hand off unresolved schema blanks to engineers. List each missing product decision as a blocker. Reversible implementation details may be marked as pr-en-00-engineer choice only when they cannot change data semantics, compatibility, security, operations or acceptance.

## Qualification gate

At minimum define tests for:

- clean database creation and every supported upgrade path;
- populated, empty, boundary, invalid, duplicate and referential-integrity cases;
- all unique/check/foreign-key constraints and database-to-domain error mapping;
- concurrent create/update/delete, optimistic conflicts, idempotent replay and lock/deadlock behavior;
- transaction rollback at each injected failure point and crash/restart recovery;
- query plans or measured thresholds for every performance-critical access pattern;
- retention/purge, audit immutability, backup restoration, orphan repair and future-version rejection;
- application compatibility before, during and after rollout.

Each case must name environment, fixture, steps, expected database and user-visible state, threshold/oracle, retained logs/dumps/checksums and `QUAL-*` trace. Passing unit tests alone does not prove migration, restore or production-volume behavior.
