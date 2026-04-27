# C Architecture Idioms

## Use When

- Reviewing C modules, headers, resource ownership, state management, or procedural boundaries.

## Heuristics

- Use headers as stable public contracts.
- Hide internals with opaque structs when callers should not depend on layout.
- Document ownership, lifetime, error return rules, and thread-safety.
- Keep platform-specific code behind narrow interfaces.
- Move global state into explicit context structures when testability or concurrency matters.

## Common Risks

- Public headers exposing private fields.
- Unclear ownership of allocated memory.
- Mixed I/O, parsing, business logic, and resource cleanup.
- Hidden shared state.

