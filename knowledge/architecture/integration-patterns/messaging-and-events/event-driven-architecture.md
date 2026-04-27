# Event-Driven Architecture

## Project Fit

Event-driven architecture fits systems where state changes need to notify independent consumers or trigger asynchronous workflows.

## Use When

- Multiple independent consumers react to business events.
- Workflows need decoupling, async processing, audit trails, or integration boundaries.
- Producers should not know every consumer.

## Avoid When

- A simple synchronous call is clearer and failure behavior is easier.
- Consumers require immediate strong consistency.
- Event schemas, retries, ordering, and observability are not ready.

## Core Idea

Publish events that describe meaningful facts, and let consumers react independently.

## Fits Best With

- Backend services, data pipelines, integrations, audit/event logs, async workflows.

## Risks

- Eventual consistency can surprise users.
- Ordering, retries, idempotency, and duplicate handling must be explicit.
- Event schemas become public contracts.

## Verification

- Producers and consumers have clear ownership.
- Consumers are idempotent where retries are possible.
- Monitoring covers failed or delayed event processing.
