---
name: sr-data-generation-qc
description: "SR-数据生成与质量检查：需要生成实验或仿真数据并检查收敛、单位、范围、缺失、重复和失败样本时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-30"
  aspect: "实验设计与执行"
  short-description: "SR-数据生成与质量检查"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-数据生成与质量检查

Use this leaf Skill when: 需要生成实验或仿真数据并检查收敛、单位、范围、缺失、重复和失败样本时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 冻结采样方案、设备或求解器配置
2. 运行小批次并亲自检查原始输出
3. 逐项检查收敛、单位、范围、缺失和重复
4. 保留失败样本及失败原因后再扩批

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 自动校验、汇总分布、计算 hash、画质量图并标异常。

**Human intervention:** 博士生确认仪器、求解器和现场状态，决定异常样本修复、排除或保留。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 数据manifest：样本ID / 参数 / 来源 / 状态 / 校验 / hash / 失败原因

Recommended optional adapters: `nature-experiment-log`, `k-dense/exploratory-data-analysis`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

采样和配置冻结，数据可追溯，质量规则通过或异常有人工处置，失败样本未被静默删除。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-data-split`, `$sr-result-integrity`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
