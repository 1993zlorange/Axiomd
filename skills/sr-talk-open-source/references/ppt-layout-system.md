# PPT layout system for SR-58

Use this reference before choosing a slide layout or after a page feels crowded. Layout decisions follow the page's cognitive object; word count is only a secondary signal.

## Cognitive-object-first rule

Classify each page before writing content:

| `cognitive_type` | Page answers | Do not mix with |
|---|---|---|
| `claim` | What is proved or delivered? | process detail |
| `context` | What prior commitment or condition frames this talk? | new result |
| `artifact` | What visible system/data/card proves the work? | abstract architecture |
| `mechanism` | Why does the design work? | chronological flow |
| `role` | Who owns or checks what? | step-by-step execution |
| `process` | In what order does work move? | component architecture |
| `architecture` | What layers/components contain it? | time order |
| `case` | How was it used in one real case? | a second unrelated case |
| `metric` | What number changed under what baseline? | narrative background |
| `risk` | What can fail or block a decision? | ordinary result |
| `reflection` | What should human/AI do differently? | new experimental claim |
| `decision` | What approval or choice is needed? | supporting implementation detail |
| `backup` | What evidence supports an earlier page? | a new main claim |

A slide has one primary cognitive object. If the page needs two different summaries or two competing reading paths, split it. Split by cognitive object before reducing words.

## Layout patterns

### Claim page

Use for a conclusion or stage result.

```text
kicker + conclusion title
SR58-SUMMARY
1 evidence / deliverable
2 method or mechanism
3 boundary or human verdict
```

Text can lead, but the three numbered blocks must not carry unrelated topics.

### Evidence screenshot page

Use for a platform, workbench, achievement card, code run, dataset, or deployed system.

```text
conclusion title + summary
large screenshot / interface
numbered callouts around the evidence
source, version, time, and acceptance state
```

Target areas: visual evidence 55–70%, text 25–35%. The screenshot must prove a stated claim; it is not decoration.

### Mechanism map page

Use for a design principle or method transformation.

```text
left: source/general mechanism
middle: numbered correspondence or transformation
right: local implementation
bottom: hard rule or boundary
```

Keep the comparison to 3–5 rows. Do not add a time flow to this page.

### Process flow page

Use for a workflow, pipeline, experiment loop, or approval sequence.

```text
one dominant left-to-right or top-to-bottom path
stage bands
numbered nodes
explicit GATE nodes
dashed loops for failure/rework
```

One page shows one primary path. Put detailed subflows on continuation pages with the same main kicker.

### Architecture page

Use for layers, modules, memory, or system boundaries.

```text
layer bands
component blocks inside layers
directional interfaces
key constraints on the right or bottom
```

Architecture explains containment and direction, not chronology. Keep 3–5 modules per layer.

### Case page

Use for one practice example.

```text
case kicker + specific conclusion
input / action / output
evidence or screenshot
boundary or negative lesson
```

One case per page. A second case receives its own page and a parallel title.

### Reflection page

Use for human/AI responsibility and review principles.

```text
reflection conclusion
strategic / operational / execution layers
key checkpoints or never-delegate items
```

Every principle must map to a real risk; delete slogans.

## Grid and area budget

Use a 12-column × 6-row conceptual grid on a 16:9 slide:

| Zone | Height | Content |
|---|---:|---|
| Header | 8–12% | kicker, title |
| Summary | 8–10% | `SR58-SUMMARY` |
| Body | 65–75% | diagram, screenshot, comparison, or bullets |
| Evidence/footer | 8–12% | source, version, boundary, page number |

Area guidance:

| Pattern | Text | Visual |
|---|---:|---:|
| Claim | 60% | 40% |
| Evidence screenshot | 25–35% | 65–75% |
| Mechanism map | 45% | 55% |
| Process flow | 20–30% | 70–80% |
| Architecture | 25% | 75% |
| Case | 35–45% | 55–65% |
| Reflection | 55% | 45% |

Reserve at least one 24pt Chinese-character margin. Avoid edge-flush text and screenshots.

## Density and splitting

Use this gate:

| Level | Signal | Action |
|---|---|---|
| Normal | <220 visible characters and one cognitive object | proceed |
| Watch | 220–320 characters, many spans, or a crowded diagram | record split review |
| Blocking | >320 visible characters, two cognitive objects, >12 diagram nodes, >3 branches, or two needed summaries | split |

Also split when:

- a title cannot state one conclusion;
- role mapping and process flow compete;
- an abstract mechanism and a concrete screenshot compete;
- a result and a reflection compete;
- verified output and unverified plan compete;
- a long source paragraph is being pasted instead of transformed.

Consecutive watch-density pages require a layout change, a split, or an explicit exception in the page plan.

## Title and numbering grammar

Separate the structural number from the claim:

```text
kicker: 2.2 机制2
title: 角色制衡避免单模型自我强化
```

Use stable main numbering:

```text
0 成果与结论
1 动机
2 机制
3 实践
4 反思
5 下一步
```

Use sub-numbering for the cognitive object, not merely page order:

```text
2.1 机制1｜68工作包拆解
2.2 机制2｜角色制衡
2.3 机制3｜12工作流与人工门
2.4 机制4｜双层架构与交接卡
3.1 实践1｜119卡积累
3.2 实践2｜场景需求定义
3.3 实践3｜文献检索收敛
```

Continuation pages share the main kicker and state their object:

```text
2.2 机制2｜角色制衡（1/2）
2.2 机制2｜阶段映射（2/2）
```

Do not reuse a generic title such as “实践探索” across unrelated pages. Differentiate the changed case, number, condition, or decision.

## Layout selection checklist

- [ ] One primary cognitive object is declared.
- [ ] The chosen layout pattern matches that object.
- [ ] The title is a claim, while the kicker carries numbering.
- [ ] The visual has enough area to be understood.
- [ ] Text explains rather than duplicates the visual.
- [ ] The page has exactly one summary sentence.
- [ ] No unverified content remains in a main-path page.
- [ ] Repeated modules use the same geometry and highlight the difference.

## 20260830 v8 layout patterns

Use these patterns with `assets/sr58-group-meeting-v8-style-template.pptx`.

| Pattern | Slide source | Required geometry/meaning |
|---|---|---|
| V8 cover | 1 | Blue horizontal band, centered 36pt title, speaker/unit/date block, summary below. |
| V8 rule page | 2–3 | Centered white card; only one principle per page; no decorative fill. |
| V8 last-week review | 4 | Upper block for last plan, lower block for advisor advice and evidence status. |
| V8 agenda | 5 | Centered numbered outline around x=3.3–10.3 inches. |
| V8 result summary | 6 | Centered statement block for completion, time estimate, and unresolved problem. |
| V8 method page | 7 | Left text skeleton plus right supporting figure; text is primary. |
| V8 next plan | 8 | P0/P1 cards plus a human-decision strip. |
| V8 model geometry | 10 | Left four-view region and right mesh/key-detail region; coordinates and scales mandatory. |
| V8 model settings | 11 | Four editable native tables: excitation, geometry, detail, medium/boundary. |
| V8 material parameters | 12 | Left curve area plus right data/source table. |
| V8 resource statistics | 13 | Mesh, unknown/resource, and time-step tables with units and comparable definitions. |
| V8 evidence figures | 14–16 | Labeled view/figure placeholders with coordinate, unit, legend, caption, and visualization checks. |
| V8 negative check | 17–18 | Left failure checklist and right example placeholders; never copy the original negative images. |
| V8 delivery check | 19 | Three checks plus one red no-go condition. |
