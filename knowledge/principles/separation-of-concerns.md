# Separation Of Concerns

## Use When

- One file, class, function, query, or component handles unrelated responsibilities.
- A change in formatting, persistence, validation, business rules, or transport causes unrelated edits.

## Core Idea

Separate responsibilities that change for different reasons.

## Common Concern Boundaries

- Domain rules vs transport.
- Domain rules vs persistence.
- Query shape vs presentation shape.
- Cache policy vs business rules.
- UI state vs server state.
- Validation vs orchestration.

## Avoid

- Splitting code into layers that only pass data through.
- Separating concerns so aggressively that simple workflows become hard to trace.
