---
name: sr-core-figures
description: "SR-核心图表制作：需要为科研数据、导师汇报或论文制作一图一结论的核心图，诚实呈现原始点、不确定性、单位和图例，或生成/修改可编辑的科研 draw.io 示意图、方法流程图、技术路线图和机制图时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-53"
  aspect: "论文与成果表达"
  short-description: "SR-核心图表制作"
---

Before any user-facing reply, read and apply [AGENTS.md](AGENTS.md). These rules govern chat wording; they do not override professional methods, safety requirements, or approved output templates.

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-核心图表制作

Use this leaf Skill when: 需要为科研数据、导师汇报或论文制作一图一结论的核心图，诚实呈现原始点、不确定性、单位和图例，或需要生成/修改可编辑的科研 draw.io 示意图、方法流程图、技术路线图和机制图时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md) and [../sr-research-shared/references/body-writing-standard.md](../sr-research-shared/references/body-writing-standard.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 先填写图表约定：唯一结论、证据角色、数据来源、样本量、对照、单位、不确定性和结论边界
2. 按图型选择表达和脱敏参考图：成本、对照、配对、误差结构、参数覆盖、场分布、长期稳定性或方法定位
3. 手画草图并确定阅读顺序、面板关系和阅读路径
4. 把研究对象转成拓扑、网格布局和语义图形方案
5. 生成绘图代码或可编辑 draw.io 源，保持颜色、线型、点形、公式、单位和数据映射可追溯
6. 检查数据不变量、图例间距、多面板理由、导出预览和人工复核结论

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 提供图表约定、绘图代码或 draw.io XML、版式和路由候选、语义图形、公式排版、色彩与图例可读性检查、导出预览 QA 和图注草案。

**Human intervention:** 博士生确认数据、删点、样本量、误差条、单位、图注、视觉编码、图例间距、箭头因果解释、结论边界和 draw.io 版式不误导。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Scientific data figure authoring

Before writing chart code, complete the chart brief in [assets/figure-contract-template.md](assets/figure-contract-template.md). Read [references/scientific-figure-authoring.md](references/scientific-figure-authoring.md) for the claim/evidence workflow, data invariants, archetypes, visual grammar, legend spacing, and reproducible Python/Matplotlib style. For an advisor report, also read [references/advisor-figure-patterns.md](references/advisor-figure-patterns.md), and inspect the closest synthetic PNG in [references/figure-pattern-exemplars.md](references/figure-pattern-exemplars.md). For publication-style topology or field-figure structure, also read [references/paper-figure-patterns.md](references/paper-figure-patterns.md); use it only as an abstract style reference and never copy copyrighted artwork.

Core workflow:

```text
fix one claim and one evidence role
→ choose the chart archetype
→ preserve raw points, sample size, comparison, units, and uncertainty
→ define color/line/marker/field encodings and the boxed legend
→ justify every panel and panel letter
→ export SVG/PDF from the versioned script/source
→ run brief checks and visual QA
→ obtain user/advisor review
```

Before closing a data figure, run `python skills/sr-core-figures/scripts/qa_scientific_figure.py <figure-contract.md> --figure <figure.svg>` when Python is available. Fix every `ERROR`; resolve or explicitly justify every `WARN`. If export is genuinely blocked, record `export_status=blocked` and the reason rather than claiming visual QA passed.

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

Use this template: Figure brief：claim / evidence role / data source / sample size / comparison / encoding / units / uncertainty / boundary / legend / panel logic / export QA / caption

本地 [assets/output-template.md](assets/output-template.md) 是强制的记录骨架；正文必须执行 [../sr-research-shared/references/body-writing-standard.md](../sr-research-shared/references/body-writing-standard.md) 的十条写作标准。上面的一行结构只提示专业交付物。

Optional implementation aid: `k-dense/scientific-visualization`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using it. Missing adapters are not a blocker; the scientific-figure workflow in this Skill is self-contained.

## Completion gate

图的结论唯一且不过界，数据、样本量、单位和不确定性可追溯，原始点和汇总不隐藏，颜色、线型、点形和图例可识别且不遮挡，多面板有直接比较理由；绘图源或 draw.io 源可复现，导出预览通过或如实记录阻塞。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-abstract-introduction`, `$sr-internal-review`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
