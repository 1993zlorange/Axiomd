#!/usr/bin/env python3
"""从中文目录生成 68 个可独立使用的研究技能；--check 只检查，不写入。"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

GENERATED_MARKER = "<!-- 由 sr-doctoral-research/catalog.json 生成；请修改目录或本地专业补充后重新生成。 -->"
GUIDE = "沟通方式见 [AGENTS.md](AGENTS.md)：先说结果，用中文解释步骤、依据和限制。"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def validate_catalog(catalog: dict) -> list[dict]:
    items = catalog.get("skills", [])
    if [x.get("id") for x in items] != [f"SR-{i:02d}" for i in range(1, 69)]:
        raise ValueError("目录应按顺序包含 SR-01 至 SR-68")
    if len({x["name"] for x in items}) != len(items):
        raise ValueError("技能名称重复")
    for item in items:
        if not re.fullmatch(r"sr-[a-z0-9-]{1,60}", item["name"]) or not item["manual_steps"]:
            raise ValueError(f"技能名称或步骤不完整：{item['id']}")
    return items


def leaf_skill_text(item: dict, supplement: str = "") -> str:
    title = item["display_name"].removeprefix("SR-")
    steps = "\n".join(f"{i}. {step.rstrip('。')}。" for i, step in enumerate(item["manual_steps"], 1))
    return f'''---
name: {item["name"]}
description: {yaml_string(title + '：' + item['use_when'].rstrip('。') + '。')}
metadata:
  sr-id: {yaml_string(item["id"])}
  aspect: {yaml_string(item["aspect"])}
  short-description: {yaml_string(title)}
---

{GENERATED_MARKER}

# {title}

{GUIDE}

## 什么时候用

{item['use_when'].rstrip('。')}。按用户的任务自然使用，不要求用户说出技能名，也不要求指定负责人姓名。

## 先看什么

先读用户提供的材料和项目中与这项任务直接相关的文件，明确要回答的问题、已有结果和当前限制。已有手算、草图或研究笔记可以作为比较依据；没有时直接开展工作，不补造人工判断，也不要求用户先完成一套表格。

## 怎么做

{steps}
{supplement}
## 交付什么

使用本目录的 [结果模板](assets/output-template.md)。专业内容包括：{item['template']}。

精简模式下结果写实际专题产物，仅科研进展追加日志，任务范围进入需求，不另生成成果卡/契约/交接书。

未启用精简模式的项目：简单问题直接在对话中给出结果；需要保存科研结果时，按项目、上海记录日、规范类型定位唯一日文件。在 `08-项目推进与下一步计划/YYYYMMDD-科研结果-成果卡.md` 追加独立条目，不按任务、Agent、SR、阶段或目录另建文件。每条保留稳定ID、SR身份、来源、状态和适用范围，支持文件加锚点引用；实际专题产物仍在原责任目录。模板表达单条内容，没有真实条目不建日文件，常规实现检查只保留内部证据。

## 怎么检查

{item['completion_gate'].rstrip('。')}。

核对关键数字、来源位置、计算或运行结果；明确哪些是事实、解释、假设和计划。缺少输入时完成能做的部分，并说明缺什么、影响什么。没有运行的实验不能写成已完成，没有证据的推断不能写成结论。

## 需要用户决定时

{item['human_intervention']}

已有明确要求或授权就继续；仅当缺失信息会改变研究方向、费用、公开范围或不可逆操作时再提问。普通分析、草稿和本地验证可以直接交付；用户确认是独立状态，不是每项工作的前置签名。需要确认时用推荐、理由和代价说清楚，不从沉默推定同意。

本技能已包含完成任务所需的方法。按需使用本目录资料和现有工具，不加载其他技能，不自动安装扩展，也不自动启动超出授权的下一项研究工作。同一已批准目标内的剩余单元、必要修复、断点恢复、结果汇总和复核属于原任务，不能因叶技能结束、交接、工具等待超时或科学接受待确认而重复索要原授权。超预算、改变科学条件或权限时仅暂停受影响分支。
'''


def openai_yaml_text(item: dict) -> str:
    title = item["display_name"].removeprefix("SR-")
    return f'''interface:
  display_name: {yaml_string(title)}
  short_description: {yaml_string(title + '，说明做法、结果、来源和仍需核实的问题')}
  default_prompt: {yaml_string('请用 $' + item['name'] + ' 完成' + title + '，给出可检查的结果和必要说明。')}

policy:
  allow_implicit_invocation: true
'''


def routing_manifest(catalog: dict, items: list[dict]) -> dict:
    return {"name": "sr-doctoral-research", "version": catalog["version"],
            "source": catalog["source"], "purpose": "维护时查询职责，不要求运行时转调技能",
            "routes": [{"id": x["id"], "name": x["name"], "display_name": x["display_name"],
                        "aspect": x["aspect_key"], "intent": x["intent"], "detect": x["use_when"],
                        "path": f"../{x['name']}/SKILL.md"} for x in items]}


def outputs(root: Path) -> dict[Path, str]:
    skill_root = root / "skills"
    if not (skill_root / "sr-doctoral-research/catalog.json").is_file():
        skill_root = root / ".codex/skills"
    router = skill_root / "sr-doctoral-research"
    catalog = json.loads((router / "catalog.json").read_text(encoding="utf-8"))
    items = validate_catalog(catalog)
    result = {}
    for item in items:
        target = skill_root / item["name"]
        supplement = target / "references/workflow-supplement.md"
        detail = supplement.read_text(encoding="utf-8").strip() if supplement.is_file() else ""
        def local_link(match: re.Match) -> str:
            value = match.group(1)
            if ":" in value or value.startswith("#"):
                return match.group(0)
            resolved = (supplement.parent / value).resolve()
            return "](" + resolved.relative_to(target.resolve()).as_posix() + ")"
        detail = re.sub(r"\]\(([^)]+)\)", local_link, detail)
        result[target / "SKILL.md"] = leaf_skill_text(item, "\n" + detail + "\n" if detail else "")
        result[target / "agents/openai.yaml"] = openai_yaml_text(item)
    result[router / "manifest.json"] = json.dumps(routing_manifest(catalog, items), ensure_ascii=False, indent=2) + "\n"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--check", action="store_true", help="只检查生成结果是否一致")
    args = parser.parse_args()
    differences = []
    for path, content in outputs(args.repo_root.resolve()).items():
        if path.is_file() and path.read_text(encoding="utf-8") == content:
            continue
        differences.append(path)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if args.check and differences:
        for path in differences:
            print(f"过期：{path}")
        return 1
    print(f"68 个研究技能{'检查通过' if args.check else '已生成'}；变动文件：{len(differences)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
