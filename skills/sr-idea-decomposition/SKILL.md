---
name: sr-idea-decomposition
description: "SR-Idea分解：Idea 含多个机制、增强模块和工程组件，需要收敛最小研究版本时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-18"
  aspect: "Idea、科学假设与创新点"
  short-description: "SR-Idea分解"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-Idea分解

Use this leaf Skill when: Idea 含多个机制、增强模块和工程组件，需要收敛最小研究版本时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 拆出核心机制和必要组件
2. 分离可选增强与工程便利项
3. 画依赖关系并找最短闭环
4. 删除不服务主假设的模块并定义最小版本

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 生成依赖图、最小方案和可能的模块替代。

**Human intervention:** 博士生决定哪些机制对论文主张必要，控制系统复杂度和研究风险。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: Idea结构卡：核心机制 / 必需项 / 增强项 / 工程项 / 依赖 / 最小版本

Recommended optional adapters: None; use available local tools.. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

最小版本能独立检验核心假设，每个保留模块有必要性，增强项不阻塞验证。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-mechanism-counterexample`, `$sr-minimal-falsification`, `$sr-dataflow-architecture`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
