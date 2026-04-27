# State

## Intent
Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Use When
- An object's behavior depends on its state, and it must change behavior at runtime depending on that state.
- Operations have large, multipart conditional statements that depend on the object's state.
- State transitions are explicit and well-defined.

## Structure
- Context defines the interface of interest to clients and maintains a State instance.
- State defines the interface for state-specific behavior.
- ConcreteState implements state-specific behavior and handles transitions to other states.

## Heuristics
1. **State objects are often singletons**: Since state objects have no instance state of their own, they can be shared.
2. **State transitions**: Transitions can be defined in the Context or in the State classes. State-defined transitions are more flexible but create dependencies between states.
3. **Table-driven alternatives**: For simple state machines, a state transition table is simpler than the State pattern.
4. **Entry and exit actions**: Consider defining actions that execute when entering or leaving a state.

## Common Risks
1. **Class explosion**: Each state is a separate class, which can lead to many classes.
2. **State transition complexity**: Complex state machines with many transitions are hard to verify.
3. **Context-state coupling**: The Context and State classes are tightly coupled.
4. **Over-engineering**: Simple boolean flags are often sufficient for simple state-dependent behavior.

## Related Patterns
- **Strategy**: Similar structure. State changes behavior based on internal state; Strategy lets clients choose an algorithm.
- **Singleton**: State objects are often Singletons.
- **Flyweight**: State objects can be shared using Flyweight.
