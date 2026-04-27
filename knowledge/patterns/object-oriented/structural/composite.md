# Composite

## Intent
Compose objects into tree structures to represent part-whole hierarchies. Lets clients treat individual objects and compositions uniformly.

## Use When
- You want to represent hierarchical part-whole relationships.
- Clients should be able to ignore the difference between compositions of objects and individual objects.
- The structure can have arbitrary depth.

## Structure
- Component declares the interface for all objects in the composition.
- Leaf represents leaf objects with no children.
- Composite stores child components and implements child-related operations.

## Heuristics
1. **Uniform interface**: Both Leaf and Composite should implement the same Component interface.
2. **Child management**: Decide whether to put child management methods (add, remove) in Component or Composite.
3. **Safety vs Transparency**: Safety = child methods in Composite only (type-safe). Transparency = child methods in Component (uniform but runtime checks).
4. **Caching**: Composite can cache computed results (e.g., total size) and invalidate when children change.

## Common Risks
1. **Overly general interface**: Component interface may become too broad to support both Leaf and Composite.
2. **Performance**: Traversing deep trees can be expensive. Consider caching or flattening.
3. **Circular references**: A Composite should not contain itself directly or indirectly.

## Related Patterns
- **Decorator**: Often used with Composite — decorators wrap components to add behavior.
- **Visitor**: Can be used to apply operations across a Composite structure.
- **Iterator**: Can traverse a Composite structure.
- **Flyweight**: Can share leaf nodes to reduce memory.
