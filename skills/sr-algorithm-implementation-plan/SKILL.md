---
name: sr-algorithm-implementation-plan
description: "SR-算法伪代码与实现计划：公式或方法需要转成可编码步骤、接口、不变量、复杂度和测试计划时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-27"
  aspect: "技术方案与方法设计"
  short-description: "SR-算法伪代码与实现计划"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-算法伪代码与实现计划

Use this leaf Skill when: 公式或方法需要转成可编码步骤、接口、不变量、复杂度和测试计划时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 把公式逐项拆成执行步骤
2. 标出每步输入、输出、依赖和状态
3. 估算时间空间复杂度与缓存
4. 列出边界样例和最小单元测试

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 把公式转伪代码、寻找边界条件、生成接口和测试候选。

**Human intervention:** 博士生逐步核对没有改变算法语义，确认近似和实现取舍。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 算法卡：步骤 / 输入 / 输出 / 不变量 / 复杂度 / 缓存 / 测试

Recommended optional adapters: `research-paper-writing`, `k-dense/mathematical-modeling`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

伪代码可逐步映射回公式，边界与复杂度明确，测试覆盖关键不变量。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-resource-budget`, `$sr-baseline-unification`, `$sr-exploratory-experiment`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
