---
name: sr-core-figures
description: "SR-核心图表制作：需要让一张核心图只传达一个可证据支持的结论、用诚实编码呈现不确定性，或需要生成/修改可编辑的科研 draw.io 示意图、方法流程图、技术路线图和机制图时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-53"
  aspect: "论文与成果表达"
  short-description: "SR-核心图表制作"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-核心图表制作

Use this leaf Skill when: 需要让一张核心图只传达一个可证据支持的结论、用诚实编码呈现不确定性，或需要生成/修改可编辑的科研 draw.io 示意图、方法流程图、技术路线图和机制图时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 先写这张图唯一要支持的结论
2. 选择与数据类型匹配的视觉编码
3. 手画草图并确定阅读顺序
4. 把研究对象转成拓扑、网格布局和语义图形方案
5. 用可编辑 draw.io 源生成图形并保持边、公式、单位和数据映射可追溯
6. 对原始数据、源 XML 和导出预览逐项核验

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 提供绘图代码或 draw.io XML、版式和路由候选、语义图形、公式排版、色彩与可读性检查、导出预览 QA 以及图注草案。

**Human intervention:** 博士生确认数据、误差条、单位、删点、图注、视觉编码、箭头因果解释和 draw.io 版式不误导。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Draw.io scientific authoring

Use `.drawio` as the editable primary source whenever the requested core figure is a workflow, technical route, mechanism, architecture, cohort flow, or graphical abstract (or when the user asks for draw.io). Before writing or editing XML, read [references/drawio-authoring.md](references/drawio-authoring.md). When choosing topology, shapes, color, semantic glyphs, labels, formulas, or accessibility, read [references/drawio-visual-language.md](references/drawio-visual-language.md). Before closing a draw.io task, read [references/drawio-export-qa.md](references/drawio-export-qa.md).

Core invariants:

- Build from the scientific message and topology; do not start from a decorative template.
- Prefer uncompressed mxGraph XML, stable descriptive IDs, attached source/target edges, grid-aligned geometry, reserved routing corridors, and editable semantic glyphs.
- Put formulas in dedicated cells and set `math="1"` on `mxGraphModel` when formula-like labels exist.
- Preserve existing pages, IDs, grouping, geometry, and unrelated content when editing; make a structural-edit baseline available.
- Run `python skills/sr-core-figures/scripts/qa_drawio.py <figure.drawio>` when Python is available. Fix all `ERROR` values; inspect and resolve or explicitly justify every `WARN`.
- Export SVG/PNG/PDF only through diagrams.net/draw.io so preview evidence corresponds to the source. If the desktop CLI is unavailable, deliver the source and record `preview_export=blocked`; never claim visual QA passed.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, draw.io QA, and human verdicts explicit.

Use this template: Figure brief：message / data / encoding / comparison / uncertainty / drawio topology / export QA / caption

Recommended optional adapters: `nature-figure`, `k-dense/scientific-visualization`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback. This Skill itself provides the draw.io fallback workflow.

## Completion gate

图的 message 唯一，数据可追溯，误差和单位完整，视觉未夸大差异；draw.io 源可打开、边端点有效、布局无遮挡，公式和导出预览按环境完成或如实记录阻塞，导出可复现。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-abstract-introduction`, `$sr-internal-review`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
