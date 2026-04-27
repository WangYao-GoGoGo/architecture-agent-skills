---
name: dingtalk-app-architecture
description: Use when reviewing or designing DingTalk app architecture, including bot commands, event callbacks, interactive cards, mini programs, OAuth login, and DingTalk platform constraints.
---

# DingTalk App Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/java/`
- `knowledge/api/`

## Workflow

1. Identify app scenarios: bot commands, event callbacks (message, member, attendance, approval), interactive cards, mini programs, DingTalk Login, and E应用/EApp integration.
2. Map DingTalk platform contracts: event types, callback URLs, card interaction payloads, message types, OAuth flow, token lifecycle, and rate limits.
3. Check whether event handling, card building, message formatting, or user/org mapping are mixed with domain workflow logic.
4. Review platform constraints: callback retry behavior, token refresh, rate limits, app review requirements, and enterprise data isolation.
5. Recommend event handler, card builder, message formatter, and authentication adapter boundaries.
6. Verify with DingTalk developer sandbox, event replay scenarios, card interaction testing, and permission scope validation.

## Output Format

```markdown
DingTalk app architecture:
- App scenarios:
- Platform coupling:
- Proposed boundaries:
- Enterprise data concerns:
- Verification:
```
