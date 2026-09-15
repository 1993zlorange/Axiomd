---
name: sr-data-schema-freeze
description: "SR-数据接口与Schema冻结：数据字段、形状、单位、坐标、编码、缺失规则或版本需要冻结时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-25"
  aspect: "技术方案与方法设计"
  short-description: "SR-数据接口与Schema冻结"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-数据接口与Schema冻结

Use this leaf Skill when: 数据字段、形状、单位、坐标、编码、缺失规则或版本需要冻结时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 从真实设备或仿真输出抄录字段
2. 定义 dtype、shape、unit、range 和 nullable
3. 制作最小正例、边界例和错误例
4. 人工抽检样本并让生产者与消费者共同确认

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成 schema、校验器草案、边界测试和兼容性检查。

**Human intervention:** 博士生核对真实数据含义；生产者与消费者确认版本和变更影响。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Schema：字段 / dtype / shape / unit / range / nullable / version / 示例

Recommended optional adapters: `k-dense/exploratory-data-analysis`, `k-dense/mathematical-modeling`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

schema 有版本和样例，真实抽检通过，单位坐标无歧义，变更流程与责任人明确。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-baseline-unification`, `$sr-data-generation-qc`, `$sr-data-split`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
