# PayPal Platform Knowledge

## Use When

Reviewing or designing PayPal payment integration, orders, or webhook architecture.

## Heuristics

- Keep order creation, payment capture, webhook processing, refund, and reconciliation as separate responsibilities.
- Treat PayPal webhook events as eventually consistent external events.
- Verify webhook signatures and make notification handlers idempotent.
- Keep PayPal SDK types and API details at the integration edge.

## Common Risks

- Marking orders paid from client-side success callbacks without server-side capture verification.
- Webhook handlers that repeat side effects on retry delivery.
- Missing idempotency keys for critical API calls.
