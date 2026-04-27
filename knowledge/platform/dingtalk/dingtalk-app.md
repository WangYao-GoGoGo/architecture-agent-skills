# DingTalk App Architecture

## Heuristics

- Treat event callbacks, robot webhooks, interactive cards, and API requests as platform contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate event routing, domain workflow, card message formatting, and delivery.
- Design for DingTalk's specific event types, robot interaction model, and 企业内部应用 vs 第三方应用 differences.
- Use DingTalk SDKs behind adapters for testability.

## Common Risks

- Event handlers containing full business workflows.
- Access token refresh not centralized.
- Card message format details leaking into domain services.
- Retry behavior causing repeated side effects.
- Ignoring DingTalk's rate limits and enterprise deployment constraints.

## Verification

- Event handlers are idempotent.
- Token lifecycle and retry behavior are centralized.
- Domain workflows can be tested without real DingTalk API calls.
