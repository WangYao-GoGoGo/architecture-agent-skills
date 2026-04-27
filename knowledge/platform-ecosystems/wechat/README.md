# WeChat Platform Knowledge

WeChat development is a platform ecosystem, not only a frontend framework. Architecture decisions depend on the WeChat runtime, account type, review rules, open APIs, authorization flow, message callbacks, payment contracts, cloud functions, and client version constraints.

- `mini-program.md`: mini program page/component/service structure.
- `official-account.md`: official account message, menu, OAuth, and event callback architecture.
- `wechat-pay.md`: payment, refund, notification, idempotency, and reconciliation boundaries.

## Review Focus

- Separate page/component UI, state, platform API adapters, backend APIs, and domain logic.
- Keep app secrets, payment signing, access tokens, and sensitive integration logic on trusted backend services.
- Treat platform callbacks and notifications as external API contracts with signature verification, replay protection, and idempotency.
- Design around WeChat runtime limits, package size, review constraints, API permissions, and version compatibility.
