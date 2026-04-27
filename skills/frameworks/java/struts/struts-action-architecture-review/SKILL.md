---
name: struts-action-architecture-review
description: Use when reviewing Apache Struts action mapping, form beans, interceptors, validation, tile layout, and request processing lifecycle.
---

# Struts Action Architecture Review

## When To Use

- The main decision is about Struts action class design, form bean boundaries, interceptor stack configuration, or validation strategy.
- Reviewing tile layout, result types, or request processing flow.

## Workflow

1. Identify the action mapping structure — action classes, form beans, and result types.
2. Review form bean design — are they used for both input and output, or separated?
3. Check interceptor stack configuration — custom interceptors, ordering, and parameter filtering.
4. Review validation strategy — XML validation, annotation-based, or programmatic.
5. Check tile layout and view resolution — template composition and reuse.
6. Review request processing lifecycle — pre-processing, action execution, and post-processing.
7. Recommend the smallest structural change that improves maintainability or security.

## Output Format

```markdown
Struts architecture review:
- Action mapping structure:
- Form bean design:
- Interceptor stack:
- Validation strategy:
- Tile layout:
- Request lifecycle:
- Recommended change:
- Verification:
```
