---
name: sr-weekly-literature-update
description: "SR-周度文献增量更新：已有文献基线后需要每周增量发现会改变当前判断的新工作时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-14"
  aspect: "文献调研与领域结构"
  short-description: "SR-周度文献增量更新"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-周度文献增量更新

Use this leaf Skill when: 已有文献基线后需要每周增量发现会改变当前判断的新工作时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 运行已保存检索式或提醒
2. 对新增结果去重和快速筛选
3. 只深读可能改变路线判断的文献
4. 更新 Paper Card、谱系树和行动影响

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 抓取或整理新增、打分、分类并提示与既有结论冲突。

**Human intervention:** 博士生决定新文献是否真的改变认知、优先级或实验设计。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 周增量表：新增 / 去重 / 分类 / 关键证据 / 认知变化 / 行动影响

Recommended optional adapters: `nature-literature-pipeline`, `nature-academic-search`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

新增集合有检索日期，关键论文已核验，所有路线变化均有文献证据和人类决定。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-paper-evidence-card`, `$sr-route-retrospective`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
