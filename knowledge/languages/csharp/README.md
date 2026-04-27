# C# Architecture Idioms

## Use When

- Reviewing C# class design, async patterns, LINQ queries, dependency injection, or .NET project structure.

## Heuristics

- Prefer `async Task` / `async ValueTask` over synchronous blocking in I/O-bound code.
- Use LINQ for in-memory queries but be mindful of deferred execution and multiple enumeration.
- Favor constructor injection over property injection for required dependencies.
- Use records for immutable data transfer objects.
- Prefer `IReadOnlyList<T>` / `IReadOnlyCollection<T>` over `List<T>` for public APIs.
- Use `sealed` classes by default unless inheritance is explicitly designed for.
- Keep `using` scopes narrow — dispose resources as early as possible.
- Use `Span<T>` and `Memory<T>` for high-performance scenarios.

## Common Risks

- Capturing mutable variables in closures/lambdas leading to unexpected behavior.
- Mixing `async void` (fire-and-forget) with `async Task` (awaitable).
- LINQ deferred execution causing multiple database round-trips (with EF Core).
- Overusing `dynamic` or `object` instead of generics or interfaces.
- Thread safety issues with static mutable state in ASP.NET Core applications.
