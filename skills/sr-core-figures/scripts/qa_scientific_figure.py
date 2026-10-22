#!/usr/bin/env python3
"""Check the SR-53 scientific-figure contract and nonblank export files."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = (
    "figure_id",
    "figure_version",
    "claim",
    "evidence_role",
    "data_source",
    "source_data_sha256",
    "sample_size",
    "comparison",
    "encoding",
    "units",
    "uncertainty",
    "legend",
    "panel_logic",
    "boundary",
    "caption",
    "export_status",
    "export_files",
)
PLACEHOLDER = re.compile(r"<[^>]*>|TBD|TODO|N/A\b", re.IGNORECASE)
LOCAL_PATH = re.compile(r"(?:^|[\s\"'])[(?:]?[A-Za-z]:[\\/]", re.IGNORECASE)
SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")


def clean_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value


def parse_scalar_list(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [clean_value(item) for item in inner.split(",") if item.strip()] if inner else []
    return [clean_value(value)]


def parse_contract(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```yaml\s*\n(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    if not blocks:
        raise ValueError("no yaml fenced block found")
    blocks = [block for block in blocks if "claim:" in block] or blocks
    data: dict[str, Any] = {}
    current_list: str | None = None
    for raw_line in blocks[0].splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.lstrip().startswith("- "):
            if current_list is None:
                raise ValueError(f"list item without a field: {raw_line!r}")
            data[current_list].append(clean_value(line.lstrip()[2:]))
            continue
        if line.startswith((" ", "\t")):
            # Only simple lists are used by the template; unknown nested text is ignored.
            continue
        if ":" not in line:
            raise ValueError(f"unsupported yaml line: {raw_line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Za-z0-9_]+", key):
            raise ValueError(f"unsupported field name: {key!r}")
        scalar = clean_value(value)
        data[key] = parse_scalar_list(value)
        current_list = key if not scalar or scalar.startswith("[") else None
    return data


def as_values(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value]
    return [str(value).strip()]


def has_content(value: Any) -> bool:
    return any(item and not PLACEHOLDER.search(item) for item in as_values(value))


def check_file_signature(path: Path) -> str | None:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        return f"cannot read export {path.name}: {exc}"
    if not raw:
        return f"export is blank: {path.name}"
    suffix = path.suffix.lower()
    if suffix == ".svg":
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            return f"SVG is not UTF-8 text: {path.name}"
        if "<svg" not in text.lower() or "</svg>" not in text.lower():
            return f"SVG structure is incomplete: {path.name}"
    elif suffix == ".pdf":
        if not raw.startswith(b"%PDF-") or b"%%EOF" not in raw[-2048:]:
            return f"PDF structure is incomplete: {path.name}"
    elif suffix == ".png" and not raw.startswith(b"\x89PNG\r\n\x1a\n"):
        return f"PNG signature is invalid: {path.name}"
    elif suffix in {".jpg", ".jpeg"} and not raw.startswith(b"\xff\xd8\xff"):
        return f"JPEG signature is invalid: {path.name}"
    return None


def validate(path: Path, figure: Path | None) -> tuple[list[str], list[str], int]:
    try:
        data = parse_contract(path)
    except (OSError, ValueError) as exc:
        return [f"cannot parse contract: {exc}"], [], 0

    errors: list[str] = []
    warnings: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"missing field: {field}")
        elif not has_content(data[field]) and not (
            field == "export_files" and as_values(data.get("export_status")) == ["blocked"]
        ):
            errors.append(f"empty or placeholder field: {field}")

    for field in ("data_source",):
        for value in as_values(data.get(field)):
            if LOCAL_PATH.search(value):
                errors.append(f"{field} contains a machine-specific absolute path")

    style_exemplars = as_values(data.get("style_exemplars"))
    for value in style_exemplars:
        if PLACEHOLDER.search(value):
            errors.append("style_exemplars still contains a placeholder")
        elif LOCAL_PATH.search(value):
            errors.append("style_exemplars contains a machine-specific absolute path")
        elif not value.lower().endswith(".png"):
            errors.append("style_exemplars must reference PNG files in this template")

    hashes = [item for item in as_values(data.get("source_data_sha256"))]
    if hashes and (len(hashes) != len(data.get("source_data_sha256", [])) or not all(SHA256.fullmatch(item) for item in hashes)):
        errors.append("source_data_sha256 must contain one or more 64-character hexadecimal SHA-256 values")

    export_status = as_values(data.get("export_status"))
    if export_status and export_status[0] not in {"passed", "blocked"}:
        errors.append("export_status must be passed or blocked")
    export_files = as_values(data.get("export_files"))
    if export_status == ["passed"]:
        if not export_files:
            errors.append("passed export requires at least one export_files entry")
        for name in export_files:
            candidate = Path(name)
            export_path = candidate if candidate.is_absolute() else path.parent / candidate
            if LOCAL_PATH.search(name):
                errors.append("export_files contains a machine-specific absolute path")
                continue
            if not export_path.is_file():
                errors.append(f"export file does not exist: {name}")
            else:
                issue = check_file_signature(export_path)
                if issue:
                    errors.append(issue)
    elif export_status == ["blocked"] and not has_content(data.get("export_blockage_reason")):
        errors.append("blocked export requires export_blockage_reason")

    if figure is not None:
        if not figure.is_file():
            errors.append(f"figure file does not exist: {figure}")
        else:
            issue = check_file_signature(figure)
            if issue:
                errors.append(issue)

    review = as_values(data.get("advisor_review"))
    if review and review[0] not in {"pending", "accepted", "revise"}:
        errors.append("advisor_review must be pending, accepted, or revise")

    panel_logic = " ".join(as_values(data.get("panel_logic"))).lower()
    if panel_logic and "single" not in panel_logic and "panel" not in panel_logic:
        warnings.append("panel_logic does not state a single panel or a panel comparison reason")

    uncertainty = " ".join(as_values(data.get("uncertainty"))).lower()
    allowed = ("range", "iqr", "standard deviation", "confidence interval", "not applicable")
    if uncertainty and not any(word in uncertainty for word in allowed):
        warnings.append("uncertainty does not name range, IQR, standard deviation, confidence interval, or not applicable")

    return errors, warnings, len(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path, help="Markdown figure contract with a yaml block")
    parser.add_argument("--figure", type=Path, help="Optional exported figure to check for a nonblank signature")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as blocking")
    args = parser.parse_args()
    if not args.contract.is_file():
        print(f"ERROR input contract does not exist: {args.contract}")
        return 2
    errors, warnings, field_count = validate(args.contract, args.figure)
    print(f"contract={args.contract}")
    print(f"fields={field_count}")
    print(f"errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print(f"ERROR {item}")
    for item in warnings:
        print(f"WARN {item}")
    if errors:
        return 2
    if warnings:
        print("QA=warnings")
        return 3 if args.strict else 0
    print("QA=pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
