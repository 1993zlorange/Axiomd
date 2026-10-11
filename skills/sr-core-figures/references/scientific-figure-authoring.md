# Scientific figure authoring

Use this reference whenever SR-53 creates or revises a data chart, publication figure, advisor-report figure, or evidence visualization. For editable mechanism/workflow diagrams, also read [drawio-authoring.md](drawio-authoring.md).

## Scientific evidence comes before style

A figure is a visual argument. Before coding or drawing, complete this figure brief:

| Field | Requirement |
|---|---|
| claim | One sentence and one evidence chain; do not mix multiple objectives |
| evidence role | Configuration, cost, validation, mechanism, method positioning, research design, or boundary |
| data source | Every point, line, bar, color, statistic, and reference line is traceable |
| sample size | Report n, repeats, layouts, bins, or snapshots where relevant |
| comparison | Name the baseline/reference and the condition being compared |
| encoding | Define color, line style, marker shape, bar, colorbar, and error-bar meanings |
| units | Axes, colorbars, and numeric annotations have units; dimensionless values say so |
| uncertainty | State whether bars are range, IQR, standard deviation, or confidence interval |
| boundary | State what the figure cannot support |
| caption | Put the full explanation in the manuscript/report caption, not inside the figure |

A chart that only shows a summary is usually incomplete. Prefer raw observations plus a transparent summary.

## Figure archetypes

| Claim/evidence | Preferred expression |
|---|---|
| Cost or runtime | Bars for means + raw repeated points + range/error definition + n |
| Accuracy across conditions | Absolute values plus signed differences or paired relationships |
| Agreement between methods | Truth-vs-prediction scatter with identity line + separate signed residual panel |
| Error structure | Raw points, median, mean, IQR/range, and bin definitions |
| Parameter coverage | 2D parameter space with marker shapes and known/interpolated status |
| Field distribution | Field map with physical quantity, units, colorbar range, and region markers |
| Stability over time | Time curve with clear axis units, comparison baseline, and growth annotation |
| Method positioning | Evidence-status matrix or map; do not invent a performance ranking |
| Research design | Existing evidence and planned data in visually separate states |

Use one archetype per figure. A secondary panel is allowed only when it directly clarifies the primary comparison.

## Data invariants

Before and after every visual revision:

1. Do not change raw data, delete unfavorable points, or alter derived metrics.
2. Preserve point count, sample size, repeat count, and numeric values.
3. Do not add thresholds, significance, or superiority claims that were not defined before viewing results.
4. Do not promote a candidate mechanism to a verified mechanism.
5. Do not turn a plan into a completed result.
6. Record the source-data hash when the figure is revised.
7. Version the figure and report; never overwrite an accepted prior version.

If the display range must expand to make room for a legend or annotation, do not move or remove data; record the reason.

## Visual grammar

### Layout

- Use a four-sided frame for data-analysis plots.
- Put a short, centered title above the frame.
- Use light gridlines when readers need to estimate numeric values.
- Keep the main reading path left-to-right or top-to-bottom.
- Use bold lowercase panel letters such as `(a)`, `(b)`, `(c)` under or beside panels.
- Use multi-panel figures only for direct comparison under the same logic; otherwise split them.

### Text and fonts

- Use English inside generated figures unless the user explicitly requests another language.
- Translate internal code/task names into reader-facing object names.
- Use Arial, Helvetica, Nimbus Sans, or DejaVu Sans consistently.
- Put long explanation in the caption; keep the figure title and labels short.
- Figure text must not cover data, axes, legends, colorbars, panel letters, or annotations.

### Color semantics

Use a restrained palette:

| Color | Meaning |
|---|---|
| red | high fidelity, reference line, key marker, proposed method, or key result |
| black | primary data, comparison, text |
| blue | boundary, intermediate fidelity, or secondary comparison |
| gray | structure, weak emphasis, or baseline |
| light gray/blue | backgrounds or weak bars |
| cividis | continuous fields when perceptual accessibility matters |

Rules:

- Keep one color meaning throughout the figure set.
- Do not use rainbow palettes.
- Never let color be the only encoding; combine it with line style, marker shape, direct labels, or position.
- Continuous fields require a colorbar with quantity, units, and range strategy.
- If snapshots use different scales, explain why and show each range.

## Legend rules

Add an in-figure legend whenever a figure has:

- multiple curves;
- multiple classes or marker shapes;
- multiple line styles;
- bars plus points or error bars;
- median, mean, IQR, or range in one plot;
- identity, zero, or threshold reference lines;
- discrete classes in addition to a colorbar.

advisor-report boxed-legend style boxed legend:

```text
white background
black solid border
placed in a corner or clearly empty region
outer clearance to axes/data: at least about 1x legend font size
inner padding: about 0.85x legend font size
sample-to-text gap: about 0.70x legend font size
row spacing: about 0.45x legend font size
```

Audit method:

1. Render the final figure.
2. Expand a protection band one legend-font-size outside the legend.
3. Hide the legend and re-render.
4. Check whether non-background pixels enter the protection band; light grids may be ignored.
5. If needed, move the legend or expand the display range—never move or delete data.

A single unambiguous series may omit a legend, but the caption must define it.

## Multi-panel rules

Keep panels together only when they:

- compare the same object under different conditions;
- show absolute and signed-difference views of the same comparison;
- show truth-prediction agreement and its residual;
- show successive snapshots of the same field;
- form one method/framework evidence chain.

Split panels when they:

- have different data types, units, or sample sizes without a shared comparison;
- merely avoid creating another file;
- make one panel's visual scale compress another panel's differences;
- contain unrelated claims.

Use a shared axis and encoding when panels are intended for direct comparison.

## Reproducible implementation

Prefer a script plus source data over a hand-edited bitmap.

For Python/Matplotlib-style charts:

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "axes.linewidth": 0.8,
    "axes.grid": True,
    "grid.color": "#D9D9D9",
    "grid.linewidth": 0.5,
})

fig, axes = plt.subplots(
    ncols=2,
    figsize=(7.0, 3.1),
    constrained_layout=True,
)
axes[0].set_title("Cost per solve", fontsize=9)
axes[0].set_xlabel("Grid level", fontsize=8)
axes[0].set_ylabel("Wall time (s)", fontsize=8)
axes[0].errorbar(
    [0, 1], [4.21, 0.599],
    yerr=[[0.624, 0.049], [0.624, 0.049]],
    fmt="none",
    ecolor="#B71C1C",
    capsize=2.5,
    label="Range (n=2)",
)
axes[0].scatter([0, 0, 1, 1], [3.58, 4.83, 0.648, 0.550], color="black", label="Raw run")
axes[0].legend(
    frameon=True,
    facecolor="white",
    edgecolor="black",
    framealpha=1.0,
    borderpad=0.6,
    labelspacing=0.45,
    handletextpad=0.7,
    fontsize=7,
)
fig.savefig("figure.svg", bbox_inches="tight")
fig.savefig("figure.pdf", bbox_inches="tight")
```

Keep the script, source data, and exports versioned together. Export SVG or PDF for publication and PNG only for quick preview. Do not hand-edit the exported bitmap and call it reproducible.

## QA

Run the chart-brief check after filling [../assets/figure-contract-template.md](../assets/figure-contract-template.md):

```bash
python skills/sr-core-figures/scripts/qa_scientific_figure.py figure-contract.md --figure figure.svg
```

If export is genuinely blocked, set `export_status: blocked`, explain `export_blockage_reason`, and still check the data/encoding contract.

Check:

- claim and evidence role are explicit;
- data hash and point/sample counts are unchanged;
- axes, colorbars, and annotations have units;
- uncertainty is defined;
- legend covers every ambiguous encoding and has adequate clearance;
- multi-panel structure has a comparison reason;
- figure text is readable and does not overlap data;
- color survives grayscale and is not the only encoding;
- exports are nonblank and versioned;
- the caption states conditions, encoding, result, and boundary.

Automatic QA cannot judge scientific truth or fully replace human visual comfort. A final advisor/user review is required for report figures.
