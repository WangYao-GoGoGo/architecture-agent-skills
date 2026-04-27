# Prototype

## Intent
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## Use When
- Classes to instantiate are specified at runtime (dynamic loading).
- Building many instances of a class that differ only in a few configurations.
- Avoiding subclassing of a factory class to create products.
- Object creation is expensive and you want to avoid re-initialization.

## Structure
- Prototype declares a `clone()` method.
- ConcretePrototype implements `clone()`.
- Client creates new objects by calling `clone()` on a prototype.

## Heuristics
1. **Deep vs shallow copy**: Decide whether the clone should be deep (copy referenced objects) or shallow (share references). Document this clearly.
2. **Use a prototype registry**: Store a map of pre-configured prototypes that clients can clone.
3. **Clone with configuration**: Allow setting some properties after cloning to customize the copy.
4. **Language support**: Java's `Cloneable`, C# `ICloneable`, JavaScript `Object.assign()` / spread operator.

## Common Risks
1. **Deep copy complexity**: Objects with complex object graphs are hard to deep-copy correctly.
2. **Circular references**: Cloning objects with circular references requires special handling.
3. **Broken encapsulation**: The `clone()` method must access the internals of the object being cloned.
4. **Overuse**: Simple object creation with `new` is usually clearer than cloning.

## Related Patterns
- **Abstract Factory**: Can use Prototype instead of Factory Methods.
- **Composite**: Prototype can be used to clone complex Composite structures.
- **Decorator**: Prototype can help create decorated objects without re-applying decorators.
