# Alipay Payment Integration Architecture

## Heuristics

- Keep order creation, payment request signing, notification handling, refund, reconciliation, and ledger updates as separate responsibilities.
- Treat payment notifications as eventually consistent external events.
- Verify signatures and make notification handlers idempotent.
- Keep payment SDK types and cryptographic details at the integration edge.
- Reconcile internal order state against Alipay's transaction state.
- Design for Alipay's specific notification retry behavior and timeout windows.

## Common Risks

- Marking orders paid from client-side success callbacks.
- Payment notification handlers that repeat side effects.
- Refund and reconciliation logic bolted onto checkout code.
- Payment provider models leaking into core order domain code.

## Verification

- Duplicate notifications do not double-apply business effects.
- Order state transitions are explicit and auditable.
- Failure paths for signing, notification, refund, and reconciliation are covered.
