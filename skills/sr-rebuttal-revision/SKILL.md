---
name: sr-rebuttal-revision
description: "SR-Rebuttal与修订：审稿意见已拆解，需要逐点回复、补证据、修改稿件并闭环追踪时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-57"
  aspect: "论文与成果表达"
  short-description: "SR-Rebuttal与修订"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Rebuttal与修订

Use this leaf Skill when: 审稿意见已拆解，需要逐点回复、补证据、修改稿件并闭环追踪时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 每条先写直接回答结论
2. 再给现有或新增证据
3. 标出稿件具体修改位置
4. 更新稿件、逐条闭环并由合作者复核

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 起草逐点回复、维护追踪表、检查遗漏和口径冲突。

**Human intervention:** 博士生批准论证、实验承诺、礼貌程度和最终措辞；合作者确认对外提交。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 回复模板：Comment / Response / Evidence / Change / Location / Residual limitation

Recommended optional adapters: `nature-response`, `academic-research-skills/academic-paper`, `research-paper-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

所有意见逐条闭环，回复与稿件一致，新增实验有证据，承诺和提交经人批准。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-internal-review`, `$sr-talk-open-source`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
