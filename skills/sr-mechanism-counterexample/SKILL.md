---
name: sr-mechanism-counterexample
description: "SR-机制推演与反例构造：需要从机制导出预测、用极端条件和反例挑战 Idea 时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-19"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-机制推演与反例构造"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-机制推演与反例构造

Use this leaf Skill when: 需要从机制导出预测、用极端条件和反例挑战 Idea 时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 手工写出完整因果链
2. 从各环节导出可观测预测
3. 构造极端条件、边界情况和反例
4. 比较主机制与替代解释的不同结果

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 扮演反方、扩展反例、寻找因果跳步和隐藏假设。

**Human intervention:** 博士生确认反例符合领域规律，判断哪些失败会推翻或只限制假设。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 机制—反例表：环节 / 假设 / 预测 / 反例 / 替代解释 / 区分证据

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

关键机制经过至少一个强反例检验，因果跳步显式化，区分证据可执行。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-minimal-falsification`, `$sr-mathematical-model`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
