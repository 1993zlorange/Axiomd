# Advisor-report figure patterns

These patterns abstract the 2026-09-30 advisor-report boxed-legend iteration. Use them as structural references; do not copy private project data or figures.

## Model configuration

Use when the figure establishes what was simulated.

```text
geometry/domain outline
+ material or hotspot region
+ boundary arrows and labels
+ coordinate/reference dimensions
+ short centered title
```

Requirements:

- distinguish heat source, convection, insulation, and material boundaries by stable colors and direct labels;
- state the spatial dimension and representative geometry;
- avoid decorative 3D effects when a 2D cross-section explains the claim better.

## Cost evidence

Use when the claim is that a lower-fidelity run is cheaper.

```text
bars = mean cost
points = raw repeated runs
error line = predeclared range
legend = bar, point, and error definitions
caption = n and absence/presence of a cost threshold
```

A mean-only bar chart is not sufficient.

## Grid or method comparison

Use two linked panels when absolute values compress small differences:

1. absolute output for each condition;
2. signed difference relative to a named reference.

Preserve every configuration as a point. Do not jitter overlapping points unless the jitter rule is stated.

## Paired structure

Use truth/reference-versus-prediction or condition-versus-condition panels:

```text
identity line (y=x)
raw paired points
sample size
descriptive statistic without overstating significance
```

If a statistic is descriptive, label it as descriptive.

## Error-location analysis

Use binned statistics only with a domain reason:

```text
raw points
median
mean
IQR or range
per-bin n
bin definition
```

A trend in bins is a structural clue, not automatically a mechanism.

## Prediction and residual

Pair a prediction scatter with signed residuals:

```text
panel 1: truth vs prediction + identity line
panel 2: residual vs sample or condition + zero line
```

Do not hide sign by plotting absolute error unless absolute error is the estimand.

## Field snapshot

For field maps:

- state physical quantity and units;
- use a perceptually defensible colormap;
- mark design regions or interfaces;
- keep one colorbar for directly compared snapshots;
- if scales differ, show separate colorbars and explain why;
- label coordinates and, for time snapshots, the time value.

## Method positioning / research design

Separate:

```text
verified evidence
candidate mechanism
planned data
not in current scope
```

Never use proximity or size to imply a performance ranking that was not measured.

## Final advisor-report visual rules

- Figure text: English, reader-facing, no internal code IDs.
- Fonts: Arial/Helvetica/Nimbus Sans/DejaVu Sans.
- Data plots: four-sided frame, centered short title, light grid.
- Reference lines: identity, zero, and threshold lines must be defined.
- Legend: white boxed legend with black border; every line/marker/statistic defined.
- Spacing: legend must not touch axes or data; leave inner and outer breathing room.
- Multi-panel: direct comparisons only; unrelated claims split.
- Caption: outside the figure; it explains conditions, encoding, result, and boundary.
