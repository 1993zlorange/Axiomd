### 数据图

先填写 [图表说明模板](../assets/figure-contract-template.md)，明确唯一结论、数据版本、样本量、比较对象、单位、不确定性及结论范围。具体做法见 [科学绘图说明](scientific-figure-authoring.md)。选择图型时可参照 [导师汇报图型](advisor-figure-patterns.md)、[参考图索引](figure-pattern-exemplars.md) 和 [论文图型](paper-figure-patterns.md)，参考图只提供结构，不提供研究事实。

从原始数据生成图，保留原始点、统计口径及排除理由。颜色、线型和点形各自表达稳定含义；图例不遮挡数据，多面板必须服务于直接比较。交付绘图源及 SVG/PDF，并检查导出图的文字、单位、图例和数值。可运行本目录 `scripts/qa_scientific_figure.py <图表说明.md> --figure <图.svg>`，修复错误并说明未解决警告。缺少导出工具时如实记录 `export_status=blocked`，不能把结构检查当成视觉检查。

### 可编辑示意图

流程、技术路线、机制或架构图默认交付 `.drawio` 源文件；用户指定其他可编辑格式时遵从用户。按 [绘制方法](drawio-authoring.md)、[视觉语言](drawio-visual-language.md) 和 [导出检查](drawio-export-qa.md) 完成。

使用未压缩的 mxGraph XML、稳定的节点标识、连接源/目标的箭头和留有连线通道的网格。公式放入独立单元，并在 `mxGraphModel` 设置 `math="1"`。编辑时保留已有页面、标识、分组和无关内容。运行本目录 `scripts/qa_drawio.py <图.drawio>`；通过 diagrams.net/draw.io 导出预览，确认导出对应实际源文件。工具缺失时交付源文件并标记 `preview_export=blocked`，不伪造已查看预览。
