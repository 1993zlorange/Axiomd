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
