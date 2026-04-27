# Twitter/X Platform Knowledge

## Use When

Reviewing or designing Twitter/X platform integration, API v2, or social media publishing architecture.

## Heuristics

- Treat Twitter API v2 endpoints, OAuth 2.0 flows, rate limits, and content policies as platform contracts.
- Keep publishing logic, media handling, user data processing, and analytics collection separate from domain workflow logic.
- Design for rate limits, OAuth token refresh, API versioning, and content moderation policies.
- Separate API client adapters from domain content and analytics models.

## Common Risks

- Publishing logic mixed with domain content workflow.
- Rate limit handling absent, causing silent failures.
- OAuth 2.0 PKCE flow not correctly implemented.
