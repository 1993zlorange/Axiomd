---
name: sr-research-question-review
description: "SR-研究问题评审：研究问题准备冻结、需要从创新性、可证伪性、边界和资源角度接受挑战时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-06"
  aspect: "研究问题与选题"
  short-description: "SR-研究问题评审"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-研究问题评审

Use this leaf Skill when: 研究问题准备冻结、需要从创新性、可证伪性、边界和资源角度接受挑战时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 把问题陈述和边界交给导师或同学
2. 逐条记录质疑而不立即辩解
3. 按证据修改问题或范围
4. 再次评审未关闭的致命问题

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 模拟不同审稿视角、分类质疑并检查回应是否有证据。

**Human intervention:** 博士生组织真人评审，判断采纳、拒绝或延期，并记录理由。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 问题评审单：质疑 / 类型 / 严重度 / 回应证据 / 修改 / 状态

Recommended optional adapters: `nature-reviewer`, `academic-research-skills/academic-paper-reviewer`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

无未处理的致命质疑；问题、边界、价值和最小验证得到人类签认。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-search-strategy`, `$sr-core-hypothesis`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
