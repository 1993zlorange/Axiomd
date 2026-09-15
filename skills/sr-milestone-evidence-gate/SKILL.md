---
name: sr-milestone-evidence-gate
description: "SR-里程碑与证据门管理：进入下一阶段前需要设置数据、基线、机制、性能或写作证据门槛时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-61"
  aspect: "项目推进与下一步计划"
  short-description: "SR-里程碑与证据门管理"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-里程碑与证据门管理

Use this leaf Skill when: 进入下一阶段前需要设置数据、基线、机制、性能或写作证据门槛时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 写出下一阶段会增加的成本或承诺
2. 为进入条件定义可测 criterion 和 threshold
3. 逐条链接当前证据
4. 由指定批准人作 Go/No-Go/Revise 判断

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 检查材料齐全性、阈值歧义和证据是否真正对应 criterion。

**Human intervention:** 博士生或导师决定门是否通过；AI 不得自动越过里程碑。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 证据门：milestone / criterion / threshold / evidence / verdict / approver / next

Recommended optional adapters: `academic-research-skills/academic-pipeline`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

门槛在评估前定义，证据可追踪，批准人和 verdict 明确，未通过不会启动下阶段。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-weekly-plan`, `$sr-risk-contingency`, `$sr-stage-archive`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
