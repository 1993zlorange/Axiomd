---
name: sr-abstract-introduction
description: "SR-摘要与引言重写：核心证据已稳定，需要用具体问题、精确缺口、方法、定量结果和有边界贡献重写摘要或引言时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-54"
  aspect: "论文与成果表达"
  short-description: "SR-摘要与引言重写"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-摘要与引言重写

Use this leaf Skill when: 核心证据已稳定，需要用具体问题、精确缺口、方法、定量结果和有边界贡献重写摘要或引言时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 先对现有全文做反向提纲
2. 写具体问题、受众和精确缺口
3. 用最少句子写方法与决定性结果
4. 核对 novelty、数字、引用和影响边界

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 重组漏斗、压缩语言、生成中英草稿并检查主张重复。

**Human intervention:** 博士生保证 novelty、数字、引用和适用范围正确，批准最终措辞。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 摘要六句：背景 / 问题 / 缺口 / 方法 / 结果 / 影响与边界

Recommended optional adapters: `nature-writing`, `nature-polishing`, `research-paper-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

摘要与主结果一致，引言缺口有文献，关键数字可核验，贡献没有超出证据。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-internal-review`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
