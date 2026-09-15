---
name: sr-core-figures
description: "SR-核心图表制作：需要让一张图只传达一个可证据支持的结论，并用诚实编码呈现不确定性时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-53"
  aspect: "论文与成果表达"
  short-description: "SR-核心图表制作"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-核心图表制作

Use this leaf Skill when: 需要让一张图只传达一个可证据支持的结论，并用诚实编码呈现不确定性时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 先写这张图唯一要支持的结论
2. 选择与数据类型匹配的视觉编码
3. 手画草图和阅读顺序
4. 用脚本生成并逐点对原始数据核验

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 提供绘图代码、版式候选、色彩与可读性检查以及图注草案。

**Human intervention:** 博士生确认数据、误差条、单位、删点、图注和视觉编码不误导。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Figure brief：message / data / encoding / comparison / uncertainty / caption / export

Recommended optional adapters: `nature-figure`, `k-dense/scientific-visualization`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

图的 message 唯一，数据可追溯，误差和单位完整，视觉未夸大差异，导出可复现。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-abstract-introduction`, `$sr-internal-review`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
