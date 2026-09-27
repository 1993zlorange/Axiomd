---
title: "<日期>-<内容简述>-PPT页计划"
document_id: "sr-talk-open-source-ppt-plan-<YYYYMMDD>"
source_documents: []
template_deck: "<用户提供的本地模板路径引用；不得提交私有模板>"
status: "草稿"
---

# PPT 页计划

> 每页先声明唯一认知对象和版式，再写结论式标题与 `SR58-SUMMARY`。证据不足写“待定”；待验证内容默认进入 backup 或下一步页，不占据正文主链。

## Deck contract

```yaml
deck:
  presentation_mode: "group-meeting-process-review | academic-talk | quick-review | release-demo"
  audience: ""
  occasion: ""
  key_messages: []
  page_budget: "18-25"
  slide_size: ""
  template_layouts_inspected: false
  layout_map: {}
  language_font: "Microsoft YaHei / 微软雅黑"
  summary_shape: "SR58-SUMMARY"
  summary_font_pt: "20-22 preferred; >=18 hard minimum"
  narrative_order:
    - "advisor_context"
    - "key_conclusion"
    - "agenda"
    - "artifact_evidence"
    - "motivation"
    - "mechanisms"
    - "practice_cases"
    - "reflection"
    - "next_plan"
    - "backup"
  output: "<YYYYMMDD-内容简述-学术汇报.pptx>"
  qa:
    cognitive_object_qa: "not-run"
    layout_qa: "not-run"
    summary_sentence_qa: "not-run"
    pptx_source_qa: "not-run"
    visual_template_qa: "not-run"
    human_rehearsal: "pending"
    public_release_approved: "pending"
```

## Evidence coverage matrix

| 证据簇 / 实践案例 | 认知对象 | 正文页 | Backup | 讲稿 | 删除 | 理由 |
|---|---|---:|---:|---:|---:|---|
|  | artifact / case / metric / risk |  |  |  |  |  |

## Claim map

| 源文档结论 | 类型 | 证据路径 | 用在页/层 | kicker | 一句总结 | 不能推出 |
|---|---|---|---|---|---|---|
|  | 结果/方法/设置/限制/决定 |  |  |  |  |  |

## Slide contract

```yaml
slide:
  no: 1
  kicker: "0.1 成果"
  title: "完成了 <交付> ｜ 用 <方法/证据> ｜ 实现 <结果/状态>"
  cognitive_type: "claim"
  layout_pattern: "claim"
  summary_sentence: "在<条件>下，<对象/方法>实现<结果>，支持<结论边界>。"
  summary_style: "blue-bold"
  summary_shape: "SR58-SUMMARY"
  purpose: ""
  evidence: []
  layout:
    text_area_ratio: 0.60
    visual_area_ratio: 0.40
  visual:
    type: "none | screenshot | logic-diagram | table | chart"
    nodes: 0
    branches: 0
    gates: []
    loops: []
  bullets:
    - text: ""
      level: "critical | important | normal | de-emphasized"
      style: "红色+加粗+下划线 | 蓝色+加粗 | 黑色关键词可加粗 | 黑色常规"
  repeated_module_difference: ""
  split_check:
    one_cognitive_object: true
    needs_two_summaries: false
    split_recommended: false
    density_exception_reason: ""
  deletion:
    - text: ""
      action: "delete | demote | speaker-notes"
      reason: ""
  red_count: 0
```

## Slide 1 — Cover

- `kicker`：`cover`
- `title`：
- `cognitive_type`：`context`
- `layout_pattern`：`claim`
- `summary_sentence`：`本汇报说明<问题>、<方法>和<主要结果>。`
- `summary_style`：`blue-bold`
- 副标题：汇报人 / 单位 / 日期
- 视觉与证据：

## Slide 2 — Advisor context / last commitments

- `kicker`：`0.1 上周`
- `title`：`对照 <导师建议/上周承诺> ｜ 核验 <实际产物> ｜ 确定 <状态>`
- `cognitive_type`：`context`
- `layout_pattern`：`claim`
- `summary_sentence`：`<证据>表明<已完成/仍差距>，因此<下一步判断>。`
- [important] 蓝色+加粗：
- [normal] 黑色：
- 删减/降级：

## Slide 3 — Key conclusion

- `kicker`：`0.2 核心结论`
- `title`：`完成了 <交付> ｜ 用 <方法/证据> ｜ 实现 <结果/状态>`
- `cognitive_type`：`claim`
- `layout_pattern`：`claim`
- `summary_sentence`：`在<条件>下，<对象/方法>实现<量化结果>，支持<边界内结论>。`
- `summary_style`：`blue-bold` 或唯一页级决定项 `red-bold-underline`
- ① [critical] 红色+加粗+下划线：
- ② [important] 蓝色+加粗：
- ③ [normal] 黑色：
- 红色数量：
- 删减/降级：

## Slide 4 — Agenda

- `kicker`：`agenda`
- `title`：`按 <主线> 组织 ｜ 分 <N> 个主题 ｜ 优先讲 <关键项>`
- `cognitive_type`：`context`
- `layout_pattern`：`claim`
- `summary_sentence`：`按<主线>依次说明<主题一>、<主题二>和<下一步>。`
- ① `<4-8字主题>`：
- ② `<4-8字主题>`：
- ③ `<4-8字主题>`：

## Slide N — Artifact evidence

- `kicker`：`0.3 成果｜<对象>`
- `title`：`构建 <系统/数据/归档> ｜ 显示 <可检查状态> ｜ 支撑 <结论>`
- `cognitive_type`：`artifact`
- `layout_pattern`：`evidence-screenshot`
- `summary_sentence`：`<截图/记录>显示<对象>已实现<可检查状态>，边界为<限制>。`
- 视觉：截图占 55–70%，编号标注不超过 5 个
- 证据路径 / 版本 / 时间：
- 人工验收状态：

## Slide N — Motivation

- `kicker`：`1.1 动机`
- `title`：`针对 <核心问题> ｜ 识别 <约束/痛点> ｜ 导出 <设计目标>`
- `cognitive_type`：`context`
- `layout_pattern`：`mechanism-map`
- `summary_sentence`：`<问题/约束>要求<设计目标>，因此采用<方向>。`
- 视觉：三栏或三卡片，不叠加第二套分类框架

## Slide N — Mechanism

- `kicker`：`2.N 机制N｜<4-8字对象>`
- `title`：`建立 <机制> ｜ 用 <关键规则> ｜ 避免 <失效方式>`
- `cognitive_type`：`mechanism | role | process | architecture`
- `layout_pattern`：`mechanism-map | process-flow | architecture`
- `summary_sentence`：`通过<机制/规则>建立<对象>，解决<问题>并支撑<验证>。`
- 逻辑图契约：节点数 / 分支数 / 人工门 / 回跳：
- 硬规则或边界：

## Slide N — Practice case

- `kicker`：`3.N 实践N｜<4-8字案例>`
- `title`：`在 <案例场景> 中 ｜ 执行 <工作流> ｜ 得到 <可检查结果>`
- `cognitive_type`：`case`
- `layout_pattern`：`case`
- `summary_sentence`：`在<案例>中运行<工作流>，得到<输出/经验>，不能推出<边界外结论>。`
- 输入 / 行动 / 输出：
- 负面或待验证边界：

## Slide N — Reflection

- `kicker`：`4.N 反思N｜<4-8字对象>`
- `title`：`明确 <人机分工> ｜ 保留 <关键把关> ｜ 降低 <风险>`
- `cognitive_type`：`reflection`
- `layout_pattern`：`reflection`
- `summary_sentence`： `<风险>要求人保留<关键决策>，AI承担<执行/验证方式>。`
- 战略层 / 操作层 / 执行层：
- 永不放手事项：

## Slide N — Next action

- `kicker`：`5.1 下一步`
- `title`：`锁定 <P0/P1> ｜ 交付 <可检查物> ｜ 以 <DoD> 验收`
- `cognitive_type`：`decision`
- `layout_pattern`：`claim`
- `summary_sentence`：`下一步优先完成<P0>，因为它直接决定<未知量/导师要求>。`
- P0 / 至多两个 P1：
- 责任人、时间、风险：

## Slide N — Backup

- `kicker`：`B.N 备份`
- `title`：`补充 <证据类型> ｜ 支撑 <正文页码/结论> ｜ 不新增主张`
- `cognitive_type`：`backup`
- `layout_pattern`：`evidence-screenshot | case`
- `summary_sentence`：`本页用<证据>支撑第<N>页的<结论>，不新增主张。`
- 为什么不进正文：

## Cognitive-object / layout QA table

| Slide | kicker | 认知对象 | 版式 | 文字区 | 视觉区 | 节点/分支 | 一句总结 | 拆页检查 |
|---:|---|---|---|---:|---:|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Per-page deletion/demotion log

| Slide | 原文/内容 | 处理 | 理由 |
|---|---|---|---|
|  |  | 删除 / 降级 / 讲稿 / backup |  |

## Human revision feedback

```yaml
revision_feedback:
  retrospective_record: ""
  applied_candidate_rules: []
  applied_stable_rules: []
  rejected_one_off_preferences: []
  unresolved_conflicts: []
```

## Deck closure

```yaml
closure:
  skill: "sr-talk-open-source"
  artifact: "<YYYYMMDD-内容简述-学术汇报.pptx>"
  page_plan: "<YYYYMMDD-内容简述-PPT页计划.md>"
  evidence: []
  result: ""
  cannot_conclude: []
  cognitive_object_qa: "not-run"
  layout_qa: "not-run"
  summary_sentence_qa: "not-run"
  template_fidelity: "pass / partial / blocked"
  color_semantics_qa: "pass / warnings-accepted / fail / not-run"
  font_size_qa: "pass / warnings-accepted / fail / not-run"
  human_revision_retrospective: "not-applicable / recorded"
  human_rehearsal: "pending / accepted / revise"
  public_release_approved: "pending / approved / rejected"
  human_verdict: "待定"
  next_skill: "sr-stage-archive"
```
