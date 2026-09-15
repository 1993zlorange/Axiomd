---
name: sr-data-split
description: "SR-数据划分设计：训练验证测试或 ID/OOD 划分需要匹配目标 claim 并排除泄漏时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-31"
  aspect: "实验设计与执行"
  short-description: "SR-数据划分设计"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-数据划分设计

Use this leaf Skill when: 训练验证测试或 ID/OOD 划分需要匹配目标 claim 并排除泄漏时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 根据研究问题选择划分单位和类型
2. 手工检查重复体、近邻和上游关联
3. 比较各 split 分布与覆盖
4. 冻结规则、seed、清单和 hash

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 检测重复、近邻、分布偏差和潜在泄漏，生成统计摘要。

**Human intervention:** 博士生确认划分确实回答目标 claim，接受分布偏差或重新设计。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Split卡：目的 / 单位 / 规则 / seed / 数量 / 分布 / 泄漏检查 / hash

Recommended optional adapters: `k-dense/experimental-design`, `k-dense/exploratory-data-analysis`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

划分单位与 claim 一致，无未解释泄漏，清单和 hash 冻结且可复建。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-baseline-reproduction`, `$sr-exploratory-experiment`, `$sr-generalization-ood`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
