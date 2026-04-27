---
name: tiktok-platform-architecture
description: Use when reviewing or designing TikTok platform integration, including TikTok API, OAuth, video upload, user data access, webhooks, and TikTok platform constraints.
---

# TikTok Platform Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: TikTok API endpoints, OAuth 2.0 flow, video upload/posting, user profile/data access, webhook events, and analytics data retrieval.
2. Map TikTok platform contracts: API endpoint structure, OAuth token lifecycle, video upload format and size limits, webhook event types, and rate limits.
3. Check whether posting logic, video handling, user data processing, or analytics collection are mixed with domain workflow logic.
4. Review platform constraints: rate limits, OAuth token refresh, video size/duration limits, content moderation policies, and app review requirements.
5. Recommend API client, video upload service, webhook handler, and analytics collector boundaries.
6. Verify with TikTok developer sandbox, OAuth flow testing, webhook event simulation, and rate limit scenarios.

## Output Format

```markdown
TikTok platform architecture:
- Integration scenarios:
- API coupling:
- Rate-limit/moderation concerns:
- Proposed boundaries:
- Verification:
```
