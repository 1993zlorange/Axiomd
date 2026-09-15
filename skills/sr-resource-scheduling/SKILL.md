---
name: sr-resource-scheduling
description: "SR-资源与运行调度：GPU、仿真、存储、人力或设备有限，需要按研究价值安排队列和停止条件时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-64"
  aspect: "项目推进与下一步计划"
  short-description: "SR-资源与运行调度"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-资源与运行调度

Use this leaf Skill when: GPU、仿真、存储、人力或设备有限，需要按研究价值安排队列和停止条件时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 清点可用资源和不可用时段
2. 把每个 job 绑定到假设或决策
3. 按信息价值和依赖排序
4. 设置启动、超时、停止、抢占和责任人

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成队列、监控状态、提醒异常和重排候选。

**Human intervention:** 博士生决定资源取舍、抢占和超预算，协调共享设备所有者。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 运行队列：job / hypothesis / resource / priority / start / timeout / stop / owner

Recommended optional adapters: `nature-experiment-log`, `academic-research-skills/academic-pipeline`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

资源只服务明确问题，队列和停止条件可执行，抢占与责任人获人类确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-weekly-plan`, `$sr-result-integrity`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
