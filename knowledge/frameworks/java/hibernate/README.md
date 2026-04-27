# Hibernate Knowledge

## Heuristics

- Keep entity lifecycle, lazy loading, cascading, and dirty checking visible.
- Avoid serializing lazy entities directly through API boundaries.
- Review fetch plans for N+1 behavior.
- Keep transaction scope aligned with use cases.

