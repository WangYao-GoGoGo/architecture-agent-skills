---
name: instagram-platform-architecture
description: Use when reviewing or designing Instagram platform integration, including Instagram Graph API, Basic Display API, media publishing, webhooks, and Instagram platform constraints.
---

# Instagram Platform Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: Instagram Graph API, Basic Display API, media publishing (images, video, carousel, stories), comment management, webhook events, and insights/analytics.
2. Map Instagram platform contracts: Graph API endpoint structure, OAuth token lifecycle, media container creation/publishing flow, webhook event types, and rate limits.
3. Check whether publishing logic, media handling, comment processing, or analytics collection are mixed with domain workflow logic.
4. Review platform constraints: rate limits, OAuth token refresh, media format/size limits, content policy, app review requirements, and Instagram Business/Facebook Page linking.
5. Recommend API client, media publisher, webhook handler, and analytics collector boundaries.
6. Verify with Instagram test users, Graph API Explorer, webhook testing, and rate limit scenarios.

## Output Format

```markdown
Instagram platform architecture:
- Integration scenarios:
- API coupling:
- Rate-limit/review concerns:
- Proposed boundaries:
- Verification:
```
