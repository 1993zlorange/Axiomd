---
name: sr-progress-narrative
description: "科研进展叙事化：把已验收的成果卡、交接记录和历史科研材料只读整理成导师能一遍读懂的研究时间线、逐点结论和通俗科研经历展示。Use only as a research-project-lead presentation aid; it must not create new scientific claims or replace source records."
metadata:
  skill-role: "research-project-lead-auxiliary"
  maintainer: "Axiom Agents maintainers"
  not-sr-work-package: true
---

Before any user-facing reply, read and apply [AGENTS.md](AGENTS.md). These rules govern chat wording; they do not override professional methods, safety requirements, or approved output templates.

# 科研进展叙事化

## 唯一责任

把项目内已经存在的成果卡、交接记录和历史材料，转成面向导师或同方向研究者的科研进展叙事展示：

```text
研究时间线
+ 逐时间点结论
+ 科研经历三阶段叙述
+ 当前位置与下一步
+ 事实 / 推断边界
```

本 Skill 是只读的派生视图工具，不是新的事实来源。

## 触发条件

用户要求做以下事情时使用：

- 梳理科研进展；
- 制作研究时间线或进展展示页；
- 叙述科研经历；
- 给导师看当前研究进展；
- 把成果卡整理成能一遍读懂的展示材料。

## 非目标

不要做以下事情：

- 不新增科学论断；
- 不修改成果卡、交接记录或原始实验材料；
- 不把本 Skill 的输出当作事实来源；
- 不制作论文核心图表（使用 `$sr-core-figures`）；
- 不生成 P0/P1 管理呈报（使用科研项目负责人的评估流程）；
- 不启动实验、外部服务或高成本计算。

## 必读规则

先读：

1. [references/rules.md](references/rules.md)
2. [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md)
3. [../sr-research-shared/references/body-writing-standard.md](../sr-research-shared/references/body-writing-standard.md)

若项目有本地 `AGENTS.md` 或成果目录规则，先读取并遵守其只读边界。

## 工作流程

1. **确认读者和用途**
   - 读者是谁：导师、同方向研究者、评审或普通听众；
   - 输出形式：HTML、Markdown、汇报页或对话内答复；
   - 时间范围：全程、治理期、某个阶段或自定义区间；
   - 科学边界：哪些内容必须保留“未定 / 无结论 / 待复核”。

2. **只读盘点材料**
   - 成果卡；
   - 交接记录；
   - 历史组会材料、实验报告或论文草稿；
   - 只在必要时引用工程证据，不复制或修改。

3. **建立数据源分级**
   - 记录事实：来自成果卡 frontmatter、状态字段或明确记录日期；
   - 推断信息：来自历史文件名、材料时间或不完整记录；
   - 事实和推断必须分栏或分标签，不得混用。

4. **梳理时间线**
   - 全程总览：按月或按阶段；
   - 重点时期详图：按日或按工作步骤；
   - 区分已完成、进行中、待执行和里程碑；
   - 每个条目必须能追溯到来源路径。

5. **补齐逐点结论**
   - 每个时间点写一句结论；
   - 结论只能来自成果卡“结论 / 发现 / 不能得出的结论”、交接记录或历史材料原文；
   - 提取不到结论时，只写能确认的事实，并标记“原文未给出结论”。

6. **通俗化改写**
   - 删除管理动作词和治理编号；
   - 展开专业对象、假设、方法、比较对象、预算、实验顺序和结果含义；
   - 英文术语首次出现时配中文解释；
   - 不弱化任何科学边界。

7. **制作展示**
   - 使用 [assets/output-template.md](assets/output-template.md) 的结构；
   - HTML 输出应单文件自包含、离线可用；
   - 甘特条目悬停应显示该时间点结论，不只显示文件名。

8. **渲染与内容验证**
   - 有浏览器工具时做实际渲染检查；
   - 检查布局溢出、重叠、悬停显示和页面横向滚动；
   - 用规则清单扫描行话、编号残留和逐点结论完整性；
   - 工具不可用时记录“渲染验证受阻”，不得声称通过。

9. **人工检查点**
   - 输出前请研究者确认：
     - 时间线是否符合材料；
     - 结论是否没有夸大；
     - 科学边界是否保留；
     - 导师是否能读懂。

## 权限和失败边界

- 默认只读：不修改科研材料；
- 输出文件只写入用户明确批准的位置；
- 缺少成果卡日期时，标记为推断，不伪造精确时间；
- 缺少结论时，标记“原文未给出结论”，不编造；
- 历史材料与成果卡冲突时，同时列出并请求人工判断；
- 无法渲染验证时，如实记录阻塞。

## 幂等性

重复运行时：

- 不覆盖已有人工确认版本；
- 新版本应引用旧版本；
- 只重新读取源材料；
- 输出文件名使用新的生产日期。

## 完成门

交付必须满足：

1. 输入材料和输出论断一一可追溯；
2. 事实与推断没有混用；
3. 每个时间点都有结论或明确说明没有结论；
4. 管理术语、治理编号和未解释代号已清除或展开；
5. 读者不需要了解项目内部流程也能读懂；
6. “未定、无性能结论、待复核”等边界没有被弱化；
7. HTML 或图表经过渲染检查，或如实记录无法验证；
8. 研究者已确认输出没有超出材料记载。

## 交付物

使用 [assets/output-template.md](assets/output-template.md)。

命名：

```text
YYYYMMDD-研究进展叙事-展示页.html
YYYYMMDD-研究进展叙事-成果卡.md
```

本 Skill 的成果卡是派生展示记录，不替代任何 SR 工作包成果卡。
