# Vert.x Knowledge

## Heuristics

- Design verticles as bounded processing units with clear message contracts.
- Organize event bus addresses by domain and event type for observability.
- Use backpressure-aware stream types; avoid unbounded buffers.
- Use shared data structures (`SharedData`, `LocalMap`) with clear ownership boundaries.
- Handle verticle deployment failure and restart with `AbstractVerticle` lifecycle hooks.

## Common Risks

- Verticles that are too large or too fragmented.
- Event bus addresses that are not namespaced.
- Unbounded buffers in reactive streams.
