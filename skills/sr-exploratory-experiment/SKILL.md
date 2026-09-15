---
name: sr-exploratory-experiment
description: "SR-探索性实验：需要在简化 setting 中一次验证一个机制，决定是否进入正式主实验时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-33"
  aspect: "实验设计与执行"
  short-description: "SR-探索性实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-探索性实验

Use this leaf Skill when: 需要在简化 setting 中一次验证一个机制，决定是否进入正式主实验时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 选择一个明确机制问题
2. 简化数据、模型或运行规模
3. 预写唯一改动、控制和正负判据
4. 运行并立即记录 Go/No-Go 决定

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 检查混杂、生成配置和分析脚本、比较结果与预设判据。

**Human intervention:** 博士生选择机制、批准运行并判断失败是科学结果还是实现问题。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 探索实验卡：问题 / 假设 / 单变量 / 控制 / 判据 / 结果 / Go-No-Go

Recommended optional adapters: `k-dense/hypothesis-generation`, `k-dense/experimental-design`, `nature-experiment-log`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

一次只测一个核心因素，结果可定位，按预设判据做继续、修改或停止决定。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-main-comparison`, `$sr-minimal-diagnostic`, `$sr-idea-prioritization`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
