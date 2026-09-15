---
name: sr-internal-review
description: "SR-内部审稿：稿件或成果包需要在投稿前从创新、技术、实验和表达四个角度找拒稿风险时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-55"
  aspect: "论文与成果表达"
  short-description: "SR-内部审稿"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-内部审稿

Use this leaf Skill when: 稿件或成果包需要在投稿前从创新、技术、实验和表达四个角度找拒稿风险时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 自己隔天按审稿人视角通读
2. 分别执行创新、技术、实验和表达审查
3. 把问题分为致命、重要和次要
4. 邀请同学盲审并制定修改责任

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成相互独立的 reviewer reports、证据缺口和可执行修改项。

**Human intervention:** 博士生与真人审稿者复核 AI 漏报误报，决定是否补实验、降 claim 或暂缓投稿。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 内审表：concern / evidence / severity / affected claim / action / owner / status

Recommended optional adapters: `nature-reviewer`, `academic-research-skills/academic-paper-reviewer`, `k-dense/peer-review`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

所有致命问题关闭或触发暂停，重要问题有责任人，AI 与真人审查差异被处理。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-abstract-introduction`, `$sr-core-figures`, `$sr-talk-open-source`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
