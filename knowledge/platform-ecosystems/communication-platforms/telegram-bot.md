# Telegram Bot Architecture

## Heuristics

- Treat update objects, commands, inline queries, callback queries, and webhook delivery as API contracts.
- Keep webhook verification, update deduplication, rate limit handling, and token management at the integration edge.
- Separate command routing, domain workflow, message formatting, and delivery.
- Design for Telegram's specific update types, inline mode, and rate limits.
- Use python-telegram-bot or similar SDKs behind adapters for testability.

## Common Risks

- Update handlers containing full business workflows.
- Webhook certificate and secret token setup not handled correctly.
- Message format and chat IDs leaking into domain code.
- Retry behavior causing repeated side effects.
- Ignoring Telegram's rate limits on outgoing messages.

## Verification

- Update handlers are idempotent.
- Webhook setup and certificate management are correct.
- Domain workflows can be tested without real Telegram API calls.
