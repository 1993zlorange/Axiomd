# Optional Third-Party Skill Adapters

SR leaf Skills own the work contract and evidence gate. Third-party Skills are optional implementation aids, not scientific authorities.

## Routing aliases

- Nature Skills: academic search, reader, paper card, experiment log, data availability, statistics, figures, writing, polishing, reviewer, response, paper-to-PPT.
- K-Dense Scientific Agent Skills: hypothesis generation, experimental design, exploratory data analysis, statistical analysis, scientific visualization, scientific writing, peer review, mathematical modeling, poster generation.
- Academic Research Skills: deep research, academic paper, academic paper reviewer, academic pipeline.
- Research Paper Writing: story-first manuscript structure, reverse outline, claim–evidence alignment, adversarial review.
- Tencent BrowserSkill: optional local browser bridge for reading user-authorized, already logged-in research pages; use only with the dedicated [authenticated browser retrieval reference](browser-skill-literature-search.md).

## Invocation conditions

Invoke an adapter only when all are true:

1. The selected SR leaf explicitly needs that capability.
2. The upstream Skill is actually installed and its exact version/source is known.
3. Its license permits the intended use and redistribution.
4. Its network, filesystem, subprocess, credential, and external-action permissions fit the work contract.
5. Its output will be checked through the SR leaf's completion gate.

Do not default to high-risk download/search automation. In the 2026-09-08 local scan, `nature-academic-search` and `nature-downloader` required restricted treatment; treat later versions as untrusted until rescanned. A clean scan is not proof of safety.

When no adapter is installed, perform the leaf workflow using available local tools and disclose the limitation.

BrowserSkill is a runtime capability rather than a scientific authority. Treat its page reads as `observation` evidence, preserve the source URL and timestamp, and never treat the browser session as permission to extract credentials or bypass site controls.
