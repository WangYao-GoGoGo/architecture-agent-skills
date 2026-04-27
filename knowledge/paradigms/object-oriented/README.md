# Object-Oriented Design

## Core Idea

Object-oriented design organizes behavior around objects that own state, rules, and collaborations. The primary mechanism is message passing between objects, with polymorphism enabling variation.

## Use When

- Domain concepts have clear behavior and invariants that should be encapsulated together.
- Variation is handled through polymorphism (subtypes, interfaces, duck typing).
- Mutable state needs to be scoped and controlled within object boundaries.
- The system benefits from a shared vocabulary that maps directly to domain objects.

## Heuristics

1. **Responsibility-driven design**: Assign each responsibility to the object that has the data needed to fulfill it. If no object fits, create one.
2. **Prefer composition over inheritance**: Use inheritance only when there is a genuine substitutable relationship (Liskov substitution). For code reuse, use composition, delegation, or traits.
3. **Keep interfaces small**: An interface should have one clear purpose (Interface Segregation Principle). Consumers should not depend on methods they don't use.
4. **Depend on abstractions, not concretions**: High-level policy should not depend on low-level details. Both should depend on abstractions (Dependency Inversion Principle).
5. **Encapsulate what varies**: Identify what changes in the system and encapsulate it behind a stable interface. This is the foundation of most design patterns.
6. **Beware of anemic models**: If objects are just data holders with no behavior, the OO model is not pulling its weight. Consider moving logic closer to the data.
7. **Law of Demeter**: An object should only talk to its immediate neighbors. Chain calls (`a.getB().getC().doSomething()`) indicate coupling to deep structure.
8. **Favor small methods with clear intent**: Methods should do one thing at one level of abstraction. Extract conditionals into named predicate methods.
9. **Open for extension, closed for modification**: Add new behavior through new classes, not by modifying existing ones. Use polymorphism rather than conditionals.
10. **Tell, don't ask**: Instead of querying an object's state and then making a decision, tell the object to perform the operation and let it decide internally.

## Common Risks

1. **God classes**: A single class that knows too much or does too much. Split by responsibility.
2. **Inheritance misuse**: Using inheritance for code reuse rather than substitutability. Leads to fragile base class problems.
3. **Interface explosion**: Too many tiny interfaces with no clear purpose. Consolidate around consumer needs.
4. **Premature abstraction**: Adding interfaces, factories, and indirection before there is a second implementation. Wait for the second case.
5. **Framework leakage**: Domain objects that depend on framework base classes, annotations, or container APIs. Keep domain pure.
6. **Deep inheritance hierarchies**: More than 2-3 levels of inheritance is usually a sign of design problems. Flatten with composition.
7. **Setter overuse**: Mutable objects with public setters for every field break encapsulation. Prefer constructor injection and immutable objects.
8. **Circular dependencies**: Two objects that depend on each other create tight coupling. Introduce an interface or mediator.

## Verification

- Can each class be described in one sentence about its single responsibility?
- Can you replace a concrete implementation with a test double without changing the consumer?
- Are all inheritance relationships substitutable (Liskov)?
- Do domain objects contain behavior, or are they just data containers?
- Can you add a new variant without modifying existing code (Open/Closed)?
- Are there any circular dependencies between packages or modules?
- Do method signatures reveal internal state or implementation details?

## Design Patterns Reference

All 35 OO design patterns are documented under [`patterns/`](patterns/):

- **Creational** (7): [`Singleton`](patterns/creational/singleton.md), [`Factory Method`](patterns/creational/factory-method.md), [`Abstract Factory`](patterns/creational/abstract-factory.md), [`Builder`](patterns/creational/builder.md), [`Prototype`](patterns/creational/prototype.md), [`Object Pool`](patterns/creational/object-pool.md), [`Dependency Injection`](patterns/creational/dependency-injection.md)
- **Structural** (7): [`Adapter`](patterns/structural/adapter.md), [`Bridge`](patterns/structural/bridge.md), [`Composite`](patterns/structural/composite.md), [`Decorator`](patterns/structural/decorator.md), [`Facade`](patterns/structural/facade.md), [`Flyweight`](patterns/structural/flyweight.md), [`Proxy`](patterns/structural/proxy.md)
- **Behavioral** (11): [`Chain of Responsibility`](patterns/behavioral/chain-of-responsibility.md), [`Command`](patterns/behavioral/command.md), [`Interpreter`](patterns/behavioral/interpreter.md), [`Iterator`](patterns/behavioral/iterator.md), [`Mediator`](patterns/behavioral/mediator.md), [`Memento`](patterns/behavioral/memento.md), [`Observer`](patterns/behavioral/observer.md), [`State`](patterns/behavioral/state.md), [`Strategy`](patterns/behavioral/strategy.md), [`Template Method`](patterns/behavioral/template-method.md), [`Visitor`](patterns/behavioral/visitor.md)
- **Extended** (12): [`Null Object`](patterns/extended/null-object.md), [`MVC`](patterns/extended/mvc.md), [`Repository`](patterns/extended/repository.md), [`Unit of Work`](patterns/extended/unit-of-work.md), [`Specification`](patterns/extended/specification.md), [`Service Locator`](patterns/extended/service-locator.md), [`Lazy Initialization`](patterns/extended/lazy-initialization.md), [`Double-Checked Locking`](patterns/extended/double-checked-locking.md), [`Thread Pool`](patterns/extended/thread-pool.md), [`Balking`](patterns/extended/balking.md), [`Scheduler`](patterns/extended/scheduler.md), [`Pipeline`](patterns/extended/pipeline.md)

Use the [`skills/paradigms/object-oriented/design-pattern-selector/SKILL.md`](../../../skills/paradigms/object-oriented/design-pattern-selector/SKILL.md) skill to select the right pattern for a given design pressure.
