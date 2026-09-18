---
title: "<内容简述>成果卡"
document_id: "sr-core-figures-<YYYYMMDD>"
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
- 目标图表类型与最终尺寸：
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

## 4. 图表契约

- 唯一 message：
- 原始数据/结果证据：
- 数据到视觉编码映射：
- 比较基线与公平性：
- 不确定性/误差呈现：
- 色彩、形状、单位和可读性检查：
- 结论边界与图注草案：

### 4.1 draw.io 契约（如适用）

```yaml
drawio:
  source_path: ""
  archetype: ""
  topology_and_reading_order: ""
  layout_grid_and_routing: ""
  semantic_glyphs: []
  formulas_and_units: []
  source_qa: "pass / warnings-accepted / fail / not-run"
  preview_export: "pass / fail / blocked"
  visual_inspection: "pass / revisions-required / not-run"
  reviewer_risks: []
```

## 5. 方法、过程与架构

### 5.1 方法/步骤

1.
2.
3.

### 5.2 输入-处理-输出

```text
输入 -> 处理/判定 -> 输出或失败边界
```

### 5.3 关键假设、不变量与替代路径

| ID | 假设/不变量 | 证据 | 失效后的处理 |
|---|---|---|---|
|  |  |  |  |

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

## 9. 交付与追踪

- 产物路径（源文件 / 代码 / 导出预览）：
- 代码/数据/配置/图表版本：
- 需求或工作流追踪：
- 下一步：
- 人工判定：待定 / 接受 / 修改 / 暂停 / 拒绝

## 10. 关闭记录

```yaml
closure:
  skill: "sr-core-figures"
  artifact: "<YYYYMMDD-内容简述-成果卡.md>"
  evidence: []
  result: ""
  conclusion: ""
  cannot_conclude: []
  drawio_source_qa: "not-applicable"
  drawio_preview_export: "not-applicable"
  human_verdict: "待定"
  next_skill: "无"
```

文件命名：`YYYYMMDD-内容简述-文档类型.扩展名`；日期使用生产日期，内容简述使用稳定短语，文档类型使用“成果卡”“实验记录”或“审查报告”等中文名称。
