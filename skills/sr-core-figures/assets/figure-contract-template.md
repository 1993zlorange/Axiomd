# 科学图表约定模板

使用说明：先在项目内复制本模板，逐项替换占位内容；导出前运行 `python skills/sr-core-figures/scripts/qa_scientific_figure.py <图表约定.md> --figure <figure.svg>`。路径写项目内相对路径，不写本机绝对路径。

```yaml
figure_id: "<YYYYMMDD-图表简称>"
figure_version: "<v0.1>"
claim: "<这张图只支持的一句话结论>"
evidence_role: "<configuration | cost | validation | mechanism | method positioning | research design | boundary>"
data_source:
  - "<项目相对数据路径>"
source_data_sha256:
  - "<数据的64位十六进制校验值>"
sample_size: "<n、重复次数、布局数、分箱数或快照数>"
style_exemplars:
  - "<assets/figure-pattern-exemplars/choose-one-exemplar.png>"
comparison: "<对照对象、参考线和比较条件>"
encoding: "<颜色、线型、点形、柱体、色棒、误差线的含义>"
units: "<坐标轴、色棒和数值标注单位；无量纲量写 dimensionless>"
uncertainty: "<range | IQR | standard deviation | confidence interval，并写清定义>"
legend: "<图例对象、白底黑边方框、外间距和框内留白>"
panel_logic: "<单图或多面板编号及比较理由>"
boundary: "<这张图不能支持的结论>"
caption: "<图注：实验条件、视觉映射、结果和边界>"
export_status: "passed | blocked"
export_files:
  - "<图.svg 或 图.pdf>"
export_blockage_reason: "<仅 export_status=blocked 时填写>"
advisor_review: "pending"  # 可选：用户有实际确认时才更改

```
