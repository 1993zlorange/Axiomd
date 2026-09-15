---
name: sr-main-comparison
description: "SR-主对比实验：假设和实验协议已冻结，需要与低、主流和强基线做公平正式比较时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-34"
  aspect: "实验设计与执行"
  short-description: "SR-主对比实验"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-主对比实验

Use this leaf Skill when: 假设和实验协议已冻结，需要与低、主流和强基线做公平正式比较时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 冻结数据、split、预算、调参和随机种子
2. 先跑冒烟与一条完整链路
3. 按统一协议运行全部方法
4. 核对日志、统计和公平性后封存主结果

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 编排运行、监控失败、汇总统计并检查预算和配置差异。

**Human intervention:** 博士生批准正式运行，处理异常，确认比较公平与结果可进入结论。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 主结果表：方法 / 预算 / seed / 主指标 / 辅指标 / 区间 / 资源 / 备注

Recommended optional adapters: `k-dense/experimental-design`, `k-dense/statistical-analysis`, `nature-statistics`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

协议在结果前冻结，基线覆盖合理，多种子和不确定性齐全，异常与排除有记录。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-ablation-study`, `$sr-sensitivity-robustness`, `$sr-quantitative-analysis`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
