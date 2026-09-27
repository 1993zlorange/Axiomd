# Document-to-PPT conversion for SR-58

Use this when a manuscript, README, achievement card, experiment record, review report, release note, or project evidence set must become an academic/group-meeting deck.

## Input gate

Read the named source document and, when SR workflow context exists, the linked evidence and shared research contract. Before writing slides, build a claim map:

| Source claim | Type | Evidence path | Slide use | Summary sentence | Cannot conclude |
|---|---|---|---|---|---|
|  | result / method / setup / limitation / decision |  | title / summary / bullet / figure / notes |  |  |

Rules:

- Do not turn a plan into a result.
- Do not turn “ran once” into “validated”, or “demo worked locally” into “reproducible”.
- Do not show a metric without units, baseline, dataset/split, condition, and version when those facts affect interpretation.
- Keep private paths, credentials, unpublished collaborator data, and unapproved release material out of slides.
- Put detailed caveats and citations in speaker notes when they would overload the page.

## Presentation mode

Choose a mode before setting the page budget:

| Mode | Audience goal | Typical pages | Strategy |
|---|---|---:|---|
| `group-meeting-process-review` | advisor reviews process and evidence | 18–25 | artifact-first, mechanisms and practice cases can expand |
| `academic-talk` | external audience understands contribution | 12–18 | claim-first, fewer internal details |
| `quick-review` | decision or progress check | 6–12 | only decision-relevant evidence |
| `release-demo` | reproducibility/public release | 10–18 | demo, license, privacy, install, and rollback |

For a group-meeting process review, prefer this order:

```text
advisor context / last commitments
→ key conclusion
→ agenda
→ artifact evidence
→ motivation
→ mechanisms, one cognitive object per page
→ practice cases
→ reflection
→ next P0/P1
→ backup
```

Do not force this order when the user explicitly supplies another narrative.

## Evidence coverage matrix

Before deleting material “for brevity”, classify every source evidence cluster:

| Evidence cluster | Main page | Backup | Speaker note | Deleted | Reason |
|---|---:|---:|---:|---:|---|
|  |  |  |  |  |  |

A process-review deck must not silently drop:

- artifact screenshots or run records;
- achievement-card counts and versions;
- representative practice cases;
- boundaries and failed/unverified paths;
- advisor-requested actions.

If evidence is omitted, record the reason in the page plan.

## Cognitive-object extraction

1. List candidate claims and group them by user question/topic.
2. Reject a group that has no evidence or does not change the audience's decision.
3. For each kept group, assign one `cognitive_type` from [ppt-layout-system.md](ppt-layout-system.md).
4. Write a 4–8 character parallel topic label and a conclusion title.
5. Decide whether evidence belongs on the slide, in a backup slide, or only in speaker notes.
6. Compress each surviving page into one complete `SR58-SUMMARY` sentence.

Split by cognitive object before considering word count. If a page would contain role mapping and a time flow, mechanism and concrete screenshot, result and reflection, or verified output and unverified plan, split it.

## Page decision rules

- If a paragraph contains one conclusion plus detail, make the conclusion the title and move detail to numbered bullets or notes.
- If a section contains multiple conclusions, split it into pages.
- If a section is only background, compress it to one context line or move it to appendix.
- If a method and result are mixed, split them on result pages; result pages lead with the result.
- If a table has more than one decisive fact, consider one page per comparison or highlight only the decisive row/column.
- If a repeated module differs in only number/condition/status, reuse the layout and highlight that difference.
- If a page needs two summary sentences, split it; each page may have exactly one `SR58-SUMMARY`.
- If content is exploratory, unverified, or “not reported here”, move it to backup or a next-plan page unless it is the stated risk being reviewed.

## Layout and diagram planning

Read [ppt-layout-system.md](ppt-layout-system.md) before selecting layouts. Choose one of:

```text
claim | evidence-screenshot | mechanism-map | process-flow |
architecture | case | reflection
```

Read [logic-diagram-style.md](logic-diagram-style.md) before drawing any flowchart, mechanism map, architecture, or case loop. Record node count, branches, gates, and loops in the page plan.

For every page record:

```yaml
layout_pattern: ""
cognitive_type: ""
text_area_ratio: 0.45
visual_area_ratio: 0.55
split_check:
  one_cognitive_object: true
  needs_two_summaries: false
  split_recommended: false
```

## Template adaptation

1. Copy the user PPTX to a private build/output directory.
2. Inspect slide size, masters, layouts, placeholders, theme, fonts, logos, footers, dates, page numbers, margins, and repeated decoration.
3. Map page roles to actual template layouts, for example:
   - cover -> title layout;
   - agenda -> title/content or custom agenda layout;
   - method -> content/figure layout;
   - comparison -> comparison/two-column layout;
   - result image -> picture/title layout;
   - backup -> blank/only-title layout.
4. Fill placeholders. Keep master decorations, logos, footer, page number, and margins. Put each page's full conclusion sentence into a visible text shape named `SR58-SUMMARY`.
5. Use a separate kicker text shape when the template title cannot safely carry both numbering and the claim.
6. If the template lacks a needed semantic style, add explicit run formatting; do not change global theme colors silently.
7. Export to a new file. Preserve the user's original deck unchanged.

The user's explicit font-size and red/blue/black contract overrides inherited template styles for content text. Preserve layout geometry and decoration while adding explicit run formatting.

## Human revision retrospective

When a human edits an AI draft, read [human-revision-retrospective.md](human-revision-retrospective.md) and compare layout, titles, color, diagrams, evidence order, and cognitive-object splitting. Produce a retrospective record before replacing the old page plan.

Generalize conservatively:

- once: one-off preference;
- twice: candidate rule;
- three times with no conflict: stable rule.

Never store private source decks or local paths in this repository.

## Output contract

Deliver or prepare:

```text
editable deck: YYYYMMDD-内容简述-学术汇报.pptx
page plan: YYYYMMDD-内容简述-PPT页计划.md
speaker notes: embedded in PPT or a separate讲稿 file
acceptance card: SR-58 achievement card with evidence and human verdict
QA: script result + rendered-slide inspection + template fidelity note
human revision retrospective: when a human edit is supplied
```

The page plan must satisfy the per-slide YAML contract in `group-meeting-ppt-standard.md`. A deck without a traceable page plan, evidence map, and one primary cognitive object per page is not closed.

## Failure handling

- Missing source evidence: keep the slide as `待定` or remove the claim.
- Missing template: ask for it when the user required one.
- Presentation tool cannot preserve PPTX masters/layouts: produce content/page plan and record the tool blocker; do not paste a screenshot into a new deck and call it template-based.
- Render unavailable: run source QA if possible and mark `visual_qa=blocked`.
- Human has not rehearsed/approved public release: status remains draft; release actions need explicit authorization.
