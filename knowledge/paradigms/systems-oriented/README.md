# Systems-Oriented Design

## Core Idea

Systems-oriented design focuses on resource ownership, memory, concurrency, lifecycle, failure, and operational behavior.

## Use When

- Designing or reviewing C/C++/Rust-style low-level modules.
- Working with networking, storage, runtime, and infrastructure code.
- Building high-performance or failure-sensitive systems.
- Reviewing resource ownership, cleanup paths, and shutdown sequences.

## Heuristics

- Make ownership explicit: every resource should have a clear owner and a deterministic cleanup path.
- Separate initialization, steady-state operation, and teardown into distinct phases.
- Document concurrency assumptions: what can run in parallel, what must be serialized, and what protects shared state.
- Treat failure as a first-class state: define what happens when any operation fails, not just the happy path.
- Prefer compile-time guarantees (types, ownership, borrowing) over runtime checks where the language supports them.
- Keep unsafe blocks small, documented, and reviewed.
- Use error types that distinguish recoverable from unrecoverable failures.
- Add observability (logs, metrics, traces) at module boundaries, not inside every function.
- Design for testability at the module boundary: inject dependencies, mock hardware or network interfaces.

## Common Risks

- Hidden ownership rules that are not documented or enforced by the type system.
- Unsafe shared state accessed without clear synchronization contracts.
- Unclear cleanup and shutdown paths, leading to resource leaks or partial teardown.
- Missing observability for failure modes, making production incidents hard to diagnose.
- Over-engineering: adding abstractions (async runtimes, lock-free structures) before profiling proves they are needed.
