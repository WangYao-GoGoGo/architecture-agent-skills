# Procedural Design

## Core Idea

Procedural design organizes code around functions, modules, and explicit data flow. Unlike object-oriented design, behavior and data are separated — functions operate on data structures passed as parameters.

## Use When

- The problem is a straightforward sequence of steps or a data transformation pipeline.
- The language does not have strong OO support (C, assembly, early scripting).
- Performance and predictable memory layout are critical (embedded, kernel, game engines).
- The team is more comfortable with a flat, explicit control flow.
- The system is small enough that OO abstraction overhead is not justified.

## Heuristics

1. **Separate pure calculation from I/O**: Functions that compute results from inputs should not perform I/O. Isolate side effects at the edges of the system.
2. **Group functions by data ownership**: Functions that operate on the same data structure should live in the same module. This creates implicit cohesion.
3. **Keep module interfaces narrow**: Each module should expose a small, stable set of functions. Hide internal helpers and data structures.
4. **Pass data explicitly**: Avoid global state. Pass all required data as function parameters. If parameter lists grow too long, group related data into a struct.
5. **One level of abstraction per function**: A function should either orchestrate high-level steps or implement a low-level detail, not both.
6. **Use return values, not output parameters**: Prefer returning results rather than modifying pointers/references passed in. This makes data flow visible.
7. **Fail fast and early**: Check preconditions at the top of each function. Return error codes or use a consistent error handling strategy.
8. **Limit function length**: If a function exceeds 20-30 lines, it likely mixes multiple responsibilities. Extract helper functions.
9. **Use consistent naming conventions**: Function names should indicate what they do (`compute_total`, `validate_input`, `write_record`). Module names should indicate what they own.
10. **Document data flow explicitly**: In procedural code, the data flow is not implicit (as in OO). Use comments or clear naming to show how data moves through the system.

## Common Risks

1. **Global state**: Mutable global variables create hidden dependencies and make testing and reasoning difficult. Pass state explicitly.
2. **Long functions**: Functions that span hundreds of lines mix multiple responsibilities and hide side effects. Extract aggressively.
3. **Hidden side effects**: A function that modifies global state, writes to a file, or changes a parameter without clear indication. Make side effects visible in the function name or signature.
4. **Weak module boundaries**: Modules that expose too many internal functions or data structures create coupling. Keep the public API small.
5. **Copy-paste duplication**: Without OO polymorphism, procedural code often duplicates logic across similar functions. Extract shared logic into helper functions.
6. **Tight coupling via shared structs**: When many modules depend on the same data structure, changes ripple across the system. Define stable data contracts.
7. **No error handling strategy**: Inconsistent error handling (mix of return codes, exceptions, and halting) makes the system unreliable. Choose one strategy and apply it consistently.
8. **Parameter explosion**: Functions with 6+ parameters indicate missing abstraction. Group related parameters into a struct.

## Verification

- Can every function be described in one sentence about what it does?
- Are all side effects visible from the function signature or name?
- Is global state eliminated or strictly scoped to a single module?
- Can you test each pure function without setting up external state?
- Are module boundaries stable — can you change one module's internals without affecting others?
- Is error handling consistent across all functions?
- Can you trace the data flow from input to output without reading the entire file?
