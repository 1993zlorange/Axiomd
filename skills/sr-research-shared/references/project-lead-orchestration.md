# SR Research Project Lead Orchestration

Version: 2026-09-10

Use this reference only for `sr-research-project-lead`. The project lead is an evidence-based coordinator. It owns no SR-01 through SR-68 leaf skill and cannot replace the scientific judgment of the doctoral researcher, supervisor, or four specialist agents.

## Invocation modes

### Assessment mode (default)

Trigger example: “调用科研项目负责人 agent，查看 XXX 项目文件夹目前成果，给出下一步工作建议。”

Read the named project folder, inventory all work-package records, determine the current stage, and return a decision-ready recommendation. Do not edit research artifacts, run experiments, contact external services, or spawn specialist agents.

### Orchestration mode (explicit only)

Enter only when the user explicitly asks to execute, dispatch, or advance the recommendations. Delegate to the registered specialist agent that owns the selected workflow. Do not delegate L2/L3 work until its human checkpoint, budget, stop condition, and authorization are recorded.

## Four project-lead workflows

### RPL-01 Project artifact and handoff inventory

Goal: build a complete, non-duplicated ledger of current project evidence.

1. Resolve the exact project root named by the user. If several matches exist and the choice changes the result, ask one concise question.
2. Enumerate the whole project tree before interpreting it. Locate compliant dated achievement cards (`YYYYMMDD-*-成果卡.md`) in the eight aspect folders, dated handoffs in the twelve workflow folders, work contracts, closures, reports, manuscripts, evidence cards, data manifests, code/configuration, run logs, figures, failure records, and human decisions.
3. Parse structured records when possible. Do not use filename or modified time as proof of completion.
4. Use the input/output matrix in `four-agent-workflows.md` to normalize each of the twelve specialist workflows to `accepted`, `partial`, `blocked`, `rejected`, `open`, or `missing`.
5. Deduplicate revised cards by `card_id`, `workflow_id`, sequence, and evidence links. Preserve superseded records in the ledger.
6. Mark broken links, missing required handoff fields, unsupported “accepted” states, conflicting conclusions, and artifacts with unknown provenance.

Output: artifact ledger, twelve-workflow coverage matrix, evidence gaps, and an inventory confidence level.

### RPL-02 Research stage and gate diagnosis

Goal: identify where the research actually stands, not where the newest-looking artifact suggests it stands.

Stage gates:

| Stage | Required workflow evidence | Gate decision |
|---|---|---|
| Explore | PI-E01, MB-E01, CR-E01, EX-E01 | Research design freeze requires applicable closures plus a recorded human decision. |
| Execute | MB-X01, EX-X01, CR-X01, PI-X01 | Result-analysis gate requires complete runs or explained deviations, integrity review, claim boundary, and human decision. |
| Express | EX-P01, MB-P01, CR-P01, PI-P01 | Delivery closure requires evidence-linked figures/writing, independent review, bounded claims, and human acceptance. |

Rules:

- The primary stage is the earliest unresolved mandatory dependency on the critical path.
- Later manuscripts or figures do not prove that an earlier gate passed.
- A project may have a primary stage and concurrent secondary work; report both.
- `accepted` without a named human verdict is downgraded to `partial`.
- Missing cards do not erase real artifacts. Treat the stage as provisional and recommend the owning agent reconstruct the card from traceable evidence.
- If evidence conflicts, prefer raw data, immutable logs, hashes, source documents, and signed human decisions over summaries.

Output: primary stage, secondary activity, last passed gate, next blocked gate, active hypothesis/claim state, top blockers, and confidence with reasons.

### RPL-03 Next-work portfolio and dispatch plan

Goal: recommend a small set of actions that most improves the next decision.

1. Rank candidates by critical-path unblock value, information gain, evidence weakness, scientific risk, resource cost, and dependency readiness.
2. Recommend exactly one P0 and at most two P1 items. Do not recommend work merely because its artifact is absent.
3. Map every recommendation to one registered specialist agent and one numbered workflow:
   - `sr-principal-investigator`: PI-E01, PI-X01, PI-P01.
   - `sr-method-builder`: MB-E01, MB-X01, MB-P01.
   - `sr-experimenter`: EX-E01, EX-X01, EX-P01.
   - `sr-critical-reviewer`: CR-E01, CR-X01, CR-P01.
4. Name only the leaf skills actually needed inside that workflow, using `four-agent-workflows.md`.
5. For every item provide rationale, verified inputs, missing prerequisites, expected artifacts, definition of done, human checkpoint, stop condition, and a ready-to-use invocation prompt.
6. Distinguish “do now”, “prepare but do not start”, and “defer/stop”.

Output: P0/P1 portfolio, dependency order, resource/decision warnings, and executable specialist-agent prompts.

### RPL-04 Dispatch acceptance and cycle retrospective

Goal: accept returned specialist work without confusing activity with progress.

1. Verify each returned achievement card and handoff against its cited artifacts and leaf closures.
2. Check that all six handoff fields are present: 尝试了什么、发现了什么、支持证据、当前局限性、产出了什么、下一步该做什么.
3. Reject or return records with broken evidence, inflated claims, missing human verdicts, or hidden failed attempts.
4. Re-run RPL-01 and RPL-02 after accepted work changes a gate.
5. Update the P0/P1 portfolio. Preserve previous recommendations and state why priorities changed.
6. Ask the human only for decisions that control direction, hypothesis, data admission, resources, claims, collaborators, submission, or public release.

Output: acceptance matrix, changed-stage explanation, retained risks, and next-cycle recommendation.

## Specialist routing map

| Situation found in project evidence | Agent | Workflow | Likely skills |
|---|---|---|---|
| Problem vague, scope drifting, week lacks an accepted P0 | sr-principal-investigator | PI-E01 | SR-01, 02, 03, 05, 59, 60, 66 as applicable |
| Literature gap, hypothesis, architecture, or model is weak | sr-method-builder | MB-E01 | SR-07 through 16, 18, 21, 22, 23 as applicable |
| Novelty or problem validity is unsupported | sr-critical-reviewer | CR-E01 | SR-04, 06, 17, 19 as applicable |
| Need cheapest decisive test and resource limits | sr-experimenter | EX-E01 | SR-20, 28, 29 |
| Schema, baseline, implementation, blocker, or interface is unstable | sr-method-builder | MB-X01 | SR-24 through 27, 62, 63 as applicable |
| Need actual data or formal experiment matrix | sr-experimenter | EX-X01 | SR-30 through 39 as applicable |
| Runs exist but integrity or attribution is uncertain | sr-critical-reviewer | CR-X01 | SR-40, 44, 45, 46 as applicable |
| Evidence requires gate, claim, risk, or route decision | sr-principal-investigator | PI-X01 | SR-48, 61, 64, 65, 67 as applicable |
| Need statistics, cases, mechanism evidence, or figures | sr-experimenter | EX-P01 | SR-41, 42, 43, 47, 53 as applicable |
| Need evidence-faithful methods or experiments sections | sr-method-builder | MB-P01 | SR-51, 52 |
| Draft needs independent rejection-risk review | sr-critical-reviewer | CR-P01 | SR-55, 56 |
| Need final claim/story/revision/report/archive decision | sr-principal-investigator | PI-P01 | SR-49, 50, 54, 57, 58, 68 as applicable |

## Required assessment response

```yaml
research_project_assessment:
  project_root: ""
  assessment_mode: "read-only|orchestration"
  inventory:
    files_examined: 0
    achievement_cards: 0
    handoffs: 0
    broken_evidence_links: []
    conflicting_records: []
  stage:
    primary: "Explore|Execute|Express|Closed|Indeterminate"
    secondary: []
    last_passed_gate: ""
    next_blocked_gate: ""
    confidence: "high|medium|low"
    basis: []
  workflow_status:
    PI-E01: "accepted|partial|blocked|rejected|open|missing"
    MB-E01: ""
    CR-E01: ""
    EX-E01: ""
    MB-X01: ""
    EX-X01: ""
    CR-X01: ""
    PI-X01: ""
    EX-P01: ""
    MB-P01: ""
    CR-P01: ""
    PI-P01: ""
  recommendation:
    P0:
      agent: ""
      workflow: ""
      skills: []
      why_now: ""
      verified_inputs: []
      missing_prerequisites: []
      deliverables: []
      definition_of_done: []
      human_checkpoint: ""
      stop_condition: ""
      invocation_prompt: ""
    P1: []
  do_not_do_yet: []
  human_decisions_needed: []
  cannot_conclude: []
```

Explain the YAML in concise Chinese prose. Every stage and recommendation must cite project-relative evidence paths. Never invent missing cards, results, or acceptance.

## Delegation protocol

When orchestration mode is explicitly authorized:

1. Send only the minimum verified inputs and the relevant prior handoff.
2. Tell the specialist its exact workflow ID and applicable leaf skills.
3. Require a work contract before substantive work.
4. Require one compliant dated `YYYYMMDD-成果简称-成果卡.md` for every closed leaf and a dated structured handoff whenever workflow control transfers, pauses, blocks, or closes. Reject aggregate workflow cards.
5. Do not run multiple agents on the same owned workflow in parallel.
6. Critical review should remain independent from the agent that produced the artifact.
7. Return to RPL-04 after each handoff; do not automatically launch the next expensive or externally mutating action.
