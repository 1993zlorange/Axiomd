---
name: sr-weekly-plan
description: "SR-周计划制定：需要从关键未知量制定下一周一个 P0、最多两个 P1 的可验收科研计划时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-66"
  aspect: "项目推进与下一步计划"
  short-description: "SR-周计划制定"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-周计划制定

Use this leaf Skill when: 需要从关键未知量制定下一周一个 P0、最多两个 P1 的可验收科研计划时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 回看上周验收和当前总目标
2. 列出最影响路线的未知量
3. 只选一个 P0 和最多两个 P1
4. 为每项写交付物、完成标准、时间、风险和缓冲

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 根据依赖和信息价值生成计划候选、检查任务是否可验收。

**Human intervention:** 博士生按真实日程作承诺，导师确认重大优先级或资源变化。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 周计划：priority / question / task / deliverable / DoD / schedule / risk

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

P0 不超过一项、P1 不超过两项，每项有可检查交付物、DoD、日程和风险。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-last-week-acceptance`, `$sr-weekly-meeting`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
