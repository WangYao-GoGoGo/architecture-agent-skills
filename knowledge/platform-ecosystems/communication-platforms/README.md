# Communication Platform Ecosystem Knowledge

Communication platforms include chat, bot, messaging, collaboration, customer-service, notification, and social platforms where the platform owns events, identity, permissions, rate limits, and message delivery.

Examples include Slack, Discord, Telegram, Feishu, DingTalk, LINE, WhatsApp Business, enterprise chat platforms, and webhook-driven bot platforms.

## Heuristics

- Treat inbound events, commands, interactive callbacks, webhooks, outbound messages, and platform rate limits as API contracts.
- Keep signature verification, deduplication, permission checks, retries, and token refresh at the integration edge.
- Separate conversation routing, domain workflow, message formatting, and delivery.
- Design for duplicate events, delayed delivery, platform outages, and permission changes.

## Common Risks

- Bot handlers containing full business workflows.
- Message format and platform user IDs leaking into domain code.
- Retry behavior causing repeated side effects.
- No clear separation between platform permissions and application authorization.
