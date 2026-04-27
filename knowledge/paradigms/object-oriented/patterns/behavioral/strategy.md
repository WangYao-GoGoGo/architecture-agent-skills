# Strategy

## Intent
Define a family of algorithms, encapsulate each one, and make them interchangeable. Lets the algorithm vary independently from clients that use it.

## Use When
- Many related classes differ only in their behavior.
- You need different variants of an algorithm (performance vs memory trade-off).
- An algorithm uses data that clients shouldn't know about.
- Conditional statements choose between many related algorithms.

## Structure
- Strategy declares the interface common to all supported algorithms.
- ConcreteStrategy implements the algorithm.
- Context maintains a reference to a Strategy and may define an interface for accessing data.

## Heuristics
1. **Prefer strategy over conditionals**: If you have a switch/if-else chain selecting an algorithm, extract each branch into a Strategy.
2. **Strategies are stateless**: Strategies should not maintain state between calls. State belongs in the Context.
3. **Strategy vs State**: Strategy is selected by the client; State changes automatically based on internal conditions.
4. **Function pointers/lambdas**: In modern languages, strategies can often be passed as functions or lambdas instead of full classes.

## Common Risks
1. **Over-engineering**: If there are only 2-3 algorithms that rarely change, a simple conditional is simpler.
2. **Client awareness**: Clients must know about available strategies to choose the right one.
3. **Communication overhead**: The Context may need to pass data to the Strategy that the Strategy doesn't use.

## Related Patterns
- **State**: Similar structure. Strategy is for interchangeable algorithms; State is for state-dependent behavior.
- **Flyweight**: Strategy objects can be shared using Flyweight.
- **Decorator**: Strategy changes the guts; Decorator changes the skin.
- **Template Method**: Template Method uses inheritance; Strategy uses composition.
