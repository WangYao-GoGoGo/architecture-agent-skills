# Slack Platform Knowledge

## Use When

Reviewing or designing Slack app architecture, commands, events, or Block Kit integration.

## Heuristics

- Treat slash commands, interactive components, event subscriptions, and modals as API contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate command routing, domain workflow, message formatting (Block Kit), and delivery.
- Design for Slack's specific event types and rate limits.

## Common Risks

- Command handlers containing full business workflows.
- Bot token and user token management not centralized.
- Block Kit message format details leaking into domain services.
