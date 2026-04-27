# Systems & Concurrency Patterns

Reusable structures for low-level, concurrent, and resource-managed code. These patterns apply when the primary concerns are memory management, thread safety, and hardware interaction.

## Patterns

| Pattern | Intent |
|---------|--------|
| **RAII (Resource Acquisition Is Initialization)** | Bind resource lifetime to scope; release is automatic on scope exit |
| **Resource Pool** | Maintain a pool of reusable resources (connections, buffers, threads) to avoid allocation overhead |
| **Buffer Management** | Control allocation, reuse, and recycling of memory buffers to reduce fragmentation |
| **Zero-Copy** | Minimize data copying by passing references or ownership between layers |
| **Lock-Free Structure** | Design concurrent data structures that progress without mutual exclusion locks |
| **Actor Model** | Isolate state within lightweight actors that communicate only through message passing |
| **Reactor** | Demultiplex and dispatch I/O events synchronously |
| **Proactor** | Demultiplex and dispatch I/O events asynchronously using completion callbacks |
| **Scheduler** | Control task execution order, preemption, and priority |
| **Thread Pool** | Manage a fixed set of worker threads to execute tasks without per-task thread creation |
| **Read-Write Lock** | Allow concurrent reads but exclusive writes to shared state |
| **Barrier** | Synchronize multiple threads at a specific point before proceeding |

## Use When

- The primary language provides manual memory management (C, C++, Rust, Zig)
- Performance requirements demand fine-grained control over allocation and concurrency
- The system interacts directly with hardware, OS primitives, or real-time constraints
- Predictable latency and resource usage are critical requirements

## Related Knowledge

- [`knowledge/paradigms/systems-oriented/`](../../paradigms/systems-oriented/) — systems-oriented design heuristics and risks
- [`knowledge/languages/rust/`](../../languages/rust/) — Rust ownership and borrowing patterns
- [`knowledge/languages/c/`](../../languages/c/) — C memory and concurrency patterns
- [`skills/paradigms/systems/systems-boundary-review/SKILL.md`](../../../skills/paradigms/systems/systems-boundary-review/SKILL.md) — skill for reviewing systems boundaries
