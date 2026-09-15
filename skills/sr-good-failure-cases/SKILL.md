---
name: sr-good-failure-cases
description: "SR-Good与Failure case分析：需要用代表性成功、普通和失败案例理解模型行为与误差模式时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-43"
  aspect: "结果分析与问题诊断"
  short-description: "SR-Good与Failure case分析"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Good与Failure case分析

Use this leaf Skill when: 需要用代表性成功、普通和失败案例理解模型行为与误差模式时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 在看具体案例前写选择规则
2. 抽取成功、普通与失败样本
3. 叠加输入、真值、预测和误差
4. 人工检查数据正确性并归纳共性

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 排序案例、自动组图、提取共同特征和候选原因。

**Human intervention:** 博士生确认案例代表性、排除数据错误和挑例偏差，判断领域解释。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 案例卡：选择规则 / 输入特征 / 真值 / 预测 / 误差 / 共性 / 假设

Recommended optional adapters: `k-dense/exploratory-data-analysis`, `nature-figure`, `nature-paper-card`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

案例按规则选择且可定位，数据已核查，共性转成可证伪原因而非故事。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-error-decomposition`, `$sr-cause-tree`, `$sr-minimal-diagnostic`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
