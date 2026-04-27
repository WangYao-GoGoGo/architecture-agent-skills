# Factory Method

## Intent
Define an interface for creating an object, but let subclasses decide which class to instantiate.

## Use When
- A class cannot anticipate the class of objects it must create.
- A class wants its subclasses to specify the objects it creates.
- You want to localize the logic of which class to instantiate.

## Structure
- Creator (abstract or base class) declares the factory method.
- ConcreteCreator overrides the factory method to return a ConcreteProduct.
- Product defines the interface of objects the factory method creates.

## Heuristics
1. **Name factory methods clearly**: `createX()`, `makeX()`, `newX()` — avoid generic `getInstance()`.
2. **Keep factory methods simple**: They should just instantiate and return. Complex logic belongs elsewhere.
3. **Parameterized factory methods**: Pass a parameter to decide which concrete class to create, but prefer separate factory methods for clarity.
4. **Factory Method vs Abstract Factory**: Factory Method is a single method on a class. Abstract Factory is an object with multiple factory methods.

## Common Risks
1. **Overuse**: Creating a factory method for every class adds unnecessary indirection. Use only when the concrete type varies.
2. **Class explosion**: Each new product variant requires a new ConcreteCreator subclass.
3. **Testing**: Factory methods can be harder to mock than constructor injection.

## Related Patterns
- **Abstract Factory**: Often implemented with Factory Methods.
- **Template Method**: Factory Method is a specialization of Template Method.
- **Prototype**: Alternative that avoids subclassing the creator.
