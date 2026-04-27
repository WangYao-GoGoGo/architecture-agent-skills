# Communication Platform Ecosystem Knowledge

Communication platforms include chat, bot, messaging, collaboration, customer-service, notification, and social platforms where the platform owns events, identity, permissions, rate limits, and message delivery.

Examples include Slack, Discord, Telegram, Feishu, DingTalk, LINE, WhatsApp Business, enterprise chat platforms, and webhook-driven bot platforms.

## Platform-Specific Cards

- `alipay-mini-program.md`: Alipay mini program page/component/service structure.
- `alipay-payment.md`: Alipay payment integration, notification, refund, and reconciliation.
- `line-bot.md`: LINE bot webhook, messaging API, and bot architecture.
- `facebook-platform.md`: Facebook/Meta Graph API, webhook, and platform architecture.
- `slack-app.md`: Slack app commands, events, modals, and Block Kit architecture.
- `discord-bot.md`: Discord bot interactions, gateway, and command architecture.
- `telegram-bot.md`: Telegram bot updates, commands, and inline mode architecture.
- `feishu-app.md`: Feishu/Lark app events, cards, and API architecture.
- `dingtalk-app.md`: DingTalk app robot, events, and enterprise architecture.
- `whatsapp-business.md`: WhatsApp Business API, message templates, and messaging architecture.

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
