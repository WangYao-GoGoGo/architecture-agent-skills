# Double-Checked Locking

## Intent
Reduce the overhead of acquiring a lock by first testing the locking criterion without actually acquiring the lock. Only if the check succeeds does the lock actually become necessary.

## Use When
- You need lazy initialization in a multi-threaded context.
- The initialization code is expensive and the lock overhead matters.
- The object is read frequently but created rarely.

## Structure
- First check (without lock): test if the resource is initialized.
- Acquire lock.
- Second check (with lock): test again to handle race conditions.
- Initialize if still not initialized.
- Release lock.

## Heuristics
1. **Volatile keyword**: The shared variable must be volatile (or use atomic) to prevent instruction reordering.
2. **Language-specific solutions**: In C#, use Lazy<T>. In Java, use the holder class idiom. In Go, use sync.Once.
3. **Measure first**: Lock overhead is rarely the bottleneck. Only use this pattern if profiling shows it matters.
4. **Alternative: eager initialization**: If the object is always needed, eager initialization is simpler and thread-safe.

## Common Risks
1. **Broken without volatile**: Without proper memory barriers, the first check can see a partially constructed object.
2. **Complexity**: The pattern is subtle and easy to get wrong.
3. **Premature optimization**: Most code doesn't need this level of optimization.
4. **Platform-specific behavior**: The pattern's correctness depends on the memory model of the platform.

## Related Patterns
- **Singleton**: Often used to implement thread-safe lazy Singleton.
- **Lazy Initialization**: Double-Checked Locking is a thread-safe variant.
- **Proxy**: Can use Double-Checked Locking for thread-safe virtual proxy.
