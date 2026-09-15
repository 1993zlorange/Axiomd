---
name: sr-baseline-landscape
description: "SR-Baseline与基准调研：需要选择公平、可运行且能代表低中强水平的比较基线时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-13"
  aspect: "文献调研与领域结构"
  short-description: "SR-Baseline与基准调研"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Baseline与基准调研

Use this leaf Skill when: 需要选择公平、可运行且能代表低中强水平的比较基线时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 查论文、代码、许可证、数据和评价口径
2. 记录训练预算、硬件和调参范围
3. 本地最小试跑或核验可获得性
4. 按角色选择低基线、主流基线和强基线

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 搜索和整理候选，比较配置与指标，暴露公平性问题。

**Human intervention:** 博士生检查许可证、可运行性、资源现实与对原文的忠实程度。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Baseline 表：来源 / 代码 / 许可 / 数据 / 指标 / 预算 / 复现难度 / 角色

Recommended optional adapters: `nature-academic-search`, `nature-ref-verifier`, `academic-research-skills/deep-research`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每个入选基线有来源、许可、预算、指标和可运行性证据，排除理由可解释。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-baseline-unification`, `$sr-baseline-reproduction`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
