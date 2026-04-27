# Kotlin Multiplatform Knowledge

## Heuristics

- Put shared domain, use cases, data contracts, and pure business logic in common modules.
- Keep platform UI, permissions, storage, networking details, and lifecycle behavior in platform modules.
- Design expect/actual APIs as stable platform ports.
- Test shared logic without mobile runtime boot where possible.

## Common Risks

- Shared modules depending on platform lifecycle assumptions.
- expect/actual boundaries becoming arbitrary wrappers.
- Platform-specific error and offline behavior handled inconsistently.
