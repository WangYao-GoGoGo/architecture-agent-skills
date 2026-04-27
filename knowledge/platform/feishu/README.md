# Feishu/Lark Platform Knowledge

## Use When

Reviewing or designing Feishu/Lark app architecture, events, or card interactions.

## Heuristics

- Treat event callbacks, card actions, commands, and API requests as platform contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate event routing, domain workflow, card message formatting, and delivery.
- Design for Feishu's specific event types, card interaction model, and tenant isolation.

## Common Risks

- Event handlers containing full business workflows.
- Tenant access token refresh not centralized.
- Card message format details leaking into domain services.
