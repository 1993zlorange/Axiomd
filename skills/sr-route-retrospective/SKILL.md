---
name: sr-route-retrospective
description: "SR-路线复盘与优先级调整：新证据改变原假设、任务价值或关键路径，需要继续、暂停、放弃或转向时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-67"
  aspect: "项目推进与下一步计划"
  short-description: "SR-路线复盘与优先级调整"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-路线复盘与优先级调整

Use this leaf Skill when: 新证据改变原假设、任务价值或关键路径，需要继续、暂停、放弃或转向时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 重新写总体研究问题和当前里程碑
2. 汇总改变判断的新证据
3. 比较各分支的价值、成本和剩余不确定性
4. 明确继续、暂停、放弃与重开条件

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 对照路线与证据、估算继续投入价值并提出停止候选。

**Human intervention:** 博士生结合毕业、投稿、合作和机会成本决策，重大转向请导师确认。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 路线决策：branch / original rationale / new evidence / value / cost / decision / date

Recommended optional adapters: `k-dense/hypothesis-generation`, `academic-research-skills/academic-pipeline`, `nature-reviewer`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

调整由新证据驱动，停止项和重开条件明确，资源与下周计划已同步。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-weekly-plan`, `$sr-core-hypothesis`, `$sr-stage-archive`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
