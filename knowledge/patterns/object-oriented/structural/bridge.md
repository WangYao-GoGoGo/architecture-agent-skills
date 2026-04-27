# Bridge

## Intent
Decouple an abstraction from its implementation so that the two can vary independently.

## Use When
- You want to avoid a permanent binding between abstraction and implementation.
- Both the abstraction and implementation should be extensible by subclassing.
- Changes to the implementation should not affect clients of the abstraction.

## Structure
- Abstraction defines the high-level control interface.
- RefinedAbstraction extends the abstraction.
- Implementor defines the implementation interface.
- ConcreteImplementor implements the implementor.

## Heuristics
1. **Identify what varies**: Separate the abstraction (what) from the implementation (how).
2. **Bridge vs Adapter**: Bridge is designed upfront to allow independent variation. Adapter is retrofitted to make things work together.
3. **Use with platform independence**: Bridge is ideal for UI frameworks that need to work on multiple platforms (Windows, macOS, Linux).
4. **Keep implementor interface stable**: Changes to the implementor ripple to all abstractions.

## Common Risks
1. **Increased complexity**: The indirection makes the design harder to understand.
2. **Over-engineering**: If the abstraction and implementation don't vary independently, Bridge adds unnecessary layers.
3. **Performance**: The extra delegation layer adds method call overhead.

## Related Patterns
- **Adapter**: Similar structure. Bridge is designed upfront; Adapter is retrofitted.
- **Strategy**: Similar structure. Bridge separates abstraction from implementation; Strategy encapsulates algorithms.
- **Abstract Factory**: Can create and configure a specific Bridge implementation.
