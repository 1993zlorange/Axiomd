# Draw.io scientific authoring

Use this reference whenever SR-53 must create or revise an editable diagrams.net/draw.io figure, including a method workflow, technical route, mechanism schematic, model architecture, cohort flow, or graphical abstract. A draw.io file is a source artifact, not a screenshot substitute.

## Author from a contract, not a template

Before writing XML, record a compact diagram contract in the working notes or achievement card:

```yaml
drawio_contract:
  scientific_message: ""
  archetype: "experimental workflow | computational pipeline | cohort flow | method architecture | mechanism schematic | graphical abstract | hybrid panel"
  audience_and_size: "slide | manuscript single column | manuscript double column"
  topology:
    nodes: []
    groups: []
    edges: []
    branches: []
    loops: []
  layout:
    reading_direction: "left-to-right | top-to-bottom"
    grid_unit: 20
    major_gutters: 40
    protected_zones: []
  visual_vocabulary:
    shapes: ""
    colors: ""
    semantic_glyphs: []
  mathematics:
    required: false
    formulas: []
  export:
    source: "*.drawio"
    preview: "svg by default; png/pdf only when requested or required"
    qa: "source QA + visual preview"
```

If the user gives only a topic, state a provisional message and topology in the response rather than hiding the assumption in a polished figure.

## Choose one dominant archetype

| Archetype | Use when | Layout signal |
|---|---|---|
| Experimental workflow | treatments, assays, specimens, or measurement order drive the claim | ordered protocol lanes |
| Computational pipeline | data move through preprocessing, models, statistics, and outputs | left-to-right data flow |
| Cohort or study flow | inclusion, exclusion, grouping, or follow-up counts matter | staged funnel with counts attached to branches |
| Method architecture | component relationships matter more than time | central hero module with input/output rails |
| Mechanism schematic | a causal or physical pathway is the argument | spatial pathway; causal language only with evidence |
| Graphical abstract | the whole paper message must be summarized | problem, approach, result |
| Hybrid panel | a schematic is one panel of a larger figure | one dominant schematic plus compact support |

Let secondary structures become supporting modules. Do not compete with two reading directions.

## Engineer layout before connectors

1. List nodes and remove any node that does not change the scientific decision.
2. Assign nodes to modules and lanes; equal semantic tiers get equal sizes.
3. Place node origins on a 20 px grid and small glyph parts on a 10 px grid.
4. Reserve 40-60 px corridors between major modules and at least 24 px around text-bearing nodes.
5. Put formulas, legends, and panel labels in protected zones.
6. Only after all bounds are stable, add connectors attached to real source and target cell IDs.
7. Route directly when possible; use one explicit waypoint for an L-shaped route and two for one obstacle. More waypoints require a named obstacle.
8. Keep long edge labels in separate frameless text cells, not on the edge.

No connector may pass through a text-bearing node, formula, matrix tile, legend, panel label, or the interior of a semantic glyph unless it explains an internal mechanism.

## mxGraph XML rules

Prefer uncompressed XML for generated files:

```xml
<mxfile host="app.diagrams.net">
  <diagram id="figure-sr53" name="Figure">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" page="1" pageWidth="1169" pageHeight="827" math="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

- Give generated cells stable descriptive IDs: `node-raw-data`, `group-evaluation`, `edge-raw-data-preprocess`.
- Create vertices before edges. Every edge needs valid `source` and `target` IDs.
- Keep geometry explicit. A vertex uses `mxGeometry x/y/width/height`; an edge uses relative geometry plus waypoints only when needed.
- Escape `&`, `<`, `>`, and quotes in XML attributes. Use `html=1` and `<br>` for controlled short line breaks.
- Use `parent` nesting only when children should move with a semantic group. Use a light background container behind unrelated nodes instead of trapping them.
- Attach external arrows to a group boundary or transparent port, never to an arbitrary internal decorative primitive.
- Set `math="1"` on `mxGraphModel` when labels contain `\( ... \)`, `$$ ... $$`, superscripts, subscripts, tensor notation, or related formula syntax.
- Put long captions outside the source diagram. Keep the diagram editable and the caption in the achievement card or manuscript.

### Minimal process vertex

```xml
<mxCell id="node-preprocess" value="Preprocess" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F7F9FC;strokeColor=#4D5E6E;fontColor=#1F2933;fontFamily=Arial;fontSize=11;" vertex="1" parent="1">
  <mxGeometry x="220" y="120" width="120" height="60" as="geometry"/>
</mxCell>
```

### Minimal attached edge

```xml
<mxCell id="edge-input-preprocess" value="" style="edgeStyle=orthogonalEdgeStyle;endArrow=block;html=1;rounded=0;strokeColor=#4D5E6E;strokeWidth=1.2;" edge="1" parent="1" source="node-input" target="node-preprocess">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### Semantic glyph group

Use a parent group, a transparent connector target when necessary, and a label beside or below the glyph. Keep most glyphs to 3-12 editable primitives. Examples are mini axes for a real metric, tiled rectangles for matrices, small circles for cohorts, stacked blocks for model layers, or an ellipse plus internal marks for a cell. Do not invent data values in a chart-like glyph.

## Editing an existing file

- Make a copy before a structural edit if the user did not provide a revision baseline.
- Parse XML; do not apply broad regex substitutions.
- Preserve pages, names, unrelated cells, IDs, grouping, geometry, and user style unless the requested change requires them.
- Identify whether `<diagram>` contains XML or a compressed payload. If compressed and no reliable decoder is available, stop rather than corrupt the file.
- Report what changed and re-run QA after editing.

## Local source QA

Run from the repository or installed skill directory when Python is available:

```bash
python skills/sr-core-figures/scripts/qa_drawio.py path/to/figure.drawio
```

Interpretation:

- `ERROR`: blocking; fix before delivery.
- `WARN`: inspect and revise unless the design genuinely justifies it; record the exception.
- Add `--strict` when warnings must also block publication delivery.

Source QA does not replace visual inspection or export preview.
