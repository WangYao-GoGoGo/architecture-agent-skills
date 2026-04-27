# Memento

## Intent
Without violating encapsulation, capture and externalize an object's internal state so the object can be restored to this state later.

## Use When
- You need to save and restore an object's state (undo/redo, checkpoints).
- Direct access to the object's state would break encapsulation.
- The state to be saved is a snapshot that should not be modified externally.

## Structure
- Originator creates a Memento containing a snapshot of its internal state.
- Memento stores the Originator's internal state (opaque to other objects).
- Caretaker requests Mementos from the Originator and stores them safely.

## Heuristics
1. **Wide vs narrow interfaces**: Memento should provide a wide interface to the Originator and a narrow (empty) interface to other objects.
2. **State size**: If the Originator has a large state, Mementos can consume significant memory.
3. **Incremental saves**: Store only the changes (delta) rather than full state snapshots.
4. **Serialization**: In practice, serialization/deserialization is often used instead of implementing Memento.

## Common Risks
1. **Large memory usage**: Storing many Mementos can consume significant memory.
2. **Encapsulation violation**: If the Memento exposes internal state, encapsulation is broken.
3. **Implementation complexity**: Supporting narrow/wide interfaces requires language support (C++ friend, package-private in Java).
4. **Serialization issues**: If using serialization, versioning and compatibility become concerns.

## Related Patterns
- **Command**: Commands can use Memento to store state for undo.
- **Prototype**: Can be used to clone state instead of creating Mementos.
- **Iterator**: Memento can save iterator state for checkpoint/resume.
