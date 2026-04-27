# Event-Driven Architecture

## Use When

- Multiple independent consumers react to business events.
- Workflows need decoupling, async processing, audit trails, or integration boundaries.

## Core Idea

Publish events that describe meaningful facts, and let consumers react independently.

## Risks

- Eventual consistency can surprise users.
- Ordering, retries, idempotency, and duplicate handling must be explicit.
- Event schemas become public contracts.

## Verification

- Producers and consumers have clear ownership.
- Consumers are idempotent where retries are possible.
- Monitoring covers failed or delayed event processing.
