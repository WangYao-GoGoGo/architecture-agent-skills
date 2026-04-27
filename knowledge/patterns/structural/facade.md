# Facade

## Use When

- Callers interact with a complex subsystem through many steps.
- A simpler boundary would reduce duplication or coupling.

## Avoid When

- The facade only forwards one method to one object.
- It hides important failure or consistency details.

## Core Idea

Provide a simple interface over a complex subsystem while keeping detailed behavior inside.

## Agent Heuristics

- Use for orchestration across several collaborators.
- Keep facade methods aligned with use cases.
- Do not let the facade become a god class.
