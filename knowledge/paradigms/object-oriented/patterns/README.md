# Object-Oriented Design Patterns

Reference knowledge for OO design patterns organized by category.

## Creational Patterns

Patterns that abstract object creation.

| Pattern | Intent |
|---------|--------|
| [`Singleton`](creational/singleton.md) | Ensure a class has only one instance |
| [`Factory Method`](creational/factory-method.md) | Define an interface for creating an object, let subclasses decide |
| [`Abstract Factory`](creational/abstract-factory.md) | Create families of related objects without specifying concrete classes |
| [`Builder`](creational/builder.md) | Separate construction of a complex object from its representation |
| [`Prototype`](creational/prototype.md) | Create new objects by cloning a prototype |
| [`Object Pool`](creational/object-pool.md) | Reuse objects that are expensive to create |
| [`Dependency Injection`](creational/dependency-injection.md) | Provide dependencies from outside rather than creating internally |

## Structural Patterns

Patterns that compose classes and objects.

| Pattern | Intent |
|---------|--------|
| [`Adapter`](structural/adapter.md) | Convert one interface to another |
| [`Bridge`](structural/bridge.md) | Decouple abstraction from implementation |
| [`Composite`](structural/composite.md) | Treat individual and composite objects uniformly |
| [`Decorator`](structural/decorator.md) | Add responsibilities to objects dynamically |
| [`Facade`](structural/facade.md) | Provide a unified interface to a subsystem |
| [`Flyweight`](structural/flyweight.md) | Share fine-grained objects for efficiency |
| [`Proxy`](structural/proxy.md) | Control access to another object |

## Behavioral Patterns

Patterns that define communication between objects.

| Pattern | Intent |
|---------|--------|
| [`Chain of Responsibility`](behavioral/chain-of-responsibility.md) | Pass request along a chain of handlers |
| [`Command`](behavioral/command.md) | Encapsulate a request as an object |
| [`Interpreter`](behavioral/interpreter.md) | Define grammar and interpret sentences |
| [`Iterator`](behavioral/iterator.md) | Traverse a collection without exposing its structure |
| [`Mediator`](behavioral/mediator.md) | Reduce coupling between communicating objects |
| [`Memento`](behavioral/memento.md) | Capture and restore object state |
| [`Observer`](behavioral/observer.md) | Notify dependents of state changes |
| [`State`](behavioral/state.md) | Alter behavior when internal state changes |
| [`Strategy`](behavioral/strategy.md) | Define a family of interchangeable algorithms |
| [`Template Method`](behavioral/template-method.md) | Define skeleton of algorithm, defer steps to subclasses |
| [`Visitor`](behavioral/visitor.md) | Add operations to a class hierarchy without modifying it |

## Extended Patterns

Additional patterns beyond the original GoF 23.

| Pattern | Category | Intent |
|---------|----------|--------|
| [`Null Object`](extended/null-object.md) | Behavioral | Provide a default no-op object |
| [`MVC`](extended/mvc.md) | Architectural | Separate model, view, and controller |
| [`Repository`](extended/repository.md) | Architectural | Mediate between domain and data mapping |
| [`Unit of Work`](extended/unit-of-work.md) | Architectural | Track changes to objects during a transaction |
| [`Specification`](extended/specification.md) | Architectural | Encapsulate business rules for selection |
| [`Service Locator`](extended/service-locator.md) | Architectural | Abstract service lookup |
| [`Lazy Initialization`](extended/lazy-initialization.md) | Creational | Defer object creation until needed |
| [`Double-Checked Locking`](extended/double-checked-locking.md) | Concurrency | Reduce locking overhead |
| [`Thread Pool`](extended/thread-pool.md) | Concurrency | Manage a pool of worker threads |
| [`Balking`](extended/balking.md) | Concurrency | Only execute an action when in the right state |
| [`Scheduler`](extended/scheduler.md) | Concurrency | Control task execution order |
| [`Pipeline`](extended/pipeline.md) | Architectural | Chain processing stages |

**Total: 23 GoF + 12 extended = 35 patterns**

## How To Use This Knowledge

These pattern cards are reference material for the [`skills/paradigms/object-oriented/design-pattern-selector/SKILL.md`](../../../../skills/paradigms/object-oriented/design-pattern-selector/SKILL.md) skill. When selecting a pattern:

1. Identify the **design pressure** (what problem are you solving?)
2. Check the **Use When** section of candidate patterns
3. Consider **simpler alternatives** before committing
4. Review **Common Risks** to avoid misapplication
