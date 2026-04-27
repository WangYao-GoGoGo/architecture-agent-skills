---
name: architecture-before-coding
description: Use before implementing a new feature or non-trivial code change when the agent should design responsibilities, boundaries, interfaces, data flow, and verification before writing code. Especially useful for object-oriented Java or Python work, backend services, domain logic, and changes likely to grow over time.
---

# Architecture Before Coding

Use this skill before writing new code or making a broad feature change. The goal is to prevent large unstructured code generation by forcing a small architecture pass first.

## When To Use

- The user asks for a new feature with multiple responsibilities.
- The change touches domain logic, persistence, APIs, workflows, or integrations.
- The code may need extension points later.
- The implementation could become a long method, god class, large conditional, or tangled dependency graph.

Do not use this skill for tiny edits, simple bug fixes, formatting, or one-line changes.

## Workflow

1. Inspect the existing codebase and identify local conventions.
2. State the feature goal in one or two sentences.
3. Identify responsibilities and assign an owner for each one.
4. Define boundaries: public interfaces, internal helpers, data models, external services, persistence, and side effects.
5. Decide whether a known pattern is justified. If unsure, prefer the simpler structure.
6. Propose the smallest implementation sequence that keeps behavior verifiable.
7. Implement in small steps and verify with existing tests or focused checks.

## Knowledge To Use

- `knowledge/architecture/application-styles/` for in-process application structure.
- `knowledge/architecture/integration-patterns/` when events, async workflows, gateways, or read/write model separation are involved.
- `knowledge/architecture/distributed-systems/` when service boundaries or deployment units are involved.
- `knowledge/principles/` and `knowledge/patterns/` for responsibility and pattern decisions.

## Design Checklist

- What is the domain concept?
- Which class, module, or service owns the core rule?
- Which dependencies point inward, and which point outward?
- What should be mocked or substituted in tests?
- What future change is likely, and is it worth designing for now?
- Which abstraction would be harmful if the feature never grows?

## Pattern Selection Rules

- Use Strategy when behavior varies by type, mode, policy, or provider.
- Use Factory Method or Abstract Factory when object creation varies and callers should not know concrete classes.
- Use Builder when construction has many optional parts or validation steps.
- Use Adapter when integrating an incompatible external interface.
- Use Facade when callers need a simpler boundary over a complex subsystem.
- Use Observer when many subscribers react to domain events.
- Use Template Method only when the algorithm skeleton is stable and subclasses fill clear steps.

If none of these conditions is present, use plain classes or functions with clear names.

## Output Format Before Coding

When the task is non-trivial, produce this concise plan before editing:

```markdown
Design sketch:
- Goal:
- Responsibilities:
- Boundaries:
- Pattern, if any:
- Files likely to change:
- Verification:
- Overengineering check:
```

After the design sketch, proceed with implementation unless the user asks to pause.
