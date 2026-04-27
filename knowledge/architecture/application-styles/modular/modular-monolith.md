# Modular Monolith

## Project Fit

Modular monolith is language-neutral. It fits applications that should deploy as one unit while preserving clear business or technical module boundaries.

## Use When

- A system should stay deployable as one unit while keeping business capabilities separated.
- The team wants clear module boundaries before considering microservices.
- Transactions and local calls are still valuable, but code ownership needs more discipline.

## Avoid When

- The codebase is too small to need module boundaries.
- Independent deployment is already a hard requirement.
- Modules cannot own data or public interfaces clearly.

## Core Idea

A modular monolith keeps one deployment but organizes code into explicit modules with owned data, public interfaces, and dependency rules.

## Fits Best With

- Backend business applications.
- Full-stack apps with clear feature or domain modules.
- Teams preparing for possible future service extraction.

## Heuristics

- Define modules around business capability or ownership.
- Keep module internals private where the language allows it.
- Avoid cross-module database access unless explicitly owned.
- Use events or interfaces for module collaboration when direct calls create coupling.
- Treat module boundaries as seriously as service boundaries, but without network cost.

## Adaptation Notes

- Java: packages and module boundaries can enforce visibility.
- Python/TypeScript: use package/module exports and import rules.
- Frontend: feature modules can mirror business capabilities.
- Database: prefer clear table ownership even when one database is shared.

## Risks

- Modules are only folders with no dependency discipline.
- Shared database tables blur ownership.
- A central common module becomes a dumping ground.

## Verification

- Each module has a public surface and private internals.
- Dependency rules can be reviewed or automated.
- A future service extraction path is imaginable but not required.
