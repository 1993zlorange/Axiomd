---
name: sr-resource-budget
description: "SR-复杂度与资源预算：需要估算样本、GPU、CPU、仿真、存储、人时并设置缩减与停止条件时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-28"
  aspect: "技术方案与方法设计"
  short-description: "SR-复杂度与资源预算"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-复杂度与资源预算

Use this leaf Skill when: 需要估算样本、GPU、CPU、仿真、存储、人时并设置缩减与停止条件时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 按任务估算样本和运行次数
2. 估显存、训练、仿真、存储和人时
3. 执行一次小跑校准估算
4. 冻结预算、优先级、超时和缩减方案

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 建立预算模型、外推运行量、生成队列和超限提醒。

**Human intervention:** 博士生确认真实资源、机会成本和共享资源承诺，批准超预算动作。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 资源表：任务 / GPU小时 / CPU小时 / 存储 / 人时 / 优先级 / 停止阈值

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

预算由小跑校准，关键实验优先，超时与停止可执行，资源负责人已确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-failure-fallback`, `$sr-resource-scheduling`, `$sr-exploratory-experiment`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
