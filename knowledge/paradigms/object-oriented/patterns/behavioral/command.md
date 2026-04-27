# Command

## Intent
Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## Use When
- You want to parameterize objects by an action to perform.
- You want to specify, queue, and execute requests at different times.
- You need undo/redo functionality.
- You want to log changes for auditing or recovery.

## Structure
- Command declares an interface for executing an operation.
- ConcreteCommand implements Execute and stores receiver and parameters.
- Receiver knows how to perform the actual operation.
- Invoker asks the command to carry out the request.
- Client creates ConcreteCommand and sets its receiver.

## Heuristics
1. **Separate command from receiver**: The command captures intent; the receiver performs the action.
2. **Support undo**: Store enough state in the command to reverse the operation.
3. **Composite commands**: Use macro commands that execute multiple commands in sequence.
4. **Command history**: Maintain a stack of executed commands for undo/redo.

## Common Risks
1. **Class explosion**: Each command is a separate class, which can lead to many small classes.
2. **State management**: Undo requires storing previous state, which can be memory-intensive.
3. **Command vs Strategy**: Command encapsulates a request; Strategy encapsulates an algorithm.

## Related Patterns
- **Composite**: Macro commands are Composite commands.
- **Memento**: Can be used to store state for undo.
- **Prototype**: Can be used to copy commands for queuing.
- **Observer**: Can notify when commands are executed.
