# Clean Architecture

## Use When

- Domain policy should remain independent from frameworks, UI, databases, and vendors.
- The project has enough complexity to justify explicit boundaries.

## Core Idea

Keep business rules near the center and implementation details at the edges. Dependencies point inward.

## Practical Guidance

- Use cases orchestrate application workflows.
- Entities or domain models hold core rules.
- Adapters translate between external details and internal contracts.
- Ports should exist because substitution or boundary control matters, not by habit.

## Avoid

- Creating many layers for a small CRUD feature.
- Making every object an interface.
