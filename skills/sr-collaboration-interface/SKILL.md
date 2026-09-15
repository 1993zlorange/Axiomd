---
name: sr-collaboration-interface
description: "SR-多人接口协调：多人或系统之间需要冻结字段、单位、目录、版本、样例和验收接口时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-63"
  aspect: "项目推进与下一步计划"
  short-description: "SR-多人接口协调"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-多人接口协调

Use this leaf Skill when: 多人或系统之间需要冻结字段、单位、目录、版本、样例和验收接口时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 让生产者与消费者共同列接口需求
2. 冻结字段、单位、目录、版本和样例
3. 双方评审正常、边界和错误样例
4. 执行契约测试并记录每次变更

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成接口文档、样例、契约测试草案和影响分析。

**Human intervention:** 博士生组织双方确认、处理冲突和批准破坏性变更。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 接口契约：producer / consumer / schema / unit / version / example / test / change

Recommended optional adapters: `k-dense/mathematical-modeling`, `academic-research-skills/academic-pipeline`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

生产者消费者共同签认，样例和契约测试通过，变更有版本、影响与迁移方案。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-resource-scheduling`, `$sr-task-decomposition`, `$sr-blocker-resolution`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
