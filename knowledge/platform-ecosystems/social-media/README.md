# Social Media Platform Ecosystem Knowledge

Social media platforms include content publishing, media upload, user data access, analytics, webhook events, and API-driven integration where the platform owns identity, rate limits, content policies, and data access.

Examples include Twitter/X (API v2), TikTok (TikTok API), Instagram (Graph API), and YouTube (Data API v3).

## Heuristics

- Treat API endpoints, OAuth flows, rate limits, webhook events, and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.

## Common Risks

- Publishing logic mixed with domain content workflow, making it hard to switch or add platforms.
- Rate limit handling absent, causing silent failures or throttled accounts.
- OAuth token refresh not handled, causing periodic authentication failures.
- Media format/size assumptions tied to one platform's constraints.
- Content policy violations from assuming all platforms have the same rules.
