#!/usr/bin/env python3
"""Collect objective traceability signals for a project-alignment audit.

This script deliberately does not decide whether a project is aligned. A missing
textual requirement ID in code is only a signal; behavioral inspection remains
necessary.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


ID_PREFIXES = ("FR", "DATA", "INT", "NFR", "OPS", "CON", "ENV", "UC", "QUAL")
ID_PATTERN = re.compile(r"\b(?:" + "|".join(ID_PREFIXES) + r")-\d{3}\b")
DEFINED_ID_PATTERN = re.compile(
    r"^\s*\|\s*((?:" + "|".join(ID_PREFIXES) + r")-\d{3})\s*\|"
)
PLACEHOLDER_PATTERN = re.compile(
    r"\b(?:TODO|FIXME|HACK|XXX)\b|NotImplementedError|UnsupportedOperationException",
    re.IGNORECASE,
)
TEXT_EXTENSIONS = {
    ".py",
    ".pyi",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".kt",
    ".kts",
    ".cs",
    ".cpp",
    ".cc",
    ".cxx",
    ".c",
    ".h",
    ".hpp",
    ".rs",
    ".go",
    ".rb",
    ".php",
    ".sql",
    ".sh",
    ".ps1",
    ".toml",
    ".yaml",
    ".yml",
    ".json",
    ".md",
    ".html",
    ".css",
}
IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
    "coverage",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect requirements/design/source/test alignment signals as JSON."
    )
    parser.add_argument("--root", type=Path, required=True, help="Project root")
    parser.add_argument(
        "--requirements",
        type=Path,
        help="Requirements document; relative paths resolve from --root",
    )
    parser.add_argument(
        "--design",
        type=Path,
        action="append",
        default=[],
        help="Architecture/design document; repeat for multiple files",
    )
    parser.add_argument(
        "--source-root",
        action="append",
        default=["src"],
        help="Source subtree relative to --root; repeat as needed",
    )
    parser.add_argument(
        "--test-root",
        action="append",
        default=["tests"],
        help="Test subtree relative to --root; repeat as needed",
    )
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    return parser.parse_args()


def resolve_from_root(root: Path, value: Path) -> Path:
    return value if value.is_absolute() else root / value


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def iter_text_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return
    if root.is_file():
        if root.suffix.lower() in TEXT_EXTENSIONS:
            yield root
        return
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        yield path


def discover_requirements(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in iter_text_files(root):
        lower = path.name.lower()
        if path.suffix.lower() == ".md" and (
            "需求" in path.name or "requirement" in lower or "srs" in lower
        ):
            candidates.append(path)
    return sorted(set(candidates))


def discover_design(root: Path, requirements: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in iter_text_files(root):
        if path == requirements or path.suffix.lower() != ".md":
            continue
        lower = path.name.lower()
        if (
            "架构" in path.name
            or "设计" in path.name
            or "architecture" in lower
            or "design" in lower
            or "sdd" in lower
        ):
            candidates.append(path)
    return sorted(set(candidates))


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata


def document_record(root: Path, path: Path) -> dict[str, object]:
    text = read_text(path)
    meta = parse_frontmatter(text)
    return {
        "path": path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path),
        "exists": path.exists(),
        "document_id": meta.get("document_id"),
        "version": meta.get("version"),
        "status": meta.get("status"),
        "date": meta.get("date"),
        "related_srs": meta.get("related_srs"),
        "related_architecture": meta.get("related_architecture"),
    }


def count_ids(paths: Iterable[Path], ids: list[str]) -> dict[str, int]:
    counts: Counter[str] = Counter()
    wanted = set(ids)
    for path in paths:
        try:
            text = read_text(path)
        except OSError:
            continue
        for match in ID_PATTERN.findall(text):
            if match in wanted:
                counts[match] += 1
    return {item: counts[item] for item in ids}


def placeholder_findings(root: Path, source_paths: Iterable[Path]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for path in source_paths:
        try:
            lines = read_text(path).splitlines()
        except OSError:
            continue
        for line_number, line in enumerate(lines, start=1):
            match = PLACEHOLDER_PATTERN.search(line)
            if not match:
                continue
            findings.append(
                {
                    "path": path.relative_to(root).as_posix()
                    if path.is_relative_to(root)
                    else str(path),
                    "line": line_number,
                    "marker": match.group(0),
                    "text": line.strip()[:240],
                }
            )
    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"error: project root is not a directory: {root}", file=sys.stderr)
        return 2

    if args.requirements:
        requirements = resolve_from_root(root, args.requirements).resolve()
        if not requirements.is_file():
            print(f"error: requirements file not found: {requirements}", file=sys.stderr)
            return 2
    else:
        candidates = discover_requirements(root)
        if len(candidates) != 1:
            print(
                "error: could not select one requirements document; pass --requirements. "
                f"Candidates: {[p.relative_to(root).as_posix() for p in candidates]}",
                file=sys.stderr,
            )
            return 2
        requirements = candidates[0]

    if args.design:
        design_paths = [resolve_from_root(root, item).resolve() for item in args.design]
        missing = [str(path) for path in design_paths if not path.is_file()]
        if missing:
            print(f"error: design file(s) not found: {missing}", file=sys.stderr)
            return 2
    else:
        design_paths = discover_design(root, requirements)

    requirements_text = read_text(requirements)
    requirement_ids: list[str] = []
    for line in requirements_text.splitlines():
        match = DEFINED_ID_PATTERN.match(line)
        if match and match.group(1) not in requirement_ids:
            requirement_ids.append(match.group(1))

    design_files = [path for doc in design_paths for path in iter_text_files(doc)]
    source_roots = [root / item for item in args.source_root]
    test_roots = [root / item for item in args.test_root]
    source_files = [path for subtree in source_roots for path in iter_text_files(subtree)]
    test_files = [path for subtree in test_roots for path in iter_text_files(subtree)]

    design_counts = count_ids(design_files, requirement_ids)
    source_counts = count_ids(source_files, requirement_ids)
    test_counts = count_ids(test_files, requirement_ids)

    traces = {
        req_id: {
            "design_references": design_counts[req_id],
            "source_references": source_counts[req_id],
            "test_references": test_counts[req_id],
        }
        for req_id in requirement_ids
    }

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project_root": str(root),
        "documents": {
            "requirements": document_record(root, requirements),
            "design": [document_record(root, path) for path in design_paths],
        },
        "requirements": {
            "defined_count": len(requirement_ids),
            "ids": requirement_ids,
        },
        "trace_signals": traces,
        "summary": {
            "without_design_reference": [
                item for item in requirement_ids if design_counts[item] == 0
            ],
            "without_source_reference": [
                item for item in requirement_ids if source_counts[item] == 0
            ],
            "without_test_reference": [
                item for item in requirement_ids if test_counts[item] == 0
            ],
            "production_placeholders": placeholder_findings(root, source_files),
            "source_files_scanned": len(source_files),
            "test_files_scanned": len(test_files),
        },
        "interpretation_notes": [
            "A textual ID reference is a traceability signal, not proof of correct behavior.",
            "A missing source/test ID reference is not by itself a drift finding; inspect behavior and qualification evidence.",
            "Placeholder hits require contextual review because some markers may be intentional domain text.",
        ],
    }

    encoded = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        output = resolve_from_root(root, args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded + "\n", encoding="utf-8")
    else:
        print(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
