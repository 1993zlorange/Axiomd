---
name: sr-last-week-acceptance
description: "SR-上周任务验收：新一周开始或组会前，需要按上周承诺和完成标准检查真实交付物时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-59"
  aspect: "项目推进与下一步计划"
  short-description: "SR-上周任务验收"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-上周任务验收

Use this leaf Skill when: 新一周开始或组会前，需要按上周承诺和完成标准检查真实交付物时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 逐项读取上周承诺和完成标准
2. 实际打开代码、数据、图表或文档
3. 判定完成、部分完成、取消或失败
4. 记录偏差原因和遗留项

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 汇总承诺与产物、发现缺失链接和标准变化。

**Human intervention:** 博士生实际验收；投入时间、聊天总结和接近完成均不能替代交付物。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 验收表：承诺 / 标准 / 实际产物 / 证据 / 状态 / 偏差 / 遗留

Recommended optional adapters: `academic-research-skills/academic-pipeline`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每项承诺有可检查产物或真实失败状态，标准未事后降低，偏差进入后续决定。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-route-retrospective`, `$sr-weekly-plan`, `$sr-blocker-resolution`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
