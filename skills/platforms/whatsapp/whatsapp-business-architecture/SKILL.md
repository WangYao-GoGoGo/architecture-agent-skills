---
name: whatsapp-business-architecture
description: Use when reviewing or designing WhatsApp Business API integration, including message templates, webhook events, media handling, business profile, and WhatsApp Cloud API constraints.
---

# WhatsApp Business API Architecture

## Knowledge To Use

- `knowledge/platform/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify integration scenarios: message templates (pre-approved), session messages, webhook event handling, media upload/download, business profile management, and phone number management.
2. Map WhatsApp Cloud API contracts: webhook verification, message types (text, template, media, interactive, location), rate limits, quality rating, and phone number registration.
3. Check whether message routing, template management, media handling, or user opt-in/opt-out logic are mixed with domain workflow.
4. Review platform constraints: template approval process, 24-hour session window, rate limits, quality rating penalties, and business verification requirements.
5. Recommend webhook handler, message router, template manager, and media service boundaries.
6. Verify with WhatsApp Cloud API test senders, webhook testing, template rejection scenarios, and rate limit simulation.

## Output Format

```markdown
WhatsApp Business API architecture:
- Integration scenarios:
- Platform coupling:
- Proposed boundaries:
- Template/session concerns:
- Verification:
```
