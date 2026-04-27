# Abstract Factory

## Intent
Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

## Use When
- A system should be independent of how its products are created.
- A system should be configured with one of multiple families of products.
- Related product objects are designed to be used together.

## Structure
- AbstractFactory declares creation methods for each product type.
- ConcreteFactory implements creation methods for a specific variant.
- AbstractProduct declares interface for a product type.
- ConcreteProduct implements a product variant.

## Heuristics
1. **Add products sparingly**: Adding a new product type requires changing the AbstractFactory interface and all ConcreteFactories.
2. **Use with dependency injection**: Inject the AbstractFactory rather than letting clients create it.
3. **Combine with Factory Method**: Each creation method in AbstractFactory is typically a Factory Method.
4. **Test with mock factories**: Create a test-only ConcreteFactory that returns test doubles.

## Common Risks
1. **Rigid interface**: Adding a new product type requires changing all factory implementations.
2. **Over-engineering**: If you only have one product family, Abstract Factory adds unnecessary complexity.
3. **Complexity**: The indirection can make it hard to trace which concrete class is being created.

## Related Patterns
- **Factory Method**: Abstract Factory is often implemented with Factory Methods.
- **Singleton**: A ConcreteFactory is often a Singleton.
- **Prototype**: Alternative that uses cloning instead of factory methods.
