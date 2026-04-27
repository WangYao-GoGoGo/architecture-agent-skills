# Stripe Platform Knowledge

## Use When

Reviewing or designing Stripe payment integration, checkout, or webhook architecture.

## Heuristics

- Keep payment intent creation, checkout session handling, webhook processing, refund, and reconciliation as separate responsibilities.
- Treat Stripe webhook events as eventually consistent external events with idempotency keys.
- Verify webhook signatures and make notification handlers idempotent.
- Keep Stripe SDK types and API details at the integration edge.

## Common Risks

- Marking orders paid from client-side success callbacks without server-side verification.
- Webhook handlers that repeat side effects on retry delivery.
- Missing idempotency keys for critical API calls.
