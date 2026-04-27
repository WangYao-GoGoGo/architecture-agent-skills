# Architecture Patterns

Reusable structures for system-level organization. These patterns apply at the highest level of abstraction, defining how components, services, and modules interact across process and network boundaries.

## Patterns

| Pattern | Intent |
|---------|--------|
| **Layered Architecture** | Organize code into strict dependency layers (presentation → application → domain → infrastructure) |
| **Hexagonal Architecture (Ports & Adapters)** | Isolate core business logic from infrastructure by defining ports (interfaces) and adapters (implementations) |
| **CQRS (Command Query Responsibility Segregation)** | Separate read models (queries) from write models (commands) to optimize each independently |
| **Event Sourcing** | Store application state as a sequence of immutable events; reconstruct state by replaying events |
| **Saga** | Manage distributed transactions as a sequence of local transactions with compensating actions on failure |
| **Pipes and Filters** | Process data through a sequence of independent, composable stages |
| **Event-Driven Architecture** | Decouple components through asynchronous event publication and subscription |
| **Microkernel (Plugin Architecture)** | Provide a minimal core system with pluggable extension points |
| **Space-Based Architecture** | Distribute processing and data across multiple nodes with no central database |
| **Service-Oriented Architecture (SOA)** | Decompose functionality into loosely coupled, independently deployable services |
| **Serverless / FaaS** | Deploy individual functions that are triggered by events and scale automatically |

## Use When

- The system has multiple deployment units or service boundaries
- Different parts of the system have different scaling, consistency, or latency requirements
- The team needs to evolve parts of the system independently
- Long-term maintainability requires clear separation of concerns at the system level

## Related Knowledge

- [`knowledge/architecture/`](../../architecture/) — architecture styles, patterns, and decision guidance
- [`knowledge/architecture/application-styles/`](../../architecture/application-styles/) — application-level architecture styles
- [`knowledge/architecture/integration-patterns/`](../../architecture/integration-patterns/) — integration and messaging patterns
- [`knowledge/principles/`](../../principles/) — SOLID, GRASP, and design principles
- [`skills/core/architecture-before-coding/SKILL.md`](../../../skills/core/architecture-before-coding/SKILL.md) — skill for architecture-first design
