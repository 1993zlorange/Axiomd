# External Skill and design-engineering review

Reviewed on 2026-08-30 using GitHub metadata and source files. Popularity figures are point-in-time signals and must be re-checked before future claims.

| Source | Popularity at review | Useful mechanism | Adoption decision |
|---|---:|---|---|
| [anthropics/skills](https://github.com/anthropics/skills), `frontend-design` | 172,475 stars / 20,494 forks | Ground design in subject/audience/page job; deliberate typography, hierarchy and motion; design-plan and self-critique passes | Adopt subject-specific design, token planning, one signature element, screenshot critique, and anti-template discipline. Upstream license is referenced in its own terms, so no source text is vendored. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 82,189 stars / 5,628 forks | Infer page type, audience, brand and constraints; avoid common AI-generated visual defaults | Adopt Design Read and context-driven anti-default review. MIT. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), `react-best-practices` | 30,616 stars / 2,728 forks | Prioritized performance rules for async waterfalls, bundles, rendering, client state and re-renders | Adopt framework-neutral performance priorities. Do not introduce React/Next.js because the current project is Python/server-rendered and offline. The referenced Skill declares MIT. |
| [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills), `web-design-engineer` | 11,662 stars / 1,448 forks | Design calibration, browser acceptance, critique, style references and redesign protocol | Adopt browser evidence, calibration and critique stages without importing its large style library. MIT. |
| [educlopez/ui-craft](https://github.com/educlopez/ui-craft) | 297 stars / 17 forks | Surface-specific recipes, state completeness, accessibility, responsive and finish passes | Adopt state lattice, craft pass, motion restraint and completion review. MIT. |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 122,520 stars / 10,031 forks | Open-code, composable, accessible component practice | Use as component-engineering reference when compatible; do not migrate the project stack or copy a theme by default. MIT. |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | 19,222 stars / 1,234 forks | Accessible interaction primitives and state semantics | Adopt accessibility and interaction-contract ideas; no React dependency is added to this project. MIT. |

OpenAI's curated Skill list was also checked. It includes Figma design and implementation Skills, but they were not installed because this project has no configured Figma MCP workflow and the user requested an pr-en-00-engineer capability rather than a Figma dependency.

No third-party Skill was installed verbatim. This project Skill combines selected mechanisms with the existing `$pr-en-02-senior-engineer`, `$playwright`, approved project architecture, local-first/no-CDN constraints, and the fallback Python coding standard.
