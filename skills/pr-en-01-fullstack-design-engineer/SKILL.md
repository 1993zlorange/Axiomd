---
name: pr-en-01-fullstack-design-engineer
description: Implement approved full-stack Web work by researching relevant high-adoption product references, defining an original design direction, building and browser-verifying a distinctive accessible interactive frontend, then implementing the architecture-conformant Python backend and end-to-end tests. Use for new pages, redesigns, dashboards, workflows, forms, or full-stack features. Do not use to invent requirements, copy another site's identity, or force frontend research onto a backend-only defect.
---

# Full-Stack Design Engineer

Deliver a complete product surface, not a styled mockup and not a backend with a token UI. For UI-bearing work, frontend design and interaction are established first; backend implementation follows the approved interaction, data, and state contracts.

## Entry gate

Before implementation, identify the user-confirmed Requirements Understanding Contract, exact SRS/SDD/architecture baseline, requirement and design IDs, success/failure behavior, and excluded scope. If the product decision is unresolved, return it to the project manager. If the approved architecture cannot support a Must requirement, return it to the architect. Do not hide upstream uncertainty inside frontend or backend code.

## 1. Inspect the existing product

Read the current UI, target prototype, design tokens, assets, routes, domain/API contracts, tests, user manual, and project instructions. For `scienceresearch`, preserve local-first operation, progressive enhancement, server-rendered core flows, no CDN dependency, and the current approved prototype direction unless the baseline explicitly changes them.

## 2. Research high-adoption references

When network access is authorized and UI work is material, find 3-5 products or websites with a comparable user, information density, or workflow. Read [references/reference-research.md](references/reference-research.md) and produce a compact reference matrix before choosing the design direction.

Popularity is evidence, not taste. Prefer official product pages plus verifiable adoption signals such as repository stars/forks, package downloads, public customer or usage figures, respected awards, or credible traffic data. Record the source and date. Mark unsupported popularity claims `Unverified`.

Extract transferable patterns: information architecture, navigation, progressive disclosure, interaction feedback, data density, empty/error states, and responsive behavior. Do not copy trademarks, proprietary copy, illustrations, screenshots, or a distinctive layout wholesale. The output must remain recognizably this product.

## 3. Declare the Design Read

Before substantial frontend code, state:

```text
Surface and single job:
Target user and usage pressure:
Visual language and density:
Information hierarchy:
Interaction model:
Token direction:
Signature element:
Reference patterns adopted:
References or patterns rejected:
Accessibility and responsive risks:
```

If this direction materially changes an approved visual or workflow decision, obtain confirmation before coding. Otherwise proceed and retain the Design Read as implementation evidence.

## 4. Define the frontend contract

Sketch the smallest data, action, state, and error contracts the UI needs. This is not permission to implement the entire backend first. It prevents a beautiful prototype from depending on impossible data.

For every interactive control, define:

- user intent and specific action label;
- request method/path or local action;
- idle, loading, success, empty, invalid, conflict, and dependency-failure behavior as applicable;
- visible response and focus destination;
- persisted state and refresh behavior;
- no-JavaScript or degraded-mode behavior for core flows;
- authorization and destructive-action constraints.

## 5. Build the frontend vertical slice

Implement the surface using the approved project stack. Prefer semantic HTML, CSS design tokens, narrow JavaScript islands, and progressive enhancement in this project. Create a coherent visual system rather than styling elements independently.

Read [references/frontend-quality-gate.md](references/frontend-quality-gate.md) before implementation and again for the final critique. The UI must include real content shape and complete states; placeholders and mock adapters may be used only as isolated development seams and must not remain as the final business source of truth.

## 6. Critique in a real browser

Use Playwright or the project's browser tool to navigate, fill, click, reload, resize, and inspect. Capture at least desktop, medium, and mobile evidence, normally 1440, 900, and 390 pixels wide. Check the exact visible result, URL, request/response, Console, PageError, persisted state, keyboard order, focus, reduced motion, and horizontal overflow.

Perform two passes:

1. **Interaction pass:** every changed control works on normal, invalid, duplicate, missing-prerequisite, and stale/conflict paths where relevant.
2. **Craft pass:** hierarchy, typography, spacing rhythm, density, alignment, content clarity, responsive composition, state visibility, and unnecessary decoration.

Do not declare the frontend complete from source inspection or HTTP 200 alone.

## 7. Implement the backend

After the interaction contract and frontend slice are stable, use the senior-engineer workflow and the project coding standard. Keep the approved dependency direction and module ownership. In particular:

- domain and application logic do not live in HTTP handlers, templates, or JavaScript;
- queries are read-only and commands have visible, bounded side effects;
- public inputs and outputs are typed and validated;
- errors have stable codes, correct HTTP status, actionable detail, and no secret or absolute-path leakage;
- transactions, optimistic versions, retries, idempotency, cancellation, and atomic file writes are explicit where applicable;
- paths stay inside approved roots, SQL is parameterized, subprocesses use argument arrays and `shell=False`;
- API, page, and database state cannot disagree after refresh;
- backend tests cover normal, boundary, invalid, dependency-failure, conflict, recovery, and compatibility behavior in proportion to risk.

Read [references/backend-quality-gate.md](references/backend-quality-gate.md) for the final backend review.

## 8. Integrate and finish

Replace temporary frontend fixtures with real application ports. Run focused tests, full unit/integration/contract tests, architecture checks, and browser E2E. Re-run browser screenshots after backend integration because real content and failures often change layout.

Handoff only when every Must requirement maps to code and retained evidence, no changed button is inert, no required state is invisible, no temporary mock is the final source of truth, and engineering logs name the time, requirement/design IDs, files, commands, results, and remaining risks.

## Modes

- **Full-stack feature/redesign:** run the complete workflow.
- **Frontend-only approved change:** stop after frontend integration and browser verification; do not invent backend work.
- **Backend-only feature or defect:** use the senior-engineer workflow directly; website research and visual design are not required.
- **Defect fix:** reproduce first, add a regression test, make the smallest complete correction, and browser-test it if user-facing.

Read [references/source-review.md](references/source-review.md) when explaining why this workflow uses these design and engineering mechanisms.
