---
name: scala-functional-architecture
description: Use when reviewing Scala functional programming patterns, type class design, effect systems, and JVM architecture.
---

# Scala Functional Architecture

## When To Use
- The main decision is about type class design, effect system selection, or functional module organization.
- Reviewing `given`/`using` (Scala 3) or `implicit` (Scala 2) usage, and `for` comprehension patterns.

## Workflow
1. Identify type class design — are type classes used for cross-cutting concerns?
2. Review `given`/`using` or `implicit` usage — is implicit resolution predictable?
3. Check effect system choice — is `ZIO`, `Cats Effect`, or plain `Future` appropriate?
4. Review `for` comprehension usage — are monadic chains readable and well-structured?
5. Check algebraic data types — are `sealed trait`/`enum` used for domain modeling?
6. Review module organization — are packages organized by domain, not layer?
7. Recommend the simplest functional design.

## Output Format
```markdown
Scala functional review:
- Type class design:
- Implicit/given usage:
- Effect system:
- For comprehensions:
- ADT modeling:
- Module organization:
- Recommended change:
- Verification:
```
