# 已吸收的工程方法

2026-10-22 核对以下当前可访问的主分支内容，改写为本目录的工程流程，普通使用无需调用它们。

- 故障诊断：先复现和定位来源，再用最小改变验证原因；来源为 https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md 。
- 最终检查：从原始要求审查完整改动，按行为影响选择检查强度；来源为 https://github.com/openai/openai-agents-python/blob/main/.agents/skills/implementation-final-review/SKILL.md 。

2026-10-23 继续核对：

- [行为测试方法](https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/test-driven-development/SKILL.md)：修复时先复现失败，检查测试确实能识别问题，再实施最小修正。
- [运行行为探查](https://github.com/openai/openai-agents-python/blob/main/.agents/skills/runtime-behavior-probe/SKILL.md)：不能仅由静态代码推断实际行为，使用有限场景记录输入与观察结果。未采用其必须点名和每次重复审批要求。
- [代码评审](https://github.com/anthropics/knowledge-work-plugins/blob/main/engineering/skills/code-review/SKILL.md)：核对正确性、错误处理、性能与安全；报告具体可行动的问题。

以上通用方法已包含在本目录的工程流程中。不照搬其他仓库的专用工具、审批记录或固定评审人数，不在运行时转调来源技能。
