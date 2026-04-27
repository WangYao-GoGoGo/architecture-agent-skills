# Tight Coupling

## Use When

- A unit knows too much about another unit's internals.
- Core logic directly imports vendors, databases, caches, UI, or framework details.

## Why It Hurts

- Changes cascade across boundaries.
- Tests become slow or hard to isolate.
- Reuse becomes difficult.

## Refactoring Moves

- Introduce an adapter at the volatile edge.
- Define a small interface owned by the consumer.
- Move framework-specific code outward.
- Keep direct dependencies when they are stable and local.
