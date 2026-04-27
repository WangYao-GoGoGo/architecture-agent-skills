---
name: youtube-platform-architecture
description: Use when reviewing or designing YouTube platform integration, including YouTube Data API, OAuth 2.0, video upload, live streaming, webhooks, and YouTube platform constraints.
---

# YouTube Platform Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: YouTube Data API v3, OAuth 2.0 flow, video upload, playlist management, live streaming (LiveBroadcast, LiveChat), comments, captions, and webhook/push notifications.
2. Map YouTube platform contracts: API endpoint structure, OAuth scope model, video upload resumable protocol, live stream lifecycle, PubSubHubbub webhook format, and quota limits.
3. Check whether upload logic, playlist management, live stream handling, or comment processing are mixed with domain workflow logic.
4. Review platform constraints: daily quota limits, OAuth scope restrictions, video processing time, content ID/copyright policies, and API versioning.
5. Recommend API client, video upload service, live stream manager, and notification handler boundaries.
6. Verify with YouTube test accounts, OAuth playground, quota estimation, and webhook notification testing.

## Output Format

```markdown
YouTube platform architecture:
- Integration scenarios:
- API coupling:
- Quota/content concerns:
- Proposed boundaries:
- Verification:
```
