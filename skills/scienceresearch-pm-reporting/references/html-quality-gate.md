# HTML Deliverable Quality Gate

Use this reference before handing off either report.

## Content

- The report date, repository, SRS/SDD/ARCH version/status, QA run, and evidence scope are visible.
- The project-stage report leads with an outcome, distinguishes technical validation from customer acceptance, and directly contains the complete requirements journey evidence chapter.
- The report table of contents and primary evidence action link to the integrated journey chapter, not only to the compatibility file.
- The compatibility evidence book mirrors/extracts the integrated journey evidence and prominently links back to the report journey anchor.
- Every currently operable in-scope journey is in the authoritative report; non-operable or unverified requirements are explicit.
- Every screenshot caption states the action/result it proves; archived screenshots include their source run.
- Risks, unresolved customer decisions, and next actions have owners or state that an owner is unknown.

## Files and links

- Resolve links relative to the HTML file's directory. An HTML file under `output/` normally references `output/playwright/...` as `playwright/...`, not `output/playwright/...`.
- Check that every `img src` and local `href` exists.
- Validate image signatures or open the images; do not rename YAML/text evidence to `.png`.
- Keep trace, API, database, and report paths selectable as text even when the browser cannot open them directly.
- Cross-link the project-stage report, evidence book, and user manual.
- Verify cross-file fragments such as `YYYYMMDD-内容简述-项目阶段汇报.html#journeys`, not just target-file existence.
- Confirm that no material screenshot, actual result, state evidence, failure label, limitation, or baseline caveat exists only in the compatibility evidence book.

## Browser checks

Open the HTML in a real browser and check at least:

- desktop: approximately 1440×900;
- intermediate: approximately 900×900;
- mobile: approximately 390×844.

At each width check page width, image scaling, table/diagram overflow, navigation, anchor jumps, readable captions, and visible focus. Report `ConsoleError` and `PageError`; do not hide unrelated errors.

If report images use lazy loading, scroll through every journey group, wait for image completion, and require `pending=0` and `broken=0`. Report Console Error, Warning, and PageError counts separately.

## Safety and cleanup

- Use a dedicated `output/pm-chain-<YYYYMMDD>/data/` database for demonstration flows.
- Stop the temporary application server and close the browser session after validation.
- Do not delete existing evidence, logs, customer-authored text, or historical defect records.
- Do not expose absolute machine-specific paths inside the HTML except in a clearly labeled local-run appendix when useful; prefer repository-relative evidence paths.
