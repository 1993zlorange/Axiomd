"""按项目 AGENTS 配置生成项目治理文档。"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from datetime import datetime
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSET_ROOT = SKILL_ROOT / "assets"
DOCUMENT_TYPES = {
    "requirement": ("requirements_dir", "需求记录", "20260912-用户需求-需求记录模板.md"),
    "supervision": ("supervision_dir", "监督记录", "20260912-项目操作监督-监督记录模板.md"),
    "log": ("logs_dir", "日志", "20260912-项目工作-日志模板.md"),
    "reflection": ("reflections_dir", "反思", "20260912-问题缺陷-反思模板.md"),
    "change": ("changes_dir", "变更记录", "20260912-项目变更-变更记录模板.md"),
    "cost": ("costs_dir", "统计", "20260912-成本时间-统计模板.md"),
    "quality": ("quality_dir", "质量门禁", "20260912-质量门禁-检查模板.md"),
    "skill-proposal": ("skills_dir", "技能提案", "20260912-技能提案-提案模板.md"),
    "script-api": ("tools_dir", "API说明", "20260912-脚本工具-API说明模板.md"),
    "document-type": ("templates_dir", "文档类型登记", "20260912-新文档类型-登记模板.md"),
    "placement": ("supervision_dir", "放置决策", "20260912-文件放置-决策模板.md"),
}
CONFIG_PATTERN = re.compile(r"```project-supervision\s*\n(.*?)\n```", re.DOTALL)


class ProjectConfigError(ValueError):
    """表示项目监理配置缺失、无效或越界。"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="按项目配置生成中文治理文档。")
    parser.add_argument("--project-root", required=True, type=Path, help="包含 AGENTS.md 的项目根目录。")
    parser.add_argument("--type", required=True, choices=sorted(DOCUMENT_TYPES), help="治理文档类型。")
    parser.add_argument("--summary", required=True, help="用于文件名的简短内容说明。")
    parser.add_argument("--write", action="store_true", help="实际写入；省略时只预览。")
    return parser.parse_args()


def load_project_config(project_root: Path) -> dict[str, object]:
    agents_files = [path for path in project_root.iterdir() if path.is_file() and path.name.lower() == "agents.md"]
    if len(agents_files) != 1:
        raise ProjectConfigError("项目根必须且只能有一个 AGENTS.md。")
    text = agents_files[0].read_text(encoding="utf-8")
    match = CONFIG_PATTERN.search(text)
    if match is None:
        raise ProjectConfigError("AGENTS.md 缺少 project-supervision 配置块。")
    try:
        config = tomllib.loads(match.group(1))
    except tomllib.TOMLDecodeError as exc:
        raise ProjectConfigError(f"project-supervision 配置无法解析：{exc}") from exc
    return config


def resolve_inside(root: Path, relative_value: object, field_name: str) -> Path:
    if not isinstance(relative_value, str) or not relative_value.strip():
        raise ProjectConfigError(f"配置字段 {field_name} 缺失或不是字符串。")
    relative_path = Path(relative_value)
    if relative_path.is_absolute():
        raise ProjectConfigError(f"配置字段 {field_name} 必须是项目根相对路径。")
    resolved = (root / relative_path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ProjectConfigError(f"配置字段 {field_name} 解析后越出项目根。") from exc
    return resolved


def normalize_summary(value: str) -> str:
    normalized = re.sub(r"[\\/:*?\"<>|\s]+", "-", value.strip())
    normalized = re.sub(r"-+", "-", normalized).strip("-.")
    if not normalized:
        raise ProjectConfigError("内容简述不能为空或只包含非法文件名字符。")
    return normalized


def build_target(project_root: Path, config: dict[str, object], document_type: str, summary: str) -> tuple[Path, Path]:
    management_root = resolve_inside(project_root, config.get("project_management_root"), "project_management_root")
    directory_key, label, template_name = DOCUMENT_TYPES[document_type]
    relative_directory = config.get(directory_key)
    if not isinstance(relative_directory, str):
        raise ProjectConfigError(f"配置缺少 {directory_key}。")
    target_directory = resolve_inside(management_root, relative_directory, directory_key)
    date_text = datetime.now().astimezone().strftime("%Y%m%d")
    target = target_directory / f"{date_text}-{normalize_summary(summary)}-{label}.md"
    return ASSET_ROOT / template_name, target


def main() -> int:
    args = parse_args()
    try:
        project_root = args.project_root.resolve(strict=True)
        if not project_root.is_dir():
            raise ProjectConfigError("--project-root 必须是目录。")
        config = load_project_config(project_root)
        template, target = build_target(project_root, config, args.type, args.summary)
        if not template.is_file():
            raise ProjectConfigError(f"全局模板不存在：{template.name}")
        if target.exists():
            print(f"目标已存在，拒绝覆盖：{target}", file=sys.stderr)
            return 4
        print(f"模板：{template}")
        print(f"目标：{target}")
        if not args.write:
            print("预览完成；未写入。提供 --write 后执行。")
            return 0
        target.parent.mkdir(parents=True, exist_ok=True)
        content = template.read_text(encoding="utf-8").replace(
            'produced_at: "YYYY-MM-DD"',
            f'produced_at: "{datetime.now().astimezone().date().isoformat()}"',
            1,
        )
        target.write_text(content, encoding="utf-8", newline="\n")
        print(f"已生成：{target}")
        return 0
    except FileNotFoundError as exc:
        print(f"项目根不存在：{exc}", file=sys.stderr)
        return 3
    except ProjectConfigError as exc:
        print(f"项目配置错误：{exc}", file=sys.stderr)
        return 3
    except OSError as exc:
        print(f"写入失败：{exc}", file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
