---
name: sr-talk-open-source
description: "SR-学术报告与开源成果：需要面向特定听众准备报告、演示、README 或可复现公开成果时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-58"
  aspect: "论文与成果表达"
  short-description: "SR-学术报告与开源成果"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-学术报告与开源成果

Use this leaf Skill when: 需要面向特定听众准备报告、演示、README 或可复现公开成果时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 明确听众和希望记住的三点
2. 选择三张核心图并亲自排练
3. 从干净环境运行 demo 或复现入口
4. 检查许可、引用、隐私、敏感数据和发布清单

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成 slides、讲稿、README 草案和一致性/可访问性检查。

**Human intervention:** 博士生现场演练、核对所有证据并批准公开范围；发布动作需明确授权。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 发布包：audience / three messages / slides / demo / README / license / privacy checklist

Recommended optional adapters: `nature-paper2ppt`, `nature-figure`, `nature-data`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

受众主线清楚，demo 可运行，证据与引用准确，许可隐私审查完成且发布获授权。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-stage-archive`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
