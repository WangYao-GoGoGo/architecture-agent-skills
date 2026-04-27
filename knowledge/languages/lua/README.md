# Lua Architecture Idioms

## Use When

- Reviewing Lua metatable usage, module patterns, coroutine design, or embedded scripting architecture.

## Heuristics

- Use metatables for prototype-based OOP — `__index` for method lookup, `__newindex` for property control.
- Use the module pattern (returning a table) for namespace organization.
- Use coroutines for cooperative concurrency — they yield control explicitly.
- Prefer local variables over globals — every global is a table lookup.
- Use `:colon` syntax for method calls with implicit `self`.
- Keep the C API boundary thin when embedding — push/pop stack discipline.
- Use `require` for dependency loading — it caches and returns the module table.
- Use `...` (varargs) sparingly — prefer explicit parameters.

## Common Risks

- Global variable pollution from forgetting `local` declarations.
- Metatable cycles causing garbage collector issues.
- Over-using `setfenv`/`getfenv` (Lua 5.1) or `_ENV` (Lua 5.2+) for sandboxing without proper restrictions.
- Table traversal order assumptions — table order is not guaranteed.
- Coroutine stack overflows from deeply nested yields.
