---
name: sr-scenario-needs
description: "SR-场景与需求定义：课题来源、真实使用场景、对象、输入输出或约束尚不清楚时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-01"
  aspect: "研究问题与选题"
  short-description: "SR-场景与需求定义"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-场景与需求定义

Use this leaf Skill when: 课题来源、真实使用场景、对象、输入输出或约束尚不清楚时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 访谈需求方并保留原话与来源
2. 区分科学问题、工程要求和个人猜测
3. 写出使用者、时机、输入、输出与性能约束
4. 请需求方核对误解和遗漏

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 整理访谈、聚类需求、暴露矛盾和缺项。

**Human intervention:** 博士生确认原意、敏感信息、真实约束以及哪些需求进入研究范围。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 场景卡：使用者 / 时机 / 输入 / 输出 / 性能约束 / 来源 / 待确认

Recommended optional adapters: `nature-proposal-writer`, `academic-research-skills/deep-research`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

场景卡有来源、边界和需求方复核；科学问题与工程要求未混写。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-problem-formalization`, `$sr-scope-convergence`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
