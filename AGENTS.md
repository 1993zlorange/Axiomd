# Axiom Agents repository instructions

This repository is a redistributable Codex asset package. Keep the source repository portable: do not add machine-specific absolute paths, credentials, private project evidence, generated logs, or large binary artifacts.

Before changing agents or skills:

1. Run `python scripts/validate.py` and record the baseline result.
2. Explain the behavior change, affected profiles, and compatibility risk.
3. Keep agent names, skill directory names, and profile membership consistent.
4. Regenerate `manifest.json` and `docs/asset-index.md` with `python scripts/build_inventory.py`.
5. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.
6. Write every commit message as a Chinese `类型: 说明` summary (for example `修复: ...`); complex changes add a body listing the change reason, affected profiles/assets, and verification commands with actual results.

The installer is safety-critical. Preserve path validation, staged activation, backups, verification, and uninstall behavior.

## PR/SR interaction guides

The PR/SR skill-local `AGENTS.md` files are generated from `docs/pr-sr-interaction-standard.md`. To update them, edit that canonical file, run `python scripts/generate_pr_sr_interaction_guides.py`, then run `python scripts/generate_pr_sr_interaction_guides.py --check`. Do not edit individual generated copies directly.

## SR record templates

SR-01 through SR-68 use plain-language achievement-card templates generated from `skills/sr-research-shared/references/record-templates/`. To update them, edit the base/aspect/special/handoff module, run `python scripts/generate_sr_record_templates.py`, then run `python scripts/generate_sr_record_templates.py --check`. Do not edit the 68 generated local templates directly.

## PR management document standard

PR management documents follow `skills/pr-ps-00-project-supervision/references/20260929-管理文档写作标准-管理规范.md`. Requirement and log templates are A-level; supervision, change, and reflection templates are B-level; quality and cost templates are C-level. Use `skills/pr-ps-00-project-supervision/scripts/ps_01_create_governance_document.py` to generate project documents and validate them with `skills/pr-ps-00-project-supervision/scripts/ps_04_validate_management_document.py`.
