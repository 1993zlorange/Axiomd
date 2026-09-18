---
title: "<内容简述>成果卡"
document_id: "sr-talk-open-source-<YYYYMMDD>"
version: "v0.1"
status: "草稿"
produced_at: "YYYY-MM-DD"
owner: "<负责人>"
source_contract: "<工作契约或证据路径>"
---

# <内容简述>

> 空白模板：只填写已核验事实、来源、计算、观察、解释和人工决定；未知项保持“待定”，不得用占位内容伪装结论。

## 1. 输出目的与范围

- 关联 SR/工作流 ID：
- 当前研究问题：
- 本文档解决的未知量：
- 听众、场合和希望记住的三点：
- 不在范围内：

## 2. 输入与证据

| 输入/证据 | 版本或时间 | 来源路径 | 可用性与限制 |
|---|---|---|---|
|  |  |  |  |

## 3. 人工基线与工作契约

- 人工基线：
- 工作契约：
- 权限级别：
- 人工检查点与停止条件：
- 模板 PPT 路径引用（不提交模板本身）：

## 4. 方法、过程与架构

### 4.1 方法/步骤

1.
2.
3.

### 4.2 输入-处理-输出

```text
源文档/证据 -> 主题与页计划 -> 模板化 PPT/讲稿/demo -> QA -> 人工排练与验收
```

### 4.3 关键假设、不变量与替代路径

| ID | 假设/不变量 | 证据 | 失效后的处理 |
|---|---|---|---|
|  |  |  |  |

## 5. PPT/Demo 发布计划

- 页计划路径：
- 源文档到页的映射：
- 模板版式检查：
- 三条关键 message：
- Demo/复现入口与环境：
- 讲稿与备注路径：
- 公开范围：

### 5.1 PPT 样式契约

```yaml
ppt_style:
  font: "Microsoft YaHei / 微软雅黑"
  title_bold: true
  summary_shape: "SR58-SUMMARY"
  summary_font_pt: "20-22 preferred; >=18 hard minimum"
  summary_per_page: "exactly one"
  body_min_pt: 18
  figure_table_label_min_pt: 14
  red_per_page_max: 3
  red_style: "bold+underline"
  blue_style: "bold"
  black_use: "normal facts; keywords may be bold"
  repeated_module_diff_highlight: true
  template_fidelity: "pass / partial / blocked"
```

### 5.2 逐页输出（摘要）

| 页 | 结论式页题 | SR58-SUMMARY 一句总结 | [级别] 要点与颜色样式 | 视觉/表格 | 删减/降级及理由 | 红色数 |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 6. 结果与证据

| 结果 ID | 结果/观察 | 证据路径 | 状态 |
|---|---|---|---|
|  |  |  | 建议 / 部分完成 / 阻塞 / 已接受 |

## 7. 结论边界

- 可以得出的结论：
- 不能得出的结论：
- 仍需验证：
- 潜在替代解释：

## 8. 风险、偏差与人工决定

| 风险/偏差 | 影响 | 缓解或补充证据 | 决策人 | 状态 |
|---|---|---|---|---|
|  |  |  |  |  |

## 9. 许可、隐私与发布检查

- 代码/数据/模型许可：
- 第三方素材与引用：
- 隐私、敏感信息、出口/合规约束：
- 公开发布授权：
- 仓库/归档路径：

## 10. 交付与追踪

- 产物路径（PPT / 页计划 / 讲稿 / README / demo）：
- 代码/数据/配置/图表版本：
- 需求或工作流追踪：
- 下一步：
- 人工判定：待定 / 接受 / 修改 / 暂停 / 拒绝

## 11. 关闭记录

```yaml
closure:
  skill: "sr-talk-open-source"
  artifact: "<YYYYMMDD-内容简述-成果卡.md>"
  evidence: []
  result: ""
  conclusion: ""
  cannot_conclude: []
  pptx_source_qa: "not-run"
  summary_sentence_qa: "not-run"
  template_fidelity: "not-applicable"
  color_semantics_qa: "not-applicable"
  font_size_qa: "not-applicable"
  human_rehearsal: "pending"
  public_release_approved: "pending"
  human_verdict: "待定"
  next_skill: "无"
```

文件命名：`YYYYMMDD-内容简述-文档类型.扩展名`；日期使用生产日期，内容简述使用稳定短语，文档类型使用“成果卡”“实验记录”“审查报告”或“PPT页计划”等中文名称。
