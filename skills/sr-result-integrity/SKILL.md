---
name: sr-result-integrity
description: "SR-结果完整性检查：分析前需要核对运行数、配置、日志、退出状态、checkpoint 和评价脚本是否完整时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-40"
  aspect: "结果分析与问题诊断"
  short-description: "SR-结果完整性检查"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-结果完整性检查

Use this leaf Skill when: 分析前需要核对运行数、配置、日志、退出状态、checkpoint 和评价脚本是否完整时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 按计划清点每个 run
2. 逐项打开配置、日志和退出状态
3. 核对 checkpoint 与评价脚本版本
4. 决定缺失补跑、异常排除或保留

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 自动建立审计表、比对配置和检测缺失或异常运行。

**Human intervention:** 博士生判断异常运行的科学与工程含义，并批准排除或补跑。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 结果审计表：run / config / status / artifact / valid / exclusion reason / action

Recommended optional adapters: `nature-experiment-log`, `k-dense/exploratory-data-analysis`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

计划运行均有状态，有效性和排除规则明确，任何补跑或排除经人确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-quantitative-analysis`, `$sr-blocker-resolution`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
