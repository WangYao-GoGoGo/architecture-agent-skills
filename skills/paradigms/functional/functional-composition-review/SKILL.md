---
name: functional-composition-review
description: Use when reviewing functional or function-heavy code for composition, pure core boundaries, immutability, error flow, and side-effect isolation.
---

# Functional Composition Review

Use this skill to improve function-heavy code without introducing unnecessary classes.

## Workflow

1. Identify pure transformations and side-effecting operations.
2. Check whether data flow is explicit.
3. Look for hidden mutation, broad shared state, and unclear error handling.
4. Recommend smaller composable functions where it improves readability.
5. Keep orchestration readable; do not split every expression.
6. Verify with focused input/output tests.

## Output Format

```markdown
Functional review:
- Pure core:
- Side effects:
- Composition issues:
- Refactoring steps:
- Verification:
```
