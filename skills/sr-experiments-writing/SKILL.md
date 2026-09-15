---
name: sr-experiments-writing
description: "SR-实验部分写作：实验已完成，需要按问题、设置、结果、解释、边界和复现信息组织章节时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-52"
  aspect: "论文与成果表达"
  short-description: "SR-实验部分写作"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-实验部分写作

Use this leaf Skill when: 实验已完成，需要按问题、设置、结果、解释、边界和复现信息组织章节时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 为每组实验先写它回答的问题
2. 核对设置、数据、指标和预算
3. 从原始结果抄录数字并标图表
4. 写解释、不能推出项和复现细节

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 对齐表图、统计与文字，检查数字、配置和 claim 不一致。

**Human intervention:** 博士生核对每个数字、实验配置、排除项和实际解释。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 实验段：Question / Setup / Metric / Result / Interpretation / Boundary / Artifact

Recommended optional adapters: `nature-writing`, `research-paper-writing`, `nature-statistics`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每组实验回答明确问题，数字可追到 artifact，统计与边界完整，无选择性报告。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-core-figures`, `$sr-abstract-introduction`, `$sr-internal-review`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
