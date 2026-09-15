---
name: sr-baseline-reproduction
description: "SR-Baseline复现：需要在本地复现论文或官方基线并解释与报告值的差异时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-32"
  aspect: "实验设计与执行"
  short-description: "SR-Baseline复现"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Baseline复现

Use this leaf Skill when: 需要在本地复现论文或官方基线并解释与报告值的差异时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 锁定代码、依赖、数据和硬件环境
2. 按原文或官方配置运行
3. 按本项目统一口径再运行
4. 比较来源值与本地值并建立差异原因树

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 维护复现清单、环境记录、差异表和候选原因。

**Human intervention:** 博士生阅读原文、执行或监督关键跑次，签认差异是否可接受。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 复现表：来源值 / 本地值 / 配置 / 环境 / 差异 / 候选原因 / 状态

Recommended optional adapters: `nature-experiment-log`, `k-dense/exploratory-data-analysis`, `k-dense/statistical-analysis`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

环境和命令可重现，差异被量化并解释或标为阻塞，人类签认后方可作为基线。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-main-comparison`, `$sr-blocker-resolution`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
