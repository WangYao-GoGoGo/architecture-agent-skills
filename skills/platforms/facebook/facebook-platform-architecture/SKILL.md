---
name: facebook-platform-architecture
description: Use when reviewing or designing Facebook/Meta platform integration, including Facebook Login, Graph API, Messenger bot, webhooks, sharing, ads, and Instagram Basic Display API.
---

# Facebook/Meta Platform Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: Facebook Login, Graph API queries, Messenger bot webhooks, page subscriptions, sharing, ads management, and Instagram Basic Display API.
2. Map Meta platform contracts: OAuth flow, access token lifecycle, webhook verification, Graph API pagination, rate limits, and app review requirements.
3. Check whether login logic, token management, Graph API calls, or webhook event handling are mixed with domain user/profile logic.
4. Review platform constraints: app review, permission scopes, token expiration, webhook retry behavior, rate limits, and API versioning.
5. Recommend authentication adapter, Graph API client, webhook handler, and token refresh boundaries.
6. Verify with Meta app dashboard, webhook tester, sandbox users, and token expiration scenarios.

## Output Format

```markdown
Facebook/Meta platform architecture:
- Integration scenarios:
- Platform coupling:
- Proposed boundaries:
- App review/permission concerns:
- Verification:
```
