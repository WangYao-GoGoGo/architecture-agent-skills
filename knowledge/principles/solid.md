# SOLID

## Use When

- Reviewing object-oriented or service/module boundaries.
- Refactoring classes with too many reasons to change.
- Designing extension points for behavior that is likely to vary.

## Core Idea

SOLID is a set of heuristics for keeping responsibilities focused and dependencies manageable.

- Single Responsibility: one unit should have one primary reason to change.
- Open/Closed: extend behavior without repeatedly editing stable code.
- Liskov Substitution: subtypes must preserve the expectations of their base type.
- Interface Segregation: callers should depend only on operations they use.
- Dependency Inversion: high-level policy should not depend directly on low-level details.

## Agent Heuristics

- If a class mixes domain rules, persistence, transport, and formatting, look for responsibility splits.
- If callers switch on type or mode repeatedly, consider polymorphism or Strategy.
- If an interface has many unused methods, split it by caller need.
- If domain logic imports framework or vendor details, consider an inward-facing boundary.

## Avoid

- Creating one interface per class without a substitution or boundary need.
- Applying every principle mechanically in tiny scripts or simple CRUD code.
