# Transactional Outbox

## Project Fit

Transactional outbox fits services that need to change local state and publish messages reliably without a distributed transaction.

## Use When

- A service must update its database and publish an event reliably.
- The database update and event publication must not diverge silently.
- Consumers can tolerate at-least-once delivery.

## Avoid When

- Events are best-effort and loss is acceptable.
- The system cannot operate or monitor an outbox relay.
- A simpler synchronous call is enough.

## Core Idea

Write the business change and an outbox record in the same local transaction. A relay later publishes the outbox event.

## Fits Best With

- Microservices, event-driven systems, integration events, CDC-like publishing.

## Heuristics

- Use outbox to avoid dual-write failure between database and broker.
- Make event publishing idempotent.
- Monitor stuck or failed outbox records.
- Include ordering requirements if consumers depend on order.

## Risks

- Outbox table grows without cleanup.
- Consumers assume exactly-once delivery.
- Relay failure is not observable.

## Verification

- Business write and outbox write commit together.
- Relay retries are safe.
- Stuck outbox records alert owners.
