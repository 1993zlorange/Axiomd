# Backend quality gate

Apply the approved SDD and `$pr-en-02-senior-engineer`. Use the target repository's approved project-local coding standard. If none exists, ask which standard to apply rather than borrowing another project's examples.

## Architecture and contracts

- requirement and design IDs are named;
- domain/application/interface/adapter ownership follows the approved dependency direction;
- routes parse protocol, call a use case, and present results; they do not duplicate business rules or SQL;
- templates render view models and do not calculate domain state;
- public functions, DTOs, errors, and state transitions are typed and stable;
- GET and query methods are read-only; commands make side effects explicit.

## Data, failure, and security

- validate untrusted input and reject unknown or ambiguous fields where required;
- parameterize values and allowlist dynamic fields;
- resolve and constrain paths to approved roots;
- subprocess calls use argument lists, `shell=False`, timeouts, and retained failure state;
- transactions are atomic; version conflicts, retries, idempotency, cancellation, and rollback are explicit where applicable;
- important files use temporary output, validation, and atomic replacement;
- errors have stable codes and correct HTTP status, preserve recoverable user input, and do not expose secrets, stack traces, SQL, or absolute paths;
- logs use stable messages and structured context without research content or secrets.

## Verification

- feature tests derive from acceptance behavior; defect tests reproduce the reported cause;
- test normal, boundary, invalid, missing prerequisite, dependency failure, conflict, retry/recovery, compatibility, and path-security cases in proportion to risk;
- run focused unit/regression tests, full repository tests, architecture checks, and relevant browser E2E;
- compare page, API, and persisted state after refresh;
- no test writes normal project data or depends on live external services by default;
- exact commands, results, unverified conditions, and residual risks are recorded honestly.
