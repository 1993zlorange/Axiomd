---
name: sr-ablation-study
description: "SR-消融实验：需要验证各方法组件的必要性、增益和声称机制时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-35"
  aspect: "实验设计与执行"
  short-description: "SR-消融实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-消融实验

Use this leaf Skill when: 需要验证各方法组件的必要性、增益和声称机制时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 从模块—挑战矩阵取出预测
2. 每次只移除或替换一个组件
3. 保持数据、预算和其余配置不变
4. 同时检查总体、局部指标和多种子波动

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成消融矩阵、执行统计、检查并非单一变化的变体。

**Human intervention:** 博士生判断结果是否支持机制，避免把相关性写成因果贡献。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 消融表：变体 / 唯一变化 / 机制预测 / 指标 / CI / 结论 / 边界

Recommended optional adapters: `k-dense/experimental-design`, `k-dense/statistical-analysis`, `nature-statistics`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每个关键组件有公平变体，变化唯一，结果与机制预测对齐或明确冲突。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-mechanism-validation`, `$sr-claim-boundary-decision`, `$sr-minimal-diagnostic`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
