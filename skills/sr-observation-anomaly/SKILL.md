---
name: sr-observation-anomaly
description: "SR-观察与异常提炼：数据、实验或阅读中出现异常现象，需要先保存事实再形成问题时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-15"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-观察与异常提炼"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-观察与异常提炼

Use this leaf Skill when: 数据、实验或阅读中出现异常现象，需要先保存事实再形成问题时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 保存原始现象、时间和上下文
2. 亲自检查是否可重复观察
3. 把事实描述与解释猜测分开
4. 比较多个异常并寻找共同模式

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 整理日志、聚类异常、检查缺失上下文并提出可验证问题。

**Human intervention:** 博士生确认原始数据和实验状态真实，判断异常是否值得进入研究主线。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 观察台账：时间 / 数据版本 / 现象 / 重复次数 / 事实 / 解释 / 待测问题

Recommended optional adapters: `nature-experiment-log`, `k-dense/exploratory-data-analysis`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

原始现象可定位、至少一次复核，事实与解释分开，并形成可回答问题。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-core-hypothesis`, `$sr-cause-tree`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
