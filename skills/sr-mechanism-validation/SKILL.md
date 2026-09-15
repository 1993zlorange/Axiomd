---
name: sr-mechanism-validation
description: "SR-机制验证：性能差异之外还需要用中间量、残差、守恒、探针或对照支持声称机制时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-47"
  aspect: "结果分析与问题诊断"
  short-description: "SR-机制验证"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-机制验证

Use this leaf Skill when: 性能差异之外还需要用中间量、残差、守恒、探针或对照支持声称机制时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 从机制 claim 导出预期可观测变化
2. 选择能代表机制的中间量或 probe
3. 设计随机、替代解释或负对照
4. 比较结果并评估代理指标有效性

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成探针、分析中间量、制图并列出替代解释。

**Human intervention:** 博士生确认 probe 是否真正代表机制，决定证据只能支持相关还是因果。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 机制证据表：机制claim / 预测 / probe / 对照 / 结果 / 替代解释 / 强度

Recommended optional adapters: `k-dense/hypothesis-generation`, `k-dense/statistical-analysis`, `nature-figure`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

机制预测、probe 和对照对齐，代理有效性被讨论，证据强度与措辞匹配。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-claim-boundary-decision`, `$sr-core-claim-alignment`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
