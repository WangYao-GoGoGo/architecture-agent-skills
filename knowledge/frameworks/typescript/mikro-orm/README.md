# MikroORM Knowledge

## Heuristics

- Keep entity definitions, identity map usage, and transaction boundaries coherent.
- Review eager/lazy loading and populate patterns.
- Treat migration strategy and schema synchronization as architecture.
- Use the unit of work pattern for complex write operations.

## Common Risks

- Identity map growing too large in long-running processes.
- Populate patterns causing unexpected query volume.
- Schema synchronization not reviewed before production.
