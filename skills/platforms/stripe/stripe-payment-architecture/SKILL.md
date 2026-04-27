---
name: stripe-payment-architecture
description: Use when reviewing or designing Stripe payment integration, including Checkout, Payment Intents, webhooks, subscriptions, Connect platform, and Stripe API constraints.
---

# Stripe Payment Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify payment scenarios: Checkout Sessions, Payment Intents, Setup Intents, subscriptions, invoices, Connect platform accounts, and refund/dispute handling.
2. Map Stripe API contracts: idempotency keys, webhook event types, payment method types, customer objects, price/plan models, and Connect account tiers.
3. Check whether payment logic, webhook handling, subscription management, or customer data are mixed with domain order/subscription logic.
4. Review security: webhook signature verification, idempotency key usage, PCI compliance scope, Connect platform risk, and API key management.
5. Recommend payment service, webhook handler, subscription manager, and Connect adapter boundaries.
6. Verify with Stripe test mode, webhook forwarding, idempotency retry scenarios, and Connect account onboarding flows.

## Output Format

```markdown
Stripe payment architecture:
- Payment scenarios:
- API coupling:
- Security concerns:
- Proposed boundaries:
- Verification:
```
