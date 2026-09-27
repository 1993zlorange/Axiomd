# Logic diagram style for SR-58

Use this reference for flowcharts, mechanism maps, architecture diagrams, case loops, and other visual arguments. A logic diagram is not decoration; it must make the reasoning easier to review.

## Core rules

1. **One diagram, one question.** A diagram answers one of: what happened, how it runs, why it works, who checks it, or what is blocked.
2. **Node text is a phrase.** Use 4–10 Chinese characters where possible. Put explanations outside the node.
3. **Number the order.** Use ①②③ or 1. 2. 3. consistently across diagram, title, and speaker notes.
4. **Keep one main path.** The eye should follow one left-to-right or top-to-bottom route without backtracking.
5. **Make human gates explicit.** `GATE F`, `GATE E`, and `GATE D` are distinct decision shapes, not ordinary steps.
6. **Explain loops.** Failure, rework, evidence supplement, and method rollback use dashed arrows with a short reason.
7. **Use color semantically.** Color identifies meaning; it is not a palette decoration.

## Node and arrow semantics

| Element | Style |
|---|---|
| Ordinary node | white or very light fill, black text, neutral stroke |
| Method/core mechanism node | light blue fill, blue stroke, blue bold text |
| Human gate / key decision | white fill, red stroke, red bold text |
| Critical result / blocker | red emphasis, used sparingly |
| Main path | dark neutral or deep-blue solid arrow |
| Method/data stream | blue solid arrow |
| Failure/rework loop | red dashed arrow |
| Hypothetical/optional path | black dashed arrow |
| Evidence/archive relation | black solid thin arrow |

Do not use rainbow fills, gradients, shadows, or color-only distinctions. Shape, label, position, and dash pattern must also carry meaning.

## Mechanism map

Use for a general method transformed into a local design.

```text
left column: source mechanism
center: numbered correspondence
right column: local implementation
bottom: hard rule / boundary
```

Rules:

- 3–5 comparison rows.
- Correspondence arrows point from source to local implementation.
- Do not draw a time axis.
- Highlight the row that carries the page's main claim.

## Three-stage process

Use for a nonlinear workflow.

```text
探索 → 执行 → 表达
```

Rules:

- Show the three stages first.
- Place at most four workflows under each stage on the overview.
- Put detailed role actions on a continuation page.
- Draw human gates between stages.
- Rework loops return to a named stage or gate, not to an unspecified edge.

## Architecture diagram

Use for layers and boundaries.

```text
core research layer
↓ structured request / curated return
support layer
↓ achievement cards / handoff records
evidence and memory layer
```

Rules:

- Components remain inside their semantic layer.
- Arrows show request/result or evidence direction.
- Do not imply chronology.
- Keep external systems, human decisions, and storage visually distinct.

## Four-quadrant mechanism

Use for four supporting mechanisms.

```text
① project governance      ② decoupled cards
③ extensible engineering  ④ reflection loop
```

Rules:

- Each quadrant has a 4–8 character title and at most three short lines.
- Use the same node size and internal alignment.
- Highlight only the changed mechanism, number, or risk.
- Do not turn the quadrants into four paragraphs.

## Case loop

Use for one practice example:

```text
input → action / workflow → observable output → boundary
```

Rules:

- Label the actual SR workflow when known.
- Negative cases state the failure or non-claim.
- Do not use an arrow to imply validation when the case was only exploratory.

## Diagram QA

- [ ] The diagram answers one question.
- [ ] Node labels are short and editable.
- [ ] Numbering matches the page structure.
- [ ] Main path is visually dominant.
- [ ] Gates and loops are explicit.
- [ ] No connector crosses text or node bodies.
- [ ] Color meanings are consistent across the deck.
- [ ] Text inside the diagram is at least 14pt at final size.
- [ ] A reviewer can explain the diagram after one reading.
