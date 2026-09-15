---
name: sr-minimal-falsification
description: "SR-最小证伪实验设计：需要用最低成本实验决定假设继续、修改或停止，而非直接做大规模实验时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-20"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-最小证伪实验设计"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-最小证伪实验设计

Use this leaf Skill when: 需要用最低成本实验决定假设继续、修改或停止，而非直接做大规模实验时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 选择最关键的不确定性
2. 优先使用现有数据或简单模型
3. 设计单变量对照并冻结主要控制项
4. 在看结果前写正负阈值、预算和停止条件

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成实验卡、检查混杂、估计最小样本或运行量并提出备选诊断。

**Human intervention:** 博士生批准实验、资源预算、阈值和 Go/No-Go 规则后才能执行。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 证伪实验卡：假设 / 自变量 / 控制 / 指标 / 正负阈值 / 预算 / 决策

Recommended optional adapters: `k-dense/hypothesis-generation`, `k-dense/experimental-design`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

实验能区分关键假设，成本受控，判据预先冻结，执行前取得人类批准。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-idea-prioritization`, `$sr-exploratory-experiment`, `$sr-claim-boundary-decision`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
