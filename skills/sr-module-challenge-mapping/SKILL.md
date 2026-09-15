---
name: sr-module-challenge-mapping
description: "SR-模块—挑战对应设计：方法模块较多，需要证明每个模块解决哪个挑战并预设消融时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-24"
  aspect: "技术方案与方法设计"
  short-description: "SR-模块—挑战对应设计"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-模块—挑战对应设计

Use this leaf Skill when: 方法模块较多，需要证明每个模块解决哪个挑战并预设消融时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 为每个挑战指定一个主要负责模块
2. 写出模块必要性和机制预测
3. 删除没有假设支持的模块
4. 为保留模块预设移除或替换消融

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 检查多对多映射、冗余模块和无法区分的机制。

**Human intervention:** 博士生确认模块确实可能影响预测，决定删减和消融优先级。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 对应矩阵：问题 / 挑战 / 模块 / 机制 / 预测 / 消融 / 判据

Recommended optional adapters: `k-dense/hypothesis-generation`, `k-dense/experimental-design`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每个模块有挑战、机制预测与消融判据，无孤立模块或未覆盖核心挑战。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-data-schema-freeze`, `$sr-baseline-unification`, `$sr-algorithm-implementation-plan`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
