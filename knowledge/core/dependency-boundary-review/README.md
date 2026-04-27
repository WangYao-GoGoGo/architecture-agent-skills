# Dependency Boundary Review Knowledge

## Use When

Reviewing dependencies between modules, packages, services, layers, schemas, frontend components, or infrastructure boundaries to reduce coupling and clarify ownership.

## Heuristics

- Map the current dependency direction before proposing changes.
- Identify the stable core: domain rules, policies, contracts, or data ownership.
- Identify volatile edges: frameworks, vendors, transport, persistence, UI, cache, external APIs.
- Volatile edges should depend inward; the core should not depend outward.
- Domain rules should not know transport or persistence details unless the project deliberately chooses an active record style.
- UI state should not leak into domain or persistence logic.
- Database schemas should be owned by a clear service, module, or migration process.
- Cache access should sit behind a policy or repository boundary when consistency matters.
- Framework dependencies are acceptable at the edge; they are risky in reusable core logic.

## Common Risks

- Proposing abstractions before understanding actual dependency pain.
- Making boundaries too fine-grained, increasing indirection without reducing change cost.
- Ignoring the cost of introducing a boundary (interface, factory, module split) vs the cost of the coupling.
