---
name: refactoring-planner
description: Use before changing existing code when behavior must remain stable and the agent should plan a safe sequence of refactoring steps, tests, boundaries, and rollback points across any language or domain.
---

# Refactoring Planner

Use this skill before modifying existing code with non-trivial structure, dependencies, or behavior.

## When To Use

- The user asks to refactor, clean up, modularize, or improve architecture.
- The code has unclear ownership, duplication, long methods, large conditionals, tight coupling, or hard-to-test logic.
- The change affects multiple files, modules, schemas, APIs, or workflows.

Do not use this skill for tiny edits that can be safely made directly.

## Workflow

1. Inspect current behavior, public interfaces, tests, and callers.
2. Name the architecture pressure.
3. Identify behavior that must not change.
4. Choose the smallest target structure.
5. Split the refactor into behavior-preserving steps.
6. Add or identify verification before risky moves.
7. Implement incrementally and check after each meaningful step.

## Planning Heuristics

- Preserve external behavior first; improve shape second.
- Extract one responsibility at a time.
- Prefer moving code behind an existing boundary before changing callers.
- Keep compatibility adapters temporarily when many callers exist.
- Avoid renaming and behavior changes in the same step.
- For database or API changes, include migration and compatibility strategy.

## Output Format

```markdown
Refactoring plan:
- Current pressure:
- Behavior to preserve:
- Target structure:
- Steps:
- Verification:
- Risks:
- Overengineering check:
```
