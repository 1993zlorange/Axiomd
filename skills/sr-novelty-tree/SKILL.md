---
name: sr-novelty-tree
description: "SR-Novelty tree：需要按问题、表示、模型、训练、评价或应用层定位创新空间时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-11"
  aspect: "文献调研与领域结构"
  short-description: "SR-Novelty tree"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Novelty tree

Use this leaf Skill when: 需要按问题、表示、模型、训练、评价或应用层定位创新空间时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 将创新拆成多个可比较层级
2. 把已有工作放入相应单元
3. 标记拥挤区域、空白和可能的伪空白
4. 对候选空白重新执行最近邻检索

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成候选空白、同义表达和创新维度组合。

**Human intervention:** 博士生逐项核验最近邻，未经证据不得使用“首次”或“没有人做过”。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Novelty 矩阵：创新层 / 已有工作 / 密度 / 空白 / 可检验差异 / 风险

Recommended optional adapters: `nature-academic-search`, `k-dense/hypothesis-generation`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

候选创新与至少三个最近邻比较，差异可测，首次性措辞与检索证据匹配。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-challenge-insight-tree`, `$sr-nearest-neighbor-difference`, `$sr-core-hypothesis`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
