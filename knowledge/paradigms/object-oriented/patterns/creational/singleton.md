# Singleton

## Intent
Ensure a class has only one instance and provide a global point of access to it.

## Use When
- Exactly one instance of a class is needed (logging, configuration, thread pool, connection pool).
- The single instance must be accessible from a well-known access point.
- You want to control access to a shared resource.

## Structure
- Private constructor
- Static method that returns the single instance
- Static variable holding the instance
- Optional: thread-safe initialization (lazy or eager)

## Heuristics
1. **Prefer dependency injection over Singleton**: DI makes dependencies explicit and testable. Singleton hides dependencies.
2. **Use lazy initialization only if construction is expensive**: Otherwise, eager initialization is simpler and thread-safe by default.
3. **Thread safety**: In Java/C#, use `synchronized` or `static inner class` or `enum`. In Go, use `sync.Once`.
4. **Keep Singleton scope narrow**: Application-wide singletons are often a sign of poor design. Consider request-scoped or session-scoped instances instead.

## Common Risks
1. **Hidden coupling**: Consumers depend on the Singleton directly, making it hard to replace or test.
2. **Global state**: Singletons are essentially global variables, making code harder to reason about.
3. **Testing difficulty**: Singletons are hard to mock or reset between tests.
4. **Thread safety bugs**: Double-checked locking without proper memory barriers can fail.

## Related Patterns
- **Factory Method**: Can create the Singleton instance.
- **Monostate**: Alternative that makes all instances share the same state.
- **Dependency Injection**: Preferred alternative that avoids global state.
