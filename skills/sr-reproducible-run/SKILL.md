---
name: sr-reproducible-run
description: "SR-可复现实验封装：实验需要保存代码、数据、环境、配置、种子、命令和输出并从空目录重跑时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-39"
  aspect: "实验设计与执行"
  short-description: "SR-可复现实验封装"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-可复现实验封装

Use this leaf Skill when: 实验需要保存代码、数据、环境、配置、种子、命令和输出并从空目录重跑时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 记录 code commit、data hash 和环境
2. 冻结配置、seed、命令和输出约定
3. 从干净目录按入口运行
4. 比较关键结果并记录偏差与限制

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成 manifest、环境清单、README 和复现检查脚本。

**Human intervention:** 博士生确认原始数据可用、许可和敏感信息边界，并亲自核验重跑结果。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Run manifest：code SHA / data SHA / env / config / seed / command / outputs

Recommended optional adapters: `nature-experiment-log`, `nature-data`, `k-dense/scientific-writing`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

从干净环境可到达关键结果，所有输入版本可定位，限制、许可和失败均记录。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-result-integrity`, `$sr-stage-archive`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
