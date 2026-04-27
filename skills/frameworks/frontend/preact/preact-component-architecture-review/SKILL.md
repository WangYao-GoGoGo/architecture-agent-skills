---
name: preact-component-architecture-review
description: Use when reviewing Preact component architecture, hooks, signals, state management, and component boundaries.
---

# Preact Component Architecture Review

## When To Use

- The main decision is about Preact component organization, hook design, signal usage, or state management patterns.
- Reviewing component boundaries or rendering performance.

## Workflow

1. Identify component roles — page, feature, shared, and primitive components.
2. Review hook design — are hooks extracting reusable logic or creating hidden dependencies?
3. Check signal usage — are signals used for local or cross-component state?
4. Review state ownership — local state, signals, and global state boundaries.
5. Check component boundaries — do components mix data loading, business logic, and rendering?
6. Review rendering performance — are expensive computations memoized?
7. Recommend the smallest change that clarifies component or state ownership.

## Output Format

```markdown
Preact architecture review:
- Component roles:
- Hook design:
- Signal usage:
- State ownership:
- Component boundaries:
- Rendering performance:
- Recommended change:
- Verification:
```
