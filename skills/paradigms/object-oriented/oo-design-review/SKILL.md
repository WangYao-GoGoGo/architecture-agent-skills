---
name: oo-design-review
description: Use when reviewing object-oriented code for responsibilities, encapsulation, inheritance, polymorphism, coupling, SOLID, GRASP, and design pattern fit.
---

# OO Design Review

Use this skill to review object-oriented structure, not just syntax or style.

## Workflow

1. Identify domain concepts and their current class/module owners.
2. Check whether behavior lives near the data and policy it needs.
3. Look for god classes, anemic models, large conditionals, inheritance misuse, and framework leakage.
4. Recommend responsibility moves before adding new patterns.
5. Prefer composition unless inheritance expresses a real substitutable relationship.
6. Include verification steps for behavior-preserving changes.

## Output Format

```markdown
OO review:
- Responsibility issues:
- Coupling issues:
- Pattern fit, if any:
- Refactoring steps:
- Verification:
```
