# Facade

## Intent
Provide a unified interface to a set of interfaces in a subsystem. Defines a higher-level interface that makes the subsystem easier to use.

## Use When
- You want to provide a simple interface to a complex subsystem.
- There are many dependencies between clients and the implementation classes of an abstraction.
- You want to layer your subsystem — use Facade as an entry point to each layer.

## Structure
- Facade provides a simple, unified interface.
- Subsystem classes implement the actual functionality.
- Clients interact only with the Facade.

## Heuristics
1. **Keep the Facade simple**: It should delegate to subsystem classes, not contain business logic.
2. **Multiple Facades**: A subsystem can have multiple Facades for different client needs.
3. **Facade vs Mediator**: Facade simplifies a subsystem interface. Mediator coordinates communication between objects.
4. **Backward compatibility**: Use Facade to provide a new interface while keeping old interfaces working.

## Common Risks
1. **God facade**: If the Facade knows about too many subsystems, it becomes a bottleneck.
2. **Leaky abstraction**: If clients need to bypass the Facade to access subsystem features, the Facade is too restrictive.
3. **Performance**: Every call goes through the Facade, adding a layer of indirection.

## Related Patterns
- **Adapter**: Adapter changes an interface; Facade provides a simpler interface.
- **Mediator**: Similar in that both abstract communication. Facade abstracts a subsystem; Mediator abstracts peer-to-peer communication.
- **Singleton**: A Facade is often a Singleton.
- **Abstract Factory**: Can be used with Facade to create subsystem objects.
