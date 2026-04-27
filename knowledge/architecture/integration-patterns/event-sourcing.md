# Event Sourcing

## Use When

- The history of state changes is a core business asset.
- Auditability, reconstruction, temporal queries, or complex state transitions matter.

## Core Idea

Store state changes as an append-only event log. Current state is derived by replaying events or reading projections.

## Heuristics

- Model events as business facts, not CRUD notifications.
- Version event schemas carefully.
- Plan snapshots or projections when replay becomes expensive.
- Keep idempotency and ordering explicit.

## Risks

- Event schema mistakes are hard to undo.
- Simple CRUD becomes unnecessarily complex.
- Projections and migrations require strong discipline.

