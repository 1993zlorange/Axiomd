#!/usr/bin/env python3
"""Validate SR records against the approved body-writing standard.

The checker reviews structure, wording, cleanliness, notation, and internal
consistency. It cannot decide whether a scientific claim is true; that judgment
remains with the researcher and, where required, the named human reviewer.

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
    "## 1. 原来遇到什么问题",
    "## 2. 问题原因分析",
    "## 3. 当时有哪些可能做法",
    "## 4. 本阶段做了什么",
    "## 5. 遇到的困难和处理方式",
    "## 6. 当前结果",
    "## 7. 本阶段没有解决的问题",
    "## 8. 下一步计划",
    "## 附录A：支撑材料",
    "## 附录B：系统记录",
    "## 附录C：原文保留区",
]
CARD_REQUIRED = ["# 一句话结论", "## 9. 专业补充"]
HANDOFF_REQUIRED = [
    "# 交接结论",
    "## 0. 交接信息",
    "## 9. 本次产生或更新的成果卡",
    "## 10. 接收人先检查什么",
    "## 11. 需要人工决定什么",
    "不从沉默推定同意",
    "## 12. 工作流交接补充",
]

GOVERNANCE_ID = re.compile(r"\b(?:REQ|HDEC|RPL|CP|SUP|CHG)-[A-Za-z0-9_-]+\b", re.IGNORECASE)
PATH_RE = re.compile(r"(?:[A-Za-z]:)?(?:[\\/][A-Za-z0-9_.-]+){2,}\b|(?:[A-Za-z0-9_.-]+[\\/]){2,}[A-Za-z0-9_.-]+\b")
EXTENSION_RE = re.compile(r"\.(?:py|md|json|yaml|yml|toml|csv|pdf|png|jpg|jpeg|html|ipynb)\b", re.IGNORECASE)
HASH_RE = re.compile(r"\b[0-9a-fA-F]{64}\b")
BACKTICK_RE = re.compile(r"`+")
SESSION_MECHANICS_RE = re.compile(r"(提示注入|注入摘要|协调方|子代理|落盘|会话机制)", re.IGNORECASE)
PRONOUN_RE = re.compile(r"(我们|这轮|老师|说白了)")
BUREAUCRACY_RE = re.compile(r"(具名|检查点|予以|旨在|等待人工裁决|派发|冻结)")
ASSIGNMENT_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\s*(?:=|:=)\s*[^=]")
VERSION_RE = re.compile(r"\bv?\d+(?:\.\d+)+(?:[-+][A-Za-z0-9_.-]+)?\b", re.IGNORECASE)
SNAKE_CODE_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b")
ROADSIGNS = ("先说结论", "综上所述", "总结一下", "概括来说")


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def section_text(body: str, heading: str) -> str:
    match = re.search(re.escape(heading) + r"\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    return match.group(1) if match else ""


def has_no_record(section: str) -> bool:
    first = next((line.strip() for line in section.splitlines() if line.strip()), "")
    return first in {"（本项无记录）", "(本项无记录)"}


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*[\"']?([^\"'\n]+)[\"']?\s*$", frontmatter)
    return match.group(1).strip() if match else None


def sentence_metrics(text: str) -> tuple[int, int, list[str]]:
    long_sentences: list[str] = []
    max_length = 0
    for raw_line in text.splitlines():
        if raw_line.lstrip().startswith(("|", "```", "<!--", "- #")):
            continue
        cleaned = re.sub(r"\s+", " ", raw_line.replace("#", " ")).strip()
        if not cleaned:
            continue
        for sentence in re.split(r"(?<=[。！？!?；;])", cleaned):
            sentence = sentence.strip()
            if not sentence:
                continue
            max_length = max(max_length, len(sentence))
            if len(sentence) > 60:
                long_sentences.append(sentence)
    return len(long_sentences), max_length, long_sentences


def parenthesis_metrics(text: str) -> tuple[int, int]:
    nested = 0
    multiple = 0
    for line in text.splitlines():
        if line.lstrip().startswith(("|", "```", "<!--")):
            continue
        if ("(" in line and ")" in line and "(" in line[line.find(")") + 1 :]) or ("（" in line and "）" in line and "（" in line[line.find("）") + 1 :]):
            nested += 1
        plain = re.sub(r"<[^>]+>", "", line)
        if plain.count("(") + plain.count("（") > 1:
            multiple += 1
    return nested, multiple


def validate(path: Path) -> tuple[list[str], list[str], dict[str, object]]:
    text = path.read_text(encoding="utf-8")
    frontmatter, full_body = split_frontmatter(text)
    body = strip_comments(full_body)
    appendix_a = body.find("## 附录A：支撑材料")
    appendix_b = body.find("## 附录B：系统记录")
    narrative_end = min(index for index in (appendix_a, appendix_b, len(body)) if index >= 0)
    main_body = body[:narrative_end]
    appendix_beyond = body[appendix_b:] if appendix_b >= 0 else ""
    errors: list[str] = []
    warnings: list[str] = []
    is_handoff = "# 交接结论" in body

    for required in COMMON_REQUIRED + (HANDOFF_REQUIRED if is_handoff else CARD_REQUIRED):
        if required not in body:
            errors.append(f"missing section: {required}")

    for heading, min_rows in [
        ("## 2. 问题原因分析", 1),
        ("## 3. 当时有哪些可能做法", 2),
        ("## 5. 遇到的困难和处理方式", 1),
        ("## 7. 本阶段没有解决的问题", 1),
    ]:
        section = section_text(body, heading)
        if not section:
            errors.append(f"missing section content: {heading}")
            continue
        if has_no_record(section):
            continue
        rows = [line for line in section.splitlines() if line.startswith("|")]
        data_rows = [line for line in rows[2:] if not re.fullmatch(r"\|[\s:|-]+\|", line)]
        if len(data_rows) < min_rows:
            errors.append(f"{heading} needs {min_rows} data row(s) or “（本项无记录）”")

    if "是否推荐" not in body and not has_no_record(section_text(body, "## 3. 当时有哪些可能做法")):
        errors.append("option table must compare benefits, costs/risks, and recommendation")
    if not re.search(r"推荐方案及原因[:：]?\s*\S+", body) and not has_no_record(section_text(body, "## 3. 当时有哪些可能做法")):
        errors.append("recommended option and reason are missing")

    # Clean reader-facing body.
    checks = [
        ("governance ID", GOVERNANCE_ID),
        ("path or repository location", PATH_RE),
        ("file extension", EXTENSION_RE),
        ("hash string", HASH_RE),
        ("session mechanism", SESSION_MECHANICS_RE),
        ("forbidden pronoun/register", PRONOUN_RE),
        ("bureaucratic wording", BUREAUCRACY_RE),
        ("code assignment", ASSIGNMENT_RE),
    ]
    for label, pattern in checks:
        match = pattern.search(main_body)
        if match:
            errors.append(f"{label} in reader-facing body: '{match.group(0)}'")
            break

    if BACKTICK_RE.search(main_body):
        errors.append("backtick/code formatting in reader-facing body; use plain Chinese and put the exact symbol in an appendix")

    outside_parentheses = re.sub(r"[（(][^（）()]*[）)]", "", main_body)
    for label, pattern in [
        ("version-like notation outside a ledger parenthesis", VERSION_RE),
        ("snake_case field outside a ledger parenthesis", SNAKE_CODE_RE),
    ]:
        match = pattern.search(outside_parentheses)
        if match:
            warnings.append(f"{label}: '{match.group(0)}'")

    road_signs = sum(main_body.count(sign) for sign in ROADSIGNS)
    if road_signs > 2:
        errors.append(f"conclusion road-sign phrases exceed 2 ({road_signs})")
    nested, multiple = parenthesis_metrics(main_body)
    if nested:
        errors.append(f"nested parenthesis in reader-facing body ({nested} line(s))")
    if multiple:
        warnings.append(f"more than one parenthesis in a sentence ({multiple} line(s))")

    long_count, max_sentence, _ = sentence_metrics(main_body)
    if long_count:
        warnings.append(f"{long_count} sentence(s) exceed 60 characters; maximum={max_sentence}")

    if re.search(r"(?m)^#{1,3}\s*(SR-\d+|[A-Z]{2}-[A-Z]\d+)", main_body):
        errors.append("reader-facing heading starts with an internal ID")

    summary = re.search(r"# (?:交接结论|一句话结论)\s*\n+(.+?)(?:\n\n|\Z)", body)
    if not summary or not summary.group(1).strip():
        errors.append("one-line conclusion is missing")
    elif "<" in summary.group(1) and ">" in summary.group(1):
        warnings.append("one-line conclusion still contains a template placeholder")

    supplement = section_text(body, "## 9. 专业补充")
    if not is_handoff:
        if len(supplement.strip()) < 20:
            errors.append("professional supplement is empty")
        elif not re.search(r"^###\s+\S+", supplement, re.MULTILINE):
            errors.append("professional supplement lacks a domain-specific subsection")

    if "这些结果不能支持的说法" not in body:
        errors.append("result boundary is missing")
    if not re.search(r"做到什么程度算完成[:：]?\s*\S+", body):
        errors.append("completion criterion for the next action is missing")

    if is_handoff:
        info = section_text(body, "## 0. 交接信息")
        nonempty = [line for line in info.splitlines() if line.strip().startswith("-")]
        if len(nonempty) > 2:
            errors.append("handoff information section has more than two lines")

    # Numbers should be traceable within the same file (appendices, frontmatter, or source table).
    number_count = len(re.findall(r"\d+(?:\.\d+)?", main_body))
    appendix_start = body.find("## 附录A：支撑材料")
    appendix_c = body.find("## 附录C：原文保留区")
    appendix_end = appendix_c if appendix_c >= 0 else len(body)
    appendix_sources = body[appendix_start:appendix_end] if appendix_start >= 0 else appendix_beyond
    number_audit = "not-applicable"
    if number_count:
        number_audit = "pass" if not re.search(r"(<[^>]+>|（本项无记录）|未记录)", appendix_sources) else "review"
        if number_audit == "review":
            warnings.append("numbers exist in the body, but Appendix A/B still contains placeholders or no-record wording")

    # Frontmatter and Appendix B status synchronization when both are present.
    fm_status = frontmatter_value(frontmatter, "status")
    fm_verdict = frontmatter_value(frontmatter, "human_verdict")
    machine_status = frontmatter_value(appendix_beyond, "status")
    machine_verdict = frontmatter_value(appendix_beyond, "human_verdict")
    sync_status = "not-applicable"
    if fm_status and machine_status and "|" not in fm_status and "|" not in machine_status:
        sync_status = "pass" if fm_status == machine_status else "review"
        if sync_status == "review":
            warnings.append(f"frontmatter/Appendix B status differ: {fm_status!r} vs {machine_status!r}")
    elif fm_verdict and machine_verdict and "|" not in fm_verdict and "|" not in machine_verdict:
        sync_status = "pass" if fm_verdict == machine_verdict else "review"
        if sync_status == "review":
            warnings.append(f"frontmatter/Appendix B human verdict differ: {fm_verdict!r} vs {machine_verdict!r}")

    metrics = {
        "long_sentences": long_count,
        "max_sentence_chars": max_sentence,
        "nested_parenthesis_lines": nested,
        "multi_parenthesis_lines": multiple,
        "road_signs": road_signs,
        "body_number_count": number_count,
        "number_source_audit": number_audit,
        "machine_status_sync": sync_status,
    }
    return errors, warnings, metrics


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
        errors, warnings, metrics = validate(args.record)
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ERROR cannot read record: {exc}")
        return 2
    print(f"record={args.record}")
    print(f"errors={len(errors)} warnings={len(warnings)}")
    for key, value in metrics.items():
        print(f"metric {key}={value}")
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
