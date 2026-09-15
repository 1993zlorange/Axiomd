---
name: sr-research-shared
description: Internal shared-reference package for SR doctoral research skills, defining work contracts, human-AI authority, weekly evidence loops, and optional third-party adapters. Do not invoke as a standalone research workflow; load only the reference requested by an SR router or leaf skill.
metadata:
  short-description: Shared contracts for the SR research skill family
---

# SR Research Shared References

如需保存共享契约加载记录，使用本目录的 [中文空白模板](assets/output-template.md)；本包仍不可作为独立科研工作流调用。

Use this package only as a dependency of another SR Skill.

- Load [references/research-contract.md](references/research-contract.md) at the start and close of a leaf workflow.
- Load [references/human-ai-collaboration.md](references/human-ai-collaboration.md) when authority, permission, scientific judgment, ethics, privacy, resources, submission, or release matters.
- Load [references/weekly-loop.md](references/weekly-loop.md) for weekly planning, acceptance, and group-meeting preparation.
- Load [references/four-agent-workflows.md](references/four-agent-workflows.md) for four-agent ownership, twelve numbered workflows, achievement-card rules, and structured handoffs.
- Load [references/project-lead-orchestration.md](references/project-lead-orchestration.md) when the research project lead must inventory a project, determine its evidence-backed stage, recommend the next work portfolio, or dispatch and accept work from the four research agents.
- Load [references/source-adapters.md](references/source-adapters.md) only when an installed third-party Skill may be composed into the current leaf workflow.
- Return to the requesting SR Skill for task logic, output template, and completion criteria.
- Each closed SR leaf produces its own dated card named `YYYYMMDD-内容简述-成果卡.md` in the mapped project aspect folder, with the SR ID in frontmatter. Workflow transfer, pause, blockage, or closure produces a dated handoff using the same convention; never create aggregate workflow cards.
- Project-lead assessment is read-only by default. It may recommend delegation, but it must not start specialist work unless the user explicitly asks it to execute the recommendation.
