#!/usr/bin/env python3
"""Regenerate manifest.json and human-readable asset indexes from repository contents."""
from __future__ import annotations

import hashlib
import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_hash(root: Path) -> str:
    if root.is_file() and not root.is_symlink():
        return file_hash(root)
    digest = hashlib.sha256()
    files = sorted(p for p in root.rglob("*") if p.is_file() and not p.is_symlink())
    for path in files:
        rel = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(len(rel).to_bytes(8, "big"))
        digest.update(rel)
        digest.update(file_hash(path).encode("ascii"))
    return digest.hexdigest()


def skill_description(path: Path) -> str:
    match = SKILL_FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return "See SKILL.md."
    block = match.group(1)
    lines = block.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        value = line.split(":", 1)[1].strip()
        if value in {">-", ">", "|", "|-", "|+", ">+"}:
            indented: list[str] = []
            for following in lines[index + 1 :]:
                if following.startswith((" ", "\t")):
                    indented.append(following.strip())
                else:
                    break
            return " ".join(indented).strip() or "See SKILL.md."
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            try:
                return str(json.loads(value))
            except json.JSONDecodeError:
                pass
        return value.strip("'\"")
    return "See SKILL.md."


def agent_description(path: Path) -> str:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    return str(data.get("description", "")).strip()


def profiles_for(asset: str, kind: str, profiles: dict[str, dict]) -> list[str]:
    result = []
    for profile_name, profile in profiles.items():
        if asset in profile[kind]:
            result.append(profile_name)
    return result


def optional_profiles_for(asset: str, kind: str, profiles: dict[str, dict]) -> list[str]:
    result = []
    for profile_name, profile in profiles.items():
        if asset in profile.get("optional_skills", []) and kind == "skills":
            result.append(profile_name)
    return result


def clean_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def profile_mark(membership: list[str], optional: list[str]) -> str:
    labels = []
    if "ai4programming" in membership:
        labels.append("P")
    if "ai4science" in membership:
        labels.append("S")
    if "all" in membership:
        labels.append("A")
    if optional:
        labels.append("opt")
    return "/".join(labels) or "-"


def build() -> None:
    profiles = {path.stem: read_json(path) for path in sorted((ROOT / "profiles").glob("*.json"))}
    agent_paths = sorted((ROOT / "agents").glob("*.toml"))
    skill_paths = sorted((ROOT / "skills").iterdir())
    skill_paths = [path for path in skill_paths if path.is_dir() and (path / "SKILL.md").is_file()]
    skill_names = [path.name for path in skill_paths]

    agents: dict[str, dict] = {}
    for path in agent_paths:
        agents[path.stem] = {
            "description": agent_description(path),
            "hash": tree_hash(path),
            "profiles": profiles_for(path.stem, "agents", profiles),
        }

    skills: dict[str, dict] = {}
    for path in skill_paths:
        skills[path.name] = {
            "description": skill_description(path / "SKILL.md"),
            "hash": tree_hash(path),
            "profiles": profiles_for(path.name, "skills", profiles),
            "optional_profiles": optional_profiles_for(path.name, "skills", profiles),
        }

    plugin = read_json(ROOT / "plugin.json")
    manifest = {
        "schema_version": 1,
        "name": plugin["name"],
        "version": plugin["version"],
        "description": plugin["description"],
        "license": plugin["license"],
        "profiles": {
            name: {
                "description": profile["description"],
                "agents": len(profile["agents"]),
                "skills": len(profile["skills"]),
                "optional_skills": len(profile.get("optional_skills", [])),
            }
            for name, profile in profiles.items()
        },
        "agents": agents,
        "skills": skills,
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    # Full asset index.
    lines = [
        "# MyAgent asset index",
        "",
        f"This index is generated by `python scripts/build_inventory.py`. It lists {len(agents)} agents and {len(skills)} skills.",
        "",
        "Profile marks: **P** = AI4PROGRAMMING core, **S** = AI4SCIENCE core, **A** = all profile, **opt** = optional in that profile.",
        "",
        "## Agents",
        "",
        "| Agent | Profiles | Description |",
        "| --- | --- | --- |",
    ]
    for name, data in agents.items():
        lines.append(f"| [`{name}`](../agents/{name}.toml) | {profile_mark(data['profiles'], [])} | {clean_cell(data['description'])} |")
    lines.extend(["", "## Skills", ""])
    groups = [
        ("Programming governance and delivery", [n for n in skills if n.startswith("pr-")]),
        ("Doctoral research workflow", [n for n in skills if n.startswith("sr-")]),
        ("ScienceResearch compatibility", [n for n in skills if n.startswith("scienceresearch-")]),
        ("Browser verification", [n for n in skills if n == "playwright"]),
    ]
    for title, names in groups:
        if not names:
            continue
        lines.extend([f"### {title}", "", "| Skill | Profiles | Description |", "| --- | --- | --- |"])
        for name in names:
            data = skills[name]
            lines.append(f"| [`{name}`](../skills/{name}/SKILL.md) | {profile_mark(data['profiles'], data['optional_profiles'])} | {clean_cell(data['description'])} |")
        lines.append("")
    (ROOT / "docs/asset-index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")

    # Explicit agent-to-skill map.
    map_lines = [
        "# Agent-to-skill map",
        "",
        "This map is generated from each agent TOML's `[[skills.config]]` entries and skill names mentioned in its developer instructions.",
        "",
    ]
    known = set(skill_names)
    for agent_path in agent_paths:
        data = tomllib.loads(agent_path.read_text(encoding="utf-8"))
        configured = [item.get("path", "").replace("../skills/", "") for item in data.get("skills", {}).get("config", [])]
        instructions = str(data.get("developer_instructions", ""))
        mentioned = sorted(
            name for name in known
            if name not in configured and re.search(r"(?<![A-Za-z0-9_-])" + re.escape(name) + r"(?![A-Za-z0-9_-])", instructions)
        )
        map_lines.extend([f"## `{agent_path.stem}`", "", clean_cell(str(data.get("description", ""))), ""])
        map_lines.append("**Configured skills**")
        map_lines.append("")
        if configured:
            map_lines.extend(f"- `{name}`" for name in configured)
        else:
            map_lines.append("- None.")
        map_lines.extend(["", "**Referenced in instructions**", ""])
        if mentioned:
            map_lines.extend(f"- `{name}`" for name in mentioned)
        else:
            map_lines.append("- None.")
        map_lines.append("")
    (ROOT / "docs/agent-skill-map.md").write_text("\n".join(map_lines).rstrip() + "\n", encoding="utf-8", newline="\n")

    print(f"Generated manifest.json, docs/asset-index.md, and docs/agent-skill-map.md: {len(agents)} agents, {len(skills)} skills.")


if __name__ == "__main__":
    build()
