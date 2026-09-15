---
name: sr-blocker-resolution
description: "SR-Blocker定位与清除：“进展慢”需要转成具体阻塞、根因、所需输入、责任人和期限时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-62"
  aspect: "项目推进与下一步计划"
  short-description: "SR-Blocker定位与清除"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Blocker定位与清除

Use this leaf Skill when: “进展慢”需要转成具体阻塞、根因、所需输入、责任人和期限时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 把症状改写成无法继续的具体条件
2. 用五问或原因树定位根因
3. 明确需要的输入、决定或资源
4. 指定责任人、期限和临时绕行方案

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成根因树、依赖分析、绕行选项和清除清单。

**Human intervention:** 博士生协调真人、共享资源和优先级；涉及他人承诺时必须获得确认。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Blocker卡：symptom / root cause / needed input / owner / due / workaround / status

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

阻塞可观测，根因与症状区分，责任人和期限已确认，绕行风险清楚。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-collaboration-interface`, `$sr-risk-contingency`, `$sr-weekly-plan`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
