---
name: sr-dataflow-architecture
description: "SR-数据流与系统架构设计：需要把数据来源、处理、模型、评价、存储和模块责任连成可实现数据流时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-22"
  aspect: "技术方案与方法设计"
  short-description: "SR-数据流与系统架构设计"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-数据流与系统架构设计

Use this leaf Skill when: 需要把数据来源、处理、模型、评价、存储和模块责任连成可实现数据流时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 盘点数据来源、处理、输入、输出和评价
2. 手画端到端数据流与状态边界
3. 定义每个模块责任、接口和持久化
4. 沿失败路径检查断点和回退

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成多版架构、检查断链、接口歧义和隐藏状态。

**Human intervention:** 博士生选择与真实实验环境、团队能力和维护成本相容的方案。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 架构卡：节点 / 输入 / 输出 / 责任 / 接口 / 持久化 / 失败处理

Recommended optional adapters: `k-dense/mathematical-modeling`, `nature-proposal-writer`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

数据能从来源追到结果，模块责任单一，接口可验证，主要失败有可观测处理。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-mathematical-model`, `$sr-data-schema-freeze`, `$sr-algorithm-implementation-plan`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
