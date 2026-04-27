# Event Sourcing

## Project Fit

Event sourcing fits domains where the sequence of changes is as important as the current state.

## Use When

- The history of state changes is a core business asset.
- Auditability, reconstruction, temporal queries, or complex state transitions matter.
- Events can be modeled as stable business facts.

## Avoid When

- The system is simple CRUD and only current state matters.
- Event versioning, replay, and projection operations are beyond team capacity.
- Business facts are not stable enough to store as long-lived events.

## Core Idea

Store state changes as an append-only event log. Current state is derived by replaying events or reading projections.

## Fits Best With

- Financial ledgers, audit-heavy domains, workflow histories, collaborative state, temporal models.

## Heuristics

- Model events as business facts, not CRUD notifications.
- Version event schemas carefully.
- Plan snapshots or projections when replay becomes expensive.
- Keep idempotency and ordering explicit.

## Risks

- Event schema mistakes are hard to undo.
- Simple CRUD becomes unnecessarily complex.
- Projections and migrations require strong discipline.

## Verification

- Events can rebuild current state.
- Event schema evolution is documented.
- Projection lag and replay cost are understood.
