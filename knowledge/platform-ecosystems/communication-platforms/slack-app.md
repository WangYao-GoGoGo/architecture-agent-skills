# Slack App Architecture

## Heuristics

- Treat slash commands, interactive components, event subscriptions, modals, and OAuth flows as API contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate command routing, domain workflow, message formatting (Block Kit), and delivery.
- Design for Slack's specific event types, payload structures, and rate limits.
- Use Slack SDKs behind adapters for testability.

## Common Risks

- Command handlers containing full business workflows.
- Bot token and user token management not centralized.
- Block Kit message format details leaking into domain services.
- Retry behavior causing repeated side effects.
- Ignoring Slack's rate limits on API calls and event delivery guarantees.

## Verification

- Event handlers are idempotent.
- Token lifecycle and retry behavior are centralized.
- Domain workflows can be tested without real Slack API calls.
