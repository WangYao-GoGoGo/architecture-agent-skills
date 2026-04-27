# Builder

## Intent
Separate the construction of a complex object from its representation so the same construction process can create different representations.

## Use When
- An object requires many optional parameters or complex initialization.
- The construction process should allow different representations of the object.
- You want to avoid telescoping constructors (constructors with many parameters).

## Structure
- Builder declares abstract steps for building parts of a product.
- ConcreteBuilder implements the steps and returns the product.
- Director defines the order of building steps.
- Product is the complex object being built.

## Heuristics
1. **Fluent interface**: Return `this` from builder methods to enable method chaining.
2. **Immutability**: Build immutable objects by setting all fields in the builder and constructing the final object at once.
3. **Validate at build time**: Check that all required fields are set in the `build()` method.
4. **Builder vs Constructor**: Use Builder when there are 4+ parameters, especially if many are optional.

## Common Risks
1. **Builder proliferation**: Creating a Builder for every class adds boilerplate. Use only for complex construction.
2. **Forgotten calls**: The Director or client must call all required builder methods. Missing a call produces an incomplete product.
3. **Mutable builders**: If the builder is reused, ensure `build()` creates a new instance or resets state.

## Related Patterns
- **Abstract Factory**: Similar in that both create objects. Builder focuses on step-by-step construction; Abstract Factory creates families.
- **Prototype**: Alternative that clones a pre-configured object.
- **Composite**: Builder can build complex Composite structures.
