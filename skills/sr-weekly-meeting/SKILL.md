---
name: sr-weekly-meeting
description: Build a doctoral weekly group-meeting report from closed or truthfully statused SR work contracts, artifacts, evidence, conclusion boundaries, blockers, and next-week decisions. Use after one or more SR leaf workflows have produced reviewable outputs. Do not invent progress from chat history or replace unfinished scientific work with polished slides.
metadata:
  short-description: Turn verified SR outputs into a weekly group-meeting report
---

# SR Weekly Meeting

Read [../sr-research-shared/references/weekly-loop.md](../sr-research-shared/references/weekly-loop.md) and the weekly template in `idea/科研工作分解与每周组会汇报模板_20260828.md`.

## Intake

Collect the reporting week, overall research question, last week's commitments, selected SR work contracts, closure records, artifact paths, failed attempts, blockers, and the decision needed from the group. Mark absent evidence as missing.

## Human-first pass

The doctoral researcher first writes three lines without AI: the most important result, what it does not establish, and the question the supervisor should answer. AI may challenge and refine these lines but may not silently replace the scientific judgment.

## Build the report

1. Verify last week's commitments with `sr-last-week-acceptance` output.
2. Select only one or two substantive work packages for the main narrative.
3. For each, present question → action → evidence → interpretation → boundary → next decision.
4. Use conclusion-style slide/page titles. Show units, sample size, uncertainty, versions, and artifact locations where applicable.
5. Include failures when they remove a hypothesis or narrow the search space.
6. End with one P0, at most two P1 items, their deliverables, definitions of done, risks, and requested human decisions.

## Human checkpoints

- The researcher approves the opening conclusion and every scientific claim.
- The researcher selects what confidential or unpublished material may be shown.
- The researcher presents the options and recommendation to the group; AI does not impersonate supervisor approval.

## Output template

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the report `YYYYMMDD-内容简述-周组会汇报.md`; keep the reporting week and human-approved claim boundaries explicit.

```markdown
# 第 N 周组会：一句话核心结论

## 本周摘要
- 本周目标：
- 主要 SR Skill：
- 新增认识：
- 关键证据/产物：
- 当前不能得出的结论：
- 希望组会决策：

## 上周任务验收
| 承诺 | 完成标准 | 实际产物 | 状态 | 偏差 |
|---|---|---|---|---|

## 工作一/二
- 问题与开始前判断：
- 行动与控制条件：
- 结果与证据：
- 解释与边界：
- 下一步决策：

## 下周计划
| 优先级 | SR Skill | 任务 | 交付物 | 完成标准 | 风险 |
|---|---|---|---|---|---|
```

The report is ready only when every result points to evidence, unsupported statements are labeled, and the researcher has approved claim strength and the requested meeting decision.
