# Balking

## Intent
Only execute an action on an object when the object is in a particular state. If the object is not in the right state, the action is ignored (balked).

## Use When
- An operation should only be performed when the object is in a specific state.
- The operation is called frequently but should only execute when conditions are right.
- You want to avoid blocking or waiting.

## Structure
- GuardedObject has a state and methods that check the state before executing.
- Client calls the method; if the state is wrong, the method returns immediately.

## Heuristics
1. **Fail silently or notify**: Decide whether balking should be silent or return a status.
2. **Combine with State pattern**: State can manage the conditions for balking.
3. **Thread safety**: State checks must be atomic in multi-threaded contexts.
4. **Log balking**: In debugging, log when operations balk to understand behavior.

## Common Risks
1. **Silent failures**: Balking can hide problems if the caller expects the operation to succeed.
2. **Stale state**: The state may change between the check and the action.
3. **Overuse**: Not every precondition check should use Balking. Sometimes blocking or queuing is better.

## Related Patterns
- **State**: Balking can be implemented using State.
- **Guarded Suspension**: Balking returns immediately; Guarded Suspension waits.
- **Strategy**: Different balking strategies can be used.
