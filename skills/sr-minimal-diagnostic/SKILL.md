---
name: sr-minimal-diagnostic
description: "SR-最小诊断实验：需要用最低成本、单一改动区分两个主要原因时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-46"
  aspect: "结果分析与问题诊断"
  short-description: "SR-最小诊断实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-最小诊断实验

Use this leaf Skill when: 需要用最低成本、单一改动区分两个主要原因时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 选择最影响路线的两个原因
2. 写出各自在同一设置下的相反预测
3. 只改变一个因素并保留对照
4. 运行低成本实验后更新原因概率和行动

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 估计信息增益、生成对照配置并检查混杂。

**Human intervention:** 博士生批准诊断实验，判断结果的因果限制以及是否需要复验。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 诊断卡：原因A/B / 区分预测 / 唯一改动 / 对照 / 结果 / 决策

Recommended optional adapters: `k-dense/hypothesis-generation`, `k-dense/experimental-design`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

实验确实区分原因，唯一变化与对照清晰，结果驱动明确的保留、排除或再诊断决定。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-mechanism-validation`, `$sr-core-hypothesis`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
