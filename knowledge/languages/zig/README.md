# Zig Architecture Idioms

## Use When

- Reviewing Zig allocator strategy, comptime code, error union handling, or module organization.

## Heuristics

- Pass allocators explicitly — prefer arena allocators for short-lived scopes.
- Use `comptime` for code generation and type introspection, not for runtime logic.
- Handle errors with error unions — Zig has no exceptions or null.
- Use `defer` for cleanup — pair allocation and deallocation closely.
- Organize code into files that mirror the namespace hierarchy.
- Prefer slices over pointers with length for buffer management.
- Use `@fieldParentPtr` for type-safe downcasting in container patterns.
- Test with `test` blocks co-located with the code they test.

## Common Risks

- Memory leaks from missing `defer` or `errdefer` for allocated resources.
- Overusing `comptime` when runtime dispatch would be simpler.
- Integer overflow not being handled (Zig has wrapping and explicit overflow ops).
- Ignoring the return value of functions that return error unions.
- Mixing allocator strategies (arena vs general-purpose) without clear ownership.
