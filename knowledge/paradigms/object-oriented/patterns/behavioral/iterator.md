# Iterator

## Intent
Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

## Use When
- You need to traverse a collection without exposing its structure.
- You want to support multiple traversal methods (forward, backward, filtered).
- You want a uniform interface for traversing different collection types.

## Structure
- Iterator defines the traversal interface (First, Next, IsDone, CurrentItem).
- ConcreteIterator implements the Iterator interface and tracks the current position.
- Aggregate defines the interface for creating an Iterator.
- ConcreteAggregate implements the Aggregate interface.

## Heuristics
1. **Use language built-in iterators**: Most modern languages have built-in iterator support (for-each, generators, iterators). Use them instead of implementing from scratch.
2. **External vs internal iterators**: External (client controls iteration) vs internal (collection controls iteration). External is more flexible.
3. **Fail-fast**: Detect concurrent modification and throw an exception.
4. **Lazy iteration**: Use generators or yield to produce elements on demand.

## Common Risks
1. **Concurrent modification**: Modifying the collection during iteration can cause undefined behavior.
2. **Performance**: Iterator allocation overhead for simple traversals.
3. **Bidirectional complexity**: Supporting both forward and backward iteration doubles the interface.

## Related Patterns
- **Composite**: Iterators are often used to traverse Composite structures.
- **Factory Method**: The Aggregate's CreateIterator method is a Factory Method.
- **Memento**: Can be used to save iterator state for checkpoint/resume.
