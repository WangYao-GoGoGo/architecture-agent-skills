# Project Vision

Modern AI coding agents can produce code quickly, but speed alone does not guarantee software that is easy to understand, test, operate, or change. This project gives agents a reusable architecture layer: a set of skills, knowledge cards, examples, and review checklists that guide them toward maintainable design across languages, paradigms, and technical domains.

## North Star

Help AI agents write and refactor code with explicit architectural intent.

That means every meaningful change should answer:

- What responsibilities exist?
- Which objects, modules, services, functions, schemas, components, or pipelines own them?
- What dependencies are allowed?
- What data, cache, API, UI, or infrastructure boundaries matter?
- What should be easy to change later?
- What complexity is not worth introducing yet?

## Scope

The project scope is broad software architecture for agent-assisted coding:

- Core workflows: architecture before coding, refactoring planning, dependency boundary review, architecture decision review.
- Paradigms: object-oriented, procedural, functional, and systems-oriented design.
- Languages: Java, Python, C, SQL, TypeScript, JavaScript, Shell, and future language packs.
- Domains: backend services, frontend component architecture, databases, caches, search systems, vector search, data pipelines, APIs, operations, and integrations.
- Frameworks: ORMs, migration tools, frontend frameworks, backend frameworks, generated clients, and framework lifecycle boundaries.
- Knowledge: principles, design patterns, architecture patterns, language idioms, framework boundaries, code smells, data modeling smells, operational risks, and refactoring moves.

Object-oriented architecture is an early content focus because it has a mature vocabulary around responsibilities, patterns, and refactoring. It should be treated as one strong pillar, not the outer wall of the project.

## Non-Goals

- Do not force every code problem into an object-oriented design pattern.
- Do not replace language, framework, or project-specific judgment.
- Do not reward abstract architecture diagrams that do not improve code.
- Do not optimize for academic completeness before practical usefulness.
- Do not treat application code as the only architecture surface; data, cache, frontend state, APIs, and operational boundaries also count.

## What Good Output Looks Like

A good skill should make an agent produce:

- a short diagnosis of the current design problem
- a small set of candidate structures
- a recommended structure with tradeoffs
- a refactoring or implementation sequence
- tests or verification steps
- warnings against overengineering when the change is small

## Initial Roadmap

1. Make the core skills usable: architecture before coding, pattern selection, refactoring planning, dependency boundary review.
2. Build the first paradigm packs: object-oriented, procedural modular design, functional composition, and systems boundary review.
3. Add Java, Python, C, SQL, TypeScript, JavaScript, and Shell language packs with concrete before/after examples.
4. Add database, cache, backend, frontend, data pipeline, operations, and vector search domain packs.
5. Add framework packs for ORMs, migration tools, and frontend/backend frameworks.
6. Add evaluation checklists so contributors can judge whether a skill improves agent behavior.
