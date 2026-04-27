---
name: react-component-architecture-review
description: Use when reviewing React component architecture, component boundaries, hooks, state management, effects, context, and rendering boundaries.
---

# React Component Architecture Review

## When To Use

- The main decision is about React component organization, state ownership, hook design, effect boundaries, or rendering performance.
- Reviewing context usage, prop drilling, or server/client component boundaries (Next.js).

## Workflow

1. Identify component roles — page, feature, shared, and primitive components.
2. Map state ownership — local UI state, server state, derived state, and global app state.
3. Review hook design — are hooks extracting reusable logic or creating hidden dependencies?
4. Check effect boundaries — are effects used for synchronization or general control flow?
5. Review context usage — is context used for cross-cutting concerns or avoiding prop drilling?
6. Check rendering boundaries — are expensive computations memoized appropriately?
7. Recommend the smallest change that clarifies component or state ownership.

## Output Format

```markdown
React architecture review:
- Component roles:
- State ownership:
- Hook design:
- Effect boundaries:
- Context usage:
- Rendering boundaries:
- Recommended change:
- Verification:
```
