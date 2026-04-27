---
name: component-architecture-review
description: Use when reviewing frontend component boundaries, state ownership, data loading, prop flow, side effects, reusable components, and UI workflow architecture.
---

# Component Architecture Review

## Workflow

1. Identify page, feature, shared, and primitive component roles.
2. Map local state, server state, derived state, and global state.
3. Check whether data loading and side effects are placed at clear boundaries.
4. Look for prop drilling, duplicated UI logic, over-generic components, and mixed concerns.
5. Recommend the smallest component or state ownership change.
6. Verify with UI tests, story coverage, or targeted manual checks.

## Output Format

```markdown
Frontend architecture review:
- Component roles:
- State ownership:
- Side effects:
- Recommended change:
- Verification:
```
