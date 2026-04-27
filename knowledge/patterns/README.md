# Patterns

Pattern cards describe reusable structures that may reduce change cost. They are not prescriptions.

## Selection Rule

Use a pattern only when it improves readability, testability, substitution, or change isolation for a current or credible near-term problem.

## Categories

### Object-Oriented Patterns

GoF 23 + 12 extended patterns for class and object composition.

| Category | Count | Directory |
|----------|-------|-----------|
| Creational | 7 | [`object-oriented/creational/`](object-oriented/creational/) |
| Structural | 7 | [`object-oriented/structural/`](object-oriented/structural/) |
| Behavioral | 11 | [`object-oriented/behavioral/`](object-oriented/behavioral/) |
| Extended | 12 | [`object-oriented/extended/`](object-oriented/extended/) |

Full index: [`object-oriented/README.md`](object-oriented/README.md) (35 patterns total)

### Procedural Patterns

Reusable structures for procedural and data-oriented code.

| Pattern | Use Case |
|---------|----------|
| Layered Module | Organize code into strict dependency layers |
| Callback / Handler Chain | Sequential processing with pluggable steps |
| State Machine | Explicit state transitions and guarded actions |
| Data-Oriented Design | Organize data for cache-friendly access |
| Table-Driven Logic | Replace conditionals with lookup tables |
| Stepwise Refinement | Decompose functions by abstraction level |

Full index: [`procedural/README.md`](procedural/README.md)

### Functional Patterns

Reusable structures for functional and declarative code.

| Pattern | Use Case |
|---------|----------|
| Functor | Map a function over a wrapped value |
| Monad | Chain computations with context (Maybe, Either, IO) |
| Applicative | Apply a wrapped function to a wrapped value |
| Lens | Immutable access and update of nested data |
| Currying | Transform multi-argument functions into chains |
| Pattern Matching | Dispatch based on data structure shape |
| Algebraic Data Types | Model data with sum and product types |
| Pure Pipeline | Compose pure transformations end-to-end |

Full index: [`functional/README.md`](functional/README.md)

### Systems & Concurrency Patterns

Reusable structures for low-level, concurrent, and resource-managed code.

| Pattern | Use Case |
|---------|----------|
| RAII | Bind resource lifetime to scope |
| Resource Pool | Reuse limited resources efficiently |
| Buffer Management | Control allocation and reuse of buffers |
| Zero-Copy | Minimize data copying between layers |
| Lock-Free Structure | Concurrent access without locks |
| Actor Model | Isolated state with message passing |
| Reactor / Proactor | Event-driven I/O demultiplexing |
| Scheduler | Control task execution order and preemption |
| Thread Pool | Manage worker thread lifecycle |

Full index: [`systems/README.md`](systems/README.md)

### Architecture Patterns

Reusable structures for system-level organization.

| Pattern | Use Case |
|---------|----------|
| Layered Architecture | Strict dependency layers (presentation → domain → data) |
| Hexagonal Architecture | Isolate core logic from infrastructure |
| CQRS | Separate read and write models |
| Event Sourcing | Store state as a sequence of events |
| Saga | Manage distributed transactions |
| Pipes and Filters | Process data through sequential stages |
| Event-Driven Architecture | Decoupled communication via events |
| Microkernel | Minimal core with pluggable extensions |

Full index: [`architecture/README.md`](architecture/README.md)

## Related Resources

- [`knowledge/paradigms/`](../paradigms/) — paradigm-specific heuristics and design guidance
- [`knowledge/principles/`](../principles/) — SOLID, GRASP, and other design principles
- [`skills/paradigms/object-oriented/design-pattern-selector/SKILL.md`](../../skills/paradigms/object-oriented/design-pattern-selector/SKILL.md) — skill for selecting OO patterns
- [`skills/core/design-pattern-selector/SKILL.md`](../../skills/core/design-pattern-selector/SKILL.md) — cross-paradigm pattern selection skill
