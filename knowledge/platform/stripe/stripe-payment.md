# Stripe Payment Architecture

## Heuristics

- Keep payment intent creation, checkout session handling, webhook notification processing, refund, and reconciliation as separate responsibilities.
- Treat Stripe webhook events as eventually consistent external events with idempotency keys.
- Verify webhook signatures and make notification handlers idempotent.
- Keep Stripe SDK types and API details at the integration edge.
- Reconcile internal order state against Stripe's payment intent or charge state.
- Design for Stripe's specific event types (payment_intent.succeeded, charge.refunded, etc.) and retry behavior.

## Common Risks

- Marking orders paid from client-side success callbacks without server-side verification.
- Webhook handlers that repeat side effects on retry delivery.
- Refund and reconciliation logic bolted onto checkout code.
- Stripe API models leaking into core order domain code.
- Missing idempotency keys for critical API calls.

## Verification

- Duplicate webhook events do not double-apply business effects.
- Order state transitions are explicit and auditable.
- Failure paths for payment intent, webhook, refund, and reconciliation are covered.
