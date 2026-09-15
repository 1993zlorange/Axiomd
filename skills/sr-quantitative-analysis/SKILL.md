---
name: sr-quantitative-analysis
description: "SR-总体定量分析：主结果需要均值、方差、区间、效应量、检验和实际阈值解释时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-41"
  aspect: "结果分析与问题诊断"
  short-description: "SR-总体定量分析"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-总体定量分析

Use this leaf Skill when: 主结果需要均值、方差、区间、效应量、检验和实际阈值解释时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 明确 estimand 和分析单位
2. 检查统计假设与样本独立性
3. 手算一个小样例并复核脚本
4. 计算均值、区间、效应量并对预设阈值解释

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 执行统计、生成表图、检查多重比较和数值一致性。

**Human intervention:** 博士生选择检验与 estimand，解释实际意义、因果限制和结论强度。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 统计表：estimand / n / mean / CI / effect / test / correction / threshold

Recommended optional adapters: `k-dense/statistical-analysis`, `nature-statistics`, `nature-figure`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

分析单位和假设明确，数字可复核，统计与实际意义同时报告，结论不过界。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-slice-analysis`, `$sr-good-failure-cases`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
