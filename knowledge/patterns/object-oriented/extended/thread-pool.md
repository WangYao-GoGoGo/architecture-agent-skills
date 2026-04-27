# Thread Pool

## Intent
Manage a pool of worker threads that can execute tasks concurrently, avoiding the overhead of thread creation and destruction.

## Use When
- You need to execute many short-lived tasks concurrently.
- Thread creation overhead is significant.
- You want to limit the number of concurrent threads to prevent resource exhaustion.

## Structure
- ThreadPool maintains a collection of reusable threads.
- TaskQueue holds tasks waiting to be executed.
- WorkerThread picks tasks from the queue and executes them.

## Heuristics
1. **Right-size the pool**: Pool size depends on CPU cores and task type (CPU-bound vs I/O-bound).
2. **Use bounded queues**: An unbounded task queue can cause memory exhaustion.
3. **Rejection policy**: Define what happens when the queue is full (abort, discard, caller-runs).
4. **Monitor pool health**: Track queue depth, active threads, and task completion times.

## Common Risks
1. **Pool sizing**: Too few threads → underutilization. Too many → contention and context switching overhead.
2. **Thread starvation**: If tasks depend on each other (nested tasks), deadlock can occur.
3. **Resource leaks**: Forgotten thread pools prevent JVM/process shutdown.
4. **Unbounded growth**: Without a maximum pool size, load spikes can crash the system.

## Related Patterns
- **Object Pool**: Thread Pool is a specialized Object Pool.
- **Command**: Tasks are often Command objects.
- **Strategy**: Different scheduling strategies can be used.
