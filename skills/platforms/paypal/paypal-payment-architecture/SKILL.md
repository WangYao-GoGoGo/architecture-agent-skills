---
name: paypal-payment-architecture
description: Use when reviewing or designing PayPal payment integration, including PayPal Checkout, Vault, webhooks, subscriptions, Payouts, and PayPal API constraints.
---

# PayPal Payment Architecture

## Knowledge To Use

- `knowledge/platform-ecosystems/communication-platforms/`
- `knowledge/languages/javascript/`
- `knowledge/languages/python/`
- `knowledge/api/`

## Workflow

1. Identify payment scenarios: PayPal Checkout (Orders API), Vault (saved payment methods), subscriptions, Payouts, dispute handling, and identity (Log In with PayPal).
2. Map PayPal API contracts: Orders API flow, webhook event types, OAuth2 token lifecycle, subscription/billing plan models, and Payouts batch format.
3. Check whether payment logic, webhook handling, subscription management, or payer data are mixed with domain order/subscription logic.
4. Review security: webhook signature verification, OAuth2 token refresh, PCI compliance scope, fraud protection, and API credential management.
5. Recommend payment service, webhook handler, subscription manager, and payout service boundaries.
6. Verify with PayPal sandbox, webhook simulation, IPN vs webhook migration scenarios, and dispute lifecycle testing.

## Output Format

```markdown
PayPal payment architecture:
- Payment scenarios:
- API coupling:
- Security concerns:
- Proposed boundaries:
- Verification:
```
