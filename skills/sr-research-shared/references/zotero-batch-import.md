# Zotero 批量导入交付契约

SR-07 与 SR-08 在成果卡之外，可交付 Zotero 可批量导入的文献元数据文件。Zotero 官方支持通过 `File -> Import... -> A file` 导入 RIS、BibTeX 等标准格式；大批量数据库记录应优先使用数据库原生批量导出，而不是逐条使用 Connector。[Zotero 标准格式导入](https://www.zotero.org/support/kb/importing_standardized_formats) [Zotero 大规模数据库导入建议](https://www.zotero.org/support/adding_items_to_zotero#large-scale_imports_from_databases)

## 输出选择

- 默认输出 UTF-8 `RIS`，文件名为 `YYYYMMDD-内容简述-Zotero导入.ris`。RIS 跨数据库兼容性较好，也便于人工检查。
- 用户需要 LaTeX 工作流时，可并列输出 UTF-8 `BibTeX`，文件名为 `YYYYMMDD-内容简述-Zotero导入.bib`。
- SR-07 只导出实际采集并进入候选集的记录。页面显示的总命中数不是已导出数。
- SR-08 默认只导出博士生确认纳入的记录；排除记录保留在 PRISMA 台账，不进入默认 Zotero 文件。若用户明确要求边界样本，可另建文件并加筛选状态标签，不得与最终纳入集混写。

## 数据来源优先级

1. 优先保存数据库自身导出的 RIS 或 BibTeX，并保留数据库名、检索式、筛选条件、导出日期和导出范围。
2. 原生导出不可用时，可从 API、网页可见字段或本地台账生成，但每个字段必须能追到来源；未知字段省略，不得由题名或常识猜测。
3. DOI 统一去掉 `https://doi.org/` 前缀后存储；URL 保留完整来源链接。作者保持原有顺序，每位作者单独映射。
4. 只交付书目元数据。PDF、补充材料、快照和受限全文不随 RIS/BibTeX 自动打包，除非用户另行明确授权且许可允许。

## 去重规则

按以下优先级使用稳定标识符：DOI、PMID、arXiv ID、ISBN；均缺失时使用规范化题名 + 年份 + 第一作者。规范化只用于匹配，不覆盖原始题名。冲突记录进入人工复核，不自动合并相互矛盾的年份、作者或题名。

## RIS 最小结构

每条记录以 `TY  -` 开始，以 `ER  -` 结束，并在记录间保留空行。作者与关键词使用重复标签。至少应有可核验的类型和题名；其余字段缺失时省略。

```text
TY  - JOUR
TI  - Verified article title
AU  - Family, Given
PY  - 2026
JO  - Verified Journal
DO  - 10.xxxx/verified-doi
UR  - https://example.org/record
KW  - verified keyword
N1  - Source database: Example; screening status: included
ER  -
```

常用映射：期刊论文 `TY/JOUR`，会议论文 `TY/CPAPER`，书籍 `TY/BOOK`，书章 `TY/CHAP`；题名 `TI`，作者 `AU`，年份 `PY`，期刊 `JO`，卷期页 `VL/IS/SP/EP`，DOI `DO`，URL `UR`，摘要 `AB`，关键词 `KW`。类型无法确认时暂停复核，不随意指定。

## BibTeX 最小结构

每条记录使用与文献类型一致的条目类型；引用键必须唯一、稳定且只含 ASCII 字母、数字、连字符或下划线。保护专名大小写，转义 BibTeX 特殊字符，并保持作者顺序。

```bibtex
@article{family2026shorttitle,
  title = {Verified article title},
  author = {Family, Given},
  year = {2026},
  journal = {Verified Journal},
  doi = {10.xxxx/verified-doi},
  url = {https://example.org/record}
}
```

## 交付前检查

- 文件使用 UTF-8，扩展名与内容格式一致。
- RIS 每条记录恰有一个 `TY` 起始和一个 `ER` 结束；BibTeX 每条记录括号配对且引用键唯一。
- 导出记录数等于成果卡声明的记录数；抽查首条、末条及至少一个含 DOI 的记录。
- DOI、PMID、arXiv ID 或 ISBN 无重复；无稳定标识符的记录已按规范化组合检查。
- 标题、作者顺序、年份、来源、DOI 和筛选状态均能追到数据库导出、页面证据或筛选台账。
- 在可用的 Zotero 环境中执行一次测试导入并记录成功数、警告和字段偏差；无法实际导入时明确标为“结构检查通过，Zotero 实机导入未验证”，不得写成导入成功。

成果卡记录：导出文件相对路径、格式、范围、记录数、去重前后数量、来源数据库、生成/导出方式、结构检查结果、Zotero 实机导入结果与已知字段损失。
