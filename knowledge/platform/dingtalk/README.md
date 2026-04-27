# DingTalk Platform Knowledge

## Use When

Reviewing or designing DingTalk app architecture, robot, or enterprise integration.

## Heuristics

- Treat event callbacks, robot webhooks, interactive cards, and API requests as platform contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate event routing, domain workflow, card message formatting, and delivery.
- Design for DingTalk's specific event types and enterprise deployment constraints.

## Common Risks

- Event handlers containing full business workflows.
- Access token refresh not centralized.
- Card message format details leaking into domain services.
