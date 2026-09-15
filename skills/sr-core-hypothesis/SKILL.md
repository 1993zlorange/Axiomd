---
name: sr-core-hypothesis
description: "SR-核心假设撰写：需要把观察或差距转成带机制、预测、竞争解释和证伪判据的科学假设时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-16"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-核心假设撰写"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-核心假设撰写

Use this leaf Skill when: 需要把观察或差距转成带机制、预测、竞争解释和证伪判据的科学假设时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 写出若 A 则 B 因为 C
2. 列出至少一个竞争假设
3. 为主假设和竞争假设写不同预测
4. 定义支持、否定判据和适用边界

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 扩展竞争解释、检查可证伪性、生成不同条件下的预测。

**Human intervention:** 博士生选择主假设，确认理论依据、关键变量和可接受证伪结果。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 假设卡：观察 / A / B / C / 竞争假设 / 支持判据 / 否定判据 / 边界

Recommended optional adapters: `k-dense/hypothesis-generation`, `academic-research-skills/deep-research`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

假设能被观察否定，竞争解释产生可区分预测，判据在看结果前写定并由人确认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-nearest-neighbor-difference`, `$sr-mechanism-counterexample`, `$sr-minimal-falsification`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
