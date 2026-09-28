---
name: sr-talk-open-source
description: "SR-学术报告与开源成果：需要面向特定听众准备报告、演示、PPT、README 或可复现公开成果，或需要把文档转成结构化编号、按认知对象拆页、每页有一句总结性话的模板化学术/组会汇报 PPT 时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-58"
  aspect: "论文与成果表达"
  short-description: "SR-学术报告与开源成果"
---

Before any user-facing reply, read and apply [AGENTS.md](AGENTS.md). These rules govern chat wording; they do not override professional methods, safety requirements, or approved output templates.

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-学术报告与开源成果

Use this leaf Skill when: 需要面向特定听众准备报告、演示、PPT、README 或可复现公开成果，或需要把文档转成结构化编号、按认知对象拆页、每页有一句总结性话的模板化学术/组会汇报 PPT 时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md) and [../sr-research-shared/references/body-writing-standard.md](../sr-research-shared/references/body-writing-standard.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 明确听众、场合、汇报模式和希望记住的三点
2. 读取源文档，映射证据覆盖，按认知对象分组而不是按字数切页
3. 为每页写出 kicker 编号、结论式页题和一句可证据支持的总结性话
4. 选择版式和逻辑图骨架，画出页面结构并亲自排练
5. 用上传模板生成或修改可编辑 PPT，保持讲稿、demo 和证据一致
6. 从干净环境运行 demo 或复现入口
7. 检查排版布局、配文配色、逻辑图、标题编号、许可、引用、隐私、敏感数据和发布清单
8. 若有人工修改版，复盘页面映射与可复用规则

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 解析源文档，生成证据覆盖矩阵、认知对象拆页、结构化编号、逐页计划、slides、讲稿、README 草案，并执行模板匹配、排版布局、字体字号、红/蓝/黑语义、逻辑图和一致性检查。

**Human intervention:** 博士生现场演练、核对所有证据、确认模板版式、认知拆页和公开范围；发布动作需明确授权。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Document-to-PPT bridge

When converting documents into slides, read [references/document-to-ppt.md](references/document-to-ppt.md). First map every source claim to evidence, classify the evidence coverage, choose the presentation mode, and classify every page by one primary cognitive object. Do not turn plans into results, local runs into reproducibility, or missing evidence into a polished claim.

Then read [references/group-meeting-ppt-standard.md](references/group-meeting-ppt-standard.md) and enforce:

- one complete, visible `SR58-SUMMARY` sentence on every page, placed separately from the page title;
- one primary `cognitive_type` per page: claim, context, artifact, mechanism, role, process, architecture, case, metric, risk, reflection, decision, or backup;
- cognitive-object splitting before word-count trimming: role mapping, process flow, architecture, concrete evidence, result, reflection, and unverified plan occupy separate pages when they compete;
- a separate structural kicker plus a conclusion title, for example `2.2 机制②` + `角色制衡避免单模型自我强化`;
- artifact-first order for group-meeting process reviews: advisor context → key conclusion → agenda → artifact evidence → motivation → mechanisms → practice cases → reflection → next plan;
- 4–8 character parallel topic labels and visible ①②③ or 1. 2. 3. ordering;
- Microsoft YaHei throughout and bold titles;
- body ≥18pt; figure/table labels ≥14pt; split by cognitive object or delete instead of shrinking;
- only red/blue/black semantic emphasis: critical=red+bold+underline, important=blue+bold, normal=black, modifiers deleted or regular black;
- no more than three red items per page;
- result pages foreground results and let methods recede;
- bold table titles/headers; red for decisive facts, blue for important facts, black for context;
- unified repeated modules with changed numbers/conditions/status visibly highlighted;
- varied layout/density so consecutive pages do not become visually indistinct;
- preserved masters, layouts, placeholders, margins, footers, logos, and page numbering when using a supplied PPTX template.

For layout selection read [references/ppt-layout-system.md](references/ppt-layout-system.md). Choose `claim`, `evidence-screenshot`, `mechanism-map`, `process-flow`, `architecture`, `case`, or `reflection`; record text/visual area ratios and the split check. A page that needs two summaries, has two cognitive objects, more than 12 diagram nodes, or more than three branches must be split unless the page plan records a reviewed exception.

For any flowchart, mechanism map, architecture, or case loop, read [references/logic-diagram-style.md](references/logic-diagram-style.md). Use short nodes, stable numbering, one dominant path, explicit human gates, meaningful loops, and fixed red/blue/black arrow semantics.

For every page, record the kicker, conclusion title, primary cognitive type, layout pattern, its one-sentence `SR58-SUMMARY`, evidence, `[级别]` + color style, visual contract, split check, deletion/demotion list, and red count in [assets/ppt-page-plan.md](assets/ppt-page-plan.md). The deck draft is incomplete without this page plan.

## Human revision retrospective

When the user supplies an AI draft and a human-revised deck or PDF, read [references/human-revision-retrospective.md](human-revision-retrospective.md). Compare page mapping, layout, title numbering, text density, color semantics, diagram style, evidence order, and cognitive-object splitting. Record one-off preferences separately from candidate and stable rules. Do not store private source files, local paths, credentials, or restricted project evidence in this repository.

## Template and presentation-tool rules

If the user supplied a PPTX template, work on a copy and inspect its masters/layouts before writing. Never overwrite the source. The user’s explicit font-size and red/blue/black contract overrides inherited template styles for content; preserve layout geometry and decoration while adding explicit run formatting. Do not commit private templates, credentials, restricted figures, or machine-specific paths. If the local presentation tool cannot preserve PPTX structure, deliver the page plan and source mapping, and record the blocker instead of claiming template fidelity.

When Python is available, run `python skills/sr-talk-open-source/scripts/qa_group_meeting_pptx.py <deck.pptx> --page-plan <page-plan.md>`. Fix all `ERROR` values; inspect and resolve or explicitly justify every `WARN`. Then render/inspect slides for overflow, readability, template fidelity, layout pattern, diagram semantics, and claim agreement.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture and [assets/ppt-page-plan.md](assets/ppt-page-plan.md) when a deck is requested. Name each artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 发布包：audience / presentation mode / three messages / evidence coverage / cognitive-object page plan / per-page summary sentence / slides / demo / README / license / privacy checklist

本地 [assets/output-template.md](assets/output-template.md) 是强制的记录骨架；正文必须执行 [../sr-research-shared/references/body-writing-standard.md](../sr-research-shared/references/body-writing-standard.md) 的十条写作标准。上面的一行结构只提示专业交付物。

Recommended optional adapters: `nature-paper2ppt`, `nature-figure`, `nature-data`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

受众主线清楚，证据覆盖可追踪，每页有唯一认知对象、结构化编号、结论式页题和一句证据边界内的总结性话；排版布局、逻辑图、字体字号和红/蓝/黑语义通过检查或如实记录阻塞；人工修改已按规则复盘（如有）；demo 可运行，证据与引用准确，许可隐私审查完成且发布获授权。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-stage-archive`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
