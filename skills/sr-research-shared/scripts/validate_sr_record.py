#!/usr/bin/env python3
"""Validate plain-language SR achievement cards and workflow handoffs.

The checker reviews structure and wording only. It cannot decide whether a
scientific claim is true; that judgment remains with the researcher and, where
required, the named human reviewer.

Exit codes:
  0 = pass, or warnings without --strict
  1 = warnings with --strict
  2 = missing file or blocking structural/language errors
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


COMMON_REQUIRED = [
    "# 一句话结论",
    "## 1. 原来遇到什么问题",
    "## 2. 问题原因分析",
    "## 3. 当时有哪些可能做法",
    "推荐方案及原因",
    "## 4. 本阶段做了什么",
    "## 5. 遇到的困难和处理方式",
    "## 6. 当前结果",
    "## 7. 本阶段没有解决的问题",
    "## 8. 下一步计划",
    "## 附录A：支撑材料",
    "## 附录B：系统记录",
]
CARD_REQUIRED = ["## 9. 专业补充"]
HANDOFF_REQUIRED = [
    "# 交接结论",
    "## 0. 交接信息",
    "## 9. 本次产生或更新的成果卡",
    "## 10. 接收人先检查什么",
    "## 11. 需要人工决定什么",
    "## 12. 工作流交接补充",
]
INTERNAL_TERMS = re.compile(
    r"(\bfreeze\b|\bgate\b|\bclosure\b|\bhandoff\b|\bworkflow\b|"
    r"冻结|启动门|证据|证据链|回退|工作合同|工作契约|合同|契约|成效卡|派单|关闭记录)",
    re.IGNORECASE,
)


def frontmatter_body(text: str) -> str:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    return text[match.end() :] if match else text


def validate(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    body = frontmatter_body(text)
    appendix_b = body.find("## 附录B：系统记录")
    main_body = body[:appendix_b] if appendix_b >= 0 else body
    errors: list[str] = []
    warnings: list[str] = []
    is_handoff = "# 交接结论" in body

    for required in COMMON_REQUIRED + (HANDOFF_REQUIRED if is_handoff else CARD_REQUIRED):
        if required not in body:
            errors.append(f"missing section: {required}")

    for header, min_rows in [
        ("## 2. 问题原因分析", 1),
        ("## 3. 当时有哪些可能做法", 2),
        ("## 5. 遇到的困难和处理方式", 1),
        ("## 7. 本阶段没有解决的问题", 1),
    ]:
        match = re.search(re.escape(header) + r"\s*\n((?:\|.*\|\s*\n)+)", body)
        if not match:
            errors.append(f"missing table under {header}")
            continue
        rows = [line for line in match.group(1).splitlines() if line.startswith("|")]
        data_rows = [line for line in rows[2:] if not re.fullmatch(r"\|[\s:|-]+\|", line)]
        if len(data_rows) < min_rows:
            errors.append(f"{header} needs at least {min_rows} data row(s)")

    if "是否推荐" not in body:
        errors.append("option table must compare benefits, costs/risks, and recommendation")
    if not re.search(r"推荐方案及原因[:：]?\s*\S+", body):
        errors.append("recommended option and reason are missing")

    for term in INTERNAL_TERMS.finditer(main_body):
        errors.append(f"internal management term in reader-facing body: '{term.group(0)}'")
        break

    if re.search(r"(?m)^#{1,3}\s*(SR-\d+|[A-Z]{2}-[A-Z]\d+)", main_body):
        errors.append("reader-facing heading starts with an internal ID")

    summary = re.search(r"# (?:交接结论|一句话结论)\s*\n+(.+?)(?:\n\n|\Z)", body)
    if not summary or not summary.group(1).strip():
        errors.append("one-line conclusion is missing")
    elif "<" in summary.group(1) and ">" in summary.group(1):
        warnings.append("one-line conclusion still contains a template placeholder")

    if "## 9. 专业补充" in body:
        supplement = body.split("## 9. 专业补充", 1)[1].split("## 附录A", 1)[0]
        if len(supplement.strip()) < 20:
            errors.append("professional supplement is empty")
        elif not re.search(r"^###\s+\S+", supplement, re.MULTILINE):
            errors.append("professional supplement lacks a domain-specific subsection")

    if "这些结果不能支持的说法" not in body:
        errors.append("result boundary is missing")
    if not re.search(r"做到什么程度算完成[:：]?\s*\S+", body):
        errors.append("completion criterion for the next action is missing")

    return errors, warnings


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, help="achievement card or workflow handoff Markdown")
    parser.add_argument("--strict", action="store_true", help="treat warnings as blocking")
    args = parser.parse_args()
    if not args.record.is_file():
        print(f"ERROR record does not exist: {args.record}")
        return 2
    try:
        errors, warnings = validate(args.record)
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ERROR cannot read record: {exc}")
        return 2
    print(f"record={args.record}")
    print(f"errors={len(errors)} warnings={len(warnings)}")
    for error in errors:
        print(f"ERROR {error}")
    for warning in warnings:
        print(f"WARN {warning}")
    if errors:
        return 2
    if warnings:
        print("QA=warnings")
        return 1 if args.strict else 0
    print("QA=pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
