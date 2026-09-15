---
name: pr-ps-05-skill-authoring
description: 提议、创建或演化带代号的项目级 Codex Skill，并验证职责、触发、权限、脚本、模板和生命周期。适用于重复问题已具备证据时；不把单次项目特例直接升级为通用 Skill。
---

# PS-05 Skill 编写与演化

读取主监理[Skill 与脚本生成规范](../pr-ps-00-project-supervision/references/20260912-技能与脚本工具生成-技术规范.md)、[进化策略](../pr-ps-00-project-supervision/references/20260912-质量门禁与进化策略-管理规范.md)及项目 `AGENTS.md`。

先使用 [中文空白模板](assets/20260912-技能编写-输出模板.md)形成技能提案，确认现有 Skill 无法覆盖、代号唯一、责任单一、维护人和验证方式明确。目录与 frontmatter `name` 使用 `<代号>-<英文技能名称>`。

可使用主技能工具 `scripts/ps_02_create_project_skill.py` 生成候选骨架。凡 Skill 产生文档，必须同时生成中文空白模板并在 `SKILL.md` 中引用模板路径、命名和项目落点。候选 Skill 经正常、边界、失败、重复执行、权限和误触发试点后，等待人工批准再默认启用。项目提供 Skill 晋升只读审计器时，在提交全局晋升材料前运行它；审计通过不替代独立评审、人工批准或实际全局安装记录。
