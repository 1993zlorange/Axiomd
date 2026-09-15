"""创建带代号的项目级 Codex Skill。"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from datetime import datetime
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
PROPOSAL_TEMPLATE = SKILL_ROOT / "assets" / "20260912-技能提案-提案模板.md"
CONFIG_PATTERN = re.compile(r"```project-supervision\s*\n(.*?)\n```", re.DOTALL)
CODE_PATTERN = re.compile(r"^[a-z][a-z0-9]*-\d{2}$")
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class SkillCreationError(ValueError):
    """表示 Skill 创建参数或项目配置无效。"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="创建符合项目治理规则的 Codex Skill。")
    parser.add_argument("--project-root", required=True, type=Path, help="包含 AGENTS.md 的项目根目录。")
    parser.add_argument("--code", required=True, help="技能代号，例如 ds-01。")
    parser.add_argument("--name", required=True, help="英文 kebab-case 技能名称。")
    parser.add_argument("--display-name", required=True, help="中文显示名称。")
    parser.add_argument("--description", required=True, help="中文触发说明。")
    parser.add_argument("--document-output", action="store_true", help="声明该 Skill 会生成文档并创建中文模板。")
    parser.add_argument("--write", action="store_true", help="实际写入；省略时只预览。")
    return parser.parse_args()


def load_config(project_root: Path) -> dict[str, object]:
    agents_files = [path for path in project_root.iterdir() if path.is_file() and path.name.lower() == "agents.md"]
    if len(agents_files) != 1:
        raise SkillCreationError("项目根必须且只能有一个 AGENTS.md。")
    match = CONFIG_PATTERN.search(agents_files[0].read_text(encoding="utf-8"))
    if match is None:
        raise SkillCreationError("AGENTS.md 缺少 project-supervision 配置块。")
    try:
        return tomllib.loads(match.group(1))
    except tomllib.TOMLDecodeError as exc:
        raise SkillCreationError(f"project-supervision 配置无法解析：{exc}") from exc


def resolve_inside(root: Path, relative_value: object, field_name: str) -> Path:
    if not isinstance(relative_value, str) or not relative_value.strip():
        raise SkillCreationError(f"配置字段 {field_name} 缺失。")
    path = Path(relative_value)
    if path.is_absolute():
        raise SkillCreationError(f"配置字段 {field_name} 必须是相对路径。")
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise SkillCreationError(f"配置字段 {field_name} 越出项目根。") from exc
    return resolved


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def build_short_description(display_name: str, description: str) -> str:
    candidate = description.strip().replace("\n", " ")
    if len(candidate) < 25:
        candidate = f"{display_name}：{candidate}，用于当前项目的受控工作流程。"
    return candidate[:64]


def skill_markdown(skill_name: str, display_name: str, description: str, template_name: str | None) -> str:
    output_section = ""
    if template_name:
        output_section = f"""
## 文档输出

生成文档时必须从 [中文空白模板](assets/{template_name})开始，按项目 `AGENTS.md` 的目录配置写入。输出命名为 `YYYYMMDD-内容简述-文档类型.扩展名`，不得把模板占位符或未经验证的事实写成结论。
"""
    return f"""---
name: {skill_name}
description: {description}
---

# {display_name}

## 职责与边界

<说明本 Skill 的唯一工作结果、适用范围和明确非目标。>

## 前置输入

- <项目规则、批准基线、输入文件和权限。>

## 执行流程

1. <检查现状和输入契约。>
2. <执行最小可回滚动作。>
3. <验证正常、边界和失败行为。>

## 输出与失败边界

- 输出：<产物、状态和证据。>
- 阻塞：<权限、依赖、冲突或证据不足条件。>
- 回滚：<恢复方式。>
{output_section}
## 验证

- <项目可复现的验证命令或审查方法。>

## 权限

不自动提交、推送、发布、删除、覆盖、读取凭据或写入外部系统；需要这些动作时单独取得明确授权。
"""


def main() -> int:
    args = parse_args()
    try:
        project_root = args.project_root.resolve(strict=True)
        config = load_config(project_root)
        if not CODE_PATTERN.fullmatch(args.code):
            raise SkillCreationError("--code 必须符合小写字母/数字加两位序号，例如 ds-01。")
        if not NAME_PATTERN.fullmatch(args.name):
            raise SkillCreationError("--name 必须是小写 kebab-case。")
        skill_name = f"{args.code}-{args.name}"
        if len(skill_name) > 64:
            raise SkillCreationError("完整 Skill 名称不得超过 64 个字符。")
        skills_root = resolve_inside(project_root, config.get("project_skills_root"), "project_skills_root")
        management_root = resolve_inside(project_root, config.get("project_management_root"), "project_management_root")
        skill_records = resolve_inside(management_root, config.get("skills_dir"), "skills_dir")
        target_root = skills_root / skill_name
        date_text = datetime.now().astimezone().strftime("%Y%m%d")
        proposal = skill_records / f"{date_text}-{args.display_name}-技能说明.md"
        template_name = f"{date_text}-{args.display_name}-输出模板.md" if args.document_output else None
        targets = [target_root / "SKILL.md", target_root / "agents" / "openai.yaml", proposal]
        if template_name:
            targets.append(target_root / "assets" / template_name)
        conflicts = [path for path in targets if path.exists()]
        if conflicts:
            print("目标已存在，拒绝覆盖：", file=sys.stderr)
            for path in conflicts:
                print(path, file=sys.stderr)
            return 4
        print("计划生成：")
        for path in targets:
            print(path)
        if not args.write:
            print("预览完成；未写入。提供 --write 后执行。")
            return 0
        for path in targets:
            path.parent.mkdir(parents=True, exist_ok=True)
        (target_root / "SKILL.md").write_text(
            skill_markdown(skill_name, args.display_name, args.description, template_name), encoding="utf-8", newline="\n"
        )
        openai_yaml = (
            "interface:\n"
            f"  display_name: {yaml_quote(args.display_name)}\n"
            f"  short_description: {yaml_quote(build_short_description(args.display_name, args.description))}\n"
            f"  default_prompt: {yaml_quote(f'使用 ${skill_name} 完成已批准的工作。')}\n"
            "\npolicy:\n  allow_implicit_invocation: false\n"
        )
        (target_root / "agents" / "openai.yaml").write_text(openai_yaml, encoding="utf-8", newline="\n")
        if template_name:
            template_text = f"""---
title: "<{args.display_name}输出标题>"
document_id: "<稳定文档 ID>"
produced_at: "YYYY-MM-DD"
status: "草稿"
owner: "<责任人>"
---

# <{args.display_name}输出标题>

## 1. 目的、范围与非目标

## 2. 输入、约束与证据

## 3. 正文

## 4. 验证、限制与结论边界

## 5. 追溯、人工决定与下一步
"""
            (target_root / "assets" / template_name).write_text(template_text, encoding="utf-8", newline="\n")
        proposal_text = PROPOSAL_TEMPLATE.read_text(encoding="utf-8")
        proposal_text = proposal_text.replace("<代号>-<技能名称>", skill_name).replace("<维护人>", "待指定")
        proposal_text = proposal_text.replace('produced_at: "YYYY-MM-DD"', f'produced_at: "{datetime.now().astimezone().date().isoformat()}"')
        proposal.write_text(proposal_text, encoding="utf-8", newline="\n")
        print(f"已生成 Skill：{target_root}")
        print(f"已生成技能说明：{proposal}")
        return 0
    except FileNotFoundError as exc:
        print(f"项目根不存在：{exc}", file=sys.stderr)
        return 3
    except SkillCreationError as exc:
        print(f"创建条件错误：{exc}", file=sys.stderr)
        return 3
    except OSError as exc:
        print(f"写入失败：{exc}", file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
