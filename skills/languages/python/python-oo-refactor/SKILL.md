---
name: python-oo-refactor
description: Use when refactoring Python object-oriented or class-heavy code for responsibilities, protocols, composition, dependency injection, design patterns, and testability.
---

# Python OO Refactor

## Workflow

1. Inspect modules, classes, call sites, tests, and typing style.
2. Identify long methods, god classes, large conditionals, or hidden dependencies.
3. Prefer small classes, plain functions, dataclasses, and protocols where they fit.
4. Use patterns lightly; Python often needs less ceremony than Java.
5. Verify with focused tests or characterization checks.

## Python Rules

- Prefer composition and dependency parameters over global state.
- Use `Protocol` when structural substitution helps tests or boundaries.
- Avoid abstract base classes unless runtime enforcement or shared behavior is needed.
- Keep modules cohesive around domain or workflow concepts.

## Output Format

```markdown
Python refactor:
- Design pressure:
- Recommended structure:
- Python idioms used:
- Steps:
- Verification:
```
