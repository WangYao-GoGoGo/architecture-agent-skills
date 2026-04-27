# Python Architecture Idioms

## Use When

- Reviewing Python modules, class-heavy code, clean architecture, protocols, or dependency boundaries.

## Heuristics

- Prefer simple modules and functions until classes add ownership or substitution value.
- Use `Protocol` for structural boundaries when tests or adapters benefit.
- Use dataclasses for data shape, not for hiding complex domain behavior by default.
- Avoid importing framework, database, or network details into pure domain logic.
- Keep side effects at clear edges.

## Common Risks

- Java-style interface hierarchies copied into Python.
- Global mutable configuration.
- Hidden I/O inside seemingly pure helpers.
- Overusing inheritance where composition or callables would be simpler.

