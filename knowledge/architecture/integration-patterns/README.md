# Integration Patterns

Integration pattern cards describe how components, services, and data flows communicate.

## Structure

- `messaging-and-events/`: event-driven architecture, publish-subscribe, message queues, webhooks.
- `consistency-and-transactions/`: saga, transactional outbox, idempotent consumer.
- `read-write-models/`: CQRS, event sourcing, read model projections.
- `edge-and-client/`: API gateway, backend-for-frontend, API composition.

## Selection Guide

| Pressure | Start With |
| --- | --- |
| Decoupled communication or async work | `messaging-and-events/` |
| Cross-service consistency or reliable event publishing | `consistency-and-transactions/` |
| Different read/write models or event history | `read-write-models/` |
| Client-facing aggregation, routing, or API shaping | `edge-and-client/` |

## Fit Rule

Integration patterns add operational and consistency complexity. Use them when they reduce coupling or make a real workflow safer, not because a system has multiple components.
