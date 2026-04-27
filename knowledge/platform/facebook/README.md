# Facebook/Meta Platform Knowledge

## Use When

Reviewing or designing Facebook/Meta platform integration, Graph API, or webhook architecture.

## Heuristics

- Treat Graph API endpoints, webhook events, page access tokens, and rate limits as platform contracts.
- Keep signature verification, token refresh, deduplication, and rate limit handling at the integration edge.
- Separate conversation routing, domain workflow, message formatting, and delivery.
- Design for Facebook's specific webhook verification and messaging types.

## Common Risks

- Webhook handlers containing full business workflows.
- Page access token refresh not centralized.
- Message format and platform user IDs leaking into domain code.
