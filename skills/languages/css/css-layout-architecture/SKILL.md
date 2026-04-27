---
name: css-layout-architecture
description: Use when reviewing CSS layout strategy, responsive design, naming conventions, and styling architecture.
---

# CSS Layout Architecture

## When To Use
- The main decision is about layout system selection (Grid vs Flexbox), responsive breakpoints, or naming methodology.
- Reviewing CSS custom property usage, cascade management, or styling performance.

## Workflow
1. Identify layout strategy — is CSS Grid used for 2D layouts and Flexbox for 1D?
2. Review responsive design — are breakpoints chosen based on content, not device widths?
3. Check naming methodology — is BEM, SMACSS, or CSS Modules used consistently?
4. Review CSS custom properties — are theme values defined as variables?
5. Check specificity management — is `!important` avoided? Is `@layer` used for cascade control?
6. Review container queries — are they used for component-level responsive design?
7. Recommend the most maintainable CSS architecture.

## Output Format
```markdown
CSS layout review:
- Layout strategy:
- Responsive design:
- Naming methodology:
- Custom properties:
- Specificity management:
- Container queries:
- Recommended change:
- Verification:
```
