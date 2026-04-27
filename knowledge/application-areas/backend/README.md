# Backend Architecture Knowledge

## Heuristics

- Model service boundaries around ownership and business capability, not only technical layers.
- Keep transaction and consistency rules explicit.
- Separate transport contracts from domain and persistence details.
- Make external integrations visible at adapter boundaries.
- Treat observability and failure behavior as architecture.

## Common Risks

- Services split before ownership is clear.
- Shared databases across unclear ownership boundaries.
- Hidden synchronous calls in critical paths.
- Domain rules scattered across controllers, jobs, and repositories.

