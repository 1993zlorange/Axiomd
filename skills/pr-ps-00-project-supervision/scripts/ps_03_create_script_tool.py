"""创建 Python 脚本工具及配套 API 说明。"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from datetime import datetime
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
API_TEMPLATE = SKILL_ROOT / "assets" / "20260912-脚本工具-API说明模板.md"
CONFIG_PATTERN = re.compile(r"```project-supervision\s*\n(.*?)\n```", re.DOTALL)
MODULE_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")


class ToolCreationError(ValueError):
    """表示脚本工具创建参数或项目配置无效。"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="创建 Python 脚本工具及中文 API 说明。")
    parser.add_argument("--project-root", required=True, type=Path, help="包含 AGENTS.md 的项目根目录。")
    parser.add_argument("--module-name", required=True, help="符合 snake_case 的 Python 模块名。")
    parser.add_argument("--summary", required=True, help="工具的中文内容简述。")
    parser.add_argument("--write", action="store_true", help="实际写入；省略时只预览。")
    return parser.parse_args()


def load_config(project_root: Path) -> dict[str, object]:
    agents_files = [path for path in project_root.iterdir() if path.is_file() and path.name.lower() == "agents.md"]
    if len(agents_files) != 1:
        raise ToolCreationError("项目根必须且只能有一个 AGENTS.md。")
    match = CONFIG_PATTERN.search(agents_files[0].read_text(encoding="utf-8"))
    if match is None:
        raise ToolCreationError("AGENTS.md 缺少 project-supervision 配置块。")
    try:
        return tomllib.loads(match.group(1))
    except tomllib.TOMLDecodeError as exc:
        raise ToolCreationError(f"project-supervision 配置无法解析：{exc}") from exc


def resolve_inside(root: Path, relative_value: object, field_name: str) -> Path:
    if not isinstance(relative_value, str) or not relative_value.strip():
        raise ToolCreationError(f"配置字段 {field_name} 缺失。")
    relative_path = Path(relative_value)
    if relative_path.is_absolute():
        raise ToolCreationError(f"配置字段 {field_name} 必须是相对路径。")
    resolved = (root / relative_path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ToolCreationError(f"配置字段 {field_name} 越出项目根。") from exc
    return resolved


def normalize_summary(value: str) -> str:
    normalized = re.sub(r"[\\/:*?\"<>|\s]+", "-", value.strip())
    normalized = re.sub(r"-+", "-", normalized).strip("-.")
    if not normalized:
        raise ToolCreationError("内容简述无效。")
    return normalized


def script_source(summary: str) -> str:
    return f'''"""{summary}。"""

from __future__ import annotations

import argparse


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description="{summary}。")
    parser.add_argument("--input", required=True, help="显式输入路径或值。")
    parser.add_argument("--write", action="store_true", help="实际写入；省略时只预览。")
    return parser.parse_args()


def main() -> int:
    """执行工具并返回稳定退出码。"""
    args = parse_args()
    print(f"输入：{{args.input}}")
    print("待实现：请先补充输入输出契约、路径边界、错误、幂等、测试和回滚。")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
'''


def main() -> int:
    args = parse_args()
    try:
        project_root = args.project_root.resolve(strict=True)
        config = load_config(project_root)
        if not MODULE_PATTERN.fullmatch(args.module_name):
            raise ToolCreationError("--module-name 必须符合 Python snake_case。")
        scripts_root = resolve_inside(project_root, config.get("scripts_root"), "scripts_root")
        management_root = resolve_inside(project_root, config.get("project_management_root"), "project_management_root")
        tools_directory = resolve_inside(management_root, config.get("tools_dir"), "tools_dir")
        script_path = scripts_root / f"{args.module_name}.py"
        date_text = datetime.now().astimezone().strftime("%Y%m%d")
        api_path = tools_directory / f"{date_text}-{normalize_summary(args.summary)}-API说明.md"
        conflicts = [path for path in (script_path, api_path) if path.exists()]
        if conflicts:
            print("目标已存在，拒绝覆盖：", file=sys.stderr)
            for path in conflicts:
                print(path, file=sys.stderr)
            return 4
        print(f"脚本：{script_path}")
        print(f"API 说明：{api_path}")
        if not args.write:
            print("预览完成；未写入。提供 --write 后执行。")
            return 0
        script_path.parent.mkdir(parents=True, exist_ok=True)
        api_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text(script_source(args.summary), encoding="utf-8", newline="\n")
        api_text = API_TEMPLATE.read_text(encoding="utf-8")
        api_text = api_text.replace("<工具名称>", args.summary)
        api_text = api_text.replace('produced_at: "YYYY-MM-DD"', f'produced_at: "{datetime.now().astimezone().date().isoformat()}"')
        api_text = api_text.replace("- 源文件：", f"- 源文件：`{script_path.relative_to(project_root).as_posix()}`")
        api_text = api_text.replace("<命令或函数调用>", f"python {script_path.relative_to(project_root).as_posix()} --help")
        api_path.write_text(api_text, encoding="utf-8", newline="\n")
        print(f"已生成脚本：{script_path}")
        print(f"已生成 API 说明：{api_path}")
        return 0
    except FileNotFoundError as exc:
        print(f"项目根不存在：{exc}", file=sys.stderr)
        return 3
    except ToolCreationError as exc:
        print(f"创建条件错误：{exc}", file=sys.stderr)
        return 3
    except OSError as exc:
        print(f"写入失败：{exc}", file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
