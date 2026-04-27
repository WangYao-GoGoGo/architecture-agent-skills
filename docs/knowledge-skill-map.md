# Knowledge To Skill Map

This map keeps `knowledge/` and `skills/` aligned.

## Core Skills

Core skills should load only the knowledge needed for the task:

- `architecture-before-coding`: `principles/`, `architecture/application-styles/`, `architecture/integration-patterns/`, `patterns/`, `smells/`
- `refactoring-planner`: `refactoring/`, `smells/`, `principles/`
- `dependency-boundary-review`: `principles/dependency-inversion.md`, `principles/separation-of-concerns.md`, `frameworks/core/framework-boundaries.md`
- `anti-overengineering-review`: `principles/`, `smells/`, `patterns/`
- `architecture-decision-review`: `architecture/`, especially `architecture/decision-governance/`, plus `data-systems/`, `api/`, `frameworks/`, `platform-ecosystems/` as needed

## Paradigm Skills

- `skills/paradigms/object-oriented/`: `knowledge/paradigms/object-oriented/`, `principles/solid.md`, `principles/grasp.md`, `patterns/`
- `skills/paradigms/procedural/`: `knowledge/paradigms/procedural/`, `knowledge/languages/c/`, `refactoring/`
- `skills/paradigms/functional/`: `knowledge/paradigms/functional/`
- `skills/paradigms/systems/`: `knowledge/paradigms/systems-oriented/`, `knowledge/platform/`

## Language Skills

- Java: `knowledge/languages/java/`, plus OO, framework, and data-system cards as needed.
- Python: `knowledge/languages/python/`, plus clean architecture, ORM, and framework cards as needed.
- C: `knowledge/languages/c/`, plus procedural and systems-oriented cards.
- SQL: `knowledge/languages/sql/`, plus data-system cards.
- TypeScript: `knowledge/languages/typescript/`, plus frontend, API, and framework cards.
- JavaScript: `knowledge/languages/javascript/`, plus frontend, API, and framework cards.
- Shell: `knowledge/languages/shell/`, plus operations cards.

## Domain Skills

- Backend: `knowledge/application-areas/backend/`, `knowledge/api/`, `knowledge/data-systems/`
- Frontend: `knowledge/application-areas/frontend/`, `knowledge/languages/typescript/`, `knowledge/languages/javascript/`, `knowledge/frameworks/frontend/frontend-frameworks.md`
- Data systems: `knowledge/data-systems/`, plus technology-specific skill instructions.
- Vector search: `knowledge/data-systems/vector/`, `knowledge/data-systems/search/`, `knowledge/data-systems/core/access-patterns.md`
- Data pipeline: `knowledge/application-areas/data-pipeline/`, `knowledge/data-systems/core/consistency.md`, `knowledge/api/contract-design.md`
- Operations and shell automation: `knowledge/application-areas/operations/`, `knowledge/platform/`, `knowledge/languages/shell/`

## Framework Skills

- Framework boundary review: `knowledge/frameworks/core/framework-boundaries.md`
- ORM boundary review: `knowledge/frameworks/orm/orm-boundaries.md`, `knowledge/data-systems/`
- Migration tools: `knowledge/frameworks/migrations/migration-tools.md`, `knowledge/data-systems/core/migrations.md`
- Frontend frameworks: `knowledge/frameworks/frontend/frontend-frameworks.md`, `knowledge/application-areas/frontend/`
- Backend, mobile, desktop, data, and AI-agent frameworks: `knowledge/frameworks/`, loaded by `framework-boundary-review` or a narrower domain/language skill until a dedicated framework workflow is needed.
- Robotics frameworks: `knowledge/frameworks/robotics/`, plus `knowledge/platform-ecosystems/robotics/` when hardware or vendor runtime constraints matter.

## Platform Skills

- Platform ecosystem review: `knowledge/platform-ecosystems/`, `knowledge/api/`, `knowledge/frameworks/core/framework-boundaries.md`, `knowledge/platform/`
- WeChat mini program architecture: `knowledge/platform-ecosystems/wechat/`, `knowledge/languages/javascript/`, `knowledge/languages/typescript/`, `knowledge/api/`
- Robotics platform architecture: `knowledge/platform-ecosystems/robotics/`, `knowledge/frameworks/robotics/`, `knowledge/languages/python/`, `knowledge/languages/c/`, `knowledge/platform/`

## Coverage Checks

When adding a new category, check both sides:

- Knowledge exists for durable concepts.
- A skill exists for executable review or implementation workflow.

Examples:

- `knowledge/languages/shell/` is paired with `skills/languages/shell/shell-script-architecture`.
- `knowledge/languages/typescript/` is paired with `skills/languages/typescript/typescript-module-architecture`.
- `knowledge/languages/javascript/` is paired with `skills/languages/javascript/javascript-module-architecture`.
- `knowledge/platform/` is paired with `skills/domains/operations/operational-script-review`.
- `knowledge/frameworks/` is paired with `skills/frameworks/framework-boundary-review` and `skills/frameworks/orm-boundary-review`.
- `knowledge/data-systems/vector/` is paired with `skills/domains/database/vector/vector-search-architecture-review`.
- `knowledge/platform-ecosystems/` is paired with `skills/platforms/platform-ecosystem-architecture-review`.
- `knowledge/platform-ecosystems/wechat/` is paired with `skills/platforms/wechat/wechat-mini-program-architecture`.
- `knowledge/platform-ecosystems/robotics/` is paired with `skills/platforms/robotics/robotics-platform-architecture`.

## Rule For New Skills

Every non-trivial skill should include a short `Knowledge To Use` section listing relevant knowledge cards. This keeps each `SKILL.md` concise while making deeper context discoverable.

## Methodology Notes

Named learning systems such as Suntone architecture, Java architecture curricula, or GoF reading paths belong under `knowledge/methodologies/`. Reusable concepts from those systems should still be linked to their canonical cards in `principles/`, `patterns/`, `architecture/`, `languages/`, or `frameworks/`.
