# Lazy Initialization

## Intent
Defer the creation of an object, the calculation of a value, or some other expensive process until the first time it is needed.

## Use When
- Object creation is expensive and may not be needed.
- You want to improve startup time by deferring initialization.
- The cost of creation is high and the object is not always used.

## Structure
- LazyHolder holds a reference to the object (initially null).
- Getter checks if the object is null, creates it if so, and returns it.

## Heuristics
1. **Thread safety**: Lazy initialization in multi-threaded contexts requires synchronization (double-checked locking, Lazy<T>, synchronized).
2. **Measure first**: Only use lazy initialization if profiling shows it's needed.
3. **Lazy<T>**: In C#, use Lazy<T>. In Java, use Supplier or Holder.
4. **Resource cleanup**: Lazy-loaded resources (connections, files) must be properly disposed.

## Common Risks
1. **Thread safety bugs**: Double-checked locking without proper memory barriers can fail.
2. **First-call latency**: The first call is slow, which can cause unexpected delays.
3. **Memory leaks**: Lazy objects that are never used still hold references.
4. **Debugging difficulty**: Lazy initialization can make object creation timing unpredictable.

## Related Patterns
- **Proxy**: Virtual Proxy is a form of Lazy Initialization.
- **Singleton**: Can use Lazy Initialization for thread-safe singleton creation.
- **Factory Method**: Can implement Lazy Initialization.
