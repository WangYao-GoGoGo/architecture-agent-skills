# Null Object

## Intent
Provide a default no-op object that implements an interface, eliminating the need for null checks.

## Use When
- You frequently check for null before calling methods.
- A default "do nothing" behavior is meaningful.
- You want to simplify client code by removing conditional checks.

## Structure
- AbstractObject declares the interface.
- RealObject implements the interface with real behavior.
- NullObject implements the interface with no-op behavior.

## Heuristics
1. **Make NullObject a singleton**: Since it has no state, a single instance can be shared.
2. **Return NullObject from methods**: Instead of returning null, return a NullObject instance.
3. **NullObject should not throw**: All methods should be safe to call and do nothing.
4. **Combine with Factory**: Have the factory return NullObject when creation fails.

## Common Risks
1. **Silent failures**: NullObjects can hide bugs by silently ignoring operations.
2. **Debugging difficulty**: It's harder to trace why nothing happened when NullObjects are used.
3. **Overuse**: Not every null check should be replaced with NullObject. Sometimes null is the correct semantic.

## Related Patterns
- **Strategy**: NullObject is a special case of Strategy.
- **State**: NullObject is similar to a no-op State.
- **Factory Method**: Can return NullObject when creation fails.
