# LINE Platform Knowledge

## Use When

Reviewing or designing LINE bot architecture and messaging API integration.

## Heuristics

- Treat webhook events, message types, reply tokens, and push messages as API contracts.
- Keep signature verification, event deduplication, and rate limit handling at the integration edge.
- Separate conversation routing, domain workflow, message formatting, and delivery.
- Design for LINE's specific message type constraints and rate limits.

## Common Risks

- Bot handlers containing full business workflows.
- Message format and platform user IDs leaking into domain code.
- Retry behavior causing repeated side effects.
