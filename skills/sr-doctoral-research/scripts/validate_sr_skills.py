#!/usr/bin/env python3
"""Validate the SR leaf family and four global research-agent ownership model."""

from __future__ import annotations

import argparse
import json
import re
import tomllib
from collections import Counter
from pathlib import Path


AGENTS = {
    "sr-principal-investigator": {
        "file": "sr-principal-investigator.toml",
        "ids": [1, 2, 3, 5, 48, 49, 50, 54, 57, 58, 59, 60, 61, 64, 65, 66, 67, 68],
        "workflows": ["PI-E01", "PI-X01", "PI-P01"],
        "extra": {"sr-research-shared", "sr-weekly-meeting"},
    },
    "sr-method-builder": {
        "file": "sr-method-builder.toml",
        "ids": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 21, 22, 23, 24, 25, 26, 27, 51, 52, 62, 63],
        "workflows": ["MB-E01", "MB-X01", "MB-P01"],
        "extra": {"sr-research-shared"},
    },
    "sr-experimenter": {
        "file": "sr-experimenter.toml",
        "ids": [20, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 47, 53],
        "workflows": ["EX-E01", "EX-X01", "EX-P01"],
        "extra": {"sr-research-shared"},
    },
    "sr-critical-reviewer": {
        "file": "sr-critical-reviewer.toml",
        "ids": [4, 6, 17, 19, 40, 44, 45, 46, 55, 56],
        "workflows": ["CR-E01", "CR-X01", "CR-P01"],
        "extra": {"sr-research-shared"},
    },
}

REQUIRED_HANDOFF_FIELDS = [
    "尝试了什么", "发现了什么", "支持证据", "当前局限性", "产出了什么", "下一步该做什么"
]

PROJECT_LEAD = {
    "name": "sr-research-project-lead",
    "file": "sr-research-project-lead.toml",
    "workflows": ["RPL-01", "RPL-02", "RPL-03", "RPL-04"],
}

ASPECT_DIRS = [
    "01-研究问题与选题",
    "02-文献调研与领域结构",
    "03-Idea科学假设与创新点",
    "04-技术方案与方法设计",
    "05-实验设计与执行",
    "06-结果分析与问题诊断",
    "07-论文与成果表达",
    "08-项目推进与下一步计划",
]

WORKFLOW_HANDOFF_DIRS = {
    "PI-E01": "08-项目推进与下一步计划/PI-E01/",
    "PI-X01": "08-项目推进与下一步计划/PI-X01/",
    "PI-P01": "07-论文与成果表达/PI-P01/",
    "MB-E01": "02-文献调研与领域结构/MB-E01/",
    "MB-X01": "04-技术方案与方法设计/MB-X01/",
    "MB-P01": "07-论文与成果表达/MB-P01/",
    "EX-E01": "05-实验设计与执行/EX-E01/",
    "EX-X01": "05-实验设计与执行/EX-X01/",
    "EX-P01": "06-结果分析与问题诊断/EX-P01/",
    "CR-E01": "01-研究问题与选题/CR-E01/",
    "CR-X01": "06-结果分析与问题诊断/CR-X01/",
    "CR-P01": "07-论文与成果表达/CR-P01/",
}


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def frontmatter_name(text: str) -> str | None:
    match = re.match(r"^---\n(?P<body>.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    name = re.search(r"^name:\s*([^\s]+)\s*$", match.group("body"), re.MULTILINE)
    return name.group(1) if name else None


def configured_skill_names(agent_path: Path, agent: dict) -> set[str]:
    result = set()
    for entry in agent.get("skills", {}).get("config", []):
        result.add(Path(entry["path"]).name)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--global-codex-root", type=Path, default=Path.home() / ".codex")
    args = parser.parse_args()

    root = args.repo_root.resolve()
    global_root = args.global_codex_root.resolve()
    router = root / ".codex" / "skills" / "sr-doctoral-research"
    catalog = json.loads((router / "catalog.json").read_text(encoding="utf-8"))
    manifest = json.loads((router / "manifest.json").read_text(encoding="utf-8"))
    project_config = tomllib.loads((root / ".codex" / "config.toml").read_text(encoding="utf-8"))
    global_config = tomllib.loads((global_root / "config.toml").read_text(encoding="utf-8"))
    guide_path = root / "doc" / "SR四Agent科研工作流与交接说明_20260910.md"
    guide = guide_path.read_text(encoding="utf-8") if guide_path.is_file() else ""
    failures: list[str] = []

    skills = catalog.get("skills", [])
    expected_ids = [f"SR-{number:02d}" for number in range(1, 69)]
    require(len(skills) == 68, "catalog does not contain 68 skills", failures)
    require([item.get("id") for item in skills] == expected_ids, "catalog IDs are not SR-01..SR-68", failures)
    names = [item.get("name") for item in skills]
    require(len(names) == len(set(names)), "catalog contains duplicate names", failures)
    require(len(manifest.get("routes", [])) == 68, "manifest does not contain 68 routes", failures)
    id_to_name = {index + 1: name for index, name in enumerate(names)}

    for item in skills:
        name = item["name"]
        skill_dir = root / ".codex" / "skills" / name
        skill_file = skill_dir / "SKILL.md"
        ui_file = skill_dir / "agents" / "openai.yaml"
        require(skill_file.is_file(), f"missing project skill {name}/SKILL.md", failures)
        require(ui_file.is_file(), f"missing project skill {name}/agents/openai.yaml", failures)
        if skill_file.is_file():
            text = skill_file.read_text(encoding="utf-8")
            require(frontmatter_name(text) == name, f"frontmatter name mismatch: {name}", failures)
            require(item["id"] in text, f"missing SR ID in {name}", failures)
            require("## Completion gate" in text, f"missing completion gate in {name}", failures)
        if ui_file.is_file():
            ui = ui_file.read_text(encoding="utf-8")
            require(f"$" + name in ui, f"default prompt does not mention $" + name, failures)

    for route in manifest.get("routes", []):
        require((router / route["path"]).resolve().is_file(), f"broken route for {route['name']}", failures)

    project_agents = project_config.get("agents", {})
    require("phd-researcher" not in project_agents, "project config still registers phd-researcher", failures)
    require(not (root / ".codex" / "agents" / "phd-researcher.toml").exists(), "project phd-researcher.toml still exists", failures)
    require("phd-researcher" not in global_config.get("agents", {}), "global config still registers phd-researcher", failures)
    require(not (global_root / "agents" / "phd-researcher.toml").exists(), "global phd-researcher.toml still exists", failures)
    require(PROJECT_LEAD["name"] not in project_agents, "project config must not register the research project lead", failures)
    require(not (root / ".codex" / "agents" / PROJECT_LEAD["file"]).exists(), "project-local research project lead must not exist", failures)

    assigned_leaf_names: list[str] = []
    global_agents = global_config.get("agents", {})
    for agent_name, spec in AGENTS.items():
        registration = global_agents.get(agent_name, {})
        expected_path = (global_root / "agents" / spec["file"]).resolve()
        config_value = registration.get("config_file", "")
        configured_path = Path(config_value).resolve() if config_value else Path()
        require(configured_path == expected_path, f"{agent_name} registration path mismatch", failures)
        require(expected_path.is_file(), f"missing global agent file: {spec['file']}", failures)
        if not expected_path.is_file():
            continue
        agent = tomllib.loads(expected_path.read_text(encoding="utf-8"))
        require(agent.get("name") == agent_name, f"agent name mismatch: {agent_name}", failures)
        configured = configured_skill_names(expected_path, agent)
        expected_leaf = {id_to_name[value] for value in spec["ids"]}
        require(configured == expected_leaf | spec["extra"], f"{agent_name} skill ownership mismatch", failures)
        assigned_leaf_names.extend(expected_leaf)
        instructions = agent.get("developer_instructions", "")
        for workflow in spec["workflows"]:
            require(workflow in instructions, f"{agent_name} instructions missing {workflow}", failures)
        for field in REQUIRED_HANDOFF_FIELDS:
            require(field in instructions, f"{agent_name} instructions missing handoff field {field}", failures)
        require("取消聚合成效卡" in instructions, f"{agent_name} still lacks the no-aggregate rule", failures)
        require("SR-<两位编号>-<成果简称>.md" in instructions, f"{agent_name} lacks per-SR card naming", failures)
        require("YYYYMMDD-HHmmss-<工作简要>.md" in instructions, f"{agent_name} lacks timestamped handoff naming", failures)
        require("输入矩阵" in instructions, f"{agent_name} does not require upstream card/handoff reads", failures)
        for skill_name in configured:
            require((global_root / "skills" / skill_name).is_dir(), f"global skill missing for {agent_name}: {skill_name}", failures)

    counts = Counter(assigned_leaf_names)
    require(set(assigned_leaf_names) == set(names), "four agents do not cover all 68 leaf skills", failures)
    require(len(assigned_leaf_names) == 68, "four agents do not assign exactly 68 leaf skills", failures)
    require(all(count == 1 for count in counts.values()), "one or more leaf skills have duplicate owners", failures)

    lead_registration = global_agents.get(PROJECT_LEAD["name"], {})
    lead_path = (global_root / "agents" / PROJECT_LEAD["file"]).resolve()
    lead_config_value = lead_registration.get("config_file", "")
    configured_lead_path = Path(lead_config_value).resolve() if lead_config_value else Path()
    require(configured_lead_path == lead_path, "research project lead registration path mismatch", failures)
    require(lead_path.is_file(), "missing global research project lead agent", failures)
    if lead_path.is_file():
        lead = tomllib.loads(lead_path.read_text(encoding="utf-8"))
        lead_skills = configured_skill_names(lead_path, lead)
        require(lead.get("name") == PROJECT_LEAD["name"], "research project lead name mismatch", failures)
        require(lead_skills == {"sr-research-shared"}, "research project lead must own no SR leaf skill", failures)
        lead_instructions = lead.get("developer_instructions", "")
        for workflow in PROJECT_LEAD["workflows"]:
            require(workflow in lead_instructions, f"research project lead instructions missing {workflow}", failures)
        for specialist in AGENTS:
            require(specialist in lead_instructions, f"research project lead cannot route {specialist}", failures)
        require("只读评估模式" in lead_instructions, "research project lead lacks read-only default", failures)
        require("禁止要求或接受聚合工作流成效卡" in lead_instructions, "research project lead still accepts aggregate cards", failures)
        require("SR-NN-成果简称.md" in lead_instructions, "research project lead lacks per-SR card contract", failures)

    for base in [root / ".codex" / "skills", global_root / "skills"]:
        shared = base / "sr-research-shared"
        require((shared / "references" / "four-agent-workflows.md").is_file(), f"missing four-agent workflow reference under {base}", failures)
        require((shared / "references" / "project-lead-orchestration.md").is_file(), f"missing project-lead orchestration reference under {base}", failures)
        if (shared / "SKILL.md").is_file():
            shared_text = (shared / "SKILL.md").read_text(encoding="utf-8")
            require("four-agent-workflows.md" in shared_text, f"shared skill does not route to four-agent contract under {base}", failures)
            require("project-lead-orchestration.md" in shared_text, f"shared skill does not route to project-lead contract under {base}", failures)
            require("never create aggregate workflow cards" in shared_text, f"shared skill still permits aggregate cards under {base}", failures)
        contract_path = shared / "references" / "four-agent-workflows.md"
        if contract_path.is_file():
            contract = contract_path.read_text(encoding="utf-8")
            require("There is no aggregate workflow achievement card." in contract, f"missing no-aggregate invariant under {base}", failures)
            require("SR-<two-digit-id>-<short-result-name>.md" in contract, f"missing per-SR filename contract under {base}", failures)
            require("YYYYMMDD-HHmmss-<工作简要>.md" in contract, f"missing handoff filename contract under {base}", failures)
            for workflow, folder in WORKFLOW_HANDOFF_DIRS.items():
                require(workflow in contract, f"four-agent contract missing {workflow} under {base}", failures)
                require(folder in contract, f"four-agent contract missing handoff path {folder} under {base}", failures)
        research_contract_path = shared / "references" / "research-contract.md"
        if research_contract_path.is_file():
            research_contract = research_contract_path.read_text(encoding="utf-8")
            require("achievement_card:" in research_contract, f"leaf closure lacks achievement-card path under {base}", failures)

    require(guide_path.is_file(), "missing four-agent Chinese usage guide", failures)
    for workflow in [value for spec in AGENTS.values() for value in spec["workflows"]]:
        require(workflow in guide, f"usage guide missing workflow {workflow}", failures)
    for field in REQUIRED_HANDOFF_FIELDS:
        require(field in guide, f"usage guide missing handoff field {field}", failures)
    require("achievement_card:" in guide, "usage guide missing achievement-card template", failures)
    require("handoff:" in guide, "usage guide missing handoff template", failures)
    require("取消聚合成效卡" in guide, "usage guide still lacks no-aggregate rule", failures)
    require("SR-<两位编号>-<成果简称>.md" in guide, "usage guide missing per-SR card filename", failures)
    require("YYYYMMDD-HHmmss-<工作简要>.md" in guide, "usage guide missing timestamped handoff filename", failures)
    for aspect_dir in ASPECT_DIRS:
        require(aspect_dir in guide, f"usage guide missing aspect folder {aspect_dir}", failures)
    for workflow, folder in WORKFLOW_HANDOFF_DIRS.items():
        require(folder in guide, f"usage guide missing handoff path {folder}", failures)
    lead_guide_path = root / "doc" / "SR科研项目负责人Agent使用说明_20260910.md"
    lead_guide = lead_guide_path.read_text(encoding="utf-8") if lead_guide_path.is_file() else ""
    require(lead_guide_path.is_file(), "missing research project lead usage guide", failures)
    for workflow in PROJECT_LEAD["workflows"]:
        require(workflow in lead_guide, f"research project lead guide missing {workflow}", failures)
    for specialist in AGENTS:
        require(specialist in lead_guide, f"research project lead guide cannot route {specialist}", failures)
    require("research_project_assessment:" in lead_guide, "research project lead guide missing assessment schema", failures)

    if failures:
        print(f"FAIL: {len(failures)} issue(s)")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: 68 catalog items, 68 routes, and 68 project leaf skills")
    print("PASS: four global research agents own 18 + 22 + 18 + 10 unique leaf skills")
    print("PASS: 12 workflows use per-SR cards, eight aspect folders, and timestamped six-field handoffs")
    print("PASS: global research project lead owns no leaf skills and defines RPL-01 through RPL-04")
    print("PASS: no project-local or legacy global phd-researcher agent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
