# High-adoption reference research

Use this protocol for a concrete UI task. The purpose is calibrated design judgment, not visual cloning.

## Search from the job, not the style

Start with the screen's user and job: research workspace, evidence review, weekly planning, data-dense dashboard, approval flow, report builder, and so on. Search for products that solve a comparable job before searching for vague style terms such as `beautiful dashboard`.

Select references with different roles:

- one information-architecture reference;
- one interaction and state-feedback reference;
- one visual hierarchy or typography reference;
- one domain-specific reference when available;
- one accessibility or dense-data reference when the surface needs it.

## Evidence grades

| Grade | Acceptable evidence |
|---|---|
| A | Official usage/customer figures, public package download statistics, or a maintained open-source repository with substantial stars/forks and recent activity |
| B | Credible industry award, independent traffic estimate, or several consistent reputable reviews |
| C | Visible design quality or personal familiarity without adoption evidence |

Do not describe Grade C as `high popularity`. If no reliable metric exists, write `Popularity unverified; selected for design relevance`.

## Required reference matrix

```text
Product / URL:
Evidence and checked date:
Comparable user/job:
Pattern worth learning:
Pattern rejected:
Licensing or copying boundary:
```

Use 3-5 references. More references usually produce a collage rather than a coherent design.

## Pattern extraction

Prefer learning:

- how the product prioritizes the next action;
- how dense information is grouped and progressively disclosed;
- how filters, search, selection, details, and bulk actions preserve context;
- how loading, empty, invalid, conflict, permission, and success states are communicated;
- how mobile composition differs rather than merely shrinks;
- how visual tokens express hierarchy and product identity;
- how keyboard, focus, accessible names, contrast, and reduced motion are handled.

Do not copy:

- brand names, logos, proprietary illustrations, photos, or product copy;
- a signature layout or animation closely enough to cause source confusion;
- source code whose license is incompatible with the project;
- visual details that do not serve the approved user outcome.

## Current scienceresearch calibration set

Checked 2026-08-30. Re-check before using these numbers in a future task.

| Reference | Popularity signal | Potential lesson |
|---|---:|---|
| [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy) | 76,063 stars / 5,929 forks | Local-first workspace, projects plus knowledge structure, editable content surfaces |
| [Plane](https://github.com/makeplane/plane) | 58,527 stars / 5,569 forks | Modern issue/workflow navigation, state transitions, cycles and context preservation |
| [Logseq](https://github.com/logseq/logseq) | 44,678 stars / 2,790 forks | Local-first research/knowledge capture and linked context |
| [OpenProject](https://github.com/opf/openproject) | 15,968 stars / 3,454 forks | Dense project planning, work-package tables, filters, Gantt and portfolio hierarchy |
| [eLabFTW](https://github.com/elabftw/elabftw) | 1,408 stars / 325 forks | Research-specific electronic lab notebook concepts, experiments, evidence and traceability |

These are possible workflow references, not a direction to replace the approved `scienceresearch` prototype. Repository licenses also do not grant permission to copy brand identity or product content.
