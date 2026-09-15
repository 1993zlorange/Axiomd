---
name: sr-methods-writing
description: "SR-方法部分写作：符号、方法和实现已冻结，需要写可理解、可复现且不过度包装的方法章节时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-51"
  aspect: "论文与成果表达"
  short-description: "SR-方法部分写作"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-方法部分写作

Use this leaf Skill when: 符号、方法和实现已冻结，需要写可理解、可复现且不过度包装的方法章节时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 冻结符号表、前提和方法边界
2. 先写目标与总览再写组件
3. 逐式写算法、损失、复杂度和实现细节
4. 由自己或同学按文字复述实现

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 按章节规则起草、统一术语、检查缺失定义和复现细节。

**Human intervention:** 博士生逐式核对、补实验室隐性知识并确认文字未改变算法语义。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 方法模板：目标 / 前提 / 表示 / 算法 / 损失 / 复杂度 / 实现 / 限制

Recommended optional adapters: `nature-writing`, `research-paper-writing`, `academic-research-skills/academic-paper`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

方法可由独立读者复述，公式、伪代码和实现一致，限制与不可见细节明确。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-experiments-writing`, `$sr-internal-review`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
