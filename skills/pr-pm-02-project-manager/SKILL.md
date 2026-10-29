---
name: pr-pm-02-project-manager
description: "编写需求说明、实施计划、功能介绍、用户手册或项目状态说明；用于把已有目标和材料整理成可执行、可验证的文档。"
---

# 需求文档与项目说明

沟通方式见 [AGENTS.md](AGENTS.md)：先说结果，用中文解释步骤、依据和限制。

## 什么时候用

编写需求说明、实施计划、功能介绍、用户手册或项目状态说明；用于把已有目标和材料整理成可执行、可验证的文档。按任务内容自然使用，不要求用户说出技能名或指定姓名。

## 先看什么

先读用户请求、适用的项目说明和直接相关的现有材料。已有决定继续有效，只询问会实质影响结果的缺失信息。

## 怎么做

1. 确认本次文档用途和读者，读取用户要求、现有文档、实现与测试；从已有材料解决可以查到的问题。
2. 按用途选择需求、计划、说明书或状态报告；只补齐当前文档需要的信息，不要求先运行另一套访谈。
3. 需求写清使用者、触发条件、输入、行为、输出和错误，区分必须、本次可选和以后再做。已有编号继续使用，没有时按需建立简单编号。
4. 计划列出有实际结果的步骤、依赖与完成条件；状态报告用实际产物和验证结果支撑。用户手册按真实操作顺序写，必要截图放在步骤旁。
5. 核对描述与实现、测试和现有决定是否一致；发现冲突分别记录文档目标与实际情况，给出影响和建议。

本技能不制作演示文稿，也不把编写文档当作实现、正式验收或发布。普通文字修改不重新发起需求审批。

## 交付什么

按实际用途选用本目录模板，删除不适用部分；简单回答无需另存。过程记录按项目、上海记录日和规范类型定位唯一日文件，任务为独立条目，不按内容简述或运行ID拆文件；无真实内容不创建。正式方案、API说明、手册等实体文档按对象身份持续维护，不能换名规避日记录规则。

- [feature-overview-template](assets/feature-overview-template.md)
- [prd-template](assets/prd-template.md)
- [requirements-document-template](assets/requirements-document-template.md)
- [software-srs-template](assets/software-srs-template.md)
- [user-manual-template](assets/user-manual-template.md)

本目录的补充资料按任务需要阅读：
- [document-output-standard](references/document-output-standard.md)
- [documentation-suite-guide](references/documentation-suite-guide.md)
- [prd-guide](references/prd-guide.md)
- [software-srs-guide](references/software-srs-guide.md)

## 怎么检查

需求可测试、步骤可执行、来源可定位，未实现和未验证部分明确；不编造日期、预算或完成比例。

本技能直接完成其范围内工作，必要方法已写入本目录。使用现有工具，不递归调用其他技能，不为普通任务增加管理表、额外角色或重复确认。
