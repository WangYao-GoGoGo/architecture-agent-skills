# Onion Architecture

## Project Fit

Onion architecture is language-neutral, but it fits best when a domain model and domain rules are central to the application.

## Use When

- Domain rules should remain independent of infrastructure, UI, and persistence.
- The team needs a strong dependency direction around a domain model.
- The domain model has invariants, behavior, and vocabulary worth protecting.

## Avoid When

- The application is data-entry CRUD with little domain behavior.
- The domain model is anemic and all behavior lives naturally in workflows or functions.
- Layers would be created only to satisfy architecture style.

## Core Idea

Onion architecture places domain concepts at the center and surrounds them with application services, interfaces, infrastructure, and delivery mechanisms. Dependencies point inward.

## Heuristics

- Keep domain rules free of database, web, and framework details.
- Put use-case orchestration outside the domain model.
- Use interfaces or ports where outer layers need to satisfy inner policies.
- Avoid creating empty layers that only pass data through.

## Fits Best With

- Domain-heavy backend systems.
- Java/C#/TypeScript/Python systems with explicit domain objects.
- Applications where database or framework details should not shape the domain model.

## Adaptation Notes

- Backend: domain entities and value objects sit at the center.
- Frontend: use only for complex client-side business domains, not ordinary UI state.
- Functional/procedural code: adapt the idea as dependency direction around pure policy functions rather than classes.

## Relationship To Nearby Styles

- Similar to clean architecture in dependency direction.
- Similar to hexagonal architecture in protecting the core from adapters.
- More domain-model-centered in emphasis.

## Risks

- Too many layers for simple CRUD.
- Interfaces created without substitution or boundary value.
- Domain model becomes anemic while services hold all behavior.

## Verification

- Domain rules do not import persistence, UI, or framework details.
- Application services orchestrate use cases without swallowing all domain behavior.
- Infrastructure can change without rewriting core domain policy.
