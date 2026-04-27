# Payment Platform Ecosystem Knowledge

Payment platforms include online payment gateways, merchant APIs, subscription billing, refunds, dispute handling, and settlement where the platform owns transaction processing, compliance scope, and notification delivery.

Examples include Alipay Pay, WeChat Pay, Stripe, and PayPal.

## Heuristics

- Treat payment creation, notification handling, refunds, disputes, and settlement as platform contracts.
- Keep payment logic, order-payment mapping, notification processing, and refund workflows separate from domain order logic.
- Design for idempotency, duplicate notifications, timeout, partial refunds, and platform outages.
- Separate payment adapter, notification handler, and refund service from domain order management.

## Common Risks

- Payment notification handling mixed with order status updates, causing idempotency issues.
- Signature verification or webhook authentication missing, allowing forged notifications.
- Refund logic tightly coupled to one payment provider's API.
- PCI compliance scope not properly isolated.
- Settlement and reconciliation logic absent or ad-hoc.
