# SR Research Contract

Every SR leaf workflow uses the same start and close contract. Keep the scientific judgment human-owned while making the work inspectable and reproducible.

## Human baseline

Before AI synthesis, obtain a short `human_baseline`. The researcher spends roughly 15–30 minutes writing from memory or inspecting the primary material first. Do not enforce elapsed time mechanically; require the content:

```yaml
human_baseline:
  current_unknown: ""
  initial_judgment: ""
  evidence_already_checked: []
  competing_explanations: []
  decision_needed: ""
```

If the user already supplied equivalent information, reuse it. If they cannot form a baseline because the field is new, help them write questions and unknowns without supplying a fake judgment.

## Work contract

Return this contract before substantial work:

```yaml
work_contract:
  skill: "sr-..."
  research_question: ""
  current_unknown: ""
  inputs: []
  assumptions: []
  deliverable: ""
  definition_of_done: []
  permission_level: "L0|L1|L2|L3"
  human_checkpoints: []
  stop_condition: ""
```

Permission levels:

- `L0`: read, organize, reason, draft, or analyze provided/local material without external mutation.
- `L1`: create or edit local research artifacts, scripts, figures, and reports in the user-approved scope.
- `L2`: run bounded computation or experiments that consume material resources; the human approves the plan, budget, and stop conditions first.
- `L3`: contact external systems or people, submit, publish, release, purchase, alter shared resources, or handle ethics/privacy-sensitive data; require explicit authorization immediately before action.

## Evidence discipline

Label statements as one of: `fact`, `source_claim`, `observation`, `calculation`, `interpretation`, `hypothesis`, `decision`, or `plan`. Preserve source location, data version, code/config version, and uncertainty whenever they matter. Missing evidence becomes a placeholder or open item, never invented content.

## Closure record

Do not call a work package complete because prose was produced. Close it only when the leaf completion gate is satisfied and the human-owned verdict has been recorded where required.

```yaml
closure:
  skill: "sr-..."
  artifact: "path, identifier, or inline section"
  achievement_card: "project-relative path/YYYYMMDD-内容简述-成果卡.md"
  evidence: []
  result: ""
  conclusion: ""
  cannot_conclude: []
  deviations: []
  human_verdict: "accepted|revise|pause|reject|pending"
  next_skill: "sr-...|none"
  next_question: ""
```

For a four-agent research project, every closed leaf writes its own achievement card using the local `assets/output-template.md`, the SR ID in frontmatter, and the aspect-folder mapping in `four-agent-workflows.md`. Every produced document uses `YYYYMMDD-内容简述-文档类型.扩展名`; the SR ID is not used as the filename prefix. The workflow handoff separately records `produced_or_updated_cards`, `cards_read`, and `handoffs_read`; a workflow-level aggregate card is prohibited.
