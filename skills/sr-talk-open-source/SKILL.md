---
name: sr-talk-open-source
description: "SR-学术报告与开源成果：需要面向特定听众准备报告、演示、PPT、README 或可复现公开成果，或需要把文档转成每页有一句总结性话的模板化学术/组会汇报 PPT 时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-58"
  aspect: "论文与成果表达"
  short-description: "SR-学术报告与开源成果"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-学术报告与开源成果

Use this leaf Skill when: 需要面向特定听众准备报告、演示、PPT、README 或可复现公开成果，或需要把文档转成每页有一句总结性话的模板化学术/组会汇报 PPT 时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 明确听众、场合和希望记住的三点
2. 读取源文档并手工分组主题、提炼页题和证据映射
3. 选择三张核心图，画出页面骨架并亲自排练
4. 用上传模板生成/修改可编辑 PPT，保持讲稿、demo 和证据一致
5. 从干净环境运行 demo 或复现入口
6. 检查字体、颜色语义、图表、许可、引用、隐私、敏感数据和发布清单

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 解析源文档、生成逐页计划和 slides、讲稿、README 草案，执行模板匹配、字体字号、红/蓝/黑语义、一致性和可访问性检查。

**Human intervention:** 博士生现场演练、核对所有证据、确认模板版式和公开范围；发布动作需明确授权。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Document-to-PPT bridge

When converting documents into slides, read [references/document-to-ppt.md](references/document-to-ppt.md). First map every source claim to evidence and classify it as result, method, setup, limitation, or decision. Do not turn plans into results, local runs into reproducibility, or missing evidence into a polished claim.

Then read [references/group-meeting-ppt-standard.md](references/group-meeting-ppt-standard.md) and enforce:

- one complete, visible `SR58-SUMMARY` sentence on every page, placed separately from the page title;
- conclusion-first page titles, usually “完成了 XX ｜ 用 XX 方法 ｜ 实现了 XX”;
- 4–8 character parallel topic labels and visible ①②③ or 1. 2. 3. ordering;
- Microsoft YaHei throughout and bold titles;
- body ≥18pt; figure/table labels ≥14pt; split or delete instead of shrinking;
- only red/blue/black semantic emphasis: critical=red+bold+underline, important=blue+bold, normal=black, modifiers deleted or regular black;
- no more than three red items per page;
- result pages foreground results and let methods recede;
- bold table titles/headers; red for decisive facts, blue for important facts, black for context;
- unified repeated modules with changed numbers/conditions/status visibly highlighted;
- varied layout/density so consecutive pages do not become visually indistinct;
- preserved masters, layouts, placeholders, margins, footers, logos, and page numbering when using a supplied PPTX template.

For every page, record the optimized conclusion title, its one-sentence `SR58-SUMMARY`, evidence, `[级别]` + color style, visual/table decision, deletion/demotion list, and red count in [assets/ppt-page-plan.md](assets/ppt-page-plan.md). The deck draft is incomplete without this page plan.

If the user supplied a PPTX template, work on a copy and inspect its masters/layouts before writing. Never overwrite the source. The user’s explicit font-size and red/blue/black contract overrides inherited template styles for content; preserve layout geometry and decoration while adding explicit run formatting. Do not commit private templates, credentials, restricted figures, or machine-specific paths. If the local presentation tool cannot preserve PPTX structure, deliver the page plan and source mapping, and record the blocker instead of claiming template fidelity.

When Python is available, run `python skills/sr-talk-open-source/scripts/qa_group_meeting_pptx.py <deck.pptx>`. Fix all `ERROR` values; inspect and resolve or explicitly justify every `WARN`. Then render/inspect slides for overflow, readability, template fidelity, and semantic agreement.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture and [assets/ppt-page-plan.md](assets/ppt-page-plan.md) when a deck is requested. Name each artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 发布包：audience / three messages / document-to-slide plan / slides / demo / README / license / privacy checklist

Recommended optional adapters: `nature-paper2ppt`, `nature-figure`, `nature-data`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

受众主线清楚，每页有且仅有一句证据边界内的总结性话，逐页计划与证据一致，PPT 字体字号和红/蓝/黑语义通过检查或如实记录阻塞，demo 可运行，证据与引用准确，许可隐私审查完成且发布获授权。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-stage-archive`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
