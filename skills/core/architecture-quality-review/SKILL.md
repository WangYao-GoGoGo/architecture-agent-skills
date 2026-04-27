---
name: architecture-quality-review
description: Use to evaluate whether generated or existing code meets architecture quality standards — maintainability, readability, testability, dependency direction, and appropriate abstraction level.
---

# Architecture Quality Review

Use this skill to evaluate whether code meets architecture quality standards. This is the verification counterpart to `architecture-before-coding` and `refactoring-planner` — it checks whether the result actually achieves the intended quality.

## When To Use

- After generating code with `architecture-before-coding` or `new-project-scaffolding`.
- After completing a refactoring with `refactoring-planner`.
- When reviewing AI-generated code for architecture quality.
- When a code review needs a structured quality assessment.
- Before merging a pull request that touches architecture-significant code.

Do **not** use this skill for trivial formatting reviews, one-line changes, or code that is explicitly temporary.

## Workflow

### Step 1: Check Dependency Direction

Verify that dependencies point in the correct direction:

- Domain/core code must not import infrastructure, framework, or UI code.
- High-level policy must not depend on low-level details.
- Interfaces should be owned by the consumer, not the implementor.
- No cyclic dependencies between modules or packages.

**Pass criteria**: All dependency rules are satisfied. Any violation is documented as a finding.

### Step 2: Check Responsibility Boundaries

Verify that each unit has a clear, single responsibility:

- Classes/modules have names that describe a single concept.
- Methods/functions operate at a single level of abstraction.
- No god classes, long methods, or large conditionals.
- Data and behavior that change together are in the same unit.

**Pass criteria**: No smell exceeds the project's threshold. Each unit has a clear purpose.

### Step 3: Check Testability

Verify that the code can be tested effectively:

- Domain logic can be tested without infrastructure (database, network, filesystem).
- Dependencies can be substituted (mocked, stubbed, or faked) at boundaries.
- Tests do not require complex setup for simple assertions.
- Side effects are explicit and testable.

**Pass criteria**: Core domain logic is unit-testable. Integration points have clear test strategies.

### Step 4: Check Abstraction Level

Verify that abstractions are justified and not over-engineered:

- Every abstraction solves a current problem, not a hypothetical future one.
- The abstraction level is consistent within each module.
- No unnecessary indirection layers.
- Patterns are applied only when they reduce real complexity.

**Pass criteria**: No abstraction is present without a clear, current justification.

### Step 5: Check Readability & Maintainability

Verify that the code is easy to read and change:

- Names reflect domain concepts, not implementation details.
- Functions are small enough to understand in one screen.
- Comments explain "why", not "what".
- Error handling is explicit and consistent.
- Configuration is externalized, not hard-coded.

**Pass criteria**: A developer unfamiliar with the code can understand the structure and make a safe change.

### Step 6: Assign Quality Score

Based on the checks above, assign a quality score:

| Score | Meaning | Action |
|---|---|---|
| 🟢 **Pass** | All checks pass. Code meets architecture standards. | Merge as-is. |
| 🟡 **Minor** | 1-2 minor violations. No structural issues. | Fix violations, then merge. |
| 🟠 **Major** | 3+ violations or 1 structural issue. | Fix before merge. May need refactoring plan. |
| 🔴 **Critical** | Dependency direction violation or untestable core logic. | Do not merge. Create refactoring plan first. |

## Knowledge To Use

- [`knowledge/principles/`](../../knowledge/principles/README.md) — SOLID, GRASP, dependency inversion, separation of concerns.
- [`knowledge/smells/`](../../knowledge/smells/README.md) — symptom identification for quality issues.
- [`knowledge/refactoring/`](../../knowledge/refactoring/README.md) — refactoring moves to fix quality issues.
- [`knowledge/architecture/application-styles/`](../../knowledge/architecture/application-styles/README.md) — expected structure for the chosen architecture style.
- [`skills/core/anti-overengineering-review/`](../anti-overengineering-review/README.md) — to check abstraction justification.

## Output Format

```markdown
## Architecture Quality Review

### Score: 🟢 Pass / 🟡 Minor / 🟠 Major / 🔴 Critical

### Findings

| # | Category | Severity | Description | Recommendation |
|---|---|---|---|---|
| 1 | Dependency Direction | High | ... | ... |
| 2 | Responsibility | Medium | ... | ... |

### Summary

- Dependency direction: ✅ / ❌ (details)
- Responsibility boundaries: ✅ / ❌ (details)
- Testability: ✅ / ❌ (details)
- Abstraction level: ✅ / ❌ (details)
- Readability: ✅ / ❌ (details)

### Action Required

- [ ] Fix minor violations
- [ ] Create refactoring plan for structural issues
- [ ] Re-review after fixes
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — to design code that passes quality review.
- [`refactoring-planner`](../refactoring-planner/README.md) — to plan fixes for quality issues found.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to check abstraction justification.
- [`new-project-scaffolding`](../new-project-scaffolding/README.md) — to generate code with quality built in.
