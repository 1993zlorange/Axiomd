---
name: sr-generalization-ood
description: "SR-泛化与OOD实验：需要区分跨参数、跨几何、跨类别、跨设备或其他 OOD 泛化 claim 时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-37"
  aspect: "实验设计与执行"
  short-description: "SR-泛化与OOD实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-泛化与OOD实验

Use this leaf Skill when: 需要区分跨参数、跨几何、跨类别、跨设备或其他 OOD 泛化 claim 时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 明确写出泛化类型和距离概念
2. 独立构造 ID 与 OOD 划分
3. 按组运行并报告覆盖与不确定性
4. 检查 failure case 和泄漏后限制 claim

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 检查分组、距离、覆盖和泄漏，自动汇总各 OOD 子组。

**Human intervention:** 博士生确认 OOD 定义符合领域现实，决定 claim 只能覆盖哪些类型。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: OOD卡：分布定义 / 距离 / split / 指标 / 覆盖 / failure / 适用边界

Recommended optional adapters: `k-dense/experimental-design`, `k-dense/exploratory-data-analysis`, `k-dense/statistical-analysis`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

OOD 定义预先明确，无泄漏，覆盖可解释，结论不把一种泛化偷换成另一种。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-slice-analysis`, `$sr-good-failure-cases`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
