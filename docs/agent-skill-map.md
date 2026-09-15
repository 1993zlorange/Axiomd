# Agent-to-skill map

This map is generated from each agent TOML's `[[skills.config]]` entries and skill names mentioned in its developer instructions.

## `pr-ar-00-project-architect`

负责基于已批准需求和证据设计、评审并维护可实现、可验证、可追溯的软件架构与详细设计。

**Configured skills**

- None.

**Referenced in instructions**

- `pr-ar-01-project-architect`
- `pr-pm-02-project-manager`

## `pr-en-00-engineer`

全栈实现负责人：按目标项目批准的需求和设计实现、验证并交付软件；仅在目标项目明确适用时调用领域专用能力。

**Configured skills**

- None.

**Referenced in instructions**

- `playwright`
- `pr-ar-01-project-architect`
- `pr-en-01-fullstack-design-engineer`
- `pr-en-02-senior-engineer`

## `pr-pm-00-project-manager`

负责软件、数据和科研项目的需求澄清、范围控制、交付协调、对齐审计和受控发布；按目标项目规则选择领域能力。

**Configured skills**

- None.

**Referenced in instructions**

- `pr-pm-01-project-manager-socratic-discovery`
- `pr-pm-02-project-manager`
- `pr-pm-03-project-alignment-audit`
- `pr-rl-01-software-project-release-management`
- `scienceresearch-pm-reporting`
- `scienceresearch-release-management`

## `pr-ps-00-project-supervisor`

全局项目监理：在软件、数据和科研项目的所有项目相关操作前后执行治理监控，维护需求、日志、反思、命名、文件归属、质量门禁以及 Skill 和脚本工具生命周期。

**Configured skills**

- `pr-ps-00-project-supervision`
- `pr-ps-01-project-governance`
- `pr-ps-02-quality-gate`
- `pr-ps-03-project-logging`
- `pr-ps-04-reflection-loop`
- `pr-ps-05-skill-authoring`
- `pr-ps-06-script-tool-authoring`
- `pr-ps-07-transfer-pilot`
- `pr-ps-08-evolution-review`

**Referenced in instructions**

- None.

## `pr-qa-00-project-test`

独立验证当前项目的需求、接口、数据和用户路径，报告可复现缺陷；仅在目标项目明确适用时使用领域专用测试能力。

**Configured skills**

- None.

**Referenced in instructions**

- `playwright`
- `pr-qa-01-software-project-functional-qa`
- `scienceresearch-functional-qa`

## `sr-critical-reviewer`

ScienceResearch 批判性评审员：独立挑战问题、差距、最近邻与机制，并审计结果完整性、归因和投稿风险。

**Configured skills**

- `sr-research-shared`
- `sr-solution-gap-analysis`
- `sr-research-question-review`
- `sr-nearest-neighbor-difference`
- `sr-mechanism-counterexample`
- `sr-result-integrity`
- `sr-error-decomposition`
- `sr-cause-tree`
- `sr-minimal-diagnostic`
- `sr-internal-review`
- `sr-review-comment-analysis`

**Referenced in instructions**

- None.

## `sr-experimenter`

ScienceResearch 实验员：负责最小证伪、资源预算、数据质控、实验矩阵、复现记录、分析与核心图表。

**Configured skills**

- `sr-research-shared`
- `sr-minimal-falsification`
- `sr-resource-budget`
- `sr-failure-fallback`
- `sr-data-generation-qc`
- `sr-data-split`
- `sr-baseline-reproduction`
- `sr-exploratory-experiment`
- `sr-main-comparison`
- `sr-ablation-study`
- `sr-sensitivity-robustness`
- `sr-generalization-ood`
- `sr-efficiency-resources`
- `sr-reproducible-run`
- `sr-quantitative-analysis`
- `sr-slice-analysis`
- `sr-good-failure-cases`
- `sr-mechanism-validation`
- `sr-core-figures`

**Referenced in instructions**

- None.

## `sr-method-builder`

ScienceResearch 方法构建者：负责文献证据、假设与知识树、数学模型、架构、实现契约和方法实验写作。

**Configured skills**

- `sr-research-shared`
- `sr-search-strategy`
- `sr-literature-screening`
- `sr-paper-evidence-card`
- `sr-literature-tree`
- `sr-novelty-tree`
- `sr-challenge-insight-tree`
- `sr-baseline-landscape`
- `sr-weekly-literature-update`
- `sr-observation-anomaly`
- `sr-core-hypothesis`
- `sr-idea-decomposition`
- `sr-idea-prioritization`
- `sr-dataflow-architecture`
- `sr-mathematical-model`
- `sr-module-challenge-mapping`
- `sr-data-schema-freeze`
- `sr-baseline-unification`
- `sr-algorithm-implementation-plan`
- `sr-methods-writing`
- `sr-experiments-writing`
- `sr-blocker-resolution`
- `sr-collaboration-interface`

**Referenced in instructions**

- None.

## `sr-principal-investigator`

ScienceResearch 首席研究员：负责研究问题与范围、阶段门控、资源路线决策、论文主张与成果交付。

**Configured skills**

- `sr-research-shared`
- `sr-weekly-meeting`
- `sr-scenario-needs`
- `sr-problem-formalization`
- `sr-scope-convergence`
- `sr-value-feasibility`
- `sr-claim-boundary-decision`
- `sr-core-claim-alignment`
- `sr-paper-storyline`
- `sr-abstract-introduction`
- `sr-rebuttal-revision`
- `sr-talk-open-source`
- `sr-last-week-acceptance`
- `sr-task-decomposition`
- `sr-milestone-evidence-gate`
- `sr-resource-scheduling`
- `sr-risk-contingency`
- `sr-weekly-plan`
- `sr-route-retrospective`
- `sr-stage-archive`

**Referenced in instructions**

- None.

## `sr-research-project-lead`

ScienceResearch 科研项目负责人：从项目文件夹中的工作包成效卡、交接书和原始证据判断研究阶段，形成 P0/P1 建议，并在明确授权后编排四个专业科研 Agent。

**Configured skills**

- `sr-research-shared`

**Referenced in instructions**

- None.
