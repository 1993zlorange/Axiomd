---
name: sr-claim-boundary-decision
description: "SR-结论边界与决策：需要把全部证据映射到可说、不可说和下一步继续、修改、暂停或转向决定时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-48"
  aspect: "结果分析与问题诊断"
  short-description: "SR-结论边界与决策"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-结论边界与决策

Use this leaf Skill when: 需要把全部证据映射到可说、不可说和下一步继续、修改、暂停或转向决定时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 逐条建立 claim-evidence 映射
2. 写明数据、指标、场景和统计边界
3. 列出当前证据不能推出的结论
4. 比较继续、修改、暂停和转向选项并签认

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 审计过度结论、证据断链、遗漏反例和措辞强度。

**Human intervention:** 博士生签认 claim、边界和路线决定，重大转向交导师讨论。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 决策卡：claim / evidence / boundary / uncertainty / options / decision / rationale

Recommended optional adapters: `k-dense/scientific-writing`, `nature-reviewer`, `academic-research-skills/academic-paper-reviewer`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每个 claim 有直接证据和边界，不能推出项明确，人类作出并记录路线决定。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-core-claim-alignment`, `$sr-route-retrospective`, `$sr-minimal-diagnostic`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
