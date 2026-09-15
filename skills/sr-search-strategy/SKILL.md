---
name: sr-search-strategy
description: "SR-检索式设计与试检索：需要系统检索某一研究问题、建立可复跑检索协议或降低漏检与噪声时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-07"
  aspect: "文献调研与领域结构"
  short-description: "SR-检索式设计与试检索"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-检索式设计与试检索

Use this leaf Skill when: 需要系统检索某一研究问题、建立可复跑检索协议或降低漏检与噪声时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 把问题拆为对象、任务、方法和约束词组
2. 手工扩展中英文同义词和排除词
3. 在多个数据库试跑布尔检索式
4. 查看前若干结果并调整召回与精度

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 扩展术语、生成布尔式、比较数据库语法并记录试检索结果。

**Human intervention:** 博士生确定数据库、时间窗口、纳排标准和检索停止点。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 检索协议：问题 / 词组 / 完整检索式 / 数据库 / 日期 / 命中 / 纳排

Recommended optional adapters: `nature-academic-search`, `nature-literature-pipeline`, `academic-research-skills/deep-research`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

协议可重复执行，试检索能覆盖已知核心文献，噪声来源和限制已记录。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-literature-screening`, `$sr-weekly-literature-update`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
