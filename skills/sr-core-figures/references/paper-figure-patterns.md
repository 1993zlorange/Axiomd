# Paper figure patterns

These are abstract structural patterns distilled from user-supplied publication figures. They are style references only. Do not copy copyrighted figures, exact artwork, or unconfirmed font/line settings into redistributable output.

## Unified framework diagram

Use for a method that connects a physical principle to multiple application classes.

```text
problem/application row
→ governing physical operator
→ numerical flux or core solver
→ time/space discretization
→ validated application examples
```

Style:

- use lanes for applications and core method;
- highlight the preserved physical principle;
- keep secondary implementation details in a lower lane;
- use arrows only for actual derivation/data flow;
- separate verified components from proposed extensions.

## Domain configuration diagram

Use for simulation setup.

```text
physical region
+ absorbing/PML/material boundary
+ excitation source and direction
+ observation boundary
+ coordinate reference
```

Style:

- color the special region and explain it in the legend/caption;
- mark excitation with an arrow and waveform label;
- state dimensions and units in the caption;
- avoid over-decorating the geometry when the claim concerns boundaries.

## Long-time stability curve

Use for stability or damping claims.

```text
x = time or periods
y = energy/amplitude/error
proposed method = solid red/reference line
baseline = visually distinct comparison
growth/failure region annotated only if measured
```

Use logarithmic scaling when dynamic range is large, and state the axis transformation. Do not annotate instability without evidence.

## Experimental comparison curve

Use for validation against measurements:

```text
line = computed result
points = experimental data
legend = method and measurement definitions
```

Keep sampling points visible. Do not let a smooth line imply denser measured data than exists.

## Field snapshot sequence

Use for wave, current, temperature, or stress evolution:

```text
(a)(b)(c)(d) = time snapshots
constant colorbar for direct comparison
time label near each panel
```

If early and late fields need different scales, use separate colorbars and explicitly state the ranges.

## Large-scale configuration

Use for extreme-scale simulation claims:

```text
object geometry
+ surrounding boundary/PML
+ incident-wave direction
+ resource/scale annotation in caption
```

The visual geometry supports setup, not correctness; correctness requires the separate evidence curve or table.

## Copyright and reference-image boundary

- Inspect a user-supplied PDF only as a style or topology reference.
- Do not embed publication artwork unless the user owns it or provides permission.
- Do not copy exact fonts, line widths, colors, or layout as confirmed standards.
- Record the reference title/path only in the local project evidence, not in a redistributable figure template.
