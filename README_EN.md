# Axiom

**Axiom Agents: Governed Codex Agent and Skill Stack**

- [Install](#install)
- [Profiles](#profiles)
- [Agent index](#agent-index)
- [Full asset index](docs/asset-index.md)
- [中文](README.md)

## Purpose

Axiom packages the 10 agent definitions and 95 skills required by the AI4PROGRAMMING and AI4SCIENCE global Codex workflows into a publishable, verifiable, and reversible repository. It does not create business projects; it gives a new Codex user the same governance, delivery, research-evidence, and independent-review capabilities.

You can install it with one command, choose the `ai4programming`, `ai4science`, or `all` profile, and use the same flow on Windows, macOS, and Linux. The installer verifies hashes, stages changes, rolls back on failure, keeps timestamped backups, and touches only assets declared by this repository.

## Install

Requirements are Codex CLI or Desktop, Python 3.11+, and Git. Node.js 18+ and `npx` are needed only for Playwright browser verification.

```bash
git clone https://github.com/1993zlorange/Axiomd.git axiom
cd axiom
python scripts/install.py --profile all
```

Windows may use `py -3 .\scripts\install.py --profile all` or `powershell -ExecutionPolicy Bypass -File .\install.ps1 -Profile all`. macOS and Linux may use `./install.sh all`.

Start a new Codex session and verify with:

```bash
python scripts/install.py --profile all --check
python scripts/validate.py
```

The installer writes to `~/.codex/agents/`, `~/.codex/skills/`, and `~/.codex/.axiom-install.json`. It honors `CODEX_HOME`; `--codex-home` can override it.

## Profiles

| Profile | Agents | Core skills | Optional skills | Use case |
| --- | ---: | ---: | ---: | --- |
| `ai4programming` | 5 | 18 | 6 | Governed software delivery |
| `ai4science` | 6 | 79 | 1 | Governed research workflow |
| `all` (default) | 10 | 95 | 0 | Complete bundle |

```bash
python scripts/install.py --profile ai4programming
python scripts/install.py --profile ai4science
python scripts/install.py --profile all
python scripts/install.py --profile ai4programming --include-optional
python scripts/install.py --profile ai4science --prune
```

The two core profiles union to 88 skills. The `all` profile adds five conditional `scienceresearch-*` skills, `pr-ps-09-daily-log-summary`, and `sr-doctoral-research`.

## Agent index

### AI4PROGRAMMING

- `pr-ps-00-project-supervisor` — supervision, registration, quality gates, logs, and closure.
- `pr-pm-00-project-manager` — requirements, PRD/SRS, planning, alignment, release coordination.
- `pr-ar-00-project-architect` — architecture, detailed design, data, migration, and ADRs.
- `pr-en-00-engineer` — approved-scope implementation and verification.
- `pr-qa-00-project-test` — independent functional QA and release verification.

### AI4SCIENCE

- `pr-ps-00-project-supervisor` — shared supervision entry.
- `sr-research-project-lead` — evidence inventory, stage diagnosis, P0/P1, dispatch, and acceptance.
- `sr-principal-investigator` — research questions, claim boundaries, storyline, and cycle decisions.
- `sr-method-builder` — literature, hypotheses, models, methods, and implementation contracts.
- `sr-experimenter` — falsification, resources, data QC, experiments, analysis, and figures.
- `sr-critical-reviewer` — independent challenge, integrity, attribution, and submission risk.

See the [agent-to-skill map](docs/agent-skill-map.md) and [full asset index](docs/asset-index.md).

## Usage

Use your AI4PROGRAMMING or AI4SCIENCE template as the project root. This package installs global agents and skills; project `AGENTS.md` files continue to provide local boundaries.

AI4PROGRAMMING follows supervisor registration, PM requirements, user approval, architecture, engineering, independent QA, and supervisor closure. AI4SCIENCE adds a read-only research-lead assessment, explicit P0/P1 dispatch, per-leaf achievement cards and handoffs, independent critical review, lead acceptance, and supervisor closure.

High-cost work, external writes, deployments, removals, paid services, scientific conclusions, ethics decisions, and publication require explicit human authorization.

## Update, verify, and uninstall

```bash
cd axiom
git pull --ff-only
python scripts/install.py --profile all
python scripts/install.py --profile all --check
python scripts/validate.py
python scripts/install.py --profile all --uninstall
```

Uninstall removes only assets recorded in `.axiom-install.json`, after backing them up. Modified assets require `--force`.

## Plugin form and structure

The repository includes portable plugin metadata and can be consumed as a local plugin or marketplace for skills. Agent TOML files are deployed by `scripts/install.py`; run that script for complete orchestration.

```text
axiom/
├── agents/
├── skills/
├── profiles/
├── scripts/
├── docs/
├── tests/
├── plugin.json
├── .codex-plugin/plugin.json
├── .agents/plugins/marketplace.json
└── manifest.json
```

## Security and contribution

Do not commit secrets, real logs or data, private evidence, or paid-service credentials. Machine-specific paths were removed; target projects must provide an approved coding standard or ask the user to select one. The installer rejects traversal, symlinked assets, and hash mismatches.

Before contributing, run `python scripts/validate.py`. After changing assets, run `python scripts/build_inventory.py`, then validation and unit tests.

## License

[MIT](LICENSE). Distributing this repository does not grant rights to third-party services, datasets, models, or commercial APIs.
