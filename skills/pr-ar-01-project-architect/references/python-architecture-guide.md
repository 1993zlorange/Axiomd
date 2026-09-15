# Python Architecture Decision Guide

Use this guide to make proportional, evidence-based architecture decisions. It is guidance, not a mandatory stack.

## Select the system shape

| Conditions | Starting point | Upgrade trigger |
|---|---|---|
| One operator, one workflow, local files | Script or CLI with tested modules | Multiple workflows, shared state, or a stable external interface |
| Small web/API tool, one team, one database | Layered monolith | Domain boundaries become difficult to change independently |
| Several cohesive domains, one deployment cadence | Modular monolith | Proven need for independent deployability, scaling, or isolation |
| Complex domain with volatile infrastructure | Ports and adapters / clean boundaries | Keep it; reduce ceremony where interfaces have only one stable implementation |
| Independent ownership and operational requirements | Services | Consolidate when operational cost exceeds the isolation benefit |

Default to a modular monolith for a new Python business, data, or research application unless evidence supports another shape.

## Choose tools by capability

| Need | Common choice | Decision note |
|---|---|---|
| Packaging and dependencies | `pyproject.toml`; project-standard installer | Lock applications; keep libraries compatible within a declared range |
| HTTP API | FastAPI or the repository's existing framework | Use OpenAPI and boundary validation; do not leak ORM models |
| CLI | `argparse` for minimal dependencies; Typer when richer UX is justified | Keep command handlers thin |
| Validation/settings | Pydantic at I/O boundaries; `pydantic-settings` or environment adapter | Domain objects need not inherit framework models |
| Relational persistence | SQLAlchemy and Alembic | Own transactions in the application boundary; test migrations |
| Local/offline persistence | SQLite when concurrency and durability constraints fit | Define file location, backup, locking, and schema migration |
| Production relational DB | PostgreSQL when its operational cost is justified | Decide from workload and hosting constraints |
| Background work | In-process jobs first; queue only for durability, isolation, or scale | Define idempotency, retries, timeouts, poison-job behavior |
| Testing | pytest with unit, integration, contract, and architecture suites | Test behavior and boundaries, not private implementation |
| Quality | Ruff plus the project's type checker | Enforce in CI and keep suppressions explicit |
| Observability | Structured logs, metrics, traces where needed | Correlation IDs and error taxonomy at boundaries |

Do not select a library solely because it appears in this table. Prefer the repository's established, maintained equivalent.

## Repository layouts

For a small tool, keep the layout small:

```text
project/
  pyproject.toml
  src/tool_name/
    __init__.py
    cli.py
    service.py
    models.py
  tests/
```

For a domain-oriented application:

```text
project/
  pyproject.toml
  src/app/
    domain/          # business rules and domain types
    application/     # use cases, ports, transactions
    adapters/        # HTTP, CLI, files, external services
    infrastructure/  # database, queue, runtime implementations
    bootstrap.py     # composition root
  tests/
    unit/
    integration/
    contract/
    architecture/
  docs/
    architecture/
    adr/
```

For a modular monolith, repeat the domain/application/adapters grouping within meaningful bounded modules, not for every entity. Shared code must have a narrow, documented purpose.

## Dependency rules

- Domain code depends on the Python standard library and explicitly approved domain libraries.
- Application code may depend on domain code and stable port protocols.
- Adapters implement ports and translate transport, database, or vendor models.
- Infrastructure is wired at one composition root.
- Cross-module calls use public application interfaces, not another module's tables or internals.
- Shared utility packages must not become an unowned dumping ground.

Use `Protocol` or abstract base classes when substitutability is required. A plain callable or concrete dependency is preferable when there is no real variation.

## Contracts and errors

- Version external schemas and document compatibility policy.
- Validate at trust boundaries; preserve domain invariants inside the domain.
- Define success, validation, authorization, conflict, retryable, and internal-error behavior.
- Make idempotency explicit for retried writes and background jobs.
- Use stable identifiers; do not expose storage-specific keys without intent.
- Place pagination, filtering, units, timestamps, encoding, and nullability in contracts.

## Sync, async, and parallel work

Choose `asyncio` when a request coordinates many concurrent non-blocking I/O operations and the dependency stack supports async end to end. Keep synchronous code for CPU-heavy or straightforward blocking workflows. Move sustained CPU work to separate processes or workers. Measure before adding caching or concurrency.

## Data and research systems

- Keep immutable raw inputs separate from derived datasets.
- Store a manifest with source, checksum, schema version, units, coordinate system, license, and processing history.
- Make pipelines restartable and deterministic where possible.
- Version feature definitions, models, parameters, and evaluation datasets.
- Treat large binary artifacts separately from transactional metadata.
- Define incomplete-run cleanup and artifact retention.

## Architecture fitness functions

Automate important design promises. Useful Python checks include import-boundary rules, dependency-cycle checks, schema compatibility, migration tests, offline execution, reproducible pipeline fixtures, resource budgets, and end-to-end smoke tests. A rule that matters but is never checked will eventually drift.
