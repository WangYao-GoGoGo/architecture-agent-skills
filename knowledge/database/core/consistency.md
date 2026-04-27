# Consistency

## Use When

- Reviewing transactions, caches, distributed writes, event processing, or denormalized data.

## Core Idea

Consistency is a product and architecture decision. Strong consistency protects invariants immediately. Eventual consistency improves decoupling and scale but requires explicit user experience, retries, reconciliation, and observability.

## Agent Heuristics

- Identify the invariant that must hold.
- Keep strongly consistent writes inside one transaction when possible.
- Use idempotency for retries and async consumers.
- Define stale-data tolerance before adding cache or asynchronous replication.
- For distributed writes, prefer saga/outbox patterns over hidden best-effort updates.

## Verification

- Failure paths do not silently violate invariants.
- Retries are safe.
- Stale reads are acceptable or clearly bounded.
- Monitoring can detect delayed or failed propagation.

