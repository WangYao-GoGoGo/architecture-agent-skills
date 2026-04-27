# Telegram Platform Knowledge

## Use When

Reviewing or designing Telegram bot architecture, commands, or inline mode integration.

## Heuristics

- Treat update objects, commands, inline queries, and callback queries as API contracts.
- Keep webhook verification, update deduplication, and rate limit handling at the integration edge.
- Separate command routing, domain workflow, message formatting, and delivery.
- Design for Telegram's specific update types and inline mode.

## Common Risks

- Update handlers containing full business workflows.
- Webhook certificate and secret token setup not handled correctly.
- Message format and chat IDs leaking into domain code.
