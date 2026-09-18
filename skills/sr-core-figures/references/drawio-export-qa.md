# Draw.io export and visual QA

Use this reference before closing any SR-53 task that creates or edits `.drawio` source.

## Bundle

For a publication-oriented figure, deliver or explicitly prepare:

```text
editable source: figure.drawio
primary preview: figure.svg
optional quick preview: figure.png
optional print export: figure.pdf
achievement card: message, topology, data/encoding mapping, QA evidence, limitations
```

Do not silently omit the editable source when draw.io is the requested or selected format. If another format is explicitly requested as primary, still preserve the `.drawio` source when one exists.

## Source QA

Run:

```bash
python skills/sr-core-figures/scripts/qa_drawio.py path/to/figure.drawio
```

Fix every `ERROR`. Inspect every `WARN`; revise it unless the intended design justifies an exception and the exception is recorded. Use `--strict` for publication or reviewer-sensitive delivery.

## Visual preview

When diagrams.net/draw.io Desktop is installed, export an SVG and, when useful for inspection, a PNG. A typical command is:

```bash
draw.io --export --format svg --output exports/figure.svg path/to/figure.drawio
```

The executable may be `drawio`, `draw.io`, or a installed desktop path. If the command is unavailable, report `preview_export=blocked` with the exact missing tool; do not claim visual QA passed.

Inspect the preview at the target physical size:

- nonblank page and correct crop;
- intended reading path and topology;
- labels, formulas, panel letters, legends, and numbers visible and editable in source;
- no text truncation, overlap, clipping, or pseudo-text;
- semantic glyphs and inserted vector assets render;
- connectors have no unnecessary crossings or occlusions;
- color remains readable in grayscale and color meanings stay consistent;
- exported file matches the source layout and intended evidence boundary.

If a preview fails, edit the `.drawio` source and export again. Do not repair only the bitmap.

## Trace and reference-image tasks

When the request is to redraw a raster reference:

1. Record the reference and the intended fidelity level.
2. Extract module bounding regions and reading order before drawing.
3. Rebuild labels, formulas, arrows, and abstract structure as editable draw.io elements.
4. Export a preview and compare it visually against the reference.
5. Iterate until topology, proportions, labels, and semantic objects match the accepted target; document remaining differences.

Do not embed the raster reference as the final body unless the user explicitly requests a raster-backed figure. Do not claim pixel-perfect similarity without a measured comparison or a clearly stated visual-only check.

## Close only with evidence

The closure record must distinguish:

- `source_qa`: pass / warnings-accepted / fail / not-run + reason;
- `preview_export`: pass / fail / blocked + missing dependency;
- `visual_inspection`: pass / revisions required / not-run + reason;
- `reference_comparison`: pass / partial / fail / not-applicable;
- remaining reviewer risks and human verdict.
