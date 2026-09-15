---
name: sr-doctoral-research
description: Route a doctoral research request to one focused ScienceResearch leaf skill across problem framing, literature, hypotheses, methods, experiments, analysis, papers, and weekly progress. Use when the user asks what research work to do next, requests an end-to-end research workflow, or has not named a specific SR leaf skill. Do not perform the leaf task inside this router.
metadata:
  short-description: Route doctoral work to one evidence-led SR skill
---

# SR Doctoral Research Router

如需保存路由记录，使用本目录的 [中文空白模板](assets/output-template.md)，文件名遵循 `YYYYMMDD-内容简述-路由记录.md`。

Select the smallest work package that can close the current highest-value uncertainty. This Skill routes; the selected leaf Skill performs the work.

## Routing protocol

1. Read [manifest.json](manifest.json). It contains only routing metadata and leaf paths.
2. Detect these axes from the request and supplied project context:
   - `aspect`: problem, literature, idea, method, experiment, analysis, paper, or progress.
   - `intent`: explore, decide, design, execute, diagnose, communicate, or review.
   - `state`: proposed, ready, running, blocked, evidence-ready, or closed.
   - `time_horizon`: today, this week, milestone, or manuscript cycle.
3. Identify one primary leaf. Prefer the work package whose deliverable would change the next scientific decision. State one line: `Detected: aspect=...; intent=...; primary=$sr-...; human checkpoint=...`.
4. Read [../sr-research-shared/references/research-contract.md](../sr-research-shared/references/research-contract.md), then read only the selected leaf `SKILL.md` from the path in the manifest.
5. Load other shared references only when triggered:
   - Human/AI authority is unclear or the task changes scope, resources, claims, ethics, privacy, collaboration, submission, or release: read [../sr-research-shared/references/human-ai-collaboration.md](../sr-research-shared/references/human-ai-collaboration.md).
   - The user asks for a weekly plan, weekly review, or group meeting: read [../sr-research-shared/references/weekly-loop.md](../sr-research-shared/references/weekly-loop.md) and use `$sr-weekly-meeting` after leaf outputs are checked.
   - A leaf recommends a third-party capability: read [../sr-research-shared/references/source-adapters.md](../sr-research-shared/references/source-adapters.md) before invoking it.
6. Return control to the selected leaf. Do not synthesize its substantive deliverable from this router.

## Selection rules

- Choose one primary Skill per work contract. A secondary Skill must consume the primary Skill's named output.
- Do not force a linear march through all 68 Skills. Research may loop from analysis back to hypothesis, method, or data.
- If the request names a leaf explicitly, validate its prerequisites and use it directly.
- If two Skills appear plausible, choose the one producing the earlier missing artifact. Example: use data-split before main-comparison when the split is not frozen.
- Use progress Skills only to manage scientific work; they do not replace literature, experiments, analysis, or human scientific decisions.

## Router output

```yaml
routing:
  aspect: ""
  intent: ""
  state: ""
  primary_skill: "sr-..."
  reason: ""
  prerequisite_artifacts: []
  optional_secondary_skill: null
  human_checkpoint: ""
```

If the necessary project context is absent, ask only for the one missing decision that changes routing. Otherwise proceed with explicit assumptions.
