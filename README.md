<div align="center">

# Axiom

**Axiom Agents：治理型 Codex 智能体与技能栈**

![Agents](https://img.shields.io/badge/agents-10-111827) ![Skills](https://img.shields.io/badge/skills-95-0ea5e9) ![Profiles](https://img.shields.io/badge/profiles-3-8b5cf6) ![License](https://img.shields.io/badge/license-MIT-2ea44f)

[一键安装](#一键安装) · [安装档案](#安装档案) · [Agent 索引](#agent-索引) · [使用方式](#使用方式) · [完整资产索引](docs/asset-index.md) · [English](README_EN.md)

</div>

---

## 项目定位

Axiom 的完整定位是 **Axiom Agents：治理型 Codex 智能体与技能栈**。Axiom 代表可依赖的公理、规则边界和可审计约束；Axiom Agents 把这层治理延伸到软件工程和科研工作流中的每个智能体与技能。

## 你能用它做什么

如果你要在 Codex 里启动软件项目或推进科研工作，可以直接安装 Axiom Agents。它会把 **10 个智能体** 和 **95 个 Skill** 安装到你的 Codex 环境中，让你不需要手动复制文件，也不用自己判断每类任务应该交给哪个角色。

安装后，你可以：

- 在软件项目中先明确目标与授权，再按风险选择需求、架构、实现及独立验收能力；
- 在科研项目中优先利用已有性能结果，按唯一已批准队列推进必要实验，并把过程记录写入同日同类型文件的独立条目；
- 选择 `ai4programming`、`ai4science` 或 `all` 档案，只安装你需要的部分；
- 在 Windows、macOS 和 Linux 上使用同一条安装流程；
- 随时校验安装结果，更新或卸载时保留时间戳备份。

Axiom Agents 只管理本仓库声明的智能体和 Skill，不会删除或覆盖你手动保留的其他 Codex 配置。

## 一键安装

要求：

- 已安装并能启动 Codex CLI / Codex Desktop；
- Python 3.11+；
- Git；
- Node.js 18+ 和 `npx` 仅在需要 `playwright` 真实浏览器验证时必需。

使用以下命令一键克隆并安装：

```bash
git clone https://github.com/1993zlorange/Axiomd.git axiom
cd axiom
python scripts/install.py --profile all
```

Windows 用户也可以使用：

```powershell
git clone https://github.com/1993zlorange/Axiomd.git axiom
cd axiom
py -3 .\scripts\install.py --profile all
# 或：
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Profile all
```

macOS / Linux 也可以使用：

```bash
./install.sh all
```

安装完成后 **重启 Codex，或开启一个新会话**，然后输入：

```text
列出当前可用的 axiom 智能体，并说明 AI4PROGRAMMING 和 AI4SCIENCE 的入口角色。
```

验证安装：

```bash
python scripts/install.py --profile all --check
python scripts/validate.py
```

安装器会写入：

```text
~/.codex/agents/pr-*.toml
~/.codex/agents/sr-*.toml
~/.codex/skills/<skill-name>/
~/.codex/.axiom-install.json
```

`CODEX_HOME` 已设置时，安装器使用该目录；也可以用 `--codex-home /path/to/codex-home` 覆盖。

## PR/SR 使用方式

直接用中文描述任务即可，不必点名技能或指定负责人。技能提供独立流程和本地模板；周报与时间线统一为科研进展整理，PPT 统一为学术演示文稿制作。功能边界、来源核对和旧入口迁移见 [PR/SR 维护说明](docs/pr-sr-maintenance.md)。

## 科研主线与同日记录

科研负责人维护一个最高优先任务和最多两个后续候选；先分析已有性能数据，再决定最必要的补充实验。每项实验对应研究要点、比较对象、指标和证据缺口。已批准矩阵内的必要修复、断点恢复、剩余单元和汇总接续执行；工具等待结束、角色交接或科学接受待确认不等于任务终止。长任务保存唯一执行者、版本身份、单元状态、有限重试和恢复入口，不能保证靠一句提示永不中断。

工程正确性、格式和恢复检查继续作为内部质量保障，默认不单独生成用户科研成果或日报条目。影响性能结论的缺陷才在相应研究结果中说明；对比保留正、零、负及失败结果，不以全部得到正结果为完成标准。

**同项目、上海记录日和规范类型，只维护一个可编辑记录文件。** 任务、Agent、阶段、目录和格式不参与拆分；事项使用稳定条目ID和证据锚点。有真实内容才建文件，原始run、输入、配置及正式报告等对象不强并成日记，导出只读。

从本仓库运行记录工具：

```text
python skills/pr-ps-00-project-supervision/scripts/ps_01_create_governance_document.py --project-root <派生项目根> --type log --summary <本条事项标题>
python skills/pr-ps-00-project-supervision/scripts/ps_01_create_governance_document.py --project-root <派生项目根> --type 日志 --summary <本条事项标题> --entry-file <真实条目.json> --write
```

第一条仅预览，不创建空文件。实际追加需真实JSON条目；同一事件/尝试及内容跨日重复提交仍引用原记录，修订使用新条目和revision_of。项目根AGENTS的record_policy_registry可指向现有功能登记中的record_policy，统一类型别名、固定名称与责任目录；软件日志绑定需求/任务，科研日志绑定研究要点及出处。

字段和边界见[工具API说明](skills/pr-ps-00-project-supervision/references/20260912-项目监理脚本工具-API说明.md)、[中文条目空白模板](skills/pr-ps-00-project-supervision/assets/20261029-项目日记录-条目模板.md)和[本轮维护说明](docs/20261029-科研主线与同日记录-变更说明.md)。本仓只分发能力、规则和模板，不保存派生项目的实际日记录；安装/更新仍须使用原安装流程，本次规则更新不自动安装全局能力。

## 安装档案

| 档案 | Agent | 核心 Skill | 可选 Skill | 适用场景 |
| --- | ---: | ---: | ---: | --- |
| `ai4programming` | 5 | 18 | 6 | 通用软件项目：需求、架构、实现、测试、发布、浏览器验证 |
| `ai4science` | 6 | 79 | 1 | 科研项目：项目监理、科研负责人、PI、方法、实验、批判评审 |
| `all`（默认） | 10 | 95 | 0 | 两个项目全集，并包含条件兼容与路由便利技能 |

选择档案：

```bash
python scripts/install.py --profile ai4programming
python scripts/install.py --profile ai4science
python scripts/install.py --profile all
```

带可选兼容技能：

```bash
python scripts/install.py --profile ai4programming --include-optional
```

从一个档案切换到另一个档案但移除旧档案独有资产：

```bash
python scripts/install.py --profile ai4science --prune
```

`--prune` 只会清理上一份 `.axiom-install.json` 记录且当前档案不再使用的 Axiom Agents 资产；用户手工修改过的旧资产默认跳过，除非显式使用 `--force`。

### `all` 档案的 7 个附加资产

两个核心档案的并集是 88 个 Skill。`all` 档案额外包含 7 个资产，用于保持全局 Agent 提示词的条件引用和入口路由完整：

- `scienceresearch-functional-qa`
- `scienceresearch-pm-reporting`
- `scienceresearch-release-management`
- `scienceresearch-repository-layout`
- `scienceresearch-user-manual`
- `pr-ps-09-daily-log-summary`
- `sr-doctoral-research`

前五个服务于 `pr-pm`、`pr-qa`、`pr-en` 中仅目标项目明确识别为 ScienceResearch 时才启用的能力；后两个分别是日志汇总和科研路由便利入口。不使用这些条件能力时，它们不会被普通软件开发或科研工作流主动触发。

## Agent 索引

### AI4PROGRAMMING

| Agent | 角色 |
| --- | --- |
| `pr-ps-00-project-supervisor` | 全局项目监理：登记需求、路径、权限、风险、质量、日志、反思与关闭 |
| `pr-pm-00-project-manager` | 需求所有者与交付协调：PRD/SRS、计划、对齐审计、发布协调 |
| `pr-ar-00-project-architect` | 架构与详细设计：边界、接口、数据、事务、迁移、质量属性与 ADR |
| `pr-en-00-engineer` | 实现负责人：按批准需求/设计实现、验证并交付 |
| `pr-qa-00-project-test` | 独立功能 QA：用户路径、回归、发布前验证与缺陷报告 |

### AI4SCIENCE

| Agent | 角色 |
| --- | --- |
| `pr-ps-00-project-supervisor` | 共享项目监理入口 |
| `sr-research-project-lead` | 科研项目负责人：证据盘点、阶段诊断、P0/P1、派单与交接验收 |
| `sr-principal-investigator` | 首席研究员：研究问题、主张边界、论文叙事、周期决定 |
| `sr-method-builder` | 方法构建者：文献、假设、数学模型、方法架构与实现契约 |
| `sr-experimenter` | 实验员：最小证伪、资源预算、数据质控、实验矩阵、分析与图表 |
| `sr-critical-reviewer` | 批判性评审员：机制反例、结果完整性、归因与投稿风险 |

每个 Agent 实际声明和引用的 Skill 见 [docs/agent-skill-map.md](docs/agent-skill-map.md)，完整描述见 [docs/asset-index.md](docs/asset-index.md)。

## 使用方式

`axiom` 安装的是全局 Agent 与 Skill，不会替你创建业务项目目录。请继续使用你的 AI4PROGRAMMING / AI4SCIENCE 项目模板作为项目根，并让模板中的 `AGENTS.md` 继续生效。

### AI4PROGRAMMING 路径

```text
pr-ps-00-project-supervisor 登记需求、范围、目标路径、权限和验收方式
  -> pr-pm-00-project-manager 形成需求理解契约 / PRD / SRS
  -> 用户确认基线
  -> pr-ar-00-project-architect 输出架构 / SDD / ADR
  -> pr-en-00-engineer 实现并运行相关测试
  -> pr-qa-00-project-test 独立验收
  -> pr-ps-00-project-supervisor 记录质量、日志、变更并关闭
```

示例请求：

```text
调用 pr-ps-00-project-supervisor 登记本次需求澄清。
项目根：E:/path/to/your/ai4programming-project。
目标：为用户管理模块形成可确认的 PRD/SRS 和验收标准。
禁止写入外部系统；完成后给出需求 ID、待确认问题和下一步。
```

### AI4SCIENCE 路径

```text
pr-ps-00-project-supervisor 登记科研操作
  -> sr-research-project-lead 只读盘点项目证据与阶段
  -> 输出唯一 P0 / 最多两个 P1 与派单建议
  -> 用户明确授权后派发 sr-principal-investigator / sr-method-builder / sr-experimenter
  -> 专业 Agent 每个叶子任务产出成果卡和交接书
  -> sr-critical-reviewer 独立批判评审
  -> sr-research-project-lead 验收交接
  -> pr-ps-00-project-supervisor 记录证据、成本、反思并关闭
```

示例请求：

```text
调用 sr-research-project-lead，只读评估 E:/path/to/your/ai4science-project。
请遍历项目成效卡、交接书、实验记录、论文材料和人工决定，
判断当前 primary stage、最后通过 Gate、证据矛盾和下一步 P0/P1。
不要修改文件，不要启动实验，不要访问付费服务。
```

## 更新、验证与卸载

更新：

```bash
cd axiom
git pull --ff-only
python scripts/install.py --profile all
```

验证：

```bash
python scripts/validate.py
python scripts/install.py --profile all --check
```

卸载：

```bash
python scripts/install.py --profile all --uninstall
```

卸载只会读取 `.axiom-install.json`，备份并移除本次安装管理的 Agent / Skill；你手工保留的其他 Codex 配置不会被删除。安装后被你修改过的资产会拒绝静默删除，需使用 `--force` 才会先备份再移除。

## Codex 插件形式

仓库包含符合插件目录约定的：

```text
plugin.json
.codex-plugin/plugin.json
.agents/plugins/marketplace.json
skills/
```

因此也可以把仓库作为本地插件 / marketplace 引入，让 Codex 使用 `skills/`。需要注意：插件清单分发的是 Skill；本仓库的 Agent TOML 仍由 `scripts/install.py` 复制到 `~/.codex/agents/`。如果要获得完整的 Agent 编排能力，推荐始终执行一键安装脚本。

## 仓库结构

```text
axiom/
├── agents/                     # 10 个 Codex Agent TOML
├── skills/                     # 95 个 Skill 目录
├── profiles/                   # 3 个安装档案
├── scripts/
│   ├── install.py              # 跨平台安装 / 校验 / 卸载
│   ├── build_inventory.py      # 重建 manifest 和资产索引
│   └── validate.py             # 仓库质量门禁
├── docs/
│   ├── agent-skill-map.md      # Agent 与 Skill 对应关系
│   └── asset-index.md          # 全量资产索引
├── tests/                      # 无第三方依赖的安装器测试
├── plugin.json                 # 便携插件清单
├── .codex-plugin/plugin.json   # Codex 兼容清单
├── .agents/plugins/marketplace.json
└── manifest.json               # 版本、档案、资产哈希
```

## 安全与边界

- 不提交秘密、真实日志、真实数据、付费凭据或私有项目证据。
- Agent 与 Skill 只提供流程约束和能力说明，不会自动获得额外权限。
- 发布、部署、外部系统写入、付费服务、数据迁移、删除、覆盖和公开发布都需要用户明确授权。
- 科研结论、资源投入、伦理 / 合规判断和论文主张保留人工检查点。
- 本仓库已移除源机器的绝对路径回退规则；目标项目应显式提供自己的编程规范或让用户确认适用基线。
- 安装器会拒绝路径穿越、符号链接资产和不匹配哈希。

## 贡献

1. Fork 并创建特性分支。
2. 修改前运行 `python scripts/validate.py`。
3. 保持 Agent / Skill 名称、目录名、frontmatter `name` 和 profile 成员一致。
4. 如改动资产，运行 `python scripts/build_inventory.py` 更新哈希和索引。
5. 运行：

   ```bash
   python scripts/validate.py
   python -m unittest discover -s tests -v
   ```

6. 提交 PR 时说明影响的档案、行为边界和验证证据。

## 许可证

[MIT License](LICENSE)。安装与分发本仓库不会授予任何第三方服务、数据、模型或商业 API 的使用权限。
