# Design Pattern Selector Knowledge

## Use When

Choosing whether a design pattern is appropriate for new or existing code — especially around object-oriented design, large conditionals, duplicated workflows, object creation, adapters, notifications, commands, or extension points.

## Heuristics

- Name the design pressure before selecting a pattern: variation, creation, integration, notification, workflow, lifecycle, or dependency boundary.
- Check if the problem is current, not imaginary.
- List at most three candidate patterns.
- Choose the simplest candidate that improves readability, testability, or change isolation.
- Explain why rejected candidates are not needed.
- Do not add Strategy for two branches that are unlikely to grow.
- Do not add Factory just to hide a constructor with no variation.
- Do not use Singleton to avoid dependency injection.
- Do not introduce inheritance when composition is enough.
- The default answer can be "no pattern needed."

## Quick Decision Table

| Pressure | Prefer | Use When |
|---|---|---|
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

## Common Risks

- Applying a pattern because it is familiar, not because it solves a real problem.
- Making every pattern class public when callers only need a simple function.
- Introducing inheritance hierarchies where composition would be simpler.
- Using Singleton as a lazy substitute for dependency injection.
