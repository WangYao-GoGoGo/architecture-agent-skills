# TikTok Platform Knowledge

## Use When

Reviewing or designing TikTok platform integration, video publishing, or social media architecture.

## Heuristics

- Treat TikTok API endpoints, OAuth flows, rate limits, and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.

## Common Risks

- Publishing logic mixed with domain content workflow.
- Rate limit handling absent, causing silent failures.
- Video format/size assumptions tied to TikTok's specific constraints.
