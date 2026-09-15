---
name: sr-nearest-neighbor-difference
description: "SR-最近邻差异分析：已有 Idea 需要与最接近工作逐维比较并确认哪些部分不构成创新时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-17"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-最近邻差异分析"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-最近邻差异分析

Use this leaf Skill when: 已有 Idea 需要与最接近工作逐维比较并确认哪些部分不构成创新时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 找到最接近的三项工作
2. 比较问题、机制、信息、监督和证据
3. 标出完全相同、局部不同和未验证部分
4. 为每个声称差异写验证方法

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成逐维对比和可能忽略的邻居或同义方法。

**Human intervention:** 博士生逐项回原文，能够接受当前 Idea 没有实质创新的结论。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 最近邻表：维度 / 本工作 / 邻居1～3 / 相同点 / 差异 / 验证方法

Recommended optional adapters: `nature-academic-search`, `nature-paper-card`, `k-dense/hypothesis-generation`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

最近邻证据可追溯，非创新部分明确，剩余差异可通过实验或理论检查。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-idea-decomposition`, `$sr-idea-prioritization`, `$sr-search-strategy`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
