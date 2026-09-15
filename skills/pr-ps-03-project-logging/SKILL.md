---
name: pr-ps-03-project-logging
description: 在项目原子操作或运行批次结束后维护事实日志、用户可见变更和成本时间记录。适用于完成、失败、跳过和阻塞状态；不把计划、需求或推测混入事实日志。
---

# PS-03 项目记账

读取主监理[需求日志反思机制](../pr-ps-00-project-supervision/references/20260912-需求日志反思机制-管理规范.md)和[文件命名与归属规范](../pr-ps-00-project-supervision/references/20260912-文件命名与归属-管理规范.md)。从当前操作的任务 ID、实际变更、命令、证据和时间数据生成日志；用户可见变化同步变更记录，可观测成本同步成本时间记录。

使用 [中文空白模板](assets/20260912-项目记账-输出模板.md)，按项目 `AGENTS.md` 分别写入日志、变更和成本目录。文件命名为 `YYYYMMDD-内容简述-日志.md`、`YYYYMMDD-内容简述-变更记录.md`或`YYYYMMDD-内容简述-统计.md`。

每条记录必须独立填写 `why`、`expected_impact`、`actual_impact`、`affected_requirements`、`affected_files`、`affected_downstream` 和 `decision_basis`。目标不是原因，结果不是影响；未执行项、推测和事实分别记录。

不补造缺失时间、费用、测试或发布状态。补记历史只依据仓库、运行和测试证据，且不覆盖原记录。
