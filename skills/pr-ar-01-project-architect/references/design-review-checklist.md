# Architecture Design Review Checklist

Use only relevant checks. Report review findings by severity and include evidence, impact, recommendation, and verification.

## Intent and evidence

- Are document ID/version/status, governing SRS/architecture baselines, approval record, change history, and decision owner consistent?
- Are goals, non-goals, constraints, assumptions, and decision owners explicit?
- Are key requirements traceable to architecture decisions and acceptance gates?
- Are quality attributes expressed as measurable scenarios?
- Does the current-state description match repository and runtime evidence?
- Are current implementation facts, target design, recommendations, and approved constraints visibly distinguished in the technology-stack description?

## Boundaries and dependencies

- Does each module or service have one clear responsibility and owner?
- Are dependency direction and allowed cross-boundary calls explicit?
- Are domain rules insulated from transport, persistence, and vendor details where useful?
- Are abstractions justified by volatility, substitution, testing, or ownership?
- Is shared code narrow and governed?

## Interfaces and data

- Does every SRS module/submodule map to an exact design interface function or a justified internal-only contract, with no duplicate ownership or unmapped submodule?
- Are direct, combined, and internal-adaptation mappings labeled honestly, without using a facade, shell, or bridge to hide a missing domain interface?
- Does every mapped API reference resolve to a unique function table with function name/description/input/output and the applicable error, execution, compatibility, and verification constraints?
- Are API, event, file, job, and error contracts versioned and testable?
- Are units, coordinate systems, timestamps, encodings, nullability, and identifiers defined?
- Are transactions, consistency, idempotency, retries, and duplicate handling explicit?
- Are schema ownership, migrations, retention, backup, restore, provenance, and deletion covered?
- For every database-backed module, are engine/version conventions, complete physical fields, relationship cardinalities, named PK/FK/UNIQUE/CHECK constraints, and access-pattern-derived indexes specified?
- Does each database object have executable or mechanically translatable DDL/migration definitions, and does each user-visible command have an operation-level transaction, locking, conflict, idempotency, failure and recovery contract?
- Are migration/backfill steps deterministic and restartable, with compatibility order, validation checkpoints, rollback or backup-restore policy, and positive/negative/concurrency/migration qualification cases?
- Can an pr-en-00-engineer implement the schema, queries, transactions and migrations without inventing data semantics? If not, are the missing decisions explicitly blocking rather than delegated implicitly?

## Runtime and operations

- Is the deployment topology consistent with the architecture diagrams?
- Are configuration, secrets, health checks, logging, metrics, traces, and alert ownership defined?
- Are timeouts, rate limits, resource limits, failure isolation, graceful shutdown, and recovery addressed?
- For offline systems, are assets bundled and all network dependencies removable?

## Security and privacy

- Are trust boundaries, authentication, authorization, least privilege, and input validation visible?
- Are sensitive data classification, encryption, audit, retention, and deletion requirements addressed?
- Are dependency and supply-chain risks managed?
- Does failure behavior avoid exposing secrets or internal details?

## Delivery and evolution

- Can the architecture be built and verified incrementally?
- Are rollout, migration, backward compatibility, rollback, and decommissioning defined?
- Do tests cover domain behavior, boundaries, contracts, migrations, and critical workflows?
- Are important architecture rules automated as fitness functions?
- Are alternatives, trade-offs, reversal costs, revisit triggers, and unresolved decisions documented?

## Review outcome

Use these severities:

- **Critical**: design cannot meet a mandatory requirement or creates an unacceptable security/data-loss risk.
- **High**: likely production failure, major rework, or unowned cross-system risk.
- **Medium**: material maintainability, operability, or testability weakness.
- **Low**: localized improvement with limited impact.

A design is ready only when critical and high findings are resolved or explicitly accepted by the accountable decision owner.
