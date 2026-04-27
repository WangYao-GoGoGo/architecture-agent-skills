# C++ Architecture Idioms

## Use When

- Reviewing C++ class hierarchies, memory management, template design, or STL usage.

## Heuristics

- Use RAII for resource management — avoid raw `new`/`delete`.
- Prefer `std::unique_ptr` for exclusive ownership, `std::shared_ptr` for shared ownership.
- Use `const` correctness throughout — mark methods and parameters `const` where possible.
- Favor value semantics over pointer/reference semantics unless polymorphism is needed.
- Use `std::vector` as the default container.
- Prefer compile-time polymorphism (templates/concepts) over runtime polymorphism (virtual).
- Use `= default` and `= delete` for special member functions explicitly.
- Keep header files minimal — prefer `.cpp` implementation details.

## Common Risks

- Object slicing when passing polymorphic types by value.
- Template bloat from excessive or unconstrained template instantiation.
- Undefined behavior from dangling references, iterator invalidation, or data races.
- Overuse of raw pointers for ownership.
- Exception safety issues in complex constructors or assignment operators.
