# User Manual Structure

Use this reference to route content into the existing ScienceResearch manual without creating duplicate chapters.

| Chapter | Content ownership | Typical evidence |
|---|---|---|
| 1 | purpose, audience, document/product status | document metadata |
| 2 | product purpose, composition, data directories | architecture and filesystem |
| 3 | installation, startup, shutdown, ports | terminal result or running page when useful |
| 4 | home workbench, navigation, responsive/accessibility behavior | desktop/mobile home screenshots |
| 5 | work-package search, filtering, detail, templates | filtered directory and detail screenshots |
| 6 | Context creation and Workflow lifecycle | context form/result and 68 Workflow screenshots |
| 7 | Week, Item, execution, Evidence, gates, completion | state-specific execution screenshots plus API/database evidence |
| 8 | Recommendation, ReportModel, author confirmation, outcome card, PPTX | report/recommendation/export screenshots and file evidence |
| 9 | Skill registration, planning, approval, manual guidance, safety | Skill page/run evidence |
| 10 | governance, project logs, health, backup, restore/import | governance and operations screenshots |
| 11 | CLI and API reference | exact current command/route list and representative response |
| 12 | SRS implementation trace and test status | trace matrix, QA report, stage-report evidence |
| 13 | common failures, causes, and recovery | error screenshot only when it visibly proves the error |
| 14 | version, backup, support, diagnostic data | operations/health evidence |
| 15 | user acceptance sequence and scope boundary | stage report and evidence-book links |

Prefer updating an existing subsection. Add a subsection only when the behavior has a distinct user goal or materially different prerequisites/error recovery.

Do not add a general “screenshots” chapter after chapter 15. Put each result image where the reader performs the action. A separate HTML evidence book may retain exhaustive step-by-step proof.
