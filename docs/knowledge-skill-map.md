# Knowledge To Skill Map

This map keeps `knowledge/` and `skills/` aligned.

## Core Skills

Core skills should load only the knowledge needed for the task:

- `architecture-before-coding`: `principles/`, `architecture/application-styles/`, `architecture/integration-patterns/`, `patterns/`, `smells/`
- `refactoring-planner`: `refactoring/`, `smells/`, `principles/`
- `dependency-boundary-review`: `principles/dependency-inversion.md`, `principles/separation-of-concerns.md`, `frameworks/core/framework-boundaries.md`
- `anti-overengineering-review`: `principles/`, `smells/`, `patterns/`
- `architecture-decision-review`: `architecture/`, especially `architecture/decision-governance/`, plus `database/`, `api/`, `frameworks/` as needed

## Paradigm Skills

- `skills/paradigms/object-oriented/`: `knowledge/paradigms/object-oriented/`, `principles/solid.md`, `principles/grasp.md`, `patterns/`
- `skills/paradigms/procedural/`: `knowledge/paradigms/procedural/`, `knowledge/languages/c/`, `refactoring/`
- `skills/paradigms/functional/`: `knowledge/paradigms/functional/`
- `skills/paradigms/systems/`: `knowledge/paradigms/systems-oriented/`, `knowledge/operations/`

## Language Skills

- Java: `knowledge/languages/java/`, plus OO, framework, and database cards as needed.
- Python: `knowledge/languages/python/`, plus clean architecture, ORM, and framework cards as needed.
- C: `knowledge/languages/c/`, plus procedural and systems-oriented cards.
- SQL: `knowledge/languages/sql/`, plus database cards.
- TypeScript: `knowledge/languages/typescript/`, plus frontend, API, and framework cards.
- JavaScript: `knowledge/languages/javascript/`, plus frontend, API, and framework cards.
- Shell: `knowledge/languages/shell/`, plus operations cards.

## Domain Skills

- Backend: `knowledge/domains/backend/`, `knowledge/api/`, `knowledge/database/`
- Frontend: `knowledge/domains/frontend/`, `knowledge/languages/typescript/`, `knowledge/languages/javascript/`, `knowledge/frameworks/frontend/frontend-frameworks.md`
- Database: `knowledge/database/`, plus technology-specific skill instructions.
- Vector search: `knowledge/database/vector/`, `knowledge/database/search/`, `knowledge/database/core/access-patterns.md`
- Data pipeline: `knowledge/domains/data-pipeline/`, `knowledge/database/core/consistency.md`, `knowledge/api/contract-design.md`
- Operations and shell automation: `knowledge/domains/operations/`, `knowledge/operations/`, `knowledge/languages/shell/`

## Framework Skills

- Framework boundary review: `knowledge/frameworks/core/framework-boundaries.md`
- ORM boundary review: `knowledge/frameworks/orm/orm-boundaries.md`, `knowledge/database/`
- Migration tools: `knowledge/frameworks/migrations/migration-tools.md`, `knowledge/database/core/migrations.md`
- Frontend frameworks: `knowledge/frameworks/frontend/frontend-frameworks.md`, `knowledge/domains/frontend/`

## Coverage Checks

When adding a new category, check both sides:

- Knowledge exists for durable concepts.
- A skill exists for executable review or implementation workflow.

Examples:

- `knowledge/languages/shell/` is paired with `skills/languages/shell/shell-script-architecture`.
- `knowledge/languages/typescript/` is paired with `skills/languages/typescript/typescript-module-architecture`.
- `knowledge/languages/javascript/` is paired with `skills/languages/javascript/javascript-module-architecture`.
- `knowledge/operations/` is paired with `skills/domains/operations/operational-script-review`.
- `knowledge/frameworks/` is paired with `skills/frameworks/framework-boundary-review` and `skills/frameworks/orm-boundary-review`.
- `knowledge/database/vector/` is paired with `skills/domains/database/vector/vector-search-architecture-review`.

## Rule For New Skills

Every non-trivial skill should include a short `Knowledge To Use` section listing relevant knowledge cards. This keeps each `SKILL.md` concise while making deeper context discoverable.

## Methodology Notes

Named learning systems such as Suntone architecture, Java architecture curricula, or GoF reading paths belong under `knowledge/methodologies/`. Reusable concepts from those systems should still be linked to their canonical cards in `principles/`, `patterns/`, `architecture/`, `languages/`, or `frameworks/`.
