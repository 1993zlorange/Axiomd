---
name: sr-search-strategy
description: "SR-检索式设计与试检索：需要系统检索某一研究问题、建立可复跑检索协议、降低漏检与噪声，或把实际采集的候选文献批量导入 Zotero 时；若数据库需要登录，可在用户明确授权下复用其浏览器中的现有登录会话读取检索页面。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-07"
  aspect: "文献调研与领域结构"
  short-description: "SR-检索式设计与试检索"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-检索式设计与试检索

Use this leaf Skill when: 需要系统检索某一研究问题、建立可复跑检索协议、降低漏检与噪声，或把实际采集的候选文献批量导入 Zotero 时；若数据库需要登录，可在用户明确授权下复用其浏览器中的现有登录会话读取检索页面。

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 把问题拆为对象、任务、方法和约束词组
2. 手工扩展中英文同义词和排除词
3. 确定数据库、域名、时间范围、纳排标准、停止条件和文献导出范围，并获得检索授权
4. 优先用公开接口或本地工具试跑；需要登录时，按 [BrowserSkill 登录态文献检索参考](../sr-research-shared/references/browser-skill-literature-search.md) 复用用户现有会话
5. 在数据库页面试跑布尔检索式，观察并记录书目信息、摘要、来源 URL、时间戳、筛选器和结果计数
6. 保存查询式、来源 URL、时间戳、筛选器、结果计数和失败边界；按标识符优先级去重并查看前若干结果，调整召回与精度
7. 优先保存数据库原生 RIS/BibTeX；原生导出不可用时，仅从已核验元数据生成 Zotero 批量导入文件，并核对记录数与导出范围
8. 归还借用标签页并停止浏览器会话；登录、验证码、OTP、付费确认和下载许可由人完成

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 扩展术语、生成布尔式、比较数据库语法，并在用户授权的 BrowserSkill 会话中读取可见检索页面、整理书目信息、生成可复核证据和 Zotero 批量导入文件。

**Human intervention:** 博士生确定数据库、域名与权限范围、时间窗口、纳排标准、检索停止点、Zotero 导出范围和是否允许访问付费内容；登录、验证码、OTP、同意条款、下载或任何账户操作由人完成。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Authenticated browser retrieval (optional)

When a source requires the researcher's existing login, follow [Tencent BrowserSkill (bsk CLI + browser extension) workflow](../sr-research-shared/references/browser-skill-literature-search.md) and obtain explicit authorization immediately before contacting the external site. Use `L3` for this path. Safe operations: 复用用户已登录状态读取授权页面内容；导航、观察、填写检索词、点击筛选和分页；记录页面可见的书目信息与来源证据。

Never 读取或提取密码、Cookie、令牌、localStorage/sessionStorage、网络认证头或密码管理器内容；绕过登录、验证码、付费墙、域名限制或借用确认；将登录状态复制到文件、脚本、第三方服务或输出到成果卡。 The browser session is a capability boundary, not a source of credentials. Record only page-visible research evidence and clean up the session and any borrowed tab when finished.

登录、验证码、OTP、条款、付费确认或下载许可出现时，调用 `bsk request-help` 让用户完成，随后重新观察页面；帮助被取消、禁用或超时不得重复绕过。将认证状态记录为 `authenticated_content_observed`、`login_required`、`human_completed_login` 或 `blocked`，不要记录用户名、邮箱或令牌。

`bsk` 命令不可用、daemon 或扩展未连接时，报告阻塞原因，按参考文档的“Windows 安装与连接”章节提示用户安装，并确认“安装 BrowserSkill 后重试”或“切换到公开 API / 人工导出回退”；未经用户确认不得静默切换回退路径。

## Zotero batch import deliverable

Alongside the achievement card, produce a UTF-8 `RIS` file named `YYYYMMDD-内容简述-Zotero导入.ris`. Optional format: `BibTeX`. Export scope: 实际采集并进入候选集的记录；不得用总命中数代替导出记录数。

Read [Zotero batch import contract](../sr-research-shared/references/zotero-batch-import.md) before exporting. Prefer a database's native batch export over reconstructed metadata. Never invent missing bibliographic fields, attach restricted full text without authorization, or claim the displayed hit count as the exported record count. Record the file path, format, record count, deduplication basis, source coverage, and validation result in the achievement card.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: 检索协议：问题 / 词组 / 完整检索式 / 数据库 / 日期 / 命中 / 实际采集数 / 纳排 / 来源 URL / Zotero 导出文件 / 会话与人工处理记录

Recommended optional adapters: `nature-academic-search`, `nature-literature-pipeline`, `academic-research-skills/deep-research`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

协议可重复执行，试检索能覆盖已知核心文献，噪声来源和限制已记录；Zotero 导出只包含实际采集且可追踪的候选记录，记录数与声明范围一致，并通过格式结构检查；若使用登录数据库，必须记录授权范围、来源 URL、检索时间、查询与结果证据，且不保存或输出任何凭据、Cookie、令牌或账户身份。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-literature-screening`, `$sr-weekly-literature-update`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
