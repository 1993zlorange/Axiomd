# PR/SR 技能使用与维护

PR/SR 说明、界面提示、流程和模板采用中文。代码标识、目录名、命令、格式字段和必要专业术语保留兼容。用户可以直接描述任务，不需要点名技能或指定负责人。

每个技能按“什么时候用、先看什么、怎么做、交付什么、怎么检查”组织，并在本目录提供必要方法和模板。普通工作不再要求先建立管理记录、取得签名或转调其他技能。已有项目明确要求的记录与授权仍然有效。

## 功能边界

| 相近能力 | 如何区分 |
|---|---|
| 演示文稿、周报、时间线 | PPT 仅由 `sr-talk-open-source` 制作；周报和时间线统一由 `sr-progress-narrative` 整理，不再保留 `sr-weekly-meeting` |
| 科研图与演示文稿 | `sr-core-figures` 产出科研图及可编辑源；演示文稿使用已有图表，不另设科研绘图流程 |
| 需求澄清与需求文档 | 前者解决真实歧义，后者编写明确要求；需求已清楚时不重复访谈 |
| 网页实现与通用工程 | 前者处理界面及端到端交互，后者处理纯后端、通用代码和脚本；不重复执行整套流程 |
| 功能测试、一致性检查、交付检查 | 分别验证运行行为、比较需求与实现、汇总本次交付检查；检查结论不替代用户验收 |
| 记录、日报、复盘、方法评估 | 分别保存本次事实、汇总已有日志、分析具体问题、比较一段时间内的方法效果 |
| 差距、创新空间、最近邻 | 分别回答现有方法哪里不足、哪些维度值得探索、当前方案究竟不同在哪里 |
| 证伪、诊断、机制验证 | 分别挑战核心假设、区分已出现问题的原因、检验具体机制；不按固定顺序全部执行 |
| 资源预算、效率实验、运行调度 | 分别估计成本、测量成本、安排已有任务资源 |

保留 68 个不同研究任务的稳定编号；重叠的周组会入口已合并。当前共有 18 个 PR 技能、71 个 SR 技能及 6 个其他技能，总计 95 个技能，10 个 Agent，3 个安装配置。

## 参考方法

2026-10-22 至 23 日核对当前可访问的上游文件后，将文献核验、竞争解释、实验控制、统计单位、科学绘图、论文写作、演示文稿和工程检查的方法写入本地流程。来源是维护依据，使用技能时无需额外调用或安装。

版本与不可访问来源见 [研究方法来源](../skills/sr-research-shared/references/source-adapters.md)、[工程方法来源](../skills/pr-en-02-senior-engineer/references/related-skills.md) 和 [界面方法来源](../skills/pr-en-01-fullstack-design-engineer/references/source-review.md)。部分旧别名已失效，不能声称其最新版已核实。

## 生成与检查

修改 68 个研究任务的内容时编辑 `skills/sr-doctoral-research/catalog.json`。复杂的本地专业补充放在各技能 `references/workflow-supplement.md`，其中链接相对于该文件，生成器会转换为技能入口的相对路径。

成果模板仍由共用的基础、方面和专题模块生成；沟通说明仍由 `docs/pr-sr-interaction-standard.md` 生成。不要手工修改生成副本。

```powershell
python skills/sr-doctoral-research/scripts/generate_leaf_skills.py --repo-root .
python scripts/generate_sr_record_templates.py
python scripts/generate_pr_sr_interaction_guides.py
python scripts/build_inventory.py
python skills/sr-doctoral-research/scripts/generate_leaf_skills.py --repo-root . --check
python scripts/generate_sr_record_templates.py --check
python scripts/generate_pr_sr_interaction_guides.py --check
python skills/sr-doctoral-research/scripts/validate_sr_skills.py --repo-root .
python scripts/validate.py
python -m unittest discover -s tests -v
```

生成器默认写入当前资产包；`--check` 只读，过期返回 1。SR 校验器只读取指定资产包，不再依赖用户全局配置或旧项目目录；成功返回 0，错误返回 1。

研究记录检查器支持简明模板，并保留旧记录检查分支；简明记录不要求姓名、人工判定或管理附录，但必须有实际结果、来源或验证限制。通过返回 0，严格模式中的警告返回 1，缺少实质内容返回 2。

演示文稿检查器同时识别英文与中文页标题，保留原有字体、颜色、总结句和内容检查。科研图检查器不再要求导师确认字段；填写时仍检查合法值，不把人工确认当作结构验证。

## 安装兼容

本次修改不改安装器。已有安装可用原命令更新；需要清理已经合并的旧入口时使用安装器的 `--prune`，它按原安装记录处理并保留备份。如果旧技能被用户修改，先处理冲突，不用强制覆盖绕过保护。

```powershell
python scripts/install.py --profile all --prune
python scripts/install.py --profile all --check
```

仓库基线检查结果为 10 个 Agent、96 个技能、3 个配置通过。合并后数量变化属于预期；语言、模板与调用行为变化需结合实际使用继续观察，静态检查不能证明每次自然语言选择都完全正确。

最终验证（2026-10-23）：资产校验通过；17 项自动化测试全部通过，包含生成一致性、专题模板映射、自然语言入口、本地资源、图表/PPT 检查、临时安装卸载和旧入口备份清理。Git 差异格式检查通过。本次没有修改安装器，也未更新用户全局安装。
