# Layered Architecture

## Project Fit

Layered architecture is language-neutral. It can fit backend services, server-rendered web apps, desktop apps, frontend apps with clear data/application/presentation separation, and larger scripts that have distinct phases.

## Use When

- A system benefits from clear separation between presentation, application, domain, and persistence concerns.
- The team needs predictable dependency rules.
- The project has multiple concerns that change for different reasons.
- New contributors need a simple, conventional structure.

## Avoid When

- The application is a tiny script, simple page, or small CRUD flow where layers only pass data through.
- Feature work is scattered across too many folders and vertical slices would be easier to understand.
- The team cannot define what each layer owns.

## Core Idea

Organize code into layers with dependencies flowing in controlled directions. Common layers include controller/API, application service, domain, and infrastructure.

## Fits Best With

- Java, C#, Python, TypeScript, and backend services with clear controller/service/repository conventions.
- Web apps where transport, workflow, business rules, and persistence should remain separate.
- Teams that value familiar structure over highly feature-local organization.

## Adaptation Notes

- Backend: keep controllers thin and put workflow in application services.
- Frontend: treat components/views, state/use cases, domain rules, and API adapters as separate concerns.
- Scripts: use phases such as parse, validate, execute, and report instead of formal class layers.
- Data tools: separate ingestion, transformation, validation, and output.

## Risks

- Layers can become pass-through ceremony.
- Domain rules can leak into controllers or repositories.
- Strict layering can fight simple use cases.

## Verification

- Each layer has a clear reason to change.
- Dependencies do not cycle.
- Tests can target domain and application logic without full infrastructure.
