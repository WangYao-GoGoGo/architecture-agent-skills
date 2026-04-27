# Unit of Work

## Intent
Maintain a list of objects affected by a business transaction and coordinate the writing out of changes and the resolution of concurrency problems.

## Use When
- You need to track changes to objects during a transaction.
- You want to batch multiple changes into a single database transaction.
- You need to coordinate object persistence across multiple repositories.

## Structure
- UnitOfWork maintains lists of new, dirty, and removed objects.
- Repository uses UnitOfWork to register changes.
- UnitOfWork commits all changes in a single transaction.

## Heuristics
1. **Register changes automatically**: Use change tracking (snapshot comparison or AOP) rather than requiring manual registration.
2. **One UnitOfWork per transaction**: Scope the UnitOfWork to a single business transaction (often per HTTP request).
3. **Commit at the end**: Collect all changes and commit them atomically.
4. **Rollback on failure**: If any change fails, roll back all changes.

## Common Risks
1. **Long-running units**: Keeping a UnitOfWork open for too long increases contention and memory usage.
2. **Stale data**: Objects in the UnitOfWork may become stale if other processes modify the same data.
3. **Complexity**: Change tracking adds complexity, especially for large object graphs.
4. **Nested units**: Handling nested UnitOfWork scopes is complex.

## Related Patterns
- **Repository**: UnitOfWork coordinates multiple Repositories.
- **Identity Map**: Ensures each object is loaded once per UnitOfWork.
- **Memento**: Can be used to store original state for change detection.
