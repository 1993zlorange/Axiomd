---
name: sr-core-claim-alignment
description: "SR-一句话主张与贡献对齐：论文写作前需要确定读者最终应相信什么，并让每项贡献绑定证据时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-49"
  aspect: "论文与成果表达"
  short-description: "SR-一句话主张与贡献对齐"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-一句话主张与贡献对齐

Use this leaf Skill when: 论文写作前需要确定读者最终应相信什么，并让每项贡献绑定证据时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 不用 AI 写一句核心主张
2. 列出最多三项贡献
3. 为每项贡献绑定图表、定理或实验
4. 删除没有独立证据的空贡献并限制边界

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成 claim-evidence 矩阵、挑战空贡献和过强措辞。

**Human intervention:** 博士生控制贡献真实性、优先级和适用范围，最终签认主张。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 主张表：核心claim / contribution / evidence / location / status / boundary

Recommended optional adapters: `nature-writing`, `research-paper-writing`, `academic-research-skills/academic-paper`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

一句话主张可被现有证据支持，每项贡献有位置和证据，无空贡献或越界措辞。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-paper-storyline`, `$sr-core-figures`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
