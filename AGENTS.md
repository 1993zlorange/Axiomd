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


## 面向读者的项目交付

docs是给审阅者和使用者看的技术说明与使用手册，只回答项目做什么、怎么使用、结果说明什么。稳定文档为README.md、项目技术说明.md、使用指南.md、结果说明与适用范围.md。新项目尚无成果时只写真实起始入口，标明尚未建立；具备可用成果后再完成四份文档，不能复制四份空成品。

正文用完整中文讲用途、输入输出、方法关系、操作和结果范围。必要命令/参数保留并解释，函数清单、完整机器字段表、来源指纹和内部代号不进入正文或元数据头；机器信息保存在配置和运行资料。开发者参考与历史原件不在docs日常目录；旧运行使用保全的旧版本上下文，不改原输入和结果。

读者只看docs应能说明用途、按指南完成一个真实路径、理解结果及限制。结构/关键词检查不能证明可读和可用，要实际走读与操作；失败先修成品，不另写一套管理报告。科研结论由本项目真实研究决定，不复制其他项目结论。每次相关变更检查受影响的代表性用法。

项目按需求选择实际能力，服务器、训练服务、Docker、Notebook等不默认生成空结构；科研和软件分别选择唯一根模板，myagent提供能力。新项目名称、路径、规则和当前入口统一替换，模板维护材料和旧技能不复制。日常仅需求和重要进度；按已批准目标连续完成，不因缺管理文件停工。


## 新增文件先确定唯一去处

写入前先判定文件用途，查现有归属配置，明确专题、稳定成果对象、现行母版与生命周期，再选择唯一文件夹。没有匹配类型时先提出归属并更新已有配置，不先把文件写在根目录或临时建Agent/任务/日期目录。需求与日志按现有日文件追加；研究正文按用途与对象持续维护，日期放文件名或元信息，不代替对象文件夹。

默认交付实际修订正文和必要图表，不每轮附带修改说明、逐句对照、编译检查或交付流水。用户明确要求的问答、独立评审和必要来源保留；专业依据在现有母版维护，过程原件留已有内部运行，不换名专题报告规避。成效目录根和各专题根只作阅读导航；专题内按配置的分类/对象放文件。源稿、专用图和附件随对象，跨成果共用图只有一份母版；编译临时文件与补丁不进成果区。

真实采用关系不明的稿件标待确认，不按日期、大小或“最新”字样自行认定当前稿。被替代版本成套只读保存，保持旧引用与恢复关系。历史具名决定原件精确保留，不作为新日记录生成入口。一次工作结束应核对新增文件均有明确归属，更新当前阅读入口，不额外生成管理报告。
