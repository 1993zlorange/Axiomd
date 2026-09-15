---
name: sr-sensitivity-robustness
description: "SR-敏感性与鲁棒性实验：需要知道模型对超参、噪声、数据量或物理扰动的稳定区和失效阈值时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-36"
  aspect: "实验设计与执行"
  short-description: "SR-敏感性与鲁棒性实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-敏感性与鲁棒性实验

Use this leaf Skill when: 需要知道模型对超参、噪声、数据量或物理扰动的稳定区和失效阈值时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 定义有现实意义的扰动轴和范围
2. 逐轴扫描并固定其余条件
3. 使用多种子记录响应和波动
4. 识别稳定区、转折点和失效阈值

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成扫描设计、运行矩阵、曲线和变化点候选。

**Human intervention:** 博士生确认扰动范围真实，判断失败是否来自实现错误或方法边界。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 敏感性表：因素 / 范围 / 控制 / 响应 / 稳定区 / 阈值 / 解释

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

范围有领域依据，控制明确，稳定区和失效阈值有重复证据且不夸大鲁棒性。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-quantitative-analysis`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
