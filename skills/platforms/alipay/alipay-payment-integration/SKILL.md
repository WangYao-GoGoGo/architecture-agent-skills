---
name: alipay-payment-integration
description: Use when reviewing or designing Alipay payment integration, including app payment, web payment, QR code payment, refunds, notifications, signature verification, and Alipay SDK lifecycle.
---

# Alipay Payment Integration

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/api/`
- `knowledge/platform/`

## Workflow

1. Identify payment scenarios: app payment, web payment, QR code, mini program payment, recurring/subscription, refunds, and settlement.
2. Map Alipay SDK contracts: order creation, signing, notification handling, refund API, query API, and certificate management.
3. Check whether payment logic, signature generation, notification parsing, or refund workflows are mixed with domain order logic.
4. Review security: certificate rotation, signature verification, notification idempotency, timeout handling, and merchant key storage.
5. Recommend payment adapter, order-payment mapping, notification handler, and refund service boundaries.
6. Verify with Alipay sandbox, duplicate notification scenarios, timeout and retry, and refund idempotency tests.

## Output Format

```markdown
Alipay payment integration:
- Payment scenarios:
- SDK coupling:
- Security concerns:
- Proposed boundaries:
- Verification:
```
