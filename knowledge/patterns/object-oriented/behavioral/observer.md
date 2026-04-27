# Observer

## Intent
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Use When
- A change to one object requires changing others, and you don't know how many objects need to change.
- An object should notify other objects without making assumptions about who they are.
- You want loose coupling between subjects and observers.

## Structure
- Subject maintains a list of observers and provides attach/detach methods.
- Observer defines the update interface.
- ConcreteSubject stores state of interest.
- ConcreteObserver maintains a reference to ConcreteSubject and implements the update interface.

## Heuristics
1. **Push vs pull**: Push (subject sends detailed data) vs pull (observer requests what it needs). Pull is more flexible.
2. **Avoid cascading updates**: An observer update that triggers another subject change can cause infinite loops.
3. **Weak references**: Use weak references to observers to prevent memory leaks (forgotten detach).
4. **Event-based alternatives**: Modern languages provide event/delegate mechanisms that are simpler than implementing Observer from scratch.

## Common Risks
1. **Unexpected updates**: Observers may be notified in unexpected order or at unexpected times.
2. **Performance**: Many observers can make notification slow.
3. **Memory leaks**: Forgetting to detach observers prevents garbage collection.
4. **Cascading failures**: An exception in one observer can break notification for all others.
5. **Stale data**: Observers may read state that has already changed again.

## Related Patterns
- **Mediator**: Mediator centralizes communication; Observer distributes it.
- **Singleton**: The Subject is often a Singleton.
- **Command**: Can be used to encapsulate update notifications.
