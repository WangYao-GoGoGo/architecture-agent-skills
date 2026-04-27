# Feishu/Lark App Architecture

## Heuristics

- Treat event callbacks, card actions, commands, and API requests as platform contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate event routing, domain workflow, card message formatting, and delivery.
- Design for Feishu's specific event types, card interaction model, and tenant isolation.
- Use Feishu SDKs behind adapters for testability.

## Common Risks

- Event handlers containing full business workflows.
- Tenant access token refresh not centralized.
- Card message format details leaking into domain services.
- Retry behavior causing repeated side effects.
- Ignoring Feishu's rate limits and event delivery guarantees.

## Verification

- Event handlers are idempotent.
- Token lifecycle and retry behavior are centralized.
- Domain workflows can be tested without real Feishu API calls.
