---
name: sr-scope-convergence
description: "SR-研究边界收敛：课题范围过大、变量过多或博士主线与资源不匹配时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-03"
  aspect: "研究问题与选题"
  short-description: "SR-研究边界收敛"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-研究边界收敛

Use this leaf Skill when: 课题范围过大、变量过多或博士主线与资源不匹配时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 列出可能影响结论的全部对象和变量
2. 固定次要因素并保留主要矛盾
3. 明确范围内、范围外和暂不研究事项
4. 与导师确认删减项及重开条件

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 提出隐含变量、边界反例和多种范围方案。

**Human intervention:** 博士生依据毕业主线、时间、数据和设备资源裁剪，并取得导师对重大范围变更的确认。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 边界卡：范围内 / 范围外 / 固定量 / 变化量 / 删减理由 / 重开条件

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

范围能在当前阶段验证，非目标明确，任何扩展都有可观测的重开条件。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-solution-gap-analysis`, `$sr-value-feasibility`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
