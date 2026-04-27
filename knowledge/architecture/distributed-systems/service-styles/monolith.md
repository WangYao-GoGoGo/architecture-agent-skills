# Monolith

## Project Fit

A monolith fits projects that benefit from simple deployment, local transactions, and fast change while service boundaries are still evolving.

## Use When

- A product or team needs simple deployment, simple transactions, and fast iteration.
- Service boundaries are not yet stable.
- The team is small or operational capacity is limited.
- Most workflows benefit from local calls and shared transactions.

## Avoid When

- Independent deployment, scaling, or ownership is already a hard requirement.
- One codebase has become too large to test, reason about, or deploy safely.
- Strong module boundaries cannot be maintained inside one deployable.

## Core Idea

A monolith packages multiple capabilities into one deployable system. This can be a good architecture when boundaries are clear enough inside the code.

## Fits Best With

- Early-stage products.
- Small teams.
- Systems with strong consistency requirements.
- Modular monoliths where internal boundaries are still disciplined.

## Heuristics

- Prefer a modular monolith before splitting services.
- Keep internal modules cohesive.
- Use database transactions where they simplify invariants.
- Monitor growth points that may later justify extraction.

## Risks

- One deployable becomes one tangled codebase.
- Shared state and global utilities hide ownership.
- Build and test time grow without module discipline.

## Verification

- Deployment and rollback are simple.
- Module ownership is still understandable.
- Tests and builds remain acceptable.
- Future extraction candidates are visible but not prematurely split.
