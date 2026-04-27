# WhatsApp Business Platform Knowledge

## Use When

Reviewing or designing WhatsApp Business API integration, message templates, or messaging architecture.

## Heuristics

- Treat webhook events, message templates, media messages, and business profile API calls as platform contracts.
- Keep webhook verification, signature validation, and rate limit handling at the integration edge.
- Separate message routing, domain workflow, message formatting, and delivery.
- Design for WhatsApp's specific message template approval process and 24-hour messaging window.

## Common Risks

- Webhook handlers containing full business workflows.
- Message template approval not accounted for in workflow design.
- Opt-in/opt-out state not tracked, causing policy violations.
