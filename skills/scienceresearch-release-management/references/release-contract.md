# ScienceResearch release contract

This is the current user-approved default. A later explicit user decision overrides it and must be reflected here if it becomes the new standing standard.

## Package allowlist

The version directory normally contains only:

| Area | Allowed content |
|---|---|
| Runtime source | `src/` |
| Root runtime files | `README.md`, `pyproject.toml`, `.gitignore`, `serve.py`, `run_web.ps1`, `run_cli.ps1` |
| Requirements | `doc/YYYYMMDD-科研工作台需求文档-需求文档.md` |
| Design | `doc/YYYYMMDD-科研工作台架构与设计方案-设计方案.md` |
| User manual | `doc/YYYYMMDD-科研工作台用户手册-用户手册.md` |
| Stage report | `output/YYYYMMDD-科研工作台项目阶段汇报-项目阶段汇报.html` |
| Required visual assets | Only PNG/JPG/WebP/GIF/SVG files actually referenced by the packaged manual or report, at paths that make the original relative links resolve |

The standalone `doc/科研工作台项目架构_<YYYYMMDD>.md` is not part of the current release package.

## External release records

Keep these under `release/`, beside rather than inside the version directory:

- `YYYYMMDD-版本说明-版本说明.md`;
- `YYYYMMDD-发布索引-发布索引.md`;
- `<project>-v<version>_<YYYYMMDD>.zip`.

Release notes must first read the three project logs and state the functional increment, packaging-only changes, verification evidence, and remaining baseline/acceptance limitations.

## Default exclusions

- `.codex/`, Agent definitions, Skill packages;
- `tests/`, `pytest.ini`, test fixtures and traces;
- `scripts/` unless a specific runtime script is explicitly required;
- `idea/`, `log/`, ADRs, Agent manuals and internal governance documents;
- the standalone project-architecture document;
- the separate requirement-chain evidence-book HTML;
- formal `data/`, databases, backups, exports and credentials;
- browser profiles, caches, `__pycache__`, temporary runs and unrelated historical evidence;
- package-internal version notes, release lists and checksum manifests unless explicitly requested.

## README acceptance

A new Windows user with Python 3.12+ should be able to:

1. unpack the ZIP into a writable path;
2. verify `python --version`;
3. run `run_web.ps1`, including a process-scoped PowerShell-policy workaround when needed;
4. open `http://127.0.0.1:8765/`;
5. stop with `Ctrl+C`;
6. optionally run `run_cli.ps1 health` and `run_cli.ps1 catalog`;
7. understand first-run data creation and common failure remedies.

## Asset closure check

For each packaged Markdown file, extract image targets shaped like `![...](path)`. For each packaged HTML file, extract local image paths from `img src` and any local image-bearing links. Ignore `data:` URLs and remote `http/https` assets only when the document intentionally embeds or fetches them. Resolve the remaining target against the containing document's directory and require it to remain inside the package and exist as a regular image file.

The current manual uses `../output/pm-chain-<date>/browser/...`; the current report uses `pm-chain-<date>/browser/...` and `playwright/...`. Preserve those relationships rather than relocating images into `doc/`.

## Verification checklist

- package files equal the approved allowlist plus the closed image dependency set;
- every document except `README.md` follows the approved date-suffix naming convention;
- README contains functionality and new-environment instructions only;
- all local Markdown/HTML image references resolve inside the package;
- required source compiles without leaving bytecode in the package;
- runtime smoke checks do not leave `data/`, databases, backups, exports or caches in the package;
- extracted ZIP matches the version directory by relative path, file count, size and hash;
- repository layout check passes;
- isolated extraction/run directory is removed after verification;
- demand, engineering and test logs contain one timestamped paragraph each;
- release notes and index match the final archive, not an earlier attempt.
