---
name: twitter-platform-architecture
description: Use when reviewing or designing Twitter/X platform integration, including Twitter API v2, OAuth 2.0, tweet posting, media upload, webhooks, and Twitter platform rate limits.
---

# Twitter/X Platform Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: Twitter API v2 endpoints, OAuth 2.0 (PKCE) flow, tweet posting/retrieval, media upload, DM handling, webhook/account activity API, and search/timeline queries.
2. Map Twitter platform contracts: API v2 endpoint structure, OAuth 2.0 token lifecycle, media upload chunked format, webhook CRC (Challenge-Response Check), and rate limit tiers.
3. Check whether posting logic, media handling, timeline processing, or user mapping are mixed with domain workflow logic.
4. Review platform constraints: rate limits (per-endpoint, per-user), OAuth token refresh, media size limits, webhook retry behavior, and API versioning (v1.1 vs v2 migration).
5. Recommend API client, media uploader, webhook handler, and rate-limit-aware scheduler boundaries.
6. Verify with Twitter developer portal test endpoints, OAuth flow testing, webhook CRC validation, and rate limit simulation.

## Output Format

```markdown
Twitter/X platform architecture:
- Integration scenarios:
- API coupling:
- Rate-limit concerns:
- Proposed boundaries:
- Verification:
```
