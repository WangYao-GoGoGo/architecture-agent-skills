# Design Pattern Selector

Helps an agent decide whether a design pattern is justified and choose the smallest pattern that reduces real complexity.

## When To Use This Skill

- Code has repeated conditionals by type, mode, or provider.
- Object creation logic is scattered across callers.
- An external interface is incompatible with the expected contract.
- A complex subsystem needs a simpler public boundary.
- Many subscribers need to react to domain events.
- Construction has many optional parts or validation steps.

Do **not** use this skill for simple CRUD, one-off scripts, or code with only a few stable variations.

## How It Works

1. **Identify** the design pressure: creation, interface mismatch, behavior variation, communication, etc.
2. **Check** whether a simpler alternative (plain function, parameter, conditional) is sufficient.
3. **Select** the smallest pattern that addresses the pressure.
4. **Consult** the relevant knowledge card for heuristics and risks.
5. **State** the rejected alternatives explicitly.

## Knowledge Used

- [`knowledge/patterns/`](../../knowledge/patterns/README.md) — all pattern categories organized by paradigm.
- [`knowledge/patterns/object-oriented/`](../../knowledge/patterns/object-oriented/README.md) — 37 OO patterns with heuristics and risks.
- [`knowledge/patterns/procedural/`](../../knowledge/patterns/procedural/README.md) — procedural patterns for non-OO code.
- [`knowledge/patterns/functional/`](../../knowledge/patterns/functional/README.md) — functional patterns for FP code.
- [`knowledge/patterns/systems/`](../../knowledge/patterns/systems/README.md) — concurrency and systems patterns.
- [`knowledge/patterns/architecture/`](../../knowledge/patterns/architecture/README.md) — large-scale architecture patterns.

## Quick Decision Table

| Pressure | Pattern To Consider |
|---|---|
| Object creation varies | Factory Method, Abstract Factory |
| Complex construction | Builder |
| Interface mismatch | Adapter |
| Behavior varies by type | Strategy |
| Algorithm skeleton varies | Template Method |
| Many subscribers | Observer |
| Complex subsystem | Facade |
| Access control | Proxy |
| Tree structure | Composite |
| State transitions | State |
| Undoable operations | Command |

## Output

```markdown
Design pattern decision:
- Design pressure:
- Recommended pattern:
- Why it fits:
- Why simpler code is/is not enough:
- Alternatives rejected:
- Refactoring steps (if any):
- Verification:
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — to design the full structure around the chosen pattern.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to check whether the pattern is justified.
