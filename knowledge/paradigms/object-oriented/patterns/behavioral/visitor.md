# Visitor

## Intent
Represent an operation to be performed on the elements of an object structure. Lets you define a new operation without changing the classes of the elements on which it operates.

## Use When
- An object structure contains many classes with different interfaces, and you want to perform operations that depend on their concrete classes.
- Many distinct and unrelated operations need to be performed on objects in a structure.
- The classes defining the object structure rarely change, but you often want to add new operations.

## Structure
- Visitor declares a Visit operation for each ConcreteElement type.
- ConcreteVisitor implements each Visit operation.
- Element declares an Accept operation that takes a Visitor.
- ConcreteElement implements Accept.

## Heuristics
1. **Double dispatch**: Visitor achieves double dispatch — the operation depends on both the Visitor type and the Element type.
2. **Element stability**: Visitor works best when the Element hierarchy is stable (few new element types).
3. **Visitor vs Iterator**: Iterator traverses; Visitor operates. They can be combined.
4. **Acyclic Visitor**: For extensible element hierarchies, use Acyclic Visitor to avoid coupling.

## Common Risks
1. **Adding new elements**: Adding a new ConcreteElement requires changing all Visitors.
2. **Encapsulation violation**: Visitors often need access to element internals, breaking encapsulation.
3. **Complexity**: The double dispatch mechanism adds complexity.
4. **Cyclic dependencies**: Visitors and elements can create circular package dependencies.

## Related Patterns
- **Composite**: Visitors are often used to traverse and operate on Composite structures.
- **Iterator**: Can be combined with Visitor to traverse and operate.
- **Interpreter**: Visitor can define operations on an Interpreter's syntax tree.
