# New Project Scaffolding

Generates a complete project structure with clear boundaries, dependency direction, testability, and maintainability built in from the start.

## When To Use This Skill

- Creating a new project, service, module, or application from scratch.
- The project will likely grow over time and needs a maintainable foundation.
- The team wants to enforce architecture rules from the start.

## How It Works

1. **Identify project context**: language, framework, domain, scale expectations.
2. **Choose architecture style**: layered, hexagonal, modular monolith, etc.
3. **Define module boundaries**: domain, application, infrastructure, presentation.
4. **Establish dependency rules**: domain must not depend on infrastructure.
5. **Generate file structure**: source directories, tests, config, build files.
6. **Add verification**: unit tests, architecture tests, CI pipeline.

## Knowledge Used

- [`knowledge/architecture/application-styles/`](../../knowledge/architecture/application-styles/README.md) — architecture style selection.
- [`knowledge/architecture/distributed-systems/`](../../knowledge/architecture/distributed-systems/README.md) — for multi-service projects.
- [`knowledge/principles/`](../../knowledge/principles/README.md) — SOLID, GRASP, dependency inversion.
- [`knowledge/patterns/architecture/`](../../knowledge/patterns/architecture/README.md) — large-scale patterns.

## Output

A complete project scaffold with module boundaries, dependency rules, file structure, and verification plan.

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — for designing individual features.
- [`architecture-decision-review`](../architecture-decision-review/README.md) — to document architecture decisions.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to avoid over-engineering the scaffold.
