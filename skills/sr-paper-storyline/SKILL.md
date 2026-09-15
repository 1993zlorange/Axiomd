---
name: sr-paper-storyline
description: "SR-论文故事线设计：已有证据但稿件按代码模块或时间顺序堆积，需要形成问题到影响的论证主线时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-50"
  aspect: "论文与成果表达"
  short-description: "SR-论文故事线设计"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-论文故事线设计

Use this leaf Skill when: 已有证据但稿件按代码模块或时间顺序堆积，需要形成问题到影响的论证主线时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 按问题、缺口、假设、方法、证据、影响排列便签
2. 为每节写一句功能句
3. 检查每个段落只承担一个 message
4. 做反向提纲并删除不能推进主张的内容

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成故事线候选、反向提纲、发现断链和重复。

**Human intervention:** 博士生选择论文真正主线，决定舍弃哪些工作和次要结果。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 故事线：读者问题 / 缺口 / 假设 / 方法 / 关键证据 / 影响 / 章节功能

Recommended optional adapters: `nature-writing`, `research-paper-writing`, `academic-research-skills/academic-paper`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

主线从问题连续到证据与影响，每节功能唯一，所有核心图表有论证位置。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-methods-writing`, `$sr-experiments-writing`, `$sr-abstract-introduction`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
