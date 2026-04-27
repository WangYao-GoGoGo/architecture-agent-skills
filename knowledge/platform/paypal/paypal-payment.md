# PayPal Payment Architecture

## Heuristics

- Keep order creation, payment capture, webhook notification processing, refund, and reconciliation as separate responsibilities.
- Treat PayPal webhook events as eventually consistent external events.
- Verify webhook signatures and make notification handlers idempotent.
- Keep PayPal SDK types and API details at the integration edge.
- Reconcile internal order state against PayPal's order or capture state.
- Design for PayPal's specific webhook event types (CHECKOUT.ORDER.APPROVED, PAYMENT.CAPTURE.COMPLETED, etc.) and retry behavior.

## Common Risks

- Marking orders paid from client-side success callbacks without server-side capture verification.
- Webhook handlers that repeat side effects on retry delivery.
- Refund and reconciliation logic bolted onto checkout code.
- PayPal API models leaking into core order domain code.
- Missing idempotency keys for critical API calls.

## Verification

- Duplicate webhook events do not double-apply business effects.
- Order state transitions are explicit and auditable.
- Failure paths for order creation, capture, webhook, refund, and reconciliation are covered.
