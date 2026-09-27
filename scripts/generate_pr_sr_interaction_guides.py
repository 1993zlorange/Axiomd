#!/usr/bin/env python3
"""Generate local AGENTS.md guides for every PR/SR skill.

The canonical text lives in docs/pr-sr-interaction-standard.md. Local copies are
self-contained because installed skills do not always have the repository docs
directory available.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "docs" / "pr-sr-interaction-standard.md"
REFERENCE = "Before any user-facing reply, read and apply [AGENTS.md](AGENTS.md). These rules govern chat wording; they do not override professional methods, safety requirements, or approved output templates."


def skill_directories() -> list[Path]:
    return sorted(
        path
        for path in (ROOT / "skills").iterdir()
        if path.is_dir()
        and path.name.startswith(("pr-", "sr-"))
        and (path / "SKILL.md").is_file()
    )


def insert_reference(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if REFERENCE in text:
        return False
    lines = text.splitlines()
    body_start = 0
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                body_start = index + 1
                break
        else:
            raise ValueError(f"missing closed frontmatter: {path}")
    insertion = body_start
    while insertion < len(lines) and not lines[insertion].strip():
        insertion += 1
    lines.insert(insertion, REFERENCE)
    lines.insert(insertion + 1, "")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return True


def write_guides() -> tuple[int, int]:
    canonical = CANONICAL.read_text(encoding="utf-8")
    directories = skill_directories()
    changed_guides = 0
    changed_skills = 0
    for directory in directories:
        target = directory / "AGENTS.md"
        if not target.is_file() or target.read_text(encoding="utf-8") != canonical:
            target.write_text(canonical, encoding="utf-8", newline="\n")
            changed_guides += 1
        if insert_reference(directory / "SKILL.md"):
            changed_skills += 1
    return changed_guides, changed_skills


def check() -> int:
    canonical = CANONICAL.read_text(encoding="utf-8")
    failures: list[str] = []
    directories = skill_directories()
    if not directories:
        failures.append("no PR/SR skills found")
    for directory in directories:
        target = directory / "AGENTS.md"
        if not target.is_file():
            failures.append(f"missing {target.relative_to(ROOT)}")
        elif target.read_text(encoding="utf-8") != canonical:
            failures.append(f"outdated {target.relative_to(ROOT)}")
        skill = directory / "SKILL.md"
        if REFERENCE not in skill.read_text(encoding="utf-8"):
            failures.append(f"missing AGENTS reference in {skill.relative_to(ROOT)}")
    if failures:
        for failure in failures:
            print(f"ERROR {failure}", file=sys.stderr)
        return 1
    print(f"PASS: {len(directories)} PR/SR interaction guides match the canonical template")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check without writing")
    args = parser.parse_args()
    if args.check:
        return check()
    guides, skills = write_guides()
    print(f"updated AGENTS.md files: {guides}")
    print(f"updated SKILL.md references: {skills}")
    print(f"PR/SR skills: {len(skill_directories())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
