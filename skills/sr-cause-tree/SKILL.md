---
name: sr-cause-tree
description: "SR-候选原因树：同一异常有多个候选原因，需要用差异预测和实验逐步排除时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-45"
  aspect: "结果分析与问题诊断"
  short-description: "SR-候选原因树"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-候选原因树

Use this leaf Skill when: 同一异常有多个候选原因，需要用差异预测和实验逐步排除时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 准确描述现象而不夹带解释
2. 列出多个相互竞争原因
3. 为每个原因写不同可观测预测
4. 选择能区分分支的验证并更新状态

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 扩展原因树、检查不可证伪原因、生成区分实验候选。

**Human intervention:** 博士生剔除违背领域规律或不可测原因，设定原因优先级。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 原因树节点：现象 / 原因 / 预测 / 验证 / 状态 / 证据 / 下一步

Recommended optional adapters: `k-dense/hypothesis-generation`, `k-dense/mathematical-modeling`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

至少两个原因有可区分预测，树状态随证据更新，不把未排除写成已确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-minimal-diagnostic`, `$sr-mechanism-validation`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
