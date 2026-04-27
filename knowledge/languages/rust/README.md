# Rust Architecture Idioms

## Use When

- Reviewing Rust crate structure, trait bounds, ownership patterns, error handling, or async design.

## Heuristics

- Encode invariants in the type system — make illegal states unrepresentable.
- Use `Result<T, E>` for recoverable errors and `panic!` only for unrecoverable states.
- Prefer `impl Trait` in argument positions and generics with bounds for return types.
- Use `Arc<Mutex<T>>` sparingly — prefer message passing or lock-free patterns.
- Organize code into crates by boundary (domain, infrastructure, interface).
- Use `#[derive(Debug, Clone, PartialEq)]` judiciously — not every type needs them.
- Leverage the borrow checker — if it compiles, it's often correct.
- Use `async`/`await` for I/O-bound work; use threads for CPU-bound work.

## Common Risks

- Over-abstracting with traits and generics before understanding the concrete use case.
- `unwrap()`/`expect()` in production code without justification.
- Deeply nested `Rc<RefCell<...>>` or `Arc<Mutex<...>>` that obscures data flow.
- Ignoring `unsafe` blocks' soundness requirements.
- Async runtime choice (tokio vs async-std vs smol) coupling leaking into library code.
