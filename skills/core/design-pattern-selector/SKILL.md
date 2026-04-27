---
name: design-pattern-selector
description: Use when choosing whether a design pattern is appropriate for new or existing code, especially around object-oriented design, Java, Python, large conditionals, duplicated workflows, object creation, adapters, notifications, commands, or extension points.
---

# Design Pattern Selector

Use this skill to select a design pattern only when it reduces real complexity or change cost. The default answer can be "no pattern needed."

## Inputs To Inspect

- Current code structure and naming.
- Repeated conditionals or duplicated workflows.
- Places where creation logic leaks into callers.
- External APIs or libraries that do not match local interfaces.
- Expected future variation points.
- Testability and dependency direction.

## Selection Workflow

1. Name the design pressure: variation, creation, integration, notification, workflow, lifecycle, or dependency boundary.
2. Check if the problem is current, not imaginary.
3. List at most three candidate patterns.
4. Choose the simplest candidate that improves readability, testability, or change isolation.
5. Explain why rejected candidates are not needed.
6. Provide a small refactoring or implementation plan.

## Quick Decision Table

| Pressure | Prefer | Use When |
| --- | --- | --- |
| Many interchangeable behaviors | Strategy | A caller chooses or injects behavior at runtime |
| Large conditional by type | Strategy or polymorphism | Each branch is a stable behavior with its own rules |
| Complex object construction | Builder | Many optional values, validation, or stepwise construction |
| Family of related objects | Abstract Factory | Products must be created consistently together |
| Single object creation hook | Factory Method | Subclasses or modules decide concrete creation |
| Incompatible external interface | Adapter | Local code should not depend on vendor shape |
| Complex subsystem boundary | Facade | Callers need a simpler API over many collaborators |
| Cross-cutting reaction to events | Observer | Multiple consumers react independently |
| Encapsulated user action | Command | Actions need queuing, undo, logging, retries, or scheduling |
| Stable algorithm skeleton | Template Method | Steps vary but the sequence must remain fixed |

## Anti-Pattern Warnings

- Do not add Strategy for two branches that are unlikely to grow.
- Do not add Factory just to hide a constructor with no variation.
- Do not use Singleton to avoid dependency injection.
- Do not introduce inheritance when composition is enough.
- Do not make every pattern class public unless callers need it.

## Output Format

```markdown
Pattern recommendation:
- Design pressure:
- Recommended pattern:
- Why it fits:
- Why simpler code is or is not enough:
- Alternatives rejected:
- Refactoring steps:
- Verification:
```
