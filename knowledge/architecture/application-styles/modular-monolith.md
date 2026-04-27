# Modular Monolith

## Use When

- A system should stay deployable as one unit while keeping business capabilities separated.
- The team wants clear module boundaries before considering microservices.

## Core Idea

A modular monolith keeps one deployment but organizes code into explicit modules with owned data, public interfaces, and dependency rules.

## Heuristics

- Define modules around business capability or ownership.
- Keep module internals private where the language allows it.
- Avoid cross-module database access unless explicitly owned.
- Use events or interfaces for module collaboration when direct calls create coupling.
- Treat module boundaries as seriously as service boundaries, but without network cost.

## Risks

- Modules are only folders with no dependency discipline.
- Shared database tables blur ownership.
- A central common module becomes a dumping ground.

