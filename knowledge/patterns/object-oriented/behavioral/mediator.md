# Mediator

## Intent
Define an object that encapsulates how a set of objects interact. Promotes loose coupling by keeping objects from referring to each other explicitly.

## Use When
- A set of objects communicate in well-defined but complex ways.
- Reusing an object is difficult because it references many other objects.
- Behavior distributed across several classes should be customizable without subclassing.

## Structure
- Mediator defines the interface for communication between Colleague objects.
- ConcreteMediator implements the Mediator and coordinates Colleague interactions.
- Colleague communicates with other Colleagues only through the Mediator.

## Heuristics
1. **Keep mediator focused**: The mediator should coordinate, not contain business logic.
2. **Colleague simplicity**: Colleagues should be simple and know only about the Mediator.
3. **Mediator vs Observer**: Mediator centralizes communication; Observer distributes it.
4. **Event bus**: A message bus or event aggregator is a form of Mediator.

## Common Risks
1. **God mediator**: The mediator can become a god object that knows about everything.
2. **Performance bottleneck**: All communication goes through the mediator, which can become a bottleneck.
3. **Complexity**: The mediator's coordination logic can become complex and hard to maintain.
4. **Runtime overhead**: Every interaction requires a mediator call.

## Related Patterns
- **Facade**: Facade simplifies a subsystem interface; Mediator coordinates peer objects.
- **Observer**: Mediator can use Observer to listen to colleague events.
- **Command**: Commands can be sent through a Mediator.
