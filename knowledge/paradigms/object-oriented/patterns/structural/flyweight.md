# Flyweight

## Intent
Use sharing to support large numbers of fine-grained objects efficiently.

## Use When
- An application uses a large number of objects.
- Storage costs are high because of the quantity of objects.
- Most object state can be made extrinsic (externalized).
- The identity of objects does not matter (shared objects are indistinguishable).

## Structure
- Flyweight declares the interface through which flyweights can receive and act on extrinsic state.
- ConcreteFlyweight implements the Flyweight interface and stores intrinsic state (shared).
- FlyweightFactory creates and manages flyweight objects.
- Client stores extrinsic state and passes it to flyweight objects.

## Heuristics
1. **Separate intrinsic from extrinsic state**: Intrinsic state is shared (stored in Flyweight). Extrinsic state is context-dependent (passed by client).
2. **Use a factory**: FlyweightFactory ensures that flyweights are shared properly.
3. **Compute extrinsic state**: If extrinsic state can be computed from context, don't store it.
4. **Measure before using**: Flyweight adds complexity. Only use it when object count is in the thousands or more.

## Common Risks
1. **Premature optimization**: Flyweight adds complexity. Profile first to confirm memory is a problem.
2. **Thread safety**: Shared flyweight objects must be thread-safe if accessed from multiple threads.
3. **Extrinsic state management**: Clients must manage extrinsic state, which can be error-prone.
4. **Performance trade-off**: Computation of extrinsic state may offset memory savings.

## Related Patterns
- **Composite**: Flyweights are often leaf nodes in a Composite structure.
- **Singleton**: FlyweightFactory is often a Singleton.
- **State**: State objects are often shared using Flyweight.
