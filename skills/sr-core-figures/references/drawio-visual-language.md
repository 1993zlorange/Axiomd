# Scientific visual language for draw.io

Use this reference when selecting topology, shapes, colors, semantic glyphs, labels, mathematics, or accessibility treatments.

## Scientific honesty first

- One core figure should defend one message. Put secondary detail in a supporting panel or caption, not in the diagram.
- Use arrows for actual sequence, data flow, or supported causal direction. Label association, hypothesis, and inferred paths as such and use a visually distinct dashed line.
- Keep sample counts, exclusions, units, seeds, model variants, and conditions attached to the branch or node they modify.
- Do not crop, truncate, or visually exaggerate a real quantitative relationship. A miniature chart glyph must encode an actual metric or a clearly defined qualitative pattern.
- If evidence is insufficient for a mechanism, use a conceptual/hypothetical label rather than a causal arrow.
- Preserve the distinction between measured data, derived result, model internals, and interpretation.

## Typography and canvas

- Use Arial, Helvetica, or another clean sans-serif fallback consistently.
- Keep labels short and editable. Use 2-5 words in process nodes; move prose to captions.
- Dense manuscript figures usually need 6-8 pt at final size; standalone schematics need 8-10 pt. Check exported output, not only the editing canvas.
- Use single/double-column targets of roughly 89/183 mm when journal output is requested.
- Use a 20 px authoring grid, consistent node sizes by semantic tier, and visible margins.
- Bold only panel labels, module headers, and the hero module.

## Restrained palette

| Role | Fill | Stroke |
|---|---|---|
| Neutral process | `#F7F9FC` | `#4D5E6E` |
| Module background | `#EEF3F8` | `#D7E1EA` |
| Primary method or signal | `#EAF2FB` | `#0F4D92` |
| Secondary signal | `#E7F3F4` | `#42949E` |
| Validation cue | `#EDF7ED` | `#4F8A4F` |
| Warning or exclusion cue | `#FAEDEC` | `#B64342` |
| Text | transparent | text `#1F2933` |

Keep one color meaning throughout the figure. Never use rainbow decoration, heavy gradients, shadows, or red/green as the only distinction. Test grayscale readability and add position, shape, dash pattern, or direct labels.

## Shape semantics

| Meaning | Shape |
|---|---|
| Process/action | rounded rectangle |
| Data/document | rectangle or document shape |
| Persistent data store | cylinder, used sparingly |
| True decision or inclusion/exclusion | diamond |
| Result/output | emphasized rectangle or callout |
| Module | light container band |
| Semantic object | grouped editable primitive glyph |

Do not vary shape randomly. Every shape change should carry meaning.

## Connectors

- Solid arrows: primary sequence or information flow.
- Dashed arrows: optional, inferred, predicted, or feedback relationships.
- Thin internal lines: relationships inside a semantic glyph.
- Keep arrowheads and stroke weights consistent.
- Use a separate text cell for a long or bent relationship label.
- Avoid crossings; change geometry before adding style or waypoints.
- Never let a route obscure text, formulas, matrix tiles, legends, or glyph parts.

## Avoid all-text diagrams

Before drawing a plain text box, ask whether the node has a visible scientific object:

- Dataset/database: cylinder or stacked cards plus small table marks.
- Quantitative result: mini axes with bars, points, line, or confidence band tied to a real metric.
- Matrix/tensor/attention table: aligned low-saturation tiles, labels outside.
- Model/network: compact layers of blocks or circles with only meaningful connections highlighted.
- Sequence: short paired motifs on two rails; highlight only the relevant motif.
- Sample/cohort: dots or simplified sample glyphs with counts nearby.
- Cell/specimen: abstract ellipse plus internal markers, not fake microscopy.
- Instrument/imaging: minimal abstract geometry unless a real image panel is required.

A glyph is useless if its parts have no scientific interpretation. If a labeled process node is clearer, keep the text node.

## Formula and label placement

- Enable `math="1"` and put equations in dedicated formula cells.
- Use `\(...\)` or `$$...$$` MathJax delimiters; keep line breaks outside math.
- Reserve whitespace around formulas because rendering can be wider than raw text.
- Define abbreviations once in a legend or caption, not repeatedly in every node.
- Use lowercase bold panel letters near panel boundaries.
- Keep legends compact and frameless; direct labels are usually clearer.
