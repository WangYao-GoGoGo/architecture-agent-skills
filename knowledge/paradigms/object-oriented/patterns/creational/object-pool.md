# Object Pool

## Intent
Reuse objects that are expensive to create by maintaining a pool of reusable instances.

## Use When
- Object creation is expensive (database connections, thread creation, large buffers).
- The number of instances needed at any time is bounded.
- Objects can be reused after being reset to a clean state.

## Structure
- ObjectPool manages a collection of reusable objects.
- PooledObject defines the reusable resource.
- Client borrows from and returns objects to the pool.

## Heuristics
1. **Reset on return**: Clean the object state when it is returned to the pool to avoid leaking state between uses.
2. **Bounded pool size**: Set a maximum pool size to prevent resource exhaustion.
3. **Timeout and eviction**: Return a timeout error if no object is available within a reasonable time. Evict stale objects.
4. **Validate on borrow**: Check that the borrowed object is still valid (e.g., database connection is alive).

## Common Risks
1. **Resource leaks**: If clients forget to return objects, the pool drains and resources are leaked.
2. **Stale objects**: Objects in the pool may become invalid over time (closed connections, expired tokens).
3. **Thread safety**: Pool operations (borrow/return) must be thread-safe, adding synchronization overhead.
4. **Pool sizing**: Too small → contention. Too large → wasted resources. Right-sizing requires profiling.

## Related Patterns
- **Singleton**: The pool itself is often a Singleton.
- **Flyweight**: Both manage shared objects. Flyweight focuses on sharing for memory; Object Pool focuses on reuse for performance.
- **Factory Method**: Can be used to create new objects when the pool is empty.
