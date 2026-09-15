---
name: sr-slice-analysis
description: "SR-分组与切片分析：总体均值可能掩盖不同几何、参数、类别、难度或数据来源上的差异时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-42"
  aspect: "结果分析与问题诊断"
  short-description: "SR-分组与切片分析"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-分组与切片分析

Use this leaf Skill when: 总体均值可能掩盖不同几何、参数、类别、难度或数据来源上的差异时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 优先写出预定义切片和领域理由
2. 检查每组样本量与覆盖
3. 按同一指标和不确定性比较
4. 区分预注册发现与事后探索

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 枚举候选切片、计算分组统计、可视化和提醒小样本风险。

**Human intervention:** 博士生防止事后挑组，判断切片是否有领域含义并限制解释。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 切片表：维度 / 组 / n / 覆盖 / 指标 / CI / 风险 / 是否预注册

Recommended optional adapters: `k-dense/exploratory-data-analysis`, `k-dense/statistical-analysis`, `nature-figure`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

切片规则和样本量透明，事后分析已标记，多重比较与过度解读受控。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-good-failure-cases`, `$sr-error-decomposition`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
