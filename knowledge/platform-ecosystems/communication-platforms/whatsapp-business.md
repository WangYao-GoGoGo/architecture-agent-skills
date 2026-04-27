# WhatsApp Business API Architecture

## Heuristics

- Treat webhook events, message templates, media messages, and business profile API calls as platform contracts.
- Keep webhook verification, signature validation, rate limit handling, and token management at the integration edge.
- Separate message routing, domain workflow, message formatting, and delivery.
- Design for WhatsApp's specific message template approval process, opt-in/opt-out requirements, and 24-hour messaging window.
- Use WhatsApp Business API SDKs behind adapters for testability.

## Common Risks

- Webhook handlers containing full business workflows.
- Message template approval not accounted for in workflow design.
- Opt-in/opt-out state not tracked, causing policy violations.
- Ignoring WhatsApp's 24-hour customer service messaging window.
- Media message handling not designed for asynchronous download.

## Verification

- Webhook handlers are idempotent.
- Message template lifecycle and approval process are visible.
- Domain workflows can be tested without real WhatsApp API calls.
