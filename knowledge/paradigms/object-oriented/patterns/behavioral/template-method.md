# Template Method

## Intent
Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Lets subclasses redefine certain steps without changing the algorithm's structure.

## Use When
- You want to implement the invariant parts of an algorithm once and let subclasses define the variant parts.
- You want to control when and how subclass extensions are called (Hollywood Principle: "Don't call us, we'll call you").
- Common behavior among subclasses should be factored to avoid duplication.

## Structure
- AbstractClass defines the template method (the algorithm skeleton) and abstract primitive operations.
- ConcreteClass implements the primitive operations.

## Heuristics
1. **Keep primitive operations small**: Each primitive operation should be a single, well-defined step.
2. **Hook operations**: Add optional hook methods that subclasses can override but don't have to.
3. **Template method should be non-virtual**: The template method itself should not be overridable (final/ sealed).
4. **Minimize primitive operations**: Too many primitive operations make subclassing burdensome.

## Common Risks
1. **Inheritance coupling**: Template Method uses inheritance, which creates tight coupling between base and subclass.
2. **Fragile base class**: Changes to the template method or primitive operations can break all subclasses.
3. **Subclass explosion**: Each variation requires a new subclass.
4. **Violation of Liskov**: If a subclass changes the algorithm structure, it violates the intent.

## Related Patterns
- **Strategy**: Strategy uses composition; Template Method uses inheritance. Strategy is more flexible.
- **Factory Method**: Factory Method is a specialization of Template Method.
- **Adapter**: Can be implemented with Template Method.
