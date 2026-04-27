# Twitter/X Platform Architecture

## Heuristics

- Treat Twitter API v2 endpoints, OAuth 2.0 flows, rate limits, webhook events, and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.
- Design for Twitter's specific tweet length, media attachment limits, and polling vs streaming tradeoffs.

## Common Risks

- Publishing logic mixed with domain content workflow, making it hard to switch or add platforms.
- Rate limit handling absent, causing silent failures or throttled accounts.
- OAuth 2.0 PKCE flow not correctly implemented for user context.
- Media format/size assumptions tied to Twitter's specific constraints.
- Content policy violations from assuming all platforms have the same rules.

## Verification

- Publishing operations can be tested without real Twitter API calls.
- Rate limit and token refresh handling is centralized.
- Media handling accounts for Twitter's specific format and size constraints.
