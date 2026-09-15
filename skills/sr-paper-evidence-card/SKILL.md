---
name: sr-paper-evidence-card
description: "SR-单篇深读与证据卡片：需要深读一篇关键论文并区分作者主张、直接证据、局限与可复现信息时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-09"
  aspect: "文献调研与领域结构"
  short-description: "SR-单篇深读与证据卡片"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-单篇深读与证据卡片

Use this leaf Skill when: 需要深读一篇关键论文并区分作者主张、直接证据、局限与可复现信息时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 完整通读并写一段无 AI 摘要
2. 拆出问题、假设、方法、实验和结论
3. 标注关键页码、公式、图表和引用
4. 写批判笔记、复现疑点和可衍生 Idea

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 提取结构、生成 claim-evidence 映射、查术语和提出疑点。

**Human intervention:** 博士生回原文核对所有关键引文，判断证据是否真正支持作者声明。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Paper Card：定位 / RQ / 方法 / 数据 / claim-evidence / 局限 / 复现 / Idea

Recommended optional adapters: `nature-paper-card`, `nature-reader`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

卡片能定位原文证据，事实与解读分开，至少记录一个局限或复现判断。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-literature-tree`, `$sr-novelty-tree`, `$sr-nearest-neighbor-difference`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
