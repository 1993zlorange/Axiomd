# Frontend quality gate

## Product and composition

- The surface has one clear job and one obvious next action for the target user.
- Existing project content, workflow, and data shape determine the layout; the page is not a generic template populated afterward.
- Information hierarchy is visible through typography, spacing, grouping, alignment, and progressive disclosure, not only colored containers.
- A compact design-token system defines color, typography roles, spacing, radii, borders, shadows, and motion.
- One restrained signature element makes the surface memorable and serves the subject.
- Realistic copy and data are used. Labels describe the user action, not the implementation.

## Anti-template review

Revise unless specifically justified by the approved brief:

- purple/cyan gradients, glowing blobs, or glass panels used as default identity;
- a centered hero followed by identical icon-heading-text card grids;
- every section wrapped in the same rounded card;
- emoji used as product icons;
- decorative charts, fake screenshots, placeholder statistics, or invented social proof;
- repeated uppercase eyebrows, arbitrary section numbers, or generic `Learn more` actions;
- `transition: all`, constant motion, bounce effects, or animation without state/spatial meaning;
- visual copying that makes the page look like another brand.

## Interaction completeness

For every control:

- normal activation produces a visible, correct result;
- invalid input identifies the field/problem and a recovery action;
- loading prevents accidental duplicate actions without hiding context;
- empty state explains what is absent and how to create or select it;
- conflict/stale state preserves input and offers reload/retry guidance;
- success feedback names what changed and keeps the user in the relevant context;
- refresh reproduces persisted state;
- destructive action names the consequence and has appropriate confirmation;
- no-JavaScript core navigation and forms remain usable when required.

## Accessibility

- semantic landmarks, headings, labels, buttons, links, tables, lists, and form relationships;
- keyboard access and logical tab order;
- visible `:focus-visible`, correct focus after dialogs/errors/navigation, and no keyboard traps;
- accessible names for icon-only controls and live-region feedback where needed;
- color is not the only state signal and contrast is adequate;
- target size is usable on touch screens;
- `prefers-reduced-motion` is honored;
- zoom/reflow and 390-pixel layout do not hide content or require horizontal scrolling.

## Responsive and performance

- verify 1440, 900, and 390 widths using real content;
- mobile layout recomposes priority and controls instead of only shrinking desktop;
- long labels, identifiers, tables, error text, and empty states do not overflow;
- scripts are local and narrowly scoped; no unapproved CDN or third-party runtime;
- avoid unnecessary DOM, repeated listeners, layout thrash, blocking work, and unbounded rendering;
- no Console error, PageError, failed local resource, or inaccessible hidden action.

## Browser evidence

Retain screenshots or snapshots for each required viewport, request/response evidence for changed actions, Console/PageError results, keyboard/focus observations, and persisted-state checks. Source inspection and HTTP 200 are not acceptance evidence by themselves.
