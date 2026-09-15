#!/usr/bin/env python3
"""Generate the 68 SR leaf skills and routing manifest.

Agent registration and workflow documentation are maintained separately. This
generator must never create a project-local research agent.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


GENERATED_MARKER = "<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def validate_catalog(catalog: dict) -> list[dict]:
    skills = catalog.get("skills")
    if not isinstance(skills, list) or len(skills) != 68:
        raise ValueError("catalog must contain exactly 68 skills")
    expected = [f"SR-{number:02d}" for number in range(1, 69)]
    if [item.get("id") for item in skills] != expected:
        raise ValueError("skill IDs must be ordered exactly from SR-01 through SR-68")
    names = [item.get("name") for item in skills]
    if len(set(names)) != len(names):
        raise ValueError("skill names must be unique")
    required = {
        "id", "name", "display_name", "aspect", "aspect_key", "intent",
        "use_when", "manual_steps", "ai_role", "human_intervention",
        "template", "completion_gate", "next",
    }
    for item in skills:
        missing = required.difference(item)
        if missing:
            raise ValueError(f"{item.get('id', '<unknown>')} missing fields: {sorted(missing)}")
        if not re.fullmatch(r"sr-[a-z0-9-]{1,60}", item["name"]):
            raise ValueError(f"invalid skill name: {item['name']}")
        if not item["manual_steps"]:
            raise ValueError(f"{item['id']} must define manual_steps")
    return skills


def leaf_skill_text(item: dict) -> str:
    manual_steps = "\n".join(
        f"{index}. {step}" for index, step in enumerate(item["manual_steps"], start=1)
    )
    adapters = item.get("recommended_adapters", [])
    adapter_text = ", ".join(f"`{value}`" for value in adapters) if adapters else "None; use available local tools."
    next_text = ", ".join(f"`$" + value + "`" for value in item["next"]) or "none"
    description = (
        f"{item['display_name']}：{item['use_when']}。"
        "Use for this specific doctoral research work package after routing; "
        "do not use as a generic end-to-end research assistant."
    )
    return f"""---
name: {item['name']}
description: {yaml_string(description)}
metadata:
  sr-id: {yaml_string(item['id'])}
  aspect: {yaml_string(item['aspect'])}
  short-description: {yaml_string(item['display_name'])}
---

{GENERATED_MARKER}

# {item['display_name']}

Use this leaf Skill when: {item['use_when']}

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

{manual_steps}

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it so AI output can be compared with independent human judgment.

## Human-AI collaboration

**AI role:** {item['ai_role']}

**Human intervention:** {item['human_intervention']}

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use this template: {item['template']}

Recommended optional adapters: {adapter_text}. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using an adapter. Missing adapters are not a blocker; disclose the manual or local fallback.

## Completion gate

{item['completion_gate']}

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): {next_text}. Treat these as candidates, not a forced sequence; route according to the highest-value unknown.
"""


def openai_yaml_text(item: dict) -> str:
    prompt = (
        "Use $" + item["name"] + f" to complete {item['display_name']} with my human baseline, "
        "a reviewable artifact, explicit human checkpoints, and an evidence-based closure record."
    )
    return f"""interface:
  display_name: {yaml_string(item['display_name'])}
  short_description: {yaml_string(item['display_name'] + '：古法首轮、人机协作、证据验收')}
  default_prompt: {yaml_string(prompt)}

policy:
  allow_implicit_invocation: false
"""


def routing_manifest(catalog: dict, skills: list[dict]) -> dict:
    return {
        "name": "sr-doctoral-research",
        "version": catalog["version"],
        "source": catalog["source"],
        "axes": {
            "aspect": ["problem", "literature", "idea", "method", "experiment", "analysis", "paper", "progress"],
            "intent": ["explore", "decide", "design", "execute", "diagnose", "communicate", "review"],
        },
        "routes": [
            {
                "id": item["id"],
                "name": item["name"],
                "display_name": item["display_name"],
                "aspect": item["aspect_key"],
                "intent": item["intent"],
                "detect": item["use_when"],
                "path": f"../{item['name']}/SKILL.md",
            }
            for item in skills
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    args = parser.parse_args()

    root = args.repo_root.resolve()
    router = root / ".codex" / "skills" / "sr-doctoral-research"
    catalog = json.loads((router / "catalog.json").read_text(encoding="utf-8"))
    skills = validate_catalog(catalog)
    skill_root = router.parent

    for item in skills:
        leaf_root = skill_root / item["name"]
        write_text(leaf_root / "SKILL.md", leaf_skill_text(item))
        write_text(leaf_root / "agents" / "openai.yaml", openai_yaml_text(item))

    manifest = routing_manifest(catalog, skills)
    write_text(router / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    print(f"generated {len(skills)} leaf skills")
    print(f"manifest routes: {len(manifest['routes'])}")
    print("project-local research agents: not generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
