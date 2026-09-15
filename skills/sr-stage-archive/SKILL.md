---
name: sr-stage-archive
description: "SR-阶段归档：阶段结束、路线暂停、论文提交或交接前，需要整理可接续的数据、代码、配置、结果、失败和未决问题时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-68"
  aspect: "项目推进与下一步计划"
  short-description: "SR-阶段归档"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-阶段归档

Use this leaf Skill when: 阶段结束、路线暂停、论文提交或交接前，需要整理可接续的数据、代码、配置、结果、失败和未决问题时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 清点阶段范围和所有应有产物
2. 整理数据、代码、配置、结果和决定
3. 从复现入口执行一次接续检查
4. 记录失败、未决问题、许可和敏感信息

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 建立 artifact 索引、hash、阶段报告和缺失清单。

**Human intervention:** 博士生核查可接续性、数据许可、敏感内容和最终阶段结论。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 阶段包：scope / artifacts / hashes / reproduce / findings / failures / open issues

Recommended optional adapters: `nature-data`, `nature-experiment-log`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

索引可定位全部关键产物，复现入口可用，失败与未知未丢失，许可和交接由人确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): none. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
