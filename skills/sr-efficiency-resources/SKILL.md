---
name: sr-efficiency-resources
description: "SR-效率与资源实验：需要量化数据生成、训练、推理、显存、能耗或端到端精度成本权衡时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-38"
  aspect: "实验设计与执行"
  short-description: "SR-效率与资源实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-效率与资源实验

Use this leaf Skill when: 需要量化数据生成、训练、推理、显存、能耗或端到端精度成本权衡时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 把数据生成、训练、推理和端到端成本分开
2. 统一硬件、批量、预热和计时区间
3. 重复计时并记录环境
4. 结合精度找到 Pareto 前沿和盈亏点

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 自动计时、汇总资源、绘制 Pareto 图并检查比较口径。

**Human intervention:** 博士生确认计时公平，判断计算节省是否抵消前置成本并支撑工程 claim。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 资源结果：阶段 / 硬件 / batch / 时间 / 显存 / 能耗 / 精度 / 盈亏点

Recommended optional adapters: `k-dense/statistical-analysis`, `nature-figure`, `nature-experiment-log`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

计时协议可重复，硬件批量透明，前置成本未遗漏，效率 claim 有适用规模。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-quantitative-analysis`, `$sr-core-figures`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
