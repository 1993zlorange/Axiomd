# Axiom Agents repository instructions

This repository is a redistributable Codex asset package. Keep the source repository portable: do not add machine-specific absolute paths, credentials, private project evidence, generated logs, or large binary artifacts.

Before changing agents or skills:

1. Run `python scripts/validate.py` and record the baseline result.
2. Explain the behavior change, affected profiles, and compatibility risk.
3. Keep agent names, skill directory names, and profile membership consistent.
4. Regenerate `manifest.json` and `docs/asset-index.md` with `python scripts/build_inventory.py`.
5. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.
6. Write every commit message as a Chinese `类型: 说明` summary (for example `修复: ...`); complex changes add a body listing the change reason, affected profiles/assets, and verification commands with actual results.

The installer is safety-critical. Preserve path validation, staged activation, backups, verification, and uninstall behavior.

## Record ownership and approved execution

Process records use one writable file per project, Asia/Shanghai record day, and canonical record type. Task, role, stage, directory, and format do not split that identity. Keep independent entries and stable anchors, deduplicate events across days, preserve revisions, and serialize writes. Create no empty daily files or routine bundles of management documents. Source code, fixed inputs, raw runs, signed originals, and formal entity documents retain their own identities; exports are read-only. Do not relocate historical records or release snapshots to enforce a new policy.

Scientific progress reports show research-point-linked performance work; ordinary implementation checks remain internal. Prefer analyzing existing results, then the smallest necessary performance comparison. Necessary fixes, recovery, remaining units and summaries within an approved objective continue without repeating authorization; new scientific conditions, resource limits or external permissions pause only the affected branch.

## PR/SR interaction guides

The PR/SR skill-local `AGENTS.md` files are generated from `docs/pr-sr-interaction-standard.md`. To update them, edit that canonical file, run `python scripts/generate_pr_sr_interaction_guides.py`, then run `python scripts/generate_pr_sr_interaction_guides.py --check`. Do not edit individual generated copies directly.

## SR record templates

SR-01 through SR-68 use plain-language achievement-card templates generated from `skills/sr-research-shared/references/record-templates/`. To update them, edit the base/aspect/special/handoff module, run `python scripts/generate_sr_record_templates.py`, then run `python scripts/generate_sr_record_templates.py --check`. Do not edit the 68 generated local templates directly.

## PR management document standard

PR management documents follow `skills/pr-ps-00-project-supervision/references/20260929-管理文档写作标准-管理规范.md`. Requirement and log templates are A-level; supervision, change, and reflection templates are B-level; quality and cost templates are C-level. Use `skills/pr-ps-00-project-supervision/scripts/ps_01_create_governance_document.py` to generate project documents and validate them with `skills/pr-ps-00-project-supervision/scripts/ps_04_validate_management_document.py`.


科研日志按组会汇报要求逐项对应研究问题与汇报问题，正文和附录均排除工程审查、登记及检查成绩。调研、方法、写作按实际研究认识变化表达，不硬填性能数字。科研日志采用group-meeting/1.0，具体规则以sr-research-shared的references/group-meeting-reporting.md为准；无科研进展不产日志。


组会要点在可见正文中必须写出具体问题，不能只显示4.4.Q10一类编号。编号保留在机器元数据便于核对，生成器按group-meeting-questions.json展开。面向领导和导师，用完整句说明做了什么、结果说明什么、还有什么不足、接下来做什么；首次解释必要术语，禁止未解释的A/B/C、S0/S1、宏、固定流、待决等简称。保留所有必要数字、条件、负结果和结论边界，不能把改写写成新实验。


## 项目精简记录模式

项目record_policy.process_record_profile=minimal时，新日记录仅允许enabled_daily_types中的requirement和log；不逐任务生成监督、变更、反思、质量、成本、成果卡、工作契约或交接书，也不换名专题报告规避。新增要求、范围和用户决定进入需求，实际研究产物保留唯一专题正文，有意义的科研进展进入日志；原始运行、必要检查、恢复断点和简短接续指针保存在已有工程运行中，不另造人工内部日报。检查与独立评审仍执行，原始意见、真实批准及签署原件保留。没有新要求或实质进展时，两类文件也不必生成。读取真实产物，不把缺少管理表作为阻塞。以下旧类型模板只供未启用该模式的项目或读取历史材料使用。


## 工程文档按对象维护

docs仅保存当前代码的使用与维护说明：README导航、architecture实际结构、api接口导航，以及interfaces、commands、algorithms、adr。相同模块、脚本组或文件格式维护唯一当前正文，使用稳定对象名，日期与适用版本放元数据，不因修复或每次运行新增日期API文档。简单脚本优先--help及必要注释，相关脚本共用运行指南；复杂独立工具确需说明时维护一份对象文档。文档必须讲输入输出、错误、限制及真实命令，不能以目录模板补造未实现能力。

工作契约、工程交付/复验、检查成绩、修订流水、补丁和源码快照不进入docs，必要原始证据留既有run。旧的“每个新脚本新增日期API说明”要求由本节替代；这是维护现行说明，不取消必要用法文档。科研结果、图表解释和主张归achieve并引用唯一原始来源。架构决定按实际决定对象保留，不为普通修复或文件整理另写ADR。

迁移前检查当前代码、配置、命令及历史来源绑定；被封存运行绑定的原件不得覆盖、改指纹或改写旧manifest。保留原路径只读例外须逐文件登记原SHA与用途并在导航标明非现行稿，其余旧件移出日常docs。归并先提取有效字段、边界及运行语义，过程部分原件保全。文档唯一性按对象/适用版本判断，不把不同模块同日的合法文档并成一个日文件。新目录有实际文档才建，工程检查不进入科研日志。
