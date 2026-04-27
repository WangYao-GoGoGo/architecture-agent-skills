# Fortran Architecture Idioms

## Use When

- Reviewing Fortran code for numerical simulation, array operations, or HPC application architecture.

## Heuristics

- Use `implicit none` in every program unit to force explicit variable declaration.
- Use modules (`module`/`end module`) for encapsulation — use `private`/`public` attributes.
- Use `allocatable` arrays for dynamic memory — they are automatically deallocated.
- Use `do concurrent` for loop-level parallelism (Fortran 2008+).
- Use `interface` blocks for explicit procedure interfaces.
- Use `derived types` for structured data — use `type`/`end type`.
- Use `contains` for module procedures to access module-level data.
- Use `intent(in)`, `intent(out)`, `intent(inout)` for all dummy arguments.

## Common Risks

- Array index out of bounds without runtime bounds checking.
- Common block usage causing hidden data dependencies.
- Mixing single and double precision causing numerical accuracy issues.
- Non-portable extensions tied to specific compiler implementations.
- Memory leaks from `pointer` usage without proper deallocation.
