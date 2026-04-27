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
  architecture/      Application styles, distributed systems, integration patterns, governance
  paradigms/         OO, procedural, functional, systems-oriented concepts
  languages/         Java, Python, C, SQL, TypeScript, JavaScript, Shell
  application-areas/ Backend, frontend, data pipeline, operations
  data-systems/      Core data-system concepts and data-system families
  api/               API contracts and compatibility
  frameworks/        Framework, ORM, migration, frontend framework knowledge
  platform/          Linux, shell, process, filesystem, config, deploy
  methodologies/     Named learning systems and source-oriented maps
```

Use subfolders when a category is expected to grow beyond a few cards or needs technology-specific cards. Keep one-file cards when the topic is stable and small.

Architecture knowledge intentionally uses subfolders because the concerns differ: application-internal organization, distributed deployment shape, integration and consistency patterns, and decision governance should not be mixed in one flat list.

## Skill Structure

```text
skills/
  core/              Cross-language workflows
  paradigms/         Paradigm-specific workflows
  languages/         Language-specific workflows
  domains/           Technical-domain workflows
  frameworks/        Framework-specific workflows
```

Every non-trivial skill should have:

- `SKILL.md`
- optional `README.md`
- a `Knowledge To Use` section pointing to relevant knowledge cards

## Placement Rules

Choose the narrowest useful home:

1. Framework-specific
2. Language-specific
3. Domain-specific
4. Paradigm-specific
5. Core

If a concept is reusable across several skills, put it in `knowledge/`. If it tells the agent what to do step by step, put it in `skills/`.
