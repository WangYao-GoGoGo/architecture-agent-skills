# Core Skills

Core skills are the fundamental architecture skills that apply across all languages, frameworks, and domains. They form the foundation of the architecture agent workflow.

## Skills

| Skill | Purpose |
|---|---|
| [`architecture-before-coding`](architecture-before-coding/README.md) | Design responsibilities, boundaries, and patterns before implementing a non-trivial change. |
| [`refactoring-planner`](refactoring-planner/README.md) | Plan behavior-preserving refactors for existing code with unclear ownership, duplication, or coupling. |
| [`design-pattern-selector`](design-pattern-selector/README.md) | Decide whether a design pattern is justified and choose the smallest pattern that reduces real complexity. |
| [`dependency-boundary-review`](dependency-boundary-review/README.md) | Review whether dependencies between modules, services, and components point in maintainable directions. |
| [`architecture-decision-review`](architecture-decision-review/README.md) | Review or document architecture decisions, tradeoffs, alternatives, consequences, and verification. |
| [`anti-overengineering-review`](anti-overengineering-review/README.md) | Check whether a proposed architecture or abstraction is larger than the current problem needs. |
| [`new-project-scaffolding`](new-project-scaffolding/README.md) | Generate a complete project structure with clear boundaries, dependency direction, and testability from the start. |
| [`architecture-quality-review`](architecture-quality-review/README.md) | Evaluate whether generated or existing code meets architecture quality standards. |

## Workflow Integration

The core skills work together in a natural workflow:

1. **New project?** → [`new-project-scaffolding`](new-project-scaffolding/README.md) to generate the initial structure.
2. **New feature?** → [`architecture-before-coding`](architecture-before-coding/README.md) to design before implementing.
3. **Need a pattern?** → [`design-pattern-selector`](design-pattern-selector/README.md) to pick the right one.
4. **Refactoring?** → [`refactoring-planner`](refactoring-planner/README.md) to plan incremental changes.
5. **Reviewing?** → [`dependency-boundary-review`](dependency-boundary-review/README.md) or [`architecture-decision-review`](architecture-decision-review/README.md) for targeted reviews.
6. **Too complex?** → [`anti-overengineering-review`](anti-overengineering-review/README.md) to simplify.
7. **Done?** → [`architecture-quality-review`](architecture-quality-review/README.md) to verify quality.

## Knowledge Packs

Each core skill has a corresponding knowledge pack in [`knowledge/core/`](../../knowledge/core/README.md) with architecture-level heuristics.
