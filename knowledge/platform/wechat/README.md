# WeChat Platform Knowledge

## Use When

Reviewing or designing WeChat mini program, official account, or WeChat Pay integration.

## Heuristics

- Keep `wx.*` platform API calls behind adapters for testability and portability.
- Treat login, session refresh, permissions, and subscription messages as architecture concerns.
- Separate payment creation, notification handling, refund, and reconciliation.
- Verify notification signatures and make handlers idempotent.
- Design for WeChat's review process, package size limits, and subpackage loading.

## Common Risks

- Page files owning UI, state, network requests, and business policy together.
- Payment notifications causing repeated side effects.
- Platform API calls scattered across components.

## Detailed Topics

- [`mini-program.md`](mini-program.md): Mini program page/component/service structure.
- [`official-account.md`](official-account.md): Official account message, menu, OAuth, and event callback architecture.
- [`wechat-pay.md`](wechat-pay.md): Payment, refund, notification, idempotency, and reconciliation boundaries.
