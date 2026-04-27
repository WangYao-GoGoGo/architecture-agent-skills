# Directory Structure

This repository uses a two-level-first structure. Keep common concepts discoverable without making paths too deep.

## Top-Level Model

```text
skills/      Executable agent workflows
knowledge/   Durable reusable architecture concepts
examples/    Before/after examples and evaluation fixtures
templates/   Authoring templates
docs/        Project governance and contribution guidance
tests/       Human-readable evaluation checklists
```

## Knowledge Structure

```text
knowledge/
  principles/        Cross-cutting design principles
  patterns/          Design patterns and architecture patterns
  smells/            Code, schema, boundary, and architecture smells
  refactoring/       Behavior-preserving refactoring moves
  architecture/      Application styles, distributed systems, integration patterns, governance, migration strategies
  paradigms/         OO, procedural, functional, systems-oriented concepts
  languages/         40+ languages across systems, scripting, web, scientific, functional, database, hardware, blockchain, legacy, and WASM
  application-areas/ Backend, frontend, data pipeline, operations
  data-systems/      Core data-system concepts and data-system families (30+ database technologies)
  api/               API contracts and compatibility
  frameworks/        80+ frameworks across backend, frontend, mobile, desktop, data, AI agent, database tools, Java, Python ORM, TypeScript data, and robotics
  platform/          Platform-specific knowledge for 33+ platforms (social, communication, payment, cloud, gaming, social media, IoT, drone, robotics) plus generic operations (Linux, shell, process, filesystem, config, deploy)
  methodologies/     Named learning systems and source-oriented maps
```

Use subfolders when a category is expected to grow beyond a few cards or needs technology-specific cards. Keep one-file cards when the topic is stable and small.

Architecture knowledge intentionally uses subfolders because the concerns differ: application-internal organization, distributed deployment shape, integration and consistency patterns, and decision governance should not be mixed in one flat list.

Keep `frameworks/` for technology behavior that runs inside or alongside the application, such as Spring Boot, React, Electron, ORMs, or ROS middleware. Keep `platform/` for external runtimes and vendor ecosystems that own rules outside the application, such as WeChat review/API constraints, cloud accounts, IoT fleets, robot controllers, Pepper/NAOqi, app stores, or bot-platform callbacks.

## Skill Structure

```text
skills/
  core/              Cross-language workflows
  paradigms/         Paradigm-specific workflows
  languages/         Language-specific workflows (40+ languages)
  domains/           Technical-domain workflows (backend, frontend, database, etc.)
  frameworks/        Framework-specific workflows (80+ frameworks across 12 categories)
  platforms/         External-platform and vendor-ecosystem workflows
```

Every non-trivial skill should have:

- `SKILL.md`
- optional `README.md`
- a `Knowledge To Use` section pointing to relevant knowledge cards

## Placement Rules

Choose the narrowest useful home:

1. Platform-ecosystem-specific
2. Framework-specific
3. Language-specific
4. Domain-specific
5. Paradigm-specific
6. Core

If a concept is reusable across several skills, put it in `knowledge/`. If it tells the agent what to do step by step, put it in `skills/`.
