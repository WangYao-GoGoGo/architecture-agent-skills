# Decorator

## Intent
Attach additional responsibilities to an object dynamically. Provides a flexible alternative to subclassing for extending functionality.

## Use When
- You want to add responsibilities to individual objects, not to entire classes.
- You want to avoid class explosion from subclassing every combination of features.
- Responsibilities should be removable or configurable at runtime.

## Structure
- Component defines the interface for objects that can have responsibilities added.
- ConcreteComponent is the base object to which responsibilities can be added.
- Decorator maintains a reference to a Component and conforms to its interface.
- ConcreteDecorator adds specific responsibilities.

## Heuristics
1. **Keep decorators thin**: Each decorator should add exactly one responsibility.
2. **Preserve component identity**: Decorators wrap but don't replace the original object.
3. **Order matters**: The order of decorators can affect behavior (e.g., compression before encryption).
4. **Use with streams**: I/O streams are the classic example — wrap a stream with buffering, compression, encryption.

## Common Risks
1. **Many small objects**: Each decorator creates a new wrapper object, which can be confusing to debug.
2. **Type identity issues**: Decorators change the object's type, so `instanceof` checks fail.
3. **Configuration complexity**: Building the right decorator chain can be verbose.
4. **Leaky abstraction**: If decorators need to know about each other, the design breaks down.

## Related Patterns
- **Adapter**: Changes interface. Decorator extends behavior while preserving interface.
- **Composite**: Decorator can be seen as a degenerate Composite with one child.
- **Strategy**: Decorator changes the skin; Strategy changes the guts.
- **Proxy**: Similar structure. Proxy controls access; Decorator adds behavior.
