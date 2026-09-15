---
name: sr-error-decomposition
description: "SR-误差来源分解：总误差需要拆成数据、离散、优化、近似、数值或评价来源并排序时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-44"
  aspect: "结果分析与问题诊断"
  short-description: "SR-误差来源分解"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-误差来源分解

Use this leaf Skill when: 总误差需要拆成数据、离散、优化、近似、数值或评价来源并排序时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 列出理论上可能的误差来源
2. 为每类来源写机制和可观测预测
3. 寻找独立证据或上下界
4. 按可能量级和可验证性排序

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 建立误差预算候选、寻找遗漏来源和区分证据。

**Human intervention:** 博士生用领域知识判断误差是否可识别，避免把残差强行归因。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 误差预算：来源 / 机制 / 预测 / 当前证据 / 量级 / 优先级 / 验证

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

主要误差来源覆盖充分，归因有独立证据或标为假设，下一诊断按价值排序。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-cause-tree`, `$sr-minimal-diagnostic`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
