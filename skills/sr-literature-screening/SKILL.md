---
name: sr-literature-screening
description: "SR-核心文献筛选：检索结果需要去重、初筛、全文复筛、留下可审计排除理由，或把人工确认纳入的文献批量导入 Zotero 时。Use for this specific doctoral research work package after routing; do not use as a generic end-to-end research assistant."
metadata:
  sr-id: "SR-08"
  aspect: "文献调研与领域结构"
  short-description: "SR-核心文献筛选"
---

<!-- Generated from sr-doctoral-research/catalog.json; edit the catalog, not this file. -->

# SR-核心文献筛选

Use this leaf Skill when: 检索结果需要去重、初筛、全文复筛、留下可审计排除理由，或把人工确认纳入的文献批量导入 Zotero 时

Before starting, read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md). Obtain or reconstruct the `human_baseline`, then return the work contract. Do not skip directly to a polished answer.

## Doctoral old-school workflow

1. 保存原始检索结果并按 DOI、PMID、arXiv ID、ISBN 或规范化题名组合去重
2. 按标题摘要执行初筛
3. 对边界样本阅读全文复筛
4. 记录每条排除理由和复核人
5. 冻结每条记录的唯一筛选状态，由博士生确认最终纳入集
6. 从最终纳入集优先保留数据库原生 RIS/BibTeX；必要时仅用已核验元数据生成 Zotero 批量导入文件，并核对导出记录数

The old-school pass is the researcher's unaided reading, hand calculation, sketch, inspection, or small manual check. Preserve it as an artifact or concise note so AI output can be compared against independent human judgment.

## Human–AI collaboration

**AI role:** 去重、排序、初步标注、发现边界样本，并为人工确认的纳入集生成 Zotero 批量导入文件；不作最终排除。

**Human intervention:** 博士生复核核心文献与所有边界排除，确认标准未随结果漂移，并批准进入 Zotero 导出文件的最终纳入集。

Pause at that intervention point with options, evidence, uncertainty, and a recommendation. Do not infer approval from silence.

## Zotero batch import deliverable

Alongside the achievement card, produce a UTF-8 `RIS` file named `YYYYMMDD-内容简述-Zotero导入.ris`. Optional format: `BibTeX`. Export scope: 人工确认纳入的记录；排除记录保留在 PRISMA 台账但不进入默认导出。

Read [Zotero batch import contract](../sr-research-shared/references/zotero-batch-import.md) before exporting. Prefer a database's native batch export over reconstructed metadata. Never invent missing bibliographic fields, attach restricted full text without authorization, or merge excluded records into the included set. Record the file path, format, record count, deduplication basis, source coverage, and validation result in the achievement card.

## Deliverable

Use [assets/output-template.md](assets/output-template.md) as the blank document architecture. Name the artifact `YYYYMMDD-内容简述-文档类型.扩展名`; keep the SR ID in frontmatter and keep evidence, conclusion boundaries, and human verdicts explicit.

Use this template: PRISMA 台账：记录 ID / 阶段 / 决定 / 理由 / 复核人 / 日期 / Zotero 导出状态

Recommended optional adapters: `nature-literature-pipeline`, `nature-academic-search`. Read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before using any adapter. Missing adapters are not a blocker; disclose the manual/local fallback.

## Completion gate

每条记录有唯一状态，核心文献由人核验，排除理由可追踪且标准一致；Zotero 导出默认只含人工确认纳入的记录，记录数、去重依据和来源可追踪，并通过格式结构检查。

Also require traceable evidence, an explicit conclusion boundary, and the applicable human verdict in the shared closure record. If the gate fails, return `revise`, `pause`, or `reject`; never mark the package complete because a template was filled.

## Routing after closure

Likely next Skill(s): `$sr-paper-evidence-card`, `$sr-literature-tree`. Treat these as candidates, not a forced sequence; route according to the new highest-value unknown.
