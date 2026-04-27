# Adapter

## Intent
Convert the interface of a class into another interface that clients expect. Lets classes work together that couldn't otherwise because of incompatible interfaces.

## Use When
- You want to use an existing class but its interface doesn't match what you need.
- You want to create a reusable class that cooperates with unrelated or unforeseen classes.
- You need to wrap a third-party library with a clean interface.

## Structure
- Target defines the domain-specific interface.
- Adaptee defines the existing interface that needs adapting.
- Adapter adapts the Adaptee to the Target interface.

## Forms
- **Class Adapter**: Uses inheritance (adapts one class to another).
- **Object Adapter**: Uses composition (adapts any class with the required interface).

## Heuristics
1. **Prefer object adapter (composition)**: It's more flexible — a single adapter can work with the Adaptee and all its subclasses.
2. **Keep the adapter thin**: It should only translate interface calls, not add business logic.
3. **Name clearly**: `XxxAdapter` or `XxxWrapper` makes the intent obvious.
4. **Consider bidirectional adaptation**: Sometimes you need to adapt both directions.

## Common Risks
1. **Adapter chain**: Multiple adapters wrapping each other make debugging hard.
2. **Performance overhead**: Each adapter layer adds method call overhead.
3. **Leaky abstraction**: If the Adaptee's quirks leak through the adapter, clients still depend on the Adaptee.

## Related Patterns
- **Bridge**: Similar structure but different intent. Adapter makes things work *after* design; Bridge lets them vary *independently*.
- **Facade**: Provides a simpler interface, but doesn't necessarily adapt an existing interface.
- **Proxy**: Provides the same interface for access control, not interface conversion.
