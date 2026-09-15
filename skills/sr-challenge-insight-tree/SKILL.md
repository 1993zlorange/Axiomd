---
name: sr-challenge-insight-tree
description: "SR-Challenge-insight tree：需要把领域挑战追到根因，并把洞见、方法和证据连成可验证链时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-12"
  aspect: "文献调研与领域结构"
  short-description: "SR-Challenge-insight tree"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Challenge-insight tree

Use this leaf Skill when: 需要把领域挑战追到根因，并把洞见、方法和证据连成可验证链时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 从文献和实际现象收集具体挑战
2. 逐层追问挑战为何出现
3. 为每个根因写候选 insight
4. 把 insight 对应到方法、预测和待验证证据

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 聚类挑战、扩展根因、检查洞见是否只是口号。

**Human intervention:** 博士生删除没有领域依据、不可观测或无法证伪的连接。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 树节点：挑战 / 原因 / insight / 方法 / 支持证据 / 剩余缺口

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每条 insight 有原因、可观测预测和验证入口，未证实连接被明确标记。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-core-hypothesis`, `$sr-idea-decomposition`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
