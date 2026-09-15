---
name: scienceresearch-release-management
description: Prepare, correct, verify, and document versioned ScienceResearch release packages from an explicitly approved delivery scope. Use when the project manager is asked to publish, repackage, trim, add required documentation assets, or revise a release README; do not infer a release or include internal project material without authorization.
---

# ScienceResearch Release Management

For retained release notes or a release index, start from [assets/release-document-template.md](assets/release-document-template.md). Name each document `YYYYMMDD-内容简述-文档类型.扩展名` and keep the immutable package version separate from the production date.

Own the release decision, package boundary, release notes, and acceptance evidence. A release is a user-facing delivery snapshot, not a copy of the repository.

## Entry gate

1. Read `pyproject.toml`, the current release directory, `log/demand_log.md`, `log/engineer_log.md`, and `log/test_log.md` before describing the version increment.
2. Read the user's latest approved include/exclude list. Treat it as authoritative when older README, ADR, SDD, index, or prior release text conflicts with it; record the conflict instead of silently following stale guidance.
3. Confirm the version, date, target paths, and whether the request creates a new immutable version or explicitly corrects an existing package. Never overwrite an already delivered version merely because a file changed.
4. Use `$scienceresearch-repository-layout` for every created, copied, moved, generated, or deleted artifact and state a compact Placement Plan.
5. If the package boundary is materially ambiguous, ask one release-scope question before packaging. Do not interpret “source code” as permission to include tests, Agent/Skill definitions, logs, formal data, caches, or historical evidence.

Read [references/release-contract.md](references/release-contract.md) for the current approved package contract, README contract, image dependency rules, and verification checklist.

## Release workflow

### 1. Establish the release delta

- Summarize delivered functional changes from the three project logs; do not reconstruct the delta from memory or only from the current code tree.
- Separate product functionality, documentation changes, packaging changes, test evidence, limitations, and unapproved baseline status.
- Keep SRS `draft`, SDD/ARCH `proposed`, manual-review gates, and other qualification limits honest unless evidence shows approval.

### 2. Build from an allowlist

- Create the version directory under `release/` and copy only the approved files and directories.
- Preserve source-relative paths needed by runtime imports and document links.
- Put the release notes and release index beside the version directory unless the user explicitly requests them inside the package.
- Never copy formal `data/`, backups, exports, credentials, caches, browser profiles, logs, unrelated test runs, or the repository's `.codex/` into the user package.
- Do not include the standalone project-architecture document under the current contract; its approved content is already represented by the design solution delivered to users.

### 3. Make the README usable on a new machine

The package `README.md` contains only:

- what the software does;
- supported runtime prerequisites;
- unpack, install, start, access, stop, and optional CLI commands;
- first-run writable-data behavior;
- concise troubleshooting for Python/PATH, PowerShell policy, port collision, URL, permissions, and initial readiness.

Exclude repository governance, Agent/Skill instructions, internal test history, development workflow, and maintainer-only directory rules. Validate commands against the packaged entry points and do not claim dependencies that are absent from `pyproject.toml` or source evidence.

### 4. Close document asset dependencies

- Parse every packaged Markdown image target and every packaged HTML `img src` or local image link.
- Resolve each path relative to the document that contains it, not relative to the repository root.
- Copy only referenced images and the directories required to preserve those paths. Deduplicate repeated references.
- Reject missing, absolute-local, escaping, or stale image paths. A report whose text opens but images are broken is not a complete release.
- Do not include an entire evidence directory merely because one image is referenced.

### 5. Verify before handoff

- Verify the package allowlist and explicit exclusions.
- Verify document date naming, README scope, local links, image signatures, and image existence.
- Compile or smoke-test from an isolated extraction with bytecode and runtime data directed outside the immutable package; clean the run directory afterward.
- Recreate the ZIP, extract it into `output/runs/<run-id>/`, and compare file paths, counts, sizes, and hashes with the version directory.
- Run the repository layout checker and confirm no generated database, `__pycache__`, cache, or test output remains in the package.
- Record the ZIP SHA-256 in the handoff or release index. Do not put a checksum manifest inside the package unless the approved scope asks for it.

### 6. Record and hand off

- Update the external version notes with the log-derived functional delta, final package boundary, verification result, and known limitations.
- Update the release index with version, date, directory, ZIP, final scope, file count, and verification status.
- Append one timestamped paragraph to `log/demand_log.md` for the release decision, `log/engineer_log.md` for packaging changes, and `log/test_log.md` for verification.
- Lead the handoff with the version and clickable paths, then list exact contents, exclusions, file count, link result, test result, SHA-256, and any first-run limitation.

## Stop conditions

Do not declare the release complete while any required image is missing, the ZIP differs from the version directory, an unapproved file is present, the README cannot guide a new user to a running service, generated runtime state remains in the package, or the release notes claim approval/test evidence not established by the logs.
