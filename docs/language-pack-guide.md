# Language Pack Guide

Language packs adapt architecture guidance to language idioms and runtime constraints.

## What Belongs In A Language Pack

- module/package conventions
- type system or interface idioms
- dependency injection style
- error handling conventions
- testing conventions
- framework boundary guidance when common in the language

## What Does Not Belong

- Generic pattern explanations that belong in `knowledge/`.
- Domain-specific database/cache/frontend rules that belong in `skills/domains/`.
- Framework-specific rules that deserve `skills/frameworks/`.

## Quality Bar

A language skill should help an agent avoid translating patterns mechanically from another language.

Examples:

- **Go** may use interfaces, goroutines, channels, and explicit error returns instead of class hierarchies.
- **Rust** may use ownership, borrowing, traits, and `Result` types instead of garbage-collected patterns.
- **C++** may use RAII, templates, and smart pointers instead of manual resource management.
- **C#** may use async/await, LINQ, and dependency injection instead of thread-based concurrency.
- **Swift** may use protocol-oriented design, value types, and async/await instead of class inheritance.
- **Kotlin** may use coroutines, sealed classes, and extension functions instead of callback patterns.
- **Python** may use protocols or callables instead of heavy interface hierarchies.
- **Java** may use packages, constructor injection, and explicit interfaces where substitution matters.
- **C** may use headers, opaque structs, and explicit ownership contracts.
- **SQL** may use constraints, indexes, migrations, and query plans as architecture tools.
- **TypeScript** may use discriminated unions and generated type boundaries as architecture tools.
- **JavaScript** may need runtime validation, JSDoc, and explicit async error boundaries.
- **Shell** may need idempotency, quoting, cleanup traps, and Linux process/filesystem awareness.
- **Ruby** may use blocks, modules, and duck typing instead of rigid interface hierarchies.
- **PHP** may use PSR-4 autoloading, strict types, and constructor property promotion.
- **Scala** may use type classes, implicits/givens, and for-comprehensions for functional composition.
- **Elixir** may use OTP, GenServers, supervision trees, and pipe operators for fault-tolerant design.
- **HTML** may use semantic elements and ARIA for accessible document structure.
- **CSS** may use Grid, Flexbox, custom properties, and container queries for responsive layout.
- **Dart** may use null safety, streams, and sealed classes for Flutter application architecture.
- **GraphQL** may use schema-first design, DataLoader, and connection pagination for API architecture.
