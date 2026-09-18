# Document-to-PPT conversion for SR-58

Use this when a manuscript, README, achievement card, experiment record, review report, or release note must become an academic/group-meeting deck.

## Input gate

Read the named source document and, when SR workflow context exists, the linked evidence and shared research contract. Before writing slides, build a claim map:

| Source claim | Type | Evidence path | Slide use | Summary sentence | Risk if overstated |
|---|---|---|---|---|
|  | result / method / setup / limitation / decision |  | title / summary / bullet / figure / notes |  |  |

Rules:

- Do not turn a plan into a result.
- Do not turn “ran once” into “validated”, or “demo worked locally” into “reproducible”.
- Do not show a metric without units, baseline, dataset/split, condition, and version when those facts affect interpretation.
- Keep private paths, credentials, unpublished collaborator data, and unapproved release material out of slides.
- Put detailed caveats and citations in speaker notes when they would overload the page.

## Topic extraction

1. List candidate claims and group them by user question/topic.
2. Reject a group that has no evidence or does not change the audience's decision.
3. For each kept group, write a 4–8 character phrase. Prefer parallel forms:
   - `问题定义 / 方法设计 / 结果验证 / 资源分析`
   - `模型设置 / 数值通量 / 边界条件`
4. Order groups by the audience's decision path, not the source document's historical order.
5. Decide whether evidence belongs on the slide, in a backup slide, or only in speaker notes.
6. For each surviving page, compress its decision into one complete summary sentence in `SR58-SUMMARY`; do not proceed with a page whose summary cannot be stated in one evidence-bounded sentence.

## Page decision rules

- If a paragraph contains one conclusion plus detail, make the conclusion the title and move detail to numbered bullets or notes.
- If a section contains multiple conclusions, split it into pages.
- If a section is only background, compress it to one context line or move it to appendix.
- If a method and result are mixed, split them on result pages; result pages lead with the result.
- If a table has more than one decisive fact, consider one page per comparison or highlight only the decisive row/column.
- If a repeated module differs in only number/condition/status, reuse the layout and highlight that difference.
- If a page needs two summary sentences, split it; each page may have exactly one `SR58-SUMMARY`.

## Template adaptation

1. Copy the user PPTX to a private build/output directory.
2. Inspect all layouts likely to be used; record layout names.
3. Map page roles to actual template layouts, for example:
   - cover -> title layout;
   - agenda -> title/content or custom agenda layout;
   - method -> content/figure layout;
   - comparison -> comparison/two-column layout;
   - result image -> picture/title layout;
   - backup -> blank/only-title layout.
4. Fill placeholders. Keep master decorations, logos, footer, page number, and margins. Put each page's full conclusion sentence into a visible text shape named `SR58-SUMMARY`.
5. If the template lacks a needed semantic style, add explicit run formatting; do not change global theme colors silently.
6. Export to a new file. Preserve the user's original deck unchanged.

## Output contract

Deliver or prepare:

```text
editable deck: YYYYMMDD-内容简述-学术汇报.pptx
page plan: YYYYMMDD-内容简述-PPT页计划.md
speaker notes: embedded in PPT or a separate讲稿 file
acceptance card: SR-58 achievement card with evidence and human verdict
QA: script result + rendered-slide inspection + template fidelity note
```

The page plan must satisfy the per-slide YAML contract in `group-meeting-ppt-standard.md`. A deck without a traceable page plan and evidence map is not closed.

## Failure handling

- Missing source evidence: keep the slide as `待定` or remove the claim.
- Missing template: ask for it when the user required one.
- Presentation tool cannot preserve PPTX masters/layouts: produce content/page plan and record the tool blocker; do not paste a screenshot into a new deck and call it template-based.
- Render unavailable: run source QA if possible and mark `visual_qa=blocked`.
- Human has not rehearsed/approved public release: status remains draft; release actions need explicit authorization.
