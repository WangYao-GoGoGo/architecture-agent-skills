# Transactional Outbox

## Use When

- A service must update its database and publish an event reliably.

## Core Idea

Write the business change and an outbox record in the same local transaction. A relay later publishes the outbox event.

## Heuristics

- Use outbox to avoid dual-write failure between database and broker.
- Make event publishing idempotent.
- Monitor stuck or failed outbox records.
- Include ordering requirements if consumers depend on order.

## Risks

- Outbox table grows without cleanup.
- Consumers assume exactly-once delivery.
- Relay failure is not observable.

