---
name: sr-idea-prioritization
description: "SR-Idea优先级评审：多个 Idea 或路线竞争，需要按价值、新颖性、可证伪性、数据、成本和风险排序时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-21"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-Idea优先级评审"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Idea优先级评审

Use this leaf Skill when: 多个 Idea 或路线竞争，需要按价值、新颖性、可证伪性、数据、成本和风险排序时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 先写评分准则和权重
2. 为每个 Idea 收集证据而非印象
3. 讨论权重与得分敏感性
4. 确定首选、备选、暂停和放弃项

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 执行多准则评分、敏感性分析和寻找被低估的风险。

**Human intervention:** 博士生结合毕业主线、合作承诺和资源做最终排序，并请导师确认重大路线。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Idea评分表：准则 / 权重 / 证据 / 得分 / 敏感性 / 排序 / 暂停理由

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

排序对合理权重变化有解释，首选有最小验证，暂停与放弃理由被记录。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-dataflow-architecture`, `$sr-weekly-plan`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
