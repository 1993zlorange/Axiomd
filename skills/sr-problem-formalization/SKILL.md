---
name: sr-problem-formalization
description: "SR-问题形式化：自然语言问题需要转成变量、映射、目标、约束与可测指标时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-02"
  aspect: "研究问题与选题"
  short-description: "SR-问题形式化"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-问题形式化

Use this leaf Skill when: 自然语言问题需要转成变量、映射、目标、约束与可测指标时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 用一句话写清输入、处理和输出
2. 手工定义变量、符号、单位与范围
3. 写出目标函数、约束和评价指标
4. 用一个小样例手算并检查量纲

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成候选形式化、检查符号一致性、量纲和漏掉的约束。

**Human intervention:** 博士生确认物理或领域含义、可测量性和评价指标是否回答原问题。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 形式化表：符号 / 类型 / 单位 / 已知性 / 范围 / 来源 / 评价指标

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

所有核心变量可定义或标为未知，指标可测，至少一个手算样例无语义或量纲冲突。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-scope-convergence`, `$sr-solution-gap-analysis`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
