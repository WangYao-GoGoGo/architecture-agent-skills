# YouTube Platform Architecture

## Heuristics

- Treat YouTube Data API v3 endpoints, OAuth 2.0 flows, rate limits, webhook events (PubSubHubbub), and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.
- Design for YouTube's specific video upload workflow (resumable uploads), caption formats, and playlist management.

## Common Risks

- Publishing logic mixed with domain content workflow, making it hard to switch or add platforms.
- Rate limit handling absent, causing silent failures or throttled accounts.
- OAuth token refresh not handled, causing periodic authentication failures.
- Video format/size assumptions tied to YouTube's specific constraints.
- Content policy violations (copyright, community guidelines) from assuming all platforms have the same rules.

## Verification

- Publishing operations can be tested without real YouTube API calls.
- Rate limit and token refresh handling is centralized.
- Video upload and processing accounts for YouTube's specific workflow and constraints.
