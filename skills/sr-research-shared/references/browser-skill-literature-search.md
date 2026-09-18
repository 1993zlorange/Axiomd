# BrowserSkill 登录态文献检索参考

本参考把 [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill) 的 `browser-skill` 工作流适配为 SR-07 的可选运行时。它只描述如何复用用户已经在浏览器中完成的登录状态；它不授权读取、复制或导出任何认证秘密。

## Windows 安装与连接

SR-07 不把 BrowserSkill 二进制或浏览器扩展打包进可分发仓库；它通过外部 `bsk` CLI/daemon 调用。Windows 首次准备按以下顺序执行：

1. 在 PowerShell 中运行官方安装脚本：`irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex`；重新打开终端后确认 `bsk --version`。
2. 在 Codex 需要通用 BrowserSkill 指令时运行 `bsk install-skill --harness codex --json`。SR-07 自身已包含检索流程，不依赖把任何用户凭据写入 Skill 文件。
3. 安装 [Chrome 扩展](https://chromewebstore.google.com/detail/browserskill/hhcmgoofomhgciiibhipgmgkgnoenaoi) 或 [Edge 扩展](https://microsoftedge.microsoft.com/addons/detail/browserskill/emacgiaaaiojkkpkddmmdfhmokgmnikg)，在扩展弹窗中启用连接。
4. 运行 `bsk doctor --json`；必须看到 `daemon running`、`protocol compatible` 和 `extension connected` 为成功。`browsers: []` 或 `0 browsers connected` 表示还不能做真实登录态测试。
5. 在同一浏览器配置文件中由用户人工登录目标数据库；不要把用户名、密码、机构链接或验证码写入命令、日志或成果卡。

扩展安装、机构登录、验证码和 OTP 是用户浏览器动作；Agent 只能在连接成功后读取页面可见的研究内容。

## 能力与边界

- BrowserSkill 通过本地 `bsk` CLI、daemon 和浏览器扩展，在 Agent Window 中操作浏览器；新页面可用 `bsk navigate` 与 `bsk observe`，用户标签页必须先列出并显式 `bsk tab borrow`。
- “已登录”只表示页面能显示受保护的检索内容或账户允许的功能。不得把它解释成可读取密码、Cookie、令牌、认证请求头、`localStorage`/`sessionStorage` 或密码管理器数据。
- 登录、验证码、OTP、同意条款、付费确认和下载许可是人工检查点。用 `bsk request-help` 请求用户完成步骤；不得通过脚本或切换后端绕过它们。
- 访问登录数据库、借用用户标签页、读取付费内容或下载文件属于外部系统接触，按 SR 契约使用 `L3`，并在动作前取得用户对目标域名、范围和用途的明确授权。

## 推荐流程

1. 先完成 SR-07 的人工基线、数据库清单、检索式、时间范围、纳排标准和停止条件；优先选择公开 API、开放网页或本地导出作为低权限路径。
2. 检查 CLI 与扩展连接：`bsk status --json`；需要时启动 `bsk session start --json` 并保存临时 `session_id`。不要把 `BSK_HOME`、日志或诊断输出写入成果卡。
3. 新来源使用 `bsk navigate <url> --session <id>`；已有用户标签页先 `bsk tab list --scope user --session <id>`，得到用户确认后才 `bsk tab borrow <tab-id> --session <id>`。
4. 每次导航或显著 DOM 变化后重新 `bsk observe --session <id>`。只使用当前观察返回的引用；记录页面可见的标题、作者、年份、DOI、摘要、来源 URL、查询式、筛选器、时间戳和结果计数。
5. 观察到登录门、验证码、OTP、条款或付费确认时暂停，调用 `bsk request-help` 请求用户完成；用户处理后重新观察。帮助被禁用、取消或超时，不得重复请求或假设已经登录。
6. 对分页和筛选设置明确上限，尊重站点条款、速率限制和 robots/数据库许可。未知效果先观察当前状态，再决定是否重试；不要盲目刷新或并行抓取。
7. 结束时执行 `bsk tab return <tab-id> --session <id>`（如借用了标签页）和 `bsk session stop <id>`。成功与失败都要清理；若会话/标签页状态未知，先列出当前状态再处理。

## 证据记录

成果卡至少记录：

- `source`: 数据库名称、允许的域名和具体来源 URL；
- `query`: 最终检索式、数据库语法、时间范围、筛选器、排序和分页范围；
- `observed_at`: 页面观察时间和时区；
- `results`: 页面显示的命中数、导出/读取条数、去重规则与失败页；
- `auth_state`: `authenticated_content_observed`、`login_required`、`human_completed_login` 或 `blocked`，不要写账户名、邮箱或令牌；
- `evidence`: 页面可见字段、截图/导出文件的相对路径（如用户批准），以及人工处理记录；
- `cleanup`: 是否归还标签页、停止会话，以及任何未完成动作。

不要把完整 HTML、网络日志、Cookie、认证头、浏览器存储、密码字段、OTP 或下载的受限全文放进通用成果卡。必要时只保存经用户批准的书目元数据，并注明许可与访问限制。

## 失败与回退

BrowserSkill 未安装、daemon/扩展未连接、浏览器不支持、帮助被禁用或站点阻止自动化时，报告具体阻塞并切换到公开 API、人工导出 RIS/BibTeX、开放全文或手工检索。不得为了“完成命中数”绕过登录、借用确认、验证码、付费墙或站点访问限制。

## 数据库验证矩阵

以下是 2026-09-18 在本环境用测试词 `finite element` 做的公开入口/API 冒烟验证。它验证的是可达性与公开检索响应，不等同于机构登录、全文权限或 BrowserSkill 实际会话验收。

| 数据库 | 公开入口/API | 观察结果 | SR-07 路径 |
|---|---|---|---|
| Web of Science | `webofscience.com/wos/woscc/basic-search` | HTTP 200，返回入口/登录壳；未验证机构检索结果 | BrowserSkill + 用户人工完成登录后再 `observe` |
| Scopus | `scopus.com/`；`search.uri` | 根入口 HTTP 200；旧 basic-search URL 返回 404，另一搜索入口重定向 302 | 不固化旧 URL；从用户当前登录页或根入口观察实际表单 |
| arXiv | HTML 搜索与 `export.arxiv.org/api/query` | HTML/API 均返回结果；可记录标题、作者、摘要、ID 和时间 | 优先 API，网页用于补充页面证据 |
| Crossref | `api.crossref.org/works` | JSON `status=ok`，返回 `total-results` 与书目条目 | 优先 API；按 DOI 去重并保留查询参数 |
| IEEE Xplore | `ieeexplore.ieee.org/search/searchresult.jsp` | HTTP 200，但页面含反自动化脚本；未证明结果 DOM 可读 | BrowserSkill 登录态 + `observe`；遇阻回退 Crossref/OpenAlex |
| OpenAlex | `api.openalex.org/works` | JSON 返回 `meta.count` 与 works | 优先 API，适合开放元数据和 DOI 扩展 |
| PubMed | `eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` | JSON 返回 count 与 ID 列表 | 优先 E-utilities；医学/生物交叉主题补充检索 |
| Semantic Scholar | Graph API | 本次请求 HTTP 429 限流 | 限速、缓存、人工重试；不得循环轰击 |
| ACM Digital Library | `dl.acm.org/action/doSearch` | 本次请求 HTTP 403 | BrowserSkill 用户会话或人工导出；不绕过保护 |

对于工科主线，建议在机构订阅可用时追加 **Engineering Village/Compendex、Inspec**；Elsevier 将 Compendex 与 Inspec 列为 Engineering Village 的核心数据库，前者覆盖跨学科工程文献，后者覆盖物理、电气电子、计算机与控制等方向。[Engineering Village 数据库说明](https://www.elsevier.com/products/engineering-village/databases) 对土木再追加 **ASCE Library/Civil Engineering Database**；对航空航天、制造、材料、能源等垂直主题，再按课题选择 SAE Mobilus、SPIE Digital Library、ScienceDirect、SpringerLink 或 ASTM Compass。订阅型数据库的登录和全文权限必须在机构授权范围内人工确认。

## 版本与来源

实现依据：BrowserSkill `skill/SKILL.md` 与安装/连接指南，访问日期由执行者填写。安装、版本升级和扩展连接属于环境准备，不由 SR-07 自动执行；不要在可分发仓库中提交本地安装路径、真实账号信息或运行日志。
