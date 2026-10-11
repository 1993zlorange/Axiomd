# SR-58 20260830 v8 group-meeting template

This is the only bundled SR-58 group-meeting template for reports that must follow the 20260830 v8 advisor layout. It is a de-identified reconstruction: no source figures, logos, private nouns, institution names, local paths, or source slide images are copied.

## Files

- [20-slide editable template](../assets/sr58-group-meeting-v8-style-template.pptx)
- [Matching page plan](../assets/sr58-group-meeting-v8-style-template-page-plan.md)
- [Rendered contact sheet](../assets/sr58-group-meeting-v8-style-contact-sheet.png)

## V8 hard layout

1. 16:9 slide, 13.333 × 7.5 inches.
2. Full-width title occupies the top band, approximately 0–0.75 inch; use bold 28–36pt Microsoft YaHei.
3. The v8 page number is integrated into the title, such as `1.1 方法｜...`; do not draw a separate visible kicker box.
4. Put exactly one `SR58-SUMMARY` sentence immediately below the title, 20pt blue bold.
5. Main content starts around 1.35 inch and keeps at least a 24pt-character safe margin on all sides.
6. Body text is 20pt or larger. Tables, axis labels, legends, and figure captions may go down to 14pt, but never smaller.
7. Use `1. 2. 3.` numbering; do not use small-circle numerals.
8. Do not pack content to avoid splitting. If the page needs two summaries or two cognitive objects, split it.
9. Semantic text emphasis uses only red/blue/black: critical=red+bold+underline, important=blue+bold, normal=black, de-emphasized=black regular and preferably deleted.
10. Repeated model/resource modules keep the same geometry and wording, and highlight only changed values or conditions.
11. Guidance and negative-example pages are references for the author. Delete them from a real delivery unless the advisor explicitly requests them.

## Page map

| Slide | V8 source pattern | Required use |
|---:|---|---|
| 1 | Cover with blue band and centered title | Replace topic, speaker, unit placeholder, and date; no private logo. |
| 2 | General rule | One primary cognitive object; do not fill the page to show workload. |
| 3 | One-page-one-sentence and literature-first rule | Every page must be speakable in one sentence; review work states references first. |
| 4 | Last-week review | Top block records last plan; bottom block records advisor advice and actual status. |
| 5 | Centered agenda | Use numbered research sections, not source-document page order. |
| 6 | Achievement summary | State completed work, expected time, and unresolved problem in one page. |
| 7 | Method/content page | Text skeleton is primary; one supporting figure is secondary. |
| 8 | Next-report plan | Two priorities plus the decision needed from the advisor. |
| 9 | Computation-template instruction | Model settings must be complete for in-house code and commercial software. |
| 10 | Model geometry and four views | Show isometric/main/side/top views, dimensions, coordinates, mesh, and key detail. |
| 11 | Model settings four factors | Separate native tables for excitation, geometry, detail, medium, and boundary. |
| 12 | Material/frequency parameter page | Pair a curve placeholder with an editable data/source table. |
| 13 | Resource statistics | Report mesh, unknowns, time window, time step, memory, cores, and runtime. |
| 14 | Mesh and key features | Show labeled views with coordinate scales and local features. |
| 15 | Image requirements | Compare methods with units, legends, captions, and number-unit spacing. |
| 16 | ParaView/visualization requirements | Transparent background, figure title, dynamic update, physical quantity, and suitable units. |
| 17 | Negative figure case | Reject missing axes, units, view labels, physical quantity, or colorbar meaning. |
| 18 | Negative layout case | Reject edge-to-edge content; preserve a blank margin no smaller than a 24pt character. |
| 19 | Format/style contract | Demonstrate red/blue/black importance levels, result-stage sensitivity, repeated-module differences, and table color rules. |
| 20 | Delivery check | Final font/content/image/visualization/layout gate. |

## Required computational information

When a report contains a model or simulation, retain pages for:

1. geometry and four views;
2. excitation, geometry, medium, and boundary settings;
3. frequency-dependent or versioned material data;
4. mesh and unknown/resource statistics;
5. representative field/result figures with axes, units, legends, and captions.

If a real report has no simulation/model, delete pages 9–14 and 16 rather than leaving empty placeholders.

## Figure and visualization gate

Before delivery, every figure must answer:

1. physical quantity and symbol;
2. units and scale/axis range;
3. condition, method, time, and version;
4. legend meaning for every line/marker/color;
5. view name when several views are compared;
6. colorbar quantity and unit;
7. why the figure supports the page claim;
8. what the figure cannot prove.

Use a space between a number and its unit, such as `1 m` or `2 mA`. Do not use italics except formulas. Choose human-readable colorbar units, such as `2 mA` rather than `0.002 A`.

## V8 visual language

- Primary blue: `#003399`
- Reference pale blue: `#D9E2F3`
- Decisive red: `#C00000`, bold and underlined only
- Body black: `#262626`
- Neutral border: `#BFBFBF`
- Background: white

## QA

Run:

```bash
python skills/sr-talk-open-source/scripts/qa_group_meeting_pptx.py <deck.pptx> --page-plan <page-plan.md> --strict
```

Then render and inspect every page for v8 fidelity: title position, margins, model tables, units, legends, coordinate axes, and no edge-to-edge layout.
