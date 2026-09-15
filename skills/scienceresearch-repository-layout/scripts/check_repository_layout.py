"""Check high-risk ScienceResearch repository placement invariants.

This is intentionally a boundary checker, not a formatter or cleanup command.
It never modifies the repository.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ALLOWED_ROOT_DIRECTORIES = {
    ".git",
    ".codex",
    "backups",
    "data",
    "doc",
    "exports",
    "idea",
    "log",
    "output",
    "release",
    "scripts",
    "src",
    "tests",
}

ALLOWED_ROOT_FILES = {
    ".gitignore",
    "agent.md",
    "pyproject.toml",
    "pytest.ini",
    "README.md",
    "run_cli.ps1",
    "run_web.ps1",
    "serve.py",
}

DATABASE_SUFFIXES = {".db", ".sqlite", ".sqlite3"}
GENERATED_ROOT_SUFFIXES = {
    ".csv",
    ".html",
    ".jpeg",
    ".jpg",
    ".json",
    ".png",
    ".pptx",
    ".trace",
    ".zip",
}
LEGACY_ROOT_PATTERN = re.compile(
    r"^(?:audit|check|final|m\d+|offline|playwright|smoke|tmp|web-smoke)(?:[-_].*)?$",
    re.IGNORECASE,
)
RELEASE_METADATA_PATTERN = re.compile(
    r"^(?:版本说明|发布清单|SHA256SUMS)_\d{8}\.(?:md|txt)$",
    re.IGNORECASE,
)


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def database_path_is_allowed(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    parts = rel.parts
    if not parts:
        return False
    if parts[0] in {"data", "output"}:
        return True
    return len(parts) >= 2 and parts[0] == "tests" and parts[1] == "fixtures"


def check(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not (root / "pyproject.toml").is_file() or not (root / ".codex").is_dir():
        errors.append("target does not look like the scienceresearch repository root")
        return errors, warnings

    for item in sorted(root.iterdir(), key=lambda value: value.name.lower()):
        if item.is_dir():
            if item.name not in ALLOWED_ROOT_DIRECTORIES:
                errors.append(f"unexpected root directory: {item.name}")
            if LEGACY_ROOT_PATTERN.match(item.name):
                errors.append(f"run/cache-like directory must not live at root: {item.name}")
        elif item.name not in ALLOWED_ROOT_FILES and not (
            root.name.lower().startswith("scienceresearch-v")
            and RELEASE_METADATA_PATTERN.match(item.name)
        ):
            errors.append(f"unexpected root file: {item.name}")

        if item.is_file() and (
            item.suffix.lower() in DATABASE_SUFFIXES
            or item.suffix.lower() in GENERATED_ROOT_SUFFIXES
        ):
            errors.append(f"generated/runtime artifact must not live at root: {item.name}")

    required_directories = {".codex", "data", "doc", "idea", "log", "output", "src", "tests"}
    for name in sorted(required_directories):
        if not (root / name).is_dir():
            errors.append(f"required owned directory is missing: {name}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in DATABASE_SUFFIXES and not database_path_is_allowed(path, root):
            errors.append(
                "database outside formal data, isolated output, or immutable test fixtures: "
                + relative(path, root)
            )

    formal_db = root / "data" / "scienceresearch.db"
    if not formal_db.exists():
        warnings.append("formal database is absent: data/scienceresearch.db (valid only for a fresh checkout)")

    archive = root / "output" / "archive"
    if archive.exists() and not archive.is_dir():
        errors.append("output/archive exists but is not a directory")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root (default: current directory)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors, warnings = check(root)

    for message in warnings:
        print(f"WARN: {message}")
    for message in errors:
        print(f"ERROR: {message}")

    if errors:
        print(f"FAIL: {len(errors)} layout error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: repository layout boundary check ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
