---
name: pr-ar-01-project-architect
description: "把明确的软件需求变成可以实现和验证的结构、接口、数据与迁移方案；适用于新系统设计、现有系统调整和设计评审。"
---

# 软件架构与详细设计

沟通方式见 [AGENTS.md](AGENTS.md)：先说结果，用中文解释步骤、依据和限制。

## 什么时候用

把明确的软件需求变成可以实现和验证的结构、接口、数据与迁移方案；适用于新系统设计、现有系统调整和设计评审。按任务内容自然使用，不要求用户说出技能名或指定姓名。

## 先看什么

先读用户请求、适用的项目说明和直接相关的现有材料。已有决定继续有效，只询问会实质影响结果的缺失信息。

## 怎么做

1. 读需求、现有代码、部署配置和测试，分别说明目标行为与当前实际行为；缺失信息只在影响设计时提出。
2. 画出系统边界、外部依赖、数据流和主要运行过程，标明数据归谁写、哪里持久化、哪里检查权限。
3. 比较确实可行的方案，按复杂度、性能、维护成本和迁移难度推荐一个；小项目优先简单结构。
4. 逐个写清模块责任、调用关系、接口参数与响应、错误、状态变化、并发、事务及恢复方式。数据库设计包括字段类型、键、索引、约束、迁移和回滚。
5. 用正常、失败和边界场景走读设计，给出实施顺序、依赖和验证办法；检查每个必要需求都有实现位置。

仅做设计或评审时不改产品代码。兼容性、持久数据和权限变化要说明影响。使用实际项目技术栈，不照搬其他项目的数据库、目录或命名。

## 交付什么

按实际用途选用本目录模板，删除不适用部分；简单回答无需另存。过程记录按项目、上海记录日和规范类型定位唯一日文件，任务为独立条目，不按内容简述或运行ID拆文件；无真实内容不创建。正式方案、API说明、手册等实体文档按对象身份持续维护，不能换名规避日记录规则。

- [adr-template](assets/adr-template.md)
- [architecture-design-template](assets/architecture-design-template.md)
- [software-design-description-template](assets/software-design-description-template.md)

本目录的补充资料按任务需要阅读：
- [database-design-standard](references/database-design-standard.md)
- [design-review-checklist](references/design-review-checklist.md)
- [evidence-linked-design-standard](references/evidence-linked-design-standard.md)
- [python-architecture-guide](references/python-architecture-guide.md)
- [software-design-description-guide](references/software-design-description-guide.md)

## 怎么检查

设计能回答谁调用谁、数据如何流动、失败如何处理、如何验证；重要取舍有理由，未决定问题明确。

本技能直接完成其范围内工作，必要方法已写入本目录。使用现有工具，不递归调用其他技能，不为普通任务增加管理表、额外角色或重复确认。
