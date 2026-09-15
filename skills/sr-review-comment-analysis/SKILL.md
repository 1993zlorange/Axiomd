---
name: sr-review-comment-analysis
description: "SR-审稿意见拆解：收到审稿意见，需要逐条识别表面问题、真实诉求、证据缺口和回应风险时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-56"
  aspect: "论文与成果表达"
  short-description: "SR-审稿意见拆解"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-审稿意见拆解

Use this leaf Skill when: 收到审稿意见，需要逐条识别表面问题、真实诉求、证据缺口和回应风险时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 逐条编号并保留原文
2. 分类为误解、表达、实验、方法、创新或范围
3. 写出每条意见背后的真实诉求
4. 合并重复项并按影响 claim 的严重度排序

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 结构化意见、识别冲突、关联稿件位置和现有证据。

**Human intervention:** 博士生判断意见合理性、编辑意图和回应策略，不让 AI 替作者承诺。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 意见矩阵：reviewer / comment / underlying ask / evidence / action / risk / status

Recommended optional adapters: `nature-response`, `academic-research-skills/academic-paper-reviewer`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每条意见有真实诉求、证据和行动，冲突意见显式呈现，承诺均待人确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-rebuttal-revision`, `$sr-minimal-falsification`, `$sr-main-comparison`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
