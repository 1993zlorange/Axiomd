# Academic/group-meeting PPT standard for SR-58

Use this contract when SR-58 prepares slides, converts a document into a talk, or adapts a user-supplied PPTX template. The slide deck is a communication artifact. It never creates evidence, replaces the achievement card, or authorizes release.

## Template-first workflow

When the user supplies a PPTX, treat it as the visual template unless they say otherwise:

1. Work on a copy; never overwrite the source deck.
2. Inspect slide dimensions, masters, layouts, placeholders, theme, fonts, logos, footers, dates, page numbers, margins, and repeated decoration.
3. Choose the closest existing layout for each page; fill or edit existing placeholders instead of covering the template with a new design.
4. Preserve required template elements and remove only unused placeholders/source text that must be replaced.
5. Check every changed slide against the template after rendering. If a tool loses masters, layouts, logos, footer, or fonts, repair the deck or state `template_fidelity=partial/blocked`.

If no template is supplied and the user asked for “按模板”, ask for the template. If a neutral deck is explicitly acceptable, state that choice in the work contract.

The supplied template observed for this standard is 16:9 and has separate title/content, comparison, section, picture, and blank layouts. Do not hard-code private cover text or figures; reuse only the structural pattern.

## Template conflicts

The user’s explicit font-size and red/blue/black contract overrides inherited template styles for content text. Keep the template’s dimensions, layout geometry, decoration, footer, logo, and margins, but write explicit Microsoft YaHei, bold title, size, color, bold, and underline properties on affected runs. If inspecting the supplied template itself reports legacy violations, record them as a template baseline and correct the generated deliverable rather than copying the violations.

## One-sentence summary contract

Every page must contain exactly one visible, complete summary sentence, separate from short labels, section names, bullets, and the page title. The uploaded reference follows this pattern: a section/page title remains scannable, while a bold 20–22pt Microsoft YaHei sentence states what the page proves, establishes, or requires.

Write the sentence as an assertion, not a topic label:

- Result: `在<条件/基线>下，<对象/方法>实现<量化结果>，支持<边界内结论>。`
- Method/setup: `通过<方法/设置>建立<对象>，解决<问题>并支撑<后续验证>。`
- Risk/blocker: `<证据>表明<未完成/风险>，需要<决定/资源>。`
- Agenda: `按<主线>依次说明<主题一>、<主题二>和<下一步>。`
- Cover: `本汇报说明<问题>、<方法>和<主要结果>。`
- Backup: `本页用<证据>支撑第<N>页的<结论>。`

Rules:

1. Put the sentence in a visible text shape named `SR58-SUMMARY` so source QA can locate it.
2. Use one complete sentence ending with `。`（or the equivalent in the delivery language）; do not split it into bullet fragments.
3. Prefer 20–22pt bold Microsoft YaHei; never go below the 18pt body minimum.
4. Use blue + bold for a normal important summary. Use red + bold + underline only when it is the page's single decisive claim and the page still has no more than three red items.
5. Keep it evidence-bounded. A summary cannot claim more than the mapped source evidence.
6. Target 20–60 Chinese characters and hard-limit at 80; if the claim needs more, split the page.
7. If a page seems to need two summaries, it contains two page claims and must be split.

`SR58-SUMMARY` is a machine-readable shape name, not visible content. Preserve the template's position/placeholder where possible; otherwise add a compact conclusion strip under the title.

## Page architecture

Adapt this order to the template and audience. Every listed page, including cover, agenda, and backup, still obeys the one-sentence summary contract:

1. Cover: topic, speaker, affiliation, date.
2. Key conclusion: “完成了 XX ｜ 用 XX 方法 ｜ 实现了 XX”.
3. Review or baseline: promise/question, prior state, evidence gap.
4. Agenda: three to five numbered 4–8 character topics.
5. Method or model setup: concise numbered points; figure subordinate.
6. Results/evidence: result is the subject; method recedes.
7. Comparison or ablation: same format with changed numbers/conditions highlighted.
8. Demo/reproducibility: runnable entry, environment, license boundary.
9. Conclusion and next action.
10. Appendix/backup: detailed proof only if needed.

Avoid consecutive same-layout, same-density pages. Change layout or split content to create a memory point on the most important page.

## Typography

- Use Microsoft YaHei for Latin and East Asian text; write explicit run fonts rather than relying on a theme that may not travel.
- Bold every title.
- Body text minimum: 18pt.
- Figure/table internal labels minimum: 14pt.
- If text does not fit, split the page or delete supporting content; never reduce below these minima.
- Respect template margins; do not place content flush against edges. A useful guard is at least one 24pt Chinese-character margin.
- Keep equations and physical quantities visually readable; do not use italics for ordinary Chinese emphasis.

## Color semantics

Use only red, blue, and black for semantic text emphasis.

| Level | Style | Use for |
|---|---|---|
| Critical | red + bold + underline | conclusion, key contribution, decisive metric, urgent risk/decision |
| Important | blue + bold | condensed takeaway, important result, method used at an achievement/result stage |
| Normal | black; keywords may be bold | physical quantities, formula explanation, ordinary result, input/output |
| De-emphasized | black regular; preferably delete | verbs, adjectives, symbol explanations, modifiers |

Rules:

- Maximum three red items per page.
- Red is for scarce, decisive meaning—not decoration.
- On a result page, methods recede to black/background while the result remains the subject.
- Within results, classify facts again as normal / important / critical.
- Preserve non-semantic template decoration, but do not add a fourth semantic color.

## Text transformation

1. **Group by topic**: split unrelated source paragraphs; do not force them into one list.
2. **Extract the skeleton**: create a 4–8 character mini-title per topic; prefer equal length and parallel grammar.
3. **Conclusion first**: every page title must say what was completed, proved, decided, or blocked.
4. **Summary sentence**: every page has one visible `SR58-SUMMARY` sentence that turns the title and evidence into a complete claim.
5. **Make order visible**: use ①②③ or 1. 2. 3.; distinguish sequence from parallel facts.
6. **Delete or demote**: remove modifiers, duplicated background, long symbol explanations, and unsupported claims.

## Figures, logic diagrams, and tables

- Method page: the text skeleton is primary; a small figure can support it. Inside the figure use “large title + small explanation”.
- Logic diagram: encode flow with color + number + arrow; do not put paragraphs inside nodes.
- Experimental/result figure: title, axes, units, legend, baseline, condition, version, colorbar physical quantity, and range must be readable.
- Table: bold title and headers.
  - Red: decisive row/column/value or blocking state.
  - Blue: important row/column/value or accepted result.
  - Black: ordinary values and context.
- Repeated modules must share geometry, wording pattern, and ordering, but highlight the changed number, condition, seed, dataset, version, status, or owner.

## Required per-page plan

Before building the deck, produce a page plan. For every slide record the optimized title, evidence, hierarchy/style, visual, deletion/demotion list, and red count:

```yaml
slide:
  no: 1
  template_layout: ""
  title: "完成了 XX ｜ 用 XX 方法 ｜ 实现了 XX"
  summary_sentence: "在<条件>下，<对象/方法>实现<结果>，支持<结论边界>。"
  summary_style: "blue-bold | red-bold-underline"
  summary_shape: "SR58-SUMMARY"
  purpose: ""
  evidence: []
  bullets:
    - text: ""
      level: "critical | important | normal | de-emphasized"
      style: "红色+加粗+下划线 | 蓝色+加粗 | 黑色关键词可加粗 | 黑色常规"
  visual: ""
  repeated_module_difference: ""
  deletion:
    - text: ""
      action: "delete | demote | speaker-notes"
      reason: ""
  red_count: 0
```

The build is blocked until every page has a conclusion-style title, exactly one evidence-bounded summary sentence, evidence mapping, level/style tags, visual decision, deletion/demotion list, and red-count check.

## QA and handoff

When Python is available, run:

```bash
python skills/sr-talk-open-source/scripts/qa_group_meeting_pptx.py path/to/deck.pptx
```

Fix all `ERROR` values. Inspect every `WARN`; use `--strict` for delivery when warnings must block. The script checks explicit fonts, minimum sizes, title bolding, red style/count, blue bolding, and text density, but it cannot inspect text rasterized inside PNG/JPEG or verify semantic correctness.

Also render/inspect the deck for template fidelity, image readability, margins, repeated-module differences, overflow, and citation/evidence consistency. If the presentation tool renames, merges, or drops the `SR58-SUMMARY` shape, restore it before QA. If this cannot be restored, record `summary_sentence_qa=blocked` and keep the deck in draft. If rendering is unavailable, record `visual_qa=blocked`; do not claim template fidelity.

Self-check:

- [ ] Each page has exactly one visible `SR58-SUMMARY` sentence and it can be stated as “完成了什么 / 证明了什么 / 决定了什么 / 卡在哪里”.
- [ ] Red/blue/black levels match meaning; red ≤3 per page.
- [ ] No body text below 18pt; no figure/table label below 14pt.
- [ ] Repeated modules highlight differences.
- [ ] Modifiers and symbol explanations are deleted or moved to notes.
- [ ] Source document, slide claim, evidence path, and speaker note agree.
