# Project Taxonomy

This repository organizes architecture guidance by the kind of decision an agent needs to make.

## Core Skills

Cross-cutting workflows that apply across languages and domains.

Examples:

- architecture before coding
- refactoring planning
- dependency boundary review
- architecture decision review
- anti-overengineering review

Use `skills/core/` when the workflow is not specific to one language, paradigm, framework, or domain.

## Paradigm Skills

Guidance based on programming model.

Examples:

- object-oriented design
- procedural modular design
- functional composition
- systems boundary design

Use `skills/paradigms/` when the main question is how code should be structured according to a programming paradigm.

## Language Skills

Guidance based on language idioms and constraints.

Examples:

- Java package boundaries and dependency injection
- Python protocols and module organization
- C header/interface design
- SQL query and schema structure
- TypeScript type-driven module design
- JavaScript module and async workflow design
- Shell script architecture and Linux automation

Use `skills/languages/` when the answer depends on language-specific mechanics or idioms.

## Domain Skills

Guidance based on product or technical domain.

Examples:

- backend service boundaries
- frontend component and state ownership
- database modeling and indexing
- cache strategy and invalidation
- search indexing
- data pipeline architecture
- operations and shell automation

Use `skills/domains/` when the decision is about the architecture of a technical area rather than a language.

## Framework Skills

Guidance based on a specific framework or platform.

Examples:

- Spring transaction boundaries
- Django app structure
- React state and component patterns
- Redis data structure usage
- ORM entity/session/repository boundaries
- migration tool rollout behavior

Use `skills/frameworks/` when the guidance depends on framework behavior, lifecycle, conventions, or APIs.

## Knowledge Cards

Reusable concepts that skills can reference.

Examples:

- principles
- design patterns
- architecture patterns
- code smells
- schema smells
- refactoring moves
- language idioms
- framework boundaries
- Linux and operational architecture

Use `knowledge/` for durable concepts. Use `skills/` for executable agent workflows.

## Knowledge Layers

Use `knowledge/` as the shared concept library behind skills:

- `knowledge/principles/`: reusable design principles.
- `knowledge/paradigms/`: programming model concepts.
- `knowledge/languages/`: language-specific architecture idioms.
- `knowledge/domains/`: backend, frontend, pipeline, and operations concepts.
- `knowledge/database/`: relational, non-relational, cache, search, and vector concepts.
- `knowledge/frameworks/`: framework, ORM, migration, and generated-client concepts.
- `knowledge/operations/`: Linux, shell, process, filesystem, and configuration concerns.
- `knowledge/methodologies/`: named learning systems, curricula, and source-oriented maps.

For alignment rules, see `docs/knowledge-skill-map.md`.

## Placement Rule

If a contribution could fit multiple places, choose the narrowest useful home:

1. Framework-specific
2. Language-specific
3. Domain-specific
4. Paradigm-specific
5. Core

Core should stay small. It is the shared operating system, not a dumping ground.
