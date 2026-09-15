---
name: sr-solution-gap-analysis
description: "SR-现有方案差距分析：需要证明现有方法在同一条件下存在可验证不足，而不是泛泛声称研究空白时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-04"
  aspect: "研究问题与选题"
  short-description: "SR-现有方案差距分析"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-现有方案差距分析

Use this leaf Skill when: 需要证明现有方法在同一条件下存在可验证不足，而不是泛泛声称研究空白时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 找到二至三项最近邻工作
2. 逐篇阅读方法、实验条件和局限原文
3. 在同一维度与条件下比较
4. 写出可被实验或分析验证的差距

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 构建对比矩阵、追踪引用、提醒条件不一致和伪差距。

**Human intervention:** 博士生回原文核对页码、图表、实验条件和作者真实结论。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Gap 矩阵：工作 / 假设 / 输入 / 输出 / 条件 / 证据 / 失效 / 差距

Recommended optional adapters: `nature-academic-search`, `nature-paper-card`, `academic-research-skills/deep-research`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每个差距均绑定原文证据和同维比较，并能转成研究问题或验证行动。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-value-feasibility`, `$sr-research-question-review`, `$sr-search-strategy`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
