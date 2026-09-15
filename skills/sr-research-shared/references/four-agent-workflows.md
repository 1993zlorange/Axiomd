# SR Four-Agent Workflow and Artifact Contract

Version: 2026-09-10 revision 2

This contract defines the twelve specialist workflows, per-SR achievement cards, workflow handoffs, and upstream read dependencies. It replaces the former aggregate-card rule.

## Non-negotiable artifact rules

1. There is no aggregate workflow achievement card.
2. Each invoked SR leaf work package produces its own truthfully statused achievement card when that leaf closes.
3. Achievement-card filename: `YYYYMMDD-<short-result-name>-成果卡.md`; store `sr_id` and revision in frontmatter. The production date is the filename prefix.
4. Do not overwrite an accepted or cited prior card. Create a new production-date filename and link the superseded card.
5. Put each card directly in its SR aspect folder. Supporting code, data, figures, and logs may remain in governed subfolders and must be linked from the card.
6. A workflow handoff is separate from leaf cards. Put it in the workflow's designated subfolder and name it `YYYYMMDD-HHmmss-<工作简要>.md`.
7. Create a handoff whenever control moves to another workflow/agent, the workflow pauses or is blocked, or the workflow closes. Multiple chronological handoffs are expected.
8. A handoff must list every produced/updated SR card and keep the six required fields: 尝试了什么、发现了什么、支持证据、当前局限性、产出了什么、下一步该做什么.
9. Do not infer card acceptance from a filename. Use the card's status, evidence links, leaf closure, and named human verdict.
10. Legacy files named with `SR-NN_` or other patterns are evidence candidates, not compliant cards. Link them when reconstructing a new card; do not rename or overwrite them silently.

## Eight aspect folders

Resolve an existing project folder by its numeric prefix first. Preserve an existing semantic alias such as `03-Idea与科学假设`; for a new project, use the preferred name below.

| SR range | Research aspect | Preferred project folder |
|---|---|---|
| SR-01 to SR-06 | 研究问题与选题 | `01-研究问题与选题` |
| SR-07 to SR-14 | 文献调研与领域结构 | `02-文献调研与领域结构` |
| SR-15 to SR-21 | Idea科学假设与创新点 | `03-Idea科学假设与创新点` |
| SR-22 to SR-29 | 技术方案与方法设计 | `04-技术方案与方法设计` |
| SR-30 to SR-40 | 实验设计与执行 | `05-实验设计与执行` |
| SR-41 to SR-48 | 结果分析与问题诊断 | `06-结果分析与问题诊断` |
| SR-49 to SR-58 | 论文与成果表达 | `07-论文与成果表达` |
| SR-59 to SR-68 | 项目推进与下一步计划 | `08-项目推进与下一步计划` |

Before writing, locate exactly one matching aspect directory. Do not create a duplicate merely because its Chinese suffix differs.

## Workflow handoff folders

| Workflow | Handoff directory under project root |
|---|---|
| PI-E01 | `08-项目推进与下一步计划/PI-E01/` |
| PI-X01 | `08-项目推进与下一步计划/PI-X01/` |
| PI-P01 | `07-论文与成果表达/PI-P01/` |
| MB-E01 | `02-文献调研与领域结构/MB-E01/` |
| MB-X01 | `04-技术方案与方法设计/MB-X01/` |
| MB-P01 | `07-论文与成果表达/MB-P01/` |
| EX-E01 | `05-实验设计与执行/EX-E01/` |
| EX-X01 | `05-实验设计与执行/EX-X01/` |
| EX-P01 | `06-结果分析与问题诊断/EX-P01/` |
| CR-E01 | `01-研究问题与选题/CR-E01/` |
| CR-X01 | `06-结果分析与问题诊断/CR-X01/` |
| CR-P01 | `07-论文与成果表达/CR-P01/` |

If an existing aspect directory uses a semantic alias, place the workflow folder under that existing directory.

## Research flow

`PI-E01 -> MB-E01 <-> CR-E01 -> EX-E01 -> PI-X01(initial Gate F) -> MB-X01 -> EX-X01 -> CR-X01 -> PI-X01(result Gate) -> EX-P01 + MB-P01 -> PI-P01(draft) -> CR-P01 -> PI-P01(revision/archive) -> next-cycle PI-E01`

This is a dependency graph, not a forced one-pass line. A negative review or failed gate returns to the responsible upstream workflow. A reopened workflow reads all later handoffs that explicitly route work back to it.

## How to find inputs

For every listed card ID, search the whole corresponding aspect folder for dated achievement cards matching `YYYYMMDD-*-成果卡.md`. Read all non-superseded candidates and select the applicable version by the frontmatter SR ID, internal status, scope, human verdict, and evidence, not modification time. Follow evidence links to primary artifacts.

For every listed workflow folder, read all `*.md` handoffs in chronological filename order, then apply any explicit supersession links. Missing input is reported; it is never fabricated. “Conditional” means read it when the named situation exists, not that evidence checking is optional.

## Workflow input and output matrix

### Principal Investigator

#### PI-E01 Direction convergence and cycle kickoff

- Own leaf outputs: SR-01, SR-02, SR-03, SR-05, SR-59, SR-60, SR-66.
- Required card reads for an ongoing project: SR-59, SR-61, SR-65, SR-67, SR-68; latest SR-01, SR-02, SR-03, SR-05, SR-60, SR-66 when replanning.
- First-cycle exception: these prior-cycle cards may be absent; record `new_project`.
- Required handoff folders: `PI-P01/` from the prior cycle; `PI-X01/` when a gate or route decision returns the project to definition.
- Conditional handoff folders: any MB-E01, CR-E01, EX-E01, MB-X01, EX-X01, CR-X01, EX-P01, MB-P01, or CR-P01 handoff that explicitly routes back to PI-E01.
- Handoff output folder: `08-项目推进与下一步计划/PI-E01/`.

#### PI-X01 Evidence gate, resources, and route decision

- Own leaf outputs: SR-48, SR-61, SR-64, SR-65, SR-67.
- Required card reads at initial design Gate F: SR-03, SR-05, SR-16, SR-19, SR-20, SR-22, SR-23, SR-28, SR-29.
- Required card reads at result Gate: SR-24 through SR-40 and SR-44 through SR-47, plus latest SR-48, SR-61, SR-64, SR-65, SR-67 when re-entering.
- Required handoff folders: `MB-E01/`, `CR-E01/`, `EX-E01/` for Gate F; `MB-X01/`, `EX-X01/`, `CR-X01/` for the result gate.
- Conditional handoff folders: `EX-P01/`, `MB-P01/`, or `CR-P01/` when later evidence forces a claim or route reset.
- Handoff output folder: `08-项目推进与下一步计划/PI-X01/`.

#### PI-P01 Claims, storyline, revision, and delivery

- Own leaf outputs: SR-49, SR-50, SR-54, SR-57, SR-58, SR-68.
- Required card reads before the draft handoff: SR-02, SR-03, SR-04, SR-05, SR-11, SR-16, SR-17, SR-22, SR-23, SR-34 through SR-48, SR-51, SR-52, SR-53.
- Required card reads after review: SR-55 and SR-56, plus the latest SR-49, SR-50, SR-54, SR-57, SR-58, SR-68 if revising.
- Required handoff folders: `PI-X01/`, `EX-P01/`, `MB-P01/`; after draft review, `CR-P01/`.
- Conditional handoff folders: `CR-X01/` when review identifies unresolved result integrity or attribution.
- Handoff output folder: `07-论文与成果表达/PI-P01/`.

### Method Builder

#### MB-E01 Evidence to hypothesis and model blueprint

- Own leaf outputs: SR-07 through SR-16, SR-18, SR-21, SR-22, SR-23.
- Required card reads: SR-01 through SR-06.
- Re-entry card reads: latest SR-07 through SR-23 and SR-67 when review or new evidence changes the hypothesis/model.
- Required handoff folders: `PI-E01/`.
- Conditional handoff folders: `CR-E01/` for challenge-driven revision; `PI-X01/` when a gate returns the project to literature, hypothesis, architecture, or model design.
- Handoff output folder: `02-文献调研与领域结构/MB-E01/`.

#### MB-X01 Implementation contract, blockers, and interfaces

- Own leaf outputs: SR-24, SR-25, SR-26, SR-27, SR-62, SR-63.
- Required card reads: SR-16, SR-18 through SR-23, SR-28, SR-29.
- Gate-controlled card reads: SR-61, SR-64, SR-65 when PI-X01 has issued them.
- Rework card reads: SR-40, SR-44, SR-45, SR-46, SR-48 when diagnosis or claim boundaries require implementation changes.
- Required handoff folders: `MB-E01/`, `EX-E01/`, and the applicable `PI-X01/` Gate F handoff.
- Conditional handoff folders: `CR-X01/` and `EX-X01/` for implementation rework.
- Handoff output folder: `04-技术方案与方法设计/MB-X01/`.

#### MB-P01 Reproducible methods and experiments writing

- Own leaf outputs: SR-51, SR-52.
- Required card reads: SR-02, SR-03, SR-16, SR-22 through SR-40, SR-41, SR-42, SR-47, SR-48.
- Conditional card reads: SR-43 through SR-46 when cases, failures, diagnostics, or deviations affect reproducibility.
- Required handoff folders: `MB-X01/`, `EX-X01/`, `CR-X01/`, `PI-X01/`, and `EX-P01/` when analysis has closed.
- Conditional handoff folders: `CR-P01/` or `PI-P01/` when the manuscript is returned for technical correction.
- Handoff output folder: `07-论文与成果表达/MB-P01/`.

### Experimenter

#### EX-E01 Minimal falsification, resource budget, and fallback

- Own leaf outputs: SR-20, SR-28, SR-29.
- Required card reads: SR-02, SR-03, SR-05, SR-15, SR-16, SR-18, SR-19, SR-21, SR-22, SR-23.
- Conditional card reads: SR-17 when nearest-neighbor baselines constrain the minimal test; SR-64 and SR-65 on re-entry.
- Required handoff folders: `PI-E01/`, `MB-E01/`, `CR-E01/`.
- Conditional handoff folders: `PI-X01/` when Gate F requests a cheaper test or new budget.
- Handoff output folder: `05-实验设计与执行/EX-E01/`.

#### EX-X01 Data and formal experiment matrix

- Own leaf outputs: SR-30 through SR-39.
- Required card reads: SR-20, SR-22 through SR-29, SR-61, SR-64, SR-65.
- Re-run card reads: SR-40, SR-44, SR-45, SR-46, SR-48.
- Required handoff folders: `EX-E01/`, `MB-X01/`, and the applicable `PI-X01/` Gate F handoff.
- Conditional handoff folders: `CR-X01/` for diagnostics and `PI-X01/` for approved reruns or route changes.
- Handoff output folder: `05-实验设计与执行/EX-X01/`.

#### EX-P01 Quantitative analysis, cases, mechanism, and figures

- Own leaf outputs: SR-41, SR-42, SR-43, SR-47, SR-53.
- Required card reads: SR-30 through SR-40, SR-44, SR-45, SR-46, SR-48.
- Conditional card reads: SR-16, SR-19, SR-22, SR-23 when interpreting mechanism against the original hypothesis/model.
- Required handoff folders: `EX-X01/`, `CR-X01/`, `PI-X01/`.
- Conditional handoff folders: `CR-P01/` or `PI-P01/` when review requires a revised analysis or figure.
- Handoff output folder: `06-结果分析与问题诊断/EX-P01/`.

### Critical Reviewer

#### CR-E01 Problem validity and counterexample challenge

- Own leaf outputs: SR-04, SR-06, SR-17, SR-19.
- Required card reads: SR-01, SR-02, SR-03, SR-05, SR-07 through SR-16, SR-18, SR-21, SR-22, SR-23.
- Re-entry card reads: latest SR-04, SR-06, SR-17, SR-19 and SR-67.
- Required handoff folders: `PI-E01/`, `MB-E01/`.
- Conditional handoff folders: `PI-X01/` when a gate requests renewed problem, novelty, or mechanism challenge.
- Handoff output folder: `01-研究问题与选题/CR-E01/`.

#### CR-X01 Result integrity, error analysis, and minimal diagnosis

- Own leaf outputs: SR-40, SR-44, SR-45, SR-46.
- Required card reads: SR-20, SR-24 through SR-39, SR-61.
- Conditional card reads: SR-16, SR-19, SR-22, SR-23 for hypothesis/model consistency; latest SR-40 and SR-44 through SR-46 on re-entry.
- Required handoff folders: `MB-X01/`, `EX-X01/`.
- Conditional handoff folders: `PI-X01/` when a gate asks for more diagnosis.
- Handoff output folder: `06-结果分析与问题诊断/CR-X01/`.

#### CR-P01 Simulated peer review and comment analysis

- Own leaf outputs: SR-55, SR-56.
- Required card reads: SR-04, SR-06, SR-11, SR-17, SR-34 through SR-55.
- Conditional card reads: SR-22 through SR-33 when auditing method and experiment traceability; SR-57 when checking a revised response.
- Required handoff folders: `EX-P01/`, `MB-P01/`, and the draft-stage `PI-P01/`.
- Conditional handoff folders: `CR-X01/` when unresolved integrity/attribution is material.
- Handoff output folder: `07-论文与成果表达/CR-P01/`.

## Per-SR achievement card template

Filename: `YYYYMMDD-<成果简称>-成果卡.md`

```yaml
achievement_card:
  card_id: "SR-<NN>[-vN]"
  sr_id: "SR-<NN>"
  short_name: ""
  skill: "sr-..."
  agent: ""
  workflow_id: ""
  aspect_folder: ""
  status: "accepted|partial|blocked|rejected"
  human_baseline_ref: ""
  work_contract_ref: ""
  attempted: []
  findings: []
  evidence:
    - label: "fact|source_claim|observation|calculation|interpretation|hypothesis|decision|plan"
      locator: ""
      supports: ""
  artifacts: []
  conclusion: ""
  cannot_conclude: []
  deviations: []
  human_verdict:
    owner: ""
    verdict: "accepted|revise|pause|reject|pending"
    rationale: ""
  next_workflow: ""
```

A card is a reviewable record, not merely a wrapper around prose. A blocked or rejected leaf still receives a truthful card if its attempts and evidence matter.

## Workflow handoff template

Filename: `YYYYMMDD-HHmmss-<工作简要>.md`

```yaml
handoff:
  handoff_id: "HO-<workflow-id>-<YYYYMMDD-HHmmss>"
  created_at: "YYYY-MM-DDTHH:mm:ss+08:00"
  work_summary: ""
  from_agent: ""
  to_agent: ""
  workflow_id: ""
  workflow_status: "accepted|partial|blocked|rejected"
  produced_or_updated_cards:
    - "relative/path/YYYYMMDD-成果简称-成果卡.md"
  cards_read:
    - "relative/path/YYYYMMDD-成果简称-成果卡.md"
  handoffs_read:
    - "relative/path/YYYYMMDD-HHmmss-工作简要.md"
  human_decision_required: false
  human_decision_ref: ""
  尝试了什么:
    - ""
  发现了什么:
    - ""
  支持证据:
    - locator: ""
      evidence_type: ""
      supports: ""
  当前局限性:
    - ""
  产出了什么:
    - artifact: ""
      purpose: ""
  下一步该做什么:
    - owner: ""
      workflow: ""
      action: ""
      prerequisite: ""
      definition_of_done: ""
```

The receiving workflow first validates every listed card and handoff path, then opens its own work contract. “下一步该做什么” is a recommendation, not authorization.
