#!/usr/bin/env python3
"""Validate PR management documents against the approved writing standard.

Modes:
  1. Single document: validate level, structure, wording, and notation.
  2. Baseline/revised pair: compare frontmatter, protected lines, and
     ID/number/path token multisets for conservation.

The script is read-only and does not prove factual correctness.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


ID_RE = re.compile(r"(?<![A-Za-z0-9])[A-Z][A-Z0-9]*(?:-[A-Za-z0-9]+)+(?![A-Za-z0-9])")
PATH_RE = re.compile(r"(?:[A-Za-z]:)?[\\/][A-Za-z0-9_.-]+(?:[\\/][A-Za-z0-9_.-]+)+|\b[A-Za-z0-9_.-]+[\\/][A-Za-z0-9_.-]+\.[A-Za-z0-9]+\b")
NUMBER_RE = re.compile(r"\d+(?:\.\d+)?")
WORKFLOW_ID_RE = re.compile(r"\b(?:PI|MB|CR|EX)-[A-Z]\d+\b")
BANNED_RE = re.compile(r"(具名|检查点|派发|派单|予以|旨在|附登记限制)")
SENTENCE_END = re.compile(r"(?<=[。！？!?；;])")


def split_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*[\"']?([^\"'\n]+)[\"']?\s*$", frontmatter)
    return match.group(1).strip() if match else None


def infer_level(path: Path, frontmatter: str) -> str | None:
    value = frontmatter_value(frontmatter, "writing_level")
    if value:
        return value
    name = path.name
    if any(token in name for token in ("需求记录", "日志", "决定记录", "呈报", "日报")):
        return "A"
    if any(token in name for token in ("监督记录", "变更记录", "反思", "交接简报", "执行提示词")):
        return "B"
    if any(token in name for token in ("质量门禁", "统计", "模板")):
        return "C"
    return None


def body_before_appendix(body: str) -> str:
    return body.split("## 附录：管理信息", 1)[0]


def sentence_metrics(text: str) -> tuple[int, int]:
    long_count = 0
    max_length = 0
    for raw_line in text.splitlines():
        if raw_line.lstrip().startswith(("|", "```", "#", ">")):
            continue
        cleaned = " ".join(raw_line.split())
        if not cleaned:
            continue
        for sentence in SENTENCE_END.split(cleaned):
            sentence = sentence.strip()
            if not sentence:
                continue
            max_length = max(max_length, len(sentence))
            if len(sentence) > 60:
                long_count += 1
    return long_count, max_length


def narrative_lines(body: str) -> list[str]:
    result: list[str] = []
    in_code = False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped:
            continue
        if stripped.startswith(("|", "#", ">", "---")):
            continue
        result.append(stripped)
    return result


def audit_lines(body: str) -> list[str]:
    """Narrative lines excluding tables, headings, quotes, and path/ID carriers."""
    result: list[str] = []
    for line in narrative_lines(body):
        if ">" in line or "用户原话" in line:
            continue
        if ID_RE.search(line) or PATH_RE.search(line):
            continue
        result.append(line)
    return result


def strip_parentheses(text: str) -> str:
    return re.sub(r"[（(][^（）()]*[）)]", "", text)


def validate_document(path: Path, requested_level: str | None) -> tuple[list[str], list[str], dict[str, object]]:
    text = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    level = requested_level or infer_level(path, frontmatter)
    errors: list[str] = []
    warnings: list[str] = []
    if level not in {"A", "B", "C"}:
        return [f"cannot infer writing level; provide --level A|B|C"], warnings, {}
    declared_level = frontmatter_value(frontmatter, "writing_level")
    legacy_audit = declared_level is None and requested_level is not None
    if legacy_audit:
        warnings.append("frontmatter lacks writing_level; level was supplied explicitly for legacy-document audit")
    elif declared_level != level:
        errors.append(f'frontmatter must contain writing_level: "{level}"')

    appendix_present = "## 附录：管理信息" in body
    main_body = body_before_appendix(body) if appendix_present else body
    long_count, max_sentence = sentence_metrics(main_body)
    b_c_banned_lines = [line for line in audit_lines(main_body) if BANNED_RE.search(line)]
    a_banned_lines = [
        line for line in narrative_lines(main_body)
        if ">" not in line and "用户原话" not in line and BANNED_RE.search(line)
    ]

    if level == "A":
        if not appendix_present:
            errors.append("A级缺少必需结构：## 附录：管理信息")
        if legacy_audit:
            conceptual = {
                "背景": any(token in main_body for token in ("背景", "意味着什么", "定了什么")),
                "内容": any(token in main_body for token in ("做了什么", "要做什么", "研究内容", "定了什么")),
                "影响": any(token in main_body for token in ("影响", "生效解释")),
            }
            for name, present in conceptual.items():
                if not present:
                    errors.append(f"A级旧稿缺少概念结构：{name}")
        else:
            required = [
                "## 1. 背景一句话",
                "## 2. 研究内容",
                "## 3. 研究影响",
                "### 管理信息索引",
                "### 正文编号对照",
                "### 原记录对照",
            ]
            for item in required:
                if item not in body:
                    errors.append(f"A级缺少必需结构：{item}")

        governance_ids: list[str] = []
        workflow_ids: list[str] = []
        for line in narrative_lines(main_body):
            if ">" in line or "用户原话" in line:
                continue
            cleaned = strip_parentheses(line)
            for identifier in ID_RE.findall(cleaned):
                if WORKFLOW_ID_RE.fullmatch(identifier):
                    workflow_ids.append(identifier)
                else:
                    governance_ids.append(identifier)
        if governance_ids:
            errors.append(f"A级正文出现治理编号；编号应移入附录“正文编号对照”：{governance_ids[0]}")
        if workflow_ids:
            warnings.append(f"A级正文出现工作流编号，建议写成中文名（编号）：{workflow_ids[0]}")

        path_lines = [
            line for line in narrative_lines(main_body)
            if ">" not in line and "用户原话" not in line and PATH_RE.search(line)
        ]
        if path_lines:
            errors.append("A级正文出现路径；路径应移入附录")
        if "`" in main_body:
            errors.append("A级正文出现反引号或代码格式")
        if a_banned_lines:
            errors.append(f"A级正文出现公文词：{a_banned_lines[0]}")
    elif level == "B":
        if b_c_banned_lines:
            errors.append(f"B级叙述出现公文词：{b_c_banned_lines[0]}")
        if long_count:
            warnings.append(f"B级存在 {long_count} 个超过60字的长句；最大 {max_sentence} 字")
    else:
        if b_c_banned_lines:
            warnings.append(f"C级存在公文词：{b_c_banned_lines[0]}")
        if long_count:
            warnings.append(f"C级存在 {long_count} 个超过60字的长句；最大 {max_sentence} 字")

    metrics = {
        "level": level,
        "legacy_audit": legacy_audit,
        "long_sentences": long_count,
        "max_sentence_chars": max_sentence,
        "id_count": len(ID_RE.findall(text)),
        "path_count": len(PATH_RE.findall(text)),
        "number_count": len(NUMBER_RE.findall(text)),
        "banned_lines": len(a_banned_lines if level == "A" else b_c_banned_lines),
    }
    return errors, warnings, metrics


def tokens(text: str) -> Counter[str]:
    result: Counter[str] = Counter()
    result.update(ID_RE.findall(text))
    result.update(PATH_RE.findall(text))
    result.update(NUMBER_RE.findall(text))
    return result


def protected_lines(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip().startswith(">") or "留痕" in line or "不得删除" in line
    ]


def compare_documents(baseline: Path, revised: Path) -> tuple[list[str], list[str], dict[str, object]]:
    old = baseline.read_text(encoding="utf-8")
    new = revised.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    old_front, _ = split_frontmatter(old)
    new_front, _ = split_frontmatter(new)
    if old_front != new_front:
        errors.append("frontmatter machine fields changed")
    old_tokens = tokens(old)
    new_tokens = tokens(new)
    missing = old_tokens - new_tokens
    added = new_tokens - old_tokens
    for token, count in sorted(missing.items()):
        errors.append(f"token lost ({count}): {token}")
    for token, count in sorted(added.items()):
        warnings.append(f"token added ({count}): {token}")
    old_protected = protected_lines(old)
    new_protected = protected_lines(new)
    if Counter(old_protected) != Counter(new_protected):
        errors.append("protected quote/audit-retention lines changed")
    metrics = {
        "baseline_tokens": sum(old_tokens.values()),
        "revised_tokens": sum(new_tokens.values()),
        "lost_token_kinds": len(missing),
        "added_token_kinds": len(added),
        "protected_lines": len(new_protected),
    }
    return errors, warnings, metrics


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", nargs="?", type=Path, help="Single Markdown document to validate")
    parser.add_argument("--level", choices=["A", "B", "C"], help="Override or specify writing level")
    parser.add_argument("--baseline", type=Path, help="Original document for revision comparison")
    parser.add_argument("--revised", type=Path, help="Revised document for revision comparison")
    parser.add_argument("--strict", action="store_true", help="treat warnings as blocking")
    args = parser.parse_args()

    if args.baseline or args.revised:
        if not args.baseline or not args.revised:
            print("ERROR --baseline and --revised must be used together", file=sys.stderr)
            return 2
        try:
            errors, warnings, metrics = compare_documents(args.baseline, args.revised)
        except (OSError, UnicodeDecodeError) as exc:
            print(f"ERROR cannot read comparison documents: {exc}", file=sys.stderr)
            return 2
        label = f"{args.baseline} -> {args.revised}"
    else:
        if args.document is None:
            print("ERROR provide a document, or --baseline and --revised", file=sys.stderr)
            return 2
        if not args.document.is_file():
            print(f"ERROR document does not exist: {args.document}", file=sys.stderr)
            return 2
        try:
            errors, warnings, metrics = validate_document(args.document, args.level)
        except (OSError, UnicodeDecodeError) as exc:
            print(f"ERROR cannot read document: {exc}", file=sys.stderr)
            return 2
        label = str(args.document)

    print(f"document={label}")
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
