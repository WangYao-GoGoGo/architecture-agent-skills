# TikTok Platform Architecture

## Heuristics

- Treat TikTok API endpoints, OAuth flows, rate limits, webhook events, and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.
- Design for TikTok's specific video format requirements, caption length, and hashtag policies.

## Common Risks

- Publishing logic mixed with domain content workflow, making it hard to switch or add platforms.
- Rate limit handling absent, causing silent failures or throttled accounts.
- OAuth token refresh not handled, causing periodic authentication failures.
- Video format/size assumptions tied to TikTok's specific constraints.
- Content policy violations from assuming all platforms have the same rules.

## Verification

- Publishing operations can be tested without real TikTok API calls.
- Rate limit and token refresh handling is centralized.
- Video handling accounts for TikTok's specific format and size constraints.
