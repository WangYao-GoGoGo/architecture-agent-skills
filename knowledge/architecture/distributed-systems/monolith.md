# Monolith

## Use When

- A product or team needs simple deployment, simple transactions, and fast iteration.
- Service boundaries are not yet stable.

## Core Idea

A monolith packages multiple capabilities into one deployable system. This can be a good architecture when boundaries are clear enough inside the code.

## Heuristics

- Prefer a modular monolith before splitting services.
- Keep internal modules cohesive.
- Use database transactions where they simplify invariants.
- Monitor growth points that may later justify extraction.

## Risks

- One deployable becomes one tangled codebase.
- Shared state and global utilities hide ownership.
- Build and test time grow without module discipline.

