---
name: line-bot-architecture
description: Use when reviewing or designing LINE bot and Messaging API architecture, including webhook events, reply/push messages, rich menus, LIFF apps, login, and LINE platform constraints.
---

# LINE Bot Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify bot scenarios: webhook event handling, reply messages, push messages, rich menus, LIFF (LINE Front-end Framework) apps, LINE Login, and account linking.
2. Map LINE platform contracts: webhook signature verification, event types (message, follow, join, postback, beacon), reply token lifecycle, rate limits, and message types.
3. Check whether conversation logic, reply/push decisions, user ID handling, or rich menu configuration are mixed with domain workflow.
4. Review platform constraints: webhook retry behavior, rate limits, message size limits, LIFF app permissions, and channel access token management.
5. Recommend webhook handler, conversation router, message formatter, and LIFF app boundaries.
6. Verify with LINE bot simulator, duplicate webhook events, rate limit scenarios, and token refresh flows.

## Output Format

```markdown
LINE bot architecture:
- Bot scenarios:
- Platform coupling:
- Proposed boundaries:
- Security/rate-limit concerns:
- Verification:
```
