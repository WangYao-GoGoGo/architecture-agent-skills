# YouTube Platform Knowledge

## Use When

Reviewing or designing YouTube platform integration, Data API v3, or video publishing architecture.

## Heuristics

- Treat YouTube Data API v3 endpoints, OAuth 2.0 flows, rate limits, and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.

## Common Risks

- Publishing logic mixed with domain content workflow.
- Rate limit handling absent, causing silent failures.
- Video format/size assumptions tied to YouTube's specific constraints.
