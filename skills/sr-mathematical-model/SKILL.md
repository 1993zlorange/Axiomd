---
name: sr-mathematical-model
description: "SR-数学模型定义：需要统一符号并明确映射、损失、约束、训练和推理公式时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-23"
  aspect: "技术方案与方法设计"
  short-description: "SR-数学模型定义"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-数学模型定义

Use this leaf Skill when: 需要统一符号并明确映射、损失、约束、训练和推理公式时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 建立唯一符号表
2. 手写输入到输出的映射和假设
3. 推导损失、约束、训练与推理步骤
4. 检查维度、单位并用小样例手算

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 审计符号、维度、公式依赖、边界情况和前后不一致。

**Human intervention:** 博士生逐式确认推导、领域假设和近似条件，不能把 AI 公式当权威。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 数学定义表：符号 / 形状 / 单位 / 公式 / 假设 / 训练阶段 / 推理阶段

Recommended optional adapters: `k-dense/mathematical-modeling`, `k-dense/scientific-writing`, `research-paper-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

符号唯一、量纲一致、训练与推理无缺口，小样例可计算且假设有适用边界。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-module-challenge-mapping`, `$sr-algorithm-implementation-plan`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
