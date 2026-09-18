---
title: "<日期>-<内容简述>-PPT页计划"
document_id: "sr-talk-open-source-ppt-plan-<YYYYMMDD>"
source_documents: []
template_deck: "<用户提供的本地模板路径引用；不得提交私有模板>"
status: "草稿"
---

# PPT 页计划

> 只把源文档中已有证据支持的结论放入幻灯片。每页必须有且仅有一句放进 `SR58-SUMMARY` 的总结性完整句；缺失证据写“待定”或移入讲稿中的问题清单。

## Deck contract

```yaml
deck:
  audience: ""
  occasion: ""
  key_messages: []
  slide_size: ""
  template_layouts_inspected: false
  layout_map: {}
  language_font: "Microsoft YaHei / 微软雅黑"
  summary_shape: "SR58-SUMMARY"
  summary_font_pt: "20-22 preferred; >=18 hard minimum"
  output: "<YYYYMMDD-内容简述-学术汇报.pptx>"
  qa:
    summary_sentence_qa: "not-run"
    pptx_source_qa: "not-run"
    visual_template_qa: "not-run"
    human_rehearsal: "pending"
    public_release_approved: "pending"
```

## Claim map

| 源文档结论 | 类型 | 证据路径 | 用在页/层 | 一句总结 | 不能推出 |
|---|---|---|---|---|---|
|  | 结果/方法/设置/限制/决定 |  |  |  |  |

## Slide 1 — Cover

- `template_layout`：
- `summary_sentence`：`本汇报说明<问题>、<方法>和<主要结果>。`
- `summary_style`：`blue-bold`
- 标题：
- 副标题：汇报人 / 单位 / 日期
- 视觉：

## Slide 2 — Key conclusion

- 页题：`完成了 <交付> ｜ 用 <方法/证据> ｜ 实现 <结果/状态>`
- `summary_sentence`：`在<条件>下，<对象/方法>实现<量化结果>，支持<边界内结论>。`
- `summary_style`：`blue-bold` 或唯一页级决定项 `red-bold-underline`
- ① [critical] 红色+加粗+下划线：
- ② [important] 蓝色+加粗：
- ③ [normal] 黑色：
- 红色数量：
- 删减/降级：

## Slide 3 — Baseline / review

- 页题：`对照 <问题或承诺> ｜ 核验 <证据/基线> ｜ 确定 <差距/状态>`
- `summary_sentence`：`<证据>表明<已完成/仍差距>，因此<下一步判断>。`
- `summary_style`：`blue-bold`
- ① [important] 蓝色+加粗：
- ② [normal] 黑色：
- ③ [critical] 红色+加粗+下划线（仅重大缺口）：
- 删减/降级：

## Slide 4 — Agenda

- 页题：`按 <主线> 组织 ｜ 分 <N> 个主题 ｜ 优先讲 <关键项>`
- `summary_sentence`：`按<主线>依次说明<主题一>、<主题二>和<下一步>。`
- `summary_style`：`blue-bold`
- ① `<4-8字主题>`：
- ② `<4-8字主题>`：
- ③ `<4-8字主题>`：

## Slide N — Method / model setup

- 页题：`建立 <对象/模型> ｜ 用 <关键设置/方法> ｜ 支持 <后续验证>`
- `summary_sentence`：`通过<方法/设置>建立<对象>，解决<问题>并支撑<验证>。`
- `summary_style`：`blue-bold`
- ① [normal] 输入/对象：
- ② [normal] 关键参数/条件：
- ③ [important] 方法选择或假设：
- 视觉：小图 + 大标题 + 小字说明
- 删减/降级：

## Slide N — Result / evidence

- 页题：`得到 <结果> ｜ 在 <条件/基线> 下 ｜ 说明 <边界内结论>`
- `summary_sentence`：`在<条件>下，<对象/方法>实现<量化结果>，支持<边界内结论>。`
- `summary_style`：`blue-bold` 或唯一页级决定项 `red-bold-underline`
- ① [critical] 决定性指标/贡献（≤3 处）：
- ② [important] 重要结果/对比：
- ③ [normal] 数据集、单位、版本、条件：
- [de-emphasized] 建议删除：
- 视觉：图/表/逻辑图
- 差异高亮：变化数字/条件/状态：

## Slide N — Demo / reproducibility

- 页题：`运行 <入口> ｜ 在 <环境/版本> 下 ｜ 复现 <可检查结果>`
- `summary_sentence`：`在<环境/版本>中运行<入口>，得到<可检查结果>，当前支持<边界>。`
- `summary_style`：`blue-bold`
- ① [important] 运行入口/环境：
- ② [normal] 预期输出/耗时：
- ③ [critical] 许可、隐私或发布边界（如需决定）：
- 删减/降级：

## Slide N — Conclusion / next action

- 页题：`确认 <贡献> ｜ 保留 <边界> ｜ 下一步 <行动>`
- `summary_sentence`：`证据支持<贡献>，但不支持<超出边界>，下一步应<行动>。`
- `summary_style`：`blue-bold` 或唯一页级决定项 `red-bold-underline`
- ① [critical] 最重要结论：
- ② [important] 适用边界：
- ③ [normal] 下一步/所需决定：

## Slide N — Backup

- 页题：`补充 <证据类型> ｜ 支撑 <正文页码/结论> ｜ 边界 <不新增主张>`
- `summary_sentence`：`本页用<证据>支撑第<N>页的<结论>，不新增主张。`
- `summary_style`：`blue-bold`
- 目的：
- 证据：
- 版式：
- 为什么不进正文：

## Summary QA table

| Slide | SR58-SUMMARY 完整句 | 字数 | 样式 | 证据路径 | 是否只含一个主张 |
|---|---|---:|---|---|---|
|  |  |  |  |  |  |

## Per-page deletion/demotion log

| Slide | 原文/内容 | 处理 | 理由 |
|---|---|---|---|
|  |  | 删除 / 降级 / 讲稿 |  |

## Deck closure

```yaml
closure:
  skill: "sr-talk-open-source"
  artifact: "<YYYYMMDD-内容简述-学术汇报.pptx>"
  page_plan: "<YYYYMMDD-内容简述-PPT页计划.md>"
  evidence: []
  result: ""
  cannot_conclude: []
  summary_sentence_qa: "not-run"
  template_fidelity: "pass / partial / blocked"
  color_semantics_qa: "pass / warnings-accepted / fail / not-run"
  font_size_qa: "pass / warnings-accepted / fail / not-run"
  human_rehearsal: "pending / accepted / revise"
  public_release_approved: "pending / approved / rejected"
  human_verdict: "待定"
  next_skill: "sr-stage-archive"
```
