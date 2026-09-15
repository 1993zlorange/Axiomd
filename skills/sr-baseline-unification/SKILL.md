---
name: sr-baseline-unification
description: "SR-Baseline统一实现：多个基线需要在同一数据、训练循环、预算、评价和日志接口下公平实现时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-26"
  aspect: "技术方案与方法设计"
  short-description: "SR-Baseline统一实现"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Baseline统一实现

Use this leaf Skill when: 多个基线需要在同一数据、训练循环、预算、评价和日志接口下公平实现时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 冻结统一数据读取与 split
2. 统一训练循环、预算和评价脚本
3. 只替换模型或算法核心
4. 运行最小基线并与独立手算或原实现对照

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 重构公共接口、生成比较配置、检查泄漏和预算不一致。

**Human intervention:** 博士生核验公平性、与论文原实现的差异以及哪些改动可接受。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Baseline契约：split / seed / budget / metric / tuning / log / acceptance

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

基线只在声明维度变化，统一日志可复现，至少一个小样例和原文/原实现差异被解释。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-baseline-reproduction`, `$sr-main-comparison`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
