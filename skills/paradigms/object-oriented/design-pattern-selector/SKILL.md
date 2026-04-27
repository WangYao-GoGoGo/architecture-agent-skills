---
name: oo-design-pattern-selector
description: Use when selecting object-oriented design patterns such as Strategy, Factory Method, Abstract Factory, Builder, Adapter, Facade, Observer, Command, or Template Method.
---

# OO Design Pattern Selector

Use this skill for OO-specific pattern choices. For broader cross-paradigm selection, use the core design-pattern-selector.

## Knowledge To Use

- [`knowledge/paradigms/object-oriented/patterns/`](../../../knowledge/paradigms/object-oriented/patterns/) — full reference for all 35 patterns (7 creational, 7 structural, 11 behavioral, 12 extended)
- [`knowledge/paradigms/object-oriented/`](../../../knowledge/paradigms/object-oriented/) — OO design heuristics and common risks
- [`knowledge/paradigms/cross-paradigm/`](../../../knowledge/paradigms/cross-paradigm/) — paradigm comparison when the pattern crosses paradigms

## Workflow

1. **Identify the design pressure**: What problem are you solving?
   - **Creation**: Who creates objects? → Singleton, Factory Method, Abstract Factory, Builder, Prototype, Object Pool, Dependency Injection
   - **Interface mismatch**: How to make incompatible interfaces work? → Adapter, Bridge, Facade
   - **Behavior variation**: How to vary behavior? → Strategy, State, Template Method
   - **Object composition**: How to compose objects? → Composite, Decorator
   - **Communication**: How do objects communicate? → Observer, Mediator, Chain of Responsibility, Command
   - **Access control**: How to control access? → Proxy, Service Locator
   - **Data access**: How to persist and retrieve? → Repository, Unit of Work, Specification
   - **State management**: How to manage state? → Memento, State, Balking
   - **Traversal**: How to traverse collections? → Iterator, Visitor
   - **Concurrency**: How to manage threads? → Thread Pool, Double-Checked Locking, Scheduler
2. **Check whether simple OO code is enough**: Before applying a pattern, verify that a simpler solution (conditional, function, inline code) won't suffice.
3. **Select at most one primary pattern**: Avoid combining multiple patterns unless there is clear justification.
4. **Consult the pattern knowledge card**: Read the Intent, Use When, Heuristics, and Common Risks for the candidate pattern.
5. **State rejected alternatives**: Document which patterns were considered and why they were rejected.

## Output Format

```markdown
OO pattern recommendation:
- Pressure:
- Pattern:
- Why it fits:
- Simpler alternative:
- Rejected alternatives:
- Refactoring steps:
- Verification:
```
