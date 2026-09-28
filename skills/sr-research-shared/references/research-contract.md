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

## Body writing and record standard

Every SR achievement card and workflow handoff follows [body-writing-standard.md](body-writing-standard.md). The approved standard has ten rules:

1. Reader and register: write for the doctoral researcher and supervisor in plain professional Chinese.
2. Plain verbs: replace governance wording with concrete actions and human decisions.
3. Content boundary: keep research content in the body; keep IDs, paths, code symbols, hashes, and session mechanics in frontmatter or appendices.
4. Structure: cards use the eight-question body; handoffs add compact transfer information and supervisor-decision questions.
5. Self-contained exposition: expand every hypothesis, method, nearest neighbor, budget, criterion, ledger, tier, or challenge label on first use using only recorded facts.
6. Dual-write numbers: write a spoken-language value plus the original recorded value in one parenthesis.
7. Code-like notation: use a Chinese name first and put task, solver, batch, version, or field identifiers in a ledger parenthesis; domain notation may remain with a first-use explanation.
8. Sentences and parentheses: use short sentences, at most one non-nested parenthesis per sentence, and at most two “conclusion first” signposts per document.
9. Empty or missing content: write “（本项无记录）” for an empty section and “未记录” for a missing field; use plain status wording in the body.
10. Safety net: keep governance fields synchronized between frontmatter and Appendix B; preserve a rewritten legacy draft in §9 or Appendix C; run the record validator.

Use the local leaf `assets/output-template.md` for an achievement card and the applicable `../sr-research-shared/assets/workflow-handoff-<stage>-template.md` for a workflow handoff. Run `../sr-research-shared/scripts/validate_sr_record.py <record.md>` when Python is available. A structural pass does not prove scientific truth.

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
