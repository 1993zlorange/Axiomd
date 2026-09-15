---
name: sr-failure-fallback
description: "SR-失效与回退设计：方法可能出现数值、数据、OOD、资源或接口失效，需要提前设计触发器与回退时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-29"
  aspect: "技术方案与方法设计"
  short-description: "SR-失效与回退设计"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-失效与回退设计

Use this leaf Skill when: 方法可能出现数值、数据、OOD、资源或接口失效，需要提前设计触发器与回退时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 列出主要失效模式
2. 为每个失效写原因与可观测信号
3. 定义阈值、影响和回退策略
4. 用一个代表性故障演练恢复

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 扩展 failure mode、检查监控盲区和回退依赖。

**Human intervention:** 博士生批准回退是否改变研究 claim、数据口径或资源承诺。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: FMEA：失效 / 原因 / 信号 / 阈值 / 影响 / 回退 / 恢复 / 责任人

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

高影响失效有信号、阈值、责任人与回退，至少一条恢复路径经过演练。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-data-generation-qc`, `$sr-exploratory-experiment`, `$sr-risk-contingency`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
