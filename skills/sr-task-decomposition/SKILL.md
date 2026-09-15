---
name: sr-task-decomposition
description: "SR-研究任务拆解：里程碑或研究目标太大，需要拆成一至三天可完成、可验收且有依赖的工作包时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-60"
  aspect: "项目推进与下一步计划"
  short-description: "SR-研究任务拆解"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-研究任务拆解

Use this leaf Skill when: 里程碑或研究目标太大，需要拆成一至三天可完成、可验收且有依赖的工作包时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 从里程碑反推必要产物
2. 把任务拆成动词加对象
3. 为每项写输入、输出、依赖和责任人
4. 估一至三天持续时间并标关键路径

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成 WBS、依赖图、并行候选和遗漏产物。

**Human intervention:** 博士生按真实实验周期、协作者承诺和注意力调整，不接受虚假并行。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 工作包卡：动词+对象 / 输入 / 输出 / DoD / 依赖 / owner / duration

Recommended optional adapters: `academic-research-skills/academic-pipeline`, `k-dense/mathematical-modeling`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每个任务可在一至三天验收，输入可得，输出具体，依赖与责任人明确。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-milestone-evidence-gate`, `$sr-weekly-plan`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
