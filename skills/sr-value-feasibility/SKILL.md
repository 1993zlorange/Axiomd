---
name: sr-value-feasibility
description: "SR-价值与可行性评估：需要决定课题是否值得做、能否做以及最低成本验证是什么时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-05"
  aspect: "研究问题与选题"
  short-description: "SR-价值与可行性评估"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-价值与可行性评估

Use this leaf Skill when: 需要决定课题是否值得做、能否做以及最低成本验证是什么时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 分别评估科学价值和工程价值
2. 盘点数据、设备、算力、时间与合作依赖
3. 识别关键风险和失败代价
4. 设计最低成本验证并作 Go/No-Go 判断

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 补充风险、反例、替代路线和多准则评分。

**Human intervention:** 博士生承担方向选择、机会成本和资源承诺，必要时请导师批准。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 价值—可行性表：价值 / 证据 / 成本 / 风险 / 最小验证 / 决策

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

价值有证据、关键资源可获得或有预案，并记录明确 Go/No-Go/Revise 决定。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-research-question-review`, `$sr-search-strategy`, `$sr-core-hypothesis`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
