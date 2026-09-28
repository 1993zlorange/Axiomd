#!/usr/bin/env python3
"""Generate plain-language SR achievement and workflow-handoff templates.

Only catalog leaves SR-01 through SR-68 receive local achievement templates.
Shared packages and the router keep their own existing templates.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "skills" / "sr-doctoral-research" / "catalog.json"
SHARED = ROOT / "skills" / "sr-research-shared"
TEMPLATE_DIR = SHARED / "references" / "record-templates"
SHARED_ASSETS = SHARED / "assets"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").rstrip() + "\n"


def render_base(base: str, item: dict) -> str:
    text = base
    replacements = {
        "sr-<技能名>-<YYYYMMDD>": f"{item['name']}-<YYYYMMDD>",
        "<技能名>": item["name"],
        "<SR编号>": item["id"],
        "<工作流编号>": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def plain_phrase(value: str) -> str:
    """Translate repository/process wording before it enters a reader-facing card."""
    replacements = {
        "证据链": "支撑材料",
        "证据": "支撑材料",
        "冻结": "先不再改动",
        "启动门": "继续前的检查",
        "回退": "备用方案",
        "工作契约": "工作约定",
        "契约": "约定",
        "合同": "约定",
        "成效卡": "结果记录",
        "工作包": "任务",
        "关闭记录": "完成记录",
        "closure": "完成记录",
        "handoff": "交接记录",
        "workflow": "工作流程",
        "Gate": "继续前的检查",
        "gate": "继续前的检查",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def professional_block(item: dict) -> str:
    aspect = item["aspect_key"]
    aspect_path = TEMPLATE_DIR / "aspects" / f"{aspect}.md"
    if not aspect_path.is_file():
        raise ValueError(f"missing aspect template: {aspect_path}")
    special_candidates = [
        TEMPLATE_DIR / "special" / f"{item['name']}.md",
        TEMPLATE_DIR / "special" / f"{item['id'].lower()}-{item['name'].removeprefix('sr-')}.md",
    ]
    special_path = next((path for path in special_candidates if path.is_file()), None)
    parts = [
        read(aspect_path),
        "### 本工作包完成要点\n",
        f"- 交付结构：{plain_phrase(item['template'])}",
        f"- 完成要求：{plain_phrase(item['completion_gate'])}",
    ]
    if special_path is not None:
        parts.append(read(special_path))
    return "\n".join(parts).rstrip() + "\n"


def render_card(item: dict) -> str:
    base = read(TEMPLATE_DIR / "achievement-card-base.md")
    text = render_base(base, item)
    if item.get("bibliography_export"):
        text = text.replace("  evidence: []", "  bibliography_exports: []\n  evidence: []", 1)
    placeholder = "<按本工作包所属研究阶段和专业需要填写，不作为领导阅读的主文。>\n"
    if placeholder not in text:
        raise ValueError("achievement base missing professional placeholder")
    return text.replace(placeholder, professional_block(item), 1)


def write_shared_templates() -> None:
    card = read(TEMPLATE_DIR / "achievement-card-base.md")
    handoff = read(TEMPLATE_DIR / "workflow-handoff-base.md")
    SHARED_ASSETS.mkdir(parents=True, exist_ok=True)
    (SHARED_ASSETS / "achievement-card-template.md").write_text(card, encoding="utf-8", newline="\n")
    (SHARED_ASSETS / "workflow-handoff-template.md").write_text(handoff, encoding="utf-8", newline="\n")
    placeholder = "本交接按探索 / 执行 / 表达阶段补充；详细字段见本节后方的阶段补充。\n"
    for stage in ("explore", "execute", "express"):
        supplement = read(TEMPLATE_DIR / "handoffs" / f"{stage}.md")
        if placeholder not in handoff:
            raise ValueError("handoff base missing stage placeholder")
        stage_pointer = "本交接按探索 / 执行 / 表达阶段补充；详细字段见本节后方的阶段补充。\n\n"
        text = handoff.replace(placeholder, stage_pointer + supplement, 1)
        (SHARED_ASSETS / f"workflow-handoff-{stage}-template.md").write_text(
            text, encoding="utf-8", newline="\n"
        )


def catalog_items() -> list[dict]:
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    items = data.get("skills", [])
    expected = [f"SR-{number:02d}" for number in range(1, 69)]
    if [item.get("id") for item in items] != expected:
        raise ValueError("catalog does not contain ordered SR-01 through SR-68")
    return items


def write_templates() -> tuple[int, int]:
    items = catalog_items()
    changed = 0
    for item in items:
        target = ROOT / "skills" / item["name"] / "assets" / "output-template.md"
        expected = render_card(item)
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            target.write_text(expected, encoding="utf-8", newline="\n")
            changed += 1
    write_shared_templates()
    return len(items), changed


def check_templates() -> int:
    items = catalog_items()
    failures: list[str] = []
    for item in items:
        target = ROOT / "skills" / item["name"] / "assets" / "output-template.md"
        expected = render_card(item)
        if not target.is_file():
            failures.append(f"missing {target.relative_to(ROOT)}")
        elif target.read_text(encoding="utf-8") != expected:
            failures.append(f"outdated {target.relative_to(ROOT)}")
    shared_card = SHARED_ASSETS / "achievement-card-template.md"
    shared_handoff = SHARED_ASSETS / "workflow-handoff-template.md"
    for source, target in [
        (TEMPLATE_DIR / "achievement-card-base.md", shared_card),
        (TEMPLATE_DIR / "workflow-handoff-base.md", shared_handoff),
    ]:
        if not target.is_file() or target.read_text(encoding="utf-8") != read(source):
            failures.append(f"outdated {target.relative_to(ROOT)}")
    handoff_base = read(TEMPLATE_DIR / "workflow-handoff-base.md")
    placeholder = "本交接按探索 / 执行 / 表达阶段补充；详细字段见本节后方的阶段补充。\n"
    for stage in ("explore", "execute", "express"):
        target = SHARED_ASSETS / f"workflow-handoff-{stage}-template.md"
        stage_pointer = "本交接按探索 / 执行 / 表达阶段补充；详细字段见本节后方的阶段补充。\n\n"
        expected = handoff_base.replace(
            placeholder, stage_pointer + read(TEMPLATE_DIR / "handoffs" / f"{stage}.md"), 1
        )
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            failures.append(f"outdated {target.relative_to(ROOT)}")
    if failures:
        for failure in failures:
            print(f"ERROR {failure}", file=sys.stderr)
        return 1
    print(f"PASS: {len(items)} SR record templates match the canonical generator")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check without writing")
    args = parser.parse_args()
    if args.check:
        return check_templates()
    count, changed = write_templates()
    print(f"generated SR record templates: {count}")
    print(f"changed local templates: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
