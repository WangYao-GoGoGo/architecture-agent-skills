# Facebook/Meta Platform Architecture

## Heuristics

- Treat Graph API endpoints, webhook events, page access tokens, app secrets, and rate limits as platform contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate conversation routing, domain workflow, message formatting, and delivery.
- Design for Facebook's specific webhook verification, page subscriptions, and messaging types.
- Use Facebook Graph API SDKs behind adapters for testability and portability.

## Common Risks

- Webhook handlers containing full business workflows.
- Page access token refresh not centralized, causing periodic authentication failures.
- Message format and platform user IDs leaking into domain code.
- Retry behavior causing repeated side effects.
- Ignoring platform rate limits and webhook delivery guarantees.

## Verification

- Webhook handlers are idempotent.
- Token lifecycle and retry behavior are centralized.
- Domain workflows can be tested without real Facebook API calls.
