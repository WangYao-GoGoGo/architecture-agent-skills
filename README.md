# Architecture Agent Skills

Architecture Agent Skills is an open-source skill library for helping AI coding agents design, review, and refactor software with explicit architecture thinking before they write large blocks of code.

The project covers architecture across programming paradigms, languages, and technical domains: object-oriented design, procedural modular design, functional composition, backend services, frontend components, databases, caches, data pipelines, and more. Object-oriented architecture is an early focus, not the final boundary of the project.

The goal is not to make agents use patterns everywhere. The goal is to help agents choose simple, readable structures that make code easier to understand, test, change, and extend.

## What This Project Is For

- Review existing code and identify architecture smells.
- Plan refactors before changing code.
- Select design patterns only when the problem actually fits.
- Design new code around responsibilities, boundaries, and extension points.
- Provide paradigm-specific guidance for object-oriented, procedural, functional, and systems-oriented code.
- Provide language-specific guidance for Java, Python, C, SQL, TypeScript, JavaScript, Shell, and future language packs.
- Provide domain-specific guidance for backend, frontend, database, cache, search, data pipeline, and operations architecture.
- Provide platform-ecosystem guidance for WeChat, robotics, cloud, IoT, bot platforms, and vendor SDK integrations.
- Build a shared knowledge base that contributors can improve over time.

## Repository Layout

```text
skills/
  core/                 Cross-language architecture workflows
  paradigms/            Object-oriented, functional, procedural, systems thinking
  languages/            Java, Python, C, SQL, TypeScript, JavaScript, Shell guidance
  domains/              Backend, frontend, database, data pipeline, operations guidance
  frameworks/           Framework, ORM, migration-tool, generated-client guidance
  platforms/            External platform, vendor SDK, robot, IoT, cloud ecosystem guidance

knowledge/
  principles/           SOLID, GRASP, coupling/cohesion, boundaries
  patterns/             Design pattern and architecture pattern cards
  smells/               Code, schema, boundary, and architecture smell cards
  architecture/         Application styles, distributed systems, integration patterns, governance
  paradigms/            OO, procedural, functional, systems-oriented concepts
  languages/            Java, Python, C, SQL, TypeScript, JavaScript, Shell idioms
  application-areas/    Backend, frontend, data pipeline, operations
  data-systems/         Relational, document, key-value, graph, search, vector, cache
  api/                  Contracts, versioning, idempotency, pagination, errors
  frameworks/           Framework boundaries, ORM, migrations, frontend frameworks
  platform-ecosystems/  WeChat, robotics, cloud, IoT, bot and vendor platform constraints
  platform/             Linux, shell, process, filesystem, configuration
  methodologies/        Named learning systems and source-oriented maps

templates/              Reusable templates for new skills and reports
docs/                   Project vision, contribution workflow, design guide
examples/               Before/after examples for evaluation and learning
tests/                  Human-readable evaluation checklists
```

## First Core Skills

- `skills/core/architecture-before-coding`: use before implementing a feature, so the agent proposes responsibilities, boundaries, interfaces, and risks first.
- `skills/core/design-pattern-selector`: use when code has conditionals, duplicated workflows, object creation complexity, event notification, adapters, or extension needs.
- `skills/core/refactoring-planner`: use before changing existing code, especially when behavior must remain stable.

## Frameworks vs Platform Ecosystems

Put framework behavior in `knowledge/frameworks/`: Spring Boot, React, Django, Electron, ROS 2, ORMs, migration tools, and similar runtime or library ecosystems.

Put external ecosystem constraints in `knowledge/platform-ecosystems/`: WeChat, Pepper/NAOqi, robot arms, cloud accounts, IoT fleets, chat/bot platforms, app review rules, hardware controllers, platform callbacks, and vendor SDK boundaries.

## Design Philosophy

1. Prefer clear responsibility and boundaries over clever abstraction.
2. Prefer the idioms of the target paradigm and language.
3. Prefer composition before inheritance unless the domain model genuinely benefits from inheritance.
4. Prefer naming the tradeoff over forcing a pattern.
5. Prefer behavior-preserving refactors with tests or executable checks.
6. Avoid pattern shopping. A pattern is useful only when it reduces real change cost.
7. Treat data architecture, caching, APIs, and frontend state as first-class architecture concerns.

## Contributing

This repository is intentionally organized so contributors can add one small, high-quality unit at a time:

- a skill under `skills/`
- a knowledge card under `knowledge/`
- a before/after example under `examples/`
- an evaluation checklist under `tests/`

Start with `docs/skill-design-guide.md` and use the templates in `templates/`.

For placement rules, see `docs/taxonomy.md`. For the full directory model, see `docs/directory-structure.md`. For skill-to-knowledge alignment, see `docs/knowledge-skill-map.md`.
