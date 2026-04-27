# LINE Bot Architecture

## Heuristics

- Treat webhook events, message types, reply tokens, push messages, and webhook verification as API contracts.
- Keep signature verification, event deduplication, rate limit handling, and token refresh at the integration edge.
- Separate conversation routing, domain workflow, message formatting, and delivery.
- Design for LINE's specific message type constraints (text, image, flex, carousel, quick reply).
- Use LINE Messaging API SDKs behind adapters for testability.

## Common Risks

- Bot handlers containing full business workflows.
- Message format and platform user IDs leaking into domain code.
- Retry behavior causing repeated side effects (e.g., double order placement).
- No clear separation between platform permissions and application authorization.
- Ignoring LINE's rate limits on push messages and reply tokens.

## Verification

- Webhook handlers are idempotent.
- Domain workflows can be tested without real LINE API calls.
- Platform adapters have clear fallback/error behavior.
