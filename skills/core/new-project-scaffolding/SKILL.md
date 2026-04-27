---
name: new-project-scaffolding
description: Use when generating a new project from scratch. Produces a complete project structure with clear boundaries, dependency direction, testability, and maintainability built in from the start.
---

# New Project Scaffolding

Use this skill when creating a new project from scratch. The goal is to generate a project structure that is maintainable, testable, and follows architecture best practices from day one — avoiding the "big ball of mud" that emerges when structure is an afterthought.

## When To Use

- The user asks to create a new project, service, module, or application.
- A greenfield codebase needs initial structure, conventions, and boundaries.
- The project will likely grow over time and needs a maintainable foundation.
- The team wants to enforce architecture rules from the start.

Do **not** use this skill for adding a single file to an existing project, simple scripts, or prototypes that will be discarded.

## Workflow

### Step 1: Identify Project Context

Determine the following from the user or requirements:

- **Language / runtime**: Java, Python, TypeScript, Go, Rust, etc.
- **Framework**: Spring Boot, Django, Next.js, FastAPI, etc.
- **Domain**: what business problem does this project solve?
- **Scale expectations**: will this be a monolith, modular monolith, or distributed system?
- **Key quality attributes**: availability, latency, consistency, security, auditability.

### Step 2: Choose Architecture Style

Based on the context, select the appropriate architecture style:

| Context | Recommended Style |
|---|---|
| Simple CRUD, single team | Layered Architecture |
| Complex domain logic | Hexagonal / Clean Architecture |
| Multiple bounded contexts | Modular Monolith |
| Multiple teams, independent deploy | Microservices (start with modular monolith) |
| Event-heavy workflow | Event-Driven Architecture |
| Read/write asymmetry | CQRS |

### Step 3: Define Module Boundaries

Identify the core modules and their responsibilities:

- **Domain / Core**: business rules, entities, value objects, domain services.
- **Application / Use Cases**: orchestration, input validation, transaction boundaries.
- **Infrastructure / Adapters**: persistence, messaging, external APIs, caching.
- **Presentation / API**: controllers, serialization, request/response models.
- **Configuration**: dependency injection, environment config, startup.

### Step 4: Establish Dependency Rules

Define the dependency direction for the project:

- Domain layer must not depend on infrastructure or presentation.
- Application layer may depend on domain but not on infrastructure.
- Infrastructure implements interfaces defined in domain or application.
- Presentation depends on application, not directly on domain.
- All cross-cutting concerns (logging, metrics, auth) use stable abstractions.

### Step 5: Generate File Structure

Create the initial project structure with:

- Build configuration (e.g., `pom.xml`, `Cargo.toml`, `package.json`, `pyproject.toml`)
- Source directories following the chosen architecture style
- Test directories mirroring source structure
- Configuration files (environment, logging, CI)
- README with project overview and conventions

### Step 6: Add Verification

Include verification mechanisms from the start:

- Unit tests for domain logic (no infrastructure dependencies)
- Integration tests for infrastructure adapters
- Architecture tests that enforce dependency rules (e.g., ArchUnit, AdrTools)
- Linting and formatting configuration

## Knowledge To Use

- [`knowledge/architecture/application-styles/`](../../knowledge/architecture/application-styles/README.md) — to choose the right in-process structure.
- [`knowledge/architecture/distributed-systems/`](../../knowledge/architecture/distributed-systems/README.md) — if the project spans multiple services.
- [`knowledge/architecture/integration-patterns/`](../../knowledge/architecture/integration-patterns/README.md) — for event-driven or async workflows.
- [`knowledge/principles/`](../../knowledge/principles/README.md) — SOLID, GRASP, dependency inversion, separation of concerns.
- [`knowledge/patterns/architecture/`](../../knowledge/patterns/architecture/README.md) — for large-scale architecture patterns.
- [`skills/core/architecture-before-coding/`](../architecture-before-coding/README.md) — for designing individual features within the scaffold.

## Output Format

```markdown
## Project Scaffold

### Context
- Language: [language]
- Framework: [framework]
- Domain: [domain description]
- Architecture style: [chosen style]

### Module Boundaries
- `domain/` — entities, value objects, domain services, repository interfaces
- `application/` — use cases, input/output DTOs, transaction boundaries
- `infrastructure/` — persistence implementations, messaging, external APIs
- `presentation/` — controllers, serialization, request validation
- `config/` — DI configuration, environment settings

### Dependency Rules
- Domain → (nothing)
- Application → Domain
- Infrastructure → Domain interfaces
- Presentation → Application

### File Structure
```
project-root/
├── src/
│   ├── domain/
│   │   ├── model/
│   │   ├── service/
│   │   └── repository/  (interfaces only)
│   ├── application/
│   │   └── usecase/
│   ├── infrastructure/
│   │   ├── persistence/
│   │   ├── messaging/
│   │   └── external/
│   └── presentation/
│       └── api/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── architecture/
├── config/
├── README.md
└── build.gradle / Cargo.toml / package.json
```

### Verification
- [ ] Domain tests run without infrastructure
- [ ] Architecture tests enforce dependency rules
- [ ] CI pipeline includes lint, test, and architecture check
- [ ] README documents conventions and architecture decisions
```

## Related Skills

- [`architecture-before-coding`](../architecture-before-coding/README.md) — for designing individual features within the scaffold.
- [`architecture-decision-review`](../architecture-decision-review/README.md) — to document architecture decisions made during scaffolding.
- [`anti-overengineering-review`](../anti-overengineering-review/README.md) — to check that the scaffold is not over-engineered for the current needs.
