#!/usr/bin/env python3
"""只读检查当前资产包的研究技能、名称、资源和 Agent 配置，不读取用户全局配置。"""
from __future__ import annotations
import argparse
import json
import re
import tomllib
from pathlib import Path


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    router = root / "skills/sr-doctoral-research"
    catalog = json.loads((router / "catalog.json").read_text(encoding="utf-8"))
    manifest = json.loads((router / "manifest.json").read_text(encoding="utf-8"))
    items = catalog["skills"]
    if [x["id"] for x in items] != [f"SR-{i:02d}" for i in range(1, 69)]:
        errors.append("研究编号应连续包含 SR-01 至 SR-68")
    names = [x["name"] for x in items]
    if len(set(names)) != len(names):
        errors.append("研究技能名称重复")
    if [x["name"] for x in manifest["routes"]] != names:
        errors.append("技能目录与索引不一致")
    for item in items:
        base = root / "skills" / item["name"]
        for rel in ("SKILL.md", "AGENTS.md", "agents/openai.yaml", "assets/output-template.md"):
            if not (base / rel).is_file():
                errors.append(f"缺少 {item['name']}/{rel}")
        if not (base / "SKILL.md").is_file():
            continue
        text = (base / "SKILL.md").read_text(encoding="utf-8")
        if f"name: {item['name']}" not in text or item["id"] not in text:
            errors.append(f"名称或编号不匹配：{item['name']}")
        for heading in ("什么时候用", "先看什么", "怎么做", "交付什么", "怎么检查"):
            if "## " + heading not in text:
                errors.append(f"缺少 {heading}：{item['name']}")
        if re.search(r"\]\(\.\./(?:sr|pr)-[^)]+", text):
            errors.append(f"存在跨技能运行依赖：{item['name']}")
        ui = base / "agents/openai.yaml"
        if ui.is_file() and "allow_implicit_invocation: true" not in ui.read_text(encoding="utf-8"):
            errors.append(f"未允许自然语言触发：{item['name']}")
    owned = []
    for path in (root / "agents").glob("sr-*.toml"):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        for entry in data.get("skills", {}).get("config", []):
            target = (path.parent / entry["path"]).resolve()
            if not target.is_relative_to((root / "skills").resolve()) or not (target / "SKILL.md").is_file():
                errors.append(f"无效配置：{path.name} {entry['path']}")
            if target.name in names:
                owned.append(target.name)
    if sorted(owned) != sorted(names):
        errors.append("68 个研究专项应各有一个专业角色配置，不能重复或遗漏")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    try:
        errors = validate(args.repo_root.resolve())
    except (OSError, ValueError, KeyError) as exc:
        errors = [str(exc)]
    for error in errors:
        print("错误：" + error)
    if not errors:
        print("通过：68 个研究专项、索引、本地资源及角色配置一致")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
