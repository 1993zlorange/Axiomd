# Figure and Evidence Rules

Use this reference whenever the manual adds, replaces, moves, or captions a screenshot.

## Figure form

Use Markdown images followed by a visible legend:

```markdown
![工作包搜索与筛选结果](../output/pm-chain-20260830/browser/02-work-package-search.png)
图例 5-1：工作包搜索/筛选结果；展示关键词命中后的目录状态，对应 FR-002、FR-049～FR-052。
```

The legend should include only useful fields:

- chapter-scoped figure number;
- page, action, or state shown;
- the result the figure proves;
- requirement/quality IDs when traceability helps;
- source run or limitation when the figure is archived, partial, or historical.

## Evidence suitability

A screenshot is suitable only if it visibly shows the state claimed in the surrounding text. Do not:

- reuse an operations page to claim a completion-gate state;
- rename YAML, text, or API evidence to `.png`;
- use a historical failure as a current pass;
- claim persistence, idempotency, hashes, or exported-file correctness from a UI image alone;
- duplicate one generic screenshot for multiple distinct intermediate states without explaining that it is the same archived supporting view.

When a screenshot proves only UI position, say so. Pair it with the exact QA/API/database evidence that proves the final state.

## Capture and validation

- Use a real browser and an isolated data directory.
- Capture after the visible result has settled, not before submission completes.
- Prefer descriptive ordered filenames inside `output/pm-chain-<YYYYMMDD>/browser/`.
- Check the image signature as well as file existence.
- Check image scaling and caption readability in the rendered manual or downstream HTML/PDF view.
- Close the browser and temporary server after the run.
