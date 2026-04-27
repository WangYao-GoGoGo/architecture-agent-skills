# Alipay Platform Knowledge

## Use When

Reviewing or designing Alipay mini program architecture or Alipay payment integration.

## Heuristics

- Keep `my.*` platform API calls behind adapters for testability and portability.
- Treat login, session refresh, permissions, and subscription messages as architecture concerns.
- Separate payment creation, notification handling, refund, and reconciliation.
- Verify notification signatures and make handlers idempotent.
- Design for Alipay's review process, package size limits, and subpackage loading.

## Common Risks

- Page files owning UI, state, network requests, and business policy together.
- Payment notifications causing repeated side effects.
- Platform API calls scattered across components.
